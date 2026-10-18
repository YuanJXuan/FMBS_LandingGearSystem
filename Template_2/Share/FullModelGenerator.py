# -*- coding: utf-8 -*-
"""Generate one combined landing-gear ADM from a validated full-model base."""

from __future__ import print_function

import json
import math
import os
import re
import tempfile


CONFIG_FILE_NAME = "full_model_config.json"
_RECORD_RE = re.compile(r"^\s*([A-Z_]+)/([0-9]+)\s*$")
_VIEW_NAME_RE = re.compile(r"adams_view_name='([^']+)'", re.IGNORECASE)


class FullModelGenerationError(ValueError):
    """Raised when the full-model package or generated ADM is invalid."""


def _absolute_path(base_dir, value):
    value = str(value or "").strip()
    if not value:
        return ""
    if not os.path.isabs(value):
        value = os.path.join(base_dir, value)
    return os.path.abspath(value)


def _finite_triplet(value, description):
    try:
        result = tuple(float(value[index]) for index in range(3))
    except Exception:
        raise FullModelGenerationError("{}必须包含X、Y、Z三个数值".format(description))
    if not all(math.isfinite(number) for number in result):
        raise FullModelGenerationError("{}不能包含NaN或无穷大".format(description))
    return result


def _safe_model_name(value):
    value = re.sub(r"[^A-Za-z0-9_]", "_", str(value or "").strip())
    value = value.strip("_")
    if not value:
        raise FullModelGenerationError("输出模型名称不能为空")
    if value[0].isdigit():
        value = "model_" + value
    return value[:80]


def _path_key(value):
    return os.path.normcase(os.path.realpath(os.path.abspath(str(value or ""))))


def _path_is_within(path, directory):
    try:
        return os.path.commonpath(
            [os.path.abspath(path), os.path.abspath(directory)]
        ) == os.path.abspath(directory)
    except Exception:
        return False


def _normalize_configuration(model_full_dir, config_path, config):
    """Validate one configured NLG/MLG assembly combination."""
    if not isinstance(config, dict):
        raise FullModelGenerationError("完整模型组合配置必须是JSON对象")

    model_full_dir = os.path.abspath(str(model_full_dir or ""))
    base_adm = _absolute_path(model_full_dir, config.get("base_adm"))
    if not os.path.isfile(base_adm):
        raise FullModelGenerationError("未找到完整模型母版：{}".format(base_adm))
    if os.path.splitext(base_adm)[1].lower() != ".adm":
        raise FullModelGenerationError("完整模型母版必须是ADM文件")

    resource_dir = _absolute_path(
        model_full_dir,
        config.get("resource_dir") or os.path.dirname(base_adm),
    )
    if not os.path.isdir(resource_dir):
        raise FullModelGenerationError("完整模型资源目录不存在：{}".format(resource_dir))

    assemblies = config.get("assemblies")
    if not isinstance(assemblies, dict):
        raise FullModelGenerationError("完整模型配置缺少assemblies")
    normalized = {}
    for key in ("nlg", "mlg"):
        assembly = assemblies.get(key)
        if not isinstance(assembly, dict):
            raise FullModelGenerationError("完整模型配置缺少{}定义".format(key))
        source_adm = _absolute_path(model_full_dir, assembly.get("source_adm"))
        if not os.path.isfile(source_adm):
            raise FullModelGenerationError("未找到{}来源模型：{}".format(key, source_adm))
        if os.path.splitext(source_adm)[1].lower() != ".adm":
            raise FullModelGenerationError("{}来源模型必须是ADM文件".format(key))
        if not _path_is_within(source_adm, model_full_dir):
            raise FullModelGenerationError(
                "{}来源模型必须位于Model_Full目录中：{}".format(key, source_adm)
            )
        try:
            anchor_marker_id = int(assembly.get("anchor_marker_id"))
        except Exception:
            raise FullModelGenerationError("{}的anchor_marker_id无效".format(key))
        part_names = [
            str(name).strip()
            for name in assembly.get("part_names", [])
            if str(name).strip()
        ]
        if not part_names:
            raise FullModelGenerationError("{}没有配置需要整体移动的Part".format(key))
        normalized[key] = dict(assembly)
        normalized[key]["source_adm"] = source_adm
        normalized[key]["anchor_marker_id"] = anchor_marker_id
        normalized[key]["part_names"] = part_names

    marker_followers = []
    for entry in config.get("marker_followers", []):
        if not isinstance(entry, dict):
            raise FullModelGenerationError("marker_followers项目必须是JSON对象")
        try:
            marker_id = int(entry.get("marker_id"))
        except Exception:
            raise FullModelGenerationError("marker_followers中的marker_id无效")
        follows = str(entry.get("follows") or "").strip().lower()
        if follows not in normalized:
            raise FullModelGenerationError(
                "Marker/{}的follows必须是nlg或mlg".format(marker_id)
            )
        normalized_follower = dict(entry)
        normalized_follower["marker_id"] = marker_id
        normalized_follower["follows"] = follows
        marker_followers.append(normalized_follower)

    joint_checks = []
    for value in config.get("joint_checks", []):
        try:
            joint_checks.append(int(value))
        except Exception:
            raise FullModelGenerationError("joint_checks包含无效编号：{}".format(value))

    result = dict(config)
    result["config_path"] = config_path
    result["model_full_dir"] = model_full_dir
    result["base_adm"] = base_adm
    result["resource_dir"] = resource_dir
    result["assemblies"] = normalized
    result["marker_followers"] = marker_followers
    result["joint_checks"] = joint_checks
    result["output_model_name"] = _safe_model_name(
        result.get("output_model_name") or "template_full_generated"
    )
    result["combination_name"] = str(
        result.get("combination_name")
        or result.get("name")
        or "{} + {}".format(
            os.path.basename(normalized["nlg"]["source_adm"]),
            os.path.basename(normalized["mlg"]["source_adm"]),
        )
    ).strip()
    return result


def load_configurations(model_full_dir):
    """Load every configured compatible NLG/MLG combination.

    Older single-combination JSON files remain supported.  New packages may
    place shared defaults at the root and add a ``combinations`` list whose
    entries override those defaults.
    """
    model_full_dir = os.path.abspath(str(model_full_dir or ""))
    config_path = os.path.join(model_full_dir, CONFIG_FILE_NAME)
    if not os.path.isfile(config_path):
        raise FullModelGenerationError("未找到完整模型配置：{}".format(config_path))
    try:
        with open(config_path, "r", encoding="utf-8-sig") as stream:
            root_config = json.load(stream)
    except Exception as exc:
        raise FullModelGenerationError("完整模型配置读取失败：{}".format(exc))
    if not isinstance(root_config, dict):
        raise FullModelGenerationError("完整模型配置根节点必须是JSON对象")

    entries = root_config.get("combinations")
    if entries is None:
        entries = [root_config]
    elif not isinstance(entries, list) or not entries:
        raise FullModelGenerationError("combinations必须是非空JSON数组")

    shared = dict(root_config)
    shared.pop("combinations", None)
    configurations = []
    seen_pairs = set()
    for index, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            raise FullModelGenerationError(
                "combinations第{}项必须是JSON对象".format(index)
            )
        merged = dict(shared)
        merged.update(entry)
        normalized = _normalize_configuration(model_full_dir, config_path, merged)
        pair = (
            _path_key(normalized["assemblies"]["nlg"]["source_adm"]),
            _path_key(normalized["assemblies"]["mlg"]["source_adm"]),
        )
        if pair in seen_pairs:
            raise FullModelGenerationError(
                "完整模型配置中存在重复的前起/主起组合：{}".format(
                    normalized["combination_name"]
                )
            )
        seen_pairs.add(pair)
        configurations.append(normalized)
    return configurations


def load_configuration(model_full_dir, nlg_adm_path=None, mlg_adm_path=None):
    """Resolve the configuration for the selected NLG and MLG ADM files."""
    configurations = load_configurations(model_full_dir)
    if not nlg_adm_path and not mlg_adm_path:
        return configurations[0]

    requested_nlg = _path_key(nlg_adm_path) if nlg_adm_path else None
    requested_mlg = _path_key(mlg_adm_path) if mlg_adm_path else None
    matches = []
    for configuration in configurations:
        configured_nlg = _path_key(
            configuration["assemblies"]["nlg"]["source_adm"]
        )
        configured_mlg = _path_key(
            configuration["assemblies"]["mlg"]["source_adm"]
        )
        if requested_nlg and requested_nlg != configured_nlg:
            continue
        if requested_mlg and requested_mlg != configured_mlg:
            continue
        matches.append(configuration)
    if matches:
        return matches[0]

    nlg_name = os.path.basename(str(nlg_adm_path or "未选择"))
    mlg_name = os.path.basename(str(mlg_adm_path or "未选择"))
    raise FullModelGenerationError(
        "所选前起和主起没有可用的完整模型组合配置：{} + {}。"
        "请在{}中增加对应组合。".format(
            nlg_name,
            mlg_name,
            os.path.join(os.path.abspath(str(model_full_dir or "")), CONFIG_FILE_NAME),
        )
    )


def list_adm_files(model_full_dir):
    """Return selectable ADM files directly below Model_Full."""
    model_full_dir = os.path.abspath(str(model_full_dir or ""))
    if not os.path.isdir(model_full_dir):
        return []
    return sorted(
        [
            os.path.join(model_full_dir, name)
            for name in os.listdir(model_full_dir)
            if os.path.isfile(os.path.join(model_full_dir, name))
            and os.path.splitext(name)[1].lower() == ".adm"
        ],
        key=lambda path: os.path.basename(path).lower(),
    )


def _decode_adm(path):
    with open(path, "rb") as stream:
        payload = stream.read()
    for encoding in ("utf-8-sig", "gb18030", "latin-1"):
        try:
            return payload.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    raise FullModelGenerationError("ADM文件编码无法识别：{}".format(path))


def _records(lines):
    records = []
    pending_name = ""
    for index, line in enumerate(lines):
        name_match = _VIEW_NAME_RE.search(line)
        if name_match:
            pending_name = name_match.group(1).strip()
        record_match = _RECORD_RE.match(line.rstrip("\r\n"))
        if not record_match:
            continue
        if records:
            records[-1]["end"] = index
        records.append(
            {
                "type": record_match.group(1),
                "id": int(record_match.group(2)),
                "name": pending_name,
                "start": index,
                "end": len(lines),
            }
        )
        pending_name = ""
    return records


def _record_line(lines, record, property_name):
    pattern = re.compile(
        r"^\s*,\s*{}\s*=".format(re.escape(property_name)),
        re.IGNORECASE,
    )
    for index in range(record["start"] + 1, record["end"]):
        if pattern.match(lines[index]):
            return index
    return None


def _parse_triplet_line(line, property_name):
    pattern = re.compile(
        r"^(\s*,\s*{}\s*=\s*)([^!\r\n]+?)(\s*)(\r?\n)?$".format(
            re.escape(property_name)
        ),
        re.IGNORECASE,
    )
    match = pattern.match(line)
    if not match:
        raise FullModelGenerationError("无法解析ADM坐标：{}".format(line.strip()))
    tokens = [token.strip() for token in match.group(2).split(",")]
    if len(tokens) != 3:
        raise FullModelGenerationError("ADM坐标不是三维坐标：{}".format(line.strip()))
    try:
        values = tuple(float(token.replace("D", "E").replace("d", "e")) for token in tokens)
    except ValueError:
        raise FullModelGenerationError("ADM坐标包含非数值内容：{}".format(line.strip()))
    return match, values


def _format_number(value):
    value = 0.0 if abs(float(value)) < 5.0e-13 else float(value)
    return "{:.12g}".format(value)


def _replace_triplet(line, property_name, values):
    match, _old_values = _parse_triplet_line(line, property_name)
    newline = match.group(4) or ""
    return "{}{}, {}, {}{}{}".format(
        match.group(1),
        _format_number(values[0]),
        _format_number(values[1]),
        _format_number(values[2]),
        match.group(3),
        newline,
    )


def _read_int_property(lines, record, property_name):
    line_index = _record_line(lines, record, property_name)
    if line_index is None:
        return None
    match = re.match(
        r"^\s*,\s*{}\s*=\s*([0-9]+)".format(re.escape(property_name)),
        lines[line_index],
        re.IGNORECASE,
    )
    return int(match.group(1)) if match else None


def _adm_inventory(lines):
    records = _records(lines)
    parts = {}
    markers = {}
    for record in records:
        if record["type"] == "PART":
            parts[record["id"]] = record
        elif record["type"] == "MARKER":
            marker = dict(record)
            marker["part_id"] = _read_int_property(lines, record, "PART")
            qp_index = _record_line(lines, record, "QP")
            marker["qp_index"] = qp_index
            marker["qp"] = (
                _parse_triplet_line(lines[qp_index], "QP")[1]
                if qp_index is not None
                else None
            )
            markers[record["id"]] = marker
    return records, parts, markers


def _part_origin(lines, part):
    qg_index = _record_line(lines, part, "QG")
    if qg_index is None:
        return (0.0, 0.0, 0.0)
    return _parse_triplet_line(lines[qg_index], "QG")[1]


def _require_unrotated_part(lines, part, description):
    reuler_index = _record_line(lines, part, "REULER")
    if reuler_index is None:
        return
    _match, orientation = _parse_triplet_line(lines[reuler_index], "REULER")
    if any(abs(value) > 1.0e-10 for value in orientation):
        raise FullModelGenerationError(
            "{}所属Part带有初始转角，当前仅支持平移：{}".format(
                description,
                orientation,
            )
        )


def _marker_world_position(lines, parts, marker, description="Marker"):
    part = parts.get(marker.get("part_id"))
    if part is None:
        raise FullModelGenerationError(
            "{}引用了不存在的Part/{}".format(description, marker.get("part_id"))
        )
    _require_unrotated_part(lines, part, description)
    origin = _part_origin(lines, part)
    local_position = marker.get("qp") or (0.0, 0.0, 0.0)
    return tuple(left + right for left, right in zip(origin, local_position))


def _joint_records(records):
    return {
        record["id"]: record
        for record in records
        if record["type"] in ("JOINT", "JPRIM")
    }


def _validate_joint_positions(lines, records, parts, markers, joint_ids):
    joints = _joint_records(records)
    errors = []
    for joint_id in joint_ids:
        joint = joints.get(joint_id)
        if joint is None:
            errors.append("Joint/{}不存在".format(joint_id))
            continue
        i_marker_id = _read_int_property(lines, joint, "I")
        j_marker_id = _read_int_property(lines, joint, "J")
        i_marker = markers.get(i_marker_id)
        j_marker = markers.get(j_marker_id)
        if i_marker is None or j_marker is None:
            errors.append(
                "Joint/{}引用的Marker不存在：I={}，J={}".format(
                    joint_id,
                    i_marker_id,
                    j_marker_id,
                )
            )
            continue
        i_world = _marker_world_position(
            lines, parts, i_marker, "Joint/{} I Marker".format(joint_id)
        )
        j_world = _marker_world_position(
            lines, parts, j_marker, "Joint/{} J Marker".format(joint_id)
        )
        if any(abs(left - right) > 1.0e-7 for left, right in zip(i_world, j_world)):
            errors.append(
                "Joint/{}两侧Marker不重合：{} != {}".format(
                    joint_id,
                    i_world,
                    j_world,
                )
            )
    if errors:
        raise FullModelGenerationError("；".join(errors))


def _read_anchor_position(adm_path, marker_id, description):
    text, _encoding = _decode_adm(adm_path)
    lines = text.splitlines(True)
    _records_list, parts, markers = _adm_inventory(lines)
    marker = markers.get(marker_id)
    if marker is None or marker.get("qp") is None:
        raise FullModelGenerationError(
            "{}中找不到{}定位Marker：{}".format(
                os.path.basename(adm_path),
                description,
                marker_id,
            )
        )
    return _marker_world_position(
        lines,
        parts,
        marker,
        "{}定位Marker".format(description),
    )


def read_anchor_positions(model_full_dir, nlg_adm_path=None, mlg_adm_path=None):
    """Return world coordinates read from the selected source ADM files."""
    config = load_configuration(model_full_dir, nlg_adm_path, mlg_adm_path)
    result = {}
    for key, assembly in config["assemblies"].items():
        result[key] = _read_anchor_position(
            assembly["source_adm"],
            assembly["anchor_marker_id"],
            assembly.get("label") or key,
        )
    return result


def default_output_directory():
    """Choose a writable persistent folder below Jasmine's work directory."""
    work_dir = ""
    try:
        import Jusme

        getter = getattr(Jusme, "getWorkDir", None)
        if callable(getter):
            work_dir = str(getter() or "").strip()
    except Exception:
        work_dir = ""
    if work_dir:
        work_dir = os.path.abspath(work_dir)
        if os.path.basename(work_dir).lower() != "fmbs_workdir":
            work_dir = os.path.join(work_dir, "fmbs_workdir")
        return os.path.join(work_dir, "generated_models")
    return os.path.join(tempfile.gettempdir(), "Jusme", "generated_models")


def generate_combined_adm(
    model_full_dir,
    nlg_target,
    mlg_target,
    output_directory=None,
    output_model_name=None,
    nlg_adm_path=None,
    mlg_adm_path=None,
):
    """Create one ADM whose NLG and MLG anchors match the requested points."""
    config = load_configuration(model_full_dir, nlg_adm_path, mlg_adm_path)
    targets = {
        "nlg": _finite_triplet(nlg_target, "前起坐标"),
        "mlg": _finite_triplet(mlg_target, "主起坐标"),
    }
    output_model_name = _safe_model_name(
        output_model_name or config["output_model_name"]
    )

    text, encoding = _decode_adm(config["base_adm"])
    lines = text.splitlines(True)
    records, parts, markers = _adm_inventory(lines)
    if not records:
        raise FullModelGenerationError("完整模型母版中没有可识别的ADM对象")

    part_deltas = {}
    anchor_positions = {}
    deltas = {}
    claimed_parts = {}
    for key, assembly in config["assemblies"].items():
        marker = markers.get(assembly["anchor_marker_id"])
        if marker is None or marker.get("qp") is None:
            raise FullModelGenerationError(
                "完整模型母版中找不到{}定位Marker：{}".format(
                    assembly.get("label") or key,
                    assembly["anchor_marker_id"],
                )
            )
        anchor_world = _marker_world_position(
            lines,
            parts,
            marker,
            "{}定位Marker".format(assembly.get("label") or key),
        )
        anchor_positions[key] = anchor_world
        delta = tuple(target - source for target, source in zip(targets[key], anchor_world))
        deltas[key] = delta

        wanted_names = {name.lower() for name in assembly["part_names"]}
        matched_names = set()
        for part_id, part in parts.items():
            normalized_name = str(part.get("name") or "").strip().lower()
            if normalized_name not in wanted_names:
                continue
            if part_id in claimed_parts and claimed_parts[part_id] != key:
                raise FullModelGenerationError(
                    "Part/{}同时属于前起和主起，配置不安全".format(part_id)
                )
            claimed_parts[part_id] = key
            part_deltas[part_id] = delta
            matched_names.add(normalized_name)
        missing = sorted(wanted_names.difference(matched_names))
        if missing:
            raise FullModelGenerationError(
                "完整模型母版缺少{} Part：{}".format(
                    assembly.get("label") or key,
                    "、".join(missing),
                )
            )

    replacements = {}
    insertions = {}
    newline = "\r\n" if "\r\n" in text else "\n"
    for part_id, delta in part_deltas.items():
        part = parts[part_id]
        qg_index = _record_line(lines, part, "QG")
        if qg_index is None:
            insertions.setdefault(part["start"], []).append(
                ", QG = {}, {}, {}{}".format(
                    _format_number(delta[0]),
                    _format_number(delta[1]),
                    _format_number(delta[2]),
                    newline,
                )
            )
        else:
            _match, old_qg = _parse_triplet_line(lines[qg_index], "QG")
            replacements[qg_index] = _replace_triplet(
                lines[qg_index],
                "QG",
                tuple(value + change for value, change in zip(old_qg, delta)),
            )

    # Most Marker QP values are local to their Part and must remain unchanged
    # during a rigid translation.  Only explicitly configured cross-assembly
    # joint markers need a local correction so their world position follows a
    # different assembly than their owning Part.
    for follower in config["marker_followers"]:
        marker = markers.get(follower["marker_id"])
        if marker is None or marker.get("qp_index") is None:
            raise FullModelGenerationError(
                "完整模型母版缺少随动Marker/{}".format(follower["marker_id"])
            )
        parent_part = parts.get(marker.get("part_id"))
        if parent_part is None:
            raise FullModelGenerationError(
                "随动Marker/{}所属Part不存在".format(follower["marker_id"])
            )
        _require_unrotated_part(
            lines,
            parent_part,
            "随动Marker/{}".format(follower["marker_id"]),
        )
        requested_delta = deltas[follower["follows"]]
        parent_delta = part_deltas.get(marker.get("part_id"), (0.0, 0.0, 0.0))
        local_delta = tuple(
            requested - parent
            for requested, parent in zip(requested_delta, parent_delta)
        )
        qp_index = marker["qp_index"]
        old_qp = marker["qp"]
        replacements[qp_index] = _replace_triplet(
            lines[qp_index],
            "QP",
            tuple(value + change for value, change in zip(old_qp, local_delta)),
        )

    output_lines = []
    for index, line in enumerate(lines):
        if index == 0 and line.lower().startswith("adams view model name:"):
            line_newline = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
            output_lines.append("Adams View model name: {}{}".format(output_model_name, line_newline))
        else:
            output_lines.append(replacements.get(index, line))
        output_lines.extend(insertions.get(index, []))
    output_text = "".join(output_lines)

    # Validate the two requested anchors in the generated text before writing.
    generated_lines = output_text.splitlines(True)
    generated_records, generated_parts, generated_markers = _adm_inventory(generated_lines)
    for key, assembly in config["assemblies"].items():
        actual = _marker_world_position(
            generated_lines,
            generated_parts,
            generated_markers[assembly["anchor_marker_id"]],
            "{}定位Marker".format(assembly.get("label") or key),
        )
        if any(abs(left - right) > 1.0e-8 for left, right in zip(actual, targets[key])):
            raise FullModelGenerationError(
                "{}定位点生成后校验失败：{} != {}".format(
                    assembly.get("label") or key,
                    actual,
                    targets[key],
                )
            )
    _validate_joint_positions(
        generated_lines,
        generated_records,
        generated_parts,
        generated_markers,
        config["joint_checks"],
    )

    output_directory = os.path.abspath(output_directory or default_output_directory())
    try:
        os.makedirs(output_directory, exist_ok=True)
    except Exception as exc:
        raise FullModelGenerationError("无法创建模型输出目录：{}".format(exc))
    output_path = os.path.join(output_directory, output_model_name + ".adm")
    temporary_path = output_path + ".tmp-{}".format(os.getpid())
    try:
        with open(temporary_path, "wb") as stream:
            stream.write(output_text.encode(encoding if encoding != "utf-8-sig" else "utf-8"))
        os.replace(temporary_path, output_path)
    except Exception as exc:
        try:
            if os.path.isfile(temporary_path):
                os.remove(temporary_path)
        except Exception:
            pass
        raise FullModelGenerationError("完整模型ADM写入失败：{}".format(exc))

    return {
        "adm_path": output_path,
        "base_adm": config["base_adm"],
        "nlg_adm": config["assemblies"]["nlg"]["source_adm"],
        "mlg_adm": config["assemblies"]["mlg"]["source_adm"],
        "combination_name": config["combination_name"],
        "model_name": output_model_name,
        "resource_dir": config["resource_dir"],
        "model_full_dir": config["model_full_dir"],
        "targets": targets,
        "anchor_positions": anchor_positions,
        "deltas": deltas,
    }

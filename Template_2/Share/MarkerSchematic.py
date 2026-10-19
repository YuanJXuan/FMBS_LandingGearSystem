# -*- coding: utf-8 -*-
"""Model-local schematic metadata, marker matching and screen-space picking."""

import json
import math
import os


SCHEMATIC_MODELS = {
    "template_nlg_drop": "前起落震",
    "template_nlg_retract": "前起收放",
}
SCHEMATIC_FILES = {
    model: "{}_schematic_v1.points.json".format(model)
    for model in SCHEMATIC_MODELS
}


def load_schematic(model_dir):
    """Load one supported model's schematic from its active resource directory."""
    folder = os.path.realpath(model_dir)
    candidates = [
        (model, os.path.join(folder, filename))
        for model, filename in SCHEMATIC_FILES.items()
        if os.path.isfile(os.path.join(folder, filename))
    ]
    if not candidates:
        return None
    if len(candidates) != 1:
        raise ValueError("当前模型目录内有多套示意图配置，无法唯一匹配")
    expected_model, path = candidates[0]
    with open(path, "r", encoding="utf-8-sig") as stream:
        data = json.load(stream)
    if data.get("version") != 1 or data.get("model") != expected_model:
        raise ValueError("示意图配置版本或模型不受支持")
    if data.get("coordinate_origin") != "top_left":
        raise ValueError("示意图坐标原点必须为左上角")
    image_path = os.path.realpath(os.path.join(folder, data.get("image", "")))
    if (os.path.dirname(image_path) != folder
            or not image_path.lower().endswith(".png")
            or not os.path.isfile(image_path)):
        raise ValueError("示意图PNG不存在或不在当前模型目录内")
    size = data.get("image_size", [])
    if len(size) != 2 or any(not isinstance(v, int) or v <= 0 for v in size):
        raise ValueError("示意图尺寸无效")
    markers = data.get("markers", [])
    if not markers:
        raise ValueError("示意图没有点位配置")
    numbers, targets = set(), set()
    for marker in markers:
        number = marker.get("number")
        target = marker.get("target")
        if (not isinstance(number, str) or not number
                or not isinstance(target, str) or not target
                or number in numbers or target.lower() in targets):
            raise ValueError("示意图点位编号或Marker路径缺失、重复")
        numbers.add(number)
        targets.add(target.lower())
        for key in ("point_normalized", "badge_normalized"):
            values = marker.get(key, [])
            if (len(values) != 2 or any(
                not isinstance(v, (int, float)) or not math.isfinite(v)
                or not 0 <= v <= 1 for v in values
            )):
                raise ValueError("示意图点位 {} 的图片坐标无效".format(number))
    data["image_path"] = image_path
    data["title"] = SCHEMATIC_MODELS[expected_model]
    return data


def relative_marker_path(path):
    """Ignore a renamed model root, but retain the complete part/marker path."""
    parts = str(path or "").strip().lower().lstrip(".").split(".")
    return ".".join(parts[1:] if len(parts) > 2 else parts)


def match_markers(definitions, items):
    """Match configuration paths, never mutable row order or display labels."""
    result = []
    for definition in definitions:
        record = dict(definition)
        wanted = relative_marker_path(definition["target"])
        matches = []
        for index, item in enumerate(items, 1):
            entry = item.get("configuration_entry") or {}
            target = entry.get("target") or item.get("path")
            if relative_marker_path(target) == wanted:
                matches.append((index, item))
        record.update(index=0, available=False, reason="信息配置表中没有对应Marker")
        if len(matches) == 1:
            index, item = matches[0]
            available = item.get("node") is not None
            record.update(
                index=index, available=available,
                label=item.get("display") or definition.get("label") or wanted,
                reason="" if available else "当前模型中未找到该Marker",
            )
        elif len(matches) > 1:
            record["reason"] = "配置表中存在重复Marker，无法唯一匹配"
        result.append(record)
    return result


def fit_rect(image_size, viewport_size, margin=10):
    """Aspect-preserving image rectangle, in logical screen pixels."""
    iw, ih = image_size
    vw, vh = viewport_size
    if min(iw, ih, vw - margin * 2, vh - margin * 2) <= 0:
        return (0.0, 0.0, 0.0, 0.0)
    scale = min((vw - margin * 2) / iw, (vh - margin * 2) / ih)
    width, height = iw * scale, ih * scale
    return ((vw - width) / 2, (vh - height) / 2, width, height)


def screen_position(normalized, rect):
    x, y, width, height = rect
    return x + normalized[0] * width, y + normalized[1] * height


def hit_candidates(position, markers, rect, radius=12):
    """Pick dots AND badges, with a minimum hit radius after scaling down."""
    x, y = position
    left, top, width, height = rect
    if width <= 0 or height <= 0 or not (
        left <= x <= left + width and top <= y <= top + height
    ):
        return []
    hits = []
    for marker in markers:
        distance = min(
            math.hypot(x - px, y - py)
            for px, py in (
                screen_position(marker[key], rect)
                for key in ("point_normalized", "badge_normalized")
            )
        )
        if distance <= radius:
            hits.append((distance, marker))
    return [marker for _, marker in sorted(hits, key=lambda hit: hit[0])]

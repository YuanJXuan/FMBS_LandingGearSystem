"""Adams CMD -> Jusme Python converter (V5)

Designed from the supplied CMD/PY reference pairs.  The module is self-contained
and keeps compatibility entry points ``gen_blocks`` and ``pharseBlocks`` used by
older code.

Main improvements over the legacy parser:
- robust CMD continuation-line parsing;
- correct joint type mapping;
- support for ShapePlate, ForceField, Gravity, ForceGeneral, ForceSingleComponent,
  ShapeBlock, Function and Orient patterns seen in the supplied
  reference/Assembly models;
- expression conversion for LOC/ORI helper functions;
- optional fields are emitted only when present in CMD;
- ForceSingleComponent CREATE + later MODIFY function/property updates;
- Adams/Car torsion_spring UDE conversion to ForceRotSpringDamper;
- Adams/Car spring UDE conversion to ForceTransSpringDamper;
- solid-to-solid Adams Contact conversion to ForceContact;
- Adams/Car vpg_tire + vpg_road UDE conversion through FmbsShortcut TireCMD;
- unsupported commands are reported instead of silently discarded;
- one-call file conversion API and CLI.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from collections import Counter, OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List, Dict, Tuple, Optional


HEADER = [
    "import Jusme\n",
    "from Jusme import Base\n",
    "from Fmbs.import_all_node import MakeSceneNodeByType\n",
    "import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils\n",
]


@dataclass
class ConversionReport:
    total_blocks: int = 0
    converted_blocks: int = 0
    ignored_blocks: Counter = field(default_factory=Counter)
    unsupported_blocks: Counter = field(default_factory=Counter)
    deferred_blocks: Counter = field(default_factory=Counter)
    warnings: List[str] = field(default_factory=list)
    resource_sources: List[str] = field(default_factory=list)
    resource_directory: str = ""
    resource_files: List[str] = field(default_factory=list)
    missing_resources: List[str] = field(default_factory=list)

    @property
    def unsupported_count(self) -> int:
        return sum(self.unsupported_blocks.values())

    @property
    def deferred_count(self) -> int:
        return sum(self.deferred_blocks.values())

    def as_text(self) -> str:
        lines = [
            f"total_blocks={self.total_blocks}",
            f"converted_blocks={self.converted_blocks}",
            f"unsupported_blocks={self.unsupported_count}",
            f"deferred_blocks={self.deferred_count}",
        ]
        if self.unsupported_blocks:
            lines.append("unsupported:")
            for name, count in self.unsupported_blocks.most_common():
                lines.append(f"  {count:4d}  {name}")
        if self.deferred_blocks:
            lines.append("recognized_but_not_reconstructed:")
            for name, count in self.deferred_blocks.most_common():
                lines.append(f"  {count:4d}  {name}")
        if self.ignored_blocks:
            lines.append("intentionally_ignored:")
            for name, count in self.ignored_blocks.most_common():
                lines.append(f"  {count:4d}  {name}")
        if self.warnings:
            lines.append("warnings:")
            lines.extend(f"  - {w}" for w in self.warnings)
        if self.resource_directory:
            lines.append(f"resource_directory={self.resource_directory}")
        if self.resource_files:
            lines.append("resource_files:")
            lines.extend(f"  - {p}" for p in self.resource_files)
        if self.missing_resources:
            lines.append("missing_resources:")
            lines.extend(f"  - {p}" for p in self.missing_resources)
        return "\n".join(lines) + "\n"


@dataclass
class ConverterState:
    model_name: str = ""
    units_created: bool = False
    known_entities: Dict[str, str] = field(default_factory=dict)
    entity_meta: Dict[str, Dict[str, object]] = field(default_factory=dict)

    # Adams/Car UDE bookkeeping.  vpg_tire/vpg_road are not emitted as generic
    # UDE nodes; their fields are accumulated and reconstructed with TireCMD.
    ude_instances: Dict[str, Dict[str, object]] = field(default_factory=dict)
    tire_imports_emitted: bool = False
    tire_defaults_emitted: bool = False
    tire_counter: int = 0
    road_counter: int = 0
    road_names: Dict[str, str] = field(default_factory=dict)
    materialized_roads: set = field(default_factory=set)
    path_aliases: Dict[str, str] = field(default_factory=dict)
    pending_road_markers: Dict[str, List[Dict[str, str]]] = field(default_factory=dict)


# Persistent state used only by the legacy-style gen_blocks/pharseBlocks API.
# New code should prefer convert_text/convert_file, which always use a fresh state.
_legacy_state = ConverterState()


def initJusmeModel() -> None:
    """Reset compatibility state before converting another model.

    The legacy implementation exposed ``initJusmeModel()``.  Keeping the name
    makes it easier to replace the old module without changing the caller.
    """
    global _legacy_state
    _legacy_state = ConverterState()


# Commands that do not contribute executable model-building code in the supplied
# golden Python files.  They are counted, but not treated as failures.
IGNORED_PREFIXES = (
    "defaults attributes",
    "defaults coordinate_system",
    "model attributes",
    "model display",
    "view erase",
    "data_element attributes",
    "data_element create array ic_array",
    "marker attributes",
    "point attributes",
    "part attributes",
    "geometry attributes",
    "constraint attributes",
    "force attributes",
    "geometry create shape force",
    "geometry modify shape force",
    # ForceContact reconstructs the physical contact.  GContact is only the
    # Adams force-display graphic and has no effect on the model equations.
    "geometry create shape gcontact",
    "undo begin_block",
    "undo end_block",
)


JOINT_NODE_TYPES = {
    "cylindrical": "JointCylinder",
    "revolute": "JointRevolute",
    "spherical": "JointSpherical",
    "fixed": "JointFixed",
    "hooke": "JointHooke",
    "translational": "JointTranslational",
    "inplane": "JointInplane",
    "planar": "JointPlanar",
    "perpendicular": "JointPerpendicular",
}


def getElementName(full_name: str) -> str:
    return full_name.rstrip(".").split(".")[-1]


def _helper_name(full_name: str) -> str:
    # Matches the naming convention in the supplied reference Python:
    # ._AA_x.ground.p -> __AA_x_ground_p
    return full_name.strip().replace(".", "_")


def _clean_line(line: str) -> str:
    s = line.strip()
    if s.endswith("&"):
        s = s[:-1].rstrip()
    return s


def gen_blocks(cmd_lines: Iterable[str]) -> List[List[str]]:
    """Split an Adams CMD stream into command blocks.

    A line beginning with ``!`` terminates the current block.  Unlike the legacy
    implementation, the final block is always flushed even when the file does not
    end with a comment/blank line.
    """
    blocks: List[List[str]] = []
    block: List[str] = []
    for raw in cmd_lines:
        s = raw.strip()
        if not s:
            continue
        if s.startswith("!"):
            if block:
                blocks.append(block)
                block = []
            continue
        block.append(s)
    if block:
        blocks.append(block)
    return blocks


def _parse_fields(block: List[str]) -> "OrderedDict[str, str]":
    """Parse key/value lines and join Adams continuation lines.

    Examples handled correctly::

        inertia_marker = &
          .MODEL.part.inertia_frame &

        x = 1, 2, 3, &
            4, 5, 6 &

        location = &
          (LOC_RELATIVE_TO(...)) &
    """
    fields: "OrderedDict[str, str]" = OrderedDict()
    current_key: Optional[str] = None

    for raw in block[1:]:
        s = _clean_line(raw)
        if not s:
            continue
        # A continuation payload may itself contain '=' (notably quoted
        # simulation commands).  Treat only a normal Adams identifier at the
        # beginning of the line as a new key/value field.
        field_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$", s)
        if field_match:
            key = field_match.group(1).strip()
            value = field_match.group(2).strip()
            fields[key] = value
            current_key = key
        elif current_key is not None:
            # Keep commas naturally; use one blank only when needed.
            old = fields[current_key]
            if old and not old.endswith((",", "(", "{")) and not s.startswith(","):
                old += " "
            fields[current_key] = old + s
    return fields


def _normalize_model_name(model_name: str) -> str:
    """Return the scene-root name used by generated node paths."""
    return model_name.strip().strip("\"'").lstrip(".")


def _find_model_name(blocks: List[List[str]]) -> str:
    """Read the first ``model create`` name before emitting earlier blocks."""
    for block in blocks:
        if not block:
            continue
        if _clean_line(block[0]).lower().startswith("model create"):
            model_name = _normalize_model_name(
                _parse_fields(block).get("model_name", "")
            )
            if model_name:
                return model_name
    return ""


def _float_token(token: str) -> float:
    t = token.strip()
    t = re.sub(r"(?i)(deg|degree|degrees)$", "", t)
    t = t.rstrip("dD")
    return float(t)


def _num(token: str) -> str:
    return repr(_float_token(token))


def _int(token: str) -> str:
    return str(int(float(token.strip())))


def _vector(value: str, angle: bool = False) -> List[float]:
    parts = [p.strip() for p in value.split(",") if p.strip()]
    vals = []
    for p in parts:
        if angle:
            p = p.rstrip("dD")
        vals.append(float(p))
    return vals


def _vector_code(value: str, angle: bool = False) -> str:
    vals = _vector(value, angle)
    return "Base.Vector ({})".format(", ".join(repr(v) for v in vals))


def _num_list(value: str, strip_d: bool = False) -> List[float]:
    vals = []
    for p in value.split(","):
        p = p.strip()
        if not p:
            continue
        if strip_d:
            p = p.rstrip("dD")
        vals.append(float(p))
    return vals


def _emit_get_object(out: List[str], full_name: str, suffix: str = "") -> str:
    var = _helper_name(full_name)
    out.append(f"{var} = Jusme.ActiveUSScene.getObject('{full_name}'){suffix}\n")
    return var


def _strip_outer_parens(expr: str) -> str:
    e = expr.strip()
    if e.startswith("(") and e.endswith(")"):
        return e[1:-1].strip()
    return e


def _split_top_level_args(s: str) -> List[str]:
    args, buf = [], []
    depth = 0
    quote = None
    i = 0
    while i < len(s):
        ch = s[i]
        if quote:
            buf.append(ch)
            if ch == quote and (i == 0 or s[i - 1] != "\\"):
                quote = None
        else:
            if ch in "'\"":
                quote = ch
                buf.append(ch)
            elif ch in "({[":
                depth += 1
                buf.append(ch)
            elif ch in ")}]":
                depth -= 1
                buf.append(ch)
            elif ch == "," and depth == 0:
                args.append("".join(buf).strip())
                buf = []
            else:
                buf.append(ch)
        i += 1
    if buf or s.strip():
        args.append("".join(buf).strip())
    return args


def _call_parts(expr: str) -> Tuple[str, List[str]]:
    e = _strip_outer_parens(expr)
    m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*\((.*)\)$", e, re.S)
    if not m:
        return "", []
    return m.group(1), _split_top_level_args(m.group(2))


def _coord_literal(arg: str) -> str:
    """Convert {x,y,z}[inch] to a Python list, converting inch only when stated."""
    a = arg.strip()
    inch = bool(re.search(r"(?i)inch(?:es)?\s*$", a))
    # Adams may append unit words directly after the closing brace, e.g.
    # {0,0,0}inch or {0,0,0}degrees.
    a = re.sub(r"(?i)(inch(?:es)?|degrees?|deg|mm|millimeters?)\s*$", "", a).strip()
    if a.startswith("{") and a.endswith("}"):
        a = a[1:-1]
    vals = [float(x.strip().rstrip("dD")) for x in a.split(",") if x.strip()]
    if inch:
        vals = [v * 25.4 for v in vals]
    return "[{}]".format(", ".join(repr(v) for v in vals))


def _replace_paths_in_expr(expr: str, paths: List[str]) -> str:
    new = expr
    # Longest first prevents prefix replacements from damaging longer paths.
    for p in sorted(set(paths), key=len, reverse=True):
        new = new.replace(p, _helper_name(p))
    return new


def _path_tokens(text: str) -> List[str]:
    # Adams object paths in the supplied models all begin with a dot and do not
    # contain whitespace, commas or parentheses.
    return re.findall(r"\.(?:[A-Za-z_][A-Za-z0-9_]*)(?:\.[A-Za-z_][A-Za-z0-9_]*)*", text)


def _emit_direct_property_ref(
    out: List[str], target: str, expr: str, property_name: str
) -> bool:
    """Translate ``(.model.node.property)`` pose references from Adams."""
    value = _strip_outer_parens(expr)
    suffix = "." + property_name
    if not value.lower().endswith(suffix):
        return False
    object_path = value[: -len(suffix)]
    if not re.fullmatch(
        r"\.(?:[A-Za-z_][A-Za-z0-9_]*)(?:\.[A-Za-z_][A-Za-z0-9_]*)*",
        object_path,
    ):
        return False
    source = _emit_get_object(out, object_path, suffix)
    out.append(f"{target}.{property_name} = {source}\n")
    return True


def _emit_location_expr(out: List[str], target: str, expr: str) -> bool:
    if _emit_direct_property_ref(out, target, expr, "location"):
        return True

    func, args = _call_parts(expr)
    if func == "LOC_RELATIVE_TO" and len(args) >= 2:
        ref = args[1].strip()
        var = _emit_get_object(out, ref)
        out.append(f"{target}.location = (VecUtils.LOC_RELATIVE_TO({_coord_literal(args[0])}, {var}))\n")
        return True

    if func == "LOC_ALONG_LINE" and len(args) >= 3:
        p1, p2, dist = args[0].strip(), args[1].strip(), args[2].strip()
        v1 = _emit_get_object(out, p1, ".location")
        v2 = _emit_get_object(out, p2, ".location")
        paths = _path_tokens(dist) + [p1, p2]
        dist2 = _replace_paths_in_expr(dist, paths)
        if "DM(" in dist2 and "VecUtils.DM(" not in dist2:
            dist2 = dist2.replace("DM(", "VecUtils.DM(")
        out.append(f"{target}.location = (VecUtils.LOC_ALONG_LINE({v1}, {v2}, {dist2}))\n")
        return True

    if func == "LOC_ON_AXIS" and len(args) >= 3:
        p = args[0].strip()
        v = _emit_get_object(out, p, ".location")
        distance = re.sub(r"(?i)(inch(?:es)?|mm|millimeters?)$", "", args[1].strip()).strip()
        out.append(f"{target}.location = (VecUtils.LOC_ON_AXIS({v}, {distance}, {args[2].strip()}))\n")
        return True
    return False


def _emit_orientation_expr(
    out: List[str],
    target: str,
    expr: str,
    relative_to: str = "",
) -> bool:
    if _emit_direct_property_ref(out, target, expr, "orientation"):
        return True

    func, args = _call_parts(expr)

    if func == "ORI_RELATIVE_TO" and len(args) >= 2:
        ref = args[1].strip()
        var = _emit_get_object(out, ref)
        coord = _coord_literal(args[0])
        out.append(f"{target}.orientation = (VecUtils.ORI_RELATIVE_TO({coord}, {var}))\n")
        return True

    if func == "ORI_ALONG_AXIS" and len(args) >= 3:
        p1, p2 = args[0].strip(), args[1].strip()
        v1 = _emit_get_object(out, p1, ".location")
        v2 = _emit_get_object(out, p2, ".location")
        out.append(f"{target}.orientation = (VecUtils.ORI_ALONG_AXIS({v1}, {v2}, {args[2].strip()}))\n")
        return True

    if func == "ORI_IN_PLANE" and len(args) >= 4:
        # Imported Point nodes expose ``location`` but not ``global_loc``.
        # All current ORI_IN_PLANE reference points are ground-owned, so their
        # local and global coordinates are identical.
        p1, p2, p3 = (args[0].strip(), args[1].strip(), args[2].strip())
        v1 = _emit_get_object(out, p1, ".location")
        v2 = _emit_get_object(out, p2, ".location")
        v3 = _emit_get_object(out, p3, ".location")
        out.append(f"{target}.orientation = (VecUtils.ORI_IN_PLANE({v1}, {v2}, {v3}, {args[3].strip()}))\n")
        return True

    if func == "ORI_LOCAL" and len(args) >= 2:
        inner_func, inner_args = _call_parts(args[0])
        ref = args[1].strip()
        if inner_func == "ORI_ALIGN_AXIS" and len(inner_args) >= 2:
            axis_spec = _strip_outer_parens(inner_args[1]).strip().strip("'\"")
            axis_spec = re.sub(r"\s+", "", axis_spec).upper()
            same_reference = bool(relative_to) and (
                _strip_outer_parens(ref) == _strip_outer_parens(relative_to)
            )
            if axis_spec in {"Z+Z", "ZZ"} and same_reference:
                # Adams ORI_ALIGN_AXIS(frame, "Z+Z") is the identity case: it
                # returns ``frame`` in global coordinates.  Jasmine does not
                # expose ORI_ALIGN_AXIS/ORI_LOCAL, so leave the orientation
                # global here.  _emit_marker_modify's single global2local call
                # below converts both the marker location and orientation into
                # the requested relative_to part without double conversion.
                frame = _emit_get_object(out, inner_args[0].strip())
                out.append(f"{target}.orientation = {frame}.orientation\n")
                return True
    return False


def _emit_marker_modify(out: List[str], fields: Dict[str, str], report: ConversionReport):
    full = fields.get("marker_name", "")
    if not full:
        report.warnings.append("marker modify without marker_name")
        return
    name = getElementName(full)
    out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
    rel = fields.get("relative_to", "").strip()
    if rel:
        out.append(f"relative_to = Jusme.ActiveUSScene.getObject('{rel}')\n")
        out.append(f"{name}.relative_to = relative_to\n")
    out.append(f"{name}.marker_name = '{full}'\n")

    loc_ok = False
    ori_ok = False
    if fields.get("location"):
        try:
            out.append(f"{name}.location = {_vector_code(fields['location'])}\n")
            loc_ok = True
        except Exception:
            loc_ok = _emit_location_expr(out, name, fields["location"])
        if not loc_ok:
            report.warnings.append(f"unsupported location expression for {full}: {fields['location']}")
    if fields.get("orientation"):
        try:
            out.append(f"{name}.orientation = {_vector_code(fields['orientation'], True)}\n")
            ori_ok = True
        except Exception:
            ori_ok = _emit_orientation_expr(
                out,
                name,
                fields["orientation"],
                rel,
            )
        if not ori_ok:
            report.warnings.append(f"unsupported orientation expression for {full}: {fields['orientation']}")

    if rel and (loc_ok or ori_ok):
        out.append(
            f"loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, {name}.location, {name}.orientation)\n"
        )
        out.append(f"{name}.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])\n")
        if ori_ok:
            out.append(f"{name}.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])\n")
    out.extend(["\n", "\n"])


def _emit_part_modify(out: List[str], fields: Dict[str, str], report: ConversionReport):
    full = fields.get("part_name", "")
    if not full:
        report.warnings.append("part modify without part_name")
        return
    name = getElementName(full)
    out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
    out.append(f"{name}.part_name = '{full}'\n")
    if fields.get("location") and not _emit_location_expr(out, name, fields["location"]):
        report.warnings.append(f"unsupported part location expression for {full}")
    if fields.get("orientation") and not _emit_orientation_expr(out, name, fields["orientation"]):
        report.warnings.append(f"unsupported part orientation expression for {full}")
    out.extend(["\n", "\n"])


def _contact_geometry_refs(value: str, state: ConverterState) -> List[str]:
    """Return one or more Adams geometry paths from a Contact field."""
    refs = _path_tokens(value)
    if not refs:
        ref = _normalize_object_ref(value)
        refs = [ref] if ref else []
    return [_apply_path_alias(state, ref) for ref in refs]


def _emit_contact(out: List[str], f: Dict[str, str], state: ConverterState,
                  report: ConversionReport) -> bool:
    """Convert an Adams physical Contact to a Jusme ForceContact node."""
    full = f.get("contact_name", "")
    if not full:
        report.warnings.append("contact create without contact_name")
        return False

    name = getElementName(full)
    i_geometries = _contact_geometry_refs(f.get("i_geometry_name", ""), state)
    j_geometries = _contact_geometry_refs(f.get("j_geometry_name", ""), state)
    if not i_geometries or not j_geometries:
        report.warnings.append(
            f"contact geometry is incomplete for {full}: "
            f"i_geometry_name={f.get('i_geometry_name', '')!r}, "
            f"j_geometry_name={f.get('j_geometry_name', '')!r}"
        )

    out.append(f"{name} = MakeSceneNodeByType('ForceContact', '{full}')\n")
    if "type" in f:
        out.append(f"{name}.type = {_string_literal(f['type'])}\n")

    i_code = ", ".join(
        f"Jusme.ActiveUSScene.getObject('{path}')" for path in i_geometries
    )
    j_code = ", ".join(
        f"Jusme.ActiveUSScene.getObject('{path}')" for path in j_geometries
    )
    out.append(f"i_geometry_name = [{i_code}]\n")
    out.append(f"j_geometry_name = [{j_code}]\n")
    out.append(f"{name}.i_geometry_name = i_geometry_name\n")
    out.append(f"{name}.j_geometry_name = j_geometry_name\n")

    for key in ("stiffness", "exponent", "damping", "dmax"):
        if key in f:
            out.append(f"{name}.{key} = {_num(f[key])}\n")

    # The supplied Jusme ForceContact pattern uses the frictionless option.
    out.append(f"{name}.friction_opt = 0\n")
    out.append(f"{name}.no_friction = True\n")
    out.extend(["\n", "\n"])

    state.known_entities[full] = "ForceContact"
    state.entity_meta[full] = {
        "kind": "ForceContact",
        "i_geometry_name": i_geometries,
        "j_geometry_name": j_geometries,
    }
    return True


def _emit_force_field(out: List[str], f: Dict[str, str]):
    full = f.get("field_name", "")
    name = getElementName(full)
    out.append(f"{name} = MakeSceneNodeByType('ForceField', '{full}')\n")
    for key in ("i_marker_name", "j_marker_name"):
        if key in f:
            out.append(f"{key} = Jusme.ActiveUSScene.getObject('{f[key]}')\n")
            out.append(f"{name}.{key} = {key}\n")
    out.append(f"{name}.field_name = '{full}'\n")
    if "adams_id" in f:
        out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
    if "comments" in f:
        out.append(f"{name}.comments = '{f['comments']}'\n")
    for k in ("translation_at_preload", "force_preload", "torque_preload"):
        if k in f:
            out.append(f"{name}.{k} = {_vector_code(f[k])}\n")
    if "rotation_at_preload" in f:
        out.append(f"{name}.rotation_at_preload = {_vector_code(f['rotation_at_preload'], True)}\n")
    if "formulation" in f:
        out.append(f"{name}.formulation = '{f['formulation']}'\n")
    for k in ("length_tolerance", "damping_ratio"):
        if k in f:
            out.append(f"{name}.{k} = {_num(f[k])}\n")
    if "stiffness_matrix" in f:
        vals = _num_list(f["stiffness_matrix"])
        out.append(f"{name}.stiffness_matrix = {vals!r}\n")
    out.extend(["\n", "\n"])


def _emit_shape_block(out: List[str], f: Dict[str, str], state: ConverterState,
                      report: ConversionReport, *, modify: bool = False) -> bool:
    """Create or update a Jusme ShapeBlock from Adams block geometry."""
    full = _apply_path_alias(state, f.get("block_name", ""))
    if not full:
        report.warnings.append("shape block without block_name")
        return False

    name = getElementName(full)
    if modify:
        out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
    else:
        out.append(f"{name} = MakeSceneNodeByType('ShapeBlock', '{full}')\n")

    if f.get("corner_marker"):
        marker = _apply_path_alias(state, _normalize_object_ref(f["corner_marker"]))
        out.append(
            f"{name}.corner_marker = "
            f"Jusme.ActiveUSScene.getObject('{marker}')\n"
        )
    if f.get("diag_corner_coords"):
        try:
            coords = _tuple_code_with_optional_units(f["diag_corner_coords"])
            out.append(f"{name}.diag_corner_coords = {coords}\n")
        except ValueError:
            report.warnings.append(
                f"unsupported ShapeBlock diagonal coordinates for {full}: "
                f"{f['diag_corner_coords']}"
            )
    out.extend(["\n", "\n"])

    state.known_entities[full] = "ShapeBlock"
    state.entity_meta[full] = {
        "kind": "ShapeBlock",
        "corner_marker": f.get("corner_marker", ""),
        "diag_corner_coords": f.get("diag_corner_coords", ""),
    }
    return True


def _emit_shape_plate(out: List[str], f: Dict[str, str]):
    full = f.get("plate_name", "")
    name = getElementName(full)
    out.append(f"{name} = MakeSceneNodeByType('ShapePlate', '{full}')\n")
    # Keep the same cautious behavior as the supplied golden converter: these
    # links/properties are not known to be supported by Jusme's node interface.
    for prop in ("marker_name", "width", "radius"):
        if prop in f:
            out.append(f"# >>>[ERROR] CAN NOT find link prop({prop}) from {full}, Please DOUBLE CHECK!\n")
    out.append(f"{name}.plate_name = '{full}'\n")
    out.extend(["\n", "\n"])


def _cmd_bool(value: str) -> bool:
    return value.strip().lower() in ("yes", "on", "true", "1")


def _string_literal(value: str) -> str:
    """Return a safe Python string literal while preserving Adams text."""
    return repr(value)


def _emit_force_general_create(out: List[str], f: Dict[str, str], state: ConverterState) -> None:
    """Emit the ForceGeneral pattern used in RetractAssembly.py."""
    full = f.get("general_force_name", f.get("force_name", ""))
    name = getElementName(full)
    out.append(f"{name} = MakeSceneNodeByType('ForceGeneral', '{full}')\n")
    for key in ("i_marker_name", "j_floating_marker_name", "ref_marker_name"):
        if f.get(key):
            local = key
            out.append(f"{local} = Jusme.ActiveUSScene.getObject('{f[key]}')\n")
            out.append(f"{name}.{key} = {local}\n")
    # The Assembly references use function-based definition for General Force.
    out.append(f"{name}.define_using_opt = 0\n")
    out.append(f"{name}.define_function_opt = 0\n")
    for key in ("x_force_function", "y_force_function", "z_force_function",
                "x_torque_function", "y_torque_function", "z_torque_function"):
        if key in f:
            out.append(f"{name}.{key} = {_string_literal(f[key])}\n")
    state.known_entities[full] = "ForceGeneral"
    state.entity_meta[full] = {
        "kind": "ForceGeneral",
        "i_marker_name": f.get("i_marker_name", ""),
        "j_floating_marker_name": f.get("j_floating_marker_name", ""),
        "ref_marker_name": f.get("ref_marker_name", ""),
    }
    out.extend(["\n", "\n"])


def _emit_force_general_modify(out: List[str], f: Dict[str, str]) -> None:
    full = f.get("general_force_name", f.get("force_name", ""))
    name = getElementName(full)
    out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
    for key in ("x_force_function", "y_force_function", "z_force_function",
                "x_torque_function", "y_torque_function", "z_torque_function"):
        if key in f:
            out.append(f"{name}.{key} = {_string_literal(f[key])}\n")
    out.extend(["\n", "\n"])


def _single_component_force_full_name(f: Dict[str, str]) -> str:
    """Return the object name used by common Adams single-component force exports."""
    for key in (
        "single_component_force_name", "force_name", "single_force_name",
        "single_component_name", "torque_name", "element_name",
    ):
        if f.get(key):
            return f[key]
    return ""


def _single_component_freedom_opt(value: str) -> Optional[int]:
    """Map common Adams freedom labels to Jusme's freedom_opt index."""
    token = value.strip().lower()
    aliases = {
        "x": 0, "x_component": 0, "x_force": 0, "x_torque": 0,
        "y": 1, "y_component": 1, "y_force": 1, "y_torque": 1,
        "z": 2, "z_component": 2, "z_force": 2, "z_torque": 2,
    }
    if token in aliases:
        return aliases[token]
    try:
        return int(float(token))
    except ValueError:
        return None


def _emit_force_single_component(out: List[str], f: Dict[str, str], state: ConverterState) -> None:
    """Create a ForceSingleComponent from an Adams direct-force block."""
    full = _single_component_force_full_name(f)
    name = getElementName(full)
    out.append(f"{name} = MakeSceneNodeByType('ForceSingleComponent', '{full}')\n")
    if "type_of_freedom" in f:
        out.append(f"{name}.type_of_freedom = {_string_literal(f['type_of_freedom'])}\n")
    if "freedom" in f:
        val = _single_component_freedom_opt(f["freedom"])
        if val is not None:
            out.append(f"{name}.freedom_opt = {val}\n")
    elif "freedom_opt" in f:
        out.append(f"{name}.freedom_opt = {_int(f['freedom_opt'])}\n")
    if "action_only" in f:
        out.append(f"{name}.action_only = {_cmd_bool(f['action_only'])}\n")
    if "function_opt" in f:
        out.append(f"{name}.function_opt = {_int(f['function_opt'])}\n")
    else:
        out.append(f"{name}.function_opt = 0\n")
    if "function" in f:
        out.append(f"{name}.function = {_string_literal(f['function'])}\n")
    for key in ("i_marker_name", "j_marker_name"):
        if f.get(key):
            out.append(f"{key} = Jusme.ActiveUSScene.getObject('{f[key]}')\n")
            out.append(f"{name}.{key} = {key}\n")
    if "position_define_opt" in f:
        out.append(f"{name}.position_define_opt = {_int(f['position_define_opt'])}\n")
    elif f.get("i_marker_name") or f.get("j_marker_name"):
        out.append(f"{name}.position_define_opt = 1\n")
    state.known_entities[full] = "ForceSingleComponent"
    out.extend(["\n", "\n"])


def _emit_force_single_component_modify(out: List[str], f: Dict[str, str]) -> None:
    """Apply later Adams MODIFY fields to an existing ForceSingleComponent.

    This is required for exports that create the force with ``function = ""``
    and assign the real function in a later ``force modify direct ...`` block.
    """
    full = _single_component_force_full_name(f)
    name = getElementName(full)
    out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")

    if "type_of_freedom" in f:
        out.append(f"{name}.type_of_freedom = {_string_literal(f['type_of_freedom'])}\n")
    if "freedom" in f:
        val = _single_component_freedom_opt(f["freedom"])
        if val is not None:
            out.append(f"{name}.freedom_opt = {val}\n")
    elif "freedom_opt" in f:
        out.append(f"{name}.freedom_opt = {_int(f['freedom_opt'])}\n")
    if "action_only" in f:
        out.append(f"{name}.action_only = {_cmd_bool(f['action_only'])}\n")
    if "function_opt" in f:
        out.append(f"{name}.function_opt = {_int(f['function_opt'])}\n")
    if "function" in f:
        out.append(f"{name}.function = {_string_literal(f['function'])}\n")

    marker_changed = False
    for key in ("i_marker_name", "j_marker_name"):
        if f.get(key):
            marker_changed = True
            out.append(f"{key} = Jusme.ActiveUSScene.getObject('{f[key]}')\n")
            out.append(f"{name}.{key} = {key}\n")
    if "position_define_opt" in f:
        out.append(f"{name}.position_define_opt = {_int(f['position_define_opt'])}\n")
    elif marker_changed:
        out.append(f"{name}.position_define_opt = 1\n")

    out.extend(["\n", "\n"])


def _emit_measure_object(out: List[str], f: Dict[str, str], state: ConverterState,
                         report: ConversionReport, cmd: str) -> bool:
    """Convert object measures when a supplied Assembly gives a verified mapping.

    The provided RetractAssembly maps AX/AY/AZ projection-angle object measures
    to an ``Orient`` node.  No verified Jusme construction for object
    translational_velocity or element_force is present in the four supplied
    Assembly files, so those are explicitly deferred rather than guessed.
    """
    full = f.get("measure_name", "")
    name = getElementName(full)
    characteristic = f.get("characteristic", "").strip().lower()
    component = f.get("component", "").strip().lower()
    obj = f.get("object", "").strip()

    if characteristic == "ax_ay_az_projection_angles":
        meta = state.entity_meta.get(obj, {})
        i_marker = meta.get("i_marker_name", "")
        j_marker = meta.get("j_marker_name", "")
        if not (i_marker and j_marker):
            report.warnings.append(f"cannot resolve joint markers for orientation measure {full}: {obj}")
            return False
        # RetractAssembly uses characteristic_opt=0/component_angle_opt=0 for
        # the z projection-angle measure and from=i, to=j.
        out.append(f"{name} = MakeSceneNodeByType('Orient', '{full}')\n")
        out.append(f"{name}.characteristic_opt = 0\n")
        if component == "z_component":
            out.append(f"{name}.component_angle_opt = 0\n")
        else:
            report.warnings.append(f"unverified Orient component for {full}: {component}")
            out.append(f"{name}.component_angle_opt = 0\n")
        from_marker, to_marker = i_marker, j_marker
        if not _cmd_bool(f.get("from_first", "yes")):
            from_marker, to_marker = to_marker, from_marker
        out.append(f"from_frame = Jusme.ActiveUSScene.getObject('{from_marker}')\n")
        out.append(f"to_frame = Jusme.ActiveUSScene.getObject('{to_marker}')\n")
        out.append(f"{name}.from_frame = from_frame\n")
        out.append(f"{name}.to_frame = to_frame\n")
        out.extend(["\n", "\n"])
        state.known_entities[full] = "Orient"
        return True

    # Recognize the command but do not invent a Jusme node API that is absent
    # from all four supplied reference Assembly files.
    key = f"{cmd} [{characteristic}/{component}]"
    report.deferred_blocks[key] += 1
    out.append(f"# [CMD2PY DEFERRED] {full}: object measure {characteristic}/{component} on {obj}\n")
    out.append("# No verified Jusme Python construction for this measure exists in the supplied Assembly references.\n\n")
    return True


def _emit_function_measure(out: List[str], f: Dict[str, str]) -> None:
    """Emit the Function measurement pattern demonstrated in TurnAssembly.py."""
    full = f.get("measure_name", f.get("function_name", ""))
    name = getElementName(full)
    out.append(f"{name} = MakeSceneNodeByType('Function', '{full}')\n")
    if "function" in f:
        out.append(f"{name}.function = {_string_literal(f['function'])}\n")
    out.extend(["\n", "\n"])


def _emit_point_measure(out: List[str], f: Dict[str, str],
                        state: ConverterState,
                        report: ConversionReport,
                        cmd: str) -> bool:
    """Convert a point translational-velocity measure to a Jusme Pt2pt node."""
    full = f.get("measure_name", "")
    point = _apply_path_alias(state, f.get("point", ""))
    characteristic = f.get("characteristic", "").strip().lower()
    component = f.get("component", "").strip().lower()

    # Verified platform references use these options for the point-speed
    # measures found in the supplied brake/turn/swing models.
    if characteristic != "translational_velocity" or component not in (
        "x_component",
        "mag_component",
    ):
        key = f"{cmd} [{characteristic}/{component}]"
        report.deferred_blocks[key] += 1
        out.append(
            f"# [CMD2PY DEFERRED] {full}: point measure "
            f"{characteristic}/{component} on {point}\n\n"
        )
        return True

    model_name = state.model_name
    if not model_name and point.startswith("."):
        model_name = point[1:].split(".", 1)[0]
    if not (full and point and model_name):
        report.warnings.append(
            f"cannot resolve point measure path for {full}: {point}"
        )
        return False

    name = getElementName(full)
    origin = f".{model_name}.ground.origo"
    out.append(f"{name} = MakeSceneNodeByType('Pt2pt', '{full}')\n")
    out.append(f"{name}.component_opt = 3\n")
    out.append(f"{name}.characteristic_opt = 1\n")
    out.append(f"from_point = Jusme.ActiveUSScene.getObject('{origin}')\n")
    out.append(f"{name}.from_point = from_point\n")
    out.append(f"to_point = Jusme.ActiveUSScene.getObject('{point}')\n")
    out.append(f"{name}.to_point = to_point\n")
    out.extend(["\n", "\n"])
    state.known_entities[full] = "Pt2pt"
    return True


def _emit_dm_length_expr(out: List[str], target: str, expr: str) -> bool:
    """Convert DM(p1,p2) optionally followed by a numeric +/- offset."""
    e = _strip_outer_parens(expr)
    try:
        scalar_length = _length_number_with_optional_units(e)
    except ValueError:
        scalar_length = None
    if scalar_length is not None:
        out.append(f"{target}.length = {scalar_length!r}\n")
        return True
    m = re.match(r"^DM\s*\(([^,]+),\s*([^\)]+)\)\s*([+-]\s*[-+0-9.eEdD]+)?$", e, re.I)
    if not m:
        return False
    p1, p2, tail = m.group(1).strip(), m.group(2).strip(), m.group(3)
    v1 = _emit_get_object(out, p1, ".location")
    v2 = _emit_get_object(out, p2, ".location")
    code = f"VecUtils.DM({v1}, {v2})"
    if tail:
        sign = "+" if "+" in tail else "-"
        raw_num = tail.replace("+", "").replace("-", "").strip()
        code += f" {sign} {_num(raw_num)}"
    out.append(f"{target}.length = ({code})\n")
    return True



def _strip_value_wrappers(value: str) -> str:
    """Remove Adams expression parentheses / quote wrappers around scalar refs."""
    s = value.strip()
    # Repeated parentheses are common in UDE variable values.
    while s.startswith("(") and s.endswith(")") and len(s) >= 2:
        inner = s[1:-1].strip()
        # Only peel balanced one-level wrappers.
        if inner.count("(") == inner.count(")"):
            s = inner
        else:
            break
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "'\"":
        s = s[1:-1]
    return s.strip()


def _resource_file_name(value: str) -> str:
    """Return the final component of a Windows or POSIX resource path."""
    source = _strip_value_wrappers(value)
    return source.replace("\\", "/").rstrip("/").rsplit("/", 1)[-1]


def _py_resource_path(value: str, report: ConversionReport) -> str:
    """Emit a generated-script-relative path and remember its original source."""
    source = _strip_value_wrappers(value)
    if source and source not in report.resource_sources:
        report.resource_sources.append(source)

    file_name = _resource_file_name(source)
    return f"os.path.join(_MODEL_RESOURCE_DIR, {file_name!r})"


def _ude_definition_kind(definition_name: str) -> str:
    d = _strip_value_wrappers(definition_name).lower()
    if d.endswith(".vpg_tire") or d == "vpg_tire":
        return "tire"
    if d.endswith(".vpg_road") or d == "vpg_road":
        return "road"
    if d.endswith(".torsion_spring") or d == "torsion_spring":
        return "torsion_spring"
    if d.endswith(".spring") or d == "spring":
        return "trans_spring"
    return ""


def _allocate_road_name(state: ConverterState, road_full: str) -> str:
    if road_full in state.road_names:
        return state.road_names[road_full]
    state.road_counter += 1
    name = "road" if state.road_counter == 1 else f"road_{state.road_counter}"
    state.road_names[road_full] = name
    model_prefix = f".{state.model_name}" if state.model_name else ""
    state.path_aliases[f"{road_full}.road_part"] = f"{model_prefix}.{name}"
    return name


def _apply_path_alias(state: ConverterState, full_name: str) -> str:
    value = _strip_value_wrappers(full_name)
    for old, new in sorted(state.path_aliases.items(), key=lambda kv: len(kv[0]), reverse=True):
        if value == old or value.startswith(old + "."):
            return new + value[len(old):]
    return value


def _find_ude_for_variable(state: ConverterState, variable_name: str) -> Tuple[str, str]:
    full = _strip_value_wrappers(variable_name)
    for inst in sorted(state.ude_instances, key=len, reverse=True):
        if full.startswith(inst + "."):
            return inst, full[len(inst) + 1:]
    return "", ""


def _ude_var_entry(state: ConverterState, instance: str, key: str) -> Optional[Dict[str, str]]:
    meta = state.ude_instances.get(instance, {})
    vars_map = meta.get("variables", {})
    if isinstance(vars_map, dict):
        val = vars_map.get(key)
        if isinstance(val, dict):
            return val
    return None


def _ude_var_text(state: ConverterState, instance: str, key: str, default: str = "") -> str:
    entry = _ude_var_entry(state, instance, key)
    if not entry:
        return default
    return _strip_value_wrappers(entry.get("value", default))


def _number_with_optional_units(value: str) -> float:
    """Read a scalar such as ``73``, ``(73mm)`` or ``6.6E-3(N-mm/rad)``."""
    raw = _strip_value_wrappers(value)
    try:
        return _float_token(raw)
    except Exception:
        match = re.match(
            r"^([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eEdD][-+]?\d+)?)",
            raw,
        )
        if not match:
            raise ValueError(f"not a scalar value: {value}")
        return float(match.group(1).replace("D", "E").replace("d", "e"))


def _length_number_with_optional_units(value: str) -> float:
    """Read a scalar length and normalize explicit units to model millimetres."""
    raw = _strip_value_wrappers(value)
    number = _number_with_optional_units(raw)
    suffix_match = re.match(
        r"^[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eEdD][-+]?\d+)?\s*([A-Za-z]+)?$",
        raw,
    )
    if not suffix_match:
        raise ValueError("not a scalar length: {}".format(value))
    unit = (suffix_match.group(1) or "").lower()
    if unit in ("", "mm", "millimeter", "millimeters"):
        return number
    if unit in ("inch", "inches", "in"):
        return number * 25.4
    if unit in ("meter", "meters", "metre", "metres", "m"):
        return number * 1000.0
    raise ValueError("unsupported length unit: {}".format(unit))


def _tuple_code_with_optional_units(value: str) -> str:
    values = [_number_with_optional_units(part)
              for part in _split_top_level_args(value)]
    return "({})".format(", ".join(repr(number) for number in values))


def _ude_var_number(state: ConverterState, instance: str, key: str, default: float = 0.0) -> float:
    raw = _ude_var_text(state, instance, key, "")
    if not raw:
        return default
    try:
        return _number_with_optional_units(raw)
    except Exception:
        return default


def _normalize_object_ref(value: str) -> str:
    return _strip_value_wrappers(value)


def _road_instance_for_tire(state: ConverterState, tire_full: str) -> str:
    # Preferred source: road_name = (.MODEL.roadUDE)
    road_ref = _ude_var_text(state, tire_full, "road_name", "")
    if road_ref.startswith("."):
        return road_ref

    # Fallback: road_property_file = (.MODEL.roadUDE.road_property_file)
    file_ref = _ude_var_text(state, tire_full, "road_property_file", "")
    suffix = ".road_property_file"
    if file_ref.startswith(".") and file_ref.endswith(suffix):
        return file_ref[:-len(suffix)]
    return ""


def _point_location_tuple(meta: Dict[str, object]) -> Optional[Tuple[float, float, float]]:
    raw = meta.get("location")
    if isinstance(raw, (tuple, list)) and len(raw) == 3:
        try:
            return (float(raw[0]), float(raw[1]), float(raw[2]))
        except Exception:
            return None
    if isinstance(raw, str):
        try:
            vals = _vector(raw)
            if len(vals) == 3:
                return (vals[0], vals[1], vals[2])
        except Exception:
            return None
    return None


def _find_tire_center_point(state: ConverterState, instance_meta: Dict[str, object]) -> str:
    raw = instance_meta.get("location")
    try:
        target = tuple(_vector(str(raw)))
    except Exception:
        return ""
    if len(target) != 3:
        return ""

    candidates = []
    for full, meta in state.entity_meta.items():
        if meta.get("kind") != "Point":
            continue
        loc = _point_location_tuple(meta)
        if not loc:
            continue
        err = sum((loc[i] - target[i]) ** 2 for i in range(3))
        candidates.append((err, full))

    if not candidates:
        return ""
    candidates.sort(key=lambda x: x[0])
    # Coordinates in the supplied models are decimal mm.  This tolerance is
    # intentionally small so an unrelated point is never selected by accident.
    if candidates[0][0] <= 1e-8:
        return candidates[0][1]
    return ""


def _road_parent_part(state: ConverterState, road_full: str) -> str:
    ref = _ude_var_text(state, road_full, "ref_marker", "")
    ref = _normalize_object_ref(ref)
    if ref.startswith(".") and "." in ref[1:]:
        return ref.rsplit(".", 1)[0]
    model_prefix = f".{state.model_name}" if state.model_name else ""
    return f"{model_prefix}.ground"


def _ensure_tire_runtime(out: List[str], state: ConverterState) -> None:
    if not state.tire_imports_emitted:
        out.append("\n# ---- TireCMD support (converted from Adams/Car vpg_tire/vpg_road UDE) ----\n")
        out.append("import os\n")
        out.append("from FmbsShortcut.import_all_node import MakeSceneNodeByType as SCMakeSceneNodeByType\n")
        out.append("import FmbsShortcut.SCcmd.TireCMD as TireCMD\n")
        out.append("_MODEL_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\n")
        out.append(
            "_MODEL_RESOURCE_DIR = os.path.join("
            "_MODEL_SCRIPT_DIR, 'resources', "
            "os.path.splitext(os.path.basename(__file__))[0])\n"
        )
        out.append("scene = Jusme.ActiveUSScene\n")
        state.tire_imports_emitted = True
    if not state.tire_defaults_emitted:
        out.append("tire_defaults_units = MakeSceneNodeByType('DefaultsUnits', 'defaultsunits')\n")
        out.append("tire_defaults_units.length = 'Millimeter'\n")
        state.tire_defaults_emitted = True


def _emit_torsion_spring_from_ude(out: List[str], state: ConverterState,
                                  report: ConversionReport,
                                  instance: str) -> bool:
    """Rebuild an Adams ``torsion_spring`` UDE as ForceRotSpringDamper."""
    meta = state.ude_instances.get(instance)
    if not meta or meta.get("kind") != "torsion_spring":
        return False
    if meta.get("emitted"):
        return True

    i_marker = _normalize_object_ref(_ude_var_text(state, instance, "i_marker"))
    j_marker = _normalize_object_ref(_ude_var_text(state, instance, "j_marker"))
    if not i_marker or not j_marker:
        report.warnings.append(
            f"cannot resolve torsion spring markers for {instance}: "
            f"i_marker={i_marker!r}, j_marker={j_marker!r}"
        )
        return True

    i_marker = _apply_path_alias(state, i_marker)
    j_marker = _apply_path_alias(state, j_marker)
    name = getElementName(instance)

    out.append(f"{name} = MakeSceneNodeByType('ForceRotSpringDamper', '{instance}')\n")
    out.append(
        f"{name}.damping = "
        f"{_ude_var_number(state, instance, 'damping_coefficient', 0.0)!r}\n"
    )
    out.append(
        f"{name}.stiffness = "
        f"{_ude_var_number(state, instance, 'stiffness_coefficient', 0.0)!r}\n"
    )
    out.append(
        f"{name}.preload = "
        f"{_ude_var_number(state, instance, 'preload', 0.0)!r}\n"
    )
    # Adams calls the reference rotation ``free_angle``; the corresponding
    # Jusme property is ``displacement_at_preload``.
    out.append(
        f"{name}.displacement_at_preload = "
        f"{_ude_var_number(state, instance, 'free_angle', 0.0)!r}\n"
    )
    out.append(f"{name}.position_define_opt = 1\n")
    out.append(
        f"{name}.i_marker_name = "
        f"Jusme.ActiveUSScene.getObject('{i_marker}')\n"
    )
    out.append(
        f"{name}.j_marker_name = "
        f"Jusme.ActiveUSScene.getObject('{j_marker}')\n"
    )
    out.extend(["\n", "\n"])

    meta["emitted"] = True
    state.known_entities[instance] = "ForceRotSpringDamper"
    state.entity_meta[instance] = {
        "kind": "ForceRotSpringDamper",
        "i_marker_name": i_marker,
        "j_marker_name": j_marker,
    }
    return True


def _emit_trans_spring_from_ude(out: List[str], state: ConverterState,
                                report: ConversionReport,
                                instance: str) -> bool:
    """Rebuild an Adams ``spring`` UDE as ForceTransSpringDamper."""
    meta = state.ude_instances.get(instance)
    if not meta or meta.get("kind") != "trans_spring":
        return False
    if meta.get("emitted"):
        return True

    i_marker = _normalize_object_ref(_ude_var_text(state, instance, "i_marker"))
    j_marker = _normalize_object_ref(_ude_var_text(state, instance, "j_marker"))
    if not i_marker or not j_marker:
        report.warnings.append(
            f"cannot resolve translational spring markers for {instance}: "
            f"i_marker={i_marker!r}, j_marker={j_marker!r}"
        )
        return True

    i_marker = _apply_path_alias(state, i_marker)
    j_marker = _apply_path_alias(state, j_marker)
    name = getElementName(instance)

    out.append(
        f"{name} = MakeSceneNodeByType('ForceTransSpringDamper', "
        f"'{instance}')\n"
    )
    out.append(
        f"{name}.damping = "
        f"{_ude_var_number(state, instance, 'damping_coefficient', 0.0)!r}\n"
    )
    out.append(
        f"{name}.stiffness = "
        f"{_ude_var_number(state, instance, 'stiffness_coefficient', 0.0)!r}\n"
    )
    # Adams calls the reference distance ``free_length``.
    out.append(
        f"{name}.displacement_at_preload = "
        f"{_ude_var_number(state, instance, 'free_length', 0.0)!r}\n"
    )
    out.append(f"{name}.position_define_opt = 1\n")
    out.append(
        f"{name}.i_marker_name = "
        f"Jusme.ActiveUSScene.getObject('{i_marker}')\n"
    )
    out.append(
        f"{name}.j_marker_name = "
        f"Jusme.ActiveUSScene.getObject('{j_marker}')\n"
    )
    out.extend(["\n", "\n"])

    meta["emitted"] = True
    state.known_entities[instance] = "ForceTransSpringDamper"
    state.entity_meta[instance] = {
        "kind": "ForceTransSpringDamper",
        "i_marker_name": i_marker,
        "j_marker_name": j_marker,
    }
    return True


def _emit_marker_create_fields(out: List[str], f: Dict[str, str], state: ConverterState) -> None:
    full = _apply_path_alias(state, f.get("marker_name", ""))
    name = getElementName(full)
    out.append(f"{name} = MakeSceneNodeByType('Marker', '{full}')\n")
    out.append(f"{name}.marker_name = '{full}'\n")
    if "adams_id" in f:
        out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
    if "comments" in f:
        out.append(f"{name}.comments = '{f['comments']}'\n")
    if "location" in f:
        out.append(f"{name}.location = {_vector_code(f['location'])}\n")
    if "orientation" in f:
        out.append(f"{name}.orientation = {_vector_code(f['orientation'], True)}\n")


def _flush_pending_road_markers(out: List[str], state: ConverterState, road_full: str) -> None:
    pending = state.pending_road_markers.pop(road_full, [])
    for fields in pending:
        _emit_marker_create_fields(out, fields, state)
        out.append("\n")


def _emit_tire_from_ude(out: List[str], state: ConverterState, report: ConversionReport,
                        tire_full: str) -> bool:
    meta = state.ude_instances.get(tire_full)
    if not meta or meta.get("kind") != "tire":
        return False
    if meta.get("emitted"):
        return True

    # Wait until the meaningful tire fields have arrived. Adams exports can
    # contain repeated "ude modify instance" blocks.
    tire_file = _ude_var_text(state, tire_full, "property_file", "")
    if not tire_file:
        return True

    road_full = _road_instance_for_tire(state, tire_full)
    road_meta = state.ude_instances.get(road_full, {}) if road_full else {}
    if road_full and road_meta.get("kind") == "road":
        road_name = _allocate_road_name(state, road_full)
        road_file = _ude_var_text(state, road_full, "road_property_file", "")
    else:
        road_name = "road"
        road_file = _ude_var_text(state, tire_full, "road_property_file", "")
        if road_file.startswith("."):
            report.warnings.append(
                f"cannot resolve road_property_file reference for {tire_full}: {road_file}"
            )
            road_file = ""

    _ensure_tire_runtime(out, state)
    state.tire_counter += 1
    input_name = f"Tire_input_{state.tire_counter}"
    tire_name = getElementName(tire_full)

    out.append(f"\n# Tire converted from {tire_full}\n")
    out.append(f"parameter = SCMakeSceneNodeByType('Tire', '{input_name}')\n")
    out.append(f"parameter.tire_name = '{tire_name}'\n")
    out.append(f"parameter.tire_file_path = {_py_resource_path(tire_file, report)}\n")
    if road_file:
        out.append(f"parameter.road_file_path = {_py_resource_path(road_file, report)}\n")

    out.append(f"parameter.mass = {_ude_var_number(state, tire_full, 'wheel_tire_mass', 0.0)!r}\n")
    out.append(f"parameter.lxx_lyy = {_ude_var_number(state, tire_full, 'lxx_lyy', 0.0)!r}\n")
    out.append(f"parameter.Izz = {_ude_var_number(state, tire_full, 'Izz', 0.0)!r}\n")
    out.append("parameter.tire_center_direction_opt = 0\n")

    orientation = str(meta.get("orientation", "0, 0, 0"))
    try:
        tire_angles = _vector(orientation, True)
        out.append("parameter.tire_euler_angles = ({})\n".format(
            ", ".join(repr(v) for v in tire_angles)
        ))
    except Exception:
        report.warnings.append(f"bad tire UDE orientation for {tire_full}: {orientation}")

    center_ref = _find_tire_center_point(state, meta)
    if center_ref:
        out.append(f"center = Jusme.ActiveUSScene.getObject('{center_ref}')\n")
        out.append("parameter.tire_center_location = center.location\n")
    else:
        raw_loc = str(meta.get("location", ""))
        try:
            out.append(f"parameter.tire_center_location = {_vector_code(raw_loc)}\n")
            report.warnings.append(
                f"no matching wheel-center Point found for {tire_full}; using UDE location directly"
            )
        except Exception:
            report.warnings.append(f"cannot determine tire center for {tire_full}")

    # The screenshot method creates the road with the first tire and lets later
    # tires reuse that road through road_opt=1 / road_part.
    if road_full and road_full in state.materialized_roads:
        model_prefix = f".{state.model_name}" if state.model_name else ""
        out.append("parameter.road_opt = 1\n")
        out.append(
            f"parameter.road_part = Jusme.ActiveUSScene.getObject('{model_prefix}.{road_name}')\n"
        )
    else:
        out.append(f"parameter.road_name = '{road_name}'\n")
        out.append("parameter.road_direction_opt = 0\n")
        if road_meta:
            road_orientation = str(road_meta.get("orientation", "0, 0, 0"))
            try:
                angles = _vector(road_orientation, True)
                out.append("parameter.road_euler_angles = ({})\n".format(
                    ", ".join(repr(v) for v in angles)
                ))
            except Exception:
                report.warnings.append(f"bad road UDE orientation for {road_full}: {road_orientation}")
            belong = _road_parent_part(state, road_full)
        else:
            model_prefix = f".{state.model_name}" if state.model_name else ""
            belong = f"{model_prefix}.ground"
        out.append(f"parameter.road_belong_part = Jusme.ActiveUSScene.getObject('{belong}')\n")

    out.append(
        f"parameter.longitudinal_velocites = {_ude_var_number(state, tire_full, 'long_vel', 0.0)!r}\n"
    )
    out.append(
        f"parameter.spin_velocites = {_ude_var_number(state, tire_full, 'spin_vel', 0.0)!r}\n"
    )
    out.append(f"TireCMD.run_test('{input_name}')\n")

    meta["emitted"] = True
    if road_full:
        first_materialization = road_full not in state.materialized_roads
        state.materialized_roads.add(road_full)
        if first_materialization:
            # A road marker may occur in the CMD before the tire UDE is finalized.
            # TireCMD creates the new top-level road, so emit those markers now.
            _flush_pending_road_markers(out, state, road_full)
    out.append("\n")
    return True


def _direct_ude_pose_value(state: ConverterState, expr: str, which: str) -> str:
    """Resolve (.MODEL.roadUDE.location/orientation) from its UDE create block."""
    e = _strip_outer_parens(expr)
    suffix = "." + which
    if e.endswith(suffix):
        inst = e[:-len(suffix)]
        meta = state.ude_instances.get(inst)
        if meta and meta.get("kind") == "road":
            return str(meta.get(which, ""))
    return ""


def _emit_block(block: List[str], out: List[str], state: ConverterState, report: ConversionReport) -> bool:
    cmd = _clean_line(block[0]).lower()
    f = _parse_fields(block)

    # -------- units/model/data --------
    if cmd.startswith("defaults units"):
        if not state.units_created:
            units_model_name = state.model_name or "MODEL"
            units_full_name = ".{}.UNITS_1".format(units_model_name)
            out.append(
                "UNITS_1 = MakeSceneNodeByType('DefaultsUnits', '{}')\n".format(
                    units_full_name
                )
            )
            state.units_created = True
        if "length" in f:
            # Current references use length_opt=0 for mm.
            if f["length"].lower() == "mm":
                out.append("UNITS_1.length_opt = 0\n")
            out.append(f"UNITS_1.length = '{f['length']}'\n")
        for k in ("angle", "force", "mass", "time", "coordinate_system_type", "orientation_type"):
            if k in f:
                out.append(f"UNITS_1.{k} = '{f[k]}'\n")
        return True

    if cmd.startswith("model create"):
        state.model_name = _normalize_model_name(
            f.get("model_name", state.model_name)
        )
        return True

    if cmd.startswith("data_element create variable"):
        full = f.get("variable_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('DataElementVariable', '{full}')\n")
        out.append(f"{name}.variable_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        if "comments" in f: out.append(f"{name}.comments = '{f['comments']}'\n")
        if "initial_condition" in f: out.append(f"{name}.initial_condition = {_num(f['initial_condition'])}\n")
        if "function_opt" in f: out.append(f"{name}.function_opt = {_int(f['function_opt'])}\n")
        if "initial_condition_opt" in f: out.append(f"{name}.initial_condition_opt = {_int(f['initial_condition_opt'])}\n")
        if "function" in f: out.append(f"{name}.function = '{f['function']}'\n")
        return True

    if cmd.startswith("data_element create spline"):
        full = f.get("spline_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('Spline', '{full}')\n")
        out.append(f"{name}.spline_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        if "comments" in f: out.append(f"{name}.comments = '{f['comments']}'\n")
        for k in ("x", "y", "z"):
            if k in f: out.append(f"{name}.{k} = {_num_list(f[k])!r}\n")
        if "input_method_opt" in f:
            out.append(f"{name}.input_method_opt = {_int(f['input_method_opt'])}\n")
        if "linear_extrapolate" in f:
            val = "True" if f["linear_extrapolate"].lower() in ("yes", "on", "true", "1") else "False"
            out.append(f"{name}.linear_extrapolate = {val}\n")
        for k in ("x_units", "y_units", "z_units"):
            if k in f: out.append(f"{name}.{k} = '{f[k]}'\n")
        return True

    if cmd.startswith("material create"):
        full = f.get("material_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('MaterialCreate', '{full}')\n")
        out.append(f"{name}.material_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        for k in ("density", "youngs_modulus", "poissons_ratio"):
            if k in f: out.append(f"{name}.{k} = {_num(f[k])}\n")
        return True

    if cmd.startswith("defaults model"):
        part = f.get("part_name", "ground")
        full = f".{state.model_name}.{part}" if state.model_name else part
        out.append(f"{getElementName(part)} = Jusme.ActiveUSScene.getObject('{full}')\n")
        out.append(f"{getElementName(part)}.part_name = '{part}'\n")
        return True

    # -------- geometry/nodes --------
    if cmd.startswith("marker create"):
        full_original = f.get("marker_name", "")
        # vpg_road internally owns <roadUDE>.road_part.  TireCMD recreates this
        # as a top-level road object, so defer markers until that road exists and
        # remap the parent path.
        for road_full, meta in state.ude_instances.items():
            if meta.get("kind") != "road":
                continue
            prefix = road_full + ".road_part."
            if full_original.startswith(prefix):
                _allocate_road_name(state, road_full)
                if road_full not in state.materialized_roads:
                    state.pending_road_markers.setdefault(road_full, []).append(dict(f))
                    return True
                break

        _emit_marker_create_fields(out, f, state)
        full = _apply_path_alias(state, full_original)
        state.known_entities[full] = "Marker"
        if "location" in f:
            try:
                state.entity_meta[full] = {
                    "kind": "Marker",
                    "location": tuple(_vector(f["location"])),
                }
            except Exception:
                pass
        return True

    if cmd.startswith("floating_marker create"):
        full = f.get("floating_marker_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('Marker', '{full}')\n")
        out.append(f"{name}.is_floating = True\n")
        out.append(f"{name}.floating_marker_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        return True

    if cmd.startswith("point create"):
        full = f.get("point_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('Point', '{full}')\n")
        out.append(f"{name}.point_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        if "location" in f: out.append(f"{name}.location = {_vector_code(f['location'])}\n")
        state.known_entities[full] = "Point"
        meta: Dict[str, object] = {"kind": "Point"}
        if "location" in f:
            try:
                meta["location"] = tuple(_vector(f["location"]))
            except Exception:
                meta["location"] = f["location"]
        state.entity_meta[full] = meta
        return True

    if cmd.startswith("part create rigid_body name_and_position"):
        full = f.get("part_name", "")
        name = getElementName(full)
        state.known_entities[full] = "PartGeneral"
        out.append(f"{name} = MakeSceneNodeByType('PartGeneral', '{full}')\n")
        out.append(f"{name}.part_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        if "comments" in f: out.append(f"{name}.comments = '{f['comments']}'\n")
        if "location" in f: out.append(f"{name}.location = {_vector_code(f['location'])}\n")
        if "orientation" in f: out.append(f"{name}.orientation = {_vector_code(f['orientation'], True)}\n")
        return True

    if cmd.startswith("part create rigid_body mass_properties"):
        full = f.get("part_name", "")
        name = getElementName(full)
        out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
        if f.get("center_of_mass_marker"):
            out.append(f"center_of_mass_marker = Jusme.ActiveUSScene.getObject('{f['center_of_mass_marker']}')\n")
            out.append(f"{name}.center_of_mass_marker = center_of_mass_marker\n")
        if f.get("inertia_marker"):
            out.append(f"inertia_marker = Jusme.ActiveUSScene.getObject('{f['inertia_marker']}')\n")
            out.append(f"{name}.inertia_marker = inertia_marker\n")
        out.append(f"{name}.part_name = '{full}'\n")
        for k in ("mass", "ixx", "iyy", "izz", "ixy", "izx", "iyz"):
            if k in f: out.append(f"{name}.{k} = {_num(f[k])}\n")
        return True

    if cmd.startswith("geometry create shape cylinder"):
        full = f.get("cylinder_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('ShapeCylinder', '{full}')\n")
        if f.get("center_marker"):
            out.append(f"center_marker = Jusme.ActiveUSScene.getObject('{f['center_marker']}')\n")
            out.append(f"{name}.center_marker = center_marker\n")
        out.append(f"{name}.cylinder_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        for k in ("angle_extent", "length", "radius"):
            if k in f: out.append(f"{name}.{k} = {_num(f[k])}\n")
        for k in ("side_count_for_body", "segment_count_for_ends"):
            if k in f: out.append(f"{name}.{k} = {_int(f[k])}\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("geometry create shape block"):
        return _emit_shape_block(out, f, state, report)

    if cmd.startswith("geometry create shape plate"):
        _emit_shape_plate(out, f)
        return True

    if cmd.startswith("geometry create curve outline"):
        full = f.get("outline_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('CurveOutline', '{full}')\n")
        out.append(f"# >>>[ERROR] CAN NOT find link prop(marker_name) from {full}, Please DOUBLE CHECK!\n")
        out.append(f"# >>>[ERROR] CAN NOT find link prop(visibility_between_markers) from {full}, Please DOUBLE CHECK!\n")
        out.append(f"{name}.outline_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        if "close" in f: out.append(f"{name}.close = '{f['close']}'\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("geometry create shape ellipsoid"):
        full = f.get("ellipsoid_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('ShapeEllipsoid', '{full}')\n")
        if f.get("center_marker"):
            out.append(f"center_marker = Jusme.ActiveUSScene.getObject('{f['center_marker']}')\n")
            out.append(f"{name}.center_marker = center_marker\n")
        out.append(f"{name}.ellipsoid_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        for k in ("x_scale_factor", "y_scale_factor", "z_scale_factor"):
            if k in f: out.append(f"{name}.{k} = {_num(f[k])}\n")
        out.extend(["\n", "\n"])
        return True

    # -------- Adams/Car road/tire UDEs --------
    if cmd.startswith("ude create instance"):
        full = f.get("instance_name", "")
        kind = _ude_definition_kind(f.get("definition_name", ""))
        if not kind:
            return False
        state.ude_instances[full] = {
            "kind": kind,
            "definition_name": f.get("definition_name", ""),
            "location": f.get("location", "0, 0, 0"),
            "orientation": f.get("orientation", "0, 0, 0"),
            "variables": {},
            "attributes": {},
            "emitted": False,
        }
        if kind == "road":
            _allocate_road_name(state, full)
        return True

    if cmd.startswith("ude attributes"):
        full = f.get("instance_name", "")
        meta = state.ude_instances.get(full)
        if not meta:
            return False
        attrs = meta.setdefault("attributes", {})
        if isinstance(attrs, dict):
            for key, value in f.items():
                if key != "instance_name":
                    attrs[key] = value
        return True

    if cmd.startswith("variable modify"):
        var_full = f.get("variable_name", "")
        inst, key = _find_ude_for_variable(state, var_full)
        if not inst:
            return False
        meta = state.ude_instances[inst]
        vars_map = meta.setdefault("variables", {})
        value_key = ""
        for candidate in ("real_value", "integer_value", "string_value", "object_value"):
            if candidate in f:
                value_key = candidate
                break
        if isinstance(vars_map, dict):
            vars_map[key] = {
                "kind": value_key,
                "value": f.get(value_key, ""),
            }
        return True

    if cmd.startswith("ude modify instance"):
        full = f.get("instance_name", "")
        meta = state.ude_instances.get(full)
        if not meta:
            return False
        if meta.get("kind") == "torsion_spring":
            return _emit_torsion_spring_from_ude(out, state, report, full)
        if meta.get("kind") == "trans_spring":
            return _emit_trans_spring_from_ude(out, state, report, full)
        if meta.get("kind") == "road":
            # The screenshot workflow creates the road as part of the first
            # TireCMD.run_test() call, not as an independent UDE node.
            return True
        if meta.get("kind") == "tire":
            return _emit_tire_from_ude(out, state, report, full)
        return False

    # -------- equations / constraints / forces --------
    if cmd.startswith("part create equation differential_equation"):
        full = f.get("differential_equation_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('PartDifferentialEquation', '{full}')\n")
        out.append(f"{name}.differential_equation_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        if "comments" in f: out.append(f"{name}.comments = '{f['comments']}'\n")
        if "function" in f: out.append(f"{name}.function = '{f['function']}'\n")
        if "initial_condition" in f: out.append(f"{name}.initial_condition = {_num(f['initial_condition'])}\n")
        if "implicit" in f:
            v = f["implicit"].lower() in ("yes", "on", "true", "1")
            out.append(f"{name}.implicit = {v}\n")
        if "static_hold" in f:
            v = f["static_hold"].lower() in ("yes", "on", "true", "1")
            out.append(f"{name}.static_hold = {v}\n")
        out.extend(["\n", "\n", "\n", "\n"])
        return True

    if cmd.startswith("constraint create joint") or cmd.startswith("constraint create primitive_joint"):
        token = cmd.split()[-1]
        node_type = JOINT_NODE_TYPES.get(token)
        if not node_type:
            return False
        primitive = "primitive_joint" in cmd
        key = "jprim_name" if primitive else "joint_name"
        full = f.get(key, "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('{node_type}', '{full}')\n")
        for mk in ("i_marker_name", "j_marker_name"):
            if f.get(mk):
                mk_full = _apply_path_alias(state, f[mk])
                out.append(f"{mk} = Jusme.ActiveUSScene.getObject('{mk_full}')\n")
                out.append(f"{name}.{mk} = {mk}\n")
        out.append(f"{name}.{key} = '{full}'\n")
        state.known_entities[full] = node_type
        state.entity_meta[full] = {
            "kind": node_type,
            "i_marker_name": f.get("i_marker_name", ""),
            "j_marker_name": f.get("j_marker_name", ""),
        }
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        if "comments" in f: out.append(f"{name}.comments = '{f['comments']}'\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("force create direct general_force"):
        _emit_force_general_create(out, f, state)
        return True

    if cmd.startswith("contact create"):
        return _emit_contact(out, f, state, report)

    if cmd.startswith("force create direct") and "single_component" in cmd:
        _emit_force_single_component(out, f, state)
        return True

    if cmd.startswith("force create element_like field"):
        _emit_force_field(out, f)
        return True

    if cmd.startswith("force create body gravitational"):
        field_name = f.get("gravity_field_name", "gravity").strip()
        full = f".{state.model_name}.{field_name}" if state.model_name else field_name
        name = getElementName(field_name)
        out.append(f"{name} = MakeSceneNodeByType('Gravity', '{full}')\n")
        out.append(f"{name}.gravity_field_name = '{field_name}'\n")
        for k in ("x_component_gravity", "y_component_gravity", "z_component_gravity"):
            if k in f: out.append(f"{name}.{k} = {_num(f[k])}\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("simulation script create"):
        full = f.get("sim_script_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('SimuScript', '{full}')\n")
        out.append(f"{name}.sim_script_name = '{full}'\n")
        if "commands" in f: out.append(f"{name}.commands = '{f['commands']}'\n")
        return True

    if cmd.startswith("constraint create motion_generator"):
        full = f.get("motion_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('JointMotion', '{full}')\n")
        if f.get("joint_name"):
            out.append(f"joint_name = Jusme.ActiveUSScene.getObject('{f['joint_name']}')\n")
            out.append(f"{name}.joint_name = joint_name\n")
        out.append(f"{name}.motion_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        if "comments" in f: out.append(f"{name}.comments = '{f['comments']}'\n")
        if "type_of_freedom" in f:
            tof = f["type_of_freedom"].strip().lower()
            # Direct CMD->PY references encode rotational as 1; the supplied
            # Assembly motion code uses 0 for translational.
            mapping = {"translational": 0, "rotational": 1}
            val = mapping.get(tof, int(float(tof)) if re.fullmatch(r"[-+]?\d+(?:\.\d+)?", tof) else 1)
            out.append(f"{name}.type_of_freedom = {val}\n")
        if "function" in f: out.append(f"{name}.function = '{f['function']}'\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("measure create object"):
        return _emit_measure_object(out, f, state, report, cmd)

    if cmd.startswith("measure create function"):
        _emit_function_measure(out, f)
        return True

    if cmd.startswith("measure create point"):
        return _emit_point_measure(out, f, state, report, cmd)

    if cmd.startswith("measure create pt2pt"):
        full = f.get("measure_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('Pt2pt', '{full}')\n")
        for k in ("from_point", "to_point"):
            if f.get(k):
                out.append(f"{k} = Jusme.ActiveUSScene.getObject('{f[k]}')\n")
                out.append(f"{name}.{k} = {k}\n")
        out.append(f"{name}.measure_name = '{full}'\n")
        for k in ("characteristic", "component"):
            if k in f: out.append(f"{name}.{k} = '{f[k]}'\n")
        if "create_measure_display" in f:
            out.append(f"# >>>[ERROR] CAN NOT find prop(create_measure_display) from {full}'s PropertiesList, Please DOUBLE CHECK!\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("variable create"):
        full = f.get("variable_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('DesignVariable', '{full}')\n")
        out.append(f"{name}.variable_name = '{full}'\n")
        if "string_value" in f:
            out.append(f"{name}.value_type_opt = 2\n")
            out.append(f"{name}.string_value = '{f['string_value']}'\n")
        elif "integer_value" in f:
            # Integer-valued DesignVariable pattern used by gcmb6_motion.layout_config.
            out.append(f"{name}.value_type_opt = 1\n")
            out.append(f"{name}.integer_value = {_int(f['integer_value'])}\n")
            if "use_allowed_values" in f:
                b = f["use_allowed_values"].lower() in ("yes", "on", "true", "1")
                out.append(f"{name}.use_allowed_values = {b}\n")
        elif "real_value" in f:
            if "units" in f: out.append(f"{name}.units = '{f['units']}'\n")
            if "range" in f:
                r = [x.strip().lower() for x in f["range"].split(",")]
                out.append(f"{name}.range = [{', '.join(r)}]\n")
                out.append(f"{name}.use_range = True\n")
            if "use_allowed_values" in f:
                b = f["use_allowed_values"].lower() in ("yes", "on", "true", "1")
                out.append(f"{name}.use_allowed_values = {b}\n")
            if f.get("delta_type", "").lower() == "relative": out.append(f"{name}.delta_type = 0\n")
            out.append(f"{name}.value_type_opt = 0\n")
            out.append(f"{name}.real_value = {_num(f['real_value'])}\n")
        out.extend(["\n", "\n"])
        return True

    # -------- modifies --------
    if cmd.startswith("force modify direct general_force"):
        _emit_force_general_modify(out, f)
        return True

    # Some Adams exports create a single-component force with an empty
    # function and assign the real expression later in a MODIFY block.
    if cmd.startswith("force modify direct") and "single_component" in cmd:
        _emit_force_single_component_modify(out, f)
        return True

    if cmd.startswith("marker modify"):
        f2 = dict(f)
        if f2.get("location"):
            resolved = _direct_ude_pose_value(state, f2["location"], "location")
            if resolved:
                f2["location"] = resolved
        if f2.get("orientation"):
            resolved = _direct_ude_pose_value(state, f2["orientation"], "orientation")
            if resolved:
                f2["orientation"] = resolved
        _emit_marker_modify(out, f2, report)
        return True

    if cmd.startswith("part modify rigid_body name_and_position"):
        _emit_part_modify(out, f, report)
        return True

    if cmd.startswith("material modify"):
        full = f.get("material_name", "")
        name = getElementName(full)
        out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
        out.append(f"{name}.material_name = '{full}'\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("geometry modify shape block"):
        return _emit_shape_block(out, f, state, report, modify=True)

    if cmd.startswith("geometry modify shape ellipsoid"):
        full = f.get("ellipsoid_name", "")
        name = getElementName(full)
        out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
        out.append(f"{name}.ellipsoid_name = '{full}'\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("geometry modify shape cylinder"):
        full = f.get("cylinder_name", "")
        name = getElementName(full)
        out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
        out.append(f"{name}.cylinder_name = '{full}'\n")
        if "length" in f:
            if not _emit_dm_length_expr(out, name, f["length"]):
                report.warnings.append(f"unsupported cylinder length expression for {full}: {f['length']}")
        if "radius" in f:
            radius_text = _strip_outer_parens(f["radius"]).strip()
            # Adams may re-state a scalar model-unit value as ``27.5mm`` or
            # ``2.2E-02meter``.  The model's DefaultsUnits node already owns
            # the unit system, so only the numeric portion is assigned here.
            try:
                radius_value = _number_with_optional_units(radius_text)
                out.append(f"{name}.radius = {radius_value!r}\n")
            except ValueError:
                report.warnings.append(f"unsupported cylinder radius expression for {full}: {f['radius']}")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("constraint modify motion_generator"):
        full = f.get("motion_name", "")
        name = getElementName(full)
        out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
        out.append(f"{name}.motion_name = '{full}'\n")
        if "function" in f: out.append(f"{name}.function = '{f['function']}'\n")
        out.append("\n")
        return True

    if cmd.startswith("data_element modify variable"):
        full = f.get("variable_name", "")
        name = getElementName(full)
        out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
        out.append(f"{name}.variable_name = '{full}'\n")
        if "function" in f: out.append(f"{name}.function = '{f['function']}'\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("part modify equation differential_equation"):
        full = f.get("differential_equation_name", "")
        name = getElementName(full)
        out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
        out.append(f"{name}.differential_equation_name = '{full}'\n")
        if "function" in f: out.append(f"{name}.function = '{f['function']}'\n")
        out.extend(["\n", "\n"])
        return True

    if cmd.startswith("measure modify function"):
        full = f.get("measure_name", "")
        name = getElementName(full)
        out.append(f"{name} = Jusme.ActiveUSScene.getObject('{full}')\n")
        if "function" in f:
            out.append(f"{name}.function = '{f['function']}'\n")
        out.append("\n")
        return True

    if cmd.startswith("part modify rigid_body initial_velocity"):
        full = f.get("part_name", "")
        # For vpg_tire-generated wheel/belt parts the screenshot's TireCMD
        # parameters own the initial longitudinal/spin velocity setup.  The CMD
        # vm/wm blocks only select IC reference markers, so preserve them as a
        # note rather than guessing unsupported Part properties.
        if any(full.startswith(inst + ".") and meta.get("kind") == "tire"
               for inst, meta in state.ude_instances.items()):
            out.append(
                f"# TireCMD handles initial-velocity reference for {full}"
                f" (vm={f.get('vm', '')}, wm={f.get('wm', '')})\n"
            )
            return True

    return False


def pharseBlocks(blocks: List[List[str]], out_put: List[str], *, report: Optional[ConversionReport] = None,
                 state: Optional[ConverterState] = None) -> ConversionReport:
    """Compatibility entry point matching the legacy misspelled API name."""
    if report is None:
        report = ConversionReport()
    if state is None:
        state = _legacy_state
    if not state.model_name:
        state.model_name = _find_model_name(blocks)

    for block in blocks:
        if not block:
            continue
        report.total_blocks += 1
        cmd = _clean_line(block[0]).lower()

        if any(cmd.startswith(prefix) for prefix in IGNORED_PREFIXES):
            report.ignored_blocks[cmd] += 1
            continue

        try:
            handled = _emit_block(block, out_put, state, report)
        except Exception as exc:
            handled = False
            report.warnings.append(f"{cmd}: {type(exc).__name__}: {exc}")

        if handled:
            report.converted_blocks += 1
        else:
            report.unsupported_blocks[cmd] += 1
            out_put.append(f"# [CMD2PY WARNING] Unsupported CMD block: {cmd}\n")

    return report


def convert_text(cmd_text: str, *, include_header: bool = True) -> Tuple[str, ConversionReport]:
    out: List[str] = HEADER.copy() if include_header else []
    # File conversions must be isolated from prior runs.
    report = pharseBlocks(gen_blocks(cmd_text.splitlines()), out, state=ConverterState())
    return "".join(out), report


PATCH_COMMAND_PREFIXES = (
    "data_element create variable",
    "data_element modify variable",
    "part modify equation differential_equation",
    "measure modify function",
    "constraint modify motion_generator",
    "part modify rigid_body name_and_position",
    "force modify direct general_force",
    "force modify direct single_component_force",
    "marker modify",
    "geometry modify shape cylinder",
    "simulation script create",
)


def _unquote_cmd_string(value: str) -> str:
    """Remove one Adams quote wrapper from a function/string field."""
    text = value.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in ("'", '"'):
        return text[1:-1]
    return text


def _append_indented(out: List[str], lines: Iterable[str], level: int = 1) -> None:
    prefix = "    " * level
    for line in lines:
        if line.strip():
            out.append(prefix + line)
        else:
            out.append(line)


def _patch_adm_ude_kinds(
    blocks: List[List[str]], source_model_name: str
) -> Dict[str, str]:
    """Return root-relative road/tire UDE names flattened by ADM import.

    Adams CMD keeps a UDE hierarchy such as ``lm.road_part`` and
    ``lt_l.wheel_part``.  The Jasmine ADM importer exposes those objects as
    ``lm_road_part`` and ``lt_l_wheel_part`` and does not expose the UDE parent
    itself.  Recording the UDE names lets generated patches resolve either
    representation at runtime.
    """
    source_root = "." + source_model_name
    ude_kinds: Dict[str, str] = {}
    for block in blocks:
        if not block or not _clean_line(block[0]).lower().startswith(
            "ude create instance"
        ):
            continue
        fields = _parse_fields(block)
        instance_name = _strip_value_wrappers(fields.get("instance_name", ""))
        kind = _ude_definition_kind(fields.get("definition_name", ""))
        if kind not in ("road", "tire"):
            continue
        if not instance_name.startswith(source_root + "."):
            continue
        relative_name = instance_name[len(source_root) + 1:]
        if relative_name:
            ude_kinds[relative_name] = kind
    return dict(sorted(ude_kinds.items()))


def _patch_header(
    source_model_name: str, adm_ude_kinds: Optional[Dict[str, str]] = None
) -> List[str]:
    """Return the reusable runtime wrapper for an ADM overlay patch."""
    adm_ude_kinds = dict(adm_ude_kinds or {})
    return [
        "# -*- coding: utf-8 -*-\n",
        '"""Generated ADM overlay patch; do not create the physical model here.\n\n',
        "Generated from the authoritative Adams CMD.  The ADM importer owns parts,\n",
        "markers, constraints, forces and tire solver entities.  This module only\n",
        "restores design expressions and CMD-only data objects.\n",
        '"""\n\n',
        "import os\n",
        "import re\n",
        "import traceback\n",
        "import Jusme\n",
        "from Fmbs.import_all_node import MakeSceneNodeByType\n",
        "import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils\n\n",
        f"SOURCE_MODEL_NAME = {source_model_name!r}\n",
        f"ADM_UDE_KINDS = {adm_ude_kinds!r}\n\n",
        "def apply_patch(model_dir=None, model_name=None):\n",
        "    scene = Jusme.ActiveUSScene\n",
        "    if scene is None:\n",
        "        raise RuntimeError('没有活动模型，无法应用 ADM 补丁')\n",
        "    model_name = model_name or SOURCE_MODEL_NAME\n",
        "    source_root = '.' + SOURCE_MODEL_NAME\n",
        "    target_root = '.' + model_name\n",
        "    warnings = []\n",
        "    errors = []\n",
        "    updated = 0\n\n",
        "    def root_path(path):\n",
        "        if path == source_root or path.startswith(source_root + '.'):\n",
        "            return target_root + path[len(source_root):]\n",
        "        return path\n\n",
        "    def path_candidates(path):\n",
        "        resolved = root_path(path)\n",
        "        candidates = [resolved]\n",
        "        if not (resolved == target_root or resolved.startswith(target_root + '.')):\n",
        "            return candidates\n",
        "        relative = resolved[len(target_root):].lstrip('.')\n",
        "        for instance_name, kind in sorted(ADM_UDE_KINDS.items(), key=lambda item: len(item[0]), reverse=True):\n",
        "            if relative == instance_name:\n",
        "                leaf_name = 'road_part' if kind == 'road' else 'wheel_part'\n",
        "                candidate = target_root + '.' + instance_name.replace('.', '_') + '_' + leaf_name\n",
        "            elif relative.startswith(instance_name + '.'):\n",
        "                tail = relative[len(instance_name) + 1:]\n",
        "                first, separator, remainder = tail.partition('.')\n",
        "                if first in ('road_part', 'wheel_part', 'belt_part'):\n",
        "                    candidate = target_root + '.' + instance_name.replace('.', '_') + '_' + first\n",
        "                    if separator:\n",
        "                        candidate += '.' + remainder\n",
        "                else:\n",
        "                    candidate = target_root + '.' + (instance_name + '.' + tail).replace('.', '_')\n",
        "            else:\n",
        "                continue\n",
        "            if candidate not in candidates:\n",
        "                candidates.append(candidate)\n",
        "        return candidates\n\n",
        "    def target_path(path):\n",
        "        candidates = path_candidates(path)\n",
        "        for candidate in candidates:\n",
        "            if scene.getObject(candidate) is not None:\n",
        "                return candidate\n",
        "        return candidates[0]\n\n",
        "    def rewrite_expression(value):\n",
        "        text = str(value)\n",
        "        text = re.sub(re.escape(source_root), target_root, text, flags=re.I)\n",
        "        return re.sub(r'(?i)\\.GCMB(?=\\.|$)', target_root, text)\n\n",
        "    def rewrite_simulation_command(value):\n",
        "        text = rewrite_expression(value)\n",
        "        return re.sub(\n",
        "            r'(?i)(model_name\\s*=\\s*)\\.[A-Za-z_][A-Za-z0-9_]*',\n",
        "            lambda match: match.group(1) + target_root,\n",
        "            text,\n",
        "        )\n\n",
        "    def get_object(path, required=True):\n",
        "        candidates = path_candidates(path)\n",
        "        node = None\n",
        "        for resolved in candidates:\n",
        "            node = scene.getObject(resolved)\n",
        "            if node is not None:\n",
        "                break\n",
        "        if node is None and required:\n",
        "            raise RuntimeError('ADM 补丁找不到对象：{}'.format(' 或 '.join(candidates)))\n",
        "        return node\n\n",
        "    def get_or_create(node_type, path):\n",
        "        node = get_object(path, required=False)\n",
        "        if node is None:\n",
        "            node = MakeSceneNodeByType(node_type, target_path(path))\n",
        "        return node\n\n",
        "    def set_resource(path, value):\n",
        "        node = get_object(path, required=False)\n",
        "        if node is None:\n",
        "            warnings.append('未找到资源数据节点：{}'.format(target_path(path)))\n",
        "            return False\n",
        "        properties = set(getattr(node, 'PropertiesList', []) or [])\n",
        "        for prop in ('string_value', 'string', 'value'):\n",
        "            if prop in properties or hasattr(node, prop):\n",
        "                setattr(node, prop, value)\n",
        "                return True\n",
        "        warnings.append('资源数据节点没有字符串属性：{}'.format(target_path(path)))\n",
        "        return False\n\n",
        "    def record_error(step, exc):\n",
        "        error_info = {\n",
        "            'step': step,\n",
        "            'error_type': type(exc).__name__,\n",
        "            'error': str(exc),\n",
        "        }\n",
        "        errors.append(error_info)\n",
        "        print('[模型补丁错误] {step}: {error_type}: {error}'.format(**error_info))\n",
        "        trace_text = traceback.format_exc()\n",
        "        if trace_text.strip() != 'NoneType: None':\n",
        "            print(trace_text)\n\n",
    ]


def _is_road_ude_pose_marker(fields: Dict[str, str]) -> bool:
    """Whether a marker pose comes directly from an unimported road UDE."""
    marker_name = fields.get("marker_name", "").lower()
    if ".ground.lumian" not in marker_name:
        return False
    pose_values = (fields.get("location", ""), fields.get("orientation", ""))
    return any(".lumian" in value.lower() for value in pose_values)


def _patch_resource_specs(blocks: List[List[str]]) -> List[Tuple[str, str, str]]:
    """Resolve tire/road files to the ADM string nodes created for each tire."""
    literal_values: Dict[str, str] = {}
    road_values: Dict[str, str] = {}
    tire_files: Dict[str, str] = {}

    for block in blocks:
        if not block or not _clean_line(block[0]).lower().startswith("variable modify"):
            continue
        fields = _parse_fields(block)
        variable_name = fields.get("variable_name", "")
        if not variable_name or "string_value" not in fields:
            continue
        value = _strip_value_wrappers(fields["string_value"])
        literal_values[variable_name] = value
        parent, _, leaf = variable_name.rpartition(".")
        if leaf == "property_file" and value.lower().endswith(".tir"):
            tire_files[parent] = _resource_file_name(value)
        elif leaf == "road_property_file":
            road_values[parent] = value

    specs: List[Tuple[str, str, str]] = []
    for tire_parent, tire_file in tire_files.items():
        specs.append((tire_parent + ".tpf_file", tire_file, "轮胎文件路径"))
        road_value = road_values.get(tire_parent, "")
        referenced_variable = _strip_value_wrappers(road_value)
        if referenced_variable in literal_values:
            road_value = literal_values[referenced_variable]
        road_file = _resource_file_name(road_value)
        if road_file.lower().endswith(".rdf"):
            specs.append((tire_parent + ".rpf_file", road_file, "路面文件路径"))

    # Preserve command order while removing duplicate assignments.
    return list(dict.fromkeys(specs))


def convert_patch_text(cmd_text: str) -> Tuple[str, ConversionReport]:
    """Convert a full CMD into an ADM-safe, idempotent overlay module.

    Only blocks that restore functions/parametric relationships are emitted.
    Physical create blocks stay owned by the ADM importer, and Adams/Car tire
    UDE blocks are intentionally not replayed.
    """
    blocks = gen_blocks(cmd_text.splitlines())
    source_model_name = _find_model_name(blocks) or "template_2_brake"
    state = ConverterState(model_name=source_model_name)
    report = ConversionReport(total_blocks=len(blocks))
    out = _patch_header(
        source_model_name,
        _patch_adm_ude_kinds(blocks, source_model_name),
    )

    for block in blocks:
        if not block:
            continue
        cmd = _clean_line(block[0]).lower()
        fields = _parse_fields(block)

        if not any(cmd.startswith(prefix) for prefix in PATCH_COMMAND_PREFIXES):
            report.ignored_blocks[cmd] += 1
            continue

        # The road reference marker already has its evaluated ADM pose.  Its
        # CMD formula references the high-level UDE instance, which is not
        # recreated after importing the solver-level ADM tire/road entities.
        if cmd.startswith("marker modify") and _is_road_ude_pose_marker(fields):
            report.ignored_blocks["marker modify [road UDE pose retained from ADM]"] += 1
            continue

        emitted: List[str] = []

        if cmd.startswith("data_element create variable"):
            full = fields.get("variable_name", "")
            emitted.append(f"node = get_or_create('DataElementVariable', {full!r})\n")
            emitted.append("if hasattr(node, 'variable_name'):\n")
            emitted.append(f"    node.variable_name = target_path({full!r})\n")
            if "adams_id" in fields:
                emitted.append("if hasattr(node, 'adams_id'):\n")
                emitted.append(f"    node.adams_id = {_int(fields['adams_id'])}\n")
            if "initial_condition" in fields:
                emitted.append("if hasattr(node, 'initial_condition'):\n")
                emitted.append(
                    f"    node.initial_condition = {_num(fields['initial_condition'])}\n"
                )
            emitted.append("updated += 1\n\n")

        elif cmd.startswith("data_element modify variable"):
            full = fields.get("variable_name", "")
            function = _unquote_cmd_string(fields.get("function", ""))
            emitted.extend(
                [
                    f"node = get_object({full!r})\n",
                    f"node.function = rewrite_expression({function!r})\n",
                    "updated += 1\n\n",
                ]
            )

        elif cmd.startswith("force modify direct single_component_force"):
            full = _single_component_force_full_name(fields)
            function = _unquote_cmd_string(fields.get("function", ""))
            emitted.extend(
                [
                    f"node = get_object({full!r})\n",
                    f"node.function = rewrite_expression({function!r})\n",
                    "updated += 1\n\n",
                ]
            )

        elif cmd.startswith("force modify direct general_force"):
            full = fields.get("general_force_name", fields.get("force_name", ""))
            emitted.append(f"node = get_object({full!r})\n")
            for key in (
                "x_force_function", "y_force_function", "z_force_function",
                "x_torque_function", "y_torque_function", "z_torque_function",
            ):
                if key in fields:
                    function = _unquote_cmd_string(fields[key])
                    emitted.append(
                        f"node.{key} = rewrite_expression({function!r})\n"
                    )
            emitted.append("updated += 1\n\n")

        elif cmd.startswith("constraint modify motion_generator"):
            full = fields.get("motion_name", "")
            function = _unquote_cmd_string(fields.get("function", ""))
            emitted.extend(
                [
                    f"node = get_object({full!r})\n",
                    f"node.function = rewrite_expression({function!r})\n",
                    "updated += 1\n\n",
                ]
            )

        elif cmd.startswith("measure modify function"):
            full = fields.get("measure_name", "")
            function = _unquote_cmd_string(fields.get("function", ""))
            emitted.extend(
                [
                    f"node = get_object({full!r})\n",
                    f"node.function = rewrite_expression({function!r})\n",
                    "updated += 1\n\n",
                ]
            )

        elif cmd.startswith("part modify equation differential_equation"):
            full = fields.get("differential_equation_name", "")
            function = _unquote_cmd_string(fields.get("function", ""))
            emitted.extend(
                [
                    f"node = get_object({full!r})\n",
                    f"node.function = rewrite_expression({function!r})\n",
                    "updated += 1\n\n",
                ]
            )

        elif cmd.startswith("simulation script create"):
            full = fields.get("sim_script_name", "")
            commands = _unquote_cmd_string(fields.get("commands", ""))
            emitted.extend(
                [
                    f"node = get_or_create('SimuScript', {full!r})\n",
                    "if hasattr(node, 'sim_script_name'):\n",
                    f"    node.sim_script_name = target_path({full!r})\n",
                    f"node.commands = rewrite_simulation_command({commands!r})\n",
                    "updated += 1\n\n",
                ]
            )

        else:
            # Reuse the verified LOC/ORI/DM translators, but make object lookup
            # resolve the actual imported scene name at runtime.
            _emit_block(block, emitted, state, report)
            normalized: List[str] = []
            for line in emitted:
                line = line.replace("Jusme.ActiveUSScene.getObject(", "get_object(")
                line = re.sub(
                    r"(\.(?:marker_name|cylinder_name|part_name)\s*=\s*)('.*')$",
                    r"\1target_path(\2)",
                    line.rstrip("\n"),
                ) + ("\n" if line.endswith("\n") else "")
                normalized.append(line)
            emitted = normalized
            emitted.append("updated += 1\n\n")

        target = next(
            (
                fields[key]
                for key in (
                    "variable_name",
                    "single_component_force_name",
                    "force_name",
                    "general_force_name",
                    "motion_name",
                    "measure_name",
                    "differential_equation_name",
                    "part_name",
                    "marker_name",
                    "cylinder_name",
                    "sim_script_name",
                )
                if fields.get(key)
            ),
            "",
        )
        step_label = "{} {}".format(cmd, target).strip()
        out.append("    try:\n")
        _append_indented(out, emitted, level=2)
        out.append("    except Exception as exc:\n")
        out.append(f"        record_error({step_label!r}, exc)\n\n")
        report.converted_blocks += 1

    footer = []
    resource_specs = _patch_resource_specs(blocks)
    if resource_specs:
        footer.extend(
            [
                "if model_dir is None:\n",
                "    model_dir = os.path.dirname(os.path.abspath(__file__))\n",
            ]
        )
        for index, (node_path, file_name, label) in enumerate(resource_specs, 1):
            variable = "resource_path_{}".format(index)
            step_label = "{}（{}）".format(label, file_name)
            footer.extend(
                [
                    f"{variable} = os.path.abspath(os.path.join(model_dir, {file_name!r}))\n",
                    f"if not os.path.isfile({variable}):\n",
                    f"    record_error({step_label!r}, FileNotFoundError({variable}))\n",
                    "else:\n",
                    "    try:\n",
                    f"        if set_resource({node_path!r}, {variable}):\n",
                    "            updated += 1\n",
                    "    except Exception as exc:\n",
                    f"        record_error({step_label!r}, exc)\n",
                ]
            )
    footer.append("return {'updated': updated, 'warnings': warnings, 'errors': errors}\n")
    _append_indented(out, footer)
    return "".join(out), report


def convert_patch_file(cmd_path: str | Path, py_path: str | Path,
                       report_path: str | Path | None = None) -> Tuple[Path, ConversionReport]:
    """Generate a checked-in ADM overlay patch beside a template's assets."""
    src = Path(cmd_path)
    dst = Path(py_path)
    py_text, report = convert_patch_text(
        src.read_text(encoding="utf-8", errors="ignore")
    )
    dst.write_text(py_text, encoding="utf-8", newline="\n")
    if report_path is not None:
        Path(report_path).write_text(report.as_text(), encoding="utf-8")
    return dst, report


def _resource_source_candidates(source_text: str, cmd_path: Path) -> List[Path]:
    """Build conservative lookup candidates without guessing across the project."""
    expanded = os.path.expandvars(os.path.expanduser(source_text))
    source_path = Path(expanded)
    file_name = _resource_file_name(source_text)
    candidates: List[Path] = []

    if source_path.is_absolute():
        candidates.append(source_path)
    else:
        candidates.append(cmd_path.parent / source_path)

    # Also support resources moved next to the CMD before conversion.
    if file_name:
        candidates.append(cmd_path.parent / file_name)
        candidates.append(cmd_path.parent / "resources" / file_name)

    unique_candidates: List[Path] = []
    seen = set()
    for candidate in candidates:
        key = os.path.normcase(os.path.abspath(str(candidate)))
        if key not in seen:
            seen.add(key)
            unique_candidates.append(candidate)
    return unique_candidates


def _copy_model_resources(cmd_path: Path, py_path: Path,
                          report: ConversionReport) -> None:
    """Copy referenced tire/road files beside the generated model script."""
    if not report.resource_sources:
        return

    resource_dir = py_path.parent / "resources" / py_path.stem
    report.resource_directory = str(resource_dir)

    try:
        resource_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        report.warnings.append(
            f"cannot create resource directory {resource_dir}: {type(exc).__name__}: {exc}"
        )
        return

    for source_text in report.resource_sources:
        file_name = _resource_file_name(source_text)
        if not file_name:
            report.warnings.append(f"invalid model resource path: {source_text}")
            report.missing_resources.append(source_text)
            continue

        target = resource_dir / file_name
        source = next(
            (
                candidate
                for candidate in _resource_source_candidates(source_text, cmd_path)
                if candidate.is_file()
            ),
            None,
        )

        if source is None:
            # A previously copied resource is still valid when the original
            # absolute CMD path is no longer available on this computer.
            if target.is_file():
                report.resource_files.append(str(target))
                continue

            report.missing_resources.append(source_text)
            report.warnings.append(
                f"model resource not found: {source_text}; expected at {target}"
            )
            continue

        try:
            if os.path.normcase(os.path.abspath(str(source))) != os.path.normcase(
                os.path.abspath(str(target))
            ):
                shutil.copy2(source, target)
            report.resource_files.append(str(target))
        except OSError as exc:
            report.missing_resources.append(source_text)
            report.warnings.append(
                f"cannot copy model resource {source} to {target}: "
                f"{type(exc).__name__}: {exc}"
            )


def convert_file(cmd_path: str | Path, py_path: str | Path | None = None,
                 report_path: str | Path | None = None) -> Tuple[Path, ConversionReport]:
    src = Path(cmd_path)
    if py_path is None:
        py_path = src.with_suffix(".py")
    dst = Path(py_path)
    text = src.read_text(encoding="utf-8", errors="ignore")
    py_text, report = convert_text(text)
    dst.write_text(py_text, encoding="utf-8", newline="\n")
    _copy_model_resources(src, dst, report)
    if report_path is not None:
        Path(report_path).write_text(report.as_text(), encoding="utf-8")
    return dst, report


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Convert Adams CMD model commands to Jusme Python")
    parser.add_argument("input", help="input .cmd file")
    parser.add_argument("-o", "--output", help="output .py file (default: same basename)")
    parser.add_argument("--report", help="optional conversion report path")
    parser.add_argument(
        "--patch",
        action="store_true",
        help="generate an ADM overlay patch instead of a complete model script",
    )
    parser.add_argument("--strict", action="store_true", help="return exit code 2 when unsupported or deferred blocks remain")
    args = parser.parse_args(argv)

    if args.patch:
        output = args.output or str(Path(args.input).with_name(Path(args.input).stem + "_patch.py"))
        dst, report = convert_patch_file(args.input, output, args.report)
    else:
        dst, report = convert_file(args.input, args.output, args.report)
    print(f"Converted: {args.input} -> {dst}")
    print(report.as_text(), end="")
    if args.strict and (report.unsupported_count or report.deferred_count):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

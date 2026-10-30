"""Adams CMD -> Jusme Python converter (V4)

Designed from the supplied CMD/PY reference pairs.  The module is self-contained
and keeps compatibility entry points ``gen_blocks`` and ``pharseBlocks`` used by
older code.

Main improvements over the legacy parser:
- robust CMD continuation-line parsing;
- correct joint type mapping;
- support for ShapePlate, ForceField, Gravity, ForceGeneral, ForceSingleComponent,
  Function and Orient patterns seen in the supplied reference/Assembly models;
- expression conversion for LOC/ORI helper functions;
- optional fields are emitted only when present in CMD;
- ForceSingleComponent CREATE + later MODIFY function/property updates;
- unsupported commands are reported instead of silently discarded;
- one-call file conversion API and CLI.
"""

from __future__ import annotations

import argparse
import re
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
        return "\n".join(lines) + "\n"


@dataclass
class ConverterState:
    model_name: str = ""
    units_created: bool = False
    known_entities: Dict[str, str] = field(default_factory=dict)
    entity_meta: Dict[str, Dict[str, str]] = field(default_factory=dict)


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
)


JOINT_NODE_TYPES = {
    "cylindrical": "JointCylinder",
    "revolute": "JointRevolute",
    "spherical": "JointSpherical",
    "fixed": "JointFixed",
    "hooke": "JointHooke",
    "translational": "JointTranslational",
    "inplane": "JointInplane",
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


def _emit_location_expr(out: List[str], target: str, expr: str) -> bool:
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
        v = _emit_get_object(out, p, ".global_loc")
        distance = re.sub(r"(?i)(inch(?:es)?|mm|millimeters?)$", "", args[1].strip()).strip()
        out.append(f"{target}.location = (LOC_ON_AXIS({v}, {distance}, {args[2].strip()}))\n")
        return True
    return False


def _emit_orientation_expr(out: List[str], target: str, expr: str) -> bool:
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
        # Reference output uses global_loc for the first two geometry points in
        # many cases and location for the remaining point.  The convention below
        # matches the supplied samples and is safer than passing scene objects.
        p1, p2, p3 = (args[0].strip(), args[1].strip(), args[2].strip())
        v1 = _emit_get_object(out, p1, ".global_loc")
        v2 = _emit_get_object(out, p2, ".global_loc")
        v3 = _emit_get_object(out, p3, ".location")
        out.append(f"{target}.orientation = (VecUtils.ORI_IN_PLANE({v1}, {v2}, {v3}, {args[3].strip()}))\n")
        return True

    if func == "ORI_LOCAL" and len(args) >= 2:
        inner_func, inner_args = _call_parts(args[0])
        ref = args[1].strip()
        ref_var = _emit_get_object(out, ref)
        if inner_func == "ORI_ALIGN_AXIS" and len(inner_args) >= 2:
            p = inner_args[0].strip()
            p_var = _emit_get_object(out, p, ".global_loc")
            out.append(
                f"{target}.orientation = (ORI_LOCAL(ORI_ALIGN_AXIS({p_var}, {inner_args[1].strip()}), {ref_var}))\n"
            )
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
        loc_ok = _emit_location_expr(out, name, fields["location"])
        if not loc_ok:
            report.warnings.append(f"unsupported location expression for {full}: {fields['location']}")
    if fields.get("orientation"):
        ori_ok = _emit_orientation_expr(out, name, fields["orientation"])
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


def _emit_dm_length_expr(out: List[str], target: str, expr: str) -> bool:
    """Convert DM(p1,p2) optionally followed by a numeric +/- offset."""
    e = _strip_outer_parens(expr)
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


def _emit_block(block: List[str], out: List[str], state: ConverterState, report: ConversionReport) -> bool:
    cmd = _clean_line(block[0]).lower()
    f = _parse_fields(block)

    # -------- units/model/data --------
    if cmd.startswith("defaults units"):
        if not state.units_created:
            out.append("UNITS_1 = MakeSceneNodeByType('DefaultsUnits', '.MODEL.UNITS_1')\n")
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
        state.model_name = f.get("model_name", state.model_name)
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
        full = f.get("marker_name", "")
        name = getElementName(full)
        out.append(f"{name} = MakeSceneNodeByType('Marker', '{full}')\n")
        out.append(f"{name}.marker_name = '{full}'\n")
        if "adams_id" in f: out.append(f"{name}.adams_id = {_int(f['adams_id'])}\n")
        if "comments" in f: out.append(f"{name}.comments = '{f['comments']}'\n")
        if "location" in f: out.append(f"{name}.location = {_vector_code(f['location'])}\n")
        if "orientation" in f: out.append(f"{name}.orientation = {_vector_code(f['orientation'], True)}\n")
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
                out.append(f"{mk} = Jusme.ActiveUSScene.getObject('{f[mk]}')\n")
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
        _emit_marker_modify(out, f, report)
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
            # Adams may re-state a model-unit value as e.g. ``27.5mm``.
            mm_match = re.fullmatch(r"([-+0-9.eEdD]+)\s*mm", radius_text, re.I)
            if mm_match:
                out.append(f"{name}.radius = {_num(mm_match.group(1))}\n")
            else:
                try:
                    out.append(f"{name}.radius = {_num(radius_text)}\n")
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

    return False


def pharseBlocks(blocks: List[List[str]], out_put: List[str], *, report: Optional[ConversionReport] = None,
                 state: Optional[ConverterState] = None) -> ConversionReport:
    """Compatibility entry point matching the legacy misspelled API name."""
    if report is None:
        report = ConversionReport()
    if state is None:
        state = _legacy_state

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


def convert_file(cmd_path: str | Path, py_path: str | Path | None = None,
                 report_path: str | Path | None = None) -> Tuple[Path, ConversionReport]:
    src = Path(cmd_path)
    if py_path is None:
        py_path = src.with_suffix(".py")
    dst = Path(py_path)
    text = src.read_text(encoding="utf-8", errors="ignore")
    py_text, report = convert_text(text)
    dst.write_text(py_text, encoding="utf-8", newline="\n")
    if report_path is not None:
        Path(report_path).write_text(report.as_text(), encoding="utf-8")
    return dst, report


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Convert Adams CMD model commands to Jusme Python")
    parser.add_argument("input", help="input .cmd file")
    parser.add_argument("-o", "--output", help="output .py file (default: same basename)")
    parser.add_argument("--report", help="optional conversion report path")
    parser.add_argument("--strict", action="store_true", help="return exit code 2 when unsupported or deferred blocks remain")
    args = parser.parse_args(argv)

    dst, report = convert_file(args.input, args.output, args.report)
    print(f"Converted: {args.input} -> {dst}")
    print(report.as_text(), end="")
    if args.strict and (report.unsupported_count or report.deferred_count):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# -*- coding: utf-8 -*-
"""Spline discovery and dependency-free XLSX point reading."""

import colorsys
import os
import posixpath
import re
import zipfile
from xml.etree import ElementTree


_MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_DOC_REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
_PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
_DRAWING_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
_INDEXED_COLORS = (
    "000000 FFFFFF FF0000 00FF00 0000FF FFFF00 FF00FF 00FFFF "
    "000000 FFFFFF FF0000 00FF00 0000FF FFFF00 FF00FF 00FFFF "
    "800000 008000 000080 808000 800080 008080 C0C0C0 808080 "
    "9999FF 993366 FFFFCC CCFFFF 660066 FF8080 0066CC CCCCCC "
    "000080 FF00FF FFFF00 00FFFF 800080 800000 008080 0000FF "
    "00CCFF CCFFFF CCFFCC FFFF99 99CCFF FF99CC CC99FF FFCC99 "
    "3366FF 33CCCC 99CC00 FFCC00 FF9900 FF6600 666699 969696 "
    "003366 339966 003300 333300 993300 993366 333399 333333"
).split()


class SplineDataError(ValueError):
    """Raised when a workbook cannot provide a valid two-column spline."""


def _xml_text(element):
    if element is None:
        return ""
    return "".join(element.itertext())


def _shared_strings(archive):
    try:
        root = ElementTree.fromstring(archive.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    except ElementTree.ParseError as exc:
        raise SplineDataError("Excel 文件的共享文本数据已损坏。") from exc
    return [
        "".join(node.itertext())
        for node in root.findall("{{{}}}si".format(_MAIN_NS))
    ]


def _worksheet_entries(archive):
    try:
        workbook_root = ElementTree.fromstring(archive.read("xl/workbook.xml"))
        relations_root = ElementTree.fromstring(
            archive.read("xl/_rels/workbook.xml.rels")
        )
    except (KeyError, ElementTree.ParseError) as exc:
        raise SplineDataError("Excel 文件缺少有效的工作簿结构。") from exc

    relation_targets = {
        relation.attrib.get("Id", ""): relation.attrib.get("Target", "")
        for relation in relations_root.findall("{{{}}}Relationship".format(_PKG_REL_NS))
    }
    sheets = workbook_root.find("{{{}}}sheets".format(_MAIN_NS))
    if sheets is None:
        raise SplineDataError("Excel 文件中没有工作表。")

    entries = []
    for sheet in sheets:
        name = sheet.attrib.get("name", "")
        relation_id = sheet.attrib.get("{{{}}}id".format(_DOC_REL_NS), "")
        target = relation_targets.get(relation_id, "")
        if not target:
            continue
        target = target.replace("\\", "/")
        if target.startswith("/"):
            normalized = target.lstrip("/")
        else:
            normalized = posixpath.normpath(posixpath.join("xl", target))
        entries.append((name, normalized))

    if not entries:
        raise SplineDataError("Excel 文件中没有可读取的工作表。")
    return entries


def list_xlsx_sheets(file_path):
    """Return worksheet names from an XLSX file without third-party packages."""
    _validate_xlsx_path(file_path)
    try:
        with zipfile.ZipFile(file_path, "r") as archive:
            return [name for name, _target in _worksheet_entries(archive)]
    except zipfile.BadZipFile as exc:
        raise SplineDataError("选择的文件不是有效的 XLSX 工作簿。") from exc


def _validate_xlsx_path(file_path):
    if not os.path.isfile(file_path):
        raise SplineDataError("选择的 Excel 文件不存在。")
    if os.path.splitext(file_path)[1].lower() != ".xlsx":
        raise SplineDataError("目前仅支持 .xlsx 文件。")


def _cell_value(cell, shared_strings, prefer_formula=False):
    if prefer_formula:
        formula_node = cell.find("{{{}}}f".format(_MAIN_NS))
        formula = _xml_text(formula_node).strip()
        if formula:
            # XLSX stores formulas without the leading equals sign.  For the
            # variable importer the formula text itself is the useful value;
            # spline imports keep using the cached numeric result.
            return formula

    cell_type = cell.attrib.get("t", "")
    if cell_type == "inlineStr":
        return _xml_text(cell.find("{{{}}}is".format(_MAIN_NS)))

    value_node = cell.find("{{{}}}v".format(_MAIN_NS))
    value = _xml_text(value_node).strip()
    if not value:
        return None
    if cell_type == "s":
        try:
            return shared_strings[int(value)]
        except (ValueError, IndexError):
            return value
    if cell_type in ("str", "e"):
        return value
    try:
        return float(value)
    except ValueError:
        return value


def _column_number(cell_reference):
    match = re.match(r"([A-Za-z]+)", cell_reference or "")
    if not match:
        return None
    number = 0
    for character in match.group(1).upper():
        number = number * 26 + ord(character) - ord("A") + 1
    return number


def _theme_colors(archive):
    """Resolve spreadsheet theme indices (whose order differs from the XML)."""
    try:
        relations = ElementTree.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        target = next(
            relation.attrib["Target"] for relation in relations
            if relation.attrib.get("Type", "").endswith("/theme")
        ).replace("\\", "/")
        path = (target.lstrip("/") if target.startswith("/") else
                posixpath.normpath(posixpath.join("xl", target)))
        root = ElementTree.fromstring(archive.read(path))
    except (KeyError, StopIteration, ElementTree.ParseError):
        return []
    scheme = root.find(".//{{{}}}clrScheme".format(_DRAWING_NS))
    colors = []
    for name in ("lt1", "dk1", "lt2", "dk2", "accent1", "accent2",
                 "accent3", "accent4", "accent5", "accent6", "hlink", "folHlink"):
        node = scheme.find("{{{}}}{}".format(_DRAWING_NS, name)) if scheme is not None else None
        color = node[0] if node is not None and len(node) else None
        colors.append(
            (color.attrib.get("lastClr") or color.attrib.get("val", ""))
            if color is not None else ""
        )
    return colors


def _fill_color(color, theme, indexed):
    if color is None:
        return None
    try:
        if "rgb" in color.attrib:
            rgb = color.attrib["rgb"][-6:]
        elif "theme" in color.attrib:
            rgb = theme[int(color.attrib["theme"])]
        elif "indexed" in color.attrib:
            rgb = indexed[int(color.attrib["indexed"])]
        else:
            return None
        if not re.fullmatch(r"[0-9a-fA-F]{6}", rgb):
            return None
        tint = max(-1.0, min(1.0, float(color.attrib.get("tint", 0))))
        if tint:
            red, green, blue = (int(rgb[index:index + 2], 16) / 255.0 for index in (0, 2, 4))
            hue, lightness, saturation = colorsys.rgb_to_hls(red, green, blue)
            lightness = lightness * (1 + tint) if tint < 0 else lightness * (1 - tint) + tint
            rgb = "".join("{:02X}".format(round(channel * 255)) for channel in
                          colorsys.hls_to_rgb(hue, lightness, saturation))
        return rgb.upper()
    except (IndexError, TypeError, ValueError):
        return None


def _style_fill_colors(archive):
    """Return solid background colors by cell style, using only the stdlib."""
    try:
        root = ElementTree.fromstring(archive.read("xl/styles.xml"))
    except (KeyError, ElementTree.ParseError):
        return []
    ns = {"s": _MAIN_NS}
    indexed_nodes = root.findall("s:colors/s:indexedColors/s:rgbColor", ns)
    indexed = ([node.attrib.get("rgb", "")[-6:] for node in indexed_nodes]
               if indexed_nodes else _INDEXED_COLORS)
    theme = _theme_colors(archive)
    fills = []
    for fill in root.findall("s:fills/s:fill", ns):
        pattern = fill.find("s:patternFill", ns)
        fills.append(
            _fill_color(pattern.find("s:fgColor", ns), theme, indexed)
            if pattern is not None and pattern.attrib.get("patternType") == "solid"
            else None
        )
    styles = []
    for style in root.findall("s:cellXfs/s:xf", ns):
        try:
            styles.append(fills[int(style.attrib.get("fillId", 0))])
        except (IndexError, ValueError):
            styles.append(None)
    return styles


def _read_xy_rows(archive, worksheet_path, shared_strings):
    try:
        root = ElementTree.fromstring(archive.read(worksheet_path))
    except (KeyError, ElementTree.ParseError) as exc:
        raise SplineDataError("无法读取所选工作表。") from exc

    rows = []
    for row in root.findall(".//{{{}}}row".format(_MAIN_NS)):
        row_number = int(row.attrib.get("r", len(rows) + 1))
        values = {1: None, 2: None}
        for cell in row.findall("{{{}}}c".format(_MAIN_NS)):
            column = _column_number(cell.attrib.get("r", ""))
            if column in values:
                values[column] = _cell_value(cell, shared_strings)
        rows.append((row_number, values[1], values[2]))
    return rows


def _read_rows(
    archive,
    worksheet_path,
    shared_strings,
    max_columns=None,
    formula_columns=None,
    row_fills=None,
    style_fills=None,
):
    """Return sparse worksheet rows as ``(row_number, {column: value})``."""
    try:
        root = ElementTree.fromstring(archive.read(worksheet_path))
    except (KeyError, ElementTree.ParseError) as exc:
        raise SplineDataError("无法读取所选工作表。") from exc

    formula_columns = set(formula_columns or ())
    rows = []
    for row in root.findall(".//{{{}}}row".format(_MAIN_NS)):
        row_number = int(row.attrib.get("r", len(rows) + 1))
        values = {}
        for cell in row.findall("{{{}}}c".format(_MAIN_NS)):
            column = _column_number(cell.attrib.get("r", ""))
            if column == 1 and row_fills is not None:
                try:
                    style = int(cell.attrib.get("s", row.attrib.get("s", 0)))
                    row_fills[row_number] = style_fills[style]
                except (IndexError, ValueError):
                    pass
            if column is None or (max_columns is not None and column > max_columns):
                continue
            values[column] = _cell_value(
                cell,
                shared_strings,
                prefer_formula=column in formula_columns,
            )
        rows.append((row_number, values))
    return rows


def read_xlsx_rows(
    file_path,
    sheet_name=None,
    max_columns=None,
    formula_columns=None,
    include_row_fills=False,
):
    """Read sparse cell values from one worksheet without external packages.

    The returned tuple is ``(selected_sheet_name, rows)``.  ``rows`` contains
    ``(row_number, values_by_one_based_column_number)`` entries.
    With ``include_row_fills=True``, a third item maps row numbers to the
    first cell's solid fill RGB.  Existing value-only callers are unchanged.
    """
    _validate_xlsx_path(file_path)
    try:
        with zipfile.ZipFile(file_path, "r") as archive:
            worksheets = _worksheet_entries(archive)
            if sheet_name is None:
                selected_name, worksheet_path = worksheets[0]
            else:
                matches = [item for item in worksheets if item[0] == sheet_name]
                if not matches:
                    raise SplineDataError(
                        "Excel 中找不到工作表：{}".format(sheet_name)
                    )
                selected_name, worksheet_path = matches[0]
            row_fills = {} if include_row_fills else None
            rows = _read_rows(
                archive,
                worksheet_path,
                _shared_strings(archive),
                max_columns=max_columns,
                formula_columns=formula_columns,
                row_fills=row_fills,
                style_fills=_style_fill_colors(archive) if include_row_fills else None,
            )
    except zipfile.BadZipFile as exc:
        raise SplineDataError("选择的文件不是有效的 XLSX 工作簿。") from exc
    if include_row_fills:
        return selected_name, rows, row_fills
    return selected_name, rows


def read_spline_points(file_path, sheet_name=None):
    """Read X/Y values from columns A/B, allowing header rows before data."""
    _validate_xlsx_path(file_path)
    try:
        with zipfile.ZipFile(file_path, "r") as archive:
            worksheets = _worksheet_entries(archive)
            if sheet_name is None:
                sheet_name, worksheet_path = worksheets[0]
            else:
                matches = [item for item in worksheets if item[0] == sheet_name]
                if not matches:
                    raise SplineDataError(
                        "Excel 中找不到工作表：{}".format(sheet_name)
                    )
                _name, worksheet_path = matches[0]
            rows = _read_xy_rows(
                archive,
                worksheet_path,
                _shared_strings(archive),
            )
    except zipfile.BadZipFile as exc:
        raise SplineDataError("选择的文件不是有效的 XLSX 工作簿。") from exc

    points = []
    data_started = False
    for row_number, x_value, y_value in rows:
        if x_value is None and y_value is None:
            continue
        try:
            x_number = float(x_value)
            y_number = float(y_value)
        except (TypeError, ValueError):
            if not data_started:
                continue
            raise SplineDataError(
                "第 {} 行的 A、B 列必须都是数字。".format(row_number)
            )
        data_started = True
        points.append((x_number, y_number))

    if len(points) < 2:
        raise SplineDataError("样条曲线至少需要两组有效的 X、Y 数据。")
    for index in range(1, len(points)):
        if points[index][0] <= points[index - 1][0]:
            raise SplineDataError(
                "X 数据必须严格递增；第 {} 个数据点不符合要求。".format(
                    index + 1
                )
            )
    return points


def _node_children(node):
    children = []
    for attribute_name in ("Objects", "Group"):
        value = getattr(node, attribute_name, None)
        if value is not None and not callable(value):
            try:
                children.extend(list(value))
            except Exception:
                pass

    getter = getattr(node, "getObjects", None)
    if callable(getter):
        try:
            children.extend(list(getter() or []))
        except Exception:
            pass
    return children


def _is_spline(node):
    try:
        node_type = str(node.Proxy.Type)
    except Exception:
        node_type = ""
    if "spline" in node_type.lower():
        return True
    properties = set(getattr(node, "PropertiesList", []) or [])
    return "spline_name" in properties and "x" in properties and "y" in properties


def find_scene_splines(scene):
    """Find every spline in a scene using both flat and tree-style APIs."""
    if scene is None:
        return []

    pending = []
    scene_objects = getattr(scene, "Objects", None)
    if scene_objects is not None:
        try:
            pending.extend(list(scene_objects))
        except Exception:
            pass
    pending.extend(_node_children(scene))

    model_name = getattr(scene, "Name", "") or ""
    get_object = getattr(scene, "getObject", None)
    if model_name and callable(get_object):
        for group_name in (
            "DataElements",
            "Data_Elements",
            "Elements",
            "DesignTools",
            "Splines",
        ):
            try:
                group = get_object(".{}.{}".format(model_name, group_name))
            except Exception:
                group = None
            if group is not None:
                pending.append(group)

    found = {}
    visited = set()
    while pending:
        node = pending.pop(0)
        identity = id(node)
        if identity in visited:
            continue
        visited.add(identity)
        if _is_spline(node):
            name = (
                getattr(node, "Name", "")
                or getattr(node, "spline_name", "")
                or getattr(node, "Label", "")
            )
            if name:
                found[name] = node
        pending.extend(_node_children(node))
    return [found[name] for name in sorted(found, key=str.lower)]

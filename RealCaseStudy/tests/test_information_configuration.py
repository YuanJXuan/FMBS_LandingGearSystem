# -*- coding: utf-8 -*-

import sys
import tempfile
import types
import unittest
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TEMPLATE_DIR / "Share"))

import InformationConfiguration


class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class Node:
    def __init__(self, location=(0, 0, 0), **properties):
        self.location = Vector(*location)
        self.orientation = Vector(0, 0, 0)
        self.PropertiesList = list(properties)
        for name, value in properties.items():
            setattr(self, name, value)


class InformationConfigurationTests(unittest.TestCase):
    def setUp(self):
        self.case_model_dir = TEMPLATE_DIR / "Model" / "template_nlg_retract"
        self._module_names = (
            "Jusme",
            "FmbsShortcut",
            "FmbsShortcut.SCcmd",
            "FmbsShortcut.SCcmd.utils",
            "FmbsShortcut.SCcmd.utils.VecUtils",
        )
        self._previous_modules = {
            name: sys.modules.get(name) for name in self._module_names
        }
        vec_utils = types.ModuleType("FmbsShortcut.SCcmd.utils.VecUtils")

        def global2local(parent_location, parent_orientation, location, orientation):
            return (
                Vector(
                    location.x - parent_location.x,
                    location.y - parent_location.y,
                    location.z - parent_location.z,
                ),
                Vector(
                    orientation.x - parent_orientation.x,
                    orientation.y - parent_orientation.y,
                    orientation.z - parent_orientation.z,
                ),
            )

        def ori_along_axis(start, end, _axis):
            length = (
                (end.x - start.x) ** 2
                + (end.y - start.y) ** 2
                + (end.z - start.z) ** 2
            ) ** 0.5
            return Vector(
                (end.x - start.x) / length,
                (end.y - start.y) / length,
                (end.z - start.z) / length,
            )

        vec_utils.global2local = global2local
        vec_utils.ORI_ALONG_AXIS = ori_along_axis
        utils = types.ModuleType("FmbsShortcut.SCcmd.utils")
        utils.VecUtils = vec_utils
        sccmd = types.ModuleType("FmbsShortcut.SCcmd")
        sccmd.utils = utils
        shortcut = types.ModuleType("FmbsShortcut")
        shortcut.SCcmd = sccmd
        sys.modules["Jusme"] = types.SimpleNamespace(Vector=Vector)
        sys.modules["FmbsShortcut"] = shortcut
        sys.modules["FmbsShortcut.SCcmd"] = sccmd
        sys.modules["FmbsShortcut.SCcmd.utils"] = utils
        sys.modules["FmbsShortcut.SCcmd.utils.VecUtils"] = vec_utils

    def tearDown(self):
        for name, previous in self._previous_modules.items():
            if previous is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = previous

    def test_reads_every_supported_section_from_the_case_workbook(self):
        configuration = InformationConfiguration.load_information_configuration(
            str(self.case_model_dir)
        )

        self.assertTrue(configuration["file_path"].endswith("信息配置表.xlsx"))
        self.assertGreaterEqual(len(configuration["markers"]), 1)
        self.assertGreaterEqual(len(configuration["simulation_parameters"]), 1)
        self.assertGreaterEqual(len(configuration["postprocessing"]), 1)
        self.assertGreaterEqual(len(configuration["splines"]), 1)
        self.assertEqual(
            configuration["markers"][0]["coordinates"],
            (4997.0, 300.0, -1757.0),
        )
        self.assertTrue(
            any(
                entry["file_name"] == "airspring.xlsx"
                for entry in configuration["splines"]
            )
        )
        self.assertTrue(
            all(entry["target"] for entry in configuration["postprocessing"])
        )
        self.assertTrue(
            all(
                "x_unit" in entry and "y_unit" in entry
                for entry in configuration["postprocessing"]
            )
        )

    def test_reads_work_diagram_configuration_from_nlg_drop_workbook(self):
        configuration = InformationConfiguration.load_information_configuration(
            str(TEMPLATE_DIR / "Model" / "template_nlg_drop")
        )

        self.assertEqual(len(configuration["work_diagrams"]), 1)
        diagram = configuration["work_diagrams"][0]
        self.assertEqual(diagram["label"], "缓冲器功量图")
        self.assertEqual(diagram["x_source"], "缓冲器位移")
        self.assertEqual(diagram["y_source"], "轮胎垂向载荷")
        self.assertEqual(diagram["x_unit"], "mm")
        self.assertEqual(diagram["y_unit"], "N")

    def test_reads_three_parameter_sections_from_nlg_drop_workbook(self):
        configuration = InformationConfiguration.load_information_configuration(
            str(TEMPLATE_DIR / "Model" / "template_nlg_drop")
        )
        groups = InformationConfiguration.simulation_parameter_groups(
            configuration
        )

        self.assertEqual(len(groups["buffer_parameters"]), 12)
        self.assertEqual(len(groups["other_parameters"]), 1)
        self.assertEqual(len(groups["structure_property_parameters"]), 4)
        self.assertEqual(len(configuration["simulation_parameters"]), 17)
        self.assertEqual(configuration["errors"], [])
        self.assertEqual(
            groups["structure_property_parameters"][0]["target"],
            ".qianqizhiliang.mass",
        )

    def test_legacy_simulation_section_is_displayed_as_other_parameters(self):
        legacy_entry = {
            "id": "config.simulation.1",
            "row": 3,
            "label": "旧参数",
            "target": "old_variable",
            "value": 1,
            "unit": "",
        }
        groups = InformationConfiguration.simulation_parameter_groups(
            {"simulation_parameters": [legacy_entry]}
        )

        self.assertEqual(groups["buffer_parameters"], [])
        self.assertEqual(groups["structure_property_parameters"], [])
        self.assertEqual(groups["other_parameters"], [legacy_entry])

    def test_excel_lock_file_is_not_treated_as_information_workbook(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            lock_file = Path(temp_dir) / "~$信息配置表.xlsx"
            lock_file.write_bytes(b"excel lock")

            discovered = InformationConfiguration.find_information_workbook(
                temp_dir
            )

        self.assertEqual(discovered, "")

    def test_resolves_state_functions_and_object_properties(self):
        state_node = Node(function="old")
        part_node = Node(mass=5.0)

        class Scene:
            Name = "Unknown"

            def getObject(self, path):
                return {".Unknown.ges_dragbrace": part_node}.get(path)

        state_variables = [
            {
                "name": "VARIABEL_124",
                "key": "VARIABEL_124",
                "path": ".Unknown.VARIABEL_124",
                "node": state_node,
            }
        ]
        configured = [
            {
                "id": "config.simulation.1",
                "row": 7,
                "label": "面积",
                "target": "VARIABEL_124",
                "value": 20,
                "unit": "mm^2",
            },
            {
                "id": "config.simulation.2",
                "row": 8,
                "label": "质量",
                "target": ".ges_dragbrace.mass",
                "value": 100,
                "unit": "kg",
            },
        ]

        resolved = InformationConfiguration.resolve_simulation_parameters(
            Scene(), configured, state_variables
        )

        self.assertEqual(resolved[0]["value_property"], "function")
        self.assertEqual(resolved[0]["value_kind"], "expression")
        self.assertIs(resolved[0]["node"], state_node)
        self.assertEqual(resolved[1]["path"], ".Unknown.ges_dragbrace")
        self.assertEqual(resolved[1]["value_property"], "mass")
        self.assertEqual(resolved[1]["value_kind"], "numeric")

    def test_dynamic_state_variables_fill_simulation_table_without_workbook(self):
        state_node = Node(function="1")
        variables = [
            {
                "name": "speed",
                "key": "controls.speed",
                "label": "speed",
                "value": "1",
                "node": state_node,
                "path": ".Unknown.controls.speed",
                "kind": "state",
                "value_property": "function",
                "value_kind": "expression",
            }
        ]
        parameters = InformationConfiguration.dynamic_simulation_parameters(
            variables,
            {"controls.speed": "运动速度"},
        )

        class Editor:
            def text(self):
                return "2+3"

        class Table:
            def editor(self, key):
                return Editor() if key == "controls.speed" else None

        class Scene:
            Name = "Unknown"

            def __init__(self):
                self.recompute_count = 0

            def getObject(self, path):
                return state_node if path == ".Unknown.controls.speed" else None

            def recompute(self):
                self.recompute_count += 1

        scene = Scene()
        updated, errors = InformationConfiguration.apply_simulation_table(
            scene,
            Table(),
            parameters,
        )

        self.assertEqual(errors, [])
        self.assertEqual(updated, 1)
        self.assertEqual(parameters[0]["label"], "运动速度")
        self.assertEqual(state_node.function, "2+3")
        self.assertEqual(scene.recompute_count, 1)

    def test_rejects_duplicate_simulation_targets_before_writing(self):
        part_node = Node(ixx=5.0)

        class Scene:
            Name = "Unknown"

            def getObject(self, path):
                return {".Unknown.ges_dragbrace": part_node}.get(path)

            def recompute(self):
                pass

        configured = [
            {
                "id": "config.simulation.1",
                "row": 10,
                "label": "X惯量",
                "target": ".ges_dragbrace.ixx",
                "value": 20,
                "unit": "",
            },
            {
                "id": "config.simulation.2",
                "row": 11,
                "label": "Y惯量",
                "target": ".ges_dragbrace.ixx",
                "value": 30,
                "unit": "",
            },
        ]
        resolved = InformationConfiguration.resolve_simulation_parameters(
            Scene(), configured, []
        )

        class Editor:
            def __init__(self, value):
                self.value = value

            def text(self):
                return self.value

        class Table:
            def editor(self, key):
                return Editor("20" if key.endswith("1") else "30")

        updated, errors = InformationConfiguration.apply_simulation_table(
            Scene(), Table(), resolved
        )

        self.assertEqual(updated, 0)
        self.assertTrue(any("重复指向" in error for error in errors))
        self.assertEqual(part_node.ixx, 5.0)

    def test_applies_the_configured_spline_from_the_same_folder(self):
        class Proxy:
            Type = "Spline"

        configuration = InformationConfiguration.load_information_configuration(
            str(self.case_model_dir)
        )
        splines = []
        for entry in configuration["splines"]:
            spline = Node()
            spline.Name = ".Unknown." + entry["target"]
            spline.Label = entry["target"]
            spline.Proxy = Proxy()
            spline.x = [0.0, 1.0]
            spline.y = [0.0, 1.0]
            spline.z = []
            splines.append(spline)

        class Scene:
            Name = "Unknown"
            Objects = splines

            def getObjects(self):
                return []

            def getObject(self, _path):
                return None

            def recompute(self):
                pass

        updated, errors = InformationConfiguration.apply_configured_splines(
            Scene(), configuration
        )

        self.assertEqual(errors, [])
        self.assertEqual(updated, len(configuration["splines"]))
        for spline in splines:
            self.assertEqual(len(spline.x), 41)
            self.assertEqual(len(spline.y), 41)
            self.assertEqual(spline.x[0], 0.0)

    def test_marker_batch_rolls_back_if_scene_refresh_fails(self):
        marker = Node(location=(1, 2, 3))
        parent = Node(location=(10, 20, 30))

        class Scene:
            Name = "Unknown"

            def getObject(self, path):
                return {
                    ".Unknown.ground.marker": marker,
                    ".Unknown.ground": parent,
                }.get(path)

            def recompute(self):
                raise RuntimeError("refresh failed")

        entries = [
            {
                "id": "config.marker.1",
                "row": 3,
                "label": "测试点",
                "target": "ground.marker",
                "coordinates": (4, 5, 6),
            }
        ]
        updated, errors = InformationConfiguration.apply_marker_values(
            Scene(), entries, {"config.marker.1": (14, 25, 36)}
        )

        self.assertEqual(updated, 0)
        self.assertTrue(errors)
        self.assertEqual(
            (marker.location.x, marker.location.y, marker.location.z),
            (1.0, 2.0, 3.0),
        )

    def test_marker_world_coordinates_are_written_as_parent_local_coordinates(self):
        marker = Node(location=(0, 0, 0))
        parent = Node(location=(10, 20, 30))

        class Scene:
            Name = "Unknown"

            def getObject(self, path):
                return {
                    ".Unknown.part.marker": marker,
                    ".Unknown.part": parent,
                }.get(path)

            def recompute(self):
                pass

        entries = [
            {
                "id": "config.marker.1",
                "row": 3,
                "label": "测试点",
                "target": "part.marker",
                "coordinates": (13, 24, 35),
            }
        ]
        updated, errors = InformationConfiguration.apply_marker_values(
            Scene(), entries, {"config.marker.1": (13, 24, 35)}
        )

        self.assertEqual(errors, [])
        self.assertEqual(updated, 1)
        self.assertEqual(
            (marker.location.x, marker.location.y, marker.location.z),
            (3.0, 4.0, 5.0),
        )

    def test_marker_table_applies_joint_markers_parts_and_recompute(self):
        driver = Node(location=(1, 2, 3))
        driver_parent = Node(location=(10, 0, 0))
        follower = Node(location=(4, 5, 6))
        follower_parent = Node(location=(20, 0, 0))
        wheel_part = Node(location=(30, 0, 0))

        class Joint:
            def __init__(self):
                self.recompute_count = 0

            def recompute(self):
                self.recompute_count += 1

        joint = Joint()

        class Scene:
            Name = "Unknown"

            def __init__(self):
                self.recompute_count = 0

            def getObject(self, path):
                return {
                    ".Unknown.part.driver": driver,
                    ".Unknown.part": driver_parent,
                    ".Unknown.other.follow": follower,
                    ".Unknown.other": follower_parent,
                    ".Unknown.lt_1_wheel_part": wheel_part,
                    ".Unknown.wheel_joint": joint,
                }.get(path)

            def recompute(self):
                self.recompute_count += 1

        entries = [
            {
                "id": "config.marker.1",
                "row": 3,
                "label": "轮心",
                "target": ".OldModel.part.driver",
                "coordinates": (50, 4, 5),
            }
        ]
        linkages = [
            InformationConfiguration.StructuralParameterization.normalize_parameter(
                {
                    "id": "wheel",
                    "driver": "part.driver",
                    "axes": ["x", "y", "z"],
                    "table_only": True,
                    "followers": [
                        {
                            "path": "other.follow",
                            "operation": "copy",
                            "axes": ["x", "y", "z"],
                        },
                        {
                            "path": "lt_1.wheel_part",
                            "target_type": "part",
                            "operation": "copy",
                            "axes": ["x", "y", "z"],
                        },
                    ],
                    "recompute": ["wheel_joint"],
                }
            )
        ]
        scene = Scene()

        updated, errors = InformationConfiguration.apply_marker_values(
            scene,
            entries,
            {"config.marker.1": (50, 4, 5)},
            linkages,
        )

        self.assertEqual(errors, [])
        self.assertEqual(updated, 3)
        self.assertEqual(
            (driver.location.x, driver.location.y, driver.location.z),
            (40.0, 4.0, 5.0),
        )
        self.assertEqual(
            (follower.location.x, follower.location.y, follower.location.z),
            (30.0, 4.0, 5.0),
        )
        self.assertEqual(
            (wheel_part.location.x, wheel_part.location.y, wheel_part.location.z),
            (50.0, 4.0, 5.0),
        )
        self.assertEqual(joint.recompute_count, 1)
        self.assertEqual(scene.recompute_count, 2)
        self.assertEqual(
            InformationConfiguration.count_marker_linkages(entries, linkages),
            1,
        )

    def test_dropdown_marker_edit_uses_all_excel_rows_and_syncs_coincident_pair(self):
        entries = [
            {
                "id": "config.marker.1",
                "row": 3,
                "label": "质量点",
                "target": "body.mass_marker",
                "coordinates": (1, 2, 3),
            },
            {
                "id": "config.marker.2",
                "row": 4,
                "label": "安装点",
                "target": "strut.mount_marker",
                "coordinates": (1, 2, 3),
            },
            {
                "id": "config.marker.3",
                "row": 5,
                "label": "轴线端点",
                "target": "strut.axis_end",
                "coordinates": (4, 5, 6),
            },
        ]
        linkages = [
            InformationConfiguration.StructuralParameterization.normalize_parameter(
                {
                    "id": "mass_point",
                    "driver": "body.mass_marker",
                    "axes": ["x", "y", "z"],
                    "table_only": True,
                    "coincident_with": ["strut.mount_marker"],
                }
            )
        ]

        batch_entries, values, synchronized_ids = (
            InformationConfiguration.marker_coordinates_for_selection(
                entries,
                linkages,
                "config.marker.2",
                (10, 20, 30),
            )
        )

        self.assertEqual(values["config.marker.1"], (10.0, 20.0, 30.0))
        self.assertEqual(values["config.marker.2"], (10.0, 20.0, 30.0))
        self.assertNotIn("config.marker.3", values)
        self.assertEqual(
            [entry["id"] for entry in batch_entries],
            ["config.marker.1", "config.marker.2"],
        )
        self.assertEqual(
            synchronized_ids,
            {"config.marker.1", "config.marker.2"},
        )

    def test_dropdown_marker_edit_includes_required_coaxial_endpoint_only(self):
        entries = [
            {
                "id": "start",
                "row": 3,
                "label": "轴线起点",
                "target": "strut.start",
                "coordinates": (0, 0, 0),
            },
            {
                "id": "end",
                "row": 4,
                "label": "轴线终点",
                "target": "strut.end",
                "coordinates": (0, 0, 10),
            },
            {
                "id": "unrelated",
                "row": 5,
                "label": "无关安装点",
                "target": "other.mount",
                "coordinates": (8, 9, 10),
            },
        ]
        linkage = InformationConfiguration.StructuralParameterization.normalize_parameter(
            {
                "id": "strut_axis",
                "driver": "strut.start",
                "axes": ["x", "y", "z"],
                "table_only": True,
                "coaxial": [
                    {
                        "id": "strut_axis",
                        "start": "strut.start",
                        "end": "strut.end",
                        "axis": "z",
                    }
                ],
            }
        )

        batch_entries, values, synchronized_ids = (
            InformationConfiguration.marker_coordinates_for_selection(
                entries,
                [linkage],
                "start",
                (5, 0, 0),
            )
        )

        self.assertEqual([entry["id"] for entry in batch_entries], ["start", "end"])
        self.assertEqual(values["start"], (5.0, 0.0, 0.0))
        self.assertEqual(values["end"], (0.0, 0.0, 10.0))
        self.assertNotIn("unrelated", values)
        self.assertEqual(synchronized_ids, {"start"})

    def test_marker_table_keeps_axis_markers_coaxial_without_moving_parts(self):
        outer = Node(location=(0, 0, 2))
        rod = Node(location=(0, 0, 8))
        start_marker = Node(location=(0, 0, -2))
        end_marker = Node(location=(0, 0, 2))
        outer_cm = Node(location=(0, 0, 0))
        rod_cm = Node(location=(0, 0, 0))
        outer_interface = Node(location=(0, 0, 3))
        rod_interface = Node(location=(0, 0, -3))
        outer_cylinder = Node(length=6.0)
        rod_cylinder = Node(length=10.0)

        class Joint:
            def __init__(self):
                self.recompute_count = 0

            def recompute(self):
                self.recompute_count += 1

        joint = Joint()

        class Scene:
            Name = "Unknown"

            def __init__(self):
                self.recompute_count = 0

            def getObject(self, path):
                return {
                    ".Unknown.outer": outer,
                    ".Unknown.outer.start": start_marker,
                    ".Unknown.outer.cm": outer_cm,
                    ".Unknown.outer.inner": outer_interface,
                    ".Unknown.outer.cylinder": outer_cylinder,
                    ".Unknown.rod": rod,
                    ".Unknown.rod.end": end_marker,
                    ".Unknown.rod.cm": rod_cm,
                    ".Unknown.rod.inner": rod_interface,
                    ".Unknown.rod.cylinder": rod_cylinder,
                    ".Unknown.slide_joint": joint,
                }.get(path)

            def recompute(self):
                self.recompute_count += 1

        coaxial = {
            "id": "actuator_axis",
            "start": "outer.start",
            "end": "rod.end",
            "axis": "z",
            "markers": [
                {
                    "path": "outer.cm",
                    "cylinder": "outer.cylinder",
                    "distance_from": "start",
                    "align_orientation": True,
                },
                {
                    "path": "rod.cm",
                    "cylinder": "rod.cylinder",
                    "distance_from": "end",
                    "reverse": True,
                    "align_orientation": True,
                },
                {"path": "outer.inner", "fraction": 0.5},
                {"path": "rod.inner", "fraction": 0.5},
            ],
            "coincident_pairs": [["outer.inner", "rod.inner"]],
            "recompute": ["slide_joint"],
        }
        linkages = [
            InformationConfiguration.StructuralParameterization.normalize_parameter(
                {
                    "id": parameter_id,
                    "driver": driver,
                    "axes": ["x", "y", "z"],
                    "table_only": True,
                    "coaxial": [coaxial],
                }
            )
            for parameter_id, driver in (
                ("outer_end", "outer.start"),
                ("rod_end", "rod.end"),
            )
        ]
        entries = [
            {
                "id": "config.marker.1",
                "row": 3,
                "label": "外筒端点",
                "target": ".Old.outer.start",
                "coordinates": (0, 0, 0),
            },
            {
                "id": "config.marker.2",
                "row": 4,
                "label": "活塞杆端点",
                "target": ".Old.rod.end",
                "coordinates": (0, 0, 20),
            },
        ]
        scene = Scene()

        updated, errors = InformationConfiguration.apply_marker_values(
            scene,
            entries,
            {
                "config.marker.1": (10, 5, 0),
                "config.marker.2": (10, 5, 20),
            },
            linkages,
        )

        self.assertEqual(errors, [])
        self.assertEqual(updated, 6)
        self.assertEqual((outer.location.x, outer.location.y, outer.location.z), (0, 0, 2))
        self.assertEqual((rod.location.x, rod.location.y, rod.location.z), (0, 0, 8))
        self.assertEqual(outer.orientation.z, 0.0)
        self.assertEqual(rod.orientation.z, 0.0)
        self.assertEqual(start_marker.orientation.z, 1.0)
        self.assertEqual(end_marker.orientation.z, -1.0)
        self.assertEqual(outer_cm.location.z, 1.0)
        self.assertEqual(rod_cm.location.z, 7.0)
        self.assertEqual(outer_cm.orientation.z, 1.0)
        self.assertEqual(rod_cm.orientation.z, -1.0)
        self.assertEqual(outer_interface.location.z, 8.0)
        self.assertEqual(rod_interface.location.z, 2.0)
        self.assertEqual(outer_interface.orientation.z, 1.0)
        self.assertEqual(rod_interface.orientation.z, 1.0)
        self.assertEqual(joint.recompute_count, 1)
        self.assertEqual(scene.recompute_count, 2)

    def test_coincident_pair_rejects_a_split_joint_before_mutating_scene(self):
        start_parent = Node()
        end_parent = Node()
        first_parent = Node()
        second_parent = Node()
        start_marker = Node()
        end_marker = Node(location=(0, 0, 10))
        first_marker = Node(location=(0, 0, 4))
        second_marker = Node(location=(0, 0, 6))

        class Scene:
            Name = "Unknown"

            def getObject(self, path):
                return {
                    ".Unknown.start": start_parent,
                    ".Unknown.start.marker": start_marker,
                    ".Unknown.end": end_parent,
                    ".Unknown.end.marker": end_marker,
                    ".Unknown.first": first_parent,
                    ".Unknown.first.marker": first_marker,
                    ".Unknown.second": second_parent,
                    ".Unknown.second.marker": second_marker,
                }.get(path)

            def recompute(self):
                pass

        coaxial = {
            "id": "split_joint",
            "start": "start.marker",
            "end": "end.marker",
            "axis": "z",
            "markers": [
                {"path": "first.marker", "fraction": 0.4},
                {"path": "second.marker", "fraction": 0.6},
            ],
            "coincident_pairs": [["first.marker", "second.marker"]],
        }
        linkages = [
            InformationConfiguration.StructuralParameterization.normalize_parameter(
                {
                    "id": parameter_id,
                    "driver": driver,
                    "axes": ["x", "y", "z"],
                    "table_only": True,
                    "coaxial": [coaxial],
                }
            )
            for parameter_id, driver in (
                ("start", "start.marker"),
                ("end", "end.marker"),
            )
        ]
        entries = [
            {"id": "start", "row": 3, "label": "起点", "target": "start.marker"},
            {"id": "end", "row": 4, "label": "终点", "target": "end.marker"},
        ]

        updated, errors = InformationConfiguration.apply_marker_values(
            Scene(),
            entries,
            {"start": (10, 0, 0), "end": (10, 0, 10)},
            linkages,
        )

        self.assertEqual(updated, 0)
        self.assertTrue(any("副端点不重合" in error for error in errors))
        self.assertEqual((start_marker.location.x, start_marker.location.z), (0.0, 0.0))
        self.assertEqual((first_marker.location.x, first_marker.location.z), (0.0, 4.0))

    def test_coincident_parameters_must_share_one_requested_world_position(self):
        first_parent = Node()
        second_parent = Node()
        first_marker = Node()
        second_marker = Node()

        class Scene:
            Name = "Unknown"

            def getObject(self, path):
                return {
                    ".Unknown.first": first_parent,
                    ".Unknown.first.marker": first_marker,
                    ".Unknown.second": second_parent,
                    ".Unknown.second.marker": second_marker,
                }.get(path)

            def recompute(self):
                pass

        linkages = [
            InformationConfiguration.StructuralParameterization.normalize_parameter(
                {
                    "id": "mass_point",
                    "label": "质量点",
                    "driver": "first.marker",
                    "axes": ["x", "y", "z"],
                    "table_only": True,
                    "coincident_with": ["second.marker"],
                }
            ),
            InformationConfiguration.StructuralParameterization.normalize_parameter(
                {
                    "id": "mount_point",
                    "label": "安装点",
                    "driver": "second.marker",
                    "axes": ["x", "y", "z"],
                    "table_only": True,
                }
            ),
        ]
        entries = [
            {"id": "first", "row": 3, "label": "质量点", "target": "first.marker"},
            {"id": "second", "row": 4, "label": "安装点", "target": "second.marker"},
        ]

        updated, errors = InformationConfiguration.apply_marker_values(
            Scene(),
            entries,
            {"first": (10, 0, 0), "second": (11, 0, 0)},
            linkages,
        )

        self.assertEqual(updated, 0)
        self.assertTrue(any("坐标不一致" in error for error in errors))
        self.assertEqual(first_marker.location.x, 0.0)
        self.assertEqual(second_marker.location.x, 0.0)

        updated, errors = InformationConfiguration.apply_marker_values(
            Scene(),
            entries,
            {"first": (10, 0, 0), "second": (10, 0, 0)},
            linkages,
        )

        self.assertEqual(errors, [])
        self.assertEqual(updated, 2)
        self.assertEqual(first_marker.location.x, 10.0)
        self.assertEqual(second_marker.location.x, 10.0)

    def test_marker_table_updates_link_length_without_rotating_joint_markers(self):
        start_parent = Node()
        end_parent = Node()
        link_parent = Node()
        start_marker = Node()
        end_marker = Node(location=(0, 3, 4))
        midpoint = Node(location=(0, 1.5, 2))
        geometry = Node(length=5.0)

        class Scene:
            Name = "Unknown"

            def getObject(self, path):
                return {
                    ".Unknown.start_part": start_parent,
                    ".Unknown.start_part.marker": start_marker,
                    ".Unknown.end_part": end_parent,
                    ".Unknown.end_part.marker": end_marker,
                    ".Unknown.link": link_parent,
                    ".Unknown.link.cm": midpoint,
                    ".Unknown.link.geometry": geometry,
                }.get(path)

            def recompute(self):
                pass

        coaxial = {
            "id": "variable_link",
            "start": "start_part.marker",
            "end": "end_part.marker",
            "axis": "z",
            "align_start_orientation": False,
            "align_end_orientation": False,
            "markers": [{"path": "link.cm", "fraction": 0.5}],
            "length_targets": [{"path": "link.geometry"}],
        }
        linkages = [
            InformationConfiguration.StructuralParameterization.normalize_parameter(
                {
                    "id": parameter_id,
                    "driver": driver,
                    "axes": ["x", "y", "z"],
                    "table_only": True,
                    "coaxial": [coaxial],
                }
            )
            for parameter_id, driver in (
                ("start", "start_part.marker"),
                ("end", "end_part.marker"),
            )
        ]
        entries = [
            {
                "id": "config.marker.1",
                "row": 3,
                "label": "起点",
                "target": "start_part.marker",
                "coordinates": (0, 0, 0),
            },
            {
                "id": "config.marker.2",
                "row": 4,
                "label": "终点",
                "target": "end_part.marker",
                "coordinates": (0, 3, 4),
            },
        ]

        updated, errors = InformationConfiguration.apply_marker_values(
            Scene(),
            entries,
            {
                "config.marker.1": (0, 0, 0),
                "config.marker.2": (0, 6, 8),
            },
            linkages,
        )

        self.assertEqual(errors, [])
        self.assertEqual(updated, 4)
        self.assertEqual(geometry.length, 10.0)
        self.assertEqual(
            (midpoint.location.x, midpoint.location.y, midpoint.location.z),
            (0.0, 3.0, 4.0),
        )
        self.assertEqual(
            (start_marker.orientation.x, start_marker.orientation.y, start_marker.orientation.z),
            (0.0, 0.0, 0.0),
        )
        self.assertEqual(
            (end_marker.orientation.x, end_marker.orientation.y, end_marker.orientation.z),
            (0.0, 0.0, 0.0),
        )

    def test_coaxial_group_can_place_and_orient_parts_with_offset_markers(self):
        start_parent = Node()
        end_parent = Node()
        shaft_parent = Node()
        start_marker = Node()
        end_marker = Node(location=(0, 0, 10))
        joint_marker = Node(location=(-2, 0, 5))
        wheel_part = Node()

        class Scene:
            Name = "Unknown"

            def getObject(self, path):
                return {
                    ".Unknown.start": start_parent,
                    ".Unknown.start.marker": start_marker,
                    ".Unknown.end": end_parent,
                    ".Unknown.end.marker": end_marker,
                    ".Unknown.shaft": shaft_parent,
                    ".Unknown.shaft.joint": joint_marker,
                    ".Unknown.wheel": wheel_part,
                }.get(path)

            def recompute(self):
                pass

        coaxial = {
            "id": "wheel_axis",
            "start": "start.marker",
            "end": "end.marker",
            "axis": "z",
            "end_reverse": False,
            "markers": [
                {
                    "path": "wheel",
                    "target_type": "part",
                    "fraction": 0.0,
                    "align_orientation": True,
                },
                {
                    "path": "shaft.joint",
                    "fraction": 0.5,
                    "offset": {"x": -2.0},
                    "align_orientation": True,
                },
            ],
        }
        linkages = [
            InformationConfiguration.StructuralParameterization.normalize_parameter(
                {
                    "id": parameter_id,
                    "driver": driver,
                    "axes": ["x", "y", "z"],
                    "table_only": True,
                    "coaxial": [coaxial],
                }
            )
            for parameter_id, driver in (
                ("start", "start.marker"),
                ("end", "end.marker"),
            )
        ]
        entries = [
            {
                "id": "config.marker.1",
                "row": 3,
                "label": "轴线起点",
                "target": "start.marker",
                "coordinates": (0, 0, 0),
            },
            {
                "id": "config.marker.2",
                "row": 4,
                "label": "轴线终点",
                "target": "end.marker",
                "coordinates": (0, 0, 10),
            },
        ]

        updated, errors = InformationConfiguration.apply_marker_values(
            Scene(),
            entries,
            {
                "config.marker.1": (10, 0, 0),
                "config.marker.2": (10, 0, 20),
            },
            linkages,
        )

        self.assertEqual(errors, [])
        self.assertEqual(updated, 4)
        self.assertEqual(
            (wheel_part.location.x, wheel_part.location.y, wheel_part.location.z),
            (10.0, 0.0, 0.0),
        )
        self.assertEqual(
            (wheel_part.orientation.x, wheel_part.orientation.y, wheel_part.orientation.z),
            (0.0, 0.0, 1.0),
        )
        self.assertEqual(
            (joint_marker.location.x, joint_marker.location.y, joint_marker.location.z),
            (8.0, 0.0, 10.0),
        )
        self.assertEqual(
            (joint_marker.orientation.x, joint_marker.orientation.y, joint_marker.orientation.z),
            (0.0, 0.0, 1.0),
        )


if __name__ == "__main__":
    unittest.main()

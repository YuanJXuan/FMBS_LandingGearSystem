# -*- coding: utf-8 -*-

import json
import re
import sys
import tempfile
import types
import unittest
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TEMPLATE_DIR / "Share"))

import StructuralParameterization
import InformationConfiguration


def _adm_object_index(adm_text):
    """Return named ADM objects together with their owning Part."""
    commands = re.findall(
        r"(?ms)!\s*adams_view_name='([^']+)'\s*\n"
        r"([A-Z]+)/([0-9]+)(.*?)(?=\n!)",
        adm_text,
    )
    names = {name.lower() for name, _kind, _command_id, _body in commands}
    part_names = {
        command_id: name.lower()
        for name, kind, command_id, _body in commands
        if kind == "PART"
    }
    part_offsets = {}
    for _name, kind, command_id, body in commands:
        if kind != "PART":
            continue
        qg_match = re.search(r"(?m)^, QG\s*=\s*([^\n]+)", body)
        part_offsets[command_id] = (
            tuple(
                float(value.strip().replace("D", "E"))
                for value in qg_match.group(1).split(",")[:3]
            )
            if qg_match
            else (0.0, 0.0, 0.0)
        )
    marker_parts = {}
    owned_objects = set()
    geometry = {}
    graphics = []
    for name, kind, command_id, body in commands:
        if kind == "MARKER":
            match = re.search(r"(?m)^, PART\s*=\s*([0-9]+)", body)
            if match and match.group(1) in part_names:
                part_name = part_names[match.group(1)]
                marker_parts[command_id] = part_name
                owned_objects.add((part_name, name.lower()))
                qp_match = re.search(r"(?m)^, QP\s*=\s*([^\n]+)", body)
                if qp_match:
                    local_location = tuple(
                        float(value.strip().replace("D", "E"))
                        for value in qp_match.group(1).split(",")[:3]
                    )
                    part_offset = part_offsets.get(match.group(1), (0.0, 0.0, 0.0))
                    geometry[(part_name, name.lower())] = {
                        "location": tuple(
                            local_location[index] + part_offset[index]
                            for index in range(3)
                        )
                    }
        elif kind == "GRAPHICS":
            graphics.append((name.lower(), body))
    for name, body in graphics:
        match = re.search(r"(?m)^, CM\s*=\s*([0-9]+)", body)
        if match and match.group(1) in marker_parts:
            key = (marker_parts[match.group(1)], name)
            owned_objects.add(key)
            length_match = re.search(r"(?m)^, LENGTH\s*=\s*([^,\n]+)", body)
            if length_match:
                geometry[key] = {
                    "length": float(
                        length_match.group(1).strip().replace("D", "E")
                    )
                }
    return names, owned_objects, geometry


def _adm_path_exists(path, names, owned_objects):
    normalized = path.strip().lstrip(".").lower()
    if normalized in names:
        return True
    if "." not in normalized:
        return False
    part_name, object_name = normalized.rsplit(".", 1)
    return (part_name, object_name) in owned_objects


class Vector:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


class Node:
    def __init__(self, x, y, z):
        self.location = Vector(x, y, z)


class Scene:
    Name = "ImportedModel"

    def __init__(self, nodes, fail_recompute=False):
        self.nodes = nodes
        self.fail_recompute = fail_recompute
        self.recompute_count = 0

    def getObject(self, path):
        return self.nodes.get(path)

    def recompute(self):
        self.recompute_count += 1
        if self.fail_recompute:
            raise RuntimeError("refresh failed")


def _parameter():
    return StructuralParameterization.normalize_parameter(
        {
            "id": "symmetric_width",
            "label": "左右间距",
            "driver": "ground.left",
            "axes": ["y"],
            "followers": [
                {
                    "path": "ground.right",
                    "operation": "delta",
                    "axes": ["y"],
                    "scale": {"y": -1},
                },
                {
                    "path": "ground.left_outer",
                    "operation": "delta",
                    "axes": ["y"],
                },
            ],
        }
    )


class StructuralParameterizationTests(unittest.TestCase):
    def setUp(self):
        self.previous_jusme = sys.modules.get("Jusme")
        sys.modules["Jusme"] = types.SimpleNamespace(Vector=Vector)

    def tearDown(self):
        if self.previous_jusme is None:
            sys.modules.pop("Jusme", None)
        else:
            sys.modules["Jusme"] = self.previous_jusme

    def _scene(self, fail_recompute=False):
        return Scene(
            {
                ".ImportedModel.ground.left": Node(10, -20, 30),
                ".ImportedModel.ground.right": Node(10, 20, 30),
                ".ImportedModel.ground.left_outer": Node(10, -25, 30),
            },
            fail_recompute=fail_recompute,
        )

    def test_applies_driver_and_scaled_follower_deltas(self):
        scene = self._scene()
        result = StructuralParameterization.apply_parameter(
            scene, _parameter(), (10, -30, 30)
        )

        self.assertTrue(result.success)
        self.assertEqual(result.updated, 3)
        self.assertEqual(scene.nodes[".ImportedModel.ground.left"].location.y, -30)
        self.assertEqual(scene.nodes[".ImportedModel.ground.right"].location.y, 30)
        self.assertEqual(
            scene.nodes[".ImportedModel.ground.left_outer"].location.y, -35
        )

    def test_rejects_changes_to_locked_axes(self):
        scene = self._scene()
        result = StructuralParameterization.apply_parameter(
            scene, _parameter(), (11, -30, 30)
        )

        self.assertFalse(result.success)
        self.assertIn("不允许修改X坐标", result.message)
        self.assertEqual(scene.nodes[".ImportedModel.ground.left"].location.y, -20)

    def test_rolls_back_all_targets_when_refresh_fails(self):
        scene = self._scene(fail_recompute=True)
        result = StructuralParameterization.apply_parameter(
            scene, _parameter(), (10, -30, 30)
        )

        self.assertFalse(result.success)
        self.assertEqual(scene.nodes[".ImportedModel.ground.left"].location.y, -20)
        self.assertEqual(scene.nodes[".ImportedModel.ground.right"].location.y, 20)
        self.assertEqual(
            scene.nodes[".ImportedModel.ground.left_outer"].location.y, -25
        )

    def test_loads_json_and_resolves_a_different_scene_root(self):
        raw = {"parameters": [{"id": "one", "driver": ".Old.ground.left", "axes": ["x"]}]}
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "structure_parameters.json"
            path.write_text(json.dumps(raw), encoding="utf-8")
            parameters = StructuralParameterization.load_parameter_file(str(path))

        self.assertEqual(len(parameters), 1)
        self.assertEqual(
            StructuralParameterization.driver_path(self._scene(), parameters[0]),
            ".ImportedModel.ground.left",
        )

    def test_model_package_configurations_reference_their_adm(self):
        model_expectations = {
            "template_nlg_retract": (14, 7),
            "template_nlg_drop": (14, 6),
            "template_nlg_turn": (14, 6),
            "template_full_drop": (14, 6),
            "template_full_brake": (14, 6),
            "template_mlg_drop": (7, 4),
            "template_mlg_brake": (7, 4),
        }
        for model_name, (parameter_count, coaxial_count) in model_expectations.items():
            with self.subTest(model=model_name):
                model_dir = TEMPLATE_DIR / "Model" / model_name
                config_path = (
                    model_dir / (model_name + "_structure_parameters.json")
                )
                adm_text = (model_dir / (model_name + ".adm")).read_text(
                    encoding="utf-8", errors="ignore"
                )
                adm_names, owned_objects, geometry = _adm_object_index(adm_text)
                parameters = StructuralParameterization.load_parameter_file(
                    str(config_path)
                )

                self.assertEqual(len(parameters), parameter_count)
                coaxial_groups = {
                    group["id"]: group
                    for parameter in parameters
                    for group in parameter.get("coaxial", [])
                }
                self.assertEqual(len(coaxial_groups), coaxial_count)

                if "nlg" in model_name or model_name.startswith("template_full_"):
                    self.assertTrue(
                        {
                            "shock_strut_axis",
                            "wheel_axle_axis",
                            "upper_torque_arm_axis",
                            "lower_torque_arm_axis",
                        }.issubset(coaxial_groups)
                    )
                    shock_paths = {
                        marker["path"]
                        for marker in coaxial_groups["shock_strut_axis"]["markers"]
                    }
                    self.assertTrue(
                        {
                            "waitong.MARKER_79",
                            "taotong.MARKER_80",
                            "taotong.MARKER_15",
                            "taotong.cm",
                        }.issubset(shock_paths)
                    )
                    parameter_by_id = {
                        parameter["id"]: parameter for parameter in parameters
                    }
                    expected_followers = {
                        "upper_torque_arm_start": {
                            "taotong.MARKER_72",
                            "shangniulibi.MARKER_73",
                        },
                        "torque_arm_elbow": {
                            "shangniulibi.MARKER_75",
                            "xianiulibi.MARKER_76",
                        },
                        "lower_torque_arm_end": {"huosaigan.MARKER_78"},
                    }
                    for parameter_id, expected_paths in expected_followers.items():
                        self.assertEqual(
                            {
                                follower["path"]
                                for follower in parameter_by_id[parameter_id]["followers"]
                            },
                            expected_paths,
                        )

                workbook = InformationConfiguration.load_information_configuration(
                    str(model_dir)
                )
                configured_targets = {
                    ".".join(item["target"].lstrip(".").split(".")[1:]).lower()
                    for item in workbook["markers"]
                }
                self.assertEqual(
                    configured_targets,
                    {parameter["driver"].lower() for parameter in parameters},
                )

                paths = []
                for parameter in parameters:
                    self.assertTrue(parameter["table_only"])
                    paths.append(parameter["driver"])
                    paths.extend(item["path"] for item in parameter["followers"])
                    paths.extend(parameter["coincident_with"])
                    paths.extend(parameter["recompute"])
                for group in coaxial_groups.values():
                    paths.extend((group["start"], group["end"]))
                    paths.extend(marker["path"] for marker in group["markers"])
                    paths.extend(
                        marker["cylinder"]
                        for marker in group["markers"]
                        if marker.get("cylinder")
                    )
                    paths.extend(
                        target["path"] for target in group["length_targets"]
                    )
                    for pair in group["coincident_pairs"]:
                        paths.extend((pair["first"], pair["second"]))
                    paths.extend(group["recompute"])
                for path in paths:
                    with self.subTest(model=model_name, path=path):
                        self.assertTrue(
                            _adm_path_exists(path, adm_names, owned_objects),
                            "{} 不包含配置对象 {}".format(model_name, path),
                        )

                for group in coaxial_groups.values():
                    start = geometry[tuple(group["start"].lower().split(".", 1))][
                        "location"
                    ]
                    end = geometry[tuple(group["end"].lower().split(".", 1))][
                        "location"
                    ]
                    axis_length = sum(
                        (end[index] - start[index]) ** 2 for index in range(3)
                    ) ** 0.5
                    for marker in group["markers"]:
                        marker_key = tuple(marker["path"].lower().split(".", 1))
                        actual = geometry[marker_key]["location"]
                        if marker.get("cylinder"):
                            cylinder_key = tuple(
                                marker["cylinder"].lower().split(".", 1)
                            )
                            fraction = (
                                geometry[cylinder_key]["length"]
                                * marker.get("cylinder_scale", 0.5)
                                / axis_length
                            )
                            if marker.get("distance_from", "start") == "end":
                                fraction = 1.0 - fraction
                        elif marker.get("distance") is not None:
                            fraction = float(marker["distance"]) / axis_length
                            if marker.get("distance_from", "start") == "end":
                                fraction = 1.0 - fraction
                        else:
                            fraction = float(marker["fraction"])
                        expected = tuple(
                            start[index]
                            + fraction * (end[index] - start[index])
                            for index in range(3)
                        )
                        for actual_value, expected_value in zip(actual, expected):
                            self.assertAlmostEqual(
                                actual_value,
                                expected_value,
                                delta=1.0e-2,
                                msg="{} 的 {} 初始位置与共轴规则不一致".format(
                                    model_name, marker["path"]
                                ),
                            )
                    for target in group["length_targets"]:
                        target_key = tuple(target["path"].lower().split(".", 1))
                        expected_length = (
                            axis_length * target["scale"] + target["offset"]
                        )
                        self.assertAlmostEqual(
                            geometry[target_key]["length"],
                            expected_length,
                            delta=1.0e-2,
                            msg="{} 的 {} 初始长度与共轴规则不一致".format(
                                model_name, target["path"]
                            ),
                        )

    def test_resolves_flattened_adm_part_names(self):
        wheel = Node(1, 2, 3)
        scene = Scene({".ImportedModel.lt_1_wheel_part": wheel})

        path, node = StructuralParameterization.resolve_object(
            scene, "lt_1.wheel_part"
        )

        self.assertEqual(path, ".ImportedModel.lt_1_wheel_part")
        self.assertIs(node, wheel)


if __name__ == "__main__":
    unittest.main()

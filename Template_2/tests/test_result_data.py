# -*- coding: utf-8 -*-

import json
import sys
import tempfile
import types
import unittest
from pathlib import Path


TEMPLATE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TEMPLATE_DIR / "Share"))

import ResultData


class FakeResultHandle:
    def __init__(self, model_info):
        self.model_info = model_info

    def getDataInfo(self):
        return json.dumps({"model_info": self.model_info})


class FakeDataLoader:
    def __init__(self, model_info, values):
        self.handle = FakeResultHandle(model_info)
        self.values = values
        self.loaded_path = ""

    def load_result_json(self, result_directory):
        self.loaded_path = result_directory
        return self.handle

    def getdata(self, offset, _handle):
        return self.values[offset]


class ResultDataTests(unittest.TestCase):
    def setUp(self):
        self.model_info = {
            "Joint": {
                "joint-key": {
                    "name": "JOINT_19",
                    "data_indices": {
                        "Element_Force": {
                            "component": {"Mag": 7},
                        }
                    },
                }
            }
        }

    def test_resolves_singular_component_metadata(self):
        offset = ResultData.resolve_result_offset(
            self.model_info,
            "Joint.JOINT_19.Element_Force.Mag",
        )
        self.assertEqual(offset, 7)

    def test_derives_workdir_result_folder_from_installed_template_path(self):
        with tempfile.TemporaryDirectory() as root:
            template_dir = Path(root) / "bin" / "Template" / "Template_2"
            share_dir = template_dir / "Share"
            share_dir.mkdir(parents=True)
            expected = Path(root) / "fmbs_workdir" / "result" / "object_data"

            resolved = ResultData.default_result_directory(str(share_dir))

        self.assertEqual(Path(resolved), expected)

    def test_prefers_jusme_work_directory_for_result_folder(self):
        with tempfile.TemporaryDirectory() as work_directory:
            expected = (
                Path(work_directory)
                / "fmbs_workdir"
                / "result"
                / "object_data"
            )

            resolved = ResultData.default_result_directory(
                "ignored/template/path",
                work_directory=work_directory,
            )

        self.assertEqual(Path(resolved), expected)

    def test_reads_runtime_work_directory_from_jusme(self):
        with tempfile.TemporaryDirectory() as work_directory:
            expected = (
                Path(work_directory)
                / "fmbs_workdir"
                / "result"
                / "object_data"
            )
            previous = sys.modules.get("Jusme")
            sys.modules["Jusme"] = types.SimpleNamespace(
                getWorkDir=lambda: work_directory
            )
            try:
                resolved = ResultData.default_result_directory(
                    "ignored/template/path"
                )
            finally:
                if previous is None:
                    sys.modules.pop("Jusme", None)
                else:
                    sys.modules["Jusme"] = previous

        self.assertEqual(Path(resolved), expected)

    def test_accepts_fmbs_workdir_itself_as_runtime_work_directory(self):
        with tempfile.TemporaryDirectory() as root:
            work_directory = Path(root) / "fmbs_workdir"
            expected = work_directory / "result" / "object_data"

            resolved = ResultData.default_result_directory(
                work_directory=work_directory,
            )

        self.assertEqual(Path(resolved), expected)

    def test_loads_configured_curve_and_accepts_parent_result_folder(self):
        with tempfile.TemporaryDirectory() as parent:
            object_data = Path(parent) / "object_data"
            object_data.mkdir()
            loader = FakeDataLoader(
                self.model_info,
                {0: [0.0, 0.1, 0.2], 7: [10.0, 20.0, 30.0]},
            )
            loaded = ResultData.load_configured_results(
                parent,
                [
                    {
                        "id": "config.postprocessing.1",
                        "label": "轮胎垂向载荷",
                        "target": "Joint.JOINT_19.Element_Force.Mag",
                        "x_unit": "s",
                        "y_unit": "N",
                    }
                ],
                data_loader=loader,
            )

        self.assertEqual(loader.loaded_path, str(object_data))
        self.assertEqual(loaded["errors"], [])
        self.assertEqual(loaded["curves"][0]["x"], [0.0, 0.1, 0.2])
        self.assertEqual(loaded["curves"][0]["y"], [10.0, 20.0, 30.0])
        self.assertEqual(loaded["curves"][0]["y_unit"], "N")

    def test_one_missing_variable_does_not_hide_valid_curves(self):
        with tempfile.TemporaryDirectory() as result_directory:
            loader = FakeDataLoader(
                self.model_info,
                {0: [0.0, 1.0], 7: [100.0, 200.0]},
            )
            loaded = ResultData.load_configured_results(
                result_directory,
                [
                    {
                        "id": "valid",
                        "label": "有效曲线",
                        "target": "Joint.JOINT_19.Element_Force.Mag",
                    },
                    {
                        "id": "missing",
                        "label": "缺失曲线",
                        "target": "Joint.UNKNOWN.Element_Force.Mag",
                    },
                ],
                data_loader=loader,
            )

        self.assertEqual([curve["id"] for curve in loaded["curves"]], ["valid"])
        self.assertEqual(len(loaded["errors"]), 1)
        self.assertIn("缺失曲线", loaded["errors"][0])

    def test_builds_work_diagram_from_two_curve_y_series(self):
        curves = [
            {
                "id": "displacement",
                "label": "缓冲器位移",
                "target": "Joint.slide.Displacement.Mag",
                "x": [0.0, 1.0, 2.0],
                "y": [0.0, 10.0, 5.0],
                "x_unit": "s",
                "y_unit": "mm",
            },
            {
                "id": "force",
                "label": "轮胎垂向载荷",
                "target": "Joint.wheel.Element_Force.Mag",
                "x": [0.0, 1.0, 2.0],
                "y": [0.0, 100.0, 40.0],
                "x_unit": "s",
                "y_unit": "N",
            },
        ]
        built = ResultData.build_work_diagrams(
            curves,
            [
                {
                    "id": "work.1",
                    "label": "缓冲器功量图",
                    "x_source": "缓冲器位移",
                    "y_source": "轮胎垂向载荷",
                    "x_unit": "mm",
                    "y_unit": "N",
                }
            ],
        )

        self.assertEqual(built["errors"], [])
        self.assertEqual(len(built["curves"]), 1)
        diagram = built["curves"][0]
        self.assertEqual(diagram["x"], [0.0, 10.0, 5.0])
        self.assertEqual(diagram["y"], [0.0, 100.0, 40.0])
        self.assertEqual(diagram["x_label"], "缓冲器位移")
        self.assertEqual(diagram["y_label"], "轮胎垂向载荷")

    def test_work_diagram_interpolates_second_curve_on_common_time(self):
        curves = [
            {
                "id": "x",
                "label": "位移",
                "x": [0.0, 1.0, 2.0],
                "y": [0.0, 5.0, 10.0],
            },
            {
                "id": "y",
                "label": "载荷",
                "x": [0.0, 2.0],
                "y": [0.0, 200.0],
            },
        ]
        built = ResultData.build_work_diagrams(
            curves,
            [
                {
                    "id": "work",
                    "label": "功量图",
                    "x_source": "x",
                    "y_source": "y",
                }
            ],
        )

        self.assertEqual(built["errors"], [])
        self.assertEqual(built["curves"][0]["x"], [0.0, 5.0, 10.0])
        self.assertEqual(built["curves"][0]["y"], [0.0, 100.0, 200.0])

    def test_work_diagram_reports_a_missing_source_without_hiding_others(self):
        curves = [
            {"id": "x", "label": "位移", "x": [0, 1], "y": [0, 1]},
            {"id": "y", "label": "载荷", "x": [0, 1], "y": [0, 2]},
        ]
        built = ResultData.build_work_diagrams(
            curves,
            [
                {
                    "id": "valid",
                    "label": "有效功量图",
                    "x_source": "x",
                    "y_source": "y",
                },
                {
                    "id": "missing",
                    "label": "缺失功量图",
                    "x_source": "x",
                    "y_source": "unknown",
                },
            ],
        )

        self.assertEqual([curve["id"] for curve in built["curves"]], ["valid"])
        self.assertEqual(len(built["errors"]), 1)
        self.assertIn("缺失功量图", built["errors"][0])


if __name__ == "__main__":
    unittest.main()

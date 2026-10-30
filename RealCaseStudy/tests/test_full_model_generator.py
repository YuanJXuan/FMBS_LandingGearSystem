# -*- coding: utf-8 -*-

import os
import re
import sys
import tempfile
import unittest
from pathlib import Path


SHARE_DIR = Path(__file__).resolve().parents[1] / "Share"
MODEL_FULL_DIR = Path(__file__).resolve().parents[1] / "Model_Full"
sys.path.insert(0, str(SHARE_DIR))

import FullModelGenerator


def _record_block(text, record_type, record_id):
    pattern = re.compile(
        r"^{}\/{}\s*$([\s\S]*?)(?=^[A-Z_]+\/[0-9]+\s*$|\Z)".format(
            record_type,
            record_id,
        ),
        re.MULTILINE,
    )
    match = pattern.search(text)
    if not match:
        raise AssertionError("missing {}/{}".format(record_type, record_id))
    return match.group(0)


def _triplet(block, name):
    match = re.search(
        r"^,\s*{}\s*=\s*([^\r\n]+)".format(name),
        block,
        re.MULTILINE,
    )
    if not match:
        raise AssertionError("missing {}".format(name))
    return tuple(float(item.strip()) for item in match.group(1).split(","))


class FullModelGeneratorTests(unittest.TestCase):
    def test_lists_and_resolves_the_configured_source_pair(self):
        adm_files = FullModelGenerator.list_adm_files(str(MODEL_FULL_DIR))
        self.assertEqual(
            ["mlg.adm", "nlg.adm"],
            [Path(path).name for path in adm_files],
        )
        configuration = FullModelGenerator.load_configuration(
            str(MODEL_FULL_DIR),
            str(MODEL_FULL_DIR / "nlg.adm"),
            str(MODEL_FULL_DIR / "mlg.adm"),
        )
        self.assertEqual("前起 nlg + 主起 mlg", configuration["combination_name"])

    def test_rejects_an_unconfigured_source_pair(self):
        with self.assertRaises(FullModelGenerator.FullModelGenerationError):
            FullModelGenerator.load_configuration(
                str(MODEL_FULL_DIR),
                str(MODEL_FULL_DIR / "mlg.adm"),
                str(MODEL_FULL_DIR / "nlg.adm"),
            )

    def test_reads_both_reference_anchor_positions(self):
        anchors = FullModelGenerator.read_anchor_positions(str(MODEL_FULL_DIR))
        self.assertEqual((4938.0, 0.0, -57.0), anchors["nlg"])
        self.assertEqual((9380.4, 0.0, -57.0), anchors["mlg"])

    def test_generates_one_model_and_moves_each_assembly_independently(self):
        with tempfile.TemporaryDirectory() as output_dir:
            result = FullModelGenerator.generate_combined_adm(
                str(MODEL_FULL_DIR),
                (5000.0, 100.0, -100.0),
                (9500.0, 200.0, -200.0),
                output_dir,
                "combined_test",
                str(MODEL_FULL_DIR / "nlg.adm"),
                str(MODEL_FULL_DIR / "mlg.adm"),
            )
            text = Path(result["adm_path"]).read_text(encoding="utf-8")

        self.assertTrue(text.startswith("Adams View model name: combined_test"))
        self.assertEqual(
            str(MODEL_FULL_DIR / "nlg.adm"),
            result["nlg_adm"],
        )
        self.assertEqual(
            str(MODEL_FULL_DIR / "mlg.adm"),
            result["mlg_adm"],
        )
        self.assertEqual(
            (4897.0, 0.0, -57.0),
            _triplet(_record_block(text, "MARKER", 85), "QP"),
        )
        self.assertEqual(
            (9380.4, 0.0, -57.0),
            _triplet(_record_block(text, "MARKER", 1115), "QP"),
        )

        # The front and main wheels follow their own assembly translations.
        self.assertEqual(
            (5059.0, -200.0, -1800.0),
            _triplet(_record_block(text, "PART", 1026), "QG"),
        )
        self.assertEqual(
            (9991.6, 1575.0, -1792.0),
            _triplet(_record_block(text, "PART", 1030), "QG"),
        )

        # The common road is deliberately kept fixed.
        self.assertEqual(
            (0.0, 0.0, -3317.0),
            _triplet(_record_block(text, "PART", 1025), "QG"),
        )

        # Cross-assembly joint markers are corrected in local coordinates so
        # the fixed and translational joints remain assembled.
        self.assertEqual(
            (4880.4, -100.0, 43.0),
            _triplet(_record_block(text, "MARKER", 1125), "QP"),
        )
        self.assertEqual(
            (9500.0, 200.0, 3117.0),
            _triplet(_record_block(text, "MARKER", 1155), "QP"),
        )

    def test_rejects_non_finite_coordinates(self):
        with tempfile.TemporaryDirectory() as output_dir:
            with self.assertRaises(FullModelGenerator.FullModelGenerationError):
                FullModelGenerator.generate_combined_adm(
                    str(MODEL_FULL_DIR),
                    (float("nan"), 0.0, 0.0),
                    (0.0, 0.0, 0.0),
                    output_dir,
                )


if __name__ == "__main__":
    unittest.main()

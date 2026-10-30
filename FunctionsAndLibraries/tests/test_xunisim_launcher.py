# -*- coding: utf-8 -*-
"""Validate the Linux toolbar entry and execute its real Bash script safely."""

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "start_xunisim.sh"
spec = importlib.util.spec_from_file_location("xunisim_launcher_under_test", str(ROOT / "Xunisim.py"))
launcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launcher)


class XunisimDeploymentTests(unittest.TestCase):
    def test_script_stays_beside_entrypoint(self):
        self.assertEqual(SCRIPT, Path(launcher.START_SCRIPT))

    def test_relocated_installations_launch_their_sibling_program_from_unrelated_cwd(self):
        with tempfile.TemporaryDirectory(prefix="xunisim relocation ") as temp:
            root = Path(temp)
            unrelated = root / "unrelated working directory"
            unrelated.mkdir()
            # A same-named program in the working directory must not be selected.
            (unrelated / "XUnisim-Application").write_text("decoy", encoding="utf-8")
            bash = root / "bash"
            bash.write_text("test interpreter; never executed", encoding="utf-8")
            bash.chmod(0o755)
            previous_cwd = os.getcwd()
            try:
                os.chdir(str(unrelated))
                for relative_dir in ("user one/installation", "另一位置/软件 安装"):
                    with self.subTest(location=relative_dir):
                        install_dir = root / relative_dir
                        entry_dir = install_dir / "Template" / "FunctionsAndLibraries"
                        entry_dir.mkdir(parents=True)
                        shutil.copyfile(ROOT / "Xunisim.py", entry_dir / "Xunisim.py")
                        shutil.copyfile(SCRIPT, entry_dir / "start_xunisim.sh")
                        program = install_dir / "XUnisim-Application"
                        program.write_text("test application; never executed", encoding="utf-8")
                        program.chmod(0o755)
                        relocated_spec = importlib.util.spec_from_file_location(
                            "relocated_xunisim", str(entry_dir / "Xunisim.py")
                        )
                        relocated = importlib.util.module_from_spec(relocated_spec)
                        relocated_spec.loader.exec_module(relocated)
                        start = Mock(return_value=(True, 123))
                        with patch.object(relocated, "BASH_PROGRAM", str(bash)):
                            self.assertTrue(relocated.launch_xunisim(start, "linux"))
                        start.assert_called_once_with(
                            str(bash), [str(entry_dir / "start_xunisim.sh"), str(program)], str(install_dir)
                        )
            finally:
                os.chdir(previous_cwd)

    def test_script_is_utf8_without_bom_and_uses_linux_line_endings(self):
        content = SCRIPT.read_bytes()
        content.decode("utf-8")
        self.assertTrue(content.startswith(b"#!/bin/bash\n"))
        self.assertNotIn(b"\r", content)


class XunisimLauncherTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="xunisim launcher ")
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.program = root / "install with spaces" / "XUnisim-Application"
        self.program.parent.mkdir()
        self.program.write_text("placeholder", encoding="utf-8")
        self.script = root / "start xunisim.sh"
        self.script.write_text("placeholder", encoding="utf-8")
        self.bash = root / "bash"
        self.bash.write_text("placeholder", encoding="utf-8")
        for path in (self.program, self.script, self.bash):
            path.chmod(0o755)
        constants = patch.multiple(
            launcher, XUNISIM_PROGRAM=str(self.program), START_SCRIPT=str(self.script),
            BASH_PROGRAM=str(self.bash),
        )
        constants.start()
        self.addCleanup(constants.stop)
        self.start = Mock(return_value=(True, 123))

    def test_linux_launch_passes_script_and_program_as_separate_arguments(self):
        self.assertTrue(launcher.launch_xunisim(self.start, "linux"))
        self.start.assert_called_once_with(
            str(self.bash), [str(self.script), str(self.program)], str(self.program.parent)
        )

    def test_windows_does_not_start_or_open_configuration(self):
        with self.assertRaisesRegex(launcher.LaunchError, "仅支持 Linux"):
            launcher.launch_xunisim(self.start, "win32")
        self.start.assert_not_called()

    def test_missing_program_shows_calculated_path_and_expected_layout(self):
        self.program.unlink()
        with self.assertRaises(launcher.LaunchError) as error:
            launcher.launch_xunisim(self.start, "linux")
        self.assertIn(str(self.program), str(error.exception))
        self.assertIn("Template 文件夹同级", str(error.exception))
        self.start.assert_not_called()

    def test_missing_files_are_reported_before_start(self):
        original = os.path.isfile
        for missing in (self.program, self.script, self.bash):
            with self.subTest(missing=missing), patch.object(
                launcher.os.path, "isfile", side_effect=lambda path: path != str(missing) and original(path)
            ):
                with self.assertRaises(launcher.LaunchError):
                    launcher.launch_xunisim(self.start, "linux")
        self.start.assert_not_called()

    def test_file_permissions_are_checked_before_start(self):
        original = os.access
        for denied, mode in ((self.program, os.X_OK), (self.script, os.R_OK), (self.bash, os.X_OK)):
            with self.subTest(denied=denied), patch.object(
                launcher.os, "access",
                side_effect=lambda path, flag: False if (path, flag) == (str(denied), mode) else original(path, flag),
            ):
                with self.assertRaises(launcher.LaunchError):
                    launcher.launch_xunisim(self.start, "linux")
        self.start.assert_not_called()

    def test_boolean_and_tuple_launch_results(self):
        for result in (False, (False, 0)):
            with self.subTest(result=result), self.assertRaises(launcher.LaunchError):
                launcher.launch_xunisim(Mock(return_value=result), "linux")
        for result in (True, (True, 123)):
            with self.subTest(result=result):
                self.assertTrue(launcher.launch_xunisim(Mock(return_value=result), "linux"))

    def test_process_error_is_reported(self):
        with self.assertRaisesRegex(launcher.LaunchError, "denied"):
            launcher.launch_xunisim(Mock(side_effect=OSError("denied")), "linux")


def find_bash():
    if sys.platform.startswith("linux"):
        return shutil.which("bash")
    # Git Bash can validate the shell workflow on a Windows development machine.
    for path in ("C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe"):
        if Path(path).is_file():
            return path
    return None


BASH = find_bash()


@unittest.skipUnless(BASH, "Bash is not installed")
class XunisimScriptTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="xunisim shell ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.program = self.root / "install with spaces & symbols" / "XUnisim-Application"
        self.program.parent.mkdir()
        self.output = self.root / "received.txt"
        self.environment = dict(os.environ)
        self.environment["XDG_STATE_HOME"] = (self.root / "state").as_posix()
        self.environment["TEST_OUTPUT"] = self.output.as_posix()
        self.environment["EXPECTED_WORKDIR"] = self.program.parent.as_posix()

    def make_program(self, body):
        self.program.write_bytes(("#!/bin/bash\n" + body + "\n").encode("utf-8"))
        self.program.chmod(0o755)

    def run_script(self, *arguments):
        return subprocess.run(
            [BASH, SCRIPT.as_posix()] + list(arguments), cwd=str(self.root),
            env=self.environment, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            encoding="utf-8", timeout=10,
        )

    def test_bash_syntax(self):
        result = subprocess.run([BASH, "-n", SCRIPT.as_posix()], capture_output=True, timeout=10)
        self.assertEqual(0, result.returncode, result.stderr)

    def test_script_launches_program_from_its_directory_and_logs_output(self):
        self.make_program(
            '[[ "$PWD" -ef "$EXPECTED_WORKDIR" ]] || exit 9\n'
            'printf "%s\\n" "$#" > "$TEST_OUTPUT"\nprintf "software started\\n"'
        )
        result = self.run_script(self.program.as_posix())
        self.assertEqual(0, result.returncode, result.stderr)
        received = self.output.read_text(encoding="utf-8").splitlines()
        self.assertEqual(["0"], received)
        log = (self.root / "state" / "fmbs" / "xunisim.log").read_text(encoding="utf-8")
        self.assertIn("Xunisim launch:", log)
        self.assertIn("software started", log)
        self.assertEqual(0, self.run_script(self.program.as_posix()).returncode)
        log = (self.root / "state" / "fmbs" / "xunisim.log").read_text(encoding="utf-8")
        self.assertEqual(2, log.count("software started"))

    def test_missing_program_and_missing_argument_report_errors(self):
        result = self.run_script((self.root / "missing program").as_posix())
        self.assertEqual(127, result.returncode)
        self.assertIn("not found", result.stderr)
        result = self.run_script()
        self.assertEqual(2, result.returncode)
        self.assertIn("Usage:", result.stderr)

    def test_program_failure_is_recorded_in_log_and_exit_status(self):
        self.make_program('printf "missing test dependency\\n" >&2\nexit 7')
        result = self.run_script(self.program.as_posix())
        self.assertEqual(7, result.returncode)
        log = (self.root / "state" / "fmbs" / "xunisim.log").read_text(encoding="utf-8")
        self.assertIn("missing test dependency", log)

    @unittest.skipUnless(sys.platform.startswith("linux"), "Requires Linux executable permission semantics")
    def test_non_executable_program_is_rejected(self):
        self.make_program("exit 0")
        self.program.chmod(0o644)
        result = self.run_script(self.program.as_posix())
        self.assertEqual(126, result.returncode)
        self.assertIn("not executable", result.stderr)


if __name__ == "__main__":
    unittest.main()

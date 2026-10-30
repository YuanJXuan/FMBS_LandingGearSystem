# -*- coding: utf-8 -*-
"""Linux 工具栏入口：通过随附的 Bash 脚本启动 Xunisim。"""

import os
import sys


# 部署结构：<安装目录>/Template/FunctionsAndLibraries/Xunisim.py。
# XUnisim-Application 与 Template 同级，不依赖用户名或终端当前目录。
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.dirname(SCRIPT_DIR)
XUNISIM_PROGRAM = os.path.join(os.path.dirname(TEMPLATE_DIR), "XUnisim-Application")
START_SCRIPT = os.path.join(SCRIPT_DIR, "start_xunisim.sh")
BASH_PROGRAM = "/bin/bash"


class LaunchError(ValueError):
    """可向用户显示的启动错误。"""


def launch_xunisim(start_detached=None, platform=None):
    platform = sys.platform if platform is None else platform
    if not platform.startswith("linux"):
        raise LaunchError("此按钮仅支持 Linux，请在 Linux 系统中的界面上启动 Xunisim。")
    if not os.path.isfile(START_SCRIPT):
        raise LaunchError("缺少启动脚本，请将 start_xunisim.sh 与 Xunisim.py 放在同一目录：\n" + START_SCRIPT)
    if not os.access(START_SCRIPT, os.R_OK):
        raise LaunchError("启动脚本无法读取，请检查文件权限：\n" + START_SCRIPT)
    if not os.path.isfile(XUNISIM_PROGRAM):
        raise LaunchError(
            "未找到 Xunisim 启动程序。XUnisim-Application 应与 Template 文件夹同级。\n"
            "自动定位的路径：\n" + XUNISIM_PROGRAM
        )
    if not os.access(XUNISIM_PROGRAM, os.X_OK):
        raise LaunchError("Xunisim 启动程序没有执行权限，请检查文件权限：\n" + XUNISIM_PROGRAM)
    if not os.path.isfile(BASH_PROGRAM) or not os.access(BASH_PROGRAM, os.X_OK):
        raise LaunchError("未找到可执行的 /bin/bash，无法运行 Xunisim 启动脚本。")

    if start_detached is None:
        from PySide2.QtCore import QProcess
        start_detached = QProcess.startDetached
    try:
        # 参数单独传递，支持包含空格的目录；不拼接 shell 命令。
        result = start_detached(
            BASH_PROGRAM, [START_SCRIPT, XUNISIM_PROGRAM], os.path.dirname(XUNISIM_PROGRAM)
        )
    except (OSError, RuntimeError, TypeError) as exc:
        raise LaunchError("无法执行 Xunisim 启动脚本：\n{}".format(exc)) from exc
    success = result[0] if isinstance(result, tuple) else result
    if not success:
        raise LaunchError("无法执行 Xunisim 启动脚本，请检查 Bash 和脚本文件权限。")
    # 此返回值仅确认启动脚本已交给系统执行；软件运行输出由脚本记录。
    return True


def main():
    from PySide2.QtWidgets import QApplication, QMessageBox

    app = QApplication.instance() or QApplication(sys.argv)
    try:
        return launch_xunisim()
    except LaunchError as exc:
        QMessageBox.warning(app.activeWindow(), "Xunisim 启动失败", str(exc))
        return False


if __name__ == "__main__":
    main()

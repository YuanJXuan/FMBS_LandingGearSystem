"""CMD 模型转换页面。

用于选择 Adams CMD 文件，并通过 JusmeModel_v5 生成完整 Python 模型脚本
或 ADM 公式补丁。该页面既可以由茉莉平台工具栏启动，也可以独立启动。
"""

import os
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QPlainTextEdit,
    QVBoxLayout,
)


script_dir = os.path.dirname(os.path.abspath(__file__))
CMD_dir = os.path.join(script_dir, "CMDToPy")

if CMD_dir not in sys.path:
    sys.path.append(CMD_dir)

import JusmeModel_v5


class CMDConverterDialog(QDialog):
    """选择 CMD 输入文件和 PY 输出文件并执行转换。"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._auto_output_path = ""
        self._auto_patch_output_path = ""
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("CMD 模型转换")
        self.setMinimumSize(720, 460)

        title_label = QLabel("CMD 模型转换")
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")

        description_label = QLabel(
            "选择一个 Adams CMD 文件，可以生成完整 Python 模型脚本，"
            "也可以单独生成 ADM 导入所需的补丁脚本。"
        )
        description_label.setWordWrap(True)

        file_group = QGroupBox("文件设置")
        file_form = QFormLayout(file_group)

        self.input_path_edit = QLineEdit()
        self.input_path_edit.setPlaceholderText("请选择要转换的 .cmd 文件")
        self.input_path_edit.textChanged.connect(self._update_convert_button)

        input_button = QPushButton("选择文件…")
        input_button.clicked.connect(self.select_input_file)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_path_edit, 1)
        input_layout.addWidget(input_button)
        file_form.addRow("CMD 文件：", input_layout)

        self.output_path_edit = QLineEdit()
        self.output_path_edit.setPlaceholderText("请选择完整模型 .py 文件保存位置")
        self.output_path_edit.textChanged.connect(self._output_path_changed)

        output_button = QPushButton("选择位置…")
        output_button.clicked.connect(self.select_output_file)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_path_edit, 1)
        output_layout.addWidget(output_button)
        file_form.addRow("完整 PY 文件：", output_layout)

        self.patch_output_path_edit = QLineEdit()
        self.patch_output_path_edit.setPlaceholderText(
            "请选择 ADM 补丁 .py 文件保存位置"
        )
        self.patch_output_path_edit.textChanged.connect(
            self._patch_output_path_changed
        )

        patch_output_button = QPushButton("选择位置…")
        patch_output_button.clicked.connect(self.select_patch_output_file)

        patch_output_layout = QHBoxLayout()
        patch_output_layout.addWidget(self.patch_output_path_edit, 1)
        patch_output_layout.addWidget(patch_output_button)
        file_form.addRow("补丁 PY 文件：", patch_output_layout)

        result_group = QGroupBox("转换结果")
        result_layout = QVBoxLayout(result_group)

        self.status_label = QLabel("等待选择文件")
        self.status_label.setWordWrap(True)
        self.result_edit = QPlainTextEdit()
        self.result_edit.setReadOnly(True)
        self.result_edit.setPlaceholderText("转换完成后，这里会显示转换统计和提示信息。")

        result_layout.addWidget(self.status_label)
        result_layout.addWidget(self.result_edit, 1)

        self.convert_button = QPushButton("生成完整 PY")
        self.convert_button.setEnabled(False)
        self.convert_button.setMinimumHeight(34)
        self.convert_button.clicked.connect(self.convert_file)

        self.patch_button = QPushButton("生成 ADM 补丁")
        self.patch_button.setEnabled(False)
        self.patch_button.setMinimumHeight(34)
        self.patch_button.clicked.connect(self.convert_patch_file)

        close_button = QPushButton("关闭")
        close_button.setMinimumHeight(34)
        close_button.clicked.connect(self.close)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.convert_button)
        button_layout.addWidget(self.patch_button)
        button_layout.addWidget(close_button)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(title_label)
        main_layout.addWidget(description_label)
        main_layout.addSpacing(8)
        main_layout.addWidget(file_group)
        main_layout.addWidget(result_group, 1)
        main_layout.addLayout(button_layout)

    def select_input_file(self):
        current_path = self.input_path_edit.text().strip()
        initial_dir = (
            os.path.dirname(current_path)
            if current_path and os.path.isdir(os.path.dirname(current_path))
            else script_dir
        )
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "选择 CMD 文件",
            initial_dir,
            "Adams CMD 文件 (*.cmd);;所有文件 (*.*)",
        )
        if not file_path:
            return

        old_auto_path = self._auto_output_path
        old_auto_patch_path = self._auto_patch_output_path
        self.input_path_edit.setText(os.path.normpath(file_path))

        suggested_output = os.path.splitext(file_path)[0] + ".py"
        suggested_patch_output = os.path.splitext(file_path)[0] + "_patch.py"
        current_output = self.output_path_edit.text().strip()
        current_patch_output = self.patch_output_path_edit.text().strip()
        if not current_output or current_output == old_auto_path:
            self._set_auto_output_path(suggested_output)
        if not current_patch_output or current_patch_output == old_auto_patch_path:
            self._set_auto_patch_output_path(suggested_patch_output)

        self.status_label.setText("文件已选择，可以开始转换。")
        self.result_edit.clear()

    def select_output_file(self):
        input_path = self.input_path_edit.text().strip()
        current_output = self.output_path_edit.text().strip()

        if current_output:
            suggested_path = current_output
        elif input_path:
            suggested_path = os.path.splitext(input_path)[0] + ".py"
        else:
            suggested_path = os.path.join(script_dir, "converted_model.py")

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "保存 Python 文件",
            suggested_path,
            "Python 文件 (*.py);;所有文件 (*.*)",
        )
        if not file_path:
            return

        self._auto_output_path = ""
        self.output_path_edit.setText(self._ensure_py_extension(file_path))

    def select_patch_output_file(self):
        input_path = self.input_path_edit.text().strip()
        current_output = self.patch_output_path_edit.text().strip()

        if current_output:
            suggested_path = current_output
        elif input_path:
            suggested_path = os.path.splitext(input_path)[0] + "_patch.py"
        else:
            suggested_path = os.path.join(script_dir, "model_patch.py")

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "保存 ADM 补丁文件",
            suggested_path,
            "Python 文件 (*.py);;所有文件 (*.*)",
        )
        if not file_path:
            return

        self._auto_patch_output_path = ""
        self.patch_output_path_edit.setText(self._ensure_py_extension(file_path))

    def _set_auto_output_path(self, file_path):
        normalized_path = os.path.normpath(file_path)
        self._auto_output_path = normalized_path
        self.output_path_edit.setText(normalized_path)

    def _set_auto_patch_output_path(self, file_path):
        normalized_path = os.path.normpath(file_path)
        self._auto_patch_output_path = normalized_path
        self.patch_output_path_edit.setText(normalized_path)

    def _output_path_changed(self, file_path):
        if file_path.strip() != self._auto_output_path:
            self._auto_output_path = ""
        self._update_convert_button()

    def _patch_output_path_changed(self, file_path):
        if file_path.strip() != self._auto_patch_output_path:
            self._auto_patch_output_path = ""
        self._update_convert_button()

    def _update_convert_button(self):
        has_input = bool(self.input_path_edit.text().strip())
        has_output = bool(self.output_path_edit.text().strip())
        has_patch_output = bool(self.patch_output_path_edit.text().strip())
        self.convert_button.setEnabled(has_input and has_output)
        self.patch_button.setEnabled(has_input and has_patch_output)

    @staticmethod
    def _ensure_py_extension(file_path):
        root, extension = os.path.splitext(file_path)
        if extension.lower() == ".py":
            return os.path.normpath(file_path)
        if extension:
            return os.path.normpath(root + ".py")
        return os.path.normpath(file_path + ".py")

    def _validated_paths(self, patch_mode=False):
        input_path = os.path.abspath(self.input_path_edit.text().strip())
        output_edit = (
            self.patch_output_path_edit if patch_mode else self.output_path_edit
        )
        output_path = os.path.abspath(
            self._ensure_py_extension(output_edit.text().strip())
        )

        if not os.path.isfile(input_path):
            raise ValueError("选择的 CMD 文件不存在或不是有效文件。")
        if os.path.splitext(input_path)[1].lower() != ".cmd":
            raise ValueError("输入文件必须是 .cmd 文件。")
        if patch_mode and os.path.splitext(input_path)[0].lower().endswith("_hps"):
            raise ValueError(
                "补丁必须由完整模型 CMD 生成，不能选择 *_hps.cmd 硬点文件。"
            )

        output_dir = os.path.dirname(output_path)
        if not os.path.isdir(output_dir):
            raise ValueError("输出目录不存在，请重新选择保存位置。")
        if os.path.normcase(input_path) == os.path.normcase(output_path):
            raise ValueError("输入文件和输出文件不能是同一个文件。")

        self.input_path_edit.setText(os.path.normpath(input_path))
        output_edit.setText(os.path.normpath(output_path))
        return input_path, output_path

    def convert_file(self):
        self._run_conversion(patch_mode=False)

    def convert_patch_file(self):
        self._run_conversion(patch_mode=True)

    def _run_conversion(self, patch_mode=False):
        try:
            input_path, output_path = self._validated_paths(patch_mode)
        except ValueError as exc:
            QMessageBox.warning(self, "文件设置有误", str(exc))
            return

        action_name = "ADM 补丁生成" if patch_mode else "完整 PY 转换"

        if os.path.exists(output_path):
            answer = QMessageBox.question(
                self,
                "确认覆盖",
                "目标 Python 文件已经存在，是否覆盖？",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if answer != QMessageBox.Yes:
                return

        self.convert_button.setEnabled(False)
        self.patch_button.setEnabled(False)
        self.status_label.setText("正在{}，请稍候…".format(action_name))
        self.result_edit.clear()
        QApplication.processEvents()

        try:
            converter = (
                JusmeModel_v5.convert_patch_file
                if patch_mode
                else JusmeModel_v5.convert_file
            )
            destination, report = converter(input_path, output_path)
            self._show_conversion_result(
                destination, report, patch_mode=patch_mode
            )
        except Exception as exc:
            self.status_label.setText("{}失败。".format(action_name))
            self.result_edit.setPlainText(
                "{}: {}".format(type(exc).__name__, exc)
            )
            QMessageBox.critical(
                self,
                "{}失败".format(action_name),
                "{}失败，请查看页面中的错误信息。".format(action_name),
            )
        finally:
            self._update_convert_button()

    def _show_conversion_result(self, destination, report, patch_mode=False):
        warning_count = len(report.warnings)
        has_remaining = report.unsupported_count or report.deferred_count
        result_name = "ADM 补丁" if patch_mode else "完整 Python 模型"

        summary = [
            "输出文件：{}".format(destination),
            "CMD 命令块总数：{}".format(report.total_blocks),
            "已生成补丁步骤：{}".format(report.converted_blocks)
            if patch_mode
            else "已转换：{}".format(report.converted_blocks),
            "暂不支持：{}".format(report.unsupported_count),
            "已识别但未重建：{}".format(report.deferred_count),
            "其他提示：{}".format(warning_count),
        ]

        if report.resource_directory:
            summary.extend(
                [
                    "资源目录：{}".format(report.resource_directory),
                    "已准备轮胎/路面资源：{}".format(
                        len(report.resource_files)
                    ),
                    "缺少轮胎/路面资源：{}".format(
                        len(report.missing_resources)
                    ),
                ]
            )

        summary.extend(
            [
                "",
                "详细报告：",
                report.as_text().rstrip(),
            ]
        )
        self.result_edit.setPlainText("\n".join(summary))

        if has_remaining or warning_count:
            self.status_label.setText(
                "{}已生成，但部分命令需要人工检查。".format(result_name)
            )
            QMessageBox.warning(
                self,
                "{}完成".format(result_name),
                "{}已生成，但部分命令需要人工检查，详情请查看转换结果。".format(
                    result_name
                ),
            )
        else:
            self.status_label.setText("{}生成成功。".format(result_name))
            QMessageBox.information(
                self,
                "{}生成成功".format(result_name),
                "{}已生成：\n{}".format(result_name, destination),
            )


def main():
    app = QApplication.instance()
    owns_application = app is None
    if owns_application:
        app = QApplication(sys.argv)

    dialog = CMDConverterDialog()
    dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowStaysOnTopHint)
    dialog.show()

    if owns_application:
        app.exec_()
    return dialog


if __name__ == "__main__":
    _cmd_converter_dialog = main()

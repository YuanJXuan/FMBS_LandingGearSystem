# Xunisim 多学科仿真入口（Linux）

在 Linux 中点击 Template_2 工具栏的“多学科仿真”按钮，即可通过 Bash 脚本启动：

```text
/home/gaojunqi/qljqj-app/bin/XUnisim-Application
```

启动时以程序所在的 `/home/gaojunqi/qljqj-app/bin` 为工作目录。入口不再显示路径设置窗口，也不读取之前保存的启动设置。Windows 中点击会提示仅支持 Linux。

部署时保留同一目录中的 `Xunisim.py`、`start_xunisim.sh` 和 `Xunisim.png`。Python 入口向脚本传入上面的安装路径，脚本负责切换目录并执行软件。按钮通过 `/bin/bash` 读取脚本，因此脚本本身不需要执行权限；Xunisim 程序需要执行权限。脚本使用 UTF-8 和 Linux 的 LF 换行。

若软件未显示窗口，可以查看当前用户的日志：

```text
~/.local/state/fmbs/xunisim.log
```

若系统设置了 `XDG_STATE_HOME`，日志位于该目录下的 `fmbs/xunisim.log`。日志追加保存本次启动时间和软件的输出。

也可以在终端中手动运行脚本，路径包含空格时保留引号：

```bash
/bin/bash "/实际位置/Template_2/start_xunisim.sh" "/home/gaojunqi/qljqj-app/bin/XUnisim-Application"
```

如安装位置发生变化，修改 `Xunisim.py` 顶部的 `XUNISIM_PROGRAM` 即可。如软件要求额外的环境变量或环境初始化脚本，将对应命令加入 `start_xunisim.sh` 中执行软件之前的位置。当前没有添加未经确认的环境配置。

启动脚本独立运行，界面无需等待软件退出。此入口负责打开软件，不自动导入当前模型或建立联合仿真连接。

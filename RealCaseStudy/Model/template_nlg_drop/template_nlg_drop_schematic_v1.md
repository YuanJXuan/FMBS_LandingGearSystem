# 前起落震结构点位示意图（初稿）

图片：`template_nlg_drop_schematic_v1.png`（1448 × 1086 PNG）。

采用侧向结构图和横向点位图，编号依据当前信息配置表。图像由内置 image_gen 生成，为结构关系示意图，不是精确尺寸图或 CAD 渲染。

已接入“结构参数”页的左侧示意图栏，右侧两个参数板块仍横向排列。配套 `.points.json` 记录图片点位、编号位置和 Marker 路径，点选按路径匹配当前模型，不依赖配置表行顺序。图片位置与模型 XYZ 坐标独立。

使用方式：

- 打开前起落震界面并导入对应模型，点击图上的点或编号即可选择 Marker。
- 下拉框与示意图双向同步；放大窗口也可点选。
- 顶部“隐藏示意图 / 显示示意图”切换侧栏，分隔条可调整宽度。
- 图中灰点表示未匹配到模型，或当前调整方式锁定了其他主控 Marker；悬停可查看原因。
- 点击只改变当前选择，仍需点击“应用结构参数”才会写入模型。
- 切换到没有配套示意图的模型目录时，侧栏隐藏并关闭放大窗口。

| 编号 | 名称 | Marker（模型内路径） | 视图 |
|---|---|---|---|
| 01 | 右轮心 | `lunzhou.MARKER_K2` | 横向 |
| 02 | 左轮心 | `lunzhou.MARKER_K1` | 横向 |
| 03 | 撑杆活塞杆下端点 | `chengganhuosaigan.MARKER_4cg` | 侧向 |
| 04 | 撑杆外筒上端点 | `chengganwaitong.MARKER_5cg` | 侧向 |
| 05 | 收放活塞杆下端点 | `shoufanghuosaigan.MARKER_6g` | 侧向 |
| 06 | 收放外筒上端点 | `shoufangwaitong.MARKER_8a` | 侧向 |
| 07 | 活塞杆下端点 | `huosaigan.MARKER_M` | 侧向 |
| 08 | 外筒上端点 | `waitong.MARKER_OL` | 侧向 |
| 09 | 转轴左端点 | `zhuanzhou.MARKER_B` | 横向 |
| 10 | 转轴右端点 | `zhuanzhou.MARKER_A` | 横向 |
| 11 | 上扭力臂端点 | `shangniulibi.MARKER_70` | 侧向 |
| 12 | 上下扭力臂连接点 | `shangniulibi.MARKER_74` | 侧向 |
| 13 | 下扭力臂端点 | `xianiulibi.MARKER_77` | 侧向 |
| 14 | 前起质量点 | `qianqizhiliang.MARKER_85` | 侧向 |

重新绘图后必须复核热点位置。背景图暂含固定编号，程序可在对应点位叠加选中光圈；后续如需动态编号，可单独制作不带编号的底图。

完整生成提示词见同目录 `template_nlg_drop_schematic_v1.prompt.txt`。

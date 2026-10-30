# 前起收放结构点位示意图

图片：`template_nlg_retract_schematic_v1.png`（1448 × 1086 PNG）。

已接入结构参数页，支持点或编号点选、下拉框反向高亮、隐藏侧栏及放大查看。点击只选择 Marker，仍需点击“应用结构参数”提交修改。

根据当前信息配置表，14 个初始点位的相对路径和坐标与前起落震一致。此图表示初始放下姿态，是结构示意图，不随仿真运动变化。此案例使用独立的收放模型完整路径和点位文件。

| 编号 | 名称 | Marker（模型内路径） |
|---|---|---|
| 01 | 右轮心 | `lunzhou.MARKER_K2` |
| 02 | 左轮心 | `lunzhou.MARKER_K1` |
| 03 | 撑杆活塞杆下端点 | `chengganhuosaigan.MARKER_4cg` |
| 04 | 撑杆外筒上端点 | `chengganwaitong.MARKER_5cg` |
| 05 | 收放活塞杆下端点 | `shoufanghuosaigan.MARKER_6g` |
| 06 | 收放外筒上端点 | `shoufangwaitong.MARKER_8a` |
| 07 | 活塞杆下端点 | `huosaigan.MARKER_M` |
| 08 | 外筒上端点 | `waitong.MARKER_OL` |
| 09 | 转轴左端点 | `zhuanzhou.MARKER_B` |
| 10 | 转轴右端点 | `zhuanzhou.MARKER_A` |
| 11 | 上扭力臂端点 | `shangniulibi.MARKER_70` |
| 12 | 上下扭力臂连接点 | `shangniulibi.MARKER_74` |
| 13 | 下扭力臂端点 | `xianiulibi.MARKER_77` |
| 14 | 前起质量点 | `qianqizhiliang.MARKER_85` |

图片由内置 image_gen 以落震图为参考编辑，修改标题及模型名；生成后已复核全部 14 个蓝色点的位置。完整提示词见 `template_nlg_retract_schematic_v1.prompt.txt`。

替换图片后需要重新核对热点坐标。

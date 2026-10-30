import Jusme
from Jusme import Base
from Fmbs.import_all_node import MakeSceneNodeByType
import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils
UNITS_1 = MakeSceneNodeByType('DefaultsUnits', '.GCMB.UNITS_1')
UNITS_1.length_opt = 0
UNITS_1.length = 'mm'
UNITS_1.angle = 'deg'
UNITS_1.force = 'newton'
UNITS_1.mass = 'kg'
UNITS_1.time = 'sec'
UNITS_1.coordinate_system_type = 'cartesian'
UNITS_1.orientation_type = 'body313'
LMLG_S = MakeSceneNodeByType('DataElementVariable', '.GCMB.LMLG_S')
LMLG_S.variable_name = '.GCMB.LMLG_S'
LMLG_S.adams_id = 30
LMLG_S.initial_condition = 0.0
LMLG_S.function = '""'
LMLG_V = MakeSceneNodeByType('DataElementVariable', '.GCMB.LMLG_V')
LMLG_V.variable_name = '.GCMB.LMLG_V'
LMLG_V.adams_id = 31
LMLG_V.initial_condition = 0.0
LMLG_V.function = '""'
steel = MakeSceneNodeByType('MaterialCreate', '.GCMB.steel')
steel.material_name = '.GCMB.steel'
steel.adams_id = 3
steel.density = 7.801e-06
steel.youngs_modulus = 207000.0
steel.poissons_ratio = 0.29
aluminum = MakeSceneNodeByType('MaterialCreate', '.GCMB.aluminum')
aluminum.material_name = '.GCMB.aluminum'
aluminum.adams_id = 2
aluminum.density = 2.74e-06
aluminum.youngs_modulus = 71705.0
aluminum.poissons_ratio = 0.33
ground = Jusme.ActiveUSScene.getObject('.GCMB.ground')
ground.part_name = 'ground'
origo = MakeSceneNodeByType('Marker', '.GCMB.ground.origo')
origo.marker_name = '.GCMB.ground.origo'
origo.adams_id = 1
origo.location = Base.Vector (0.0, 0.0, 0.0)
origo.orientation = Base.Vector (0.0, 0.0, 0.0)
lumian_1_ref_1 = MakeSceneNodeByType('Marker', '.GCMB.ground.lumian_1_ref_1')
lumian_1_ref_1.marker_name = '.GCMB.ground.lumian_1_ref_1'
lumian_1_ref_1.adams_id = 186
lumian_1_ref_1.location = Base.Vector (12270.973957, 1811.5919597, -282.740481)
lumian_1_ref_1.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_spin_axis = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_spin_axis')
cfl_spin_axis.marker_name = '.GCMB.ground.cfl_spin_axis'
cfl_spin_axis.adams_id = 4
cfl_spin_axis.location = Base.Vector (12270.973957, -1811.59195974, 174.2595194)
cfl_spin_axis.orientation = Base.Vector (179.9999064822, 88.9999687771, 0.0053582784306)
cfl_uc_top = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_uc_top')
cfl_uc_top.marker_name = '.GCMB.ground.cfl_uc_top'
cfl_uc_top.adams_id = 17
cfl_uc_top.location = Base.Vector (12137.340597, -1439.0607744, 2153.4060818)
cfl_uc_top.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_collar_top = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_collar_top')
cfl_collar_top.marker_name = '.GCMB.ground.cfl_collar_top'
cfl_collar_top.adams_id = 25
cfl_collar_top.location = Base.Vector (12216.184789, -1494.0334506368, 988.583100554)
cfl_collar_top.orientation = Base.Vector (55.1145661544, 175.2828647294, 235.2057167569)
cfl_collar_bot = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_collar_bot')
cfl_collar_bot.marker_name = '.GCMB.ground.cfl_collar_bot'
cfl_collar_bot.adams_id = 27
cfl_collar_bot.location = Base.Vector (12230.884553, -1504.282593664, 771.41271422)
cfl_collar_bot.orientation = Base.Vector (55.1145661544, 175.2828647294, 235.2057167569)
cfl_plane_ref = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_plane_ref')
cfl_plane_ref.marker_name = '.GCMB.ground.cfl_plane_ref'
cfl_plane_ref.adams_id = 29
cfl_plane_ref.location = Base.Vector (11790.454913, -1331.23818588, 1478.5418121942)
cfl_plane_ref.orientation = Base.Vector (70.4651741872, 87.6875364203, 268.7516172662)
cfl_plane_ref_2 = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_plane_ref_2')
cfl_plane_ref_2.marker_name = '.GCMB.ground.cfl_plane_ref_2'
cfl_plane_ref_2.adams_id = 31
cfl_plane_ref_2.location = Base.Vector (11790.454913, -1331.23818588, 1478.5418121942)
cfl_plane_ref_2.orientation = Base.Vector (160.4147950495, 91.2473659421, 267.6869880055)
cfl_spin_axis_1 = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_spin_axis_1')
cfl_spin_axis_1.marker_name = '.GCMB.ground.cfl_spin_axis_1'
cfl_spin_axis_1.adams_id = 37
cfl_spin_axis_1.location = Base.Vector (12270.973957, -1811.59195974, 174.2595194)
cfl_spin_axis_1.orientation = Base.Vector (359.9999064822, 91.0000312229, 179.9946417216)
cfl_ldb_geompt_1 = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_ldb_geompt_1')
cfl_ldb_geompt_1.marker_name = '.GCMB.ground.cfl_ldb_geompt_1'
cfl_ldb_geompt_1.adams_id = 39
cfl_ldb_geompt_1.location = Base.Vector (11891.208125, -1378.1308466589, 1145.8304613444)
cfl_ldb_geompt_1.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_ldb_geompt_2 = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_ldb_geompt_2')
cfl_ldb_geompt_2.marker_name = '.GCMB.ground.cfl_ldb_geompt_2'
cfl_ldb_geompt_2.adams_id = 41
cfl_ldb_geompt_2.location = Base.Vector (11960.664303, -1405.0660792298, 1073.7874160988)
cfl_ldb_geompt_2.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_211 = MakeSceneNodeByType('Marker', '.GCMB.ground.MARKER_211')
MARKER_211.marker_name = '.GCMB.ground.MARKER_211'
MARKER_211.adams_id = 211
MARKER_211.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_211.orientation = Base.Vector (180.0, 90.0, 180.0)
MARKER_215 = MakeSceneNodeByType('Marker', '.GCMB.ground.MARKER_215')
MARKER_215.marker_name = '.GCMB.ground.MARKER_215'
MARKER_215.adams_id = 215
MARKER_215.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_215.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_226 = MakeSceneNodeByType('Marker', '.GCMB.ground.MARKER_226')
MARKER_226.marker_name = '.GCMB.ground.MARKER_226'
MARKER_226.adams_id = 226
MARKER_226.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_226.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_240 = MakeSceneNodeByType('Marker', '.GCMB.ground.MARKER_240')
MARKER_240.marker_name = '.GCMB.ground.MARKER_240'
MARKER_240.adams_id = 240
MARKER_240.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_240.orientation = Base.Vector (90.0, 90.0, 270.0)
luntai_tire_jf_1 = MakeSceneNodeByType('Marker', '.GCMB.ground.luntai_tire_jf_1')
luntai_tire_jf_1.is_floating = True
luntai_tire_jf_1.floating_marker_name = '.GCMB.ground.luntai_tire_jf_1'
luntai_tire_jf_1.adams_id = 187
hpl_udb_spndl_atch_1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_udb_spndl_atch_1')
hpl_udb_spndl_atch_1.point_name = '.GCMB.ground.hpl_udb_spndl_atch_1'
hpl_udb_spndl_atch_1.location = Base.Vector (10963.049321, -1022.41898132, 2103.08951238)
POINT_48 = MakeSceneNodeByType('Point', '.GCMB.ground.POINT_48')
POINT_48.point_name = '.GCMB.ground.POINT_48'
POINT_48.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
hpl_lc_top = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_lc_top')
hpl_lc_top.point_name = '.GCMB.ground.hpl_lc_top'
hpl_lc_top.location = Base.Vector (12205.761134, -1486.7657470108, 1142.5793907842)
hpl_wheel_center = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_wheel_center')
hpl_wheel_center.point_name = '.GCMB.ground.hpl_wheel_center'
hpl_wheel_center.location = Base.Vector (12270.973957, -1811.59195974, 174.2595194)
hpl_uc_bot = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_uc_bot')
hpl_uc_bot.point_name = '.GCMB.ground.hpl_uc_bot'
hpl_uc_bot.location = Base.Vector (12234.684072, -1506.9317387834, 715.279643629)
hpl_lc_bot = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_lc_bot')
hpl_lc_bot.point_name = '.GCMB.ground.hpl_lc_bot'
hpl_lc_bot.location = Base.Vector (12270.97482, -1532.23480192, 179.1298424)
hpl_ob_axle = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_ob_axle')
hpl_ob_axle.point_name = '.GCMB.ground.hpl_ob_axle'
hpl_ob_axle.location = Base.Vector (12270.973718, -1957.87367632, 171.7060828)
hpl_ib_axle = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_ib_axle')
hpl_ib_axle.point_name = '.GCMB.ground.hpl_ib_axle'
hpl_ib_axle.location = Base.Vector (12270.97482, -1532.234807, 179.1298424)
hpl_uc_top = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_uc_top')
hpl_uc_top.point_name = '.GCMB.ground.hpl_uc_top'
hpl_uc_top.location = Base.Vector (12137.340597, -1439.0607744, 2153.4060818)
hpl_ldb_udb_atch_1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_ldb_udb_atch_1')
hpl_ldb_udb_atch_1.point_name = '.GCMB.ground.hpl_ldb_udb_atch_1'
hpl_ldb_udb_atch_1.location = Base.Vector (11532.351205, -1238.965478376, 1518.05286178)
hpl_lta_connect_atch_1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_lta_connect_atch_1')
hpl_lta_connect_atch_1.point_name = '.GCMB.ground.hpl_lta_connect_atch_1'
hpl_lta_connect_atch_1.location = Base.Vector (12048.547912, -1562.2090168, 532.1183668)
hpl_uta_connect_atch_1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_uta_connect_atch_1')
hpl_uta_connect_atch_1.point_name = '.GCMB.ground.hpl_uta_connect_atch_1'
hpl_uta_connect_atch_1.location = Base.Vector (12052.25235, -1491.2788564, 529.0216242)
hpl_uta_connect_atch_2 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_uta_connect_atch_2')
hpl_uta_connect_atch_2.point_name = '.GCMB.ground.hpl_uta_connect_atch_2'
hpl_uta_connect_atch_2.location = Base.Vector (12087.047708, -1493.4025504, 522.0012166)
hpl_lta_lc_atch_1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_lta_lc_atch_1')
hpl_lta_lc_atch_1.point_name = '.GCMB.ground.hpl_lta_lc_atch_1'
hpl_lta_lc_atch_1.location = Base.Vector (12150.137371, -1553.6660062, 274.0663556)
hpl_uta_collar_atch_1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_uta_collar_atch_1')
hpl_uta_collar_atch_1.point_name = '.GCMB.ground.hpl_uta_collar_atch_1'
hpl_uta_collar_atch_1.location = Base.Vector (12106.652469, -1496.5360468, 800.236779)
hpl_connect_1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_connect_1')
hpl_connect_1.point_name = '.GCMB.ground.hpl_connect_1'
hpl_connect_1.location = Base.Vector (12045.992164, -1611.1431582, 534.2547862)
hpl_ldb_collar_atch_1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_ldb_collar_atch_1')
hpl_ldb_collar_atch_1.point_name = '.GCMB.ground.hpl_ldb_collar_atch_1'
hpl_ldb_collar_atch_1.location = Base.Vector (12111.152689, -1463.4257498, 917.6941514)
hpl_uplock_tab = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_uplock_tab')
hpl_uplock_tab.point_name = '.GCMB.ground.hpl_uplock_tab'
hpl_uplock_tab.location = Base.Vector (11901.482877, -1275.11231642, 1033.20487288)
zhiliang = MakeSceneNodeByType('PartGeneral', '.GCMB.zhiliang')
zhiliang.part_name = '.GCMB.zhiliang'
zhiliang.adams_id = 23
zhiliang.location = Base.Vector (0.0, 0.0, 0.0)
zhiliang.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_199 = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.MARKER_199')
MARKER_199.marker_name = '.GCMB.zhiliang.MARKER_199'
MARKER_199.adams_id = 199
MARKER_199.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_199.orientation = Base.Vector (0.0, 0.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.cm')
cm.marker_name = '.GCMB.zhiliang.cm'
cm.adams_id = 204
cm.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
cm.orientation = Base.Vector (0.0, 90.0, 0.0)
MARKER_207 = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.MARKER_207')
MARKER_207.marker_name = '.GCMB.zhiliang.MARKER_207'
MARKER_207.adams_id = 207
MARKER_207.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_207.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_210 = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.MARKER_210')
MARKER_210.marker_name = '.GCMB.zhiliang.MARKER_210'
MARKER_210.adams_id = 210
MARKER_210.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_210.orientation = Base.Vector (180.0, 90.0, 180.0)
MARKER_212 = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.MARKER_212')
MARKER_212.marker_name = '.GCMB.zhiliang.MARKER_212'
MARKER_212.adams_id = 212
MARKER_212.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_212.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_214 = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.MARKER_214')
MARKER_214.marker_name = '.GCMB.zhiliang.MARKER_214'
MARKER_214.adams_id = 214
MARKER_214.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_214.orientation = Base.Vector (90.0, 90.0, 270.0)
MARKER_228 = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.MARKER_228')
MARKER_228.marker_name = '.GCMB.zhiliang.MARKER_228'
MARKER_228.adams_id = 228
MARKER_228.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_228.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_229 = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.MARKER_229')
MARKER_229.marker_name = '.GCMB.zhiliang.MARKER_229'
MARKER_229.adams_id = 229
MARKER_229.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_229.orientation = Base.Vector (90.0, 90.0, 270.0)
MARKER_233 = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.MARKER_233')
MARKER_233.marker_name = '.GCMB.zhiliang.MARKER_233'
MARKER_233.adams_id = 233
MARKER_233.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_233.orientation = Base.Vector (180.0, 90.0, 180.0)
MARKER_239 = MakeSceneNodeByType('Marker', '.GCMB.zhiliang.MARKER_239')
MARKER_239.marker_name = '.GCMB.zhiliang.MARKER_239'
MARKER_239.adams_id = 239
MARKER_239.location = Base.Vector (12137.340597, -1439.0607744, 2253.4060818)
MARKER_239.orientation = Base.Vector (90.0, 90.0, 270.0)
zhiliang = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.cm')
zhiliang.center_of_mass_marker = center_of_mass_marker
zhiliang.part_name = '.GCMB.zhiliang'
zhiliang.mass = 12000.0
zhiliang.ixx = 4084.5940484395
zhiliang.iyy = 4084.594048436
zhiliang.izz = 4084.5940483223
zhiliang.ixy = 0.0
zhiliang.izx = 0.0
zhiliang.iyz = 0.0
ELLIPSOID_49 = MakeSceneNodeByType('ShapeEllipsoid', '.GCMB.zhiliang.ELLIPSOID_49')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_199')
ELLIPSOID_49.center_marker = center_marker
ELLIPSOID_49.ellipsoid_name = '.GCMB.zhiliang.ELLIPSOID_49'
ELLIPSOID_49.adams_id = 26
ELLIPSOID_49.x_scale_factor = 100.0
ELLIPSOID_49.y_scale_factor = 100.0
ELLIPSOID_49.z_scale_factor = 100.0


gel_upper_cylinder = MakeSceneNodeByType('PartGeneral', '.GCMB.gel_upper_cylinder')
gel_upper_cylinder.part_name = '.GCMB.gel_upper_cylinder'
gel_upper_cylinder.adams_id = 4
gel_upper_cylinder.location = Base.Vector (12186.012335, -1472.9962565924, 1434.3428627157)
gel_upper_cylinder.orientation = Base.Vector (55.1145661544, 175.2828647294, 235.2057167569)
MARKER_216 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.MARKER_216')
MARKER_216.marker_name = '.GCMB.gel_upper_cylinder.MARKER_216'
MARKER_216.adams_id = 216
MARKER_216.location = Base.Vector (6.3643534887e-10, 8.8382773322e-10, -721.507081063)
MARKER_216.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
MARKER_218 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.MARKER_218')
MARKER_218.marker_name = '.GCMB.gel_upper_cylinder.MARKER_218'
MARKER_218.adams_id = 218
MARKER_218.location = Base.Vector (6.3643534887e-10, 8.8382773322e-10, -721.507081063)
MARKER_218.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
MARKER_220 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.MARKER_220')
MARKER_220.marker_name = '.GCMB.gel_upper_cylinder.MARKER_220'
MARKER_220.adams_id = 220
MARKER_220.location = Base.Vector (6.3643534887e-10, 8.8382773322e-10, -721.507081063)
MARKER_220.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
MARKER_222 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.MARKER_222')
MARKER_222.marker_name = '.GCMB.gel_upper_cylinder.MARKER_222'
MARKER_222.adams_id = 222
MARKER_222.location = Base.Vector (6.4170973204e-10, 8.8445958447e-10, -721.507081063)
MARKER_222.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
cm = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.cm')
cm.marker_name = '.GCMB.gel_upper_cylinder.cm'
cm.adams_id = 71
cm.location = Base.Vector (-0.207563017, 6.4023904007, -14.6682621265)
cm.orientation = Base.Vector (1.8568667884, 1.160957641, 3.8718469355e-06)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.inertia_frame')
inertia_frame.marker_name = '.GCMB.gel_upper_cylinder.inertia_frame'
inertia_frame.adams_id = 72
inertia_frame.location = Base.Vector (-0.207563017, 6.4023904007, -14.6682621265)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_12 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.gralin_12')
gralin_12.marker_name = '.GCMB.gel_upper_cylinder.gralin_12'
gralin_12.adams_id = 73
gralin_12.location = Base.Vector (6.3823252239e-10, 8.838485499e-10, -721.507081063)
gralin_12.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_12 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.jxl_joint_j_12')
jxl_joint_j_12.marker_name = '.GCMB.gel_upper_cylinder.jxl_joint_j_12'
jxl_joint_j_12.adams_id = 76
jxl_joint_j_12.location = Base.Vector (0.0, 0.0, 507.1310810647)
jxl_joint_j_12.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_234 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.MARKER_234')
MARKER_234.marker_name = '.GCMB.gel_upper_cylinder.MARKER_234'
MARKER_234.adams_id = 234
MARKER_234.location = Base.Vector (-6.7533173809, -4.6926786112, -821.1683647783)
MARKER_234.orientation = Base.Vector (180.0, 92.6958536659, 3.872313078)
uel_spring_j_1 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.uel_spring_j_1')
uel_spring_j_1.marker_name = '.GCMB.gel_upper_cylinder.uel_spring_j_1'
uel_spring_j_1.adams_id = 78
uel_spring_j_1.location = Base.Vector (6.3823252239e-10, 8.838485499e-10, -721.507081063)
uel_spring_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_4 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_cylinder.jxl_joint_j_4')
jxl_joint_j_4.marker_name = '.GCMB.gel_upper_cylinder.jxl_joint_j_4'
jxl_joint_j_4.adams_id = 81
jxl_joint_j_4.location = Base.Vector (0.0, 0.0, 556.2289935088)
jxl_joint_j_4.orientation = Base.Vector (0.0, 0.0, 0.0)
gel_upper_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.cm')
gel_upper_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.inertia_frame')
gel_upper_cylinder.inertia_marker = inertia_marker
gel_upper_cylinder.part_name = '.GCMB.gel_upper_cylinder'
gel_upper_cylinder.mass = 112.770857716
gel_upper_cylinder.ixx = 20382860.753
gel_upper_cylinder.iyy = 20191575.617
gel_upper_cylinder.izz = 677030.88217
gel_upper_cylinder.ixy = 0.0
gel_upper_cylinder.izx = 0.0
gel_upper_cylinder.iyz = 0.0
gralin_upper_cylinder = MakeSceneNodeByType('ShapeCylinder', '.GCMB.gel_upper_cylinder.gralin_upper_cylinder')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.gralin_12')
gralin_upper_cylinder.center_marker = center_marker
gralin_upper_cylinder.cylinder_name = '.GCMB.gel_upper_cylinder.gralin_upper_cylinder'
gralin_upper_cylinder.adams_id = 1
gralin_upper_cylinder.angle_extent = 360.0
gralin_upper_cylinder.length = 1443.0141621266
gralin_upper_cylinder.radius = 93.98
gralin_upper_cylinder.side_count_for_body = 15
gralin_upper_cylinder.segment_count_for_ends = 15


gel_lower_cylinder = MakeSceneNodeByType('PartGeneral', '.GCMB.gel_lower_cylinder')
gel_lower_cylinder.part_name = '.GCMB.gel_lower_cylinder'
gel_lower_cylinder.adams_id = 6
gel_lower_cylinder.location = Base.Vector (12238.367977, -1509.5002744656, 660.8546165914)
gel_lower_cylinder.orientation = Base.Vector (55.1145661544, 175.2828647294, 235.2057167569)
MARKER_203 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.MARKER_203')
MARKER_203.marker_name = '.GCMB.gel_lower_cylinder.MARKER_203'
MARKER_203.adams_id = 203
MARKER_203.location = Base.Vector (0.3297699984, -278.8194421688, 501.3550984684)
MARKER_203.orientation = Base.Vector (0.067765920864, 86.3064065811, 176.1239093976)
MARKER_217 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.MARKER_217')
MARKER_217.marker_name = '.GCMB.gel_lower_cylinder.MARKER_217'
MARKER_217.adams_id = 217
MARKER_217.location = Base.Vector (-2.9251268745e-07, 1.1790534982e-09, -483.3619999809)
MARKER_217.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
MARKER_219 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.MARKER_219')
MARKER_219.marker_name = '.GCMB.gel_lower_cylinder.MARKER_219'
MARKER_219.adams_id = 219
MARKER_219.location = Base.Vector (-2.9251268745e-07, 1.1790534982e-09, -483.3619999809)
MARKER_219.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
MARKER_221 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.MARKER_221')
MARKER_221.marker_name = '.GCMB.gel_lower_cylinder.MARKER_221'
MARKER_221.adams_id = 221
MARKER_221.location = Base.Vector (-2.9251268745e-07, 1.1790534982e-09, -483.3619999809)
MARKER_221.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
MARKER_223 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.MARKER_223')
MARKER_223.marker_name = '.GCMB.gel_lower_cylinder.MARKER_223'
MARKER_223.adams_id = 223
MARKER_223.location = Base.Vector (-2.925109068e-07, 1.1796038176e-09, -483.3619999809)
MARKER_223.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
cm = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.cm')
cm.marker_name = '.GCMB.gel_lower_cylinder.cm'
cm.adams_id = 99
cm.location = Base.Vector (0.016535536877, -13.9807327446, 32.7170406567)
cm.orientation = Base.Vector (0.067765835809, 4.4745452767, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.inertia_frame')
inertia_frame.marker_name = '.GCMB.gel_lower_cylinder.inertia_frame'
inertia_frame.adams_id = 100
inertia_frame.location = Base.Vector (0.01653553688, -13.9807327446, 32.7170406567)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_14 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.gralin_14')
gralin_14.marker_name = '.GCMB.gel_lower_cylinder.gralin_14'
gralin_14.adams_id = 101
gralin_14.location = Base.Vector (-2.9251091826e-07, 1.1789319521e-09, -483.3619999809)
gralin_14.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_22 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.gralin_22')
gralin_22.marker_name = '.GCMB.gel_lower_cylinder.gralin_22'
gralin_22.adams_id = 102
gralin_22.location = Base.Vector (1.2485845691e-10, -5.0742924723e-06, 483.3620002382)
gralin_22.orientation = Base.Vector (0.067765837027, 86.3072194251, 358.9479605068)
jxl_joint_j_11 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.jxl_joint_j_11')
jxl_joint_j_11.marker_name = '.GCMB.gel_lower_cylinder.jxl_joint_j_11'
jxl_joint_j_11.adams_id = 103
jxl_joint_j_11.location = Base.Vector (114.1502170489, -26.2463754244, 381.6035459414)
jxl_joint_j_11.orientation = Base.Vector (182.811221391, 89.9999933852, 90.0001347091)
jxl_joint_i_12 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.jxl_joint_i_12')
jxl_joint_i_12.marker_name = '.GCMB.gel_lower_cylinder.jxl_joint_i_12'
jxl_joint_i_12.adams_id = 104
jxl_joint_i_12.location = Base.Vector (0.0, -3.9134147312e-10, -268.9860000012)
jxl_joint_i_12.orientation = Base.Vector (0.0, 0.0, 0.0)
coomarker_1 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.coomarker_1')
coomarker_1.marker_name = '.GCMB.gel_lower_cylinder.coomarker_1'
coomarker_1.adams_id = 105
coomarker_1.location = Base.Vector (0.3297699984, -278.8194421688, 501.3550984684)
coomarker_1.orientation = Base.Vector (180.0677659208, 93.6935934189, 183.8814472486)
uel_spring_i_1 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.uel_spring_i_1')
uel_spring_i_1.marker_name = '.GCMB.gel_lower_cylinder.uel_spring_i_1'
uel_spring_i_1.adams_id = 106
uel_spring_i_1.location = Base.Vector (-2.9251091826e-07, 1.1789319521e-09, -483.3619999809)
uel_spring_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_damper_i_1 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.uel_damper_i_1')
uel_damper_i_1.marker_name = '.GCMB.gel_lower_cylinder.uel_damper_i_1'
uel_damper_i_1.adams_id = 107
uel_damper_i_1.location = Base.Vector (-2.9251091826e-07, 1.1789319521e-09, -483.3619999809)
uel_damper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_stopper_i_1 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_cylinder.uel_stopper_i_1')
uel_stopper_i_1.marker_name = '.GCMB.gel_lower_cylinder.uel_stopper_i_1'
uel_stopper_i_1.adams_id = 108
uel_stopper_i_1.location = Base.Vector (-2.9251091826e-07, 1.1789319521e-09, -483.3619999809)
uel_stopper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
gel_lower_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.cm')
gel_lower_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.inertia_frame')
gel_lower_cylinder.inertia_marker = inertia_marker
gel_lower_cylinder.part_name = '.GCMB.gel_lower_cylinder'
gel_lower_cylinder.mass = 217.3555691677
gel_lower_cylinder.ixx = 3328449.4628
gel_lower_cylinder.iyy = 3193629.4
gel_lower_cylinder.izz = 203233.07411
gel_lower_cylinder.ixy = 0.0
gel_lower_cylinder.izx = 0.0
gel_lower_cylinder.iyz = 0.0
gralin_lower_cylinder = MakeSceneNodeByType('ShapeCylinder', '.GCMB.gel_lower_cylinder.gralin_lower_cylinder')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.gralin_14')
gralin_lower_cylinder.center_marker = center_marker
gralin_lower_cylinder.cylinder_name = '.GCMB.gel_lower_cylinder.gralin_lower_cylinder'
gralin_lower_cylinder.adams_id = 7
gralin_lower_cylinder.angle_extent = 360.0
gralin_lower_cylinder.length = 966.7239999802
gralin_lower_cylinder.radius = 63.5
gralin_lower_cylinder.side_count_for_body = 15
gralin_lower_cylinder.segment_count_for_ends = 15


gralin_geom = MakeSceneNodeByType('ShapeCylinder', '.GCMB.gel_lower_cylinder.gralin_geom')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.gralin_22')
gralin_geom.center_marker = center_marker
gralin_geom.cylinder_name = '.GCMB.gel_lower_cylinder.gralin_geom'
gralin_geom.adams_id = 8
gralin_geom.angle_extent = 360.0
gralin_geom.length = 425.7036049693
gralin_geom.radius = 25.4
gralin_geom.side_count_for_body = 15
gralin_geom.segment_count_for_ends = 15


gel_upper_dragbrace = MakeSceneNodeByType('PartGeneral', '.GCMB.gel_upper_dragbrace')
gel_upper_dragbrace.part_name = '.GCMB.gel_upper_dragbrace'
gel_upper_dragbrace.adams_id = 8
gel_upper_dragbrace.location = Base.Vector (11247.700263, -1130.692229848, 1810.57118708)
gel_upper_dragbrace.orientation = Base.Vector (69.1745865818, 133.845797857, 255.2385761183)
MARKER_208 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_dragbrace.MARKER_208')
MARKER_208.marker_name = '.GCMB.gel_upper_dragbrace.MARKER_208'
MARKER_208.adams_id = 208
MARKER_208.location = Base.Vector (-946.420910472, -220.3516670374, 372.0032663641)
MARKER_208.orientation = Base.Vector (284.7614238817, 133.845797857, 110.8254134182)
cm = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_dragbrace.cm')
cm.marker_name = '.GCMB.gel_upper_dragbrace.cm'
cm.adams_id = 119
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_dragbrace.inertia_frame')
inertia_frame.marker_name = '.GCMB.gel_upper_dragbrace.inertia_frame'
inertia_frame.adams_id = 120
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_24 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_dragbrace.gralin_24')
gralin_24.marker_name = '.GCMB.gel_upper_dragbrace.gralin_24'
gralin_24.adams_id = 121
gralin_24.location = Base.Vector (-2.2706836411e-10, -2.2812307598e-10, -422.2750593684)
gralin_24.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_14 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_dragbrace.jxl_joint_j_14')
jxl_joint_j_14.marker_name = '.GCMB.gel_upper_dragbrace.jxl_joint_j_14'
jxl_joint_j_14.adams_id = 122
jxl_joint_j_14.location = Base.Vector (2.2595814109e-10, 2.2848389847e-10, 422.2750593684)
jxl_joint_j_14.orientation = Base.Vector (193.0027634258, 90.0301580129, 133.8272261428)
uel_actuator_i_3 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_dragbrace.uel_actuator_i_3')
uel_actuator_i_3.marker_name = '.GCMB.gel_upper_dragbrace.uel_actuator_i_3'
uel_actuator_i_3.adams_id = 124
uel_actuator_i_3.location = Base.Vector (2.2595814109e-10, 2.2848389847e-10, 422.2750593684)
uel_actuator_i_3.orientation = Base.Vector (0.0, 0.0, 0.0)
gel_upper_dragbrace = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.cm')
gel_upper_dragbrace.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.inertia_frame')
gel_upper_dragbrace.inertia_marker = inertia_marker
gel_upper_dragbrace.part_name = '.GCMB.gel_upper_dragbrace'
gel_upper_dragbrace.mass = 6.7539180723
gel_upper_dragbrace.ixx = 403013.04206
gel_upper_dragbrace.iyy = 403013.04206
gel_upper_dragbrace.izz = 3137.2976041438
gel_upper_dragbrace.ixy = 0.0
gel_upper_dragbrace.izx = 0.0
gel_upper_dragbrace.iyz = 0.0
gralin_upper_dragbrace = MakeSceneNodeByType('ShapeCylinder', '.GCMB.gel_upper_dragbrace.gralin_upper_dragbrace')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.gralin_24')
gralin_upper_dragbrace.center_marker = center_marker
gralin_upper_dragbrace.cylinder_name = '.GCMB.gel_upper_dragbrace.gralin_upper_dragbrace'
gralin_upper_dragbrace.adams_id = 11
gralin_upper_dragbrace.angle_extent = 360.0
gralin_upper_dragbrace.length = 844.5501187369
gralin_upper_dragbrace.radius = 30.48
gralin_upper_dragbrace.side_count_for_body = 15
gralin_upper_dragbrace.segment_count_for_ends = 15


gel_lower_dragbrace = MakeSceneNodeByType('PartGeneral', '.GCMB.gel_lower_dragbrace')
gel_lower_dragbrace.part_name = '.GCMB.gel_lower_dragbrace'
gel_lower_dragbrace.adams_id = 10
gel_lower_dragbrace.location = Base.Vector (11821.751947, -1351.195614088, 1217.87350659)
gel_lower_dragbrace.orientation = Base.Vector (68.8036164538, 134.040966185, 254.9123665662)
cm = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_dragbrace.cm')
cm.marker_name = '.GCMB.gel_lower_dragbrace.cm'
cm.adams_id = 131
cm.location = Base.Vector (3.9348735476, 6.8056064573, 24.9786134158)
cm.orientation = Base.Vector (149.9643072355, 1.0992652329, 180.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_dragbrace.inertia_frame')
inertia_frame.marker_name = '.GCMB.gel_lower_dragbrace.inertia_frame'
inertia_frame.adams_id = 132
inertia_frame.location = Base.Vector (3.9348735476, 6.8056064573, 24.9786134158)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_26 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_dragbrace.gralin_26')
gralin_26.marker_name = '.GCMB.gel_lower_dragbrace.gralin_26'
gralin_26.adams_id = 133
gralin_26.location = Base.Vector (1.1418643808e-10, 1.377231662e-10, -431.8055559096)
gralin_26.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_i_14 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_dragbrace.jxl_joint_i_14')
jxl_joint_i_14.marker_name = '.GCMB.gel_lower_dragbrace.jxl_joint_i_14'
jxl_joint_i_14.adams_id = 134
jxl_joint_i_14.location = Base.Vector (1.1352030427e-10, 1.3820888878e-10, -431.8055559096)
jxl_joint_i_14.orientation = Base.Vector (193.0709676552, 90.2906925253, 133.6233654172)
jxl_joint_i_10 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_dragbrace.jxl_joint_i_10')
jxl_joint_i_10.marker_name = '.GCMB.gel_lower_dragbrace.jxl_joint_i_10'
jxl_joint_i_10.adams_id = 135
jxl_joint_i_10.location = Base.Vector (-1.1032841307e-10, -1.3825746104e-10, 431.8055559096)
jxl_joint_i_10.orientation = Base.Vector (193.0709676552, 90.2906925253, 133.6233654172)
graarm_1 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_dragbrace.graarm_1')
graarm_1.marker_name = '.GCMB.gel_lower_dragbrace.graarm_1'
graarm_1.adams_id = 136
graarm_1.location = Base.Vector (70.772384942, 122.4052041467, 162.0383572441)
graarm_1.orientation = Base.Vector (239.9643072355, 90.0, 337.5559025594)
graarm_2 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_dragbrace.graarm_2')
graarm_2.marker_name = '.GCMB.gel_lower_dragbrace.graarm_2'
graarm_2.adams_id = 137
graarm_2.location = Base.Vector (-2.5562885142e-11, -3.3655370157e-11, 103.6333334183)
graarm_2.orientation = Base.Vector (0.0, 0.0, 0.0)
graarm_3 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_dragbrace.graarm_3')
graarm_3.marker_name = '.GCMB.gel_lower_dragbrace.graarm_3'
graarm_3.adams_id = 138
graarm_3.location = Base.Vector (-5.3526627575e-11, -6.6412153554e-11, 207.2666668366)
graarm_3.orientation = Base.Vector (0.0, 0.0, 0.0)
gel_lower_dragbrace = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.cm')
gel_lower_dragbrace.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.inertia_frame')
gel_lower_dragbrace.inertia_marker = inertia_marker
gel_lower_dragbrace.part_name = '.GCMB.gel_lower_dragbrace'
gel_lower_dragbrace.mass = 5.6992574801
gel_lower_dragbrace.ixx = 321105.53519
gel_lower_dragbrace.iyy = 319377.80276
gel_lower_dragbrace.izz = 5107.1748959849
gel_lower_dragbrace.ixy = 0.0
gel_lower_dragbrace.izx = 0.0
gel_lower_dragbrace.iyz = 0.0
gralin_lower_dragbrace = MakeSceneNodeByType('ShapeCylinder', '.GCMB.gel_lower_dragbrace.gralin_lower_dragbrace')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.gralin_26')
gralin_lower_dragbrace.center_marker = center_marker
gralin_lower_dragbrace.cylinder_name = '.GCMB.gel_lower_dragbrace.gralin_lower_dragbrace'
gralin_lower_dragbrace.adams_id = 13
gralin_lower_dragbrace.angle_extent = 360.0
gralin_lower_dragbrace.length = 863.6111118191
gralin_lower_dragbrace.radius = 25.4
gralin_lower_dragbrace.side_count_for_body = 15
gralin_lower_dragbrace.segment_count_for_ends = 15


graarm_uplock_tab = MakeSceneNodeByType('ShapePlate', '.GCMB.gel_lower_dragbrace.graarm_uplock_tab')
# >>>[ERROR] CAN NOT find link prop(marker_name) from .GCMB.gel_lower_dragbrace.graarm_uplock_tab, Please DOUBLE CHECK!
# >>>[ERROR] CAN NOT find link prop(width) from .GCMB.gel_lower_dragbrace.graarm_uplock_tab, Please DOUBLE CHECK!
# >>>[ERROR] CAN NOT find link prop(radius) from .GCMB.gel_lower_dragbrace.graarm_uplock_tab, Please DOUBLE CHECK!
graarm_uplock_tab.plate_name = '.GCMB.gel_lower_dragbrace.graarm_uplock_tab'


gel_upper_torquearm = MakeSceneNodeByType('PartGeneral', '.GCMB.gel_upper_torquearm')
gel_upper_torquearm.part_name = '.GCMB.gel_upper_torquearm'
gel_upper_torquearm.adams_id = 12
gel_upper_torquearm.location = Base.Vector (12079.452409, -1493.9074516, 664.6292016)
gel_upper_torquearm.orientation = Base.Vector (264.4801161257, 168.6067018386, 84.5882371559)
cm = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_torquearm.cm')
cm.marker_name = '.GCMB.gel_upper_torquearm.cm'
cm.adams_id = 147
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_torquearm.inertia_frame')
inertia_frame.marker_name = '.GCMB.gel_upper_torquearm.inertia_frame'
inertia_frame.adams_id = 148
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_11 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_torquearm.gralin_11')
gralin_11.marker_name = '.GCMB.gel_upper_torquearm.gralin_11'
gralin_11.adams_id = 149
gralin_11.location = Base.Vector (-1.0365666658e-10, -2.3080929529e-11, -138.3335383036)
gralin_11.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_i_2 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_torquearm.jxl_joint_i_2')
jxl_joint_i_2.marker_name = '.GCMB.gel_upper_torquearm.jxl_joint_i_2'
jxl_joint_i_2.adams_id = 150
jxl_joint_i_2.location = Base.Vector (9.8605151821e-11, 2.2895314117e-11, 138.3335383036)
jxl_joint_i_2.orientation = Base.Vector (273.4244432527, 89.9999731825, 177.0527623566)
jxl_joint_i_3 = MakeSceneNodeByType('Marker', '.GCMB.gel_upper_torquearm.jxl_joint_i_3')
jxl_joint_i_3.marker_name = '.GCMB.gel_upper_torquearm.jxl_joint_i_3'
jxl_joint_i_3.adams_id = 151
jxl_joint_i_3.location = Base.Vector (-1.0023926134e-10, -2.1990222143e-11, -138.3335383036)
jxl_joint_i_3.orientation = Base.Vector (183.4245252295, 87.0529836943, 74.5991863345)
gel_upper_torquearm = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.cm')
gel_upper_torquearm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.inertia_frame')
gel_upper_torquearm.inertia_marker = inertia_marker
gel_upper_torquearm.part_name = '.GCMB.gel_upper_torquearm'
gel_upper_torquearm.mass = 1.5364744752
gel_upper_torquearm.ixx = 10048.562438
gel_upper_torquearm.iyy = 10048.562438
gel_upper_torquearm.izz = 495.6359362218
gel_upper_torquearm.ixy = 0.0
gel_upper_torquearm.izx = 0.0
gel_upper_torquearm.iyz = 0.0
gralin_upper_torquearm = MakeSceneNodeByType('ShapeCylinder', '.GCMB.gel_upper_torquearm.gralin_upper_torquearm')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.gralin_11')
gralin_upper_torquearm.center_marker = center_marker
gralin_upper_torquearm.cylinder_name = '.GCMB.gel_upper_torquearm.gralin_upper_torquearm'
gralin_upper_torquearm.adams_id = 15
gralin_upper_torquearm.angle_extent = 360.0
gralin_upper_torquearm.length = 276.6670766071
gralin_upper_torquearm.radius = 25.4
gralin_upper_torquearm.side_count_for_body = 15
gralin_upper_torquearm.segment_count_for_ends = 15


gel_lower_torquearm = MakeSceneNodeByType('PartGeneral', '.GCMB.gel_lower_torquearm')
gel_lower_torquearm.part_name = '.GCMB.gel_lower_torquearm'
gel_lower_torquearm.adams_id = 14
gel_lower_torquearm.location = Base.Vector (12099.342641, -1557.9375115, 403.0923612)
gel_lower_torquearm.orientation = Base.Vector (274.806891489, 21.5573785759, 85.5279353352)
cm = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_torquearm.cm')
cm.marker_name = '.GCMB.gel_lower_torquearm.cm'
cm.adams_id = 157
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_torquearm.inertia_frame')
inertia_frame.marker_name = '.GCMB.gel_lower_torquearm.inertia_frame'
inertia_frame.adams_id = 158
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_29 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_torquearm.gralin_29')
gralin_29.marker_name = '.GCMB.gel_lower_torquearm.gralin_29'
gralin_29.adams_id = 159
gralin_29.location = Base.Vector (-9.4070584655e-11, 0.0, -138.7301712808)
gralin_29.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_i_11 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_torquearm.jxl_joint_i_11')
jxl_joint_i_11.marker_name = '.GCMB.gel_lower_torquearm.jxl_joint_i_11'
jxl_joint_i_11.adams_id = 160
jxl_joint_i_11.location = Base.Vector (-9.5902452646e-11, 0.0, -138.7301712808)
jxl_joint_i_11.orientation = Base.Vector (178.1282947989, 95.1813481522, 287.4366988554)
jxl_joint_i_1 = MakeSceneNodeByType('Marker', '.GCMB.gel_lower_torquearm.jxl_joint_i_1')
jxl_joint_i_1.marker_name = '.GCMB.gel_lower_torquearm.jxl_joint_i_1'
jxl_joint_i_1.adams_id = 161
jxl_joint_i_1.location = Base.Vector (9.2766072601e-11, 0.0, 138.7301712808)
jxl_joint_i_1.orientation = Base.Vector (178.1282565411, 95.1813639555, 331.2687567728)
gel_lower_torquearm = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.cm')
gel_lower_torquearm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.inertia_frame')
gel_lower_torquearm.inertia_marker = inertia_marker
gel_lower_torquearm.part_name = '.GCMB.gel_lower_torquearm'
gel_lower_torquearm.mass = 0.45359237
gel_lower_torquearm.ixx = 292.6396534292
gel_lower_torquearm.iyy = 292.6396534292
gel_lower_torquearm.izz = 292.6396534292
gel_lower_torquearm.ixy = 0.0
gel_lower_torquearm.izx = 0.0
gel_lower_torquearm.iyz = 0.0
gralin_lower_torquearm = MakeSceneNodeByType('ShapeCylinder', '.GCMB.gel_lower_torquearm.gralin_lower_torquearm')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.gralin_29')
gralin_lower_torquearm.center_marker = center_marker
gralin_lower_torquearm.cylinder_name = '.GCMB.gel_lower_torquearm.gralin_lower_torquearm'
gralin_lower_torquearm.adams_id = 17
gralin_lower_torquearm.angle_extent = 360.0
gralin_lower_torquearm.length = 277.4603425616
gralin_lower_torquearm.radius = 25.4
gralin_lower_torquearm.side_count_for_body = 15
gralin_lower_torquearm.segment_count_for_ends = 15


gel_connector = MakeSceneNodeByType('PartGeneral', '.GCMB.gel_connector')
gel_connector.part_name = '.GCMB.gel_connector'
gel_connector.adams_id = 17
gel_connector.location = Base.Vector (12049.122257, -1551.2110073, 531.6382052)
gel_connector.orientation = Base.Vector (177.0103140237, 92.4964937717, 309.8285622575)
cm = MakeSceneNodeByType('Marker', '.GCMB.gel_connector.cm')
cm.marker_name = '.GCMB.gel_connector.cm'
cm.adams_id = 169
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.gel_connector.inertia_frame')
inertia_frame.marker_name = '.GCMB.gel_connector.inertia_frame'
inertia_frame.adams_id = 170
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_3 = MakeSceneNodeByType('Marker', '.GCMB.gel_connector.gralin_3')
gralin_3.marker_name = '.GCMB.gel_connector.gralin_3'
gralin_3.adams_id = 171
gralin_3.location = Base.Vector (0.0, 6.2061467077e-11, -60.0708472436)
gralin_3.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_1 = MakeSceneNodeByType('Marker', '.GCMB.gel_connector.jxl_joint_j_1')
jxl_joint_j_1.marker_name = '.GCMB.gel_connector.jxl_joint_j_1'
jxl_joint_j_1.adams_id = 172
jxl_joint_j_1.location = Base.Vector (-3.2030730841e-05, -3.9921405011e-05, -11.0234586256)
jxl_joint_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_2 = MakeSceneNodeByType('Marker', '.GCMB.gel_connector.jxl_joint_j_2')
jxl_joint_j_2.marker_name = '.GCMB.gel_connector.jxl_joint_j_2'
jxl_joint_j_2.adams_id = 173
jxl_joint_j_2.location = Base.Vector (0.0, -6.333583831e-11, 60.0708472436)
jxl_joint_j_2.orientation = Base.Vector (331.5687748605, 89.9998761701, 89.9997712794)
gel_connector = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.cm')
gel_connector.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.inertia_frame')
gel_connector.inertia_marker = inertia_marker
gel_connector.part_name = '.GCMB.gel_connector'
gel_connector.mass = 0.45359237
gel_connector.ixx = 292.6396534292
gel_connector.iyy = 292.6396534292
gel_connector.izz = 292.6396534292
gel_connector.ixy = 0.0
gel_connector.izx = 0.0
gel_connector.iyz = 0.0
gralin_connector = MakeSceneNodeByType('ShapeCylinder', '.GCMB.gel_connector.gralin_connector')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.gralin_3')
gralin_connector.center_marker = center_marker
gralin_connector.cylinder_name = '.GCMB.gel_connector.gralin_connector'
gralin_connector.adams_id = 19
gralin_connector.angle_extent = 360.0
gralin_connector.length = 120.1416944872
gralin_connector.radius = 12.7
gralin_connector.side_count_for_body = 15
gralin_connector.segment_count_for_ends = 15


gel_uc_collar = MakeSceneNodeByType('PartGeneral', '.GCMB.gel_uc_collar')
gel_uc_collar.part_name = '.GCMB.gel_uc_collar'
gel_uc_collar.adams_id = 19
gel_uc_collar.location = Base.Vector (12223.534671, -1499.1580221504, 879.997907387)
gel_uc_collar.orientation = Base.Vector (55.1145661544, 175.2828647294, 235.2057167569)
cm = MakeSceneNodeByType('Marker', '.GCMB.gel_uc_collar.cm')
cm.marker_name = '.GCMB.gel_uc_collar.cm'
cm.adams_id = 179
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.gel_uc_collar.inertia_frame')
inertia_frame.marker_name = '.GCMB.gel_uc_collar.inertia_frame'
inertia_frame.adams_id = 180
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_5 = MakeSceneNodeByType('Marker', '.GCMB.gel_uc_collar.gralin_5')
gralin_5.marker_name = '.GCMB.gel_uc_collar.gralin_5'
gralin_5.adams_id = 181
gralin_5.location = Base.Vector (2.6924643071e-11, 2.2060478444e-11, -108.9542389171)
gralin_5.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_3 = MakeSceneNodeByType('Marker', '.GCMB.gel_uc_collar.jxl_joint_j_3')
jxl_joint_j_3.marker_name = '.GCMB.gel_uc_collar.jxl_joint_j_3'
jxl_joint_j_3.adams_id = 182
jxl_joint_j_3.location = Base.Vector (122.0018852298, 5.9907462808, 71.4829517951)
jxl_joint_j_3.orientation = Base.Vector (182.811221391, 89.9999933852, 90.0001347091)
jxl_joint_i_4 = MakeSceneNodeByType('Marker', '.GCMB.gel_uc_collar.jxl_joint_i_4')
jxl_joint_i_4.marker_name = '.GCMB.gel_uc_collar.jxl_joint_i_4'
jxl_joint_i_4.adams_id = 183
jxl_joint_i_4.location = Base.Vector (-3.0778026931e-10, -6.2083140958e-10, -9.1530054394e-10)
jxl_joint_i_4.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_10 = MakeSceneNodeByType('Marker', '.GCMB.gel_uc_collar.jxl_joint_j_10')
jxl_joint_j_10.marker_name = '.GCMB.gel_uc_collar.jxl_joint_j_10'
jxl_joint_j_10.adams_id = 184
jxl_joint_j_10.location = Base.Vector (109.5796703534, 33.5667968494, -46.8303107227)
jxl_joint_j_10.orientation = Base.Vector (199.444502672, 90.0, 92.2365720495)
gel_uc_collar = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.cm')
gel_uc_collar.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.inertia_frame')
gel_uc_collar.inertia_marker = inertia_marker
gel_uc_collar.part_name = '.GCMB.gel_uc_collar'
gel_uc_collar.mass = 30.2539444008
gel_uc_collar.ixx = 241706.5893
gel_uc_collar.iyy = 241706.5893
gel_uc_collar.izz = 243982.93462
gel_uc_collar.ixy = 0.0
gel_uc_collar.izx = 0.0
gel_uc_collar.iyz = 0.0
gralin_uc_collar = MakeSceneNodeByType('ShapeCylinder', '.GCMB.gel_uc_collar.gralin_uc_collar')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.gralin_5')
gralin_uc_collar.center_marker = center_marker
gralin_uc_collar.cylinder_name = '.GCMB.gel_uc_collar.gralin_uc_collar'
gralin_uc_collar.adams_id = 21
gralin_uc_collar.angle_extent = 360.0
gralin_uc_collar.length = 217.9084778341
gralin_uc_collar.radius = 127.0
gralin_uc_collar.side_count_for_body = 15
gralin_uc_collar.segment_count_for_ends = 15


jolrev_lta_lc_joint = MakeSceneNodeByType('JointRevolute', '.GCMB.jolrev_lta_lc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.jxl_joint_i_11')
jolrev_lta_lc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.jxl_joint_j_11')
jolrev_lta_lc_joint.j_marker_name = j_marker_name
jolrev_lta_lc_joint.joint_name = '.GCMB.jolrev_lta_lc_joint'
jolrev_lta_lc_joint.adams_id = 2


jolcyl_lc_uc_joint = MakeSceneNodeByType('JointCylinder', '.GCMB.jolcyl_lc_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.jxl_joint_i_12')
jolcyl_lc_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.jxl_joint_j_12')
jolcyl_lc_uc_joint.j_marker_name = j_marker_name
jolcyl_lc_uc_joint.joint_name = '.GCMB.jolcyl_lc_uc_joint'
jolcyl_lc_uc_joint.adams_id = 4


jolrev_ldb_udb_joint = MakeSceneNodeByType('JointFixed', '.GCMB.jolrev_ldb_udb_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.jxl_joint_i_14')
jolrev_ldb_udb_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.jxl_joint_j_14')
jolrev_ldb_udb_joint.j_marker_name = j_marker_name
jolrev_ldb_udb_joint.joint_name = '.GCMB.jolrev_ldb_udb_joint'
jolrev_ldb_udb_joint.adams_id = 6


JOINT_58 = MakeSceneNodeByType('JointFixed', '.GCMB.JOINT_58')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_207')
JOINT_58.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.MARKER_208')
JOINT_58.j_marker_name = j_marker_name
JOINT_58.joint_name = '.GCMB.JOINT_58'
JOINT_58.adams_id = 35


JOINT_56 = MakeSceneNodeByType('JointPlanar', '.GCMB.JOINT_56')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_210')
JOINT_56.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ground.MARKER_211')
JOINT_56.j_marker_name = j_marker_name
JOINT_56.joint_name = '.GCMB.JOINT_56'
JOINT_56.adams_id = 36


JOINT_37 = MakeSceneNodeByType('JointFixed', '.GCMB.JOINT_37')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_233')
JOINT_37.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.MARKER_234')
JOINT_37.j_marker_name = j_marker_name
JOINT_37.joint_name = '.GCMB.JOINT_37'
JOINT_37.adams_id = 37


jolcyl_lta_connect = MakeSceneNodeByType('JointCylinder', '.GCMB.jolcyl_lta_connect')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.jxl_joint_i_1')
jolcyl_lta_connect.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.jxl_joint_j_1')
jolcyl_lta_connect.j_marker_name = j_marker_name
jolcyl_lta_connect.joint_name = '.GCMB.jolcyl_lta_connect'
jolcyl_lta_connect.adams_id = 12


jolrev_uta_connect = MakeSceneNodeByType('JointRevolute', '.GCMB.jolrev_uta_connect')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.jxl_joint_i_2')
jolrev_uta_connect.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.jxl_joint_j_2')
jolrev_uta_connect.j_marker_name = j_marker_name
jolrev_uta_connect.joint_name = '.GCMB.jolrev_uta_connect'
jolrev_uta_connect.adams_id = 14


jolrev_uta_collar = MakeSceneNodeByType('JointRevolute', '.GCMB.jolrev_uta_collar')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.jxl_joint_i_3')
jolrev_uta_collar.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_j_3')
jolrev_uta_collar.j_marker_name = j_marker_name
jolrev_uta_collar.joint_name = '.GCMB.jolrev_uta_collar'
jolrev_uta_collar.adams_id = 16


jolrev_collar_uc = MakeSceneNodeByType('JointFixed', '.GCMB.jolrev_collar_uc')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_i_4')
jolrev_collar_uc.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.jxl_joint_j_4')
jolrev_collar_uc.j_marker_name = j_marker_name
jolrev_collar_uc.joint_name = '.GCMB.jolrev_collar_uc'
jolrev_collar_uc.adams_id = 18


jolrev_ldb_collar = MakeSceneNodeByType('JointRevolute', '.GCMB.jolrev_ldb_collar')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.jxl_joint_i_10')
jolrev_ldb_collar.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_j_10')
jolrev_ldb_collar.j_marker_name = j_marker_name
jolrev_ldb_collar.joint_name = '.GCMB.jolrev_ldb_collar'
jolrev_ldb_collar.adams_id = 30


JPRIM_3 = MakeSceneNodeByType('JointPerpendicular', '.GCMB.JPRIM_3')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_214')
JPRIM_3.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ground.MARKER_215')
JPRIM_3.j_marker_name = j_marker_name
JPRIM_3.jprim_name = '.GCMB.JPRIM_3'
JPRIM_3.adams_id = 1


LMLG_AIR = MakeSceneNodeByType('ForceSingleComponent', '.GCMB.LMLG_AIR')
LMLG_AIR.type_of_freedom = 'translational'
LMLG_AIR.action_only = False
LMLG_AIR.function_opt = 0
LMLG_AIR.function = '""'
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.MARKER_218')
LMLG_AIR.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.MARKER_219')
LMLG_AIR.j_marker_name = j_marker_name
LMLG_AIR.position_define_opt = 1


LMLG_OIL = MakeSceneNodeByType('ForceSingleComponent', '.GCMB.LMLG_OIL')
LMLG_OIL.type_of_freedom = 'translational'
LMLG_OIL.action_only = False
LMLG_OIL.function_opt = 0
LMLG_OIL.function = '""'
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.MARKER_220')
LMLG_OIL.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.MARKER_221')
LMLG_OIL.j_marker_name = j_marker_name
LMLG_OIL.position_define_opt = 1


LMLG_STOP = MakeSceneNodeByType('ForceSingleComponent', '.GCMB.LMLG_STOP')
LMLG_STOP.type_of_freedom = 'translational'
LMLG_STOP.action_only = False
LMLG_STOP.function_opt = 0
LMLG_STOP.function = '""'
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.MARKER_222')
LMLG_STOP.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.MARKER_223')
LMLG_STOP.j_marker_name = j_marker_name
LMLG_STOP.position_define_opt = 1


Driving_force = MakeSceneNodeByType('ForceSingleComponent', '.GCMB.Driving_force')
Driving_force.type_of_freedom = 'translational'
Driving_force.action_only = True
Driving_force.function_opt = 0
Driving_force.function = '""'
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_239')
Driving_force.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ground.MARKER_240')
Driving_force.j_marker_name = j_marker_name
Driving_force.position_define_opt = 1


Last_Sim = MakeSceneNodeByType('SimuScript', '.GCMB.Last_Sim')
Last_Sim.sim_script_name = '.GCMB.Last_Sim'
Last_Sim.commands = '"simulation single_run transient type=auto_select initial_static=no end_time=30.0 step_size=1.0E-02 model_name=.GCMB"'

# ---- TireCMD support (converted from Adams/Car vpg_tire/vpg_road UDE) ----
import os
from FmbsShortcut.import_all_node import MakeSceneNodeByType as SCMakeSceneNodeByType
import FmbsShortcut.SCcmd.TireCMD as TireCMD
_MODEL_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_MODEL_RESOURCE_DIR = os.path.join(_MODEL_SCRIPT_DIR, 'resources', os.path.splitext(os.path.basename(__file__))[0])
scene = Jusme.ActiveUSScene
tire_defaults_units = MakeSceneNodeByType('DefaultsUnits', 'defaultsunits')
tire_defaults_units.length = 'Millimeter'

# Tire converted from .GCMB.luntai
parameter = SCMakeSceneNodeByType('Tire', 'Tire_input_1')
parameter.tire_name = 'luntai'
parameter.tire_file_path = os.path.join(_MODEL_RESOURCE_DIR, 'MLG.tir')
parameter.road_file_path = os.path.join(_MODEL_RESOURCE_DIR, '2d_flat.rdf')
parameter.mass = 45.359237
parameter.Ixx_Iyy = 2721548.7769
parameter.Izz = 4682234.4549
parameter.tire_center_direction_opt = 0
parameter.tire_euler_angles = (0.0, 90.0, 0.0)
center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center')
parameter.tire_center_location = center.location
parameter.road_name = 'road'
parameter.road_direction_opt = 0
parameter.road_euler_angles = (0.0, 0.0, 0.0)
parameter.road_belong_part = Jusme.ActiveUSScene.getObject('.GCMB.ground')
parameter.longitudinal_velocities = 0.0
parameter.spin_velocities = 0.0
TireCMD.run_test('Tire_input_1')

MARKER_202 = MakeSceneNodeByType('Marker', '.GCMB.luntai.wheel_part.MARKER_202')
MARKER_202.marker_name = '.GCMB.luntai.wheel_part.MARKER_202'
MARKER_202.adams_id = 202
MARKER_202.location = Base.Vector (-1.4000178794e-07, 0.0, 3.9999781265e-08)
MARKER_202.orientation = Base.Vector (359.9999064822, 91.0000312229, 359.9999983678)
MARKER_224 = MakeSceneNodeByType('Marker', '.GCMB.luntai.wheel_part.MARKER_224')
MARKER_224.marker_name = '.GCMB.luntai.wheel_part.MARKER_224'
MARKER_224.adams_id = 224
MARKER_224.location = Base.Vector (-1.4000178794e-07, 0.0, 3.9999781265e-08)
MARKER_224.orientation = Base.Vector (0.0, 90.0, 0.0)
MARKER_225 = MakeSceneNodeByType('Marker', '.GCMB.luntai.wheel_part.MARKER_225')
MARKER_225.marker_name = '.GCMB.luntai.wheel_part.MARKER_225'
MARKER_225.adams_id = 225
MARKER_225.location = Base.Vector (-1.4000178794e-07, 0.0, 3.9999781265e-08)
MARKER_225.orientation = Base.Vector (0.0, 90.0, 0.0)
JOINT_33 = MakeSceneNodeByType('JointRevolute', '.GCMB.JOINT_33')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part.MARKER_202')
JOINT_33.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.MARKER_203')
JOINT_33.j_marker_name = j_marker_name
JOINT_33.joint_name = '.GCMB.JOINT_33'
JOINT_33.adams_id = 33


LMLG_M = MakeSceneNodeByType('ForceSingleComponent', '.GCMB.LMLG_M')
LMLG_M.type_of_freedom = 'rotational'
LMLG_M.action_only = True
LMLG_M.function_opt = 0
LMLG_M.function = '""'
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part.MARKER_224')
LMLG_M.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part.MARKER_225')
LMLG_M.j_marker_name = j_marker_name
LMLG_M.position_define_opt = 1


gravity = MakeSceneNodeByType('Gravity', '.GCMB.gravity')
gravity.gravity_field_name = 'gravity'
gravity.z_component_gravity = -9809.9999999989


js_sd = MakeSceneNodeByType('Pt2pt', '.GCMB.js_sd')
js_sd.component_opt = 3
js_sd.characteristic_opt = 1
from_point = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo')
js_sd.from_point = from_point
to_point = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.cm')
js_sd.to_point = to_point


GAMA = MakeSceneNodeByType('DesignVariable', '.GCMB.GAMA')
GAMA.variable_name = '.GCMB.GAMA'
GAMA.units = '"no_units"'
GAMA.range = [-6.4516e-04, 6.4516e-04]
GAMA.use_range = True
GAMA.use_allowed_values = False
GAMA.delta_type = 0
GAMA.value_type_opt = 0
GAMA.real_value = 1.1


Patm = MakeSceneNodeByType('DesignVariable', '.GCMB.Patm')
Patm.variable_name = '.GCMB.Patm'
Patm.units = '"pressure"'
Patm.range = [-6.4516e-10, 6.4516e-10]
Patm.use_range = True
Patm.use_allowed_values = False
Patm.delta_type = 0
Patm.value_type_opt = 0
Patm.real_value = 0.101325


rou = MakeSceneNodeByType('DesignVariable', '.GCMB.rou')
rou.variable_name = '.GCMB.rou'
rou.units = '"density"'
rou.range = [0.0, 0.0]
rou.use_range = True
rou.use_allowed_values = False
rou.delta_type = 0
rou.value_type_opt = 0
rou.real_value = 8.6e-07


MLG_Aa = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_Aa')
MLG_Aa.variable_name = '.GCMB.MLG_Aa'
MLG_Aa.units = '"area"'
MLG_Aa.range = [-645.16, 645.16]
MLG_Aa.use_range = True
MLG_Aa.use_allowed_values = False
MLG_Aa.delta_type = 0
MLG_Aa.value_type_opt = 0
MLG_Aa.real_value = 8921.0


MLG_V0 = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_V0')
MLG_V0.variable_name = '.GCMB.MLG_V0'
MLG_V0.units = '"volume"'
MLG_V0.range = [-6.4516e+05, 6.4516e+05]
MLG_V0.use_range = True
MLG_V0.use_allowed_values = False
MLG_V0.delta_type = 0
MLG_V0.value_type_opt = 0
MLG_V0.real_value = 3931000.0


MLG_P0 = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_P0')
MLG_P0.variable_name = '.GCMB.MLG_P0'
MLG_P0.units = '"pressure"'
MLG_P0.range = [-6.4516e-10, 6.4516e-10]
MLG_P0.use_range = True
MLG_P0.use_allowed_values = False
MLG_P0.delta_type = 0
MLG_P0.value_type_opt = 0
MLG_P0.real_value = 1.45


MLG_Ah = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_Ah')
MLG_Ah.variable_name = '.GCMB.MLG_Ah'
MLG_Ah.units = '"area"'
MLG_Ah.range = [-645.16, 645.16]
MLG_Ah.use_range = True
MLG_Ah.use_allowed_values = False
MLG_Ah.delta_type = 0
MLG_Ah.value_type_opt = 0
MLG_Ah.real_value = 55571.0


MLG_As = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_As')
MLG_As.variable_name = '.GCMB.MLG_As'
MLG_As.units = '"area"'
MLG_As.range = [-645.16, 645.16]
MLG_As.use_range = True
MLG_As.use_allowed_values = False
MLG_As.delta_type = 0
MLG_As.value_type_opt = 0
MLG_As.real_value = 14961.0


MLG_Ahd = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_Ahd')
MLG_Ahd.variable_name = '.GCMB.MLG_Ahd'
MLG_Ahd.units = '"area"'
MLG_Ahd.range = [-645.16, 645.16]
MLG_Ahd.use_range = True
MLG_Ahd.use_allowed_values = False
MLG_Ahd.delta_type = 0
MLG_Ahd.value_type_opt = 0
MLG_Ahd.real_value = 1960.0


MLG_Ahdl = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_Ahdl')
MLG_Ahdl.variable_name = '.GCMB.MLG_Ahdl'
MLG_Ahdl.units = '"area"'
MLG_Ahdl.range = [-645.16, 645.16]
MLG_Ahdl.use_range = True
MLG_Ahdl.use_allowed_values = False
MLG_Ahdl.delta_type = 0
MLG_Ahdl.value_type_opt = 0
MLG_Ahdl.real_value = 1960.0


MLG_Asd = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_Asd')
MLG_Asd.variable_name = '.GCMB.MLG_Asd'
MLG_Asd.units = '"area"'
MLG_Asd.range = [-645.16, 645.16]
MLG_Asd.use_range = True
MLG_Asd.use_allowed_values = False
MLG_Asd.delta_type = 0
MLG_Asd.value_type_opt = 0
MLG_Asd.real_value = 3798.0


MLG_Asdl = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_Asdl')
MLG_Asdl.variable_name = '.GCMB.MLG_Asdl'
MLG_Asdl.units = '"area"'
MLG_Asdl.range = [-645.16, 645.16]
MLG_Asdl.use_range = True
MLG_Asdl.use_allowed_values = False
MLG_Asdl.delta_type = 0
MLG_Asdl.value_type_opt = 0
MLG_Asdl.real_value = 157.0


MLG_Ch = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_Ch')
MLG_Ch.variable_name = '.GCMB.MLG_Ch'
MLG_Ch.units = '"no_units"'
MLG_Ch.range = [-6.4516e-04, 6.4516e-04]
MLG_Ch.use_range = True
MLG_Ch.use_allowed_values = False
MLG_Ch.delta_type = 0
MLG_Ch.value_type_opt = 0
MLG_Ch.real_value = 0.8


MLG_Cs = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_Cs')
MLG_Cs.variable_name = '.GCMB.MLG_Cs'
MLG_Cs.units = '"no_units"'
MLG_Cs.range = [-6.4516e-04, 6.4516e-04]
MLG_Cs.use_range = True
MLG_Cs.use_allowed_values = False
MLG_Cs.delta_type = 0
MLG_Cs.value_type_opt = 0
MLG_Cs.real_value = 0.8


M = MakeSceneNodeByType('DesignVariable', '.GCMB.M')
M.variable_name = '.GCMB.M'
M.units = '"no_units"'
M.range = [-1.0, 1.0]
M.use_range = True
M.use_allowed_values = False
M.delta_type = 0
M.value_type_opt = 0
M.real_value = -2000000.0


MLG_S0 = MakeSceneNodeByType('DesignVariable', '.GCMB.MLG_S0')
MLG_S0.variable_name = '.GCMB.MLG_S0'
MLG_S0.units = '"length"'
MLG_S0.range = [-1.0, 1.0]
MLG_S0.use_range = True
MLG_S0.use_allowed_values = False
MLG_S0.delta_type = 0
MLG_S0.value_type_opt = 0
MLG_S0.real_value = 1014.262


V_sheding = MakeSceneNodeByType('DesignVariable', '.GCMB.V_sheding')
V_sheding.variable_name = '.GCMB.V_sheding'
V_sheding.units = '"velocity"'
V_sheding.range = [-1.0, 1.0]
V_sheding.use_range = True
V_sheding.use_allowed_values = False
V_sheding.delta_type = 0
V_sheding.value_type_opt = 0
V_sheding.real_value = 10000.0


LMLG_S = Jusme.ActiveUSScene.getObject('.GCMB.LMLG_S')
LMLG_S.variable_name = '.GCMB.LMLG_S'
LMLG_S.function = '".GCMB.MLG_S0-DM(.GCMB.gel_upper_cylinder.MARKER_216,.GCMB.gel_lower_cylinder.MARKER_217)"'


LMLG_V = Jusme.ActiveUSScene.getObject('.GCMB.LMLG_V')
LMLG_V.variable_name = '.GCMB.LMLG_V'
LMLG_V.function = '"-1*VR(.GCMB.gel_upper_cylinder.MARKER_216,.GCMB.gel_lower_cylinder.MARKER_217)"'


LMLG_AIR = Jusme.ActiveUSScene.getObject('.GCMB.LMLG_AIR')
LMLG_AIR.function = '"3*.GCMB.MLG_Aa*(.GCMB.MLG_P0*(.GCMB.MLG_V0/(.GCMB.MLG_V0-.GCMB.MLG_Aa*VARVAL(.GCMB.LMLG_S)))**1.1-.GCMB.Patm)"'


LMLG_OIL = Jusme.ActiveUSScene.getObject('.GCMB.LMLG_OIL')
LMLG_OIL.function = '"IF(VARVAL(.GCMB.LMLG_V):0.003*-1*(VARVAL(.GCMB.LMLG_V)*0.5*(VARVAL(.GCMB.LMLG_V)-ABS(VARVAL(.GCMB.LMLG_V)))*((.GCMB.rou*.GCMB.MLG_Ah**3/(2*.GCMB.MLG_Ch**2*.GCMB.MLG_Ahdl**2))+(.GCMB.rou*.GCMB.MLG_As**3/(2*.GCMB.MLG_Cs**2*.GCMB.MLG_Asdl**2)))),0,0.003*VARVAL(.GCMB.LMLG_V)*0.5*(VARVAL(.GCMB.LMLG_V)+ABS(VARVAL(.GCMB.LMLG_V)))*((.GCMB.rou*.GCMB.MLG_Ah**3/(2*.GCMB.MLG_Ch**2*.GCMB.MLG_Ahd**2))+(.GCMB.rou*.GCMB.MLG_As**3/(2*.GCMB.MLG_Cs**2*.GCMB.MLG_Asd**2))))"'


LMLG_STOP = Jusme.ActiveUSScene.getObject('.GCMB.LMLG_STOP')
LMLG_STOP.function = '"IF(.GCMB.MLG_S0-DM(.GCMB.gel_upper_cylinder.MARKER_216,.GCMB.gel_lower_cylinder.MARKER_217) :1.0E+09*(.GCMB.MLG_S0-DM(.GCMB.gel_upper_cylinder.MARKER_216,.GCMB.gel_lower_cylinder.MARKER_217)) , 0 , 0 )"'


LMLG_M = Jusme.ActiveUSScene.getObject('.GCMB.LMLG_M')
LMLG_M.function = '"if(vx(.GCMB.zhiliang.cm,.GCMB.ground.MARKER_226):if(time-8:0,0,.GCMB.M),0,0)"'


Driving_force = Jusme.ActiveUSScene.getObject('.GCMB.Driving_force')
Driving_force.function = '"-30000*2/3.14*atan(.GCMB.V_sheding-.GCMB.js_sd)*(STEP (TIME,0,0,1.2,1)-STEP (TIME,4.8,0,5.0,1))"'


# TireCMD handles initial-velocity reference for .GCMB.luntai.wheel_part (vm=.GCMB.luntai.wheel_part.wheel_cm, wm=.GCMB.luntai.wheel_part.wheel_cm)
# TireCMD handles initial-velocity reference for .GCMB.luntai.belt_part (vm=.GCMB.luntai.wheel_part.wheel_cm, wm=.GCMB.luntai.wheel_part.wheel_cm)
cfl_spin_axis = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_spin_axis')
cfl_spin_axis.marker_name = '.GCMB.ground.cfl_spin_axis'
_GCMB_ground_cfl_spin_axis_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_spin_axis_1')
cfl_spin_axis.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfl_spin_axis_1))
_GCMB_ground_cfl_spin_axis_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_spin_axis_1')
cfl_spin_axis.orientation = (VecUtils.ORI_RELATIVE_TO([180.0, 180.0, 180.0], _GCMB_ground_cfl_spin_axis_1))


cfl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_uc_top')
cfl_uc_top.marker_name = '.GCMB.ground.cfl_uc_top'
_GCMB_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_top')
cfl_uc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_uc_top))
_GCMB_ground_origo = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo')
cfl_uc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo))


cfl_collar_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_collar_top')
cfl_collar_top.marker_name = '.GCMB.ground.cfl_collar_top'
_GCMB_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_top').location
_GCMB_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_bot').location
cfl_collar_top.location = (VecUtils.LOC_ALONG_LINE(_GCMB_ground_hpl_uc_top, _GCMB_ground_hpl_lc_bot, 0.59 * VecUtils.DM(_GCMB_ground_hpl_uc_top, _GCMB_ground_hpl_lc_bot)))
_GCMB_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_top').location
_GCMB_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_bot').location
cfl_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_uc_top, _GCMB_ground_hpl_lc_bot, "Z"))


cfl_collar_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_collar_bot')
cfl_collar_bot.marker_name = '.GCMB.ground.cfl_collar_bot'
_GCMB_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_top').location
_GCMB_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_bot').location
cfl_collar_bot.location = (VecUtils.LOC_ALONG_LINE(_GCMB_ground_hpl_uc_top, _GCMB_ground_hpl_lc_bot, 0.7 * VecUtils.DM(_GCMB_ground_hpl_uc_top, _GCMB_ground_hpl_lc_bot)))
_GCMB_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_top').location
_GCMB_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_bot').location
cfl_collar_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_uc_top, _GCMB_ground_hpl_lc_bot, "Z"))


cfl_plane_ref_2 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_plane_ref_2')
cfl_plane_ref_2.marker_name = '.GCMB.ground.cfl_plane_ref_2'
_GCMB_ground_cfl_plane_ref = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_plane_ref')
cfl_plane_ref_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfl_plane_ref))
_GCMB_ground_cfl_plane_ref = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_plane_ref')
cfl_plane_ref_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, -90.0, 0.0], _GCMB_ground_cfl_plane_ref))


cfl_spin_axis_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_spin_axis_1')
cfl_spin_axis_1.marker_name = '.GCMB.ground.cfl_spin_axis_1'
_GCMB_ground_hpl_wheel_center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center')
cfl_spin_axis_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_wheel_center))
_GCMB_ground_hpl_wheel_center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center').location
_GCMB_ground_hpl_ob_axle = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ob_axle').location
cfl_spin_axis_1.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_wheel_center, _GCMB_ground_hpl_ob_axle, "Z"))


cfl_ldb_geompt_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_ldb_geompt_1')
cfl_ldb_geompt_1.marker_name = '.GCMB.ground.cfl_ldb_geompt_1'
_GCMB_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_udb_atch_1').location
_GCMB_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_collar_atch_1').location
cfl_ldb_geompt_1.location = (VecUtils.LOC_ALONG_LINE(_GCMB_ground_hpl_ldb_udb_atch_1, _GCMB_ground_hpl_ldb_collar_atch_1, 0.62 * VecUtils.DM(_GCMB_ground_hpl_ldb_udb_atch_1, _GCMB_ground_hpl_ldb_collar_atch_1)))
_GCMB_ground_origo = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo')
cfl_ldb_geompt_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo))


cfl_ldb_geompt_2 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_ldb_geompt_2')
cfl_ldb_geompt_2.marker_name = '.GCMB.ground.cfl_ldb_geompt_2'
_GCMB_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_udb_atch_1').location
_GCMB_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_collar_atch_1').location
cfl_ldb_geompt_2.location = (VecUtils.LOC_ALONG_LINE(_GCMB_ground_hpl_ldb_udb_atch_1, _GCMB_ground_hpl_ldb_collar_atch_1, 0.74 * VecUtils.DM(_GCMB_ground_hpl_ldb_udb_atch_1, _GCMB_ground_hpl_ldb_collar_atch_1)))
_GCMB_ground_origo = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo')
cfl_ldb_geompt_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo))


lumian_1_ref_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.lumian_1_ref_1')
lumian_1_ref_1.marker_name = '.GCMB.ground.lumian_1_ref_1'
lumian_1_ref_1.location = Base.Vector (12270.973957, 1811.5919597, -282.740481)
lumian_1_ref_1.orientation = Base.Vector (0.0, 0.0, 0.0)


MARKER_240 = Jusme.ActiveUSScene.getObject('.GCMB.ground.MARKER_240')
MARKER_240.marker_name = '.GCMB.ground.MARKER_240'
_GCMB_ground_POINT_48 = Jusme.ActiveUSScene.getObject('.GCMB.ground.POINT_48')
MARKER_240.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_POINT_48))


aluminum = Jusme.ActiveUSScene.getObject('.GCMB.aluminum')
aluminum.material_name = '.GCMB.aluminum'


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.gel_upper_cylinder.inertia_frame'
_GCMB_gel_upper_cylinder_cm = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_cylinder_cm))
_GCMB_gel_upper_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_12 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.gralin_12')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder')
gralin_12.relative_to = relative_to
gralin_12.marker_name = '.GCMB.gel_upper_cylinder.gralin_12'
_GCMB_ground_cfl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_uc_top')
gralin_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfl_uc_top))
_GCMB_ground_cfl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_uc_top').location
_GCMB_ground_hpl_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_bot').location
gralin_12.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_cfl_uc_top, _GCMB_ground_hpl_uc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_12.location, gralin_12.orientation)
gralin_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uel_spring_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.uel_spring_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder')
uel_spring_j_1.relative_to = relative_to
uel_spring_j_1.marker_name = '.GCMB.gel_upper_cylinder.uel_spring_j_1'
_GCMB_ground_cfl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_uc_top')
uel_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfl_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_spring_j_1.location, uel_spring_j_1.orientation)
uel_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_upper_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.gralin_upper_cylinder')
gralin_upper_cylinder.cylinder_name = '.GCMB.gel_upper_cylinder.gralin_upper_cylinder'
_GCMB_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_top').location
_GCMB_ground_hpl_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_bot').location
gralin_upper_cylinder.length = (VecUtils.DM(_GCMB_ground_hpl_uc_top, _GCMB_ground_hpl_uc_bot))


MARKER_216 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.MARKER_216')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder')
MARKER_216.relative_to = relative_to
MARKER_216.marker_name = '.GCMB.gel_upper_cylinder.MARKER_216'
_GCMB_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_top')
MARKER_216.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_216.location, MARKER_216.orientation)
MARKER_216.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_218 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.MARKER_218')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder')
MARKER_218.relative_to = relative_to
MARKER_218.marker_name = '.GCMB.gel_upper_cylinder.MARKER_218'
_GCMB_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_top')
MARKER_218.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_218.location, MARKER_218.orientation)
MARKER_218.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_220 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.MARKER_220')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder')
MARKER_220.relative_to = relative_to
MARKER_220.marker_name = '.GCMB.gel_upper_cylinder.MARKER_220'
_GCMB_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uc_top')
MARKER_220.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_220.location, MARKER_220.orientation)
MARKER_220.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_234 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.MARKER_234')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder')
MARKER_234.relative_to = relative_to
MARKER_234.marker_name = '.GCMB.gel_upper_cylinder.MARKER_234'
_GCMB_ground_POINT_48 = Jusme.ActiveUSScene.getObject('.GCMB.ground.POINT_48')
MARKER_234.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_POINT_48))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_234.location, MARKER_234.orientation)
MARKER_234.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.gel_lower_cylinder.inertia_frame'
_GCMB_gel_lower_cylinder_cm = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_lower_cylinder_cm))
_GCMB_gel_lower_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_lower_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_14 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.gralin_14')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
gralin_14.relative_to = relative_to
gralin_14.marker_name = '.GCMB.gel_lower_cylinder.gralin_14'
_GCMB_ground_hpl_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_top')
gralin_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_lc_top))
_GCMB_ground_hpl_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_top').location
_GCMB_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_bot').location
gralin_14.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_lc_top, _GCMB_ground_hpl_lc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_14.location, gralin_14.orientation)
gralin_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_22 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.gralin_22')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
gralin_22.relative_to = relative_to
gralin_22.marker_name = '.GCMB.gel_lower_cylinder.gralin_22'
_GCMB_ground_hpl_ib_axle = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ib_axle')
gralin_22.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_ib_axle))
_GCMB_ground_hpl_ib_axle = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ib_axle').location
_GCMB_ground_hpl_ob_axle = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ob_axle').location
gralin_22.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_ib_axle, _GCMB_ground_hpl_ob_axle, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_22.location, gralin_22.orientation)
gralin_22.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_22.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_11 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.jxl_joint_j_11')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
jxl_joint_j_11.relative_to = relative_to
jxl_joint_j_11.marker_name = '.GCMB.gel_lower_cylinder.jxl_joint_j_11'
_GCMB_ground_hpl_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_lc_atch_1')
jxl_joint_j_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_lta_lc_atch_1))
_GCMB_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_connect_atch_1').location
_GCMB_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_1').location
jxl_joint_j_11.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_lta_connect_atch_1, _GCMB_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_11.location, jxl_joint_j_11.orientation)
jxl_joint_j_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_12 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.jxl_joint_i_12')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
jxl_joint_i_12.relative_to = relative_to
jxl_joint_i_12.marker_name = '.GCMB.gel_lower_cylinder.jxl_joint_i_12'
_GCMB_gel_upper_cylinder_jxl_joint_j_12 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.jxl_joint_j_12')
jxl_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_cylinder_jxl_joint_j_12))
_GCMB_gel_upper_cylinder_jxl_joint_j_12 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.jxl_joint_j_12')
jxl_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_cylinder_jxl_joint_j_12))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_12.location, jxl_joint_i_12.orientation)
jxl_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


coomarker_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.coomarker_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
coomarker_1.relative_to = relative_to
coomarker_1.marker_name = '.GCMB.gel_lower_cylinder.coomarker_1'
_GCMB_ground_cfl_spin_axis = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_spin_axis')
coomarker_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfl_spin_axis))
_GCMB_ground_cfl_spin_axis = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_spin_axis')
coomarker_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfl_spin_axis))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_1.location, coomarker_1.orientation)
coomarker_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
coomarker_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uel_spring_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.uel_spring_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
uel_spring_i_1.relative_to = relative_to
uel_spring_i_1.marker_name = '.GCMB.gel_lower_cylinder.uel_spring_i_1'
_GCMB_ground_hpl_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_top')
uel_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_spring_i_1.location, uel_spring_i_1.orientation)
uel_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uel_damper_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.uel_damper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
uel_damper_i_1.relative_to = relative_to
uel_damper_i_1.marker_name = '.GCMB.gel_lower_cylinder.uel_damper_i_1'
_GCMB_ground_hpl_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_top')
uel_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_damper_i_1.location, uel_damper_i_1.orientation)
uel_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uel_stopper_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.uel_stopper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
uel_stopper_i_1.relative_to = relative_to
uel_stopper_i_1.marker_name = '.GCMB.gel_lower_cylinder.uel_stopper_i_1'
_GCMB_ground_hpl_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_top')
uel_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_i_1.location, uel_stopper_i_1.orientation)
uel_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_lower_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.gralin_lower_cylinder')
gralin_lower_cylinder.cylinder_name = '.GCMB.gel_lower_cylinder.gralin_lower_cylinder'
_GCMB_ground_hpl_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_top').location
_GCMB_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lc_bot').location
gralin_lower_cylinder.length = (VecUtils.DM(_GCMB_ground_hpl_lc_top, _GCMB_ground_hpl_lc_bot))


gralin_geom = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.gralin_geom')
gralin_geom.cylinder_name = '.GCMB.gel_lower_cylinder.gralin_geom'
_GCMB_ground_hpl_ib_axle = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ib_axle').location
_GCMB_ground_hpl_ob_axle = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ob_axle').location
gralin_geom.length = (VecUtils.DM(_GCMB_ground_hpl_ib_axle, _GCMB_ground_hpl_ob_axle))


MARKER_203 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.MARKER_203')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder')
MARKER_203.relative_to = relative_to
MARKER_203.marker_name = '.GCMB.gel_lower_cylinder.MARKER_203'
_GCMB_ground_hpl_wheel_center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center')
MARKER_203.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_wheel_center))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_203.location, MARKER_203.orientation)
MARKER_203.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.gel_upper_dragbrace.inertia_frame'
_GCMB_gel_upper_dragbrace_cm = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_dragbrace_cm))
_GCMB_gel_upper_dragbrace = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_24 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.gralin_24')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace')
gralin_24.relative_to = relative_to
gralin_24.marker_name = '.GCMB.gel_upper_dragbrace.gralin_24'
_GCMB_ground_hpl_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_udb_spndl_atch_1')
gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_udb_spndl_atch_1))
_GCMB_ground_hpl_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_udb_spndl_atch_1').location
_GCMB_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_udb_atch_1').location
gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_udb_spndl_atch_1, _GCMB_ground_hpl_ldb_udb_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_14 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.jxl_joint_j_14')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace')
jxl_joint_j_14.relative_to = relative_to
jxl_joint_j_14.marker_name = '.GCMB.gel_upper_dragbrace.jxl_joint_j_14'
_GCMB_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_udb_atch_1')
jxl_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_ldb_udb_atch_1))
_GCMB_gel_upper_dragbrace = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace')
_GCMB_ground_cfl_plane_ref_2 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_plane_ref_2').global_loc
jxl_joint_j_14.orientation = (ORI_LOCAL(ORI_ALIGN_AXIS(_GCMB_ground_cfl_plane_ref_2, "Z+Z"), _GCMB_gel_upper_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_14.location, jxl_joint_j_14.orientation)
jxl_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uel_actuator_i_3 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.uel_actuator_i_3')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace')
uel_actuator_i_3.relative_to = relative_to
uel_actuator_i_3.marker_name = '.GCMB.gel_upper_dragbrace.uel_actuator_i_3'
_GCMB_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_udb_atch_1')
uel_actuator_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_ldb_udb_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_i_3.location, uel_actuator_i_3.orientation)
uel_actuator_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_upper_dragbrace = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.gralin_upper_dragbrace')
gralin_upper_dragbrace.cylinder_name = '.GCMB.gel_upper_dragbrace.gralin_upper_dragbrace'
_GCMB_ground_hpl_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_udb_spndl_atch_1').location
_GCMB_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_udb_atch_1').location
gralin_upper_dragbrace.length = (VecUtils.DM(_GCMB_ground_hpl_udb_spndl_atch_1, _GCMB_ground_hpl_ldb_udb_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.gel_lower_dragbrace.inertia_frame'
_GCMB_gel_lower_dragbrace_cm = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_lower_dragbrace_cm))
_GCMB_gel_lower_dragbrace = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_lower_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_26 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.gralin_26')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace')
gralin_26.relative_to = relative_to
gralin_26.marker_name = '.GCMB.gel_lower_dragbrace.gralin_26'
_GCMB_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_udb_atch_1')
gralin_26.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_ldb_udb_atch_1))
_GCMB_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_udb_atch_1').location
_GCMB_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_collar_atch_1').location
gralin_26.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_ldb_udb_atch_1, _GCMB_ground_hpl_ldb_collar_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_26.location, gralin_26.orientation)
gralin_26.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_26.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_14 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.jxl_joint_i_14')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace')
jxl_joint_i_14.relative_to = relative_to
jxl_joint_i_14.marker_name = '.GCMB.gel_lower_dragbrace.jxl_joint_i_14'
_GCMB_gel_upper_dragbrace_jxl_joint_j_14 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.jxl_joint_j_14')
jxl_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_dragbrace_jxl_joint_j_14))
_GCMB_gel_upper_dragbrace_jxl_joint_j_14 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_dragbrace.jxl_joint_j_14')
jxl_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_dragbrace_jxl_joint_j_14))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_14.location, jxl_joint_i_14.orientation)
jxl_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_10 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.jxl_joint_i_10')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace')
jxl_joint_i_10.relative_to = relative_to
jxl_joint_i_10.marker_name = '.GCMB.gel_lower_dragbrace.jxl_joint_i_10'
_GCMB_gel_uc_collar_jxl_joint_j_10 = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_j_10')
jxl_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_uc_collar_jxl_joint_j_10))
_GCMB_gel_uc_collar_jxl_joint_j_10 = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_j_10')
jxl_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_uc_collar_jxl_joint_j_10))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_10.location, jxl_joint_i_10.orientation)
jxl_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


graarm_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.graarm_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace')
graarm_1.relative_to = relative_to
graarm_1.marker_name = '.GCMB.gel_lower_dragbrace.graarm_1'
_GCMB_ground_hpl_uplock_tab = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uplock_tab')
graarm_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_uplock_tab))
_GCMB_ground_hpl_uplock_tab = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uplock_tab').global_loc
_GCMB_ground_cfl_ldb_geompt_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_ldb_geompt_1').global_loc
_GCMB_ground_cfl_ldb_geompt_2 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_ldb_geompt_2').location
graarm_1.orientation = (VecUtils.ORI_IN_PLANE(_GCMB_ground_hpl_uplock_tab, _GCMB_ground_cfl_ldb_geompt_1, _GCMB_ground_cfl_ldb_geompt_2, "X_XY"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_1.location, graarm_1.orientation)
graarm_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
graarm_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


graarm_2 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.graarm_2')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace')
graarm_2.relative_to = relative_to
graarm_2.marker_name = '.GCMB.gel_lower_dragbrace.graarm_2'
_GCMB_ground_cfl_ldb_geompt_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_ldb_geompt_1')
graarm_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfl_ldb_geompt_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_2.location, graarm_2.orientation)
graarm_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


graarm_3 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.graarm_3')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace')
graarm_3.relative_to = relative_to
graarm_3.marker_name = '.GCMB.gel_lower_dragbrace.graarm_3'
_GCMB_ground_cfl_ldb_geompt_2 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_ldb_geompt_2')
graarm_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfl_ldb_geompt_2))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_3.location, graarm_3.orientation)
graarm_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_lower_dragbrace = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_dragbrace.gralin_lower_dragbrace')
gralin_lower_dragbrace.cylinder_name = '.GCMB.gel_lower_dragbrace.gralin_lower_dragbrace'
_GCMB_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_udb_atch_1').location
_GCMB_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_collar_atch_1').location
gralin_lower_dragbrace.length = (VecUtils.DM(_GCMB_ground_hpl_ldb_udb_atch_1, _GCMB_ground_hpl_ldb_collar_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.gel_upper_torquearm.inertia_frame'
_GCMB_gel_upper_torquearm_cm = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_torquearm_cm))
_GCMB_gel_upper_torquearm = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_torquearm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_11 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.gralin_11')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm')
gralin_11.relative_to = relative_to
gralin_11.marker_name = '.GCMB.gel_upper_torquearm.gralin_11'
_GCMB_ground_hpl_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_collar_atch_1')
gralin_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_uta_collar_atch_1))
_GCMB_ground_hpl_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_collar_atch_1').location
_GCMB_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_1').location
gralin_11.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_uta_collar_atch_1, _GCMB_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_11.location, gralin_11.orientation)
gralin_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_2 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.jxl_joint_i_2')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm')
jxl_joint_i_2.relative_to = relative_to
jxl_joint_i_2.marker_name = '.GCMB.gel_upper_torquearm.jxl_joint_i_2'
_GCMB_gel_connector_jxl_joint_j_2 = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.jxl_joint_j_2')
jxl_joint_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_connector_jxl_joint_j_2))
_GCMB_gel_connector_jxl_joint_j_2 = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.jxl_joint_j_2')
jxl_joint_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_connector_jxl_joint_j_2))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_2.location, jxl_joint_i_2.orientation)
jxl_joint_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_3 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.jxl_joint_i_3')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm')
jxl_joint_i_3.relative_to = relative_to
jxl_joint_i_3.marker_name = '.GCMB.gel_upper_torquearm.jxl_joint_i_3'
_GCMB_gel_uc_collar_jxl_joint_j_3 = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_j_3')
jxl_joint_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_uc_collar_jxl_joint_j_3))
_GCMB_gel_uc_collar_jxl_joint_j_3 = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_j_3')
jxl_joint_i_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_uc_collar_jxl_joint_j_3))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_3.location, jxl_joint_i_3.orientation)
jxl_joint_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_upper_torquearm = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_torquearm.gralin_upper_torquearm')
gralin_upper_torquearm.cylinder_name = '.GCMB.gel_upper_torquearm.gralin_upper_torquearm'
_GCMB_ground_hpl_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_collar_atch_1').location
_GCMB_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_1').location
gralin_upper_torquearm.length = (VecUtils.DM(_GCMB_ground_hpl_uta_collar_atch_1, _GCMB_ground_hpl_uta_connect_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.gel_lower_torquearm.inertia_frame'
_GCMB_gel_lower_torquearm_cm = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_lower_torquearm_cm))
_GCMB_gel_lower_torquearm = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_lower_torquearm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_29 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.gralin_29')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm')
gralin_29.relative_to = relative_to
gralin_29.marker_name = '.GCMB.gel_lower_torquearm.gralin_29'
_GCMB_ground_hpl_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_lc_atch_1')
gralin_29.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_lta_lc_atch_1))
_GCMB_ground_hpl_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_lc_atch_1').location
_GCMB_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_connect_atch_1').location
gralin_29.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_lta_lc_atch_1, _GCMB_ground_hpl_lta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_29.location, gralin_29.orientation)
gralin_29.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_29.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_11 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.jxl_joint_i_11')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm')
jxl_joint_i_11.relative_to = relative_to
jxl_joint_i_11.marker_name = '.GCMB.gel_lower_torquearm.jxl_joint_i_11'
_GCMB_gel_lower_cylinder_jxl_joint_j_11 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.jxl_joint_j_11')
jxl_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_lower_cylinder_jxl_joint_j_11))
_GCMB_gel_lower_cylinder_jxl_joint_j_11 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_cylinder.jxl_joint_j_11')
jxl_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_lower_cylinder_jxl_joint_j_11))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_11.location, jxl_joint_i_11.orientation)
jxl_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.jxl_joint_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm')
jxl_joint_i_1.relative_to = relative_to
jxl_joint_i_1.marker_name = '.GCMB.gel_lower_torquearm.jxl_joint_i_1'
_GCMB_gel_connector_jxl_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.jxl_joint_j_1')
jxl_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_connector_jxl_joint_j_1))
_GCMB_gel_connector_jxl_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.jxl_joint_j_1')
jxl_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_connector_jxl_joint_j_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_1.location, jxl_joint_i_1.orientation)
jxl_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_lower_torquearm = Jusme.ActiveUSScene.getObject('.GCMB.gel_lower_torquearm.gralin_lower_torquearm')
gralin_lower_torquearm.cylinder_name = '.GCMB.gel_lower_torquearm.gralin_lower_torquearm'
_GCMB_ground_hpl_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_lc_atch_1').location
_GCMB_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_connect_atch_1').location
gralin_lower_torquearm.length = (VecUtils.DM(_GCMB_ground_hpl_lta_lc_atch_1, _GCMB_ground_hpl_lta_connect_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.gel_connector.inertia_frame'
_GCMB_gel_connector_cm = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_connector_cm))
_GCMB_gel_connector = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_connector))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_3 = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.gralin_3')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector')
gralin_3.relative_to = relative_to
gralin_3.marker_name = '.GCMB.gel_connector.gralin_3'
_GCMB_ground_hpl_connect_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_connect_1')
gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_connect_1))
_GCMB_ground_hpl_connect_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_connect_1').location
_GCMB_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_1').location
gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_connect_1, _GCMB_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.jxl_joint_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector')
jxl_joint_j_1.relative_to = relative_to
jxl_joint_j_1.marker_name = '.GCMB.gel_connector.jxl_joint_j_1'
_GCMB_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_connect_atch_1')
jxl_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_lta_connect_atch_1))
_GCMB_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_connect_atch_1').location
_GCMB_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_1').location
jxl_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_lta_connect_atch_1, _GCMB_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_1.location, jxl_joint_j_1.orientation)
jxl_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_2 = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.jxl_joint_j_2')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector')
jxl_joint_j_2.relative_to = relative_to
jxl_joint_j_2.marker_name = '.GCMB.gel_connector.jxl_joint_j_2'
_GCMB_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_1')
jxl_joint_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_uta_connect_atch_1))
_GCMB_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_1').location
_GCMB_ground_hpl_uta_connect_atch_2 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_2').location
jxl_joint_j_2.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_uta_connect_atch_1, _GCMB_ground_hpl_uta_connect_atch_2, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_2.location, jxl_joint_j_2.orientation)
jxl_joint_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_connector = Jusme.ActiveUSScene.getObject('.GCMB.gel_connector.gralin_connector')
gralin_connector.cylinder_name = '.GCMB.gel_connector.gralin_connector'
_GCMB_ground_hpl_connect_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_connect_1').location
_GCMB_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_1').location
gralin_connector.length = (VecUtils.DM(_GCMB_ground_hpl_connect_1, _GCMB_ground_hpl_uta_connect_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.gel_uc_collar.inertia_frame'
_GCMB_gel_uc_collar_cm = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_uc_collar_cm))
_GCMB_gel_uc_collar = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_uc_collar))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_5 = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.gralin_5')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar')
gralin_5.relative_to = relative_to
gralin_5.marker_name = '.GCMB.gel_uc_collar.gralin_5'
_GCMB_ground_cfl_collar_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_collar_top')
gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfl_collar_top))
_GCMB_ground_cfl_collar_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_collar_top').location
_GCMB_ground_cfl_collar_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_collar_bot').location
gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_cfl_collar_top, _GCMB_ground_cfl_collar_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_3 = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_j_3')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar')
jxl_joint_j_3.relative_to = relative_to
jxl_joint_j_3.marker_name = '.GCMB.gel_uc_collar.jxl_joint_j_3'
_GCMB_ground_hpl_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_collar_atch_1')
jxl_joint_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_uta_collar_atch_1))
_GCMB_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_lta_connect_atch_1').location
_GCMB_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_uta_connect_atch_1').location
jxl_joint_j_3.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_lta_connect_atch_1, _GCMB_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_3.location, jxl_joint_j_3.orientation)
jxl_joint_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_4 = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_i_4')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar')
jxl_joint_i_4.relative_to = relative_to
jxl_joint_i_4.marker_name = '.GCMB.gel_uc_collar.jxl_joint_i_4'
_GCMB_gel_upper_cylinder_jxl_joint_j_4 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.jxl_joint_j_4')
jxl_joint_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_cylinder_jxl_joint_j_4))
_GCMB_gel_upper_cylinder_jxl_joint_j_4 = Jusme.ActiveUSScene.getObject('.GCMB.gel_upper_cylinder.jxl_joint_j_4')
jxl_joint_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_gel_upper_cylinder_jxl_joint_j_4))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_4.location, jxl_joint_i_4.orientation)
jxl_joint_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_10 = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.jxl_joint_j_10')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar')
jxl_joint_j_10.relative_to = relative_to
jxl_joint_j_10.marker_name = '.GCMB.gel_uc_collar.jxl_joint_j_10'
_GCMB_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ldb_collar_atch_1')
jxl_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_ldb_collar_atch_1))
_GCMB_gel_uc_collar = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar')
_GCMB_ground_cfl_plane_ref_2 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_plane_ref_2').global_loc
jxl_joint_j_10.orientation = (ORI_LOCAL(ORI_ALIGN_AXIS(_GCMB_ground_cfl_plane_ref_2, "Z+Z"), _GCMB_gel_uc_collar))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_10.location, jxl_joint_j_10.orientation)
jxl_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_uc_collar = Jusme.ActiveUSScene.getObject('.GCMB.gel_uc_collar.gralin_uc_collar')
gralin_uc_collar.cylinder_name = '.GCMB.gel_uc_collar.gralin_uc_collar'
_GCMB_ground_cfl_collar_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_collar_top').location
_GCMB_ground_cfl_collar_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_collar_bot').location
gralin_uc_collar.length = (VecUtils.DM(_GCMB_ground_cfl_collar_top, _GCMB_ground_cfl_collar_bot))


MARKER_202 = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part.MARKER_202')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part')
MARKER_202.relative_to = relative_to
MARKER_202.marker_name = '.GCMB.luntai.wheel_part.MARKER_202'
_GCMB_ground_hpl_wheel_center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center')
MARKER_202.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_wheel_center))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_202.location, MARKER_202.orientation)
MARKER_202.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_209 = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part.MARKER_209')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part')
MARKER_209.relative_to = relative_to
MARKER_209.marker_name = '.GCMB.luntai.wheel_part.MARKER_209'
_GCMB_ground_hpl_wheel_center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center')
MARKER_209.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_wheel_center))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_209.location, MARKER_209.orientation)
MARKER_209.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_224 = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part.MARKER_224')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part')
MARKER_224.relative_to = relative_to
MARKER_224.marker_name = '.GCMB.luntai.wheel_part.MARKER_224'
_GCMB_ground_hpl_wheel_center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center')
MARKER_224.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_wheel_center))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_224.location, MARKER_224.orientation)
MARKER_224.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_225 = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part.MARKER_225')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part')
MARKER_225.relative_to = relative_to
MARKER_225.marker_name = '.GCMB.luntai.wheel_part.MARKER_225'
_GCMB_ground_hpl_wheel_center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center')
MARKER_225.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_wheel_center))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_225.location, MARKER_225.orientation)
MARKER_225.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gfo_i = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part.gfo_i')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part')
gfo_i.relative_to = relative_to
gfo_i.marker_name = '.GCMB.luntai.wheel_part.gfo_i'
_GCMB_luntai_wheel_part_wheel_cm = Jusme.ActiveUSScene.getObject('.GCMB.luntai.wheel_part.wheel_cm')
gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _GCMB_luntai_wheel_part_wheel_cm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


MARKER_199 = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_199')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang')
MARKER_199.relative_to = relative_to
MARKER_199.marker_name = '.GCMB.zhiliang.MARKER_199'
_GCMB_ground_POINT_48 = Jusme.ActiveUSScene.getObject('.GCMB.ground.POINT_48')
MARKER_199.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_POINT_48))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_199.location, MARKER_199.orientation)
MARKER_199.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ELLIPSOID_49 = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.ELLIPSOID_49')
ELLIPSOID_49.ellipsoid_name = '.GCMB.zhiliang.ELLIPSOID_49'


MARKER_229 = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_229')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang')
MARKER_229.relative_to = relative_to
MARKER_229.marker_name = '.GCMB.zhiliang.MARKER_229'
_GCMB_ground_POINT_48 = Jusme.ActiveUSScene.getObject('.GCMB.ground.POINT_48')
MARKER_229.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_POINT_48))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_229.location, MARKER_229.orientation)
MARKER_229.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_233 = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_233')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang')
MARKER_233.relative_to = relative_to
MARKER_233.marker_name = '.GCMB.zhiliang.MARKER_233'
_GCMB_ground_POINT_48 = Jusme.ActiveUSScene.getObject('.GCMB.ground.POINT_48')
MARKER_233.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_POINT_48))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_233.location, MARKER_233.orientation)
MARKER_233.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_239 = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang.MARKER_239')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.zhiliang')
MARKER_239.relative_to = relative_to
MARKER_239.marker_name = '.GCMB.zhiliang.MARKER_239'
_GCMB_ground_POINT_48 = Jusme.ActiveUSScene.getObject('.GCMB.ground.POINT_48')
MARKER_239.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_POINT_48))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_239.location, MARKER_239.orientation)
MARKER_239.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


steel = Jusme.ActiveUSScene.getObject('.GCMB.steel')
steel.material_name = '.GCMB.steel'



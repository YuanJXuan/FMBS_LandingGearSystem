import Jusme
from Jusme import Base
from Fmbs.import_all_node import MakeSceneNodeByType
import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils
UNITS_1 = MakeSceneNodeByType('DefaultsUnits', '.Unknown.UNITS_1')
UNITS_1.length_opt = 0
UNITS_1.length = 'mm'
UNITS_1.angle = 'deg'
UNITS_1.force = 'newton'
UNITS_1.mass = 'kg'
UNITS_1.time = 'sec'
UNITS_1.coordinate_system_type = 'cartesian'
UNITS_1.orientation_type = 'body313'
aluminum = MakeSceneNodeByType('MaterialCreate', '.Unknown.aluminum')
aluminum.material_name = '.Unknown.aluminum'
aluminum.adams_id = 2
aluminum.density = 0.00000274
aluminum.youngs_modulus = 71705.0
aluminum.poissons_ratio = 0.33
steel = MakeSceneNodeByType('MaterialCreate', '.Unknown.steel')
steel.material_name = '.Unknown.steel'
steel.adams_id = 5
steel.density = 0.000007801
steel.youngs_modulus = 207000.0
steel.poissons_ratio = 0.29
steel_2 = MakeSceneNodeByType('MaterialCreate', '.Unknown.steel_2')
steel_2.material_name = '.Unknown.steel_2'
steel_2.adams_id = 3
steel_2.density = 0.000007801
steel_2.youngs_modulus = 207000.0
steel_2.poissons_ratio = 0.29
aluminum_2 = MakeSceneNodeByType('MaterialCreate', '.Unknown.aluminum_2')
aluminum_2.material_name = '.Unknown.aluminum_2'
aluminum_2.adams_id = 4
aluminum_2.density = 0.00000274
aluminum_2.youngs_modulus = 71705.0
aluminum_2.poissons_ratio = 0.33
ground = Jusme.ActiveUSScene.getObject('.Unknown.ground')
ground.part_name = 'ground'
origo = MakeSceneNodeByType('Marker', '.Unknown.ground.origo')
origo.marker_name = '.Unknown.ground.origo'
origo.adams_id = 1
origo.location = Base.Vector (0.0, 0.0, 0.0)
origo.orientation = Base.Vector (0.0, 0.0, 0.0)
origo1 = MakeSceneNodeByType('Marker', '.Unknown.ground.origo1')
origo1.marker_name = '.Unknown.ground.origo1'
origo1.adams_id = 287
origo1.location = Base.Vector (0.0, 0.0, 0.0)
origo1.orientation = Base.Vector (0.0, 0.0, 0.0)
cfs_uc_sf_atch_mid = MakeSceneNodeByType('Marker', '.Unknown.ground.cfs_uc_sf_atch_mid')
cfs_uc_sf_atch_mid.marker_name = '.Unknown.ground.cfs_uc_sf_atch_mid'
cfs_uc_sf_atch_mid.adams_id = 289
cfs_uc_sf_atch_mid.location = Base.Vector (6314.44, 0.0, 1691.64)
cfs_uc_sf_atch_mid.orientation = Base.Vector (0.0, 90.0, 0.0)
cfs_subframe_to_body_point = MakeSceneNodeByType('Marker', '.Unknown.ground.cfs_subframe_to_body_point')
cfs_subframe_to_body_point.marker_name = '.Unknown.ground.cfs_subframe_to_body_point'
cfs_subframe_to_body_point.adams_id = 290
cfs_subframe_to_body_point.location = Base.Vector (6704.33, 0.0, 1668.78)
cfs_subframe_to_body_point.orientation = Base.Vector (0.0, 90.0, 356.6444799092)
cfl_spin_axis1 = MakeSceneNodeByType('Marker', '.Unknown.ground.cfl_spin_axis1')
cfl_spin_axis1.marker_name = '.Unknown.ground.cfl_spin_axis1'
cfl_spin_axis1.adams_id = 292
cfl_spin_axis1.location = Base.Vector (6229.096, -209.55, 308.0)
cfl_spin_axis1.orientation = Base.Vector (0.0, 90.0, 0.0)
cfr_spin_axis1 = MakeSceneNodeByType('Marker', '.Unknown.ground.cfr_spin_axis1')
cfr_spin_axis1.marker_name = '.Unknown.ground.cfr_spin_axis1'
cfr_spin_axis1.adams_id = 293
cfr_spin_axis1.location = Base.Vector (6229.096, 209.55, 308.0)
cfr_spin_axis1.orientation = Base.Vector (180.0, 90.0, 180.0)
cfs_wheel_centers_midpoint = MakeSceneNodeByType('Marker', '.Unknown.ground.cfs_wheel_centers_midpoint')
cfs_wheel_centers_midpoint.marker_name = '.Unknown.ground.cfs_wheel_centers_midpoint'
cfs_wheel_centers_midpoint.adams_id = 294
cfs_wheel_centers_midpoint.location = Base.Vector (6229.096, 0.0, 508.0)
cfs_wheel_centers_midpoint.orientation = Base.Vector (0.0, 0.0, 0.0)
cfs_nlg_axle_lowpoint = MakeSceneNodeByType('Marker', '.Unknown.ground.cfs_nlg_axle_lowpoint')
cfs_nlg_axle_lowpoint.marker_name = '.Unknown.ground.cfs_nlg_axle_lowpoint'
cfs_nlg_axle_lowpoint.adams_id = 295
cfs_nlg_axle_lowpoint.location = Base.Vector (6229.096, 0.0, 482.6)
cfs_nlg_axle_lowpoint.orientation = Base.Vector (0.0, 0.0, 0.0)
cfs_collar_top = MakeSceneNodeByType('Marker', '.Unknown.ground.cfs_collar_top')
cfs_collar_top.marker_name = '.Unknown.ground.cfs_collar_top'
cfs_collar_top.adams_id = 296
cfs_collar_top.location = Base.Vector (6197.6, 0.0, 856.996)
cfs_collar_top.orientation = Base.Vector (0.0, 0.0, 0.0)
hps_uc_sf_atch_l = MakeSceneNodeByType('Point', '.Unknown.ground.hps_uc_sf_atch_l')
hps_uc_sf_atch_l.point_name = '.Unknown.ground.hps_uc_sf_atch_l'
hps_uc_sf_atch_l.location = Base.Vector (6314.44, -340.36, 1691.64)
hps_uc_sf_atch_r = MakeSceneNodeByType('Point', '.Unknown.ground.hps_uc_sf_atch_r')
hps_uc_sf_atch_r.point_name = '.Unknown.ground.hps_uc_sf_atch_r'
hps_uc_sf_atch_r.location = Base.Vector (6314.44, 340.36, 1691.64)
hps_lc_bot = MakeSceneNodeByType('Point', '.Unknown.ground.hps_lc_bot')
hps_lc_bot.point_name = '.Unknown.ground.hps_lc_bot'
hps_lc_bot.location = Base.Vector (6197.6, 0.0, 308.0)
hps_uc_top = MakeSceneNodeByType('Point', '.Unknown.ground.hps_uc_top')
hps_uc_top.point_name = '.Unknown.ground.hps_uc_top'
hps_uc_top.location = Base.Vector (6197.6, 0.0, 1625.6)
hps_uta_uc_atch = MakeSceneNodeByType('Point', '.Unknown.ground.hps_uta_uc_atch')
hps_uta_uc_atch.point_name = '.Unknown.ground.hps_uta_uc_atch'
hps_uta_uc_atch.location = Base.Vector (6324.6, 0.0, 838.2)
hps_lta_lc_atch = MakeSceneNodeByType('Point', '.Unknown.ground.hps_lta_lc_atch')
hps_lta_lc_atch.point_name = '.Unknown.ground.hps_lta_lc_atch'
hps_lta_lc_atch.location = Base.Vector (6299.2, 0.0, 333.4)
hps_lta_uta_atch = MakeSceneNodeByType('Point', '.Unknown.ground.hps_lta_uta_atch')
hps_lta_uta_atch.point_name = '.Unknown.ground.hps_lta_uta_atch'
hps_lta_uta_atch.location = Base.Vector (6654.8, 0.0, 611.2)
hps_uc_geompt = MakeSceneNodeByType('Point', '.Unknown.ground.hps_uc_geompt')
hps_uc_geompt.point_name = '.Unknown.ground.hps_uc_geompt'
hps_uc_geompt.location = Base.Vector (6197.6, 0.0, 1473.2)
hps_uc_bot = MakeSceneNodeByType('Point', '.Unknown.ground.hps_uc_bot')
hps_uc_bot.point_name = '.Unknown.ground.hps_uc_bot'
hps_uc_bot.location = Base.Vector (6197.6, 0.0, 762.0)
hps_lc_top = MakeSceneNodeByType('Point', '.Unknown.ground.hps_lc_top')
hps_lc_top.point_name = '.Unknown.ground.hps_lc_top'
hps_lc_top.location = Base.Vector (6197.6, 0.0, 1197.0)
hps_origin_reference = MakeSceneNodeByType('Point', '.Unknown.ground.hps_origin_reference')
hps_origin_reference.point_name = '.Unknown.ground.hps_origin_reference'
hps_origin_reference.location = Base.Vector (0.0, 0.0, 0.0)
hps_lb_uc_atch = MakeSceneNodeByType('Point', '.Unknown.ground.hps_lb_uc_atch')
hps_lb_uc_atch.point_name = '.Unknown.ground.hps_lb_uc_atch'
hps_lb_uc_atch.location = Base.Vector (6021.578, 0.0, 795.02)
hpl_wheel_center1 = MakeSceneNodeByType('Point', '.Unknown.ground.hpl_wheel_center1')
hpl_wheel_center1.point_name = '.Unknown.ground.hpl_wheel_center1'
hpl_wheel_center1.location = Base.Vector (6229.096, -209.55, 308.0)
hpr_wheel_center1 = MakeSceneNodeByType('Point', '.Unknown.ground.hpr_wheel_center1')
hpr_wheel_center1.point_name = '.Unknown.ground.hpr_wheel_center1'
hpr_wheel_center1.location = Base.Vector (6229.096, 209.55, 308.0)
hpl_ob_axle1 = MakeSceneNodeByType('Point', '.Unknown.ground.hpl_ob_axle1')
hpl_ob_axle1.point_name = '.Unknown.ground.hpl_ob_axle1'
hpl_ob_axle1.location = Base.Vector (6229.096, -285.75, 308.0)
hpr_ob_axle1 = MakeSceneNodeByType('Point', '.Unknown.ground.hpr_ob_axle1')
hpr_ob_axle1.point_name = '.Unknown.ground.hpr_ob_axle1'
hpr_ob_axle1.location = Base.Vector (6229.096, 285.75, 308.0)
hps_nlg_axle_lowpoint = MakeSceneNodeByType('Point', '.Unknown.ground.hps_nlg_axle_lowpoint')
hps_nlg_axle_lowpoint.point_name = '.Unknown.ground.hps_nlg_axle_lowpoint'
hps_nlg_axle_lowpoint.location = Base.Vector (6229.096, 0.0, 482.6)
hsg_1 = MakeSceneNodeByType('Point', '.Unknown.ground.hsg_1')
hsg_1.point_name = '.Unknown.ground.hsg_1'
hsg_1.location = Base.Vector (6197.6, 200.0, 800.0)
hsg_2 = MakeSceneNodeByType('Point', '.Unknown.ground.hsg_2')
hsg_2.point_name = '.Unknown.ground.hsg_2'
hsg_2.location = Base.Vector (5732.8083759, -112.3599625, 800.0)
ges_upper_cylinder = MakeSceneNodeByType('PartGeneral', '.Unknown.ges_upper_cylinder')
ges_upper_cylinder.part_name = '.Unknown.ges_upper_cylinder'
ges_upper_cylinder.adams_id = 34
ges_upper_cylinder.location = Base.Vector (6197.6, 0.0, 1193.8)
ges_upper_cylinder.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_481 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.MARKER_481')
MARKER_481.marker_name = '.Unknown.ges_upper_cylinder.MARKER_481'
MARKER_481.adams_id = 481
MARKER_481.location = Base.Vector (0.0, 0.0, 384.302)
MARKER_481.orientation = Base.Vector (180.0, 180.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.cm')
cm.marker_name = '.Unknown.ges_upper_cylinder.cm'
cm.adams_id = 306
cm.location = Base.Vector (-3.3167643494, 0.0, -13.382423116)
cm.orientation = Base.Vector (90.0, 2.0673379194, 270.0)
inertia_frame = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.inertia_frame')
inertia_frame.marker_name = '.Unknown.ges_upper_cylinder.inertia_frame'
inertia_frame.adams_id = 307
inertia_frame.location = Base.Vector (-3.3167643494, 0.0, -13.382423116)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_2 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.gralin_2')
gralin_2.marker_name = '.Unknown.ges_upper_cylinder.gralin_2'
gralin_2.adams_id = 308
gralin_2.location = Base.Vector (0.0, 0.0, -431.8)
gralin_2.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_3 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.gralin_3')
gralin_3.marker_name = '.Unknown.ges_upper_cylinder.gralin_3'
gralin_3.adams_id = 309
gralin_3.location = Base.Vector (-116.84, -340.36, -497.84)
gralin_3.orientation = Base.Vector (161.0534953105, 58.7414044414, 213.4869581747)
gralin_4 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.gralin_4')
gralin_4.marker_name = '.Unknown.ges_upper_cylinder.gralin_4'
gralin_4.adams_id = 310
gralin_4.location = Base.Vector (-116.84, 340.36, -497.84)
gralin_4.orientation = Base.Vector (18.9465046895, 58.7414044414, 326.5130418253)
jxs_joint_j_11 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.jxs_joint_j_11')
jxs_joint_j_11.marker_name = '.Unknown.ges_upper_cylinder.jxs_joint_j_11'
jxs_joint_j_11.adams_id = 311
jxs_joint_j_11.location = Base.Vector (0.0, 0.0, 114.3)
jxs_joint_j_11.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_spring_j_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.ues_spring_j_1')
ues_spring_j_1.marker_name = '.Unknown.ges_upper_cylinder.ues_spring_j_1'
ues_spring_j_1.adams_id = 314
ues_spring_j_1.location = Base.Vector (0.0, 0.0, -431.8)
ues_spring_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_damper_j_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.ues_damper_j_1')
ues_damper_j_1.marker_name = '.Unknown.ges_upper_cylinder.ues_damper_j_1'
ues_damper_j_1.adams_id = 315
ues_damper_j_1.location = Base.Vector (0.0, 0.0, -431.8)
ues_damper_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_stopper_j_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.ues_stopper_j_1')
ues_stopper_j_1.marker_name = '.Unknown.ges_upper_cylinder.ues_stopper_j_1'
ues_stopper_j_1.adams_id = 316
ues_stopper_j_1.location = Base.Vector (0.0, 0.0, -431.8)
ues_stopper_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_j_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.jxs_joint_j_1')
jxs_joint_j_1.marker_name = '.Unknown.ges_upper_cylinder.jxs_joint_j_1'
jxs_joint_j_1.adams_id = 317
jxs_joint_j_1.location = Base.Vector (0.0, 0.0, 336.804)
jxs_joint_j_1.orientation = Base.Vector (180.0, 180.0, 0.0)
ues_actuator_j_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.ues_actuator_j_1')
ues_actuator_j_1.marker_name = '.Unknown.ges_upper_cylinder.ues_actuator_j_1'
ues_actuator_j_1.adams_id = 318
ues_actuator_j_1.location = Base.Vector (0.0, 0.0, 336.804)
ues_actuator_j_1.orientation = Base.Vector (180.0, 180.0, 0.0)
ues_actuator_j_4 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.ues_actuator_j_4')
ues_actuator_j_4.marker_name = '.Unknown.ges_upper_cylinder.ues_actuator_j_4'
ues_actuator_j_4.adams_id = 319
ues_actuator_j_4.location = Base.Vector (0.0, 0.0, 336.804)
ues_actuator_j_4.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_2 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.MARKER_2')
MARKER_2.marker_name = '.Unknown.ges_upper_cylinder.MARKER_2'
MARKER_2.adams_id = 2
MARKER_2.location = Base.Vector (0.0, 0.0, -431.8)
MARKER_2.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_116 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_cylinder.MARKER_116')
MARKER_116.marker_name = '.Unknown.ges_upper_cylinder.MARKER_116'
MARKER_116.adams_id = 324
MARKER_116.location = Base.Vector (0.0, 0.0, -431.8)
MARKER_116.orientation = Base.Vector (180.0, 180.0, 0.0)
ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.cm')
ges_upper_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.inertia_frame')
ges_upper_cylinder.inertia_marker = inertia_marker
ges_upper_cylinder.part_name = '.Unknown.ges_upper_cylinder'
ges_upper_cylinder.mass = 82.2524279101
ges_upper_cylinder.ixx = 2775904.0478
ges_upper_cylinder.iyy = 2616359.1859
ges_upper_cylinder.izz = 827290.4746
ges_upper_cylinder.ixy = 0.0
ges_upper_cylinder.izx = 70431.892224
ges_upper_cylinder.iyz = 0.0
gralin_upper_cylinder_geom1 = MakeSceneNodeByType('ShapeCylinder', '.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom1')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.gralin_2')
gralin_upper_cylinder_geom1.center_marker = center_marker
gralin_upper_cylinder_geom1.cylinder_name = '.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom1'
gralin_upper_cylinder_geom1.adams_id = 86
gralin_upper_cylinder_geom1.angle_extent = 360.0
gralin_upper_cylinder_geom1.length = 863.6
gralin_upper_cylinder_geom1.radius = 127.0
gralin_upper_cylinder_geom1.side_count_for_body = 15
gralin_upper_cylinder_geom1.segment_count_for_ends = 15


gralin_upper_cylinder_geom2 = MakeSceneNodeByType('ShapeCylinder', '.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom2')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.gralin_3')
gralin_upper_cylinder_geom2.center_marker = center_marker
gralin_upper_cylinder_geom2.cylinder_name = '.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom2'
gralin_upper_cylinder_geom2.adams_id = 87
gralin_upper_cylinder_geom2.angle_extent = 360.0
gralin_upper_cylinder_geom2.length = 420.9662086
gralin_upper_cylinder_geom2.radius = 25.4
gralin_upper_cylinder_geom2.side_count_for_body = 15
gralin_upper_cylinder_geom2.segment_count_for_ends = 15


gralin_upper_cylinder_geom3 = MakeSceneNodeByType('ShapeCylinder', '.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom3')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.gralin_4')
gralin_upper_cylinder_geom3.center_marker = center_marker
gralin_upper_cylinder_geom3.cylinder_name = '.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom3'
gralin_upper_cylinder_geom3.adams_id = 88
gralin_upper_cylinder_geom3.angle_extent = 360.0
gralin_upper_cylinder_geom3.length = 420.9662086
gralin_upper_cylinder_geom3.radius = 25.4
gralin_upper_cylinder_geom3.side_count_for_body = 15
gralin_upper_cylinder_geom3.segment_count_for_ends = 15


ges_lower_cylinder = MakeSceneNodeByType('PartGeneral', '.Unknown.ges_lower_cylinder')
ges_lower_cylinder.part_name = '.Unknown.ges_lower_cylinder'
ges_lower_cylinder.adams_id = 35
ges_lower_cylinder.location = Base.Vector (6197.6, 0.0, 952.5)
ges_lower_cylinder.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_378 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.MARKER_378')
MARKER_378.marker_name = '.Unknown.ges_lower_cylinder.MARKER_378'
MARKER_378.adams_id = 378
MARKER_378.location = Base.Vector (-101.6, 0.0, 619.1)
MARKER_378.orientation = Base.Vector (0.0, 90.0, 180.0)
MARKER_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.MARKER_1')
MARKER_1.marker_name = '.Unknown.ges_lower_cylinder.MARKER_1'
MARKER_1.adams_id = 325
MARKER_1.location = Base.Vector (0.0, 0.0, -244.5)
MARKER_1.orientation = Base.Vector (180.0, 180.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.cm')
cm.marker_name = '.Unknown.ges_lower_cylinder.cm'
cm.adams_id = 326
cm.location = Base.Vector (-2.4871874502, 0.0, 34.740392449)
cm.orientation = Base.Vector (270.0, 0.8125241803, 90.0)
inertia_frame = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.inertia_frame')
inertia_frame.marker_name = '.Unknown.ges_lower_cylinder.inertia_frame'
inertia_frame.adams_id = 327
inertia_frame.location = Base.Vector (-2.4871874502, 0.0, 34.740392449)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_5 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.gralin_5')
gralin_5.marker_name = '.Unknown.ges_lower_cylinder.gralin_5'
gralin_5.adams_id = 328
gralin_5.location = Base.Vector (0.0, 0.0, -244.5)
gralin_5.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_i_11 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.jxs_joint_i_11')
jxs_joint_i_11.marker_name = '.Unknown.ges_lower_cylinder.jxs_joint_i_11'
jxs_joint_i_11.adams_id = 330
jxs_joint_i_11.location = Base.Vector (0.0, 0.0, -127.0)
jxs_joint_i_11.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_7 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.gralin_7')
gralin_7.marker_name = '.Unknown.ges_lower_cylinder.gralin_7'
gralin_7.adams_id = 331
gralin_7.location = Base.Vector (-31.496, 209.55, 644.5)
gralin_7.orientation = Base.Vector (0.0, 90.0, 0.0)
ues_spring_i_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.ues_spring_i_1')
ues_spring_i_1.marker_name = '.Unknown.ges_lower_cylinder.ues_spring_i_1'
ues_spring_i_1.adams_id = 332
ues_spring_i_1.location = Base.Vector (0.0, 0.0, -244.5)
ues_spring_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_damper_i_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.ues_damper_i_1')
ues_damper_i_1.marker_name = '.Unknown.ges_lower_cylinder.ues_damper_i_1'
ues_damper_i_1.adams_id = 51
ues_damper_i_1.location = Base.Vector (0.0, 0.0, -244.5)
ues_damper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_stopper_i_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.ues_stopper_i_1')
ues_stopper_i_1.marker_name = '.Unknown.ges_lower_cylinder.ues_stopper_i_1'
ues_stopper_i_1.adams_id = 333
ues_stopper_i_1.location = Base.Vector (0.0, 0.0, -244.5)
ues_stopper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
coomarker_2 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.coomarker_2')
coomarker_2.marker_name = '.Unknown.ges_lower_cylinder.coomarker_2'
coomarker_2.adams_id = 334
coomarker_2.location = Base.Vector (-31.496, 0.0, 444.5)
coomarker_2.orientation = Base.Vector (180.0, 180.0, 0.0)
coomarker_3 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.coomarker_3')
coomarker_3.marker_name = '.Unknown.ges_lower_cylinder.coomarker_3'
coomarker_3.adams_id = 335
coomarker_3.location = Base.Vector (-31.496, 0.0, 469.9)
coomarker_3.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_3 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.MARKER_3')
MARKER_3.marker_name = '.Unknown.ges_lower_cylinder.MARKER_3'
MARKER_3.adams_id = 336
MARKER_3.location = Base.Vector (-31.496, -209.55, 644.5)
MARKER_3.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_4 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.MARKER_4')
MARKER_4.marker_name = '.Unknown.ges_lower_cylinder.MARKER_4'
MARKER_4.adams_id = 337
MARKER_4.location = Base.Vector (-31.496, 209.55, 644.5)
MARKER_4.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_115 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_cylinder.MARKER_115')
MARKER_115.marker_name = '.Unknown.ges_lower_cylinder.MARKER_115'
MARKER_115.adams_id = 344
MARKER_115.location = Base.Vector (0.0, 0.0, -444.5)
MARKER_115.orientation = Base.Vector (180.0, 180.0, 0.0)
ges_lower_cylinder = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.cm')
ges_lower_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.inertia_frame')
ges_lower_cylinder.inertia_marker = inertia_marker
ges_lower_cylinder.part_name = '.Unknown.ges_lower_cylinder'
ges_lower_cylinder.mass = 84.8838172052
ges_lower_cylinder.ixx = 6834235.5549
ges_lower_cylinder.iyy = 6449459.8026
ges_lower_cylinder.izz = 803650.6432
ges_lower_cylinder.ixy = 0.0
ges_lower_cylinder.izx = -85544.003848
ges_lower_cylinder.iyz = 0.0
gralin_geom1 = MakeSceneNodeByType('ShapeCylinder', '.Unknown.ges_lower_cylinder.gralin_geom1')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.gralin_5')
gralin_geom1.center_marker = center_marker
gralin_geom1.cylinder_name = '.Unknown.ges_lower_cylinder.gralin_geom1'
gralin_geom1.adams_id = 89
gralin_geom1.angle_extent = 360.0
gralin_geom1.length = 889.0
gralin_geom1.radius = 101.6
gralin_geom1.side_count_for_body = 15
gralin_geom1.segment_count_for_ends = 15


gralin_geom2 = MakeSceneNodeByType('ShapeCylinder', '.Unknown.ges_lower_cylinder.gralin_geom2')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.gralin_7')
gralin_geom2.center_marker = center_marker
gralin_geom2.cylinder_name = '.Unknown.ges_lower_cylinder.gralin_geom2'
gralin_geom2.adams_id = 90
gralin_geom2.angle_extent = 360.0
gralin_geom2.length = 419.1
gralin_geom2.radius = 30.48
gralin_geom2.side_count_for_body = 15
gralin_geom2.segment_count_for_ends = 15


ges_upper_torque_arm = MakeSceneNodeByType('PartGeneral', '.Unknown.ges_upper_torque_arm')
ges_upper_torque_arm.part_name = '.Unknown.ges_upper_torque_arm'
ges_upper_torque_arm.adams_id = 36
ges_upper_torque_arm.location = Base.Vector (6489.7, 0.0, 774.7)
ges_upper_torque_arm.orientation = Base.Vector (90.0, 111.0375110254, 270.0)
cm = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_torque_arm.cm')
cm.marker_name = '.Unknown.ges_upper_torque_arm.cm'
cm.adams_id = 345
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_torque_arm.inertia_frame')
inertia_frame.marker_name = '.Unknown.ges_upper_torque_arm.inertia_frame'
inertia_frame.adams_id = 346
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_9 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_torque_arm.gralin_9')
gralin_9.marker_name = '.Unknown.ges_upper_torque_arm.gralin_9'
gralin_9.adams_id = 347
gralin_9.location = Base.Vector (0.0, 0.0, -176.8905311)
gralin_9.orientation = Base.Vector (90.0, 13.4695391009, 270.0)
jxs_joint_j_8 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_torque_arm.jxs_joint_j_8')
jxs_joint_j_8.marker_name = '.Unknown.ges_upper_torque_arm.jxs_joint_j_8'
jxs_joint_j_8.adams_id = 348
jxs_joint_j_8.location = Base.Vector (93.33456062, 0.0, 212.7884391)
jxs_joint_j_8.orientation = Base.Vector (0.0, 90.0, 111.0375110254)
jxs_joint_i_10 = MakeSceneNodeByType('Marker', '.Unknown.ges_upper_torque_arm.jxs_joint_i_10')
jxs_joint_i_10.marker_name = '.Unknown.ges_upper_torque_arm.jxs_joint_i_10'
jxs_joint_i_10.adams_id = 349
jxs_joint_i_10.location = Base.Vector (0.0, 0.0, -176.8905311)
jxs_joint_i_10.orientation = Base.Vector (0.0, 90.0, 111.0375110254)
ges_upper_torque_arm = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.cm')
ges_upper_torque_arm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.inertia_frame')
ges_upper_torque_arm.inertia_marker = inertia_marker
ges_upper_torque_arm.part_name = '.Unknown.ges_upper_torque_arm'
ges_upper_torque_arm.mass = 0.3898630024
ges_upper_torque_arm.ixx = 2577.4839559
ges_upper_torque_arm.iyy = 2577.4839559
ges_upper_torque_arm.izz = 31.440501824
ges_upper_torque_arm.ixy = 0.0
ges_upper_torque_arm.izx = 0.0
ges_upper_torque_arm.iyz = 0.0
gralin_upper_torque_arm_geom = MakeSceneNodeByType('ShapeCylinder', '.Unknown.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.gralin_9')
gralin_upper_torque_arm_geom.center_marker = center_marker
gralin_upper_torque_arm_geom.cylinder_name = '.Unknown.ges_upper_torque_arm.gralin_upper_torque_arm_geom'
gralin_upper_torque_arm_geom.adams_id = 91
gralin_upper_torque_arm_geom.angle_extent = 360.0
gralin_upper_torque_arm_geom.length = 400.7006863
gralin_upper_torque_arm_geom.radius = 12.7
gralin_upper_torque_arm_geom.side_count_for_body = 15
gralin_upper_torque_arm_geom.segment_count_for_ends = 15


ges_lower_torque_arm = MakeSceneNodeByType('PartGeneral', '.Unknown.ges_lower_torque_arm')
ges_lower_torque_arm.part_name = '.Unknown.ges_lower_torque_arm'
ges_lower_torque_arm.adams_id = 37
ges_lower_torque_arm.location = Base.Vector (6477.0, 0.0, 622.3)
ges_lower_torque_arm.orientation = Base.Vector (90.0, 63.4349488229, 270.0)
MARKER_379 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_torque_arm.MARKER_379')
MARKER_379.marker_name = '.Unknown.ges_lower_torque_arm.MARKER_379'
MARKER_379.adams_id = 379
MARKER_379.location = Base.Vector (178.8854382, 0.0, -288.2291623)
MARKER_379.orientation = Base.Vector (0.0, 90.0, 63.4349488229)
cm = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_torque_arm.cm')
cm.marker_name = '.Unknown.ges_lower_torque_arm.cm'
cm.adams_id = 350
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_torque_arm.inertia_frame')
inertia_frame.marker_name = '.Unknown.ges_lower_torque_arm.inertia_frame'
inertia_frame.adams_id = 351
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_i_8 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_torque_arm.jxs_joint_i_8')
jxs_joint_i_8.marker_name = '.Unknown.ges_lower_torque_arm.jxs_joint_i_8'
jxs_joint_i_8.adams_id = 352
jxs_joint_i_8.location = Base.Vector (89.4427191, 0.0, 154.0650836)
jxs_joint_i_8.orientation = Base.Vector (0.0, 90.0, 63.4349488229)
gralin_10 = MakeSceneNodeByType('Marker', '.Unknown.ges_lower_torque_arm.gralin_10')
gralin_10.marker_name = '.Unknown.ges_lower_torque_arm.gralin_10'
gralin_10.adams_id = 353
gralin_10.location = Base.Vector (178.8854382, 0.0, -288.2291623)
gralin_10.orientation = Base.Vector (270.0, 11.4324305526, 90.0)
ges_lower_torque_arm = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.cm')
ges_lower_torque_arm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.inertia_frame')
ges_lower_torque_arm.inertia_marker = inertia_marker
ges_lower_torque_arm.part_name = '.Unknown.ges_lower_torque_arm'
ges_lower_torque_arm.mass = 0.3898630024
ges_lower_torque_arm.ixx = 2577.4839559
ges_lower_torque_arm.iyy = 2577.4839559
ges_lower_torque_arm.izz = 31.440501824
ges_lower_torque_arm.ixy = 0.0
ges_lower_torque_arm.izx = 0.0
ges_lower_torque_arm.iyz = 0.0
gralin_lower_torque_arm_geom = MakeSceneNodeByType('ShapeCylinder', '.Unknown.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.gralin_10')
gralin_lower_torque_arm_geom.center_marker = center_marker
gralin_lower_torque_arm_geom.cylinder_name = '.Unknown.ges_lower_torque_arm.gralin_lower_torque_arm_geom'
gralin_lower_torque_arm_geom.adams_id = 92
gralin_lower_torque_arm_geom.angle_extent = 360.0
gralin_lower_torque_arm_geom.length = 451.2473823
gralin_lower_torque_arm_geom.radius = 12.7
gralin_lower_torque_arm_geom.side_count_for_body = 15
gralin_lower_torque_arm_geom.segment_count_for_ends = 15


ges_collar = MakeSceneNodeByType('PartGeneral', '.Unknown.ges_collar')
ges_collar.part_name = '.Unknown.ges_collar'
ges_collar.adams_id = 40
ges_collar.location = Base.Vector (6197.6, 0.0, 809.498)
ges_collar.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_482 = MakeSceneNodeByType('Marker', '.Unknown.ges_collar.MARKER_482')
MARKER_482.marker_name = '.Unknown.ges_collar.MARKER_482'
MARKER_482.adams_id = 482
MARKER_482.location = Base.Vector (0.0, 0.0, 0.0)
MARKER_482.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_j_10 = MakeSceneNodeByType('Marker', '.Unknown.ges_collar.jxs_joint_j_10')
jxs_joint_j_10.marker_name = '.Unknown.ges_collar.jxs_joint_j_10'
jxs_joint_j_10.adams_id = 368
jxs_joint_j_10.location = Base.Vector (127.0, 0.0, 28.702)
jxs_joint_j_10.orientation = Base.Vector (0.0, 90.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.Unknown.ges_collar.cm')
cm.marker_name = '.Unknown.ges_collar.cm'
cm.adams_id = 369
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.Unknown.ges_collar.inertia_frame')
inertia_frame.marker_name = '.Unknown.ges_collar.inertia_frame'
inertia_frame.adams_id = 370
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_24 = MakeSceneNodeByType('Marker', '.Unknown.ges_collar.gralin_24')
gralin_24.marker_name = '.Unknown.ges_collar.gralin_24'
gralin_24.adams_id = 371
gralin_24.location = Base.Vector (0.0, 0.0, -47.498)
gralin_24.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_i_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_collar.jxs_joint_i_1')
jxs_joint_i_1.marker_name = '.Unknown.ges_collar.jxs_joint_i_1'
jxs_joint_i_1.adams_id = 372
jxs_joint_i_1.location = Base.Vector (0.0, 0.0, 47.498)
jxs_joint_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_actuator_i_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_collar.ues_actuator_i_1')
ues_actuator_i_1.marker_name = '.Unknown.ges_collar.ues_actuator_i_1'
ues_actuator_i_1.adams_id = 373
ues_actuator_i_1.location = Base.Vector (0.0, 0.0, 47.498)
ues_actuator_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_actuator_i_4 = MakeSceneNodeByType('Marker', '.Unknown.ges_collar.ues_actuator_i_4')
ues_actuator_i_4.marker_name = '.Unknown.ges_collar.ues_actuator_i_4'
ues_actuator_i_4.adams_id = 374
ues_actuator_i_4.location = Base.Vector (0.0, 0.0, 47.498)
ues_actuator_i_4.orientation = Base.Vector (0.0, 0.0, 0.0)
ges_collar = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.cm')
ges_collar.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.inertia_frame')
ges_collar.inertia_marker = inertia_marker
ges_collar.part_name = '.Unknown.ges_collar'
ges_collar.mass = 6.4242828175
ges_collar.ixx = 85080.541407
ges_collar.iyy = 85080.541407
ges_collar.izz = 146854.2831
ges_collar.ixy = 0.0
ges_collar.izx = 0.0
ges_collar.iyz = 0.0
gralin_collar = MakeSceneNodeByType('ShapeCylinder', '.Unknown.ges_collar.gralin_collar')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.gralin_24')
gralin_collar.center_marker = center_marker
gralin_collar.cylinder_name = '.Unknown.ges_collar.gralin_collar'
gralin_collar.adams_id = 93
gralin_collar.angle_extent = 360.0
gralin_collar.length = 94.996
gralin_collar.radius = 139.7
gralin_collar.side_count_for_body = 15
gralin_collar.segment_count_for_ends = 15


JOINT_51 = MakeSceneNodeByType('JointRevolute', '.Unknown.JOINT_51')
i_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.MARKER_378')
JOINT_51.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.MARKER_379')
JOINT_51.j_marker_name = j_marker_name
JOINT_51.joint_name = '.Unknown.JOINT_51'
JOINT_51.adams_id = 51


josrev_lta_uta_joint = MakeSceneNodeByType('JointSpherical', '.Unknown.josrev_lta_uta_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.jxs_joint_i_8')
josrev_lta_uta_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.jxs_joint_j_8')
josrev_lta_uta_joint.j_marker_name = j_marker_name
josrev_lta_uta_joint.joint_name = '.Unknown.josrev_lta_uta_joint'
josrev_lta_uta_joint.adams_id = 39


josrev_uta_uc_joint = MakeSceneNodeByType('JointRevolute', '.Unknown.josrev_uta_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.jxs_joint_i_10')
josrev_uta_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_j_10')
josrev_uta_uc_joint.j_marker_name = j_marker_name
josrev_uta_uc_joint.joint_name = '.Unknown.josrev_uta_uc_joint'
josrev_uta_uc_joint.adams_id = 41


joscyl_lc_uc_joint = MakeSceneNodeByType('JointCylinder', '.Unknown.joscyl_lc_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.jxs_joint_i_11')
joscyl_lc_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_11')
joscyl_lc_uc_joint.j_marker_name = j_marker_name
joscyl_lc_uc_joint.joint_name = '.Unknown.joscyl_lc_uc_joint'
joscyl_lc_uc_joint.adams_id = 42


josrev_collar_uc_joint = MakeSceneNodeByType('JointRevolute', '.Unknown.josrev_collar_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_i_1')
josrev_collar_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_1')
josrev_collar_uc_joint.j_marker_name = j_marker_name
josrev_collar_uc_joint.joint_name = '.Unknown.josrev_collar_uc_joint'
josrev_collar_uc_joint.adams_id = 48


cfl_spin_axis1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfl_spin_axis1')
cfl_spin_axis1.marker_name = '.Unknown.ground.cfl_spin_axis1'
_turn_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpl_wheel_center1')
cfl_spin_axis1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_wheel_center1))
_turn_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpl_wheel_center1').location
_turn_ground_hpl_ob_axle1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpl_ob_axle1').location
cfl_spin_axis1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_wheel_center1, _turn_ground_hpl_ob_axle1, "Z"))


cfr_spin_axis1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfr_spin_axis1')
cfr_spin_axis1.marker_name = '.Unknown.ground.cfr_spin_axis1'
_turn_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpr_wheel_center1')
cfr_spin_axis1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_wheel_center1))
_turn_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpr_wheel_center1').location
_turn_ground_hpr_ob_axle1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpr_ob_axle1').location
cfr_spin_axis1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_wheel_center1, _turn_ground_hpr_ob_axle1, "Z"))


cfs_nlg_axle_lowpoint = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfs_nlg_axle_lowpoint')
cfs_nlg_axle_lowpoint.marker_name = '.Unknown.ground.cfs_nlg_axle_lowpoint'
_turn_ground_hps_nlg_axle_lowpoint = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_nlg_axle_lowpoint')
cfs_nlg_axle_lowpoint.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_nlg_axle_lowpoint))
_turn_ground_origo1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.origo1')
cfs_nlg_axle_lowpoint.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo1))


cfs_collar_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfs_collar_top')
cfs_collar_top.marker_name = '.Unknown.ground.cfs_collar_top'
_turn_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_bot').location
_turn_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_top').location
cfs_collar_top.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hps_uc_bot, _turn_ground_hps_uc_top, 0.11 * VecUtils.DM(_turn_ground_hps_uc_bot, _turn_ground_hps_uc_top)))
_turn_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_bot').location
_turn_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_top').location
cfs_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_uc_bot, _turn_ground_hps_uc_top, "Z"))


aluminum = Jusme.ActiveUSScene.getObject('.Unknown.aluminum')
aluminum.material_name = '.Unknown.aluminum'


steel = Jusme.ActiveUSScene.getObject('.Unknown.steel')
steel.material_name = '.Unknown.steel'


steel_2 = Jusme.ActiveUSScene.getObject('.Unknown.steel_2')
steel_2.material_name = '.Unknown.steel_2'


aluminum_2 = Jusme.ActiveUSScene.getObject('.Unknown.aluminum_2')
aluminum_2.material_name = '.Unknown.aluminum_2'


inertia_frame = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.Unknown.ges_upper_cylinder.inertia_frame'
_turn_ges_upper_cylinder_cm = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder_cm))
_turn_ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_2 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.gralin_2')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
gralin_2.relative_to = relative_to
gralin_2.marker_name = '.Unknown.ges_upper_cylinder.gralin_2'
_turn_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_top')
gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_uc_top))
_turn_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_top').location
_turn_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_bot').location
gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_uc_top, _turn_ground_hps_uc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_2.location, gralin_2.orientation)
gralin_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_3 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.gralin_3')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
gralin_3.relative_to = relative_to
gralin_3.marker_name = '.Unknown.ges_upper_cylinder.gralin_3'
_turn_ground_hps_uc_sf_atch_l = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_sf_atch_l')
gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_uc_sf_atch_l))
_turn_ground_hps_uc_sf_atch_l = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_sf_atch_l').location
_turn_ground_hps_uc_geompt = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_geompt').location
gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_uc_sf_atch_l, _turn_ground_hps_uc_geompt, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_4 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.gralin_4')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
gralin_4.relative_to = relative_to
gralin_4.marker_name = '.Unknown.ges_upper_cylinder.gralin_4'
_turn_ground_hps_uc_sf_atch_r = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_sf_atch_r')
gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_uc_sf_atch_r))
_turn_ground_hps_uc_sf_atch_r = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_sf_atch_r').location
_turn_ground_hps_uc_geompt = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_geompt').location
gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_uc_sf_atch_r, _turn_ground_hps_uc_geompt, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_spring_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.ues_spring_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
ues_spring_j_1.relative_to = relative_to
ues_spring_j_1.marker_name = '.Unknown.ges_upper_cylinder.ues_spring_j_1'
_turn_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_top')
ues_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_j_1.location, ues_spring_j_1.orientation)
ues_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ues_damper_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.ues_damper_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
ues_damper_j_1.relative_to = relative_to
ues_damper_j_1.marker_name = '.Unknown.ges_upper_cylinder.ues_damper_j_1'
_turn_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_top')
ues_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_j_1.location, ues_damper_j_1.orientation)
ues_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ues_stopper_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.ues_stopper_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
ues_stopper_j_1.relative_to = relative_to
ues_stopper_j_1.marker_name = '.Unknown.ges_upper_cylinder.ues_stopper_j_1'
_turn_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_top')
ues_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_j_1.location, ues_stopper_j_1.orientation)
ues_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
jxs_joint_j_1.relative_to = relative_to
jxs_joint_j_1.marker_name = '.Unknown.ges_upper_cylinder.jxs_joint_j_1'
_turn_ground_cfs_collar_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfs_collar_top')
jxs_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfs_collar_top))
_turn_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_bot').location
_turn_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_top').location
jxs_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_uc_bot, _turn_ground_hps_uc_top, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
jxs_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_actuator_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.ues_actuator_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
ues_actuator_j_1.relative_to = relative_to
ues_actuator_j_1.marker_name = '.Unknown.ges_upper_cylinder.ues_actuator_j_1'
_turn_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_1')
ues_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder_jxs_joint_j_1))
_turn_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_1')
ues_actuator_j_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder_jxs_joint_j_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_1.location, ues_actuator_j_1.orientation)
ues_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
ues_actuator_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_actuator_j_4 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.ues_actuator_j_4')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder')
ues_actuator_j_4.relative_to = relative_to
ues_actuator_j_4.marker_name = '.Unknown.ges_upper_cylinder.ues_actuator_j_4'
_turn_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_1')
ues_actuator_j_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder_jxs_joint_j_1))
_turn_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_1')
ues_actuator_j_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder_jxs_joint_j_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_4.location, ues_actuator_j_4.orientation)
ues_actuator_j_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
ues_actuator_j_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_upper_cylinder_geom1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom1')
gralin_upper_cylinder_geom1.cylinder_name = '.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom1'
_turn_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_top').location
_turn_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_bot').location
gralin_upper_cylinder_geom1.length = (VecUtils.DM(_turn_ground_hps_uc_top, _turn_ground_hps_uc_bot))


gralin_upper_cylinder_geom2 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom2')
gralin_upper_cylinder_geom2.cylinder_name = '.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom2'
_turn_ground_hps_uc_sf_atch_l = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_sf_atch_l').location
_turn_ground_hps_uc_geompt = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_geompt').location
gralin_upper_cylinder_geom2.length = (VecUtils.DM(_turn_ground_hps_uc_sf_atch_l, _turn_ground_hps_uc_geompt))


gralin_upper_cylinder_geom3 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom3')
gralin_upper_cylinder_geom3.cylinder_name = '.Unknown.ges_upper_cylinder.gralin_upper_cylinder_geom3'
_turn_ground_hps_uc_sf_atch_r = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_sf_atch_r').location
_turn_ground_hps_uc_geompt = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_geompt').location
gralin_upper_cylinder_geom3.length = (VecUtils.DM(_turn_ground_hps_uc_sf_atch_r, _turn_ground_hps_uc_geompt))


MARKER_378 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.MARKER_378')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
MARKER_378.relative_to = relative_to
MARKER_378.marker_name = '.Unknown.ges_lower_cylinder.MARKER_378'
_turn_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_lc_atch')
MARKER_378.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_lta_lc_atch))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_378.location, MARKER_378.orientation)
MARKER_378.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.Unknown.ges_lower_cylinder.inertia_frame'
_turn_ges_lower_cylinder_cm = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_lower_cylinder_cm))
_turn_ges_lower_cylinder = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_lower_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_5 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.gralin_5')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
gralin_5.relative_to = relative_to
gralin_5.marker_name = '.Unknown.ges_lower_cylinder.gralin_5'
_turn_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lc_top')
gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_lc_top))
_turn_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lc_top').location
_turn_ground_hps_lc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lc_bot').location
gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_lc_top, _turn_ground_hps_lc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_i_11 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.jxs_joint_i_11')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
jxs_joint_i_11.relative_to = relative_to
jxs_joint_i_11.marker_name = '.Unknown.ges_lower_cylinder.jxs_joint_i_11'
_turn_ges_upper_cylinder_jxs_joint_j_11 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_11')
jxs_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder_jxs_joint_j_11))
_turn_ges_upper_cylinder_jxs_joint_j_11 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_11')
jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder_jxs_joint_j_11))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
jxs_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_7 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.gralin_7')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
gralin_7.relative_to = relative_to
gralin_7.marker_name = '.Unknown.ges_lower_cylinder.gralin_7'
_turn_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpr_wheel_center1')
gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_wheel_center1))
_turn_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpr_wheel_center1').location
_turn_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpl_wheel_center1').location
gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_wheel_center1, _turn_ground_hpl_wheel_center1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_spring_i_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.ues_spring_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
ues_spring_i_1.relative_to = relative_to
ues_spring_i_1.marker_name = '.Unknown.ges_lower_cylinder.ues_spring_i_1'
_turn_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lc_top')
ues_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_i_1.location, ues_spring_i_1.orientation)
ues_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ues_damper_i_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.ues_damper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
ues_damper_i_1.relative_to = relative_to
ues_damper_i_1.marker_name = '.Unknown.ges_lower_cylinder.ues_damper_i_1'
_turn_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lc_top')
ues_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_i_1.location, ues_damper_i_1.orientation)
ues_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ues_stopper_i_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.ues_stopper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
ues_stopper_i_1.relative_to = relative_to
ues_stopper_i_1.marker_name = '.Unknown.ges_lower_cylinder.ues_stopper_i_1'
_turn_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lc_top')
ues_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_i_1.location, ues_stopper_i_1.orientation)
ues_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


coomarker_2 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.coomarker_2')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
coomarker_2.relative_to = relative_to
coomarker_2.marker_name = '.Unknown.ges_lower_cylinder.coomarker_2'
_turn_ground_cfs_wheel_centers_midpoint = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfs_wheel_centers_midpoint')
coomarker_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfs_wheel_centers_midpoint))
_turn_ground_cfs_wheel_centers_midpoint = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfs_wheel_centers_midpoint')
coomarker_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfs_wheel_centers_midpoint))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_2.location, coomarker_2.orientation)
coomarker_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
coomarker_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


coomarker_3 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.coomarker_3')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
coomarker_3.relative_to = relative_to
coomarker_3.marker_name = '.Unknown.ges_lower_cylinder.coomarker_3'
_turn_ground_cfs_nlg_axle_lowpoint = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfs_nlg_axle_lowpoint')
coomarker_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfs_nlg_axle_lowpoint))
_turn_ground_cfs_nlg_axle_lowpoint = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfs_nlg_axle_lowpoint')
coomarker_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfs_nlg_axle_lowpoint))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_3.location, coomarker_3.orientation)
coomarker_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
coomarker_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


MARKER_3 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.MARKER_3')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
MARKER_3.relative_to = relative_to
MARKER_3.marker_name = '.Unknown.ges_lower_cylinder.MARKER_3'
_turn_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpl_wheel_center1')
MARKER_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_wheel_center1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_3.location, MARKER_3.orientation)
MARKER_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_4 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.MARKER_4')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder')
MARKER_4.relative_to = relative_to
MARKER_4.marker_name = '.Unknown.ges_lower_cylinder.MARKER_4'
_turn_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpr_wheel_center1')
MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_wheel_center1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_4.location, MARKER_4.orientation)
MARKER_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_geom1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.gralin_geom1')
gralin_geom1.cylinder_name = '.Unknown.ges_lower_cylinder.gralin_geom1'
_turn_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lc_top').location
_turn_ground_hps_lc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lc_bot').location
gralin_geom1.length = (VecUtils.DM(_turn_ground_hps_lc_top, _turn_ground_hps_lc_bot))


gralin_geom2 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_cylinder.gralin_geom2')
gralin_geom2.cylinder_name = '.Unknown.ges_lower_cylinder.gralin_geom2'
_turn_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpr_wheel_center1').location
_turn_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hpl_wheel_center1').location
gralin_geom2.length = (VecUtils.DM(_turn_ground_hpr_wheel_center1, _turn_ground_hpl_wheel_center1))


inertia_frame = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.Unknown.ges_upper_torque_arm.inertia_frame'
_turn_ges_upper_torque_arm_cm = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_torque_arm_cm))
_turn_ges_upper_torque_arm = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_torque_arm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_9 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.gralin_9')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm')
gralin_9.relative_to = relative_to
gralin_9.marker_name = '.Unknown.ges_upper_torque_arm.gralin_9'
_turn_ground_hps_uta_uc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uta_uc_atch')
gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_uta_uc_atch))
_turn_ground_hps_uta_uc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uta_uc_atch').location
_turn_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_uta_atch').location
gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_uta_uc_atch, _turn_ground_hps_lta_uta_atch, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_j_8 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.jxs_joint_j_8')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm')
jxs_joint_j_8.relative_to = relative_to
jxs_joint_j_8.marker_name = '.Unknown.ges_upper_torque_arm.jxs_joint_j_8'
_turn_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_uta_atch')
jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_lta_uta_atch))
_turn_ground_origo1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.origo1')
jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _turn_ground_origo1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
jxs_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_i_10 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.jxs_joint_i_10')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm')
jxs_joint_i_10.relative_to = relative_to
jxs_joint_i_10.marker_name = '.Unknown.ges_upper_torque_arm.jxs_joint_i_10'
_turn_ges_collar_jxs_joint_j_10 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_j_10')
jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_collar_jxs_joint_j_10))
_turn_ges_collar_jxs_joint_j_10 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_j_10')
jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_collar_jxs_joint_j_10))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
jxs_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_upper_torque_arm_geom = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
gralin_upper_torque_arm_geom.cylinder_name = '.Unknown.ges_upper_torque_arm.gralin_upper_torque_arm_geom'
_turn_ground_hps_uta_uc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uta_uc_atch').location
_turn_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_uta_atch').location
gralin_upper_torque_arm_geom.length = (VecUtils.DM(_turn_ground_hps_uta_uc_atch, _turn_ground_hps_lta_uta_atch))


MARKER_379 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.MARKER_379')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm')
MARKER_379.relative_to = relative_to
MARKER_379.marker_name = '.Unknown.ges_lower_torque_arm.MARKER_379'
_turn_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_lc_atch')
MARKER_379.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_lta_lc_atch))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_379.location, MARKER_379.orientation)
MARKER_379.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.Unknown.ges_lower_torque_arm.inertia_frame'
_turn_ges_lower_torque_arm_cm = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_lower_torque_arm_cm))
_turn_ges_lower_torque_arm = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_lower_torque_arm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_i_8 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.jxs_joint_i_8')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm')
jxs_joint_i_8.relative_to = relative_to
jxs_joint_i_8.marker_name = '.Unknown.ges_lower_torque_arm.jxs_joint_i_8'
_turn_ges_upper_torque_arm_jxs_joint_j_8 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.jxs_joint_j_8')
jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_torque_arm_jxs_joint_j_8))
_turn_ges_upper_torque_arm_jxs_joint_j_8 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_torque_arm.jxs_joint_j_8')
jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_torque_arm_jxs_joint_j_8))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
jxs_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_10 = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.gralin_10')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm')
gralin_10.relative_to = relative_to
gralin_10.marker_name = '.Unknown.ges_lower_torque_arm.gralin_10'
_turn_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_lc_atch')
gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_lta_lc_atch))
_turn_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_lc_atch').location
_turn_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_uta_atch').location
gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_lta_lc_atch, _turn_ground_hps_lta_uta_atch, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_lower_torque_arm_geom = Jusme.ActiveUSScene.getObject('.Unknown.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
gralin_lower_torque_arm_geom.cylinder_name = '.Unknown.ges_lower_torque_arm.gralin_lower_torque_arm_geom'
_turn_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_lc_atch').location
_turn_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_lta_uta_atch').location
gralin_lower_torque_arm_geom.length = (VecUtils.DM(_turn_ground_hps_lta_lc_atch, _turn_ground_hps_lta_uta_atch))


jxs_joint_j_10 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_j_10')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar')
jxs_joint_j_10.relative_to = relative_to
jxs_joint_j_10.marker_name = '.Unknown.ges_collar.jxs_joint_j_10'
_turn_ground_hps_uta_uc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uta_uc_atch')
jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_uta_uc_atch))
_turn_ground_origo1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.origo1')
jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _turn_ground_origo1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
jxs_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.Unknown.ges_collar.inertia_frame'
_turn_ges_collar_cm = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_collar_cm))
_turn_ges_collar = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_collar))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_24 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.gralin_24')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar')
gralin_24.relative_to = relative_to
gralin_24.marker_name = '.Unknown.ges_collar.gralin_24'
_turn_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_bot')
gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_uc_bot))
_turn_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_bot').location
_turn_ground_cfs_collar_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfs_collar_top').location
gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_uc_bot, _turn_ground_cfs_collar_top, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar')
jxs_joint_i_1.relative_to = relative_to
jxs_joint_i_1.marker_name = '.Unknown.ges_collar.jxs_joint_i_1'
_turn_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_1')
jxs_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder_jxs_joint_j_1))
_turn_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_upper_cylinder.jxs_joint_j_1')
jxs_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_upper_cylinder_jxs_joint_j_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
jxs_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_actuator_i_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.ues_actuator_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar')
ues_actuator_i_1.relative_to = relative_to
ues_actuator_i_1.marker_name = '.Unknown.ges_collar.ues_actuator_i_1'
_turn_ges_collar_jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_i_1')
ues_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_collar_jxs_joint_i_1))
_turn_ges_collar_jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_i_1')
ues_actuator_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_collar_jxs_joint_i_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_1.location, ues_actuator_i_1.orientation)
ues_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
ues_actuator_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_actuator_i_4 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.ues_actuator_i_4')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar')
ues_actuator_i_4.relative_to = relative_to
ues_actuator_i_4.marker_name = '.Unknown.ges_collar.ues_actuator_i_4'
_turn_ges_collar_jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_i_1')
ues_actuator_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_collar_jxs_joint_i_1))
_turn_ges_collar_jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.jxs_joint_i_1')
ues_actuator_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_collar_jxs_joint_i_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_4.location, ues_actuator_i_4.orientation)
ues_actuator_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
ues_actuator_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_collar = Jusme.ActiveUSScene.getObject('.Unknown.ges_collar.gralin_collar')
gralin_collar.cylinder_name = '.Unknown.ges_collar.gralin_collar'
_turn_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_uc_bot').location
_turn_ground_cfs_collar_top = Jusme.ActiveUSScene.getObject('.Unknown.ground.cfs_collar_top').location
gralin_collar.length = (VecUtils.DM(_turn_ground_hps_uc_bot, _turn_ground_cfs_collar_top))



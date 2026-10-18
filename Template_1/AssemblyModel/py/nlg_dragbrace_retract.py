import Jusme
from Jusme import Base
from Fmbs.import_all_node import MakeSceneNodeByType
import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils
UNITS_1 = MakeSceneNodeByType('DefaultsUnits', '.MODEL.UNITS_1')
UNITS_1.length_opt = 0
UNITS_1.length = 'mm'
UNITS_1.angle = 'deg'
UNITS_1.force = 'newton'
UNITS_1.mass = 'kg'
UNITS_1.time = 'sec'
UNITS_1.coordinate_system_type = 'cartesian'
UNITS_1.orientation_type = 'body313'
steel = MakeSceneNodeByType('MaterialCreate', '.retract.steel')
steel.material_name = '.retract.steel'
steel.adams_id = 2
steel.density = 7.801e-06
steel.youngs_modulus = 207000.0
steel.poissons_ratio = 0.29
aluminum = MakeSceneNodeByType('MaterialCreate', '.retract.aluminum')
aluminum.material_name = '.retract.aluminum'
aluminum.adams_id = 3
aluminum.density = 2.74e-06
aluminum.youngs_modulus = 71705.0
aluminum.poissons_ratio = 0.33
steel_2 = MakeSceneNodeByType('MaterialCreate', '.retract.steel_2')
steel_2.material_name = '.retract.steel_2'
steel_2.adams_id = 1
steel_2.density = 7.801e-06
steel_2.youngs_modulus = 207000.0
steel_2.poissons_ratio = 0.29
aluminum_2 = MakeSceneNodeByType('MaterialCreate', '.retract.aluminum_2')
aluminum_2.material_name = '.retract.aluminum_2'
aluminum_2.adams_id = 4
aluminum_2.density = 2.74e-06
aluminum_2.youngs_modulus = 71705.0
aluminum_2.poissons_ratio = 0.33
ground = Jusme.ActiveUSScene.getObject('.retract.ground')
ground.part_name = 'ground'
hps_db_sf_atch = MakeSceneNodeByType('Point', '.retract.ground.hps_db_sf_atch')
hps_db_sf_atch.point_name = '.retract.ground.hps_db_sf_atch'
hps_db_sf_atch.location = Base.Vector (7484.11, 0.0, 1623.06)
hps_db_uc_atch = MakeSceneNodeByType('Point', '.retract.ground.hps_db_uc_atch')
hps_db_uc_atch.point_name = '.retract.ground.hps_db_uc_atch'
hps_db_uc_atch.location = Base.Vector (6451.6, 0.0, 1016.0)
hps_rod_bot = MakeSceneNodeByType('Point', '.retract.ground.hps_rod_bot')
hps_rod_bot.point_name = '.retract.ground.hps_rod_bot'
hps_rod_bot.location = Base.Vector (6434.3591354821, 0.0, 1005.8633047504)
hps_rod_top = MakeSceneNodeByType('Point', '.retract.ground.hps_rod_top')
hps_rod_top.point_name = '.retract.ground.hps_rod_top'
hps_rod_top.location = Base.Vector (7227.4389033572, 0.0, 1472.1512863532)
ges_sf_actuator = MakeSceneNodeByType('PartGeneral', '.retract.ges_sf_actuator')
ges_sf_actuator.part_name = '.retract.ges_sf_actuator'
ges_sf_actuator.adams_id = 7
ges_sf_actuator.location = Base.Vector (6967.855, 0.0, 1319.53)
ges_sf_actuator.orientation = Base.Vector (270.0000000009, 120.4532239116, 90.0000000003)
cm = MakeSceneNodeByType('Marker', '.retract.ges_sf_actuator.cm')
cm.marker_name = '.retract.ges_sf_actuator.cm'
cm.adams_id = 21
cm.location = Base.Vector (-2.6589288646e-08, -8.1094015533e-09, -25.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.retract.ges_sf_actuator.inertia_frame')
inertia_frame.marker_name = '.retract.ges_sf_actuator.inertia_frame'
inertia_frame.adams_id = 22
inertia_frame.location = Base.Vector (-2.6588904689e-08, -8.1094015533e-09, -25.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_1 = MakeSceneNodeByType('Marker', '.retract.ges_sf_actuator.gralin_1')
gralin_1.marker_name = '.retract.ges_sf_actuator.gralin_1'
gralin_1.adams_id = 23
gralin_1.location = Base.Vector (-2.6589286328e-08, -8.1094057298e-09, -598.873681109)
gralin_1.orientation = Base.Vector (0.0, 0.0, 0.0)
stopper_actuator = MakeSceneNodeByType('Marker', '.retract.ges_sf_actuator.stopper_actuator')
stopper_actuator.marker_name = '.retract.ges_sf_actuator.stopper_actuator'
stopper_actuator.adams_id = 87
stopper_actuator.location = Base.Vector (2.2026824809e-09, 0.0, 618.8736811067)
stopper_actuator.orientation = Base.Vector (90.0000000003, 120.4532239116, 270.0000000009)
MARKER_85 = MakeSceneNodeByType('Marker', '.retract.ges_sf_actuator.MARKER_85')
MARKER_85.marker_name = '.retract.ges_sf_actuator.MARKER_85'
MARKER_85.adams_id = 85
MARKER_85.location = Base.Vector (1.3451462166e-09, 0.0, 158.8736811071)
MARKER_85.orientation = Base.Vector (90.0000000003, 180.0, 0.0)
MARKER_89 = MakeSceneNodeByType('Marker', '.retract.ges_sf_actuator.MARKER_89')
MARKER_89.marker_name = '.retract.ges_sf_actuator.MARKER_89'
MARKER_89.adams_id = 89
MARKER_89.location = Base.Vector (2.2026824809e-09, 0.0, 618.8736811067)
MARKER_89.orientation = Base.Vector (90.0000000003, 120.4532239116, 270.0000000009)
MARKER_97 = MakeSceneNodeByType('Marker', '.retract.ges_sf_actuator.MARKER_97')
MARKER_97.marker_name = '.retract.ges_sf_actuator.MARKER_97'
MARKER_97.adams_id = 97
MARKER_97.location = Base.Vector (-4.5918824298e-10, 0.0, -598.873681109)
MARKER_97.orientation = Base.Vector (90.0000000003, 120.4532239116, 270.0000000009)
MARKER_100 = MakeSceneNodeByType('Marker', '.retract.ges_sf_actuator.MARKER_100')
MARKER_100.marker_name = '.retract.ges_sf_actuator.MARKER_100'
MARKER_100.adams_id = 100
MARKER_100.location = Base.Vector (2.2026824809e-09, 0.0, 618.8736811067)
MARKER_100.orientation = Base.Vector (90.0000000003, 120.4532239116, 270.0000000009)
ges_sf_actuator = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator')
ges_sf_actuator.part_name = '.retract.ges_sf_actuator'
gralin_dragbrace_geom = MakeSceneNodeByType('ShapeCylinder', '.retract.ges_sf_actuator.gralin_dragbrace_geom')
center_marker = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator.gralin_1')
gralin_dragbrace_geom.center_marker = center_marker
gralin_dragbrace_geom.cylinder_name = '.retract.ges_sf_actuator.gralin_dragbrace_geom'
gralin_dragbrace_geom.adams_id = 32
gralin_dragbrace_geom.angle_extent = 360.0000000012
gralin_dragbrace_geom.length = 1147.7473622179
gralin_dragbrace_geom.radius = 50.8
gralin_dragbrace_geom.side_count_for_body = 15
gralin_dragbrace_geom.segment_count_for_ends = 15


ges_sf_rod = MakeSceneNodeByType('PartGeneral', '.retract.ges_sf_rod')
ges_sf_rod.part_name = '.retract.ges_sf_rod'
ges_sf_rod.adams_id = 5
ges_sf_rod.location = Base.Vector (0.0, 0.0, 0.0)
ges_sf_rod.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_stopper_rod = MakeSceneNodeByType('Marker', '.retract.ges_sf_rod.MARKER_stopper_rod')
MARKER_stopper_rod.marker_name = '.retract.ges_sf_rod.MARKER_stopper_rod'
MARKER_stopper_rod.adams_id = 86
MARKER_stopper_rod.location = Base.Vector (6434.3591354821, 0.0, 1005.8633047504)
MARKER_stopper_rod.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_25 = MakeSceneNodeByType('Marker', '.retract.ges_sf_rod.gralin_25')
gralin_25.marker_name = '.retract.ges_sf_rod.gralin_25'
gralin_25.adams_id = 3
gralin_25.location = Base.Vector (6434.3591354821, 0.0, 1005.8633047504)
gralin_25.orientation = Base.Vector (90.0, 59.5467760909, 270.0)
cm = MakeSceneNodeByType('Marker', '.retract.ges_sf_rod.cm')
cm.marker_name = '.retract.ges_sf_rod.cm'
cm.adams_id = 76
cm.location = Base.Vector (6830.8990194193, 0.0, 1239.0072955524)
cm.orientation = Base.Vector (90.0, 59.5467760909, 0.0)
MARKER_84 = MakeSceneNodeByType('Marker', '.retract.ges_sf_rod.MARKER_84')
MARKER_84.marker_name = '.retract.ges_sf_rod.MARKER_84'
MARKER_84.adams_id = 84
MARKER_84.location = Base.Vector (6830.8990194192, 0.0, 1239.0072955517)
MARKER_84.orientation = Base.Vector (90.0000000003, 59.5467760889, 0.0)
MARKER_88 = MakeSceneNodeByType('Marker', '.retract.ges_sf_rod.MARKER_88')
MARKER_88.marker_name = '.retract.ges_sf_rod.MARKER_88'
MARKER_88.adams_id = 88
MARKER_88.location = Base.Vector (6434.3591354821, 0.0, 1005.8633047504)
MARKER_88.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_96 = MakeSceneNodeByType('Marker', '.retract.ges_sf_rod.MARKER_96')
MARKER_96.marker_name = '.retract.ges_sf_rod.MARKER_96'
MARKER_96.adams_id = 96
MARKER_96.location = Base.Vector (6434.3591354821, 0.0, 1005.8633047504)
MARKER_96.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_101 = MakeSceneNodeByType('Marker', '.retract.ges_sf_rod.MARKER_101')
MARKER_101.marker_name = '.retract.ges_sf_rod.MARKER_101'
MARKER_101.adams_id = 101
MARKER_101.location = Base.Vector (6434.3591354821, 0.0, 1005.8633047504)
MARKER_101.orientation = Base.Vector (0.0, 0.0, 0.0)
ges_sf_rod = Jusme.ActiveUSScene.getObject('.retract.ges_sf_rod')
ges_sf_rod.part_name = '.retract.ges_sf_rod'
CYLINDER_30 = MakeSceneNodeByType('ShapeCylinder', '.retract.ges_sf_rod.CYLINDER_30')
center_marker = Jusme.ActiveUSScene.getObject('.retract.ges_sf_rod.gralin_25')
CYLINDER_30.center_marker = center_marker
CYLINDER_30.cylinder_name = '.retract.ges_sf_rod.CYLINDER_30'
CYLINDER_30.adams_id = 30
CYLINDER_30.angle_extent = 360.0000000012
CYLINDER_30.length = 920.0
CYLINDER_30.radius = 27.5
CYLINDER_30.side_count_for_body = 20
CYLINDER_30.segment_count_for_ends = 20


joscly_ac_rd = MakeSceneNodeByType('JointCylinder', '.retract.joscly_ac_rd')
i_marker_name = Jusme.ActiveUSScene.getObject('.retract.ges_sf_rod.MARKER_84')
joscly_ac_rd.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator.MARKER_85')
joscly_ac_rd.j_marker_name = j_marker_name
joscly_ac_rd.joint_name = '.retract.joscly_ac_rd'
joscly_ac_rd.adams_id = 13


steel = Jusme.ActiveUSScene.getObject('.retract.steel')
steel.material_name = '.retract.steel'


aluminum = Jusme.ActiveUSScene.getObject('.retract.aluminum')
aluminum.material_name = '.retract.aluminum'


steel_2 = Jusme.ActiveUSScene.getObject('.retract.steel_2')
steel_2.material_name = '.retract.steel_2'


aluminum_2 = Jusme.ActiveUSScene.getObject('.retract.aluminum_2')
aluminum_2.material_name = '.retract.aluminum_2'


inertia_frame = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.retract.ges_sf_actuator.inertia_frame'
_retract_ges_sf_actuator_cm = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _retract_ges_sf_actuator_cm))
_retract_ges_sf_actuator = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _retract_ges_sf_actuator))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_1 = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator.gralin_1')
relative_to = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator')
gralin_1.relative_to = relative_to
gralin_1.marker_name = '.retract.ges_sf_actuator.gralin_1'
_retract_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.retract.ground.hps_db_sf_atch')
gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _retract_ground_hps_db_sf_atch))
_retract_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.retract.ground.hps_db_sf_atch').location
_retract_ground_hps_db_uc_atch = Jusme.ActiveUSScene.getObject('.retract.ground.hps_db_uc_atch').location
gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_retract_ground_hps_db_sf_atch, _retract_ground_hps_db_uc_atch, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_dragbrace_geom = Jusme.ActiveUSScene.getObject('.retract.ges_sf_actuator.gralin_dragbrace_geom')
gralin_dragbrace_geom.cylinder_name = '.retract.ges_sf_actuator.gralin_dragbrace_geom'
_retract_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.retract.ground.hps_db_sf_atch').location
_retract_ground_hps_db_uc_atch = Jusme.ActiveUSScene.getObject('.retract.ground.hps_db_uc_atch').location
gralin_dragbrace_geom.length = (VecUtils.DM(_retract_ground_hps_db_sf_atch, _retract_ground_hps_db_uc_atch) - 50.0)


gralin_25 = Jusme.ActiveUSScene.getObject('.retract.ges_sf_rod.gralin_25')
relative_to = Jusme.ActiveUSScene.getObject('.retract.ges_sf_rod')
gralin_25.relative_to = relative_to
gralin_25.marker_name = '.retract.ges_sf_rod.gralin_25'
_retract_ground_hps_rod_bot = Jusme.ActiveUSScene.getObject('.retract.ground.hps_rod_bot')
gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _retract_ground_hps_rod_bot))
_retract_ground_hps_db_uc_atch = Jusme.ActiveUSScene.getObject('.retract.ground.hps_db_uc_atch').location
_retract_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.retract.ground.hps_db_sf_atch').location
gralin_25.orientation = (VecUtils.ORI_ALONG_AXIS(_retract_ground_hps_db_uc_atch, _retract_ground_hps_db_sf_atch, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_25.location, gralin_25.orientation)
gralin_25.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_25.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


CYLINDER_30 = Jusme.ActiveUSScene.getObject('.retract.ges_sf_rod.CYLINDER_30')
CYLINDER_30.cylinder_name = '.retract.ges_sf_rod.CYLINDER_30'
_retract_ground_hps_rod_bot = Jusme.ActiveUSScene.getObject('.retract.ground.hps_rod_bot').location
_retract_ground_hps_rod_top = Jusme.ActiveUSScene.getObject('.retract.ground.hps_rod_top').location
CYLINDER_30.length = (VecUtils.DM(_retract_ground_hps_rod_bot, _retract_ground_hps_rod_top))
CYLINDER_30.radius = 27.5



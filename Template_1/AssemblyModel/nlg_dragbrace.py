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
hps_db_sf_atch = MakeSceneNodeByType('Point', '.Unknown.ground.hps_db_sf_atch')
hps_db_sf_atch.point_name = '.Unknown.ground.hps_db_sf_atch'
hps_db_sf_atch.location = Base.Vector (7484.11, 0.0, 1623.06)
hps_db_uc_atch = MakeSceneNodeByType('Point', '.Unknown.ground.hps_db_uc_atch')
hps_db_uc_atch.point_name = '.Unknown.ground.hps_db_uc_atch'
hps_db_uc_atch.location = Base.Vector (6451.6, 0.0, 1016.0)
ges_dragbrace = MakeSceneNodeByType('PartGeneral', '.Unknown.ges_dragbrace')
ges_dragbrace.part_name = '.Unknown.ges_dragbrace'
ges_dragbrace.adams_id = 33
ges_dragbrace.location = Base.Vector (6967.855, 0.0, 1319.53)
ges_dragbrace.orientation = Base.Vector (270.0, 120.4532239091, 90.0)
cm = MakeSceneNodeByType('Marker', '.Unknown.ges_dragbrace.cm')
cm.marker_name = '.Unknown.ges_dragbrace.cm'
cm.adams_id = 301
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.Unknown.ges_dragbrace.inertia_frame')
inertia_frame.marker_name = '.Unknown.ges_dragbrace.inertia_frame'
inertia_frame.adams_id = 302
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_1 = MakeSceneNodeByType('Marker', '.Unknown.ges_dragbrace.gralin_1')
gralin_1.marker_name = '.Unknown.ges_dragbrace.gralin_1'
gralin_1.adams_id = 303
gralin_1.location = Base.Vector (0.0, 0.0, -598.8736811)
gralin_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ges_dragbrace = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace.cm')
ges_dragbrace.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace.inertia_frame')
ges_dragbrace.inertia_marker = inertia_marker
ges_dragbrace.part_name = '.Unknown.ges_dragbrace'
ges_dragbrace.mass = 27.3726690382
ges_dragbrace.ixx = 3481154.0175
ges_dragbrace.iyy = 3481154.0175
ges_dragbrace.izz = 35319.502313
ges_dragbrace.ixy = 0.0
ges_dragbrace.izx = 0.0
ges_dragbrace.iyz = 0.0
gralin_dragbrace_geom = MakeSceneNodeByType('ShapeCylinder', '.Unknown.ges_dragbrace.gralin_dragbrace_geom')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace.gralin_1')
gralin_dragbrace_geom.center_marker = center_marker
gralin_dragbrace_geom.cylinder_name = '.Unknown.ges_dragbrace.gralin_dragbrace_geom'
gralin_dragbrace_geom.adams_id = 85
gralin_dragbrace_geom.angle_extent = 360.0
gralin_dragbrace_geom.length = 1197.7473622
gralin_dragbrace_geom.radius = 50.8
gralin_dragbrace_geom.side_count_for_body = 15
gralin_dragbrace_geom.segment_count_for_ends = 15


aluminum = Jusme.ActiveUSScene.getObject('.Unknown.aluminum')
aluminum.material_name = '.Unknown.aluminum'


steel = Jusme.ActiveUSScene.getObject('.Unknown.steel')
steel.material_name = '.Unknown.steel'


steel_2 = Jusme.ActiveUSScene.getObject('.Unknown.steel_2')
steel_2.material_name = '.Unknown.steel_2'


aluminum_2 = Jusme.ActiveUSScene.getObject('.Unknown.aluminum_2')
aluminum_2.material_name = '.Unknown.aluminum_2'


inertia_frame = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.Unknown.ges_dragbrace.inertia_frame'
_turn_ges_dragbrace_cm = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_dragbrace_cm))
_turn_ges_dragbrace = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ges_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_1 = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace.gralin_1')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace')
gralin_1.relative_to = relative_to
gralin_1.marker_name = '.Unknown.ges_dragbrace.gralin_1'
_turn_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_db_sf_atch')
gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hps_db_sf_atch))
_turn_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_db_sf_atch').location
_turn_ground_hps_db_uc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_db_uc_atch').location
gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hps_db_sf_atch, _turn_ground_hps_db_uc_atch, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_dragbrace_geom = Jusme.ActiveUSScene.getObject('.Unknown.ges_dragbrace.gralin_dragbrace_geom')
gralin_dragbrace_geom.cylinder_name = '.Unknown.ges_dragbrace.gralin_dragbrace_geom'
_turn_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_db_sf_atch').location
_turn_ground_hps_db_uc_atch = Jusme.ActiveUSScene.getObject('.Unknown.ground.hps_db_uc_atch').location
gralin_dragbrace_geom.length = (VecUtils.DM(_turn_ground_hps_db_sf_atch, _turn_ground_hps_db_uc_atch))



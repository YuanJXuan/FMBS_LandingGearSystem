import Jusme
from Jusme import Base
from Fmbs.import_all_node import MakeSceneNodeByType
import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils
UNITS_1 = MakeSceneNodeByType('DefaultsUnits', '.MODEL.UNITS_1')
UNITS_1.length = 'meter'
UNITS_1.angle = 'deg'
UNITS_1.force = 'newton'
UNITS_1.mass = 'kg'
UNITS_1.time = 'sec'
UNITS_1.coordinate_system_type = 'cartesian'
UNITS_1.orientation_type = 'body313'
aluminum = MakeSceneNodeByType('MaterialCreate', '.turn.aluminum')
aluminum.material_name = '.turn.aluminum'
aluminum.adams_id = 2
aluminum.density = 2740.0
aluminum.youngs_modulus = 71705000000.0
aluminum.poissons_ratio = 0.33
steel = MakeSceneNodeByType('MaterialCreate', '.turn.steel')
steel.material_name = '.turn.steel'
steel.adams_id = 5
steel.density = 7801.0
steel.youngs_modulus = 207000000000.0
steel.poissons_ratio = 0.29
steel_2 = MakeSceneNodeByType('MaterialCreate', '.turn.steel_2')
steel_2.material_name = '.turn.steel_2'
steel_2.adams_id = 3
steel_2.density = 7801.0
steel_2.youngs_modulus = 207000000000.0
steel_2.poissons_ratio = 0.29
aluminum_2 = MakeSceneNodeByType('MaterialCreate', '.turn.aluminum_2')
aluminum_2.material_name = '.turn.aluminum_2'
aluminum_2.adams_id = 4
aluminum_2.density = 2740.0
aluminum_2.youngs_modulus = 71705000000.0
aluminum_2.poissons_ratio = 0.33
ground = Jusme.ActiveUSScene.getObject('.turn.ground')
ground.part_name = 'ground'
zdt_1 = MakeSceneNodeByType('Marker', '.turn.ground.zdt_1')
zdt_1.marker_name = '.turn.ground.zdt_1'
zdt_1.adams_id = 461
zdt_1.location = Base.Vector (5.9187250255, 0.0125840225, 0.8)
zdt_1.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
zdt_2 = MakeSceneNodeByType('Marker', '.turn.ground.zdt_2')
zdt_2.marker_name = '.turn.ground.zdt_2'
zdt_2.adams_id = 462
zdt_2.location = Base.Vector (5.7792875383, -0.08112396625, 0.8)
zdt_2.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
hsg_1 = MakeSceneNodeByType('Point', '.turn.ground.hsg_1')
hsg_1.point_name = '.turn.ground.hsg_1'
hsg_1.location = Base.Vector (6.1976, 0.2, 0.8)
hsg_2 = MakeSceneNodeByType('Point', '.turn.ground.hsg_2')
hsg_2.point_name = '.turn.ground.hsg_2'
hsg_2.location = Base.Vector (5.7328083759, -0.1123599625, 0.8)
hsg = MakeSceneNodeByType('PartGeneral', '.turn.hsg')
hsg.part_name = '.turn.hsg'
hsg.adams_id = 47
hsg.location = Base.Vector (0.0, 0.0, 0.0)
hsg.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_463 = MakeSceneNodeByType('Marker', '.turn.hsg.gralin_463')
gralin_463.marker_name = '.turn.hsg.gralin_463'
gralin_463.adams_id = 463
gralin_463.location = Base.Vector (6.1976, 0.2, 0.8)
gralin_463.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
cm = MakeSceneNodeByType('Marker', '.turn.hsg.cm')
cm.marker_name = '.turn.hsg.cm'
cm.adams_id = 473
cm.location = Base.Vector (5.965204188, 0.04382001875, 0.8)
cm.orientation = Base.Vector (303.9027984088, 90.0, 89.8631118907)
MARKER_469 = MakeSceneNodeByType('Marker', '.turn.hsg.MARKER_469')
MARKER_469.marker_name = '.turn.hsg.MARKER_469'
MARKER_469.adams_id = 469
MARKER_469.location = Base.Vector (5.8490062819, -0.034269971868, 0.8)
MARKER_469.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
hsg = Jusme.ActiveUSScene.getObject('.turn.hsg')
hsg.part_name = '.turn.hsg'
CYLINDER_213 = MakeSceneNodeByType('ShapeCylinder', '.turn.hsg.CYLINDER_213')
center_marker = Jusme.ActiveUSScene.getObject('.turn.hsg.gralin_463')
CYLINDER_213.center_marker = center_marker
CYLINDER_213.cylinder_name = '.turn.hsg.CYLINDER_213'
CYLINDER_213.adams_id = 213
CYLINDER_213.angle_extent = 360.0
CYLINDER_213.length = 0.56
CYLINDER_213.radius = 0.022
CYLINDER_213.side_count_for_body = 20
CYLINDER_213.segment_count_for_ends = 20


zdt = MakeSceneNodeByType('PartGeneral', '.turn.zdt')
zdt.part_name = '.turn.zdt'
zdt.adams_id = 48
zdt.location = Base.Vector (0.0, 0.0, 0.0)
zdt.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_464 = MakeSceneNodeByType('Marker', '.turn.zdt.gralin_464')
gralin_464.marker_name = '.turn.zdt.gralin_464'
gralin_464.adams_id = 464
gralin_464.location = Base.Vector (5.9187250255, 0.0125840225, 0.8)
gralin_464.orientation = Base.Vector (303.9027984031, 90.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.turn.zdt.cm')
cm.marker_name = '.turn.zdt.cm'
cm.adams_id = 474
cm.location = Base.Vector (5.8490062819, -0.034269971868, 0.8)
cm.orientation = Base.Vector (123.9027984031, 90.0, 34.4641635531)
MARKER_470 = MakeSceneNodeByType('Marker', '.turn.zdt.MARKER_470')
MARKER_470.marker_name = '.turn.zdt.MARKER_470'
MARKER_470.adams_id = 470
MARKER_470.location = Base.Vector (5.8490062819, -0.034269971868, 0.8)
MARKER_470.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
zdt = Jusme.ActiveUSScene.getObject('.turn.zdt')
zdt.part_name = '.turn.zdt'
CYLINDER_214 = MakeSceneNodeByType('ShapeCylinder', '.turn.zdt.CYLINDER_214')
center_marker = Jusme.ActiveUSScene.getObject('.turn.zdt.gralin_464')
CYLINDER_214.center_marker = center_marker
CYLINDER_214.cylinder_name = '.turn.zdt.CYLINDER_214'
CYLINDER_214.adams_id = 214
CYLINDER_214.angle_extent = 360.0
CYLINDER_214.length = 0.168
CYLINDER_214.radius = 0.042
CYLINDER_214.side_count_for_body = 20
CYLINDER_214.segment_count_for_ends = 20


hsg_zdt = MakeSceneNodeByType('JointTranslational', '.turn.hsg_zdt')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.hsg.MARKER_469')
hsg_zdt.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.zdt.MARKER_470')
hsg_zdt.j_marker_name = j_marker_name
hsg_zdt.joint_name = '.turn.hsg_zdt'
hsg_zdt.adams_id = 66


zdt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.zdt_1')
zdt_1.marker_name = '.turn.ground.zdt_1'
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_2').location
zdt_1.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hsg_1, _turn_ground_hsg_2, 0.6 * VecUtils.DM(_turn_ground_hsg_1, _turn_ground_hsg_2)))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_2').location
zdt_1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_hsg_2, "Z"))


zdt_2 = Jusme.ActiveUSScene.getObject('.turn.ground.zdt_2')
zdt_2.marker_name = '.turn.ground.zdt_2'
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_2').location
zdt_2.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hsg_1, _turn_ground_hsg_2, 0.9 * VecUtils.DM(_turn_ground_hsg_1, _turn_ground_hsg_2)))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_2').location
zdt_2.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_hsg_2, "Z"))


aluminum = Jusme.ActiveUSScene.getObject('.turn.aluminum')
aluminum.material_name = '.turn.aluminum'


steel = Jusme.ActiveUSScene.getObject('.turn.steel')
steel.material_name = '.turn.steel'


steel_2 = Jusme.ActiveUSScene.getObject('.turn.steel_2')
steel_2.material_name = '.turn.steel_2'


aluminum_2 = Jusme.ActiveUSScene.getObject('.turn.aluminum_2')
aluminum_2.material_name = '.turn.aluminum_2'


gralin_463 = Jusme.ActiveUSScene.getObject('.turn.hsg.gralin_463')
relative_to = Jusme.ActiveUSScene.getObject('.turn.hsg')
gralin_463.relative_to = relative_to
gralin_463.marker_name = '.turn.hsg.gralin_463'
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_1')
gralin_463.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hsg_1))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_2').location
gralin_463.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_hsg_2, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_463.location, gralin_463.orientation)
gralin_463.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_463.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


MARKER_469 = Jusme.ActiveUSScene.getObject('.turn.hsg.MARKER_469')
relative_to = Jusme.ActiveUSScene.getObject('.turn.hsg')
MARKER_469.relative_to = relative_to
MARKER_469.marker_name = '.turn.hsg.MARKER_469'
_turn_zdt_cm = Jusme.ActiveUSScene.getObject('.turn.zdt.cm')
MARKER_469.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_zdt_cm))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_1').location
_turn_ground_zdt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.zdt_1').location
MARKER_469.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_zdt_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_469.location, MARKER_469.orientation)
MARKER_469.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
MARKER_469.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


CYLINDER_213 = Jusme.ActiveUSScene.getObject('.turn.hsg.CYLINDER_213')
CYLINDER_213.cylinder_name = '.turn.hsg.CYLINDER_213'
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_2').location
CYLINDER_213.length = (VecUtils.DM(_turn_ground_hsg_1, _turn_ground_hsg_2))


gralin_464 = Jusme.ActiveUSScene.getObject('.turn.zdt.gralin_464')
relative_to = Jusme.ActiveUSScene.getObject('.turn.zdt')
gralin_464.relative_to = relative_to
gralin_464.marker_name = '.turn.zdt.gralin_464'
_turn_ground_zdt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.zdt_1')
gralin_464.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_zdt_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_464.location, gralin_464.orientation)
gralin_464.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_470 = Jusme.ActiveUSScene.getObject('.turn.zdt.MARKER_470')
relative_to = Jusme.ActiveUSScene.getObject('.turn.zdt')
MARKER_470.relative_to = relative_to
MARKER_470.marker_name = '.turn.zdt.MARKER_470'
_turn_zdt_cm = Jusme.ActiveUSScene.getObject('.turn.zdt.cm')
MARKER_470.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_zdt_cm))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hsg_1').location
_turn_ground_zdt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.zdt_1').location
MARKER_470.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_zdt_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_470.location, MARKER_470.orientation)
MARKER_470.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
MARKER_470.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


CYLINDER_214 = Jusme.ActiveUSScene.getObject('.turn.zdt.CYLINDER_214')
CYLINDER_214.cylinder_name = '.turn.zdt.CYLINDER_214'
_turn_ground_zdt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.zdt_1').location
_turn_ground_zdt_2 = Jusme.ActiveUSScene.getObject('.turn.ground.zdt_2').location
CYLINDER_214.length = (VecUtils.DM(_turn_ground_zdt_1, _turn_ground_zdt_2))



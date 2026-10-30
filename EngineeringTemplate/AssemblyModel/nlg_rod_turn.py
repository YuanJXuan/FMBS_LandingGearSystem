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
zdt_1 = MakeSceneNodeByType('Marker', '.Unknown.ground.zdt_1')
zdt_1.marker_name = '.Unknown.ground.zdt_1'
zdt_1.adams_id = 461
zdt_1.location = Base.Vector (5918.7250255, 12.5840225, 800.0)
zdt_1.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
zdt_2 = MakeSceneNodeByType('Marker', '.Unknown.ground.zdt_2')
zdt_2.marker_name = '.Unknown.ground.zdt_2'
zdt_2.adams_id = 462
zdt_2.location = Base.Vector (5779.2875383, -81.12396625, 800.0)
zdt_2.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
hsg_1 = MakeSceneNodeByType('Point', '.Unknown.ground.hsg_1')
hsg_1.point_name = '.Unknown.ground.hsg_1'
hsg_1.location = Base.Vector (6197.6, 200.0, 800.0)
hsg_2 = MakeSceneNodeByType('Point', '.Unknown.ground.hsg_2')
hsg_2.point_name = '.Unknown.ground.hsg_2'
hsg_2.location = Base.Vector (5732.8083759, -112.3599625, 800.0)
hsg = MakeSceneNodeByType('PartGeneral', '.Unknown.hsg')
hsg.part_name = '.Unknown.hsg'
hsg.adams_id = 47
hsg.location = Base.Vector (0.0, 0.0, 0.0)
hsg.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_463 = MakeSceneNodeByType('Marker', '.Unknown.hsg.gralin_463')
gralin_463.marker_name = '.Unknown.hsg.gralin_463'
gralin_463.adams_id = 463
gralin_463.location = Base.Vector (6197.6, 200.0, 800.0)
gralin_463.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
cm = MakeSceneNodeByType('Marker', '.Unknown.hsg.cm')
cm.marker_name = '.Unknown.hsg.cm'
cm.adams_id = 473
cm.location = Base.Vector (5965.204188, 43.82001875, 800.0)
cm.orientation = Base.Vector (303.9027984088, 90.0, 89.8631118907)
MARKER_469 = MakeSceneNodeByType('Marker', '.Unknown.hsg.MARKER_469')
MARKER_469.marker_name = '.Unknown.hsg.MARKER_469'
MARKER_469.adams_id = 469
MARKER_469.location = Base.Vector (5849.0062819, -34.269971868, 800.0)
MARKER_469.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
hsg = Jusme.ActiveUSScene.getObject('.Unknown.hsg')
hsg.part_name = '.Unknown.hsg'
CYLINDER_213 = MakeSceneNodeByType('ShapeCylinder', '.Unknown.hsg.CYLINDER_213')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.hsg.gralin_463')
CYLINDER_213.center_marker = center_marker
CYLINDER_213.cylinder_name = '.Unknown.hsg.CYLINDER_213'
CYLINDER_213.adams_id = 213
CYLINDER_213.angle_extent = 360.0
CYLINDER_213.length = 560.0
CYLINDER_213.radius = 22.0
CYLINDER_213.side_count_for_body = 20
CYLINDER_213.segment_count_for_ends = 20


zdt = MakeSceneNodeByType('PartGeneral', '.Unknown.zdt')
zdt.part_name = '.Unknown.zdt'
zdt.adams_id = 48
zdt.location = Base.Vector (0.0, 0.0, 0.0)
zdt.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_464 = MakeSceneNodeByType('Marker', '.Unknown.zdt.gralin_464')
gralin_464.marker_name = '.Unknown.zdt.gralin_464'
gralin_464.adams_id = 464
gralin_464.location = Base.Vector (5918.7250255, 12.5840225, 800.0)
gralin_464.orientation = Base.Vector (303.9027984031, 90.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.Unknown.zdt.cm')
cm.marker_name = '.Unknown.zdt.cm'
cm.adams_id = 474
cm.location = Base.Vector (5849.0062819, -34.269971868, 800.0)
cm.orientation = Base.Vector (123.9027984031, 90.0, 34.4641635531)
MARKER_470 = MakeSceneNodeByType('Marker', '.Unknown.zdt.MARKER_470')
MARKER_470.marker_name = '.Unknown.zdt.MARKER_470'
MARKER_470.adams_id = 470
MARKER_470.location = Base.Vector (5849.0062819, -34.269971868, 800.0)
MARKER_470.orientation = Base.Vector (303.9027984088, 90.0, 90.0)
zdt = Jusme.ActiveUSScene.getObject('.Unknown.zdt')
zdt.part_name = '.Unknown.zdt'
CYLINDER_214 = MakeSceneNodeByType('ShapeCylinder', '.Unknown.zdt.CYLINDER_214')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.zdt.gralin_464')
CYLINDER_214.center_marker = center_marker
CYLINDER_214.cylinder_name = '.Unknown.zdt.CYLINDER_214'
CYLINDER_214.adams_id = 214
CYLINDER_214.angle_extent = 360.0
CYLINDER_214.length = 168.0
CYLINDER_214.radius = 42.0
CYLINDER_214.side_count_for_body = 20
CYLINDER_214.segment_count_for_ends = 20


hsg_zdt = MakeSceneNodeByType('JointTranslational', '.Unknown.hsg_zdt')
i_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.hsg.MARKER_469')
hsg_zdt.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.Unknown.zdt.MARKER_470')
hsg_zdt.j_marker_name = j_marker_name
hsg_zdt.joint_name = '.Unknown.hsg_zdt'
hsg_zdt.adams_id = 66


zdt_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.zdt_1')
zdt_1.marker_name = '.Unknown.ground.zdt_1'
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_2').location
zdt_1.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hsg_1, _turn_ground_hsg_2, 0.6 * VecUtils.DM(_turn_ground_hsg_1, _turn_ground_hsg_2)))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_2').location
zdt_1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_hsg_2, "Z"))


zdt_2 = Jusme.ActiveUSScene.getObject('.Unknown.ground.zdt_2')
zdt_2.marker_name = '.Unknown.ground.zdt_2'
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_2').location
zdt_2.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hsg_1, _turn_ground_hsg_2, 0.9 * VecUtils.DM(_turn_ground_hsg_1, _turn_ground_hsg_2)))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_2').location
zdt_2.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_hsg_2, "Z"))


aluminum = Jusme.ActiveUSScene.getObject('.Unknown.aluminum')
aluminum.material_name = '.Unknown.aluminum'


steel = Jusme.ActiveUSScene.getObject('.Unknown.steel')
steel.material_name = '.Unknown.steel'


steel_2 = Jusme.ActiveUSScene.getObject('.Unknown.steel_2')
steel_2.material_name = '.Unknown.steel_2'


aluminum_2 = Jusme.ActiveUSScene.getObject('.Unknown.aluminum_2')
aluminum_2.material_name = '.Unknown.aluminum_2'


gralin_463 = Jusme.ActiveUSScene.getObject('.Unknown.hsg.gralin_463')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.hsg')
gralin_463.relative_to = relative_to
gralin_463.marker_name = '.Unknown.hsg.gralin_463'
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_1')
gralin_463.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hsg_1))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_2').location
gralin_463.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_hsg_2, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_463.location, gralin_463.orientation)
gralin_463.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_463.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


MARKER_469 = Jusme.ActiveUSScene.getObject('.Unknown.hsg.MARKER_469')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.hsg')
MARKER_469.relative_to = relative_to
MARKER_469.marker_name = '.Unknown.hsg.MARKER_469'
_turn_zdt_cm = Jusme.ActiveUSScene.getObject('.Unknown.zdt.cm')
MARKER_469.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_zdt_cm))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_1').location
_turn_ground_zdt_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.zdt_1').location
MARKER_469.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_zdt_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_469.location, MARKER_469.orientation)
MARKER_469.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
MARKER_469.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


CYLINDER_213 = Jusme.ActiveUSScene.getObject('.Unknown.hsg.CYLINDER_213')
CYLINDER_213.cylinder_name = '.Unknown.hsg.CYLINDER_213'
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_1').location
_turn_ground_hsg_2 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_2').location
CYLINDER_213.length = (VecUtils.DM(_turn_ground_hsg_1, _turn_ground_hsg_2))


gralin_464 = Jusme.ActiveUSScene.getObject('.Unknown.zdt.gralin_464')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.zdt')
gralin_464.relative_to = relative_to
gralin_464.marker_name = '.Unknown.zdt.gralin_464'
_turn_ground_zdt_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.zdt_1')
gralin_464.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_zdt_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_464.location, gralin_464.orientation)
gralin_464.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_470 = Jusme.ActiveUSScene.getObject('.Unknown.zdt.MARKER_470')
relative_to = Jusme.ActiveUSScene.getObject('.Unknown.zdt')
MARKER_470.relative_to = relative_to
MARKER_470.marker_name = '.Unknown.zdt.MARKER_470'
_turn_zdt_cm = Jusme.ActiveUSScene.getObject('.Unknown.zdt.cm')
MARKER_470.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_zdt_cm))
_turn_ground_hsg_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.hsg_1').location
_turn_ground_zdt_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.zdt_1').location
MARKER_470.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hsg_1, _turn_ground_zdt_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_470.location, MARKER_470.orientation)
MARKER_470.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
MARKER_470.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


CYLINDER_214 = Jusme.ActiveUSScene.getObject('.Unknown.zdt.CYLINDER_214')
CYLINDER_214.cylinder_name = '.Unknown.zdt.CYLINDER_214'
_turn_ground_zdt_1 = Jusme.ActiveUSScene.getObject('.Unknown.ground.zdt_1').location
_turn_ground_zdt_2 = Jusme.ActiveUSScene.getObject('.Unknown.ground.zdt_2').location
CYLINDER_214.length = (VecUtils.DM(_turn_ground_zdt_1, _turn_ground_zdt_2))



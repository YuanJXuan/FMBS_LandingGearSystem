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
origo = MakeSceneNodeByType('Marker', '.turn.ground.origo')
origo.marker_name = '.turn.ground.origo'
origo.adams_id = 1
origo.location = Base.Vector (0.0, 0.0, 0.0)
origo.orientation = Base.Vector (0.0, 0.0, 0.0)
PART_46 = MakeSceneNodeByType('PartGeneral', '.turn.PART_46')
PART_46.part_name = '.turn.PART_46'
PART_46.adams_id = 46
PART_46.location = Base.Vector (-0.92679, 0.0, 0.5)
PART_46.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_433 = MakeSceneNodeByType('Marker', '.turn.PART_46.MARKER_433')
MARKER_433.marker_name = '.turn.PART_46.MARKER_433'
MARKER_433.adams_id = 433
MARKER_433.location = Base.Vector (11.550194959, 0.0, 2.1282477971)
MARKER_433.orientation = Base.Vector (0.0, 0.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.turn.PART_46.cm')
cm.marker_name = '.turn.PART_46.cm'
cm.adams_id = 438
cm.location = Base.Vector (11.550194959, 0.0, 2.1282477971)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
PART_46 = Jusme.ActiveUSScene.getObject('.turn.PART_46')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.PART_46.cm')
PART_46.center_of_mass_marker = center_of_mass_marker
PART_46.part_name = '.turn.PART_46'
PART_46.mass = 34246.223935
PART_46.ixx = 130707.0096
PART_46.iyy = 230707.0095
PART_46.izz = 130707.0095
PART_46.ixy = 0.0
PART_46.izx = 0.0
PART_46.iyz = 0.0
ELLIPSOID_156 = MakeSceneNodeByType('ShapeEllipsoid', '.turn.PART_46.ELLIPSOID_156')
center_marker = Jusme.ActiveUSScene.getObject('.turn.PART_46.MARKER_433')
ELLIPSOID_156.center_marker = center_marker
ELLIPSOID_156.ellipsoid_name = '.turn.PART_46.ELLIPSOID_156'
ELLIPSOID_156.adams_id = 150
ELLIPSOID_156.x_scale_factor = 0.2
ELLIPSOID_156.y_scale_factor = 0.2
ELLIPSOID_156.z_scale_factor = 0.2


_cv_part = MakeSceneNodeByType('PartGeneral', '.turn._cv_part')
_cv_part.part_name = '.turn._cv_part'
_cv_part.adams_id = 2
_cv_part.comments = '"Dummy for communicators"'
_cv_part.location = Base.Vector (0.0, 0.0, 0.0)
_cv_part.orientation = Base.Vector (0.0, 0.0, 0.0)
marker = MakeSceneNodeByType('Marker', '.turn._cv_part.marker')
marker.marker_name = '.turn._cv_part.marker'
marker.adams_id = 300
marker.comments = '"Dummy for communicators"'
marker.location = Base.Vector (0.0, 0.0, 0.0)
marker.orientation = Base.Vector (0.0, 0.0, 0.0)
_cv_part = Jusme.ActiveUSScene.getObject('.turn._cv_part')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn._cv_part.marker')
_cv_part.center_of_mass_marker = center_of_mass_marker
_cv_part.part_name = '.turn._cv_part'
_cv_part.mass = 0.0
_cv_part.ixx = 0.0
_cv_part.iyy = 0.0
_cv_part.izz = 0.0
_cv_part.ixy = 0.0
_cv_part.izx = 0.0
_cv_part.iyz = 0.0
gravity = MakeSceneNodeByType('Gravity', '.turn.gravity')
gravity.gravity_field_name = 'gravity'
gravity.z_component_gravity = -9.81


aluminum = Jusme.ActiveUSScene.getObject('.turn.aluminum')
aluminum.material_name = '.turn.aluminum'


steel = Jusme.ActiveUSScene.getObject('.turn.steel')
steel.material_name = '.turn.steel'


steel_2 = Jusme.ActiveUSScene.getObject('.turn.steel_2')
steel_2.material_name = '.turn.steel_2'


aluminum_2 = Jusme.ActiveUSScene.getObject('.turn.aluminum_2')
aluminum_2.material_name = '.turn.aluminum_2'


ELLIPSOID_156 = Jusme.ActiveUSScene.getObject('.turn.PART_46.ELLIPSOID_156')
ELLIPSOID_156.ellipsoid_name = '.turn.PART_46.ELLIPSOID_156'



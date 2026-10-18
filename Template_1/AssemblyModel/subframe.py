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
PART_46 = MakeSceneNodeByType('PartGeneral', '.Unknown.PART_46')
PART_46.part_name = '.Unknown.PART_46'
PART_46.adams_id = 46
PART_46.location = Base.Vector (-926.79, 0.0, 500.0)
PART_46.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_433 = MakeSceneNodeByType('Marker', '.Unknown.PART_46.MARKER_433')
MARKER_433.marker_name = '.Unknown.PART_46.MARKER_433'
MARKER_433.adams_id = 433
MARKER_433.location = Base.Vector (11550.194959, 0.0, 2128.2477971)
MARKER_433.orientation = Base.Vector (0.0, 0.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.Unknown.PART_46.cm')
cm.marker_name = '.Unknown.PART_46.cm'
cm.adams_id = 438
cm.location = Base.Vector (11550.194959, 0.0, 2128.2477971)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
PART_46 = Jusme.ActiveUSScene.getObject('.Unknown.PART_46')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.Unknown.PART_46.cm')
PART_46.center_of_mass_marker = center_of_mass_marker
PART_46.part_name = '.Unknown.PART_46'
PART_46.mass = 34246.223935
PART_46.ixx = 130707009600.0
PART_46.iyy = 230707009500.0
PART_46.izz = 130707009500.0
PART_46.ixy = 0.0
PART_46.izx = 0.0
PART_46.iyz = 0.0
ELLIPSOID_156 = MakeSceneNodeByType('ShapeEllipsoid', '.Unknown.PART_46.ELLIPSOID_156')
center_marker = Jusme.ActiveUSScene.getObject('.Unknown.PART_46.MARKER_433')
ELLIPSOID_156.center_marker = center_marker
ELLIPSOID_156.ellipsoid_name = '.Unknown.PART_46.ELLIPSOID_156'
ELLIPSOID_156.adams_id = 150
ELLIPSOID_156.x_scale_factor = 200.0
ELLIPSOID_156.y_scale_factor = 200.0
ELLIPSOID_156.z_scale_factor = 200.0


_cv_part = MakeSceneNodeByType('PartGeneral', '.Unknown._cv_part')
_cv_part.part_name = '.Unknown._cv_part'
_cv_part.adams_id = 2
_cv_part.comments = '"Dummy for communicators"'
_cv_part.location = Base.Vector (0.0, 0.0, 0.0)
_cv_part.orientation = Base.Vector (0.0, 0.0, 0.0)
marker = MakeSceneNodeByType('Marker', '.Unknown._cv_part.marker')
marker.marker_name = '.Unknown._cv_part.marker'
marker.adams_id = 300
marker.comments = '"Dummy for communicators"'
marker.location = Base.Vector (0.0, 0.0, 0.0)
marker.orientation = Base.Vector (0.0, 0.0, 0.0)
_cv_part = Jusme.ActiveUSScene.getObject('.Unknown._cv_part')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.Unknown._cv_part.marker')
_cv_part.center_of_mass_marker = center_of_mass_marker
_cv_part.part_name = '.Unknown._cv_part'
_cv_part.mass = 0.0
_cv_part.ixx = 0.0
_cv_part.iyy = 0.0
_cv_part.izz = 0.0
_cv_part.ixy = 0.0
_cv_part.izx = 0.0
_cv_part.iyz = 0.0
gravity = MakeSceneNodeByType('Gravity', '.Unknown.gravity')
gravity.gravity_field_name = 'gravity'
gravity.z_component_gravity = -9810.0


aluminum = Jusme.ActiveUSScene.getObject('.Unknown.aluminum')
aluminum.material_name = '.Unknown.aluminum'


steel = Jusme.ActiveUSScene.getObject('.Unknown.steel')
steel.material_name = '.Unknown.steel'


steel_2 = Jusme.ActiveUSScene.getObject('.Unknown.steel_2')
steel_2.material_name = '.Unknown.steel_2'


aluminum_2 = Jusme.ActiveUSScene.getObject('.Unknown.aluminum_2')
aluminum_2.material_name = '.Unknown.aluminum_2'


ELLIPSOID_156 = Jusme.ActiveUSScene.getObject('.Unknown.PART_46.ELLIPSOID_156')
ELLIPSOID_156.ellipsoid_name = '.Unknown.PART_46.ELLIPSOID_156'



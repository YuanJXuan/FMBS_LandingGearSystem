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
NLG_V = MakeSceneNodeByType('DataElementVariable', '.GCMB.NLG_V')
NLG_V.variable_name = '.GCMB.NLG_V'
NLG_V.adams_id = 115
NLG_V.initial_condition = 0.0
NLG_V.function = '""'
NLG_S = MakeSceneNodeByType('DataElementVariable', '.GCMB.NLG_S')
NLG_S.variable_name = '.GCMB.NLG_S'
NLG_S.adams_id = 120
NLG_S.initial_condition = 0.0
NLG_S.function = '""'
x1 = MakeSceneNodeByType('DataElementVariable', '.GCMB.x1')
x1.variable_name = '.GCMB.x1'
x1.adams_id = 121
x1.initial_condition = 0.0
x1.function = '""'
x2 = MakeSceneNodeByType('DataElementVariable', '.GCMB.x2')
x2.variable_name = '.GCMB.x2'
x2.adams_id = 122
x2.initial_condition = 0.0
x2.function = '""'
VARIABLE_123 = MakeSceneNodeByType('DataElementVariable', '.GCMB.VARIABLE_123')
VARIABLE_123.variable_name = '.GCMB.VARIABLE_123'
VARIABLE_123.adams_id = 123
VARIABLE_123.initial_condition = 0.0
VARIABLE_123.function = '""'
VARIABLE_124 = MakeSceneNodeByType('DataElementVariable', '.GCMB.VARIABLE_124')
VARIABLE_124.variable_name = '.GCMB.VARIABLE_124'
VARIABLE_124.adams_id = 124
VARIABLE_124.initial_condition = 0.0
VARIABLE_124.function = '""'
_cv_solver_variable = MakeSceneNodeByType('DataElementVariable', '.GCMB._cv_solver_variable')
_cv_solver_variable.variable_name = '.GCMB._cv_solver_variable'
_cv_solver_variable.adams_id = 1
_cv_solver_variable.comments = '"Dummy for communicators"'
_cv_solver_variable.function = '""'
SPLINE_airspring = MakeSceneNodeByType('Spline', '.GCMB.SPLINE_airspring')
SPLINE_airspring.spline_name = '.GCMB.SPLINE_airspring'
SPLINE_airspring.adams_id = 4
SPLINE_airspring.x = [-127.0, -101.6, -76.2, -50.8, -25.4, 0.0, 25.4, 50.8, 76.2, 101.6, 127.0, 152.4, 177.8, 203.2, 228.6, 254.0, 279.4, 304.8, 330.2, 355.6, 381.0, 406.4, 431.8, 457.2, 482.6]
SPLINE_airspring.y = [71171.545844, 71171.545844, 71171.545844, 71171.545844, 71171.545844, 71171.545844, 72061.190167, 74730.123136, 79178.344752, 85405.855013, 93412.65392, 103198.74147, 114764.11767, 128108.78252, 143232.73601, 160135.97815, 178818.50893, 199280.32836, 221521.43644, 245541.83316, 271341.51853, 298920.49255, 328278.75521, 359416.30651, 400339.94537]
SPLINE_airspring.linear_extrapolate = False
SPLINE_airspring.x_units = '"length"'
SPLINE_airspring.y_units = '"force"'
SPLINE_stopper = MakeSceneNodeByType('Spline', '.GCMB.SPLINE_stopper')
SPLINE_stopper.spline_name = '.GCMB.SPLINE_stopper'
SPLINE_stopper.adams_id = 3
SPLINE_stopper.x = [0.0, 0.00254, 0.00508, 0.00762, 0.01016, 0.0127, 0.01524, 0.01778, 0.02032, 0.02286, 0.0254, 0.02794, 0.03048, 0.03302, 0.03556, 0.0381, 0.04064, 0.04318, 0.04572, 0.04826, 0.0508, 0.05334, 0.05588, 0.05842, 0.06096, 0.0635, 0.06604, 0.06858, 0.07112, 0.07366, 0.0762, 0.07874, 0.08128, 0.08382, 0.08636, 0.0889, 0.09144, 0.09398, 0.09652, 0.09906, 0.1016, 0.10414, 0.10668, 0.10922, 0.11176, 0.1143, 0.11684, 0.11938, 0.12192, 0.12446, 0.127, 0.12954, 0.13208, 0.13462, 0.13716, 0.1397, 0.14224, 0.14478, 0.14732, 0.14986, 0.1524, 0.15494, 0.15748, 0.16002, 0.16256, 0.1651, 0.16764, 0.17018, 0.17272, 0.17526, 0.1778, 0.18034, 0.18288, 0.18542, 0.18796, 0.1905, 0.19304, 0.19558, 0.19812, 0.20066, 0.2032, 0.20574, 0.20828, 0.21082, 0.21336, 0.2159, 0.21844, 0.22098, 0.22352, 0.22606, 0.2286, 0.23114, 0.23368, 0.23622, 0.23876, 0.2413, 0.24384, 0.24638, 0.24892, 0.25146, 0.254, 0.508, 0.762, 1.016, 1.27, 1.524, 1.778, 2.032, 2.286, 2.54, 5.08, 7.62, 10.16, 12.7, 15.24, 17.78, 20.32, 22.86, 25.4, 50.8, 76.2, 101.6, 127.0, 152.4, 177.8, 203.2, 228.6, 254.0]
SPLINE_stopper.y = [0.0, 44.4822161526, 105.7971256484, 175.6256644225, 251.6294023717, 332.5821427257, 417.7106066388, 506.4762924022, 598.4788600706, 693.4092472062, 791.0179085764, 891.1015604533, 993.4889463047, 1098.0337196395, 1204.609995786, 1313.1083484925, 1423.4309168834, 1535.4922951036, 1649.2141944529, 1764.527222674, 1881.368659842, 1999.6802342539, 2119.4090120724, 2240.5065076819, 2362.9277940442, 2486.6315026981, 2611.5784892935, 2737.7331680574, 2865.0612876834, 2993.5321554424, 3123.1150786052, 3253.7824781978, 3385.5081097127, 3518.2675079309, 3652.0362076337, 3786.7919677129, 3922.514326349, 4059.1823769006, 4196.7769920147, 4335.2799339826, 4474.6751892065, 4614.9409614005, 4756.0696885878, 4898.0346814389, 5040.831491732, 5184.4423265806, 5328.8538413201, 5474.0482430638, 5620.0210835902, 5766.7545700128, 5914.2398058884, 6062.4634465521, 6211.4165955607, 6361.0859082494, 6511.4624881749, 6662.5374388939, 6814.3018639634, 6966.74686694, 7119.8591031589, 7273.6341243984, 7428.0630342154, 7583.132487945, 7738.8424855872, 7895.1796824772, 8052.1396303932, 8209.7134328922, 8367.8966417525, 8526.6803605309, 8686.055692784, 8846.0181902904, 9006.5589566068, 9167.6779917331, 9329.3619510046, 9491.6108344212, 9654.4157455398, 9817.7722361386, 9981.6758579961, 10146.117715, 10311.093358, 10476.59834, 10642.628211, 10809.178525, 10976.244833, 11143.818237, 11311.898739, 11480.48189, 11649.558794, 11819.12945, 11989.189411, 12159.729779, 12330.750555, 12502.247292, 12674.219987, 12846.655298, 13019.557673, 13192.918214, 13366.736921, 13541.009348, 13715.731045, 13890.902012, 14066.513353, 33455.991102, 55537.692709, 79572.190293, 105171.70569, 132091.67567, 160161.82232, 189255.68268, 219275.21797, 250141.87258, 594941.18942, 987615.51448, 1415016.2161, 1870246.7713, 2348959.4885, 2848124.6839, 3365494.671, 3899326.1919, 4448221.6153, 10579712.565, 17562566.442, 25162940.237, 33258214.273, 41771056.216, 50647629.24, 59847886.007, 69340924.721, 79101790.858]
SPLINE_stopper.linear_extrapolate = False
SPLINE_stopper.x_units = '"length"'
SPLINE_stopper.y_units = '"force"'
_cv_spline = MakeSceneNodeByType('Spline', '.GCMB._cv_spline')
_cv_spline.spline_name = '.GCMB._cv_spline'
_cv_spline.adams_id = 1
_cv_spline.comments = '"Dummy for communicators"'
_cv_spline.x = [1.0, 2.0, 3.0, 4.0]
_cv_spline.y = [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0]
_cv_spline.z = [1.0, 2.0]
_cv_spline.linear_extrapolate = False
airspring = MakeSceneNodeByType('Spline', '.GCMB.airspring')
airspring.spline_name = '.GCMB.airspring'
airspring.adams_id = 2
airspring.x = [-127.0, -101.6, -76.2, -50.8, -25.4, 0.0, 25.4, 50.8, 76.2, 101.6, 127.0, 152.4, 177.8, 203.2, 228.6, 254.0, 279.4, 304.8, 330.2, 355.6, 381.0, 406.4, 431.8, 457.2, 482.6, 508.0, 533.4]
airspring.y = [17792.886461, 17792.886461, 17792.886461, 17792.886461, 17792.886461, 17792.886461, 18015.297542, 18682.530784, 19794.586188, 21351.463753, 23353.16348, 25799.685369, 28691.029418, 32027.19563, 35808.184003, 40033.994537, 44704.627233, 49820.082091, 55380.35911, 61385.458291, 67835.379633, 74730.123136, 82069.688802, 89854.076628, 97860.875536, 106757.31877, 116543.40632]
airspring.linear_extrapolate = False
airspring.x_units = '"length"'
airspring.y_units = '"force"'
stopper = MakeSceneNodeByType('Spline', '.GCMB.stopper')
stopper.spline_name = '.GCMB.stopper'
stopper.adams_id = 5
stopper.x = [0.0, 0.00254, 0.00508, 0.00762, 0.01016, 0.0127, 0.01524, 0.01778, 0.02032, 0.02286, 0.0254, 0.02794, 0.03048, 0.03302, 0.03556, 0.0381, 0.04064, 0.04318, 0.04572, 0.04826, 0.0508, 0.05334, 0.05588, 0.05842, 0.06096, 0.0635, 0.06604, 0.06858, 0.07112, 0.07366, 0.0762, 0.07874, 0.08128, 0.08382, 0.08636, 0.0889, 0.09144, 0.09398, 0.09652, 0.09906, 0.1016, 0.10414, 0.10668, 0.10922, 0.11176, 0.1143, 0.11684, 0.11938, 0.12192, 0.12446, 0.127, 0.12954, 0.13208, 0.13462, 0.13716, 0.1397, 0.14224, 0.14478, 0.14732, 0.14986, 0.1524, 0.15494, 0.15748, 0.16002, 0.16256, 0.1651, 0.16764, 0.17018, 0.17272, 0.17526, 0.1778, 0.18034, 0.18288, 0.18542, 0.18796, 0.1905, 0.19304, 0.19558, 0.19812, 0.20066, 0.2032, 0.20574, 0.20828, 0.21082, 0.21336, 0.2159, 0.21844, 0.22098, 0.22352, 0.22606, 0.2286, 0.23114, 0.23368, 0.23622, 0.23876, 0.2413, 0.24384, 0.24638, 0.24892, 0.25146, 0.254, 0.508, 0.762, 1.016, 1.27, 1.524, 1.778, 2.032, 2.286, 2.54, 5.08, 7.62, 10.16, 12.7, 15.24, 17.78, 20.32, 22.86, 25.4, 50.8, 76.2, 101.6, 127.0, 152.4, 177.8, 203.2, 228.6, 254.0]
stopper.y = [0.0, 44.4822161526, 105.7971256484, 175.6256644225, 251.6294023717, 332.5821427257, 417.7106066388, 506.4762924022, 598.4788600706, 693.4092472062, 791.0179085764, 891.1015604533, 993.4889463047, 1098.0337196395, 1204.609995786, 1313.1083484925, 1423.4309168834, 1535.4922951036, 1649.2141944529, 1764.527222674, 1881.368659842, 1999.6802342539, 2119.4090120724, 2240.5065076819, 2362.9277940442, 2486.6315026981, 2611.5784892935, 2737.7331680574, 2865.0612876834, 2993.5321554424, 3123.1150786052, 3253.7824781978, 3385.5081097127, 3518.2675079309, 3652.0362076337, 3786.7919677129, 3922.514326349, 4059.1823769006, 4196.7769920147, 4335.2799339826, 4474.6751892065, 4614.9409614005, 4756.0696885878, 4898.0346814389, 5040.831491732, 5184.4423265806, 5328.8538413201, 5474.0482430638, 5620.0210835902, 5766.7545700128, 5914.2398058884, 6062.4634465521, 6211.4165955607, 6361.0859082494, 6511.4624881749, 6662.5374388939, 6814.3018639634, 6966.74686694, 7119.8591031589, 7273.6341243984, 7428.0630342154, 7583.132487945, 7738.8424855872, 7895.1796824772, 8052.1396303932, 8209.7134328922, 8367.8966417525, 8526.6803605309, 8686.055692784, 8846.0181902904, 9006.5589566068, 9167.6779917331, 9329.3619510046, 9491.6108344212, 9654.4157455398, 9817.7722361386, 9981.6758579961, 10146.117715, 10311.093358, 10476.59834, 10642.628211, 10809.178525, 10976.244833, 11143.818237, 11311.898739, 11480.48189, 11649.558794, 11819.12945, 11989.189411, 12159.729779, 12330.750555, 12502.247292, 12674.219987, 12846.655298, 13019.557673, 13192.918214, 13366.736921, 13541.009348, 13715.731045, 13890.902012, 14066.513353, 33455.991102, 55537.692709, 79572.190293, 105171.70569, 132091.67567, 160161.82232, 189255.68268, 219275.21797, 250141.87258, 594941.18942, 987615.51448, 1415016.2161, 1870246.7713, 2348959.4885, 2848124.6839, 3365494.671, 3899326.1919, 4448221.6153, 10579712.565, 17562566.442, 25162940.237, 33258214.273, 41771056.216, 50647629.24, 59847886.007, 69340924.721, 79101790.858]
stopper.linear_extrapolate = False
stopper.x_units = '"length"'
stopper.y_units = '"force"'
aluminum = MakeSceneNodeByType('MaterialCreate', '.GCMB.aluminum')
aluminum.material_name = '.GCMB.aluminum'
aluminum.adams_id = 2
aluminum.density = 2.74e-06
aluminum.youngs_modulus = 71705.0
aluminum.poissons_ratio = 0.33
steel = MakeSceneNodeByType('MaterialCreate', '.GCMB.steel')
steel.material_name = '.GCMB.steel'
steel.adams_id = 5
steel.density = 7.801e-06
steel.youngs_modulus = 207000.0
steel.poissons_ratio = 0.29
steel_2 = MakeSceneNodeByType('MaterialCreate', '.GCMB.steel_2')
steel_2.material_name = '.GCMB.steel_2'
steel_2.adams_id = 3
steel_2.density = 7.801e-06
steel_2.youngs_modulus = 207000.0
steel_2.poissons_ratio = 0.29
aluminum_2 = MakeSceneNodeByType('MaterialCreate', '.GCMB.aluminum_2')
aluminum_2.material_name = '.GCMB.aluminum_2'
aluminum_2.adams_id = 4
aluminum_2.density = 2.74e-06
aluminum_2.youngs_modulus = 71705.0
aluminum_2.poissons_ratio = 0.33
ground = Jusme.ActiveUSScene.getObject('.GCMB.ground')
ground.part_name = 'ground'
origo = MakeSceneNodeByType('Marker', '.GCMB.ground.origo')
origo.marker_name = '.GCMB.ground.origo'
origo.adams_id = 1
origo.location = Base.Vector (0.0, 0.0, 0.0)
origo.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_gearaero_origin_1 = MakeSceneNodeByType('Marker', '.GCMB.ground.uel_gearaero_origin_1')
uel_gearaero_origin_1.marker_name = '.GCMB.ground.uel_gearaero_origin_1'
uel_gearaero_origin_1.adams_id = 45
uel_gearaero_origin_1.location = Base.Vector (0.0, 0.0, 0.0)
uel_gearaero_origin_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_gearaero_origin_1 = MakeSceneNodeByType('Marker', '.GCMB.ground.uer_gearaero_origin_1')
uer_gearaero_origin_1.marker_name = '.GCMB.ground.uer_gearaero_origin_1'
uer_gearaero_origin_1.adams_id = 47
uer_gearaero_origin_1.location = Base.Vector (0.0, 0.0, 0.0)
uer_gearaero_origin_1.orientation = Base.Vector (0.0, 0.0, 0.0)
lumian_ref_1 = MakeSceneNodeByType('Marker', '.GCMB.ground.lumian_ref_1')
lumian_ref_1.marker_name = '.GCMB.ground.lumian_ref_1'
lumian_ref_1.adams_id = 239
lumian_ref_1.location = Base.Vector (12238.367977, 1509.5002745, -560.8546166)
lumian_ref_1.orientation = Base.Vector (0.0, 0.0, 0.0)
origo1 = MakeSceneNodeByType('Marker', '.GCMB.ground.origo1')
origo1.marker_name = '.GCMB.ground.origo1'
origo1.adams_id = 287
origo1.location = Base.Vector (0.0, 0.0, 0.0)
origo1.orientation = Base.Vector (0.0, 0.0, 0.0)
cfs_uc_sf_atch_mid = MakeSceneNodeByType('Marker', '.GCMB.ground.cfs_uc_sf_atch_mid')
cfs_uc_sf_atch_mid.marker_name = '.GCMB.ground.cfs_uc_sf_atch_mid'
cfs_uc_sf_atch_mid.adams_id = 289
cfs_uc_sf_atch_mid.location = Base.Vector (6314.44, 0.0, 1691.64)
cfs_uc_sf_atch_mid.orientation = Base.Vector (0.0, 90.0, 0.0)
cfs_subframe_to_body_point = MakeSceneNodeByType('Marker', '.GCMB.ground.cfs_subframe_to_body_point')
cfs_subframe_to_body_point.marker_name = '.GCMB.ground.cfs_subframe_to_body_point'
cfs_subframe_to_body_point.adams_id = 290
cfs_subframe_to_body_point.location = Base.Vector (6704.33, 0.0, 1668.78)
cfs_subframe_to_body_point.orientation = Base.Vector (0.0, 90.0, 356.6444799092)
cfl_spin_axis1 = MakeSceneNodeByType('Marker', '.GCMB.ground.cfl_spin_axis1')
cfl_spin_axis1.marker_name = '.GCMB.ground.cfl_spin_axis1'
cfl_spin_axis1.adams_id = 292
cfl_spin_axis1.location = Base.Vector (6229.096, -209.55, 308.0)
cfl_spin_axis1.orientation = Base.Vector (0.0, 90.0, 0.0)
cfr_spin_axis1 = MakeSceneNodeByType('Marker', '.GCMB.ground.cfr_spin_axis1')
cfr_spin_axis1.marker_name = '.GCMB.ground.cfr_spin_axis1'
cfr_spin_axis1.adams_id = 293
cfr_spin_axis1.location = Base.Vector (6229.096, 209.55, 308.0)
cfr_spin_axis1.orientation = Base.Vector (180.0, 90.0, 180.0)
cfs_wheel_centers_midpoint = MakeSceneNodeByType('Marker', '.GCMB.ground.cfs_wheel_centers_midpoint')
cfs_wheel_centers_midpoint.marker_name = '.GCMB.ground.cfs_wheel_centers_midpoint'
cfs_wheel_centers_midpoint.adams_id = 294
cfs_wheel_centers_midpoint.location = Base.Vector (6229.096, 0.0, 508.0)
cfs_wheel_centers_midpoint.orientation = Base.Vector (0.0, 0.0, 0.0)
cfs_nlg_axle_lowpoint = MakeSceneNodeByType('Marker', '.GCMB.ground.cfs_nlg_axle_lowpoint')
cfs_nlg_axle_lowpoint.marker_name = '.GCMB.ground.cfs_nlg_axle_lowpoint'
cfs_nlg_axle_lowpoint.adams_id = 295
cfs_nlg_axle_lowpoint.location = Base.Vector (6229.096, 0.0, 482.6)
cfs_nlg_axle_lowpoint.orientation = Base.Vector (0.0, 0.0, 0.0)
cfs_collar_top = MakeSceneNodeByType('Marker', '.GCMB.ground.cfs_collar_top')
cfs_collar_top.marker_name = '.GCMB.ground.cfs_collar_top'
cfs_collar_top.adams_id = 296
cfs_collar_top.location = Base.Vector (6197.6, 0.0, 856.996)
cfs_collar_top.orientation = Base.Vector (0.0, 0.0, 0.0)
lumian_ref_11 = MakeSceneNodeByType('Marker', '.GCMB.ground.lumian_ref_11')
lumian_ref_11.marker_name = '.GCMB.ground.lumian_ref_11'
lumian_ref_11.adams_id = 297
lumian_ref_11.location = Base.Vector (7484.11, 0.0, 48.26)
lumian_ref_11.orientation = Base.Vector (0.0, 0.0, 0.0)
luntai1_tire_jf_11 = MakeSceneNodeByType('Marker', '.GCMB.ground.luntai1_tire_jf_11')
luntai1_tire_jf_11.is_floating = True
luntai1_tire_jf_11.floating_marker_name = '.GCMB.ground.luntai1_tire_jf_11'
luntai1_tire_jf_11.adams_id = 298
luntai2_tire_jf_11 = MakeSceneNodeByType('Marker', '.GCMB.ground.luntai2_tire_jf_11')
luntai2_tire_jf_11.is_floating = True
luntai2_tire_jf_11.floating_marker_name = '.GCMB.ground.luntai2_tire_jf_11'
luntai2_tire_jf_11.adams_id = 299
hps_db_sf_atch = MakeSceneNodeByType('Point', '.GCMB.ground.hps_db_sf_atch')
hps_db_sf_atch.point_name = '.GCMB.ground.hps_db_sf_atch'
hps_db_sf_atch.location = Base.Vector (7484.11, 0.0, 1623.06)
hps_uc_sf_atch_l = MakeSceneNodeByType('Point', '.GCMB.ground.hps_uc_sf_atch_l')
hps_uc_sf_atch_l.point_name = '.GCMB.ground.hps_uc_sf_atch_l'
hps_uc_sf_atch_l.location = Base.Vector (6314.44, -340.36, 1691.64)
hps_uc_sf_atch_r = MakeSceneNodeByType('Point', '.GCMB.ground.hps_uc_sf_atch_r')
hps_uc_sf_atch_r.point_name = '.GCMB.ground.hps_uc_sf_atch_r'
hps_uc_sf_atch_r.location = Base.Vector (6314.44, 340.36, 1691.64)
hps_lc_bot = MakeSceneNodeByType('Point', '.GCMB.ground.hps_lc_bot')
hps_lc_bot.point_name = '.GCMB.ground.hps_lc_bot'
hps_lc_bot.location = Base.Vector (6197.6, 0.0, 308.0)
hps_uc_top = MakeSceneNodeByType('Point', '.GCMB.ground.hps_uc_top')
hps_uc_top.point_name = '.GCMB.ground.hps_uc_top'
hps_uc_top.location = Base.Vector (6197.6, 0.0, 1625.6)
hps_db_uc_atch = MakeSceneNodeByType('Point', '.GCMB.ground.hps_db_uc_atch')
hps_db_uc_atch.point_name = '.GCMB.ground.hps_db_uc_atch'
hps_db_uc_atch.location = Base.Vector (6451.6, 0.0, 1016.0)
hps_uta_uc_atch = MakeSceneNodeByType('Point', '.GCMB.ground.hps_uta_uc_atch')
hps_uta_uc_atch.point_name = '.GCMB.ground.hps_uta_uc_atch'
hps_uta_uc_atch.location = Base.Vector (6324.6, 0.0, 838.2)
hps_lta_lc_atch = MakeSceneNodeByType('Point', '.GCMB.ground.hps_lta_lc_atch')
hps_lta_lc_atch.point_name = '.GCMB.ground.hps_lta_lc_atch'
hps_lta_lc_atch.location = Base.Vector (6299.2, 0.0, 333.4)
hps_lta_uta_atch = MakeSceneNodeByType('Point', '.GCMB.ground.hps_lta_uta_atch')
hps_lta_uta_atch.point_name = '.GCMB.ground.hps_lta_uta_atch'
hps_lta_uta_atch.location = Base.Vector (6654.8, 0.0, 611.2)
hps_uc_geompt = MakeSceneNodeByType('Point', '.GCMB.ground.hps_uc_geompt')
hps_uc_geompt.point_name = '.GCMB.ground.hps_uc_geompt'
hps_uc_geompt.location = Base.Vector (6197.6, 0.0, 1473.2)
hps_uc_bot = MakeSceneNodeByType('Point', '.GCMB.ground.hps_uc_bot')
hps_uc_bot.point_name = '.GCMB.ground.hps_uc_bot'
hps_uc_bot.location = Base.Vector (6197.6, 0.0, 762.0)
hps_lc_top = MakeSceneNodeByType('Point', '.GCMB.ground.hps_lc_top')
hps_lc_top.point_name = '.GCMB.ground.hps_lc_top'
hps_lc_top.location = Base.Vector (6197.6, 0.0, 1197.0)
hps_origin_reference = MakeSceneNodeByType('Point', '.GCMB.ground.hps_origin_reference')
hps_origin_reference.point_name = '.GCMB.ground.hps_origin_reference'
hps_origin_reference.location = Base.Vector (0.0, 0.0, 0.0)
hps_lb_uc_atch = MakeSceneNodeByType('Point', '.GCMB.ground.hps_lb_uc_atch')
hps_lb_uc_atch.point_name = '.GCMB.ground.hps_lb_uc_atch'
hps_lb_uc_atch.location = Base.Vector (6021.578, 0.0, 795.02)
hpl_wheel_center1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_wheel_center1')
hpl_wheel_center1.point_name = '.GCMB.ground.hpl_wheel_center1'
hpl_wheel_center1.location = Base.Vector (6229.096, -209.55, 308.0)
hpr_wheel_center1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpr_wheel_center1')
hpr_wheel_center1.point_name = '.GCMB.ground.hpr_wheel_center1'
hpr_wheel_center1.location = Base.Vector (6229.096, 209.55, 308.0)
hpl_ob_axle1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpl_ob_axle1')
hpl_ob_axle1.point_name = '.GCMB.ground.hpl_ob_axle1'
hpl_ob_axle1.location = Base.Vector (6229.096, -285.75, 308.0)
hpr_ob_axle1 = MakeSceneNodeByType('Point', '.GCMB.ground.hpr_ob_axle1')
hpr_ob_axle1.point_name = '.GCMB.ground.hpr_ob_axle1'
hpr_ob_axle1.location = Base.Vector (6229.096, 285.75, 308.0)
hps_nlg_axle_lowpoint = MakeSceneNodeByType('Point', '.GCMB.ground.hps_nlg_axle_lowpoint')
hps_nlg_axle_lowpoint.point_name = '.GCMB.ground.hps_nlg_axle_lowpoint'
hps_nlg_axle_lowpoint.location = Base.Vector (6229.096, 0.0, 482.6)
_cv_part = MakeSceneNodeByType('PartGeneral', '.GCMB._cv_part')
_cv_part.part_name = '.GCMB._cv_part'
_cv_part.adams_id = 2
_cv_part.comments = '"Dummy for communicators"'
_cv_part.location = Base.Vector (0.0, 0.0, 0.0)
_cv_part.orientation = Base.Vector (0.0, 0.0, 0.0)
marker = MakeSceneNodeByType('Marker', '.GCMB._cv_part.marker')
marker.marker_name = '.GCMB._cv_part.marker'
marker.adams_id = 300
marker.comments = '"Dummy for communicators"'
marker.location = Base.Vector (0.0, 0.0, 0.0)
marker.orientation = Base.Vector (0.0, 0.0, 0.0)
_cv_part = Jusme.ActiveUSScene.getObject('.GCMB._cv_part')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB._cv_part.marker')
_cv_part.center_of_mass_marker = center_of_mass_marker
_cv_part.part_name = '.GCMB._cv_part'
_cv_part.mass = 0.0
_cv_part.ixx = 0.0
_cv_part.iyy = 0.0
_cv_part.izz = 0.0
_cv_part.ixy = 0.0
_cv_part.izx = 0.0
_cv_part.iyz = 0.0
ges_dragbrace = MakeSceneNodeByType('PartGeneral', '.GCMB.ges_dragbrace')
ges_dragbrace.part_name = '.GCMB.ges_dragbrace'
ges_dragbrace.adams_id = 33
ges_dragbrace.location = Base.Vector (6967.855, 0.0, 1319.53)
ges_dragbrace.orientation = Base.Vector (270.0, 120.4532239091, 90.0)
MARKER_429 = MakeSceneNodeByType('Marker', '.GCMB.ges_dragbrace.MARKER_429')
MARKER_429.marker_name = '.GCMB.ges_dragbrace.MARKER_429'
MARKER_429.adams_id = 429
MARKER_429.location = Base.Vector (-4.5918824298e-10, 0.0, -598.873681109)
MARKER_429.orientation = Base.Vector (90.0, 120.4532239091, 270.0)
cm = MakeSceneNodeByType('Marker', '.GCMB.ges_dragbrace.cm')
cm.marker_name = '.GCMB.ges_dragbrace.cm'
cm.adams_id = 301
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.ges_dragbrace.inertia_frame')
inertia_frame.marker_name = '.GCMB.ges_dragbrace.inertia_frame'
inertia_frame.adams_id = 302
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_dragbrace.gralin_1')
gralin_1.marker_name = '.GCMB.ges_dragbrace.gralin_1'
gralin_1.adams_id = 303
gralin_1.location = Base.Vector (-4.5852210917e-10, 0.0, -598.873681109)
gralin_1.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_i_12 = MakeSceneNodeByType('Marker', '.GCMB.ges_dragbrace.jxs_joint_i_12')
jxs_joint_i_12.marker_name = '.GCMB.ges_dragbrace.jxs_joint_i_12'
jxs_joint_i_12.adams_id = 304
jxs_joint_i_12.location = Base.Vector (4.5791148651e-10, 0.0, 598.873681109)
jxs_joint_i_12.orientation = Base.Vector (90.0, 120.4532239091, 270.0)
ges_dragbrace = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.cm')
ges_dragbrace.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.inertia_frame')
ges_dragbrace.inertia_marker = inertia_marker
ges_dragbrace.part_name = '.GCMB.ges_dragbrace'
ges_dragbrace.mass = 27.3726690382
ges_dragbrace.ixx = 3481154.0175
ges_dragbrace.iyy = 3481154.0175
ges_dragbrace.izz = 35319.502313
ges_dragbrace.ixy = 0.0
ges_dragbrace.izx = 0.0
ges_dragbrace.iyz = 0.0
gralin_dragbrace_geom = MakeSceneNodeByType('ShapeCylinder', '.GCMB.ges_dragbrace.gralin_dragbrace_geom')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.gralin_1')
gralin_dragbrace_geom.center_marker = center_marker
gralin_dragbrace_geom.cylinder_name = '.GCMB.ges_dragbrace.gralin_dragbrace_geom'
gralin_dragbrace_geom.adams_id = 85
gralin_dragbrace_geom.angle_extent = 360.0
gralin_dragbrace_geom.length = 1197.7473622179
gralin_dragbrace_geom.radius = 50.8
gralin_dragbrace_geom.side_count_for_body = 15
gralin_dragbrace_geom.segment_count_for_ends = 15


ges_upper_cylinder = MakeSceneNodeByType('PartGeneral', '.GCMB.ges_upper_cylinder')
ges_upper_cylinder.part_name = '.GCMB.ges_upper_cylinder'
ges_upper_cylinder.adams_id = 34
ges_upper_cylinder.location = Base.Vector (6197.6, 0.0, 1193.8)
ges_upper_cylinder.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_405 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.MARKER_405')
MARKER_405.marker_name = '.GCMB.ges_upper_cylinder.MARKER_405'
MARKER_405.adams_id = 405
MARKER_405.location = Base.Vector (0.0, 0.0, -431.8)
MARKER_405.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_407 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.MARKER_407')
MARKER_407.marker_name = '.GCMB.ges_upper_cylinder.MARKER_407'
MARKER_407.adams_id = 407
MARKER_407.location = Base.Vector (0.0, 0.0, -431.8)
MARKER_407.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_409 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.MARKER_409')
MARKER_409.marker_name = '.GCMB.ges_upper_cylinder.MARKER_409'
MARKER_409.adams_id = 409
MARKER_409.location = Base.Vector (0.0, 0.0, -431.8)
MARKER_409.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_428 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.MARKER_428')
MARKER_428.marker_name = '.GCMB.ges_upper_cylinder.MARKER_428'
MARKER_428.adams_id = 428
MARKER_428.location = Base.Vector (0.0, 0.0, -431.8)
MARKER_428.orientation = Base.Vector (180.0, 180.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.cm')
cm.marker_name = '.GCMB.ges_upper_cylinder.cm'
cm.adams_id = 306
cm.location = Base.Vector (-3.3167643494, 0.0, -13.3824231157)
cm.orientation = Base.Vector (90.0, 2.0673379194, 270.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.inertia_frame')
inertia_frame.marker_name = '.GCMB.ges_upper_cylinder.inertia_frame'
inertia_frame.adams_id = 307
inertia_frame.location = Base.Vector (-3.3167643494, 0.0, -13.3824231157)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_2 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.gralin_2')
gralin_2.marker_name = '.GCMB.ges_upper_cylinder.gralin_2'
gralin_2.adams_id = 308
gralin_2.location = Base.Vector (0.0, 0.0, -431.8)
gralin_2.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_3 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.gralin_3')
gralin_3.marker_name = '.GCMB.ges_upper_cylinder.gralin_3'
gralin_3.adams_id = 309
gralin_3.location = Base.Vector (-116.84, -340.36, -497.84)
gralin_3.orientation = Base.Vector (161.0534953105, 58.7414044414, 213.4869581747)
gralin_4 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.gralin_4')
gralin_4.marker_name = '.GCMB.ges_upper_cylinder.gralin_4'
gralin_4.adams_id = 310
gralin_4.location = Base.Vector (-116.84, 340.36, -497.84)
gralin_4.orientation = Base.Vector (18.9465046895, 58.7414044414, 326.5130418253)
jxs_joint_j_11 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.jxs_joint_j_11')
jxs_joint_j_11.marker_name = '.GCMB.ges_upper_cylinder.jxs_joint_j_11'
jxs_joint_j_11.adams_id = 311
jxs_joint_j_11.location = Base.Vector (0.0, 0.0, 114.3)
jxs_joint_j_11.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_j_12 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.jxs_joint_j_12')
jxs_joint_j_12.marker_name = '.GCMB.ges_upper_cylinder.jxs_joint_j_12'
jxs_joint_j_12.adams_id = 312
jxs_joint_j_12.location = Base.Vector (-254.0, 0.0, 177.8)
jxs_joint_j_12.orientation = Base.Vector (180.0, 180.0, 0.0)
ues_spring_j_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.ues_spring_j_1')
ues_spring_j_1.marker_name = '.GCMB.ges_upper_cylinder.ues_spring_j_1'
ues_spring_j_1.adams_id = 314
ues_spring_j_1.location = Base.Vector (0.0, 0.0, -431.8)
ues_spring_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_damper_j_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.ues_damper_j_1')
ues_damper_j_1.marker_name = '.GCMB.ges_upper_cylinder.ues_damper_j_1'
ues_damper_j_1.adams_id = 315
ues_damper_j_1.location = Base.Vector (0.0, 0.0, -431.8)
ues_damper_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_stopper_j_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.ues_stopper_j_1')
ues_stopper_j_1.marker_name = '.GCMB.ges_upper_cylinder.ues_stopper_j_1'
ues_stopper_j_1.adams_id = 316
ues_stopper_j_1.location = Base.Vector (0.0, 0.0, -431.8)
ues_stopper_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_j_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.jxs_joint_j_1')
jxs_joint_j_1.marker_name = '.GCMB.ges_upper_cylinder.jxs_joint_j_1'
jxs_joint_j_1.adams_id = 317
jxs_joint_j_1.location = Base.Vector (0.0, 0.0, 336.804)
jxs_joint_j_1.orientation = Base.Vector (180.0, 180.0, 0.0)
ues_actuator_j_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.ues_actuator_j_1')
ues_actuator_j_1.marker_name = '.GCMB.ges_upper_cylinder.ues_actuator_j_1'
ues_actuator_j_1.adams_id = 318
ues_actuator_j_1.location = Base.Vector (0.0, 0.0, 336.804)
ues_actuator_j_1.orientation = Base.Vector (180.0, 180.0, 0.0)
ues_actuator_j_4 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.ues_actuator_j_4')
ues_actuator_j_4.marker_name = '.GCMB.ges_upper_cylinder.ues_actuator_j_4'
ues_actuator_j_4.adams_id = 319
ues_actuator_j_4.location = Base.Vector (0.0, 0.0, 336.804)
ues_actuator_j_4.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_2 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.MARKER_2')
MARKER_2.marker_name = '.GCMB.ges_upper_cylinder.MARKER_2'
MARKER_2.adams_id = 2
MARKER_2.location = Base.Vector (0.0, 0.0, -431.8)
MARKER_2.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_116 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_cylinder.MARKER_116')
MARKER_116.marker_name = '.GCMB.ges_upper_cylinder.MARKER_116'
MARKER_116.adams_id = 324
MARKER_116.location = Base.Vector (0.0, 0.0, -431.8)
MARKER_116.orientation = Base.Vector (180.0, 180.0, 0.0)
ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.cm')
ges_upper_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.inertia_frame')
ges_upper_cylinder.inertia_marker = inertia_marker
ges_upper_cylinder.part_name = '.GCMB.ges_upper_cylinder'
ges_upper_cylinder.mass = 82.2524279101
ges_upper_cylinder.ixx = 2775904.0478
ges_upper_cylinder.iyy = 2616359.1859
ges_upper_cylinder.izz = 827290.47458
ges_upper_cylinder.ixy = 0.0
ges_upper_cylinder.izx = 70431.892224
ges_upper_cylinder.iyz = 0.0
gralin_upper_cylinder_geom1 = MakeSceneNodeByType('ShapeCylinder', '.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom1')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.gralin_2')
gralin_upper_cylinder_geom1.center_marker = center_marker
gralin_upper_cylinder_geom1.cylinder_name = '.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom1'
gralin_upper_cylinder_geom1.adams_id = 86
gralin_upper_cylinder_geom1.angle_extent = 360.0
gralin_upper_cylinder_geom1.length = 863.6
gralin_upper_cylinder_geom1.radius = 127.0
gralin_upper_cylinder_geom1.side_count_for_body = 15
gralin_upper_cylinder_geom1.segment_count_for_ends = 15


gralin_upper_cylinder_geom2 = MakeSceneNodeByType('ShapeCylinder', '.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom2')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.gralin_3')
gralin_upper_cylinder_geom2.center_marker = center_marker
gralin_upper_cylinder_geom2.cylinder_name = '.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom2'
gralin_upper_cylinder_geom2.adams_id = 87
gralin_upper_cylinder_geom2.angle_extent = 360.0
gralin_upper_cylinder_geom2.length = 420.9662086201
gralin_upper_cylinder_geom2.radius = 25.4
gralin_upper_cylinder_geom2.side_count_for_body = 15
gralin_upper_cylinder_geom2.segment_count_for_ends = 15


gralin_upper_cylinder_geom3 = MakeSceneNodeByType('ShapeCylinder', '.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom3')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.gralin_4')
gralin_upper_cylinder_geom3.center_marker = center_marker
gralin_upper_cylinder_geom3.cylinder_name = '.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom3'
gralin_upper_cylinder_geom3.adams_id = 88
gralin_upper_cylinder_geom3.angle_extent = 360.0
gralin_upper_cylinder_geom3.length = 420.9662086201
gralin_upper_cylinder_geom3.radius = 25.4
gralin_upper_cylinder_geom3.side_count_for_body = 15
gralin_upper_cylinder_geom3.segment_count_for_ends = 15


ges_lower_cylinder = MakeSceneNodeByType('PartGeneral', '.GCMB.ges_lower_cylinder')
ges_lower_cylinder.part_name = '.GCMB.ges_lower_cylinder'
ges_lower_cylinder.adams_id = 35
ges_lower_cylinder.location = Base.Vector (6197.6, 0.0, 952.5)
ges_lower_cylinder.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_378 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_378')
MARKER_378.marker_name = '.GCMB.ges_lower_cylinder.MARKER_378'
MARKER_378.adams_id = 378
MARKER_378.location = Base.Vector (-101.6, 0.0, 619.1)
MARKER_378.orientation = Base.Vector (0.0, 90.0, 180.0)
MARKER_406 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_406')
MARKER_406.marker_name = '.GCMB.ges_lower_cylinder.MARKER_406'
MARKER_406.adams_id = 406
MARKER_406.location = Base.Vector (0.0, 0.0, -244.5)
MARKER_406.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_408 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_408')
MARKER_408.marker_name = '.GCMB.ges_lower_cylinder.MARKER_408'
MARKER_408.adams_id = 408
MARKER_408.location = Base.Vector (0.0, 0.0, -244.5)
MARKER_408.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_410 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_410')
MARKER_410.marker_name = '.GCMB.ges_lower_cylinder.MARKER_410'
MARKER_410.adams_id = 410
MARKER_410.location = Base.Vector (0.0, 0.0, -244.5)
MARKER_410.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_1')
MARKER_1.marker_name = '.GCMB.ges_lower_cylinder.MARKER_1'
MARKER_1.adams_id = 325
MARKER_1.location = Base.Vector (0.0, 0.0, -244.5)
MARKER_1.orientation = Base.Vector (180.0, 180.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.cm')
cm.marker_name = '.GCMB.ges_lower_cylinder.cm'
cm.adams_id = 326
cm.location = Base.Vector (-2.4871874502, 0.0, 34.7403924495)
cm.orientation = Base.Vector (270.0, 0.8125241803, 90.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.inertia_frame')
inertia_frame.marker_name = '.GCMB.ges_lower_cylinder.inertia_frame'
inertia_frame.adams_id = 327
inertia_frame.location = Base.Vector (-2.4871874502, 0.0, 34.7403924495)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_5 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.gralin_5')
gralin_5.marker_name = '.GCMB.ges_lower_cylinder.gralin_5'
gralin_5.adams_id = 328
gralin_5.location = Base.Vector (0.0, 0.0, -244.5)
gralin_5.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_i_11 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.jxs_joint_i_11')
jxs_joint_i_11.marker_name = '.GCMB.ges_lower_cylinder.jxs_joint_i_11'
jxs_joint_i_11.adams_id = 330
jxs_joint_i_11.location = Base.Vector (0.0, 0.0, -127.0)
jxs_joint_i_11.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_7 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.gralin_7')
gralin_7.marker_name = '.GCMB.ges_lower_cylinder.gralin_7'
gralin_7.adams_id = 331
gralin_7.location = Base.Vector (-31.496, 209.55, 644.5)
gralin_7.orientation = Base.Vector (0.0, 90.0, 0.0)
ues_spring_i_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.ues_spring_i_1')
ues_spring_i_1.marker_name = '.GCMB.ges_lower_cylinder.ues_spring_i_1'
ues_spring_i_1.adams_id = 332
ues_spring_i_1.location = Base.Vector (0.0, 0.0, -244.5)
ues_spring_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_damper_i_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.ues_damper_i_1')
ues_damper_i_1.marker_name = '.GCMB.ges_lower_cylinder.ues_damper_i_1'
ues_damper_i_1.adams_id = 51
ues_damper_i_1.location = Base.Vector (0.0, 0.0, -244.5)
ues_damper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_stopper_i_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.ues_stopper_i_1')
ues_stopper_i_1.marker_name = '.GCMB.ges_lower_cylinder.ues_stopper_i_1'
ues_stopper_i_1.adams_id = 333
ues_stopper_i_1.location = Base.Vector (0.0, 0.0, -244.5)
ues_stopper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
coomarker_2 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.coomarker_2')
coomarker_2.marker_name = '.GCMB.ges_lower_cylinder.coomarker_2'
coomarker_2.adams_id = 334
coomarker_2.location = Base.Vector (-31.496, 0.0, 444.5)
coomarker_2.orientation = Base.Vector (180.0, 180.0, 0.0)
coomarker_3 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.coomarker_3')
coomarker_3.marker_name = '.GCMB.ges_lower_cylinder.coomarker_3'
coomarker_3.adams_id = 335
coomarker_3.location = Base.Vector (-31.496, 0.0, 469.9)
coomarker_3.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_3 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_3')
MARKER_3.marker_name = '.GCMB.ges_lower_cylinder.MARKER_3'
MARKER_3.adams_id = 336
MARKER_3.location = Base.Vector (-31.496, -209.55, 644.5)
MARKER_3.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_4 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_4')
MARKER_4.marker_name = '.GCMB.ges_lower_cylinder.MARKER_4'
MARKER_4.adams_id = 337
MARKER_4.location = Base.Vector (-31.496, 209.55, 644.5)
MARKER_4.orientation = Base.Vector (180.0, 180.0, 0.0)
MARKER_6 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_6')
MARKER_6.marker_name = '.GCMB.ges_lower_cylinder.MARKER_6'
MARKER_6.adams_id = 338
MARKER_6.location = Base.Vector (-31.496, 209.55, 644.5)
MARKER_6.orientation = Base.Vector (0.0, 90.0, 180.0)
MARKER_8 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_8')
MARKER_8.marker_name = '.GCMB.ges_lower_cylinder.MARKER_8'
MARKER_8.adams_id = 339
MARKER_8.location = Base.Vector (-31.496, -209.55, 644.5)
MARKER_8.orientation = Base.Vector (0.0, 90.0, 180.0)
MARKER_115 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_cylinder.MARKER_115')
MARKER_115.marker_name = '.GCMB.ges_lower_cylinder.MARKER_115'
MARKER_115.adams_id = 344
MARKER_115.location = Base.Vector (0.0, 0.0, -444.5)
MARKER_115.orientation = Base.Vector (180.0, 180.0, 0.0)
ges_lower_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.cm')
ges_lower_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.inertia_frame')
ges_lower_cylinder.inertia_marker = inertia_marker
ges_lower_cylinder.part_name = '.GCMB.ges_lower_cylinder'
ges_lower_cylinder.mass = 84.8838172052
ges_lower_cylinder.ixx = 6834235.5549
ges_lower_cylinder.iyy = 6449459.8026
ges_lower_cylinder.izz = 803650.64324
ges_lower_cylinder.ixy = 0.0
ges_lower_cylinder.izx = -85544.003848
ges_lower_cylinder.iyz = 0.0
gralin_geom1 = MakeSceneNodeByType('ShapeCylinder', '.GCMB.ges_lower_cylinder.gralin_geom1')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.gralin_5')
gralin_geom1.center_marker = center_marker
gralin_geom1.cylinder_name = '.GCMB.ges_lower_cylinder.gralin_geom1'
gralin_geom1.adams_id = 89
gralin_geom1.angle_extent = 360.0
gralin_geom1.length = 889.0
gralin_geom1.radius = 101.6
gralin_geom1.side_count_for_body = 15
gralin_geom1.segment_count_for_ends = 15


gralin_geom2 = MakeSceneNodeByType('ShapeCylinder', '.GCMB.ges_lower_cylinder.gralin_geom2')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.gralin_7')
gralin_geom2.center_marker = center_marker
gralin_geom2.cylinder_name = '.GCMB.ges_lower_cylinder.gralin_geom2'
gralin_geom2.adams_id = 90
gralin_geom2.angle_extent = 360.0
gralin_geom2.length = 419.1
gralin_geom2.radius = 30.48
gralin_geom2.side_count_for_body = 15
gralin_geom2.segment_count_for_ends = 15


ges_upper_torque_arm = MakeSceneNodeByType('PartGeneral', '.GCMB.ges_upper_torque_arm')
ges_upper_torque_arm.part_name = '.GCMB.ges_upper_torque_arm'
ges_upper_torque_arm.adams_id = 36
ges_upper_torque_arm.location = Base.Vector (6489.7, 0.0, 774.7)
ges_upper_torque_arm.orientation = Base.Vector (90.0, 111.0375110254, 270.0)
cm = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_torque_arm.cm')
cm.marker_name = '.GCMB.ges_upper_torque_arm.cm'
cm.adams_id = 345
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_torque_arm.inertia_frame')
inertia_frame.marker_name = '.GCMB.ges_upper_torque_arm.inertia_frame'
inertia_frame.adams_id = 346
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_9 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_torque_arm.gralin_9')
gralin_9.marker_name = '.GCMB.ges_upper_torque_arm.gralin_9'
gralin_9.adams_id = 347
gralin_9.location = Base.Vector (-6.7140737414e-11, 0.0, -176.8905311202)
gralin_9.orientation = Base.Vector (90.0, 13.4695391009, 270.0)
jxs_joint_j_8 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_torque_arm.jxs_joint_j_8')
jxs_joint_j_8.marker_name = '.GCMB.ges_upper_torque_arm.jxs_joint_j_8'
jxs_joint_j_8.adams_id = 348
jxs_joint_j_8.location = Base.Vector (93.3345606204, 0.0, 212.7884390511)
jxs_joint_j_8.orientation = Base.Vector (0.0, 90.0, 111.0375110254)
jxs_joint_i_10 = MakeSceneNodeByType('Marker', '.GCMB.ges_upper_torque_arm.jxs_joint_i_10')
jxs_joint_i_10.marker_name = '.GCMB.ges_upper_torque_arm.jxs_joint_i_10'
jxs_joint_i_10.adams_id = 349
jxs_joint_i_10.location = Base.Vector (-6.7140737414e-11, 0.0, -176.8905311202)
jxs_joint_i_10.orientation = Base.Vector (0.0, 90.0, 111.0375110254)
ges_upper_torque_arm = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.cm')
ges_upper_torque_arm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.inertia_frame')
ges_upper_torque_arm.inertia_marker = inertia_marker
ges_upper_torque_arm.part_name = '.GCMB.ges_upper_torque_arm'
ges_upper_torque_arm.mass = 0.3898630024
ges_upper_torque_arm.ixx = 2577.4839558745
ges_upper_torque_arm.iyy = 2577.4839558745
ges_upper_torque_arm.izz = 31.4405018244
ges_upper_torque_arm.ixy = 0.0
ges_upper_torque_arm.izx = 0.0
ges_upper_torque_arm.iyz = 0.0
gralin_upper_torque_arm_geom = MakeSceneNodeByType('ShapeCylinder', '.GCMB.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.gralin_9')
gralin_upper_torque_arm_geom.center_marker = center_marker
gralin_upper_torque_arm_geom.cylinder_name = '.GCMB.ges_upper_torque_arm.gralin_upper_torque_arm_geom'
gralin_upper_torque_arm_geom.adams_id = 91
gralin_upper_torque_arm_geom.angle_extent = 360.0
gralin_upper_torque_arm_geom.length = 400.7006862984
gralin_upper_torque_arm_geom.radius = 12.7
gralin_upper_torque_arm_geom.side_count_for_body = 15
gralin_upper_torque_arm_geom.segment_count_for_ends = 15


ges_lower_torque_arm = MakeSceneNodeByType('PartGeneral', '.GCMB.ges_lower_torque_arm')
ges_lower_torque_arm.part_name = '.GCMB.ges_lower_torque_arm'
ges_lower_torque_arm.adams_id = 37
ges_lower_torque_arm.location = Base.Vector (6477.0, 0.0, 622.3)
ges_lower_torque_arm.orientation = Base.Vector (90.0, 63.4349488229, 270.0)
MARKER_379 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_torque_arm.MARKER_379')
MARKER_379.marker_name = '.GCMB.ges_lower_torque_arm.MARKER_379'
MARKER_379.adams_id = 379
MARKER_379.location = Base.Vector (178.8854381999, 0.0, -288.2291622998)
MARKER_379.orientation = Base.Vector (0.0, 90.0, 63.4349488229)
cm = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_torque_arm.cm')
cm.marker_name = '.GCMB.ges_lower_torque_arm.cm'
cm.adams_id = 350
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_torque_arm.inertia_frame')
inertia_frame.marker_name = '.GCMB.ges_lower_torque_arm.inertia_frame'
inertia_frame.adams_id = 351
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_i_8 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_torque_arm.jxs_joint_i_8')
jxs_joint_i_8.marker_name = '.GCMB.ges_lower_torque_arm.jxs_joint_i_8'
jxs_joint_i_8.adams_id = 352
jxs_joint_i_8.location = Base.Vector (89.4427191001, 0.0, 154.0650836497)
jxs_joint_i_8.orientation = Base.Vector (0.0, 90.0, 63.4349488229)
gralin_10 = MakeSceneNodeByType('Marker', '.GCMB.ges_lower_torque_arm.gralin_10')
gralin_10.marker_name = '.GCMB.ges_lower_torque_arm.gralin_10'
gralin_10.adams_id = 353
gralin_10.location = Base.Vector (178.8854381999, 0.0, -288.2291622998)
gralin_10.orientation = Base.Vector (270.0, 11.4324305526, 90.0)
ges_lower_torque_arm = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.cm')
ges_lower_torque_arm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.inertia_frame')
ges_lower_torque_arm.inertia_marker = inertia_marker
ges_lower_torque_arm.part_name = '.GCMB.ges_lower_torque_arm'
ges_lower_torque_arm.mass = 0.3898630024
ges_lower_torque_arm.ixx = 2577.4839558745
ges_lower_torque_arm.iyy = 2577.4839558745
ges_lower_torque_arm.izz = 31.4405018244
ges_lower_torque_arm.ixy = 0.0
ges_lower_torque_arm.izx = 0.0
ges_lower_torque_arm.iyz = 0.0
gralin_lower_torque_arm_geom = MakeSceneNodeByType('ShapeCylinder', '.GCMB.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.gralin_10')
gralin_lower_torque_arm_geom.center_marker = center_marker
gralin_lower_torque_arm_geom.cylinder_name = '.GCMB.ges_lower_torque_arm.gralin_lower_torque_arm_geom'
gralin_lower_torque_arm_geom.adams_id = 92
gralin_lower_torque_arm_geom.angle_extent = 360.0
gralin_lower_torque_arm_geom.length = 451.2473822639
gralin_lower_torque_arm_geom.radius = 12.7
gralin_lower_torque_arm_geom.side_count_for_body = 15
gralin_lower_torque_arm_geom.segment_count_for_ends = 15


ges_subframe_2 = MakeSceneNodeByType('PartGeneral', '.GCMB.ges_subframe_2')
ges_subframe_2.part_name = '.GCMB.ges_subframe_2'
ges_subframe_2.adams_id = 38
ges_subframe_2.location = Base.Vector (6704.33, 0.0, 1668.78)
ges_subframe_2.orientation = Base.Vector (0.0, 90.0, 356.6444799092)
cm = MakeSceneNodeByType('Marker', '.GCMB.ges_subframe_2.cm')
cm.marker_name = '.GCMB.ges_subframe_2.cm'
cm.adams_id = 355
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.ges_subframe_2.inertia_frame')
inertia_frame.marker_name = '.GCMB.ges_subframe_2.inertia_frame'
inertia_frame.adams_id = 356
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
graout_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_subframe_2.graout_1')
graout_1.marker_name = '.GCMB.ges_subframe_2.graout_1'
graout_1.adams_id = 357
graout_1.location = Base.Vector (-390.5595878992, 5.9115906614e-11, -340.36)
graout_1.orientation = Base.Vector (0.0, 0.0, 0.0)
graout_2 = MakeSceneNodeByType('Marker', '.GCMB.ges_subframe_2.graout_2')
graout_2.marker_name = '.GCMB.ges_subframe_2.graout_2'
graout_2.adams_id = 358
graout_2.location = Base.Vector (-390.5595878992, 5.9115906614e-11, 340.36)
graout_2.orientation = Base.Vector (0.0, 0.0, 0.0)
graout_3 = MakeSceneNodeByType('Marker', '.GCMB.ges_subframe_2.graout_3')
graout_3.marker_name = '.GCMB.ges_subframe_2.graout_3'
graout_3.adams_id = 359
graout_3.location = Base.Vector (781.1191757984, -1.1850243009e-10, 0.0)
graout_3.orientation = Base.Vector (0.0, 0.0, 0.0)
ges_subframe_2 = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2.cm')
ges_subframe_2.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2.inertia_frame')
ges_subframe_2.inertia_marker = inertia_marker
ges_subframe_2.part_name = '.GCMB.ges_subframe_2'
ges_subframe_2.mass = 0.0045359237
ges_subframe_2.ixx = 2.9263965343
ges_subframe_2.iyy = 2.9263965343
ges_subframe_2.izz = 2.9263965343
ges_subframe_2.ixy = 0.0
ges_subframe_2.izx = 0.0
ges_subframe_2.iyz = 0.0
graout_subframe_geom = MakeSceneNodeByType('CurveOutline', '.GCMB.ges_subframe_2.graout_subframe_geom')
# >>>[ERROR] CAN NOT find link prop(marker_name) from .GCMB.ges_subframe_2.graout_subframe_geom, Please DOUBLE CHECK!
# >>>[ERROR] CAN NOT find link prop(visibility_between_markers) from .GCMB.ges_subframe_2.graout_subframe_geom, Please DOUBLE CHECK!
graout_subframe_geom.outline_name = '.GCMB.ges_subframe_2.graout_subframe_geom'
graout_subframe_geom.adams_id = 34
graout_subframe_geom.close = 'yes'


mts_body_mount_2 = MakeSceneNodeByType('PartGeneral', '.GCMB.mts_body_mount_2')
mts_body_mount_2.part_name = '.GCMB.mts_body_mount_2'
mts_body_mount_2.adams_id = 39
mts_body_mount_2.location = Base.Vector (6704.33, 0.0, 1668.78)
mts_body_mount_2.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_430 = MakeSceneNodeByType('Marker', '.GCMB.mts_body_mount_2.MARKER_430')
MARKER_430.marker_name = '.GCMB.mts_body_mount_2.MARKER_430'
MARKER_430.adams_id = 430
MARKER_430.location = Base.Vector (779.78, 0.0, -45.72)
MARKER_430.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_427 = MakeSceneNodeByType('Marker', '.GCMB.mts_body_mount_2.MARKER_427')
MARKER_427.marker_name = '.GCMB.mts_body_mount_2.MARKER_427'
MARKER_427.adams_id = 427
MARKER_427.location = Base.Vector (-506.73, 0.0, -43.18)
MARKER_427.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_109 = MakeSceneNodeByType('Marker', '.GCMB.mts_body_mount_2.MARKER_109')
MARKER_109.marker_name = '.GCMB.mts_body_mount_2.MARKER_109'
MARKER_109.adams_id = 365
MARKER_109.location = Base.Vector (0.0, 0.0, 0.0)
MARKER_109.orientation = Base.Vector (0.0, 0.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.GCMB.mts_body_mount_2.cm')
cm.marker_name = '.GCMB.mts_body_mount_2.cm'
cm.adams_id = 366
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_111 = MakeSceneNodeByType('Marker', '.GCMB.mts_body_mount_2.MARKER_111')
MARKER_111.marker_name = '.GCMB.mts_body_mount_2.MARKER_111'
MARKER_111.adams_id = 367
MARKER_111.location = Base.Vector (0.0, 0.0, 0.0)
MARKER_111.orientation = Base.Vector (90.0, 3.3555200908, 0.0)
mts_body_mount_2 = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2.cm')
mts_body_mount_2.center_of_mass_marker = center_of_mass_marker
mts_body_mount_2.part_name = '.GCMB.mts_body_mount_2'
mts_body_mount_2.mass = 5000.0
mts_body_mount_2.ixx = 292.63965343
mts_body_mount_2.iyy = 292.63965343
mts_body_mount_2.izz = 292.63965343
mts_body_mount_2.ixy = 0.0
mts_body_mount_2.izx = 0.0
mts_body_mount_2.iyz = 0.0
ELLIPSOID_38 = MakeSceneNodeByType('ShapeEllipsoid', '.GCMB.mts_body_mount_2.ELLIPSOID_38')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2.MARKER_109')
ELLIPSOID_38.center_marker = center_marker
ELLIPSOID_38.ellipsoid_name = '.GCMB.mts_body_mount_2.ELLIPSOID_38'
ELLIPSOID_38.adams_id = 38
ELLIPSOID_38.x_scale_factor = 200.0
ELLIPSOID_38.y_scale_factor = 200.0
ELLIPSOID_38.z_scale_factor = 200.0


ges_collar = MakeSceneNodeByType('PartGeneral', '.GCMB.ges_collar')
ges_collar.part_name = '.GCMB.ges_collar'
ges_collar.adams_id = 40
ges_collar.location = Base.Vector (6197.6, 0.0, 809.498)
ges_collar.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_j_10 = MakeSceneNodeByType('Marker', '.GCMB.ges_collar.jxs_joint_j_10')
jxs_joint_j_10.marker_name = '.GCMB.ges_collar.jxs_joint_j_10'
jxs_joint_j_10.adams_id = 368
jxs_joint_j_10.location = Base.Vector (127.0, 0.0, 28.702)
jxs_joint_j_10.orientation = Base.Vector (0.0, 90.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.GCMB.ges_collar.cm')
cm.marker_name = '.GCMB.ges_collar.cm'
cm.adams_id = 369
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.GCMB.ges_collar.inertia_frame')
inertia_frame.marker_name = '.GCMB.ges_collar.inertia_frame'
inertia_frame.adams_id = 370
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_24 = MakeSceneNodeByType('Marker', '.GCMB.ges_collar.gralin_24')
gralin_24.marker_name = '.GCMB.ges_collar.gralin_24'
gralin_24.adams_id = 371
gralin_24.location = Base.Vector (0.0, 0.0, -47.498)
gralin_24.orientation = Base.Vector (0.0, 0.0, 0.0)
jxs_joint_i_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_collar.jxs_joint_i_1')
jxs_joint_i_1.marker_name = '.GCMB.ges_collar.jxs_joint_i_1'
jxs_joint_i_1.adams_id = 372
jxs_joint_i_1.location = Base.Vector (0.0, 0.0, 47.498)
jxs_joint_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_actuator_i_1 = MakeSceneNodeByType('Marker', '.GCMB.ges_collar.ues_actuator_i_1')
ues_actuator_i_1.marker_name = '.GCMB.ges_collar.ues_actuator_i_1'
ues_actuator_i_1.adams_id = 373
ues_actuator_i_1.location = Base.Vector (0.0, 0.0, 47.498)
ues_actuator_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ues_actuator_i_4 = MakeSceneNodeByType('Marker', '.GCMB.ges_collar.ues_actuator_i_4')
ues_actuator_i_4.marker_name = '.GCMB.ges_collar.ues_actuator_i_4'
ues_actuator_i_4.adams_id = 374
ues_actuator_i_4.location = Base.Vector (0.0, 0.0, 47.498)
ues_actuator_i_4.orientation = Base.Vector (0.0, 0.0, 0.0)
ges_collar = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.cm')
ges_collar.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.inertia_frame')
ges_collar.inertia_marker = inertia_marker
ges_collar.part_name = '.GCMB.ges_collar'
ges_collar.mass = 6.4242828175
ges_collar.ixx = 85080.541407
ges_collar.iyy = 85080.541407
ges_collar.izz = 146854.28308
ges_collar.ixy = 0.0
ges_collar.izx = 0.0
ges_collar.iyz = 0.0
gralin_collar = MakeSceneNodeByType('ShapeCylinder', '.GCMB.ges_collar.gralin_collar')
center_marker = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.gralin_24')
gralin_collar.center_marker = center_marker
gralin_collar.cylinder_name = '.GCMB.ges_collar.gralin_collar'
gralin_collar.adams_id = 93
gralin_collar.angle_extent = 360.0
gralin_collar.length = 94.996
gralin_collar.radius = 139.7
gralin_collar.side_count_for_body = 15
gralin_collar.segment_count_for_ends = 15


_cv_diff = MakeSceneNodeByType('PartDifferentialEquation', '.GCMB._cv_diff')
_cv_diff.differential_equation_name = '.GCMB._cv_diff'
_cv_diff.adams_id = 1
_cv_diff.comments = '"Dummy for communicators"'
_cv_diff.function = '""'
_cv_diff.initial_condition = 0.0
_cv_diff.implicit = False
_cv_diff.static_hold = False




JOINT_51 = MakeSceneNodeByType('JointRevolute', '.GCMB.JOINT_51')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.MARKER_378')
JOINT_51.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.MARKER_379')
JOINT_51.j_marker_name = j_marker_name
JOINT_51.joint_name = '.GCMB.JOINT_51'
JOINT_51.adams_id = 51


JOINT_57 = MakeSceneNodeByType('JointSpherical', '.GCMB.JOINT_57')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.MARKER_429')
JOINT_57.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2.MARKER_430')
JOINT_57.j_marker_name = j_marker_name
JOINT_57.joint_name = '.GCMB.JOINT_57'
JOINT_57.adams_id = 57


JOINT_56 = MakeSceneNodeByType('JointFixed', '.GCMB.JOINT_56')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2.MARKER_427')
JOINT_56.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.MARKER_428')
JOINT_56.j_marker_name = j_marker_name
JOINT_56.joint_name = '.GCMB.JOINT_56'
JOINT_56.adams_id = 56


josrev_lta_uta_joint = MakeSceneNodeByType('JointSpherical', '.GCMB.josrev_lta_uta_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.jxs_joint_i_8')
josrev_lta_uta_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.jxs_joint_j_8')
josrev_lta_uta_joint.j_marker_name = j_marker_name
josrev_lta_uta_joint.joint_name = '.GCMB.josrev_lta_uta_joint'
josrev_lta_uta_joint.adams_id = 39


josrev_uta_uc_joint = MakeSceneNodeByType('JointRevolute', '.GCMB.josrev_uta_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.jxs_joint_i_10')
josrev_uta_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_j_10')
josrev_uta_uc_joint.j_marker_name = j_marker_name
josrev_uta_uc_joint.joint_name = '.GCMB.josrev_uta_uc_joint'
josrev_uta_uc_joint.adams_id = 41


joscyl_lc_uc_joint = MakeSceneNodeByType('JointCylinder', '.GCMB.joscyl_lc_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.jxs_joint_i_11')
joscyl_lc_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_11')
joscyl_lc_uc_joint.j_marker_name = j_marker_name
joscyl_lc_uc_joint.joint_name = '.GCMB.joscyl_lc_uc_joint'
joscyl_lc_uc_joint.adams_id = 42


jossph_db_uc_joint = MakeSceneNodeByType('JointSpherical', '.GCMB.jossph_db_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.jxs_joint_i_12')
jossph_db_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_12')
jossph_db_uc_joint.j_marker_name = j_marker_name
jossph_db_uc_joint.joint_name = '.GCMB.jossph_db_uc_joint'
jossph_db_uc_joint.adams_id = 43


josrev_collar_uc_joint = MakeSceneNodeByType('JointFixed', '.GCMB.josrev_collar_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_i_1')
josrev_collar_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_1')
josrev_collar_uc_joint.j_marker_name = j_marker_name
josrev_collar_uc_joint.joint_name = '.GCMB.josrev_collar_uc_joint'
josrev_collar_uc_joint.adams_id = 48


NLG_AIR = MakeSceneNodeByType('ForceSingleComponent', '.GCMB.NLG_AIR')
NLG_AIR.type_of_freedom = 'translational'
NLG_AIR.action_only = False
NLG_AIR.function_opt = 0
NLG_AIR.function = '""'
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.MARKER_405')
NLG_AIR.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.MARKER_406')
NLG_AIR.j_marker_name = j_marker_name
NLG_AIR.position_define_opt = 1


NLG_OIL = MakeSceneNodeByType('ForceSingleComponent', '.GCMB.NLG_OIL')
NLG_OIL.type_of_freedom = 'translational'
NLG_OIL.action_only = False
NLG_OIL.function_opt = 0
NLG_OIL.function = '""'
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.MARKER_407')
NLG_OIL.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.MARKER_408')
NLG_OIL.j_marker_name = j_marker_name
NLG_OIL.position_define_opt = 1


NLG_STOP = MakeSceneNodeByType('ForceSingleComponent', '.GCMB.NLG_STOP')
NLG_STOP.type_of_freedom = 'translational'
NLG_STOP.action_only = False
NLG_STOP.function_opt = 0
NLG_STOP.function = '""'
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.MARKER_409')
NLG_STOP.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.MARKER_410')
NLG_STOP.j_marker_name = j_marker_name
NLG_STOP.position_define_opt = 1


Last_Sim = MakeSceneNodeByType('SimuScript', '.GCMB.Last_Sim')
Last_Sim.sim_script_name = '.GCMB.Last_Sim'
Last_Sim.commands = '"simulation single_run transient type=auto_select initial_static=no end_time=2.0 number_of_steps=400 model_name=.GCMB"'
Last_Sim_2 = MakeSceneNodeByType('SimuScript', '.GCMB.Last_Sim_2')
Last_Sim_2.sim_script_name = '.GCMB.Last_Sim_2'
Last_Sim_2.commands = '"simulation single_run transient type=auto_select initial_static=no end_time=2.0 number_of_steps=300 model_name=._AA_nlg_post_2hubs"'

# ---- TireCMD support (converted from Adams/Car vpg_tire/vpg_road UDE) ----
import os
from FmbsShortcut.import_all_node import MakeSceneNodeByType as SCMakeSceneNodeByType
import FmbsShortcut.SCcmd.TireCMD as TireCMD
_MODEL_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_MODEL_RESOURCE_DIR = os.path.join(_MODEL_SCRIPT_DIR, 'resources', os.path.splitext(os.path.basename(__file__))[0])
scene = Jusme.ActiveUSScene
tire_defaults_units = MakeSceneNodeByType('DefaultsUnits', 'defaultsunits')
tire_defaults_units.length = 'Millimeter'

# Tire converted from .GCMB.luntai1_2
parameter = SCMakeSceneNodeByType('Tire', 'Tire_input_1')
parameter.tire_name = 'luntai1_2'
parameter.tire_file_path = os.path.join(_MODEL_RESOURCE_DIR, 'NLG.tir')
parameter.road_file_path = os.path.join(_MODEL_RESOURCE_DIR, '2d_flat.rdf')
parameter.mass = 13.6077711
parameter.lxx_lyy = 200
parameter.Izz = 556015.3415
parameter.tire_center_direction_opt = 0
parameter.tire_euler_angles = (0.0, 90.0, 0.0)
center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center1')
parameter.tire_center_location = center.location
parameter.road_name = 'road'
parameter.road_direction_opt = 0
parameter.road_euler_angles = (0.0, 0.0, 0.0)
parameter.road_belong_part = Jusme.ActiveUSScene.getObject('.GCMB.ground')
parameter.longitudinal_velocites = 0.0
parameter.spin_velocites = 0.0
TireCMD.run_test('Tire_input_1')
MARKER_112 = MakeSceneNodeByType('Marker', '.GCMB.road.MARKER_112')
MARKER_112.marker_name = '.GCMB.road.MARKER_112'
MARKER_112.adams_id = 375
MARKER_112.location = Base.Vector (6704.3299999, 0.0, 2146.3)
MARKER_112.orientation = Base.Vector (90.0, 3.3555200908, 0.0)


MARKER_7 = MakeSceneNodeByType('Marker', '.GCMB.luntai1_2.wheel_part.MARKER_7')
MARKER_7.marker_name = '.GCMB.luntai1_2.wheel_part.MARKER_7'
MARKER_7.adams_id = 376
MARKER_7.location = Base.Vector (6229.096, -209.55, 308.0)
MARKER_7.orientation = Base.Vector (0.0, 90.0, 0.0)

# Tire converted from .GCMB.luntai2_2
parameter = SCMakeSceneNodeByType('Tire', 'Tire_input_2')
parameter.tire_name = 'luntai2_2'
parameter.tire_file_path = os.path.join(_MODEL_RESOURCE_DIR, 'NLG.tir')
parameter.road_file_path = os.path.join(_MODEL_RESOURCE_DIR, '2d_flat.rdf')
parameter.mass = 13.6077711
parameter.lxx_lyy = 200
parameter.Izz = 556015.3415
parameter.tire_center_direction_opt = 0
parameter.tire_euler_angles = (0.0, 90.0, 0.0)
center = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpr_wheel_center1')
parameter.tire_center_location = center.location
parameter.road_opt = 1
parameter.road_part = Jusme.ActiveUSScene.getObject('.GCMB.road')
parameter.longitudinal_velocites = 0.0
parameter.spin_velocites = 0.0
TireCMD.run_test('Tire_input_2')

MARKER_5 = MakeSceneNodeByType('Marker', '.GCMB.luntai2_2.wheel_part.MARKER_5')
MARKER_5.marker_name = '.GCMB.luntai2_2.wheel_part.MARKER_5'
MARKER_5.adams_id = 377
MARKER_5.location = Base.Vector (6229.096, 209.55, 308.0)
MARKER_5.orientation = Base.Vector (0.0, 90.0, 0.0)
JOINT_1 = MakeSceneNodeByType('JointRevolute', '.GCMB.JOINT_1')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.luntai2_2.wheel_part.MARKER_5')
JOINT_1.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.MARKER_6')
JOINT_1.j_marker_name = j_marker_name
JOINT_1.joint_name = '.GCMB.JOINT_1'
JOINT_1.adams_id = 1


JOINT_2 = MakeSceneNodeByType('JointRevolute', '.GCMB.JOINT_2')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.luntai1_2.wheel_part.MARKER_7')
JOINT_2.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.MARKER_8')
JOINT_2.j_marker_name = j_marker_name
JOINT_2.joint_name = '.GCMB.JOINT_2'
JOINT_2.adams_id = 49


JOINT_15 = MakeSceneNodeByType('JointTranslational', '.GCMB.JOINT_15')
i_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2.MARKER_111')
JOINT_15.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.GCMB.road.MARKER_112')
JOINT_15.j_marker_name = j_marker_name
JOINT_15.joint_name = '.GCMB.JOINT_15'
JOINT_15.adams_id = 50


gravity = MakeSceneNodeByType('Gravity', '.GCMB.gravity')
gravity.gravity_field_name = 'gravity'
gravity.z_component_gravity = -9809.9999999989


hcqwy = MakeSceneNodeByType('Function', '.GCMB.hcqwy')
hcqwy.function = '""'


minor_role = MakeSceneNodeByType('DesignVariable', '.GCMB.mts_body_mount_2.minor_role')
minor_role.variable_name = '.GCMB.mts_body_mount_2.minor_role'
minor_role.value_type_opt = 2
minor_role.string_value = '"inherit"'


NLG_Aa = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_Aa')
NLG_Aa.variable_name = '.GCMB.NLG_Aa'
NLG_Aa.units = '"area"'
NLG_Aa.range = [-645.16, 645.16]
NLG_Aa.use_range = True
NLG_Aa.use_allowed_values = False
NLG_Aa.delta_type = 0
NLG_Aa.value_type_opt = 0
NLG_Aa.real_value = 26807.17


NLG_V0 = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_V0')
NLG_V0.variable_name = '.GCMB.NLG_V0'
NLG_V0.units = '"volume"'
NLG_V0.range = [-6.4516e+05, 6.4516e+05]
NLG_V0.use_range = True
NLG_V0.use_allowed_values = False
NLG_V0.delta_type = 0
NLG_V0.value_type_opt = 0
NLG_V0.real_value = 10280000.0


NLG_P0 = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_P0')
NLG_P0.variable_name = '.GCMB.NLG_P0'
NLG_P0.units = '"pressure"'
NLG_P0.range = [-6.4516e-10, 6.4516e-10]
NLG_P0.use_range = True
NLG_P0.use_allowed_values = False
NLG_P0.delta_type = 0
NLG_P0.value_type_opt = 0
NLG_P0.real_value = 1.3


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


NLG_Ah = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_Ah')
NLG_Ah.variable_name = '.GCMB.NLG_Ah'
NLG_Ah.units = '"area"'
NLG_Ah.range = [-645.16, 645.16]
NLG_Ah.use_range = True
NLG_Ah.use_allowed_values = False
NLG_Ah.delta_type = 0
NLG_Ah.value_type_opt = 0
NLG_Ah.real_value = 19530.0


NLG_As = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_As')
NLG_As.variable_name = '.GCMB.NLG_As'
NLG_As.units = '"area"'
NLG_As.range = [-645.16, 645.16]
NLG_As.use_range = True
NLG_As.use_allowed_values = False
NLG_As.delta_type = 0
NLG_As.value_type_opt = 0
NLG_As.real_value = 6139.0


NLG_Ahd = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_Ahd')
NLG_Ahd.variable_name = '.GCMB.NLG_Ahd'
NLG_Ahd.units = '"area"'
NLG_Ahd.range = [-645.16, 645.16]
NLG_Ahd.use_range = True
NLG_Ahd.use_allowed_values = False
NLG_Ahd.delta_type = 0
NLG_Ahd.value_type_opt = 0
NLG_Ahd.real_value = 514.0


NLG_Ahdl = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_Ahdl')
NLG_Ahdl.variable_name = '.GCMB.NLG_Ahdl'
NLG_Ahdl.units = '"area"'
NLG_Ahdl.range = [-645.16, 645.16]
NLG_Ahdl.use_range = True
NLG_Ahdl.use_allowed_values = False
NLG_Ahdl.delta_type = 0
NLG_Ahdl.value_type_opt = 0
NLG_Ahdl.real_value = 314.0


NLG_Asd = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_Asd')
NLG_Asd.variable_name = '.GCMB.NLG_Asd'
NLG_Asd.units = '"area"'
NLG_Asd.range = [-645.16, 645.16]
NLG_Asd.use_range = True
NLG_Asd.use_allowed_values = False
NLG_Asd.delta_type = 0
NLG_Asd.value_type_opt = 0
NLG_Asd.real_value = 2313.0


NLG_Asdl = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_Asdl')
NLG_Asdl.variable_name = '.GCMB.NLG_Asdl'
NLG_Asdl.units = '"area"'
NLG_Asdl.range = [-645.16, 645.16]
NLG_Asdl.use_range = True
NLG_Asdl.use_allowed_values = False
NLG_Asdl.delta_type = 0
NLG_Asdl.value_type_opt = 0
NLG_Asdl.real_value = 100.0


NLG_Ch = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_Ch')
NLG_Ch.variable_name = '.GCMB.NLG_Ch'
NLG_Ch.units = '"no_units"'
NLG_Ch.range = [-6.4516e-04, 6.4516e-04]
NLG_Ch.use_range = True
NLG_Ch.use_allowed_values = False
NLG_Ch.delta_type = 0
NLG_Ch.value_type_opt = 0
NLG_Ch.real_value = 0.8


NLG_Cs = MakeSceneNodeByType('DesignVariable', '.GCMB.NLG_Cs')
NLG_Cs.variable_name = '.GCMB.NLG_Cs'
NLG_Cs.units = '"no_units"'
NLG_Cs.range = [-6.4516e-04, 6.4516e-04]
NLG_Cs.use_range = True
NLG_Cs.use_allowed_values = False
NLG_Cs.delta_type = 0
NLG_Cs.value_type_opt = 0
NLG_Cs.real_value = 0.8


NLG_V = Jusme.ActiveUSScene.getObject('.GCMB.NLG_V')
NLG_V.variable_name = '.GCMB.NLG_V'
NLG_V.function = '"-1*VR(.GCMB.ges_upper_cylinder.MARKER_2,.GCMB.ges_lower_cylinder.MARKER_1)"'


NLG_S = Jusme.ActiveUSScene.getObject('.GCMB.NLG_S')
NLG_S.variable_name = '.GCMB.NLG_S'
NLG_S.function = '"428.6-DM(.GCMB.ges_upper_cylinder.MARKER_2,.GCMB.ges_lower_cylinder.MARKER_1)"'


x1 = Jusme.ActiveUSScene.getObject('.GCMB.x1')
x1.variable_name = '.GCMB.x1'
x1.function = '"-1*(VARVAL(.GCMB.NLG_V)*0.5*(VARVAL(.GCMB.NLG_V)-ABS(VARVAL(.GCMB.NLG_V)))*((.GCMB.rou*.GCMB.NLG_Ah**3/(2*.GCMB.NLG_Ch**2*.GCMB.NLG_Ahdl**2))+(.GCMB.rou*.GCMB.NLG_As**3/(2*.GCMB.NLG_Cs**2*.GCMB.NLG_Asdl**2))))"'


x2 = Jusme.ActiveUSScene.getObject('.GCMB.x2')
x2.variable_name = '.GCMB.x2'
x2.function = '"0.00001*VARVAL(.GCMB.NLG_V)*0.5*(VARVAL(.GCMB.NLG_V)+ABS(VARVAL(.GCMB.NLG_V)))*((.GCMB.rou*.GCMB.NLG_Ah**3/(2*.GCMB.NLG_Ch**2*.GCMB.NLG_Ahd**2))+(.GCMB.rou*.GCMB.NLG_As**3/(2*.GCMB.NLG_Cs**2*.GCMB.NLG_Asd**2)))"'


VARIABLE_123 = Jusme.ActiveUSScene.getObject('.GCMB.VARIABLE_123')
VARIABLE_123.variable_name = '.GCMB.VARIABLE_123'
VARIABLE_123.function = '"IF(TIME:0,1,2)"'


VARIABLE_124 = Jusme.ActiveUSScene.getObject('.GCMB.VARIABLE_124')
VARIABLE_124.variable_name = '.GCMB.VARIABLE_124'
VARIABLE_124.function = '"VARVAL(.GCMB.NLG_V)-ABS(VARVAL(.GCMB.NLG_V))"'


_cv_solver_variable = Jusme.ActiveUSScene.getObject('.GCMB._cv_solver_variable')
_cv_solver_variable.variable_name = '.GCMB._cv_solver_variable'
_cv_solver_variable.function = '"0"'


hcqwy = Jusme.ActiveUSScene.getObject('.GCMB.hcqwy')
hcqwy.function = '"428.6-DZ(.GCMB.ges_upper_cylinder.MARKER_2,.GCMB.ges_lower_cylinder.MARKER_1)"'

_cv_diff = Jusme.ActiveUSScene.getObject('.GCMB._cv_diff')
_cv_diff.differential_equation_name = '.GCMB._cv_diff'
_cv_diff.function = '"0"'


NLG_AIR = Jusme.ActiveUSScene.getObject('.GCMB.NLG_AIR')
NLG_AIR.function = '"1*.GCMB.NLG_Aa*(.GCMB.NLG_P0*(.GCMB.NLG_V0/(.GCMB.NLG_V0-.GCMB.NLG_Aa*(428.6-DM(.GCMB.ges_upper_cylinder.MARKER_2,.GCMB.ges_lower_cylinder.MARKER_1))))**1.1-.GCMB.Patm)"'


NLG_OIL = Jusme.ActiveUSScene.getObject('.GCMB.NLG_OIL')
NLG_OIL.function = '"IF(VARVAL(.GCMB.NLG_V):-0.001*(VARVAL(.GCMB.NLG_V)*0.5*(VARVAL(.GCMB.NLG_V)-ABS(VARVAL(.GCMB.NLG_V)))*((.GCMB.rou*.GCMB.NLG_Ah**3/(2*.GCMB.NLG_Ch**2*.GCMB.NLG_Ahdl**2))+(.GCMB.rou*.GCMB.NLG_As**3/(2*.GCMB.NLG_Cs**2*.GCMB.NLG_Asdl**2)))),0,0.001*VARVAL(.GCMB.NLG_V)*0.5*(VARVAL(.GCMB.NLG_V)+ABS(VARVAL(.GCMB.NLG_V)))*((.GCMB.rou*.GCMB.NLG_Ah**3/(2*.GCMB.NLG_Ch**2*.GCMB.NLG_Ahd**2))+(.GCMB.rou*.GCMB.NLG_As**3/(2*.GCMB.NLG_Cs**2*.GCMB.NLG_Asd**2))))"'


NLG_STOP = Jusme.ActiveUSScene.getObject('.GCMB.NLG_STOP')
NLG_STOP.function = '"IF(428.6-DM(.GCMB.ges_upper_cylinder.MARKER_2,.GCMB.ges_lower_cylinder.MARKER_1) :1.0E+09*(428.6-DM(.GCMB.ges_upper_cylinder.MARKER_2,.GCMB.ges_lower_cylinder.MARKER_1)), 0 , 0 )"'


# TireCMD handles initial-velocity reference for .GCMB.luntai1_2.wheel_part (vm=.GCMB.luntai1_2.wheel_part.wheel_cm, wm=.GCMB.luntai1_2.wheel_part.wheel_cm)
# TireCMD handles initial-velocity reference for .GCMB.luntai1_2.belt_part (vm=.GCMB.luntai1_2.wheel_part.wheel_cm, wm=.GCMB.luntai1_2.wheel_part.wheel_cm)
# TireCMD handles initial-velocity reference for .GCMB.luntai2_2.wheel_part (vm=.GCMB.luntai2_2.wheel_part.wheel_cm, wm=.GCMB.luntai2_2.wheel_part.wheel_cm)
# TireCMD handles initial-velocity reference for .GCMB.luntai2_2.belt_part (vm=.GCMB.luntai2_2.wheel_part.wheel_cm, wm=.GCMB.luntai2_2.wheel_part.wheel_cm)
uel_gearaero_origin_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.uel_gearaero_origin_1')
uel_gearaero_origin_1.marker_name = '.GCMB.ground.uel_gearaero_origin_1'
_GCMB_ground_origo = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo')
uel_gearaero_origin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo))
_GCMB_ground_origo = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo')
uel_gearaero_origin_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo))


uer_gearaero_origin_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.uer_gearaero_origin_1')
uer_gearaero_origin_1.marker_name = '.GCMB.ground.uer_gearaero_origin_1'
_GCMB_ground_origo = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo')
uer_gearaero_origin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo))
_GCMB_ground_origo = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo')
uer_gearaero_origin_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo))


lumian_ref_1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.lumian_ref_1')
lumian_ref_1.marker_name = '.GCMB.ground.lumian_ref_1'
lumian_ref_1.location = Base.Vector (12238.367977, 1509.5002745, -560.8546166)
lumian_ref_1.orientation = Base.Vector (0.0, 0.0, 0.0)


cfl_spin_axis1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfl_spin_axis1')
cfl_spin_axis1.marker_name = '.GCMB.ground.cfl_spin_axis1'
_GCMB_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center1')
cfl_spin_axis1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_wheel_center1))
_GCMB_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center1').location
_GCMB_ground_hpl_ob_axle1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_ob_axle1').location
cfl_spin_axis1.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpl_wheel_center1, _GCMB_ground_hpl_ob_axle1, "Z"))


cfr_spin_axis1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfr_spin_axis1')
cfr_spin_axis1.marker_name = '.GCMB.ground.cfr_spin_axis1'
_GCMB_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpr_wheel_center1')
cfr_spin_axis1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpr_wheel_center1))
_GCMB_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpr_wheel_center1').location
_GCMB_ground_hpr_ob_axle1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpr_ob_axle1').location
cfr_spin_axis1.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpr_wheel_center1, _GCMB_ground_hpr_ob_axle1, "Z"))


cfs_nlg_axle_lowpoint = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_nlg_axle_lowpoint')
cfs_nlg_axle_lowpoint.marker_name = '.GCMB.ground.cfs_nlg_axle_lowpoint'
_GCMB_ground_hps_nlg_axle_lowpoint = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_nlg_axle_lowpoint')
cfs_nlg_axle_lowpoint.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_nlg_axle_lowpoint))
_GCMB_ground_origo1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo1')
cfs_nlg_axle_lowpoint.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo1))


cfs_collar_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_collar_top')
cfs_collar_top.marker_name = '.GCMB.ground.cfs_collar_top'
_GCMB_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_bot').location
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top').location
cfs_collar_top.location = (VecUtils.LOC_ALONG_LINE(_GCMB_ground_hps_uc_bot, _GCMB_ground_hps_uc_top, 0.11 * VecUtils.DM(_GCMB_ground_hps_uc_bot, _GCMB_ground_hps_uc_top)))
_GCMB_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_bot').location
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top').location
cfs_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_uc_bot, _GCMB_ground_hps_uc_top, "Z"))


lumian_ref_11 = Jusme.ActiveUSScene.getObject('.GCMB.ground.lumian_ref_11')
lumian_ref_11.marker_name = '.GCMB.ground.lumian_ref_11'
lumian_ref_11.location = Base.Vector (7484.11, 0.0, 48.26)
lumian_ref_11.orientation = Base.Vector (0.0, 0.0, 0.0)


aluminum = Jusme.ActiveUSScene.getObject('.GCMB.aluminum')
aluminum.material_name = '.GCMB.aluminum'


steel_2 = Jusme.ActiveUSScene.getObject('.GCMB.steel_2')
steel_2.material_name = '.GCMB.steel_2'


aluminum_2 = Jusme.ActiveUSScene.getObject('.GCMB.aluminum_2')
aluminum_2.material_name = '.GCMB.aluminum_2'


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.ges_dragbrace.inertia_frame'
_GCMB_ges_dragbrace_cm = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_dragbrace_cm))
_GCMB_ges_dragbrace = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.gralin_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace')
gralin_1.relative_to = relative_to
gralin_1.marker_name = '.GCMB.ges_dragbrace.gralin_1'
_GCMB_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_db_sf_atch')
gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_db_sf_atch))
_GCMB_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_db_sf_atch').location
_GCMB_ground_hps_db_uc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_db_uc_atch').location
gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_db_sf_atch, _GCMB_ground_hps_db_uc_atch, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_i_12 = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.jxs_joint_i_12')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace')
jxs_joint_i_12.relative_to = relative_to
jxs_joint_i_12.marker_name = '.GCMB.ges_dragbrace.jxs_joint_i_12'
_GCMB_ges_upper_cylinder_jxs_joint_j_12 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_12')
jxs_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_12))
_GCMB_ges_upper_cylinder_jxs_joint_j_12 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_12')
jxs_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_12))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_12.location, jxs_joint_i_12.orientation)
jxs_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_dragbrace_geom = Jusme.ActiveUSScene.getObject('.GCMB.ges_dragbrace.gralin_dragbrace_geom')
gralin_dragbrace_geom.cylinder_name = '.GCMB.ges_dragbrace.gralin_dragbrace_geom'
_GCMB_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_db_sf_atch').location
_GCMB_ground_hps_db_uc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_db_uc_atch').location
gralin_dragbrace_geom.length = (VecUtils.DM(_GCMB_ground_hps_db_sf_atch, _GCMB_ground_hps_db_uc_atch))


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.ges_upper_cylinder.inertia_frame'
_GCMB_ges_upper_cylinder_cm = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_cm))
_GCMB_ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_2 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.gralin_2')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
gralin_2.relative_to = relative_to
gralin_2.marker_name = '.GCMB.ges_upper_cylinder.gralin_2'
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top')
gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_top))
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top').location
_GCMB_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_bot').location
gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_uc_top, _GCMB_ground_hps_uc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_2.location, gralin_2.orientation)
gralin_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_3 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.gralin_3')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
gralin_3.relative_to = relative_to
gralin_3.marker_name = '.GCMB.ges_upper_cylinder.gralin_3'
_GCMB_ground_hps_uc_sf_atch_l = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_sf_atch_l')
gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_sf_atch_l))
_GCMB_ground_hps_uc_sf_atch_l = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_sf_atch_l').location
_GCMB_ground_hps_uc_geompt = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_geompt').location
gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_uc_sf_atch_l, _GCMB_ground_hps_uc_geompt, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_4 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.gralin_4')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
gralin_4.relative_to = relative_to
gralin_4.marker_name = '.GCMB.ges_upper_cylinder.gralin_4'
_GCMB_ground_hps_uc_sf_atch_r = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_sf_atch_r')
gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_sf_atch_r))
_GCMB_ground_hps_uc_sf_atch_r = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_sf_atch_r').location
_GCMB_ground_hps_uc_geompt = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_geompt').location
gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_uc_sf_atch_r, _GCMB_ground_hps_uc_geompt, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_j_12 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_12')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
jxs_joint_j_12.relative_to = relative_to
jxs_joint_j_12.marker_name = '.GCMB.ges_upper_cylinder.jxs_joint_j_12'
_GCMB_ground_hps_db_uc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_db_uc_atch')
jxs_joint_j_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_db_uc_atch))
_GCMB_ground_origo1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo1')
jxs_joint_j_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_12.location, jxs_joint_j_12.orientation)
jxs_joint_j_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_j_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_spring_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.ues_spring_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
ues_spring_j_1.relative_to = relative_to
ues_spring_j_1.marker_name = '.GCMB.ges_upper_cylinder.ues_spring_j_1'
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top')
ues_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_j_1.location, ues_spring_j_1.orientation)
ues_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ues_damper_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.ues_damper_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
ues_damper_j_1.relative_to = relative_to
ues_damper_j_1.marker_name = '.GCMB.ges_upper_cylinder.ues_damper_j_1'
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top')
ues_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_j_1.location, ues_damper_j_1.orientation)
ues_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ues_stopper_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.ues_stopper_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
ues_stopper_j_1.relative_to = relative_to
ues_stopper_j_1.marker_name = '.GCMB.ges_upper_cylinder.ues_stopper_j_1'
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top')
ues_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_j_1.location, ues_stopper_j_1.orientation)
ues_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
jxs_joint_j_1.relative_to = relative_to
jxs_joint_j_1.marker_name = '.GCMB.ges_upper_cylinder.jxs_joint_j_1'
_GCMB_ground_cfs_collar_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_collar_top')
jxs_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfs_collar_top))
_GCMB_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_bot').location
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top').location
jxs_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_uc_bot, _GCMB_ground_hps_uc_top, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
jxs_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_actuator_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.ues_actuator_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
ues_actuator_j_1.relative_to = relative_to
ues_actuator_j_1.marker_name = '.GCMB.ges_upper_cylinder.ues_actuator_j_1'
_GCMB_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_1')
ues_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_1))
_GCMB_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_1')
ues_actuator_j_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_1.location, ues_actuator_j_1.orientation)
ues_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
ues_actuator_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_actuator_j_4 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.ues_actuator_j_4')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
ues_actuator_j_4.relative_to = relative_to
ues_actuator_j_4.marker_name = '.GCMB.ges_upper_cylinder.ues_actuator_j_4'
_GCMB_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_1')
ues_actuator_j_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_1))
_GCMB_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_1')
ues_actuator_j_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_4.location, ues_actuator_j_4.orientation)
ues_actuator_j_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
ues_actuator_j_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_upper_cylinder_geom1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom1')
gralin_upper_cylinder_geom1.cylinder_name = '.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom1'
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top').location
_GCMB_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_bot').location
gralin_upper_cylinder_geom1.length = (VecUtils.DM(_GCMB_ground_hps_uc_top, _GCMB_ground_hps_uc_bot))


gralin_upper_cylinder_geom2 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom2')
gralin_upper_cylinder_geom2.cylinder_name = '.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom2'
_GCMB_ground_hps_uc_sf_atch_l = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_sf_atch_l').location
_GCMB_ground_hps_uc_geompt = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_geompt').location
gralin_upper_cylinder_geom2.length = (VecUtils.DM(_GCMB_ground_hps_uc_sf_atch_l, _GCMB_ground_hps_uc_geompt))


gralin_upper_cylinder_geom3 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom3')
gralin_upper_cylinder_geom3.cylinder_name = '.GCMB.ges_upper_cylinder.gralin_upper_cylinder_geom3'
_GCMB_ground_hps_uc_sf_atch_r = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_sf_atch_r').location
_GCMB_ground_hps_uc_geompt = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_geompt').location
gralin_upper_cylinder_geom3.length = (VecUtils.DM(_GCMB_ground_hps_uc_sf_atch_r, _GCMB_ground_hps_uc_geompt))


MARKER_428 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.MARKER_428')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder')
MARKER_428.relative_to = relative_to
MARKER_428.marker_name = '.GCMB.ges_upper_cylinder.MARKER_428'
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top')
MARKER_428.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_428.location, MARKER_428.orientation)
MARKER_428.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.ges_lower_cylinder.inertia_frame'
_GCMB_ges_lower_cylinder_cm = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_lower_cylinder_cm))
_GCMB_ges_lower_cylinder = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_lower_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_5 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.gralin_5')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
gralin_5.relative_to = relative_to
gralin_5.marker_name = '.GCMB.ges_lower_cylinder.gralin_5'
_GCMB_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lc_top')
gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_lc_top))
_GCMB_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lc_top').location
_GCMB_ground_hps_lc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lc_bot').location
gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_lc_top, _GCMB_ground_hps_lc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_i_11 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.jxs_joint_i_11')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
jxs_joint_i_11.relative_to = relative_to
jxs_joint_i_11.marker_name = '.GCMB.ges_lower_cylinder.jxs_joint_i_11'
_GCMB_ges_upper_cylinder_jxs_joint_j_11 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_11')
jxs_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_11))
_GCMB_ges_upper_cylinder_jxs_joint_j_11 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_11')
jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_11))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
jxs_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_7 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.gralin_7')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
gralin_7.relative_to = relative_to
gralin_7.marker_name = '.GCMB.ges_lower_cylinder.gralin_7'
_GCMB_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpr_wheel_center1')
gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpr_wheel_center1))
_GCMB_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpr_wheel_center1').location
_GCMB_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center1').location
gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hpr_wheel_center1, _GCMB_ground_hpl_wheel_center1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_spring_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.ues_spring_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
ues_spring_i_1.relative_to = relative_to
ues_spring_i_1.marker_name = '.GCMB.ges_lower_cylinder.ues_spring_i_1'
_GCMB_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lc_top')
ues_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_i_1.location, ues_spring_i_1.orientation)
ues_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ues_damper_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.ues_damper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
ues_damper_i_1.relative_to = relative_to
ues_damper_i_1.marker_name = '.GCMB.ges_lower_cylinder.ues_damper_i_1'
_GCMB_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lc_top')
ues_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_i_1.location, ues_damper_i_1.orientation)
ues_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ues_stopper_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.ues_stopper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
ues_stopper_i_1.relative_to = relative_to
ues_stopper_i_1.marker_name = '.GCMB.ges_lower_cylinder.ues_stopper_i_1'
_GCMB_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lc_top')
ues_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_i_1.location, ues_stopper_i_1.orientation)
ues_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


coomarker_2 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.coomarker_2')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
coomarker_2.relative_to = relative_to
coomarker_2.marker_name = '.GCMB.ges_lower_cylinder.coomarker_2'
_GCMB_ground_cfs_wheel_centers_midpoint = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_wheel_centers_midpoint')
coomarker_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfs_wheel_centers_midpoint))
_GCMB_ground_cfs_wheel_centers_midpoint = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_wheel_centers_midpoint')
coomarker_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfs_wheel_centers_midpoint))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_2.location, coomarker_2.orientation)
coomarker_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
coomarker_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


coomarker_3 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.coomarker_3')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
coomarker_3.relative_to = relative_to
coomarker_3.marker_name = '.GCMB.ges_lower_cylinder.coomarker_3'
_GCMB_ground_cfs_nlg_axle_lowpoint = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_nlg_axle_lowpoint')
coomarker_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfs_nlg_axle_lowpoint))
_GCMB_ground_cfs_nlg_axle_lowpoint = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_nlg_axle_lowpoint')
coomarker_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfs_nlg_axle_lowpoint))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_3.location, coomarker_3.orientation)
coomarker_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
coomarker_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


MARKER_3 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.MARKER_3')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
MARKER_3.relative_to = relative_to
MARKER_3.marker_name = '.GCMB.ges_lower_cylinder.MARKER_3'
_GCMB_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center1')
MARKER_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpl_wheel_center1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_3.location, MARKER_3.orientation)
MARKER_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_4 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.MARKER_4')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
MARKER_4.relative_to = relative_to
MARKER_4.marker_name = '.GCMB.ges_lower_cylinder.MARKER_4'
_GCMB_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpr_wheel_center1')
MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hpr_wheel_center1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_4.location, MARKER_4.orientation)
MARKER_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_geom1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.gralin_geom1')
gralin_geom1.cylinder_name = '.GCMB.ges_lower_cylinder.gralin_geom1'
_GCMB_ground_hps_lc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lc_top').location
_GCMB_ground_hps_lc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lc_bot').location
gralin_geom1.length = (VecUtils.DM(_GCMB_ground_hps_lc_top, _GCMB_ground_hps_lc_bot))


gralin_geom2 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.gralin_geom2')
gralin_geom2.cylinder_name = '.GCMB.ges_lower_cylinder.gralin_geom2'
_GCMB_ground_hpr_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpr_wheel_center1').location
_GCMB_ground_hpl_wheel_center1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.hpl_wheel_center1').location
gralin_geom2.length = (VecUtils.DM(_GCMB_ground_hpr_wheel_center1, _GCMB_ground_hpl_wheel_center1))


MARKER_378 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder.MARKER_378')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_cylinder')
MARKER_378.relative_to = relative_to
MARKER_378.marker_name = '.GCMB.ges_lower_cylinder.MARKER_378'
_GCMB_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_lc_atch')
MARKER_378.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_lta_lc_atch))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_378.location, MARKER_378.orientation)
MARKER_378.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.ges_upper_torque_arm.inertia_frame'
_GCMB_ges_upper_torque_arm_cm = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_torque_arm_cm))
_GCMB_ges_upper_torque_arm = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_torque_arm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_9 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.gralin_9')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm')
gralin_9.relative_to = relative_to
gralin_9.marker_name = '.GCMB.ges_upper_torque_arm.gralin_9'
_GCMB_ground_hps_uta_uc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uta_uc_atch')
gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uta_uc_atch))
_GCMB_ground_hps_uta_uc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uta_uc_atch').location
_GCMB_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_uta_atch').location
gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_uta_uc_atch, _GCMB_ground_hps_lta_uta_atch, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_j_8 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.jxs_joint_j_8')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm')
jxs_joint_j_8.relative_to = relative_to
jxs_joint_j_8.marker_name = '.GCMB.ges_upper_torque_arm.jxs_joint_j_8'
_GCMB_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_uta_atch')
jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_lta_uta_atch))
_GCMB_ground_origo1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo1')
jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _GCMB_ground_origo1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
jxs_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_i_10 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.jxs_joint_i_10')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm')
jxs_joint_i_10.relative_to = relative_to
jxs_joint_i_10.marker_name = '.GCMB.ges_upper_torque_arm.jxs_joint_i_10'
_GCMB_ges_collar_jxs_joint_j_10 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_j_10')
jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_collar_jxs_joint_j_10))
_GCMB_ges_collar_jxs_joint_j_10 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_j_10')
jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_collar_jxs_joint_j_10))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
jxs_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_upper_torque_arm_geom = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
gralin_upper_torque_arm_geom.cylinder_name = '.GCMB.ges_upper_torque_arm.gralin_upper_torque_arm_geom'
_GCMB_ground_hps_uta_uc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uta_uc_atch').location
_GCMB_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_uta_atch').location
gralin_upper_torque_arm_geom.length = (VecUtils.DM(_GCMB_ground_hps_uta_uc_atch, _GCMB_ground_hps_lta_uta_atch))


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.ges_lower_torque_arm.inertia_frame'
_GCMB_ges_lower_torque_arm_cm = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_lower_torque_arm_cm))
_GCMB_ges_lower_torque_arm = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_lower_torque_arm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_i_8 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.jxs_joint_i_8')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm')
jxs_joint_i_8.relative_to = relative_to
jxs_joint_i_8.marker_name = '.GCMB.ges_lower_torque_arm.jxs_joint_i_8'
_GCMB_ges_upper_torque_arm_jxs_joint_j_8 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.jxs_joint_j_8')
jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_torque_arm_jxs_joint_j_8))
_GCMB_ges_upper_torque_arm_jxs_joint_j_8 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_torque_arm.jxs_joint_j_8')
jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_torque_arm_jxs_joint_j_8))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
jxs_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_10 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.gralin_10')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm')
gralin_10.relative_to = relative_to
gralin_10.marker_name = '.GCMB.ges_lower_torque_arm.gralin_10'
_GCMB_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_lc_atch')
gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_lta_lc_atch))
_GCMB_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_lc_atch').location
_GCMB_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_uta_atch').location
gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_lta_lc_atch, _GCMB_ground_hps_lta_uta_atch, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_lower_torque_arm_geom = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
gralin_lower_torque_arm_geom.cylinder_name = '.GCMB.ges_lower_torque_arm.gralin_lower_torque_arm_geom'
_GCMB_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_lc_atch').location
_GCMB_ground_hps_lta_uta_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_uta_atch').location
gralin_lower_torque_arm_geom.length = (VecUtils.DM(_GCMB_ground_hps_lta_lc_atch, _GCMB_ground_hps_lta_uta_atch))


MARKER_379 = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm.MARKER_379')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_lower_torque_arm')
MARKER_379.relative_to = relative_to
MARKER_379.marker_name = '.GCMB.ges_lower_torque_arm.MARKER_379'
_GCMB_ground_hps_lta_lc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_lta_lc_atch')
MARKER_379.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_lta_lc_atch))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_379.location, MARKER_379.orientation)
MARKER_379.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.ges_subframe_2.inertia_frame'
_GCMB_ges_subframe_2_cm = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_subframe_2_cm))
_GCMB_ges_subframe_2 = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_subframe_2))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


graout_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2.graout_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2')
graout_1.relative_to = relative_to
graout_1.marker_name = '.GCMB.ges_subframe_2.graout_1'
_GCMB_ground_hps_uc_sf_atch_r = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_sf_atch_r')
graout_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_sf_atch_r))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_1.location, graout_1.orientation)
graout_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


graout_2 = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2.graout_2')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2')
graout_2.relative_to = relative_to
graout_2.marker_name = '.GCMB.ges_subframe_2.graout_2'
_GCMB_ground_hps_uc_sf_atch_l = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_sf_atch_l')
graout_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_sf_atch_l))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_2.location, graout_2.orientation)
graout_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


graout_3 = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2.graout_3')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_subframe_2')
graout_3.relative_to = relative_to
graout_3.marker_name = '.GCMB.ges_subframe_2.graout_3'
_GCMB_ground_hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_db_sf_atch')
graout_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_db_sf_atch))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_3.location, graout_3.orientation)
graout_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


ELLIPSOID_38 = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2.ELLIPSOID_38')
ELLIPSOID_38.ellipsoid_name = '.GCMB.mts_body_mount_2.ELLIPSOID_38'


mts_body_mount_2 = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2')
mts_body_mount_2.part_name = '.GCMB.mts_body_mount_2'
_GCMB_ground_cfs_subframe_to_body_point = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_subframe_to_body_point')
mts_body_mount_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_cfs_subframe_to_body_point))
_GCMB_ground_origo1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo1')
mts_body_mount_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_origo1))


MARKER_427 = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2.MARKER_427')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.mts_body_mount_2')
MARKER_427.relative_to = relative_to
MARKER_427.marker_name = '.GCMB.mts_body_mount_2.MARKER_427'
_GCMB_ground_hps_uc_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_top')
MARKER_427.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_427.location, MARKER_427.orientation)
MARKER_427.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


jxs_joint_j_10 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_j_10')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar')
jxs_joint_j_10.relative_to = relative_to
jxs_joint_j_10.marker_name = '.GCMB.ges_collar.jxs_joint_j_10'
_GCMB_ground_hps_uta_uc_atch = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uta_uc_atch')
jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uta_uc_atch))
_GCMB_ground_origo1 = Jusme.ActiveUSScene.getObject('.GCMB.ground.origo1')
jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _GCMB_ground_origo1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
jxs_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.GCMB.ges_collar.inertia_frame'
_GCMB_ges_collar_cm = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_collar_cm))
_GCMB_ges_collar = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_collar))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_24 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.gralin_24')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar')
gralin_24.relative_to = relative_to
gralin_24.marker_name = '.GCMB.ges_collar.gralin_24'
_GCMB_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_bot')
gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ground_hps_uc_bot))
_GCMB_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_bot').location
_GCMB_ground_cfs_collar_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_collar_top').location
gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_GCMB_ground_hps_uc_bot, _GCMB_ground_cfs_collar_top, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar')
jxs_joint_i_1.relative_to = relative_to
jxs_joint_i_1.marker_name = '.GCMB.ges_collar.jxs_joint_i_1'
_GCMB_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_1')
jxs_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_1))
_GCMB_ges_upper_cylinder_jxs_joint_j_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_upper_cylinder.jxs_joint_j_1')
jxs_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_upper_cylinder_jxs_joint_j_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
jxs_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxs_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_actuator_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.ues_actuator_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar')
ues_actuator_i_1.relative_to = relative_to
ues_actuator_i_1.marker_name = '.GCMB.ges_collar.ues_actuator_i_1'
_GCMB_ges_collar_jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_i_1')
ues_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_collar_jxs_joint_i_1))
_GCMB_ges_collar_jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_i_1')
ues_actuator_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_collar_jxs_joint_i_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_1.location, ues_actuator_i_1.orientation)
ues_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
ues_actuator_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


ues_actuator_i_4 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.ues_actuator_i_4')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar')
ues_actuator_i_4.relative_to = relative_to
ues_actuator_i_4.marker_name = '.GCMB.ges_collar.ues_actuator_i_4'
_GCMB_ges_collar_jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_i_1')
ues_actuator_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_collar_jxs_joint_i_1))
_GCMB_ges_collar_jxs_joint_i_1 = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.jxs_joint_i_1')
ues_actuator_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _GCMB_ges_collar_jxs_joint_i_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_4.location, ues_actuator_i_4.orientation)
ues_actuator_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
ues_actuator_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_collar = Jusme.ActiveUSScene.getObject('.GCMB.ges_collar.gralin_collar')
gralin_collar.cylinder_name = '.GCMB.ges_collar.gralin_collar'
_GCMB_ground_hps_uc_bot = Jusme.ActiveUSScene.getObject('.GCMB.ground.hps_uc_bot').location
_GCMB_ground_cfs_collar_top = Jusme.ActiveUSScene.getObject('.GCMB.ground.cfs_collar_top').location
gralin_collar.length = (VecUtils.DM(_GCMB_ground_hps_uc_bot, _GCMB_ground_cfs_collar_top))


gfo_i = Jusme.ActiveUSScene.getObject('.GCMB.luntai1_2.wheel_part.gfo_i')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.luntai1_2.wheel_part')
gfo_i.relative_to = relative_to
gfo_i.marker_name = '.GCMB.luntai1_2.wheel_part.gfo_i'
_GCMB_luntai1_2_wheel_part_wheel_cm = Jusme.ActiveUSScene.getObject('.GCMB.luntai1_2.wheel_part.wheel_cm')
gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _GCMB_luntai1_2_wheel_part_wheel_cm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gfo_i = Jusme.ActiveUSScene.getObject('.GCMB.luntai2_2.wheel_part.gfo_i')
relative_to = Jusme.ActiveUSScene.getObject('.GCMB.luntai2_2.wheel_part')
gfo_i.relative_to = relative_to
gfo_i.marker_name = '.GCMB.luntai2_2.wheel_part.gfo_i'
_GCMB_luntai2_2_wheel_part_wheel_cm = Jusme.ActiveUSScene.getObject('.GCMB.luntai2_2.wheel_part.wheel_cm')
gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _GCMB_luntai2_2_wheel_part_wheel_cm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


steel = Jusme.ActiveUSScene.getObject('.GCMB.steel')
steel.material_name = '.GCMB.steel'



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
cfs_subframe_ref = MakeSceneNodeByType('Marker', '.turn.ground.cfs_subframe_ref')
cfs_subframe_ref.marker_name = '.turn.ground.cfs_subframe_ref'
cfs_subframe_ref.adams_id = 3
cfs_subframe_ref.location = Base.Vector (11.550194959, 0.0, 2.1282477971)
cfs_subframe_ref.orientation = Base.Vector (180.0, 90.0, 177.5464650677)
cfl_spin_axis = MakeSceneNodeByType('Marker', '.turn.ground.cfl_spin_axis')
cfl_spin_axis.marker_name = '.turn.ground.cfl_spin_axis'
cfl_spin_axis.adams_id = 4
cfl_spin_axis.location = Base.Vector (12.2709739569, -1.8115919597, 0.1742595194)
cfl_spin_axis.orientation = Base.Vector (179.9999064666, 88.9999687773, 0.0053591761151)
cfr_spin_axis = MakeSceneNodeByType('Marker', '.turn.ground.cfr_spin_axis')
cfr_spin_axis.marker_name = '.turn.ground.cfr_spin_axis'
cfr_spin_axis.adams_id = 5
cfr_spin_axis.location = Base.Vector (12.2709739569, 1.8115919597, 0.1742595194)
cfr_spin_axis.orientation = Base.Vector (9.3533439964e-05, 88.9999687773, 179.9946408239)
cfl_torque_arm_refplane = MakeSceneNodeByType('Marker', '.turn.ground.cfl_torque_arm_refplane')
cfl_torque_arm_refplane.marker_name = '.turn.ground.cfl_torque_arm_refplane'
cfl_torque_arm_refplane.adams_id = 6
cfl_torque_arm_refplane.location = Base.Vector (12.5098362975, -1.6395888469, 0.5076864953)
cfl_torque_arm_refplane.orientation = Base.Vector (55.1145661544, 175.2828647294, 80.2814243968)
cfr_torque_arm_refplane = MakeSceneNodeByType('Marker', '.turn.ground.cfr_torque_arm_refplane')
cfr_torque_arm_refplane.marker_name = '.turn.ground.cfr_torque_arm_refplane'
cfr_torque_arm_refplane.adams_id = 7
cfr_torque_arm_refplane.location = Base.Vector (12.5098362975, 1.6395888469, 0.5076864953)
cfr_torque_arm_refplane.orientation = Base.Vector (124.8854338456, 175.2828647294, 99.7185756032)
cfl_dragbrace_refplane = MakeSceneNodeByType('Marker', '.turn.ground.cfl_dragbrace_refplane')
cfl_dragbrace_refplane.marker_name = '.turn.ground.cfl_dragbrace_refplane'
cfl_dragbrace_refplane.adams_id = 8
cfl_dragbrace_refplane.location = Base.Vector (12.070313934, -1.5107420843, 1.6281029812)
cfl_dragbrace_refplane.orientation = Base.Vector (238.6248285507, 75.5183095506, 100.5979151393)
cfr_dragbrace_refplane = MakeSceneNodeByType('Marker', '.turn.ground.cfr_dragbrace_refplane')
cfr_dragbrace_refplane.marker_name = '.turn.ground.cfr_dragbrace_refplane'
cfr_dragbrace_refplane.adams_id = 9
cfr_dragbrace_refplane.location = Base.Vector (12.070313934, 1.5107420843, 1.6281029812)
cfr_dragbrace_refplane.orientation = Base.Vector (301.3751714493, 75.5183095506, 79.4020848607)
cfl_uc_sf_atch = MakeSceneNodeByType('Marker', '.turn.ground.cfl_uc_sf_atch')
cfl_uc_sf_atch.marker_name = '.turn.ground.cfl_uc_sf_atch'
cfl_uc_sf_atch.adams_id = 10
cfl_uc_sf_atch.location = Base.Vector (12.1457499909, -1.2447481722, 2.1230446312)
cfl_uc_sf_atch.orientation = Base.Vector (357.5219193201, 81.1274829118, 15.673741043)
cfr_uc_sf_atch = MakeSceneNodeByType('Marker', '.turn.ground.cfr_uc_sf_atch')
cfr_uc_sf_atch.marker_name = '.turn.ground.cfr_uc_sf_atch'
cfr_uc_sf_atch.adams_id = 11
cfr_uc_sf_atch.location = Base.Vector (12.1457499909, 1.2447481722, 2.1230446312)
cfr_uc_sf_atch.orientation = Base.Vector (182.4780806799, 81.1274829118, 164.326258957)
cfl_axial_reference = MakeSceneNodeByType('Marker', '.turn.ground.cfl_axial_reference')
cfl_axial_reference.marker_name = '.turn.ground.cfl_axial_reference'
cfl_axial_reference.adams_id = 13
cfl_axial_reference.location = Base.Vector (12.2709748205, -1.5322348019, 0.1791298424)
cfl_axial_reference.orientation = Base.Vector (235.1145661682, 4.7171352712, 124.7942832293)
cfr_axial_reference = MakeSceneNodeByType('Marker', '.turn.ground.cfr_axial_reference')
cfr_axial_reference.marker_name = '.turn.ground.cfr_axial_reference'
cfr_axial_reference.adams_id = 14
cfr_axial_reference.location = Base.Vector (12.2709748205, 1.5322348019, 0.1791298424)
cfr_axial_reference.orientation = Base.Vector (304.8854338318, 4.7171352712, 55.2057167707)
cfl_uc_bot = MakeSceneNodeByType('Marker', '.turn.ground.cfl_uc_bot')
cfl_uc_bot.marker_name = '.turn.ground.cfl_uc_bot'
cfl_uc_bot.adams_id = 15
cfl_uc_bot.location = Base.Vector (12.2346840721, -1.5069317388, 0.7152796436)
cfl_uc_bot.orientation = Base.Vector (0.0, 0.0, 0.0)
cfr_uc_bot = MakeSceneNodeByType('Marker', '.turn.ground.cfr_uc_bot')
cfr_uc_bot.marker_name = '.turn.ground.cfr_uc_bot'
cfr_uc_bot.adams_id = 16
cfr_uc_bot.location = Base.Vector (12.2346840721, 1.5069317388, 0.7152796436)
cfr_uc_bot.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_uc_top = MakeSceneNodeByType('Marker', '.turn.ground.cfl_uc_top')
cfl_uc_top.marker_name = '.turn.ground.cfl_uc_top'
cfl_uc_top.adams_id = 17
cfl_uc_top.location = Base.Vector (12.137340597, -1.4390607744, 2.1534060818)
cfl_uc_top.orientation = Base.Vector (0.0, 0.0, 0.0)
cfr_uc_top = MakeSceneNodeByType('Marker', '.turn.ground.cfr_uc_top')
cfr_uc_top.marker_name = '.turn.ground.cfr_uc_top'
cfr_uc_top.adams_id = 18
cfr_uc_top.location = Base.Vector (12.137340597, 1.4390607744, 2.1534060818)
cfr_uc_top.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_lc_top = MakeSceneNodeByType('Marker', '.turn.ground.cfl_lc_top')
cfl_lc_top.marker_name = '.turn.ground.cfl_lc_top'
cfl_lc_top.adams_id = 19
cfl_lc_top.location = Base.Vector (12.2057611337, -1.486765747, 1.1425793908)
cfl_lc_top.orientation = Base.Vector (0.0, 0.0, 0.0)
cfr_lc_top = MakeSceneNodeByType('Marker', '.turn.ground.cfr_lc_top')
cfr_lc_top.marker_name = '.turn.ground.cfr_lc_top'
cfr_lc_top.adams_id = 20
cfr_lc_top.location = Base.Vector (12.2057611337, 1.486765747, 1.1425793908)
cfr_lc_top.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_uta_uc_atch = MakeSceneNodeByType('Marker', '.turn.ground.cfl_uta_uc_atch')
cfl_uta_uc_atch.marker_name = '.turn.ground.cfl_uta_uc_atch'
cfl_uta_uc_atch.adams_id = 21
cfl_uta_uc_atch.location = Base.Vector (12.2346840721, -1.5069317388, 0.7152796436)
cfl_uta_uc_atch.orientation = Base.Vector (0.0, 0.0, 0.0)
cfr_uta_uc_atch = MakeSceneNodeByType('Marker', '.turn.ground.cfr_uta_uc_atch')
cfr_uta_uc_atch.marker_name = '.turn.ground.cfr_uta_uc_atch'
cfr_uta_uc_atch.adams_id = 22
cfr_uta_uc_atch.location = Base.Vector (12.2346840721, 1.5069317388, 0.7152796436)
cfr_uta_uc_atch.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_lta_lc_atch = MakeSceneNodeByType('Marker', '.turn.ground.cfl_lta_lc_atch')
cfl_lta_lc_atch.marker_name = '.turn.ground.cfl_lta_lc_atch'
cfl_lta_lc_atch.adams_id = 23
cfl_lta_lc_atch.location = Base.Vector (12.2709748205, -1.5322348019, 0.1791298424)
cfl_lta_lc_atch.orientation = Base.Vector (0.0, 0.0, 0.0)
cfr_lta_lc_atch = MakeSceneNodeByType('Marker', '.turn.ground.cfr_lta_lc_atch')
cfr_lta_lc_atch.marker_name = '.turn.ground.cfr_lta_lc_atch'
cfr_lta_lc_atch.adams_id = 24
cfr_lta_lc_atch.location = Base.Vector (12.2709748205, 1.5322348019, 0.1791298424)
cfr_lta_lc_atch.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_collar_top = MakeSceneNodeByType('Marker', '.turn.ground.cfl_collar_top')
cfl_collar_top.marker_name = '.turn.ground.cfl_collar_top'
cfl_collar_top.adams_id = 25
cfl_collar_top.location = Base.Vector (12.2161847889, -1.4940334506, 0.9885831006)
cfl_collar_top.orientation = Base.Vector (55.1145661682, 175.2828647288, 235.2057167707)
cfr_collar_top = MakeSceneNodeByType('Marker', '.turn.ground.cfr_collar_top')
cfr_collar_top.marker_name = '.turn.ground.cfr_collar_top'
cfr_collar_top.adams_id = 26
cfr_collar_top.location = Base.Vector (12.2161847889, 1.4940334506, 0.9885831006)
cfr_collar_top.orientation = Base.Vector (124.8854338318, 175.2828647288, 304.7942832293)
cfl_collar_bot = MakeSceneNodeByType('Marker', '.turn.ground.cfl_collar_bot')
cfl_collar_bot.marker_name = '.turn.ground.cfl_collar_bot'
cfl_collar_bot.adams_id = 27
cfl_collar_bot.location = Base.Vector (12.2308845535, -1.5042825936, 0.7714127142)
cfl_collar_bot.orientation = Base.Vector (55.1145661682, 175.2828647288, 235.2057167707)
cfr_collar_bot = MakeSceneNodeByType('Marker', '.turn.ground.cfr_collar_bot')
cfr_collar_bot.marker_name = '.turn.ground.cfr_collar_bot'
cfr_collar_bot.adams_id = 28
cfr_collar_bot.location = Base.Vector (12.2308845535, 1.5042825936, 0.7714127142)
cfr_collar_bot.orientation = Base.Vector (124.8854338318, 175.2828647288, 304.7942832293)
cfl_plane_ref = MakeSceneNodeByType('Marker', '.turn.ground.cfl_plane_ref')
cfl_plane_ref.marker_name = '.turn.ground.cfl_plane_ref'
cfl_plane_ref.adams_id = 29
cfl_plane_ref.location = Base.Vector (11.7904549128, -1.3312381859, 1.4785418122)
cfl_plane_ref.orientation = Base.Vector (70.4651741872, 87.6875364203, 268.7516172662)
cfr_plane_ref = MakeSceneNodeByType('Marker', '.turn.ground.cfr_plane_ref')
cfr_plane_ref.marker_name = '.turn.ground.cfr_plane_ref'
cfr_plane_ref.adams_id = 30
cfr_plane_ref.location = Base.Vector (11.7904549128, 1.3312381859, 1.4785418122)
cfr_plane_ref.orientation = Base.Vector (109.5348258128, 87.6875364203, 271.2483827338)
cfl_plane_ref_2 = MakeSceneNodeByType('Marker', '.turn.ground.cfl_plane_ref_2')
cfl_plane_ref_2.marker_name = '.turn.ground.cfl_plane_ref_2'
cfl_plane_ref_2.adams_id = 31
cfl_plane_ref_2.location = Base.Vector (11.7904549128, -1.3312381859, 1.4785418122)
cfl_plane_ref_2.orientation = Base.Vector (160.4147950495, 91.2473659421, 267.6869880055)
cfr_plane_ref_2 = MakeSceneNodeByType('Marker', '.turn.ground.cfr_plane_ref_2')
cfr_plane_ref_2.marker_name = '.turn.ground.cfr_plane_ref_2'
cfr_plane_ref_2.adams_id = 32
cfr_plane_ref_2.location = Base.Vector (11.7904549128, 1.3312381859, 1.4785418122)
cfr_plane_ref_2.orientation = Base.Vector (19.5852049505, 91.2473659421, 272.3130119945)
cfl_lwract_top = MakeSceneNodeByType('Marker', '.turn.ground.cfl_lwract_top')
cfl_lwract_top.marker_name = '.turn.ground.cfl_lwract_top'
cfl_lwract_top.adams_id = 33
cfl_lwract_top.location = Base.Vector (12.301784069, -1.2914705743, 1.9010842639)
cfl_lwract_top.orientation = Base.Vector (182.4778087702, 7.7973026753, 177.4990974089)
cfr_lwract_top = MakeSceneNodeByType('Marker', '.turn.ground.cfr_lwract_top')
cfr_lwract_top.marker_name = '.turn.ground.cfr_lwract_top'
cfr_lwract_top.adams_id = 34
cfr_lwract_top.location = Base.Vector (12.301784069, 1.2914705743, 1.9010842639)
cfr_lwract_top.orientation = Base.Vector (357.5221912298, 7.7973026753, 2.5009025911)
cfl_upract_bot = MakeSceneNodeByType('Marker', '.turn.ground.cfl_upract_bot')
cfl_upract_bot.marker_name = '.turn.ground.cfl_upract_bot'
cfl_upract_bot.adams_id = 35
cfl_upract_bot.location = Base.Vector (12.3037747523, -1.337473576, 1.5648221485)
cfl_upract_bot.orientation = Base.Vector (182.4778087702, 7.7973026753, 177.4990974089)
cfr_upract_bot = MakeSceneNodeByType('Marker', '.turn.ground.cfr_upract_bot')
cfr_upract_bot.marker_name = '.turn.ground.cfr_upract_bot'
cfr_upract_bot.adams_id = 36
cfr_upract_bot.location = Base.Vector (12.3037747523, 1.337473576, 1.5648221485)
cfr_upract_bot.orientation = Base.Vector (357.5221912298, 7.7973026753, 2.5009025911)
cfl_spin_axis_1 = MakeSceneNodeByType('Marker', '.turn.ground.cfl_spin_axis_1')
cfl_spin_axis_1.marker_name = '.turn.ground.cfl_spin_axis_1'
cfl_spin_axis_1.adams_id = 37
cfl_spin_axis_1.location = Base.Vector (12.2709739569, -1.8115919597, 0.1742595194)
cfl_spin_axis_1.orientation = Base.Vector (359.9999064666, 91.0000312227, 179.9946408239)
cfr_spin_axis_1 = MakeSceneNodeByType('Marker', '.turn.ground.cfr_spin_axis_1')
cfr_spin_axis_1.marker_name = '.turn.ground.cfr_spin_axis_1'
cfr_spin_axis_1.adams_id = 38
cfr_spin_axis_1.location = Base.Vector (12.2709739569, 1.8115919597, 0.1742595194)
cfr_spin_axis_1.orientation = Base.Vector (180.0000935334, 91.0000312227, 0.0053591761151)
cfl_ldb_geompt_1 = MakeSceneNodeByType('Marker', '.turn.ground.cfl_ldb_geompt_1')
cfl_ldb_geompt_1.marker_name = '.turn.ground.cfl_ldb_geompt_1'
cfl_ldb_geompt_1.adams_id = 39
cfl_ldb_geompt_1.location = Base.Vector (11.8912081251, -1.3781308467, 1.1458304614)
cfl_ldb_geompt_1.orientation = Base.Vector (0.0, 0.0, 0.0)
cfr_ldb_geompt_1 = MakeSceneNodeByType('Marker', '.turn.ground.cfr_ldb_geompt_1')
cfr_ldb_geompt_1.marker_name = '.turn.ground.cfr_ldb_geompt_1'
cfr_ldb_geompt_1.adams_id = 40
cfr_ldb_geompt_1.location = Base.Vector (11.8912081251, 1.3781308467, 1.1458304614)
cfr_ldb_geompt_1.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_ldb_geompt_2 = MakeSceneNodeByType('Marker', '.turn.ground.cfl_ldb_geompt_2')
cfl_ldb_geompt_2.marker_name = '.turn.ground.cfl_ldb_geompt_2'
cfl_ldb_geompt_2.adams_id = 41
cfl_ldb_geompt_2.location = Base.Vector (11.9606643032, -1.4050660792, 1.0737874161)
cfl_ldb_geompt_2.orientation = Base.Vector (0.0, 0.0, 0.0)
cfr_ldb_geompt_2 = MakeSceneNodeByType('Marker', '.turn.ground.cfr_ldb_geompt_2')
cfr_ldb_geompt_2.marker_name = '.turn.ground.cfr_ldb_geompt_2'
cfr_ldb_geompt_2.adams_id = 42
cfr_ldb_geompt_2.location = Base.Vector (11.9606643032, 1.4050660792, 1.0737874161)
cfr_ldb_geompt_2.orientation = Base.Vector (0.0, 0.0, 0.0)
cfl_aero_ref = MakeSceneNodeByType('Marker', '.turn.ground.cfl_aero_ref')
cfl_aero_ref.marker_name = '.turn.ground.cfl_aero_ref'
cfl_aero_ref.adams_id = 43
cfl_aero_ref.location = Base.Vector (12.137340597, -1.4390607744, 2.1534060818)
cfl_aero_ref.orientation = Base.Vector (0.0, 0.0, 0.0)
cfr_aero_ref = MakeSceneNodeByType('Marker', '.turn.ground.cfr_aero_ref')
cfr_aero_ref.marker_name = '.turn.ground.cfr_aero_ref'
cfr_aero_ref.adams_id = 44
cfr_aero_ref.location = Base.Vector (12.137340597, 1.4390607744, 2.1534060818)
cfr_aero_ref.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_gearaero_origin_1 = MakeSceneNodeByType('Marker', '.turn.ground.uel_gearaero_origin_1')
uel_gearaero_origin_1.marker_name = '.turn.ground.uel_gearaero_origin_1'
uel_gearaero_origin_1.adams_id = 45
uel_gearaero_origin_1.location = Base.Vector (0.0, 0.0, 0.0)
uel_gearaero_origin_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_gearaero_rm_1 = MakeSceneNodeByType('Marker', '.turn.ground.uel_gearaero_rm_1')
uel_gearaero_rm_1.marker_name = '.turn.ground.uel_gearaero_rm_1'
uel_gearaero_rm_1.adams_id = 46
uel_gearaero_rm_1.location = Base.Vector (12.137340597, -1.4390607744, 2.1534060818)
uel_gearaero_rm_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_gearaero_origin_1 = MakeSceneNodeByType('Marker', '.turn.ground.uer_gearaero_origin_1')
uer_gearaero_origin_1.marker_name = '.turn.ground.uer_gearaero_origin_1'
uer_gearaero_origin_1.adams_id = 47
uer_gearaero_origin_1.location = Base.Vector (0.0, 0.0, 0.0)
uer_gearaero_origin_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_gearaero_rm_1 = MakeSceneNodeByType('Marker', '.turn.ground.uer_gearaero_rm_1')
uer_gearaero_rm_1.marker_name = '.turn.ground.uer_gearaero_rm_1'
uer_gearaero_rm_1.adams_id = 48
uer_gearaero_rm_1.location = Base.Vector (12.137340597, 1.4390607744, 2.1534060818)
uer_gearaero_rm_1.orientation = Base.Vector (0.0, 0.0, 0.0)
origo1 = MakeSceneNodeByType('Marker', '.turn.ground.origo1')
origo1.marker_name = '.turn.ground.origo1'
origo1.adams_id = 287
origo1.location = Base.Vector (0.0, 0.0, 0.0)
origo1.orientation = Base.Vector (0.0, 0.0, 0.0)
hpl_udb_spndl_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_udb_spndl_atch_1')
hpl_udb_spndl_atch_1.point_name = '.turn.ground.hpl_udb_spndl_atch_1'
hpl_udb_spndl_atch_1.location = Base.Vector (10.963049321, -1.0224189813, 2.1030895124)
hpr_udb_spndl_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_udb_spndl_atch_1')
hpr_udb_spndl_atch_1.point_name = '.turn.ground.hpr_udb_spndl_atch_1'
hpr_udb_spndl_atch_1.location = Base.Vector (10.963049321, 1.0224189813, 2.1030895124)
hpl_ib_uc_sf_atch = MakeSceneNodeByType('Point', '.turn.ground.hpl_ib_uc_sf_atch')
hpl_ib_uc_sf_atch.point_name = '.turn.ground.hpl_ib_uc_sf_atch'
hpl_ib_uc_sf_atch.location = Base.Vector (12.1541593848, -1.0504355699, 2.0926831806)
hpr_ib_uc_sf_atch = MakeSceneNodeByType('Point', '.turn.ground.hpr_ib_uc_sf_atch')
hpr_ib_uc_sf_atch.point_name = '.turn.ground.hpr_ib_uc_sf_atch'
hpr_ib_uc_sf_atch.location = Base.Vector (12.1541593848, 1.0504355699, 2.0926831806)
hpl_wheel_center = MakeSceneNodeByType('Point', '.turn.ground.hpl_wheel_center')
hpl_wheel_center.point_name = '.turn.ground.hpl_wheel_center'
hpl_wheel_center.location = Base.Vector (12.2709739569, -1.8115919597, 0.1742595194)
hpr_wheel_center = MakeSceneNodeByType('Point', '.turn.ground.hpr_wheel_center')
hpr_wheel_center.point_name = '.turn.ground.hpr_wheel_center'
hpr_wheel_center.location = Base.Vector (12.2709739569, 1.8115919597, 0.1742595194)
hpl_lc_bot = MakeSceneNodeByType('Point', '.turn.ground.hpl_lc_bot')
hpl_lc_bot.point_name = '.turn.ground.hpl_lc_bot'
hpl_lc_bot.location = Base.Vector (12.2709748205, -1.5322348019, 0.1791298424)
hpr_lc_bot = MakeSceneNodeByType('Point', '.turn.ground.hpr_lc_bot')
hpr_lc_bot.point_name = '.turn.ground.hpr_lc_bot'
hpr_lc_bot.location = Base.Vector (12.2709748205, 1.5322348019, 0.1791298424)
hpl_ob_axle = MakeSceneNodeByType('Point', '.turn.ground.hpl_ob_axle')
hpl_ob_axle.point_name = '.turn.ground.hpl_ob_axle'
hpl_ob_axle.location = Base.Vector (12.2709737181, -1.9578736763, 0.1717060828)
hpr_ob_axle = MakeSceneNodeByType('Point', '.turn.ground.hpr_ob_axle')
hpr_ob_axle.point_name = '.turn.ground.hpr_ob_axle'
hpr_ob_axle.location = Base.Vector (12.2709737181, 1.9578736763, 0.1717060828)
hpl_ib_axle = MakeSceneNodeByType('Point', '.turn.ground.hpl_ib_axle')
hpl_ib_axle.point_name = '.turn.ground.hpl_ib_axle'
hpl_ib_axle.location = Base.Vector (12.2709748205, -1.532234807, 0.1791298424)
hpr_ib_axle = MakeSceneNodeByType('Point', '.turn.ground.hpr_ib_axle')
hpr_ib_axle.point_name = '.turn.ground.hpr_ib_axle'
hpr_ib_axle.location = Base.Vector (12.2709748205, 1.532234807, 0.1791298424)
hpl_uc_top = MakeSceneNodeByType('Point', '.turn.ground.hpl_uc_top')
hpl_uc_top.point_name = '.turn.ground.hpl_uc_top'
hpl_uc_top.location = Base.Vector (12.137340597, -1.4390607744, 2.1534060818)
hpr_uc_top = MakeSceneNodeByType('Point', '.turn.ground.hpr_uc_top')
hpr_uc_top.point_name = '.turn.ground.hpr_uc_top'
hpr_uc_top.location = Base.Vector (12.137340597, 1.4390607744, 2.1534060818)
hpl_uc_geompt = MakeSceneNodeByType('Point', '.turn.ground.hpl_uc_geompt')
hpl_uc_geompt.point_name = '.turn.ground.hpl_uc_geompt'
hpl_uc_geompt.location = Base.Vector (12.1670316222, -1.3594512257, 1.7617947238)
hpr_uc_geompt = MakeSceneNodeByType('Point', '.turn.ground.hpr_uc_geompt')
hpr_uc_geompt.point_name = '.turn.ground.hpr_uc_geompt'
hpr_uc_geompt.location = Base.Vector (12.1670316222, 1.3594512257, 1.7617947238)
hpl_stator_attach = MakeSceneNodeByType('Point', '.turn.ground.hpl_stator_attach')
hpl_stator_attach.point_name = '.turn.ground.hpl_stator_attach'
hpl_stator_attach.location = Base.Vector (12.2709740483, -1.7544506694, 0.175256952)
hpr_stator_attach = MakeSceneNodeByType('Point', '.turn.ground.hpr_stator_attach')
hpr_stator_attach.point_name = '.turn.ground.hpr_stator_attach'
hpr_stator_attach.location = Base.Vector (12.2709740483, 1.7544506694, 0.175256952)
hpl_ldb_uc_atch = MakeSceneNodeByType('Point', '.turn.ground.hpl_ldb_uc_atch')
hpl_ldb_uc_atch.point_name = '.turn.ground.hpl_ldb_uc_atch'
hpl_ldb_uc_atch.location = Base.Vector (12.54125, -1.8542, 1.21285)
hpr_ldb_uc_atch = MakeSceneNodeByType('Point', '.turn.ground.hpr_ldb_uc_atch')
hpr_ldb_uc_atch.point_name = '.turn.ground.hpr_ldb_uc_atch'
hpr_ldb_uc_atch.location = Base.Vector (12.54125, 1.8542, 1.21285)
hpl_ldb_udb_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_ldb_udb_atch_1')
hpl_ldb_udb_atch_1.point_name = '.turn.ground.hpl_ldb_udb_atch_1'
hpl_ldb_udb_atch_1.location = Base.Vector (11.532351205, -1.2389654784, 1.5180528618)
hpr_ldb_udb_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_ldb_udb_atch_1')
hpr_ldb_udb_atch_1.point_name = '.turn.ground.hpr_ldb_udb_atch_1'
hpr_ldb_udb_atch_1.location = Base.Vector (11.532351205, 1.2389654784, 1.5180528618)
hpl_lta_uta_atch = MakeSceneNodeByType('Point', '.turn.ground.hpl_lta_uta_atch')
hpl_lta_uta_atch.point_name = '.turn.ground.hpl_lta_uta_atch'
hpl_lta_uta_atch.location = Base.Vector (13.02385, -1.8796, 0.62865)
hpr_lta_uta_atch = MakeSceneNodeByType('Point', '.turn.ground.hpr_lta_uta_atch')
hpr_lta_uta_atch.point_name = '.turn.ground.hpr_lta_uta_atch'
hpr_lta_uta_atch.location = Base.Vector (13.02385, 1.8796, 0.62865)
hpl_lta_connect_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_lta_connect_atch_1')
hpl_lta_connect_atch_1.point_name = '.turn.ground.hpl_lta_connect_atch_1'
hpl_lta_connect_atch_1.location = Base.Vector (12.048547912, -1.5622090168, 0.5321183668)
hpr_lta_connect_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_lta_connect_atch_1')
hpr_lta_connect_atch_1.point_name = '.turn.ground.hpr_lta_connect_atch_1'
hpr_lta_connect_atch_1.location = Base.Vector (12.048547912, 1.5622090168, 0.5321183668)
hpl_uta_connect_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_uta_connect_atch_1')
hpl_uta_connect_atch_1.point_name = '.turn.ground.hpl_uta_connect_atch_1'
hpl_uta_connect_atch_1.location = Base.Vector (12.0522523496, -1.4912788564, 0.5290216242)
hpr_uta_connect_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_uta_connect_atch_1')
hpr_uta_connect_atch_1.point_name = '.turn.ground.hpr_uta_connect_atch_1'
hpr_uta_connect_atch_1.location = Base.Vector (12.0522523496, 1.4912788564, 0.5290216242)
hpl_uta_connect_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpl_uta_connect_atch_2')
hpl_uta_connect_atch_2.point_name = '.turn.ground.hpl_uta_connect_atch_2'
hpl_uta_connect_atch_2.location = Base.Vector (12.087047708, -1.4934025504, 0.5220012166)
hpr_uta_connect_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpr_uta_connect_atch_2')
hpr_uta_connect_atch_2.point_name = '.turn.ground.hpr_uta_connect_atch_2'
hpr_uta_connect_atch_2.location = Base.Vector (12.087047708, 1.4934025504, 0.5220012166)
hpl_lta_lc_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_lta_lc_atch_1')
hpl_lta_lc_atch_1.point_name = '.turn.ground.hpl_lta_lc_atch_1'
hpl_lta_lc_atch_1.location = Base.Vector (12.150137371, -1.5536660062, 0.2740663556)
hpr_lta_lc_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_lta_lc_atch_1')
hpr_lta_lc_atch_1.point_name = '.turn.ground.hpr_lta_lc_atch_1'
hpr_lta_lc_atch_1.location = Base.Vector (12.150137371, 1.5536660062, 0.2740663556)
hpl_lta_lc_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpl_lta_lc_atch_2')
hpl_lta_lc_atch_2.point_name = '.turn.ground.hpl_lta_lc_atch_2'
hpl_lta_lc_atch_2.location = Base.Vector (12.1525627408, -1.5072279736, 0.2720389276)
hpr_lta_lc_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpr_lta_lc_atch_2')
hpr_lta_lc_atch_2.point_name = '.turn.ground.hpr_lta_lc_atch_2'
hpr_lta_lc_atch_2.location = Base.Vector (12.1525627408, 1.5072279736, 0.2720389276)
hpl_uta_collar_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_uta_collar_atch_1')
hpl_uta_collar_atch_1.point_name = '.turn.ground.hpl_uta_collar_atch_1'
hpl_uta_collar_atch_1.location = Base.Vector (12.1066524694, -1.4965360468, 0.800236779)
hpr_uta_collar_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_uta_collar_atch_1')
hpr_uta_collar_atch_1.point_name = '.turn.ground.hpr_uta_collar_atch_1'
hpr_uta_collar_atch_1.location = Base.Vector (12.1066524694, 1.4965360468, 0.800236779)
hpl_uta_collar_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpl_uta_collar_atch_2')
hpl_uta_collar_atch_2.point_name = '.turn.ground.hpl_uta_collar_atch_2'
hpl_uta_collar_atch_2.location = Base.Vector (12.1102139304, -1.428342457, 0.797259518)
hpr_uta_collar_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpr_uta_collar_atch_2')
hpr_uta_collar_atch_2.point_name = '.turn.ground.hpr_uta_collar_atch_2'
hpr_uta_collar_atch_2.location = Base.Vector (12.1102139304, 1.428342457, 0.797259518)
hpl_collar_top = MakeSceneNodeByType('Point', '.turn.ground.hpl_collar_top')
hpl_collar_top.point_name = '.turn.ground.hpl_collar_top'
hpl_collar_top.location = Base.Vector (12.216682831, -1.4943808822, 0.9812211008)
hpr_collar_top = MakeSceneNodeByType('Point', '.turn.ground.hpr_collar_top')
hpr_collar_top.point_name = '.turn.ground.hpr_collar_top'
hpr_collar_top.location = Base.Vector (12.216682831, 1.4943808822, 0.9812211008)
hpl_collar_bot = MakeSceneNodeByType('Point', '.turn.ground.hpl_collar_bot')
hpl_collar_bot.point_name = '.turn.ground.hpl_collar_bot'
hpl_collar_bot.location = Base.Vector (12.2313550394, -1.5046108084, 0.7644576024)
hpr_collar_bot = MakeSceneNodeByType('Point', '.turn.ground.hpr_collar_bot')
hpr_collar_bot.point_name = '.turn.ground.hpr_collar_bot'
hpr_collar_bot.location = Base.Vector (12.2313550394, 1.5046108084, 0.7644576024)
hpl_upr_strt_bot = MakeSceneNodeByType('Point', '.turn.ground.hpl_upr_strt_bot')
hpl_upr_strt_bot.point_name = '.turn.ground.hpl_upr_strt_bot'
hpl_upr_strt_bot.location = Base.Vector (12.2327072846, -1.5055538596, 0.7444805024)
hpr_upr_strt_bot = MakeSceneNodeByType('Point', '.turn.ground.hpr_upr_strt_bot')
hpr_upr_strt_bot.point_name = '.turn.ground.hpr_upr_strt_bot'
hpr_upr_strt_bot.location = Base.Vector (12.2327072846, 1.5055538596, 0.7444805024)
hpl_upr_strt_top = MakeSceneNodeByType('Point', '.turn.ground.hpl_upr_strt_top')
hpl_upr_strt_top.point_name = '.turn.ground.hpl_upr_strt_top'
hpl_upr_strt_top.location = Base.Vector (12.1478181986, -1.4463662462, 1.9986101506)
hpr_upr_strt_top = MakeSceneNodeByType('Point', '.turn.ground.hpr_upr_strt_top')
hpr_upr_strt_top.point_name = '.turn.ground.hpr_upr_strt_top'
hpr_upr_strt_top.location = Base.Vector (12.1478181986, 1.4463662462, 1.9986101506)
hpl_lwract_uc_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_lwract_uc_atch_1')
hpl_lwract_uc_atch_1.point_name = '.turn.ground.hpl_lwract_uc_atch_1'
hpl_lwract_uc_atch_1.location = Base.Vector (12.3053060472, -1.3728605004, 1.3061589828)
hpr_lwract_uc_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_lwract_uc_atch_1')
hpr_lwract_uc_atch_1.point_name = '.turn.ground.hpr_lwract_uc_atch_1'
hpr_lwract_uc_atch_1.location = Base.Vector (12.3053060472, 1.3728605004, 1.3061589828)
hpl_lwract_uc_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpl_lwract_uc_atch_2')
hpl_lwract_uc_atch_2.point_name = '.turn.ground.hpl_lwract_uc_atch_2'
hpl_lwract_uc_atch_2.location = Base.Vector (12.306350165, -1.3555888052, 1.3038056982)
hpr_lwract_uc_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpr_lwract_uc_atch_2')
hpr_lwract_uc_atch_2.point_name = '.turn.ground.hpr_lwract_uc_atch_2'
hpr_lwract_uc_atch_2.location = Base.Vector (12.306350165, 1.3555888052, 1.3038056982)
hpl_upract_sf_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_upract_sf_atch_1')
hpl_upract_sf_atch_1.point_name = '.turn.ground.hpl_upract_sf_atch_1'
hpl_upract_sf_atch_1.location = Base.Vector (12.30147781, -1.2843931894, 1.952816897)
hpr_upract_sf_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_upract_sf_atch_1')
hpr_upract_sf_atch_1.point_name = '.turn.ground.hpr_upract_sf_atch_1'
hpr_upract_sf_atch_1.location = Base.Vector (12.30147781, 1.2843931894, 1.952816897)
hpl_upract_sf_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpl_upract_sf_atch_2')
hpl_upract_sf_atch_2.point_name = '.turn.ground.hpl_upract_sf_atch_2'
hpl_upract_sf_atch_2.location = Base.Vector (12.303675418, -1.2504491628, 1.9481928778)
hpr_upract_sf_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpr_upract_sf_atch_2')
hpr_upract_sf_atch_2.point_name = '.turn.ground.hpr_upract_sf_atch_2'
hpr_upract_sf_atch_2.location = Base.Vector (12.303675418, 1.2504491628, 1.9481928778)
hpl_spndl_sf_atch = MakeSceneNodeByType('Point', '.turn.ground.hpl_spndl_sf_atch')
hpl_spndl_sf_atch.point_name = '.turn.ground.hpl_spndl_sf_atch'
hpl_spndl_sf_atch.location = Base.Vector (10.777681391, -0.9566499282, 2.0951467876)
hpr_spndl_sf_atch = MakeSceneNodeByType('Point', '.turn.ground.hpr_spndl_sf_atch')
hpr_spndl_sf_atch.point_name = '.turn.ground.hpr_spndl_sf_atch'
hpr_spndl_sf_atch.location = Base.Vector (10.777681391, 0.9566499282, 2.0951467876)
hpl_connect_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_connect_1')
hpl_connect_1.point_name = '.turn.ground.hpl_connect_1'
hpl_connect_1.location = Base.Vector (12.045992164, -1.6111431582, 0.5342547862)
hpr_connect_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_connect_1')
hpr_connect_1.point_name = '.turn.ground.hpr_connect_1'
hpr_connect_1.location = Base.Vector (12.045992164, 1.6111431582, 0.5342547862)
hpl_ldb_udb_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpl_ldb_udb_atch_2')
hpl_ldb_udb_atch_2.point_name = '.turn.ground.hpl_ldb_udb_atch_2'
hpl_ldb_udb_atch_2.location = Base.Vector (11.5117089298, -1.2969830804, 1.51939371)
hpr_ldb_udb_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpr_ldb_udb_atch_2')
hpr_ldb_udb_atch_2.point_name = '.turn.ground.hpr_ldb_udb_atch_2'
hpr_ldb_udb_atch_2.location = Base.Vector (11.5117089298, 1.2969830804, 1.51939371)
hpl_ldb_collar_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpl_ldb_collar_atch_1')
hpl_ldb_collar_atch_1.point_name = '.turn.ground.hpl_ldb_collar_atch_1'
hpl_ldb_collar_atch_1.location = Base.Vector (12.111152689, -1.4634257498, 0.9176941514)
hpr_ldb_collar_atch_1 = MakeSceneNodeByType('Point', '.turn.ground.hpr_ldb_collar_atch_1')
hpr_ldb_collar_atch_1.point_name = '.turn.ground.hpr_ldb_collar_atch_1'
hpr_ldb_collar_atch_1.location = Base.Vector (12.111152689, 1.4634257498, 0.9176941514)
hpl_ldb_collar_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpl_ldb_collar_atch_2')
hpl_ldb_collar_atch_2.point_name = '.turn.ground.hpl_ldb_collar_atch_2'
hpl_ldb_collar_atch_2.location = Base.Vector (12.0829855622, -1.5425928508, 0.9195237896)
hpr_ldb_collar_atch_2 = MakeSceneNodeByType('Point', '.turn.ground.hpr_ldb_collar_atch_2')
hpr_ldb_collar_atch_2.point_name = '.turn.ground.hpr_ldb_collar_atch_2'
hpr_ldb_collar_atch_2.location = Base.Vector (12.0829855622, 1.5425928508, 0.9195237896)
hpl_uplock_tab = MakeSceneNodeByType('Point', '.turn.ground.hpl_uplock_tab')
hpl_uplock_tab.point_name = '.turn.ground.hpl_uplock_tab'
hpl_uplock_tab.location = Base.Vector (11.9014828772, -1.2751123164, 1.0332048729)
hpr_uplock_tab = MakeSceneNodeByType('Point', '.turn.ground.hpr_uplock_tab')
hpr_uplock_tab.point_name = '.turn.ground.hpr_uplock_tab'
hpr_uplock_tab.location = Base.Vector (11.9014828772, 1.2751123164, 1.0332048729)
hps_origin_reference = MakeSceneNodeByType('Point', '.turn.ground.hps_origin_reference')
hps_origin_reference.point_name = '.turn.ground.hps_origin_reference'
hps_origin_reference.location = Base.Vector (0.0, 0.0, 0.0)
gel_upper_cylinder = MakeSceneNodeByType('PartGeneral', '.turn.gel_upper_cylinder')
gel_upper_cylinder.part_name = '.turn.gel_upper_cylinder'
gel_upper_cylinder.adams_id = 4
gel_upper_cylinder.location = Base.Vector (12.1860123345, -1.4729962566, 1.4343428627)
gel_upper_cylinder.orientation = Base.Vector (55.1145661544, 175.2828647294, 235.2057167569)
uel_gearaero_i_1 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.uel_gearaero_i_1')
uel_gearaero_i_1.marker_name = '.turn.gel_upper_cylinder.uel_gearaero_i_1'
uel_gearaero_i_1.adams_id = 69
uel_gearaero_i_1.location = Base.Vector (-3.3904410529e-11, 1.7865427887e-11, 0.2927550811)
uel_gearaero_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.cm')
cm.marker_name = '.turn.gel_upper_cylinder.cm'
cm.adams_id = 71
cm.location = Base.Vector (-0.00020756301703, 0.0064023904007, -0.014668262126)
cm.orientation = Base.Vector (1.8568667884, 1.160957641, 3.871847135e-06)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.inertia_frame')
inertia_frame.marker_name = '.turn.gel_upper_cylinder.inertia_frame'
inertia_frame.adams_id = 72
inertia_frame.location = Base.Vector (-0.00020756301703, 0.0064023904007, -0.014668262126)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_12 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.gralin_12')
gralin_12.marker_name = '.turn.gel_upper_cylinder.gralin_12'
gralin_12.adams_id = 73
gralin_12.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
gralin_12.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_16 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.gralin_16')
gralin_16.marker_name = '.turn.gel_upper_cylinder.gralin_16'
gralin_16.adams_id = 74
gralin_16.location = Base.Vector (-0.012679580771, 0.391098059, -0.6781339507)
gralin_16.orientation = Base.Vector (1.8570008795, 40.3514751572, 357.5638844649)
gralin_20 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.gralin_20')
gralin_20.marker_name = '.turn.gel_upper_cylinder.gralin_20'
gralin_20.adams_id = 75
gralin_20.location = Base.Vector (-0.012679580771, 0.391098059, -0.6781339507)
gralin_20.orientation = Base.Vector (1.8569053817, 96.3249984441, 196.3982135132)
jxl_joint_j_12 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.jxl_joint_j_12')
jxl_joint_j_12.marker_name = '.turn.gel_upper_cylinder.jxl_joint_j_12'
jxl_joint_j_12.adams_id = 76
jxl_joint_j_12.location = Base.Vector (0.0, 0.0, 0.5071310811)
jxl_joint_j_12.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_spring_j_1 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.uel_spring_j_1')
uel_spring_j_1.marker_name = '.turn.gel_upper_cylinder.uel_spring_j_1'
uel_spring_j_1.adams_id = 78
uel_spring_j_1.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
uel_spring_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_damper_j_1 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.uel_damper_j_1')
uel_damper_j_1.marker_name = '.turn.gel_upper_cylinder.uel_damper_j_1'
uel_damper_j_1.adams_id = 79
uel_damper_j_1.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
uel_damper_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_stopper_j_1 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.uel_stopper_j_1')
uel_stopper_j_1.marker_name = '.turn.gel_upper_cylinder.uel_stopper_j_1'
uel_stopper_j_1.adams_id = 80
uel_stopper_j_1.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
uel_stopper_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_4 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.jxl_joint_j_4')
jxl_joint_j_4.marker_name = '.turn.gel_upper_cylinder.jxl_joint_j_4'
jxl_joint_j_4.adams_id = 81
jxl_joint_j_4.location = Base.Vector (0.0, 0.0, 0.5562289935)
jxl_joint_j_4.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_i_7 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.jxl_joint_i_7')
jxl_joint_i_7.marker_name = '.turn.gel_upper_cylinder.jxl_joint_i_7'
jxl_joint_i_7.adams_id = 82
jxl_joint_i_7.location = Base.Vector (-0.1103647044, 0.1064191121, 0.1310872657)
jxl_joint_i_7.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
uel_actuator_j_3 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.uel_actuator_j_3')
uel_actuator_j_3.marker_name = '.turn.gel_upper_cylinder.uel_actuator_j_3'
uel_actuator_j_3.adams_id = 83
uel_actuator_j_3.location = Base.Vector (-0.0063397903922, 0.1955490294, -0.6998205159)
uel_actuator_j_3.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_267 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.MARKER_267')
MARKER_267.marker_name = '.turn.gel_upper_cylinder.MARKER_267'
MARKER_267.adams_id = 267
MARKER_267.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
MARKER_267.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
MARKER_272 = MakeSceneNodeByType('Marker', '.turn.gel_upper_cylinder.MARKER_272')
MARKER_272.marker_name = '.turn.gel_upper_cylinder.MARKER_272'
MARKER_272.adams_id = 272
MARKER_272.location = Base.Vector (0.0, 0.0, -0.7215070811)
MARKER_272.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
gel_upper_cylinder = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.cm')
gel_upper_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.inertia_frame')
gel_upper_cylinder.inertia_marker = inertia_marker
gel_upper_cylinder.part_name = '.turn.gel_upper_cylinder'
gel_upper_cylinder.mass = 112.770857716
gel_upper_cylinder.ixx = 20.3828607526
gel_upper_cylinder.iyy = 20.1915756173
gel_upper_cylinder.izz = 0.6770308822
gel_upper_cylinder.ixy = 0.0
gel_upper_cylinder.izx = 0.0
gel_upper_cylinder.iyz = 0.0
gralin_upper_cylinder = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_upper_cylinder.gralin_upper_cylinder')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.gralin_12')
gralin_upper_cylinder.center_marker = center_marker
gralin_upper_cylinder.cylinder_name = '.turn.gel_upper_cylinder.gralin_upper_cylinder'
gralin_upper_cylinder.adams_id = 1
gralin_upper_cylinder.angle_extent = 360.0
gralin_upper_cylinder.length = 1.4430141621
gralin_upper_cylinder.radius = 0.09398
gralin_upper_cylinder.side_count_for_body = 15
gralin_upper_cylinder.segment_count_for_ends = 15


gralin_geom = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_upper_cylinder.gralin_geom')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.gralin_16')
gralin_geom.center_marker = center_marker
gralin_geom.cylinder_name = '.turn.gel_upper_cylinder.gralin_geom'
gralin_geom.adams_id = 2
gralin_geom.angle_extent = 360.0
gralin_geom.length = 0.4529277435
gralin_geom.radius = 0.0254
gralin_geom.side_count_for_body = 15
gralin_geom.segment_count_for_ends = 15


gralin_geom3 = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_upper_cylinder.gralin_geom3')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.gralin_20')
gralin_geom3.center_marker = center_marker
gralin_geom3.cylinder_name = '.turn.gel_upper_cylinder.gralin_geom3'
gralin_geom3.adams_id = 3
gralin_geom3.angle_extent = 360.0
gralin_geom3.length = 0.3937000024
gralin_geom3.radius = 0.0127
gralin_geom3.side_count_for_body = 15
gralin_geom3.segment_count_for_ends = 15


ger_upper_cylinder = MakeSceneNodeByType('PartGeneral', '.turn.ger_upper_cylinder')
ger_upper_cylinder.part_name = '.turn.ger_upper_cylinder'
ger_upper_cylinder.adams_id = 5
ger_upper_cylinder.location = Base.Vector (12.1860123345, 1.4729962566, 1.4343428627)
ger_upper_cylinder.orientation = Base.Vector (124.8854338456, 175.2828647294, 304.7942832431)
uer_gearaero_i_1 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.uer_gearaero_i_1')
uer_gearaero_i_1.marker_name = '.turn.ger_upper_cylinder.uer_gearaero_i_1'
uer_gearaero_i_1.adams_id = 84
uer_gearaero_i_1.location = Base.Vector (-3.3904427876e-11, -1.7865197169e-11, 0.2927550811)
uer_gearaero_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.cm')
cm.marker_name = '.turn.ger_upper_cylinder.cm'
cm.adams_id = 85
cm.location = Base.Vector (-0.00020756301703, -0.0064023904007, -0.014668262126)
cm.orientation = Base.Vector (178.1431332116, 1.160957641, 179.9999961282)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.inertia_frame')
inertia_frame.marker_name = '.turn.ger_upper_cylinder.inertia_frame'
inertia_frame.adams_id = 86
inertia_frame.location = Base.Vector (-0.00020756301703, -0.0064023904007, -0.014668262126)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_13 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.gralin_13')
gralin_13.marker_name = '.turn.ger_upper_cylinder.gralin_13'
gralin_13.adams_id = 87
gralin_13.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
gralin_13.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_17 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.gralin_17')
gralin_17.marker_name = '.turn.ger_upper_cylinder.gralin_17'
gralin_17.adams_id = 88
gralin_17.location = Base.Vector (-0.012679580771, -0.391098059, -0.6781339507)
gralin_17.orientation = Base.Vector (178.1429991205, 40.3514751572, 182.4361155351)
gralin_21 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.gralin_21')
gralin_21.marker_name = '.turn.ger_upper_cylinder.gralin_21'
gralin_21.adams_id = 89
gralin_21.location = Base.Vector (-0.012679580771, -0.391098059, -0.6781339507)
gralin_21.orientation = Base.Vector (178.1430946183, 96.3249984441, 343.6017864868)
jxr_joint_j_12 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.jxr_joint_j_12')
jxr_joint_j_12.marker_name = '.turn.ger_upper_cylinder.jxr_joint_j_12'
jxr_joint_j_12.adams_id = 90
jxr_joint_j_12.location = Base.Vector (0.0, 0.0, 0.5071310811)
jxr_joint_j_12.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_spring_j_1 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.uer_spring_j_1')
uer_spring_j_1.marker_name = '.turn.ger_upper_cylinder.uer_spring_j_1'
uer_spring_j_1.adams_id = 92
uer_spring_j_1.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
uer_spring_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_damper_j_1 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.uer_damper_j_1')
uer_damper_j_1.marker_name = '.turn.ger_upper_cylinder.uer_damper_j_1'
uer_damper_j_1.adams_id = 93
uer_damper_j_1.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
uer_damper_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_stopper_j_1 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.uer_stopper_j_1')
uer_stopper_j_1.marker_name = '.turn.ger_upper_cylinder.uer_stopper_j_1'
uer_stopper_j_1.adams_id = 94
uer_stopper_j_1.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
uer_stopper_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_j_4 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.jxr_joint_j_4')
jxr_joint_j_4.marker_name = '.turn.ger_upper_cylinder.jxr_joint_j_4'
jxr_joint_j_4.adams_id = 95
jxr_joint_j_4.location = Base.Vector (0.0, 0.0, 0.5562289935)
jxr_joint_j_4.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_i_7 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.jxr_joint_i_7')
jxr_joint_i_7.marker_name = '.turn.ger_upper_cylinder.jxr_joint_i_7'
jxr_joint_i_7.adams_id = 96
jxr_joint_i_7.location = Base.Vector (-0.1103647044, -0.1064191121, 0.1310872657)
jxr_joint_i_7.orientation = Base.Vector (235.2057167569, 175.2828647294, 55.1145661544)
uer_actuator_j_3 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.uer_actuator_j_3')
uer_actuator_j_3.marker_name = '.turn.ger_upper_cylinder.uer_actuator_j_3'
uer_actuator_j_3.adams_id = 97
uer_actuator_j_3.location = Base.Vector (-0.0063397903922, -0.1955490294, -0.6998205159)
uer_actuator_j_3.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_269 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.MARKER_269')
MARKER_269.marker_name = '.turn.ger_upper_cylinder.MARKER_269'
MARKER_269.adams_id = 269
MARKER_269.location = Base.Vector (-1.3212757277e-11, 0.0, -0.7215070811)
MARKER_269.orientation = Base.Vector (235.2057167569, 175.2828647294, 55.1145661544)
MARKER_278 = MakeSceneNodeByType('Marker', '.turn.ger_upper_cylinder.MARKER_278')
MARKER_278.marker_name = '.turn.ger_upper_cylinder.MARKER_278'
MARKER_278.adams_id = 278
MARKER_278.location = Base.Vector (0.0, 0.0, -0.7215070811)
MARKER_278.orientation = Base.Vector (235.2057167569, 175.2828647294, 55.1145661544)
ger_upper_cylinder = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.cm')
ger_upper_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.inertia_frame')
ger_upper_cylinder.inertia_marker = inertia_marker
ger_upper_cylinder.part_name = '.turn.ger_upper_cylinder'
ger_upper_cylinder.mass = 112.770857716
ger_upper_cylinder.ixx = 20.3828607526
ger_upper_cylinder.iyy = 20.1915756173
ger_upper_cylinder.izz = 0.6770308822
ger_upper_cylinder.ixy = 0.0
ger_upper_cylinder.izx = 0.0
ger_upper_cylinder.iyz = 0.0
gralin_upper_cylinder = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_upper_cylinder.gralin_upper_cylinder')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.gralin_13')
gralin_upper_cylinder.center_marker = center_marker
gralin_upper_cylinder.cylinder_name = '.turn.ger_upper_cylinder.gralin_upper_cylinder'
gralin_upper_cylinder.adams_id = 4
gralin_upper_cylinder.angle_extent = 360.0
gralin_upper_cylinder.length = 1.4430141621
gralin_upper_cylinder.radius = 0.09398
gralin_upper_cylinder.side_count_for_body = 15
gralin_upper_cylinder.segment_count_for_ends = 15


gralin_geom = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_upper_cylinder.gralin_geom')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.gralin_17')
gralin_geom.center_marker = center_marker
gralin_geom.cylinder_name = '.turn.ger_upper_cylinder.gralin_geom'
gralin_geom.adams_id = 5
gralin_geom.angle_extent = 360.0
gralin_geom.length = 0.4529277435
gralin_geom.radius = 0.0254
gralin_geom.side_count_for_body = 15
gralin_geom.segment_count_for_ends = 15


gralin_geom3 = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_upper_cylinder.gralin_geom3')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.gralin_21')
gralin_geom3.center_marker = center_marker
gralin_geom3.cylinder_name = '.turn.ger_upper_cylinder.gralin_geom3'
gralin_geom3.adams_id = 6
gralin_geom3.angle_extent = 360.0
gralin_geom3.length = 0.3937000024
gralin_geom3.radius = 0.0127
gralin_geom3.side_count_for_body = 15
gralin_geom3.segment_count_for_ends = 15


gel_lower_cylinder = MakeSceneNodeByType('PartGeneral', '.turn.gel_lower_cylinder')
gel_lower_cylinder.part_name = '.turn.gel_lower_cylinder'
gel_lower_cylinder.adams_id = 6
gel_lower_cylinder.location = Base.Vector (12.2383679771, -1.5095002745, 0.6608546166)
gel_lower_cylinder.orientation = Base.Vector (55.1145661544, 175.2828647294, 235.2057167569)
cm = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.cm')
cm.marker_name = '.turn.gel_lower_cylinder.cm'
cm.adams_id = 99
cm.location = Base.Vector (1.6535536877e-05, -0.013980732745, 0.032717040657)
cm.orientation = Base.Vector (0.067765835809, 4.4745452767, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.inertia_frame')
inertia_frame.marker_name = '.turn.gel_lower_cylinder.inertia_frame'
inertia_frame.adams_id = 100
inertia_frame.location = Base.Vector (1.6535536879e-05, -0.013980732745, 0.032717040657)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_14 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.gralin_14')
gralin_14.marker_name = '.turn.gel_lower_cylinder.gralin_14'
gralin_14.adams_id = 101
gralin_14.location = Base.Vector (0.0, 4.5291156242e-11, -0.483362)
gralin_14.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_22 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.gralin_22')
gralin_22.marker_name = '.turn.gel_lower_cylinder.gralin_22'
gralin_22.adams_id = 102
gralin_22.location = Base.Vector (-2.2761403873e-11, -5.0394524422e-09, 0.4833620002)
gralin_22.orientation = Base.Vector (0.067765842413, 86.3072194254, 358.9479604232)
jxl_joint_j_11 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.jxl_joint_j_11')
jxl_joint_j_11.marker_name = '.turn.gel_lower_cylinder.jxl_joint_j_11'
jxl_joint_j_11.adams_id = 103
jxl_joint_j_11.location = Base.Vector (0.1141502171, -0.02624637539, 0.3816035459)
jxl_joint_j_11.orientation = Base.Vector (182.811221391, 89.9999933852, 90.0001347091)
jxl_joint_i_12 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.jxl_joint_i_12')
jxl_joint_i_12.marker_name = '.turn.gel_lower_cylinder.jxl_joint_i_12'
jxl_joint_i_12.adams_id = 104
jxl_joint_i_12.location = Base.Vector (3.0868047701e-11, 2.7426356325e-11, -0.2689859999)
jxl_joint_i_12.orientation = Base.Vector (0.0, 0.0, 0.0)
coomarker_1 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.coomarker_1')
coomarker_1.marker_name = '.turn.gel_lower_cylinder.coomarker_1'
coomarker_1.adams_id = 105
coomarker_1.location = Base.Vector (0.00032976997546, -0.2788194421, 0.5013550985)
coomarker_1.orientation = Base.Vector (180.0677659365, 93.6935934177, 183.881448147)
uel_spring_i_1 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.uel_spring_i_1')
uel_spring_i_1.marker_name = '.turn.gel_lower_cylinder.uel_spring_i_1'
uel_spring_i_1.adams_id = 106
uel_spring_i_1.location = Base.Vector (0.0, 4.5291156242e-11, -0.483362)
uel_spring_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_damper_i_1 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.uel_damper_i_1')
uel_damper_i_1.marker_name = '.turn.gel_lower_cylinder.uel_damper_i_1'
uel_damper_i_1.adams_id = 107
uel_damper_i_1.location = Base.Vector (0.0, 4.5291156242e-11, -0.483362)
uel_damper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_stopper_i_1 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.uel_stopper_i_1')
uel_stopper_i_1.marker_name = '.turn.gel_lower_cylinder.uel_stopper_i_1'
uel_stopper_i_1.adams_id = 108
uel_stopper_i_1.location = Base.Vector (0.0, 4.5291156242e-11, -0.483362)
uel_stopper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_266 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.MARKER_266')
MARKER_266.marker_name = '.turn.gel_lower_cylinder.MARKER_266'
MARKER_266.adams_id = 266
MARKER_266.location = Base.Vector (0.0, 0.0, -0.483362)
MARKER_266.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
MARKER_273 = MakeSceneNodeByType('Marker', '.turn.gel_lower_cylinder.MARKER_273')
MARKER_273.marker_name = '.turn.gel_lower_cylinder.MARKER_273'
MARKER_273.adams_id = 273
MARKER_273.location = Base.Vector (0.0, 0.0, -0.483362)
MARKER_273.orientation = Base.Vector (304.7942832431, 175.2828647294, 124.8854338456)
gel_lower_cylinder = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.cm')
gel_lower_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.inertia_frame')
gel_lower_cylinder.inertia_marker = inertia_marker
gel_lower_cylinder.part_name = '.turn.gel_lower_cylinder'
gel_lower_cylinder.mass = 217.3555691677
gel_lower_cylinder.ixx = 3.3284494628
gel_lower_cylinder.iyy = 3.1936294
gel_lower_cylinder.izz = 0.2032330741
gel_lower_cylinder.ixy = 0.0
gel_lower_cylinder.izx = 0.0
gel_lower_cylinder.iyz = 0.0
gralin_lower_cylinder = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_lower_cylinder.gralin_lower_cylinder')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.gralin_14')
gralin_lower_cylinder.center_marker = center_marker
gralin_lower_cylinder.cylinder_name = '.turn.gel_lower_cylinder.gralin_lower_cylinder'
gralin_lower_cylinder.adams_id = 7
gralin_lower_cylinder.angle_extent = 360.0
gralin_lower_cylinder.length = 0.966724
gralin_lower_cylinder.radius = 0.0635
gralin_lower_cylinder.side_count_for_body = 15
gralin_lower_cylinder.segment_count_for_ends = 15


gralin_geom = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_lower_cylinder.gralin_geom')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.gralin_22')
gralin_geom.center_marker = center_marker
gralin_geom.cylinder_name = '.turn.gel_lower_cylinder.gralin_geom'
gralin_geom.adams_id = 8
gralin_geom.angle_extent = 360.0
gralin_geom.length = 0.4257036049
gralin_geom.radius = 0.0254
gralin_geom.side_count_for_body = 15
gralin_geom.segment_count_for_ends = 15


ger_lower_cylinder = MakeSceneNodeByType('PartGeneral', '.turn.ger_lower_cylinder')
ger_lower_cylinder.part_name = '.turn.ger_lower_cylinder'
ger_lower_cylinder.adams_id = 7
ger_lower_cylinder.location = Base.Vector (12.2383679771, 1.5095002745, 0.6608546166)
ger_lower_cylinder.orientation = Base.Vector (124.8854338456, 175.2828647294, 304.7942832431)
cm = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.cm')
cm.marker_name = '.turn.ger_lower_cylinder.cm'
cm.adams_id = 109
cm.location = Base.Vector (1.6535536877e-05, 0.013980732745, 0.032717040657)
cm.orientation = Base.Vector (179.9322341642, 4.4745452767, 180.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.inertia_frame')
inertia_frame.marker_name = '.turn.ger_lower_cylinder.inertia_frame'
inertia_frame.adams_id = 110
inertia_frame.location = Base.Vector (1.6535536881e-05, 0.013980732745, 0.032717040657)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_15 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.gralin_15')
gralin_15.marker_name = '.turn.ger_lower_cylinder.gralin_15'
gralin_15.adams_id = 111
gralin_15.location = Base.Vector (0.0, -4.5290927259e-11, -0.483362)
gralin_15.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_23 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.gralin_23')
gralin_23.marker_name = '.turn.ger_lower_cylinder.gralin_23'
gralin_23.adams_id = 112
gralin_23.location = Base.Vector (-2.2761403873e-11, 5.0394524422e-09, 0.4833620002)
gralin_23.orientation = Base.Vector (179.9322341576, 86.3072194254, 181.0520395768)
jxr_joint_j_11 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.jxr_joint_j_11')
jxr_joint_j_11.marker_name = '.turn.ger_lower_cylinder.jxr_joint_j_11'
jxr_joint_j_11.adams_id = 113
jxr_joint_j_11.location = Base.Vector (0.1141502171, 0.02624637539, 0.3816035459)
jxr_joint_j_11.orientation = Base.Vector (357.188778609, 89.9999933852, 89.9998652909)
jxr_joint_i_12 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.jxr_joint_i_12')
jxr_joint_i_12.marker_name = '.turn.ger_lower_cylinder.jxr_joint_i_12'
jxr_joint_i_12.adams_id = 114
jxr_joint_i_12.location = Base.Vector (3.0868051171e-11, -2.742591397e-11, -0.2689859999)
jxr_joint_i_12.orientation = Base.Vector (0.0, 0.0, 0.0)
coomarker_2 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.coomarker_2')
coomarker_2.marker_name = '.turn.ger_lower_cylinder.coomarker_2'
coomarker_2.adams_id = 115
coomarker_2.location = Base.Vector (0.00032976997546, 0.2788194421, 0.5013550985)
coomarker_2.orientation = Base.Vector (359.9322340635, 93.6935934177, 356.118551853)
uer_spring_i_1 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.uer_spring_i_1')
uer_spring_i_1.marker_name = '.turn.ger_lower_cylinder.uer_spring_i_1'
uer_spring_i_1.adams_id = 116
uer_spring_i_1.location = Base.Vector (0.0, -4.5290927259e-11, -0.483362)
uer_spring_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_damper_i_1 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.uer_damper_i_1')
uer_damper_i_1.marker_name = '.turn.ger_lower_cylinder.uer_damper_i_1'
uer_damper_i_1.adams_id = 117
uer_damper_i_1.location = Base.Vector (0.0, -4.5290927259e-11, -0.483362)
uer_damper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_stopper_i_1 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.uer_stopper_i_1')
uer_stopper_i_1.marker_name = '.turn.ger_lower_cylinder.uer_stopper_i_1'
uer_stopper_i_1.adams_id = 118
uer_stopper_i_1.location = Base.Vector (0.0, -4.5290927259e-11, -0.483362)
uer_stopper_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
MARKER_268 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.MARKER_268')
MARKER_268.marker_name = '.turn.ger_lower_cylinder.MARKER_268'
MARKER_268.adams_id = 268
MARKER_268.location = Base.Vector (0.0, 0.0, -0.483362)
MARKER_268.orientation = Base.Vector (235.2057167569, 175.2828647294, 55.1145661544)
MARKER_279 = MakeSceneNodeByType('Marker', '.turn.ger_lower_cylinder.MARKER_279')
MARKER_279.marker_name = '.turn.ger_lower_cylinder.MARKER_279'
MARKER_279.adams_id = 279
MARKER_279.location = Base.Vector (0.0, 0.0, -0.483362)
MARKER_279.orientation = Base.Vector (235.2057167569, 175.2828647294, 55.1145661544)
ger_lower_cylinder = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.cm')
ger_lower_cylinder.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.inertia_frame')
ger_lower_cylinder.inertia_marker = inertia_marker
ger_lower_cylinder.part_name = '.turn.ger_lower_cylinder'
ger_lower_cylinder.mass = 217.3555691677
ger_lower_cylinder.ixx = 3.3284494628
ger_lower_cylinder.iyy = 3.1936294
ger_lower_cylinder.izz = 0.2032330741
ger_lower_cylinder.ixy = 0.0
ger_lower_cylinder.izx = 0.0
ger_lower_cylinder.iyz = 0.0
gralin_lower_cylinder = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_lower_cylinder.gralin_lower_cylinder')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.gralin_15')
gralin_lower_cylinder.center_marker = center_marker
gralin_lower_cylinder.cylinder_name = '.turn.ger_lower_cylinder.gralin_lower_cylinder'
gralin_lower_cylinder.adams_id = 9
gralin_lower_cylinder.angle_extent = 360.0
gralin_lower_cylinder.length = 0.966724
gralin_lower_cylinder.radius = 0.0635
gralin_lower_cylinder.side_count_for_body = 15
gralin_lower_cylinder.segment_count_for_ends = 15


gralin_geom = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_lower_cylinder.gralin_geom')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.gralin_23')
gralin_geom.center_marker = center_marker
gralin_geom.cylinder_name = '.turn.ger_lower_cylinder.gralin_geom'
gralin_geom.adams_id = 10
gralin_geom.angle_extent = 360.0
gralin_geom.length = 0.4257036049
gralin_geom.radius = 0.0254
gralin_geom.side_count_for_body = 15
gralin_geom.segment_count_for_ends = 15


gel_upper_dragbrace = MakeSceneNodeByType('PartGeneral', '.turn.gel_upper_dragbrace')
gel_upper_dragbrace.part_name = '.turn.gel_upper_dragbrace'
gel_upper_dragbrace.adams_id = 8
gel_upper_dragbrace.location = Base.Vector (11.247700263, -1.1306922298, 1.8105711871)
gel_upper_dragbrace.orientation = Base.Vector (69.1745865818, 133.845797857, 255.2385761183)
cm = MakeSceneNodeByType('Marker', '.turn.gel_upper_dragbrace.cm')
cm.marker_name = '.turn.gel_upper_dragbrace.cm'
cm.adams_id = 119
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_upper_dragbrace.inertia_frame')
inertia_frame.marker_name = '.turn.gel_upper_dragbrace.inertia_frame'
inertia_frame.adams_id = 120
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_24 = MakeSceneNodeByType('Marker', '.turn.gel_upper_dragbrace.gralin_24')
gralin_24.marker_name = '.turn.gel_upper_dragbrace.gralin_24'
gralin_24.adams_id = 121
gralin_24.location = Base.Vector (0.0, -2.7292432203e-11, -0.4222750594)
gralin_24.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_14 = MakeSceneNodeByType('Marker', '.turn.gel_upper_dragbrace.jxl_joint_j_14')
jxl_joint_j_14.marker_name = '.turn.gel_upper_dragbrace.jxl_joint_j_14'
jxl_joint_j_14.adams_id = 122
jxl_joint_j_14.location = Base.Vector (0.0, -6.9364805566e-11, 0.4222750594)
jxl_joint_j_14.orientation = Base.Vector (193.0027634258, 90.0301580129, 133.8272261428)
jxl_joint_i_5 = MakeSceneNodeByType('Marker', '.turn.gel_upper_dragbrace.jxl_joint_i_5')
jxl_joint_i_5.marker_name = '.turn.gel_upper_dragbrace.jxl_joint_i_5'
jxl_joint_i_5.adams_id = 123
jxl_joint_i_5.location = Base.Vector (0.0, -2.7292917926e-11, -0.4222750594)
jxl_joint_i_5.orientation = Base.Vector (12.9738148964, 0.0, 0.0)
uel_actuator_i_3 = MakeSceneNodeByType('Marker', '.turn.gel_upper_dragbrace.uel_actuator_i_3')
uel_actuator_i_3.marker_name = '.turn.gel_upper_dragbrace.uel_actuator_i_3'
uel_actuator_i_3.adams_id = 124
uel_actuator_i_3.location = Base.Vector (0.0, -6.9364805566e-11, 0.4222750594)
uel_actuator_i_3.orientation = Base.Vector (0.0, 0.0, 0.0)
gel_upper_dragbrace = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.cm')
gel_upper_dragbrace.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.inertia_frame')
gel_upper_dragbrace.inertia_marker = inertia_marker
gel_upper_dragbrace.part_name = '.turn.gel_upper_dragbrace'
gel_upper_dragbrace.mass = 6.7539180723
gel_upper_dragbrace.ixx = 0.4030130421
gel_upper_dragbrace.iyy = 0.4030130421
gel_upper_dragbrace.izz = 0.0031372976041
gel_upper_dragbrace.ixy = 0.0
gel_upper_dragbrace.izx = 0.0
gel_upper_dragbrace.iyz = 0.0
gralin_upper_dragbrace = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_upper_dragbrace.gralin_upper_dragbrace')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.gralin_24')
gralin_upper_dragbrace.center_marker = center_marker
gralin_upper_dragbrace.cylinder_name = '.turn.gel_upper_dragbrace.gralin_upper_dragbrace'
gralin_upper_dragbrace.adams_id = 11
gralin_upper_dragbrace.angle_extent = 360.0
gralin_upper_dragbrace.length = 0.8445501187
gralin_upper_dragbrace.radius = 0.03048
gralin_upper_dragbrace.side_count_for_body = 15
gralin_upper_dragbrace.segment_count_for_ends = 15


ger_upper_dragbrace = MakeSceneNodeByType('PartGeneral', '.turn.ger_upper_dragbrace')
ger_upper_dragbrace.part_name = '.turn.ger_upper_dragbrace'
ger_upper_dragbrace.adams_id = 9
ger_upper_dragbrace.location = Base.Vector (11.247700263, 1.1306922298, 1.8105711871)
ger_upper_dragbrace.orientation = Base.Vector (110.8254134182, 133.845797857, 284.7614238817)
cm = MakeSceneNodeByType('Marker', '.turn.ger_upper_dragbrace.cm')
cm.marker_name = '.turn.ger_upper_dragbrace.cm'
cm.adams_id = 125
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_upper_dragbrace.inertia_frame')
inertia_frame.marker_name = '.turn.ger_upper_dragbrace.inertia_frame'
inertia_frame.adams_id = 126
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_25 = MakeSceneNodeByType('Marker', '.turn.ger_upper_dragbrace.gralin_25')
gralin_25.marker_name = '.turn.ger_upper_dragbrace.gralin_25'
gralin_25.adams_id = 127
gralin_25.location = Base.Vector (0.0, 2.7292418325e-11, -0.4222750594)
gralin_25.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_j_14 = MakeSceneNodeByType('Marker', '.turn.ger_upper_dragbrace.jxr_joint_j_14')
jxr_joint_j_14.marker_name = '.turn.ger_upper_dragbrace.jxr_joint_j_14'
jxr_joint_j_14.adams_id = 128
jxr_joint_j_14.location = Base.Vector (0.0, 6.9364819444e-11, 0.4222750594)
jxr_joint_j_14.orientation = Base.Vector (346.9972365742, 90.0301580129, 46.1727738572)
jxr_joint_i_5 = MakeSceneNodeByType('Marker', '.turn.ger_upper_dragbrace.jxr_joint_i_5')
jxr_joint_i_5.marker_name = '.turn.ger_upper_dragbrace.jxr_joint_i_5'
jxr_joint_i_5.adams_id = 129
jxr_joint_i_5.location = Base.Vector (0.0, 2.7293250993e-11, -0.4222750594)
jxr_joint_i_5.orientation = Base.Vector (347.0261851036, 0.0, 0.0)
uer_actuator_i_3 = MakeSceneNodeByType('Marker', '.turn.ger_upper_dragbrace.uer_actuator_i_3')
uer_actuator_i_3.marker_name = '.turn.ger_upper_dragbrace.uer_actuator_i_3'
uer_actuator_i_3.adams_id = 130
uer_actuator_i_3.location = Base.Vector (0.0, 6.9364819444e-11, 0.4222750594)
uer_actuator_i_3.orientation = Base.Vector (0.0, 0.0, 0.0)
ger_upper_dragbrace = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.cm')
ger_upper_dragbrace.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.inertia_frame')
ger_upper_dragbrace.inertia_marker = inertia_marker
ger_upper_dragbrace.part_name = '.turn.ger_upper_dragbrace'
ger_upper_dragbrace.mass = 6.7539180723
ger_upper_dragbrace.ixx = 0.4030130421
ger_upper_dragbrace.iyy = 0.4030130421
ger_upper_dragbrace.izz = 0.0031372976041
ger_upper_dragbrace.ixy = 0.0
ger_upper_dragbrace.izx = 0.0
ger_upper_dragbrace.iyz = 0.0
gralin_upper_dragbrace = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_upper_dragbrace.gralin_upper_dragbrace')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.gralin_25')
gralin_upper_dragbrace.center_marker = center_marker
gralin_upper_dragbrace.cylinder_name = '.turn.ger_upper_dragbrace.gralin_upper_dragbrace'
gralin_upper_dragbrace.adams_id = 12
gralin_upper_dragbrace.angle_extent = 360.0
gralin_upper_dragbrace.length = 0.8445501187
gralin_upper_dragbrace.radius = 0.03048
gralin_upper_dragbrace.side_count_for_body = 15
gralin_upper_dragbrace.segment_count_for_ends = 15


gel_lower_dragbrace = MakeSceneNodeByType('PartGeneral', '.turn.gel_lower_dragbrace')
gel_lower_dragbrace.part_name = '.turn.gel_lower_dragbrace'
gel_lower_dragbrace.adams_id = 10
gel_lower_dragbrace.location = Base.Vector (11.821751947, -1.3511956141, 1.2178735066)
gel_lower_dragbrace.orientation = Base.Vector (68.8036164538, 134.040966185, 254.9123665662)
cm = MakeSceneNodeByType('Marker', '.turn.gel_lower_dragbrace.cm')
cm.marker_name = '.turn.gel_lower_dragbrace.cm'
cm.adams_id = 131
cm.location = Base.Vector (0.0039348735476, 0.0068056064573, 0.024978613416)
cm.orientation = Base.Vector (149.9643072355, 1.0992652329, 180.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_lower_dragbrace.inertia_frame')
inertia_frame.marker_name = '.turn.gel_lower_dragbrace.inertia_frame'
inertia_frame.adams_id = 132
inertia_frame.location = Base.Vector (0.0039348735476, 0.0068056064573, 0.024978613416)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_26 = MakeSceneNodeByType('Marker', '.turn.gel_lower_dragbrace.gralin_26')
gralin_26.marker_name = '.turn.gel_lower_dragbrace.gralin_26'
gralin_26.adams_id = 133
gralin_26.location = Base.Vector (0.0, -1.3320421155e-11, -0.4318055559)
gralin_26.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_i_14 = MakeSceneNodeByType('Marker', '.turn.gel_lower_dragbrace.jxl_joint_i_14')
jxl_joint_i_14.marker_name = '.turn.gel_lower_dragbrace.jxl_joint_i_14'
jxl_joint_i_14.adams_id = 134
jxl_joint_i_14.location = Base.Vector (0.0, -1.33211428e-11, -0.4318055559)
jxl_joint_i_14.orientation = Base.Vector (193.0709676552, 90.2906925253, 133.6233654172)
jxl_joint_i_10 = MakeSceneNodeByType('Marker', '.turn.gel_lower_dragbrace.jxl_joint_i_10')
jxl_joint_i_10.marker_name = '.turn.gel_lower_dragbrace.jxl_joint_i_10'
jxl_joint_i_10.adams_id = 135
jxl_joint_i_10.location = Base.Vector (0.0, 1.3321697911e-11, 0.4318055559)
jxl_joint_i_10.orientation = Base.Vector (193.0709676552, 90.2906925253, 133.6233654172)
graarm_1 = MakeSceneNodeByType('Marker', '.turn.gel_lower_dragbrace.graarm_1')
graarm_1.marker_name = '.turn.gel_lower_dragbrace.graarm_1'
graarm_1.adams_id = 136
graarm_1.location = Base.Vector (0.070772384935, 0.1224052042, 0.1620383572)
graarm_1.orientation = Base.Vector (239.9643072438, 90.0000000001, 337.5559025676)
graarm_2 = MakeSceneNodeByType('Marker', '.turn.gel_lower_dragbrace.graarm_2')
graarm_2.marker_name = '.turn.gel_lower_dragbrace.graarm_2'
graarm_2.adams_id = 137
graarm_2.location = Base.Vector (0.0, 0.0, 0.1036333334)
graarm_2.orientation = Base.Vector (0.0, 0.0, 0.0)
graarm_3 = MakeSceneNodeByType('Marker', '.turn.gel_lower_dragbrace.graarm_3')
graarm_3.marker_name = '.turn.gel_lower_dragbrace.graarm_3'
graarm_3.adams_id = 138
graarm_3.location = Base.Vector (0.0, 0.0, 0.2072666668)
graarm_3.orientation = Base.Vector (0.0, 0.0, 0.0)
gel_lower_dragbrace = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.cm')
gel_lower_dragbrace.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.inertia_frame')
gel_lower_dragbrace.inertia_marker = inertia_marker
gel_lower_dragbrace.part_name = '.turn.gel_lower_dragbrace'
gel_lower_dragbrace.mass = 5.6992574801
gel_lower_dragbrace.ixx = 0.3211055352
gel_lower_dragbrace.iyy = 0.3193778028
gel_lower_dragbrace.izz = 0.005107174896
gel_lower_dragbrace.ixy = 0.0
gel_lower_dragbrace.izx = 0.0
gel_lower_dragbrace.iyz = 0.0
gralin_lower_dragbrace = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_lower_dragbrace.gralin_lower_dragbrace')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.gralin_26')
gralin_lower_dragbrace.center_marker = center_marker
gralin_lower_dragbrace.cylinder_name = '.turn.gel_lower_dragbrace.gralin_lower_dragbrace'
gralin_lower_dragbrace.adams_id = 13
gralin_lower_dragbrace.angle_extent = 360.0
gralin_lower_dragbrace.length = 0.8636111118
gralin_lower_dragbrace.radius = 0.0254
gralin_lower_dragbrace.side_count_for_body = 15
gralin_lower_dragbrace.segment_count_for_ends = 15


graarm_uplock_tab = MakeSceneNodeByType('ShapePlate', '.turn.gel_lower_dragbrace.graarm_uplock_tab')
# >>>[ERROR] CAN NOT find link prop(marker_name) from .turn.gel_lower_dragbrace.graarm_uplock_tab, Please DOUBLE CHECK!
# >>>[ERROR] CAN NOT find link prop(width) from .turn.gel_lower_dragbrace.graarm_uplock_tab, Please DOUBLE CHECK!
# >>>[ERROR] CAN NOT find link prop(radius) from .turn.gel_lower_dragbrace.graarm_uplock_tab, Please DOUBLE CHECK!
graarm_uplock_tab.plate_name = '.turn.gel_lower_dragbrace.graarm_uplock_tab'


ger_lower_dragbrace = MakeSceneNodeByType('PartGeneral', '.turn.ger_lower_dragbrace')
ger_lower_dragbrace.part_name = '.turn.ger_lower_dragbrace'
ger_lower_dragbrace.adams_id = 11
ger_lower_dragbrace.location = Base.Vector (11.821751947, 1.3511956141, 1.2178735066)
ger_lower_dragbrace.orientation = Base.Vector (111.1963835462, 134.040966185, 285.0876334338)
cm = MakeSceneNodeByType('Marker', '.turn.ger_lower_dragbrace.cm')
cm.marker_name = '.turn.ger_lower_dragbrace.cm'
cm.adams_id = 139
cm.location = Base.Vector (0.0039348735476, -0.0068056064573, 0.024978613416)
cm.orientation = Base.Vector (30.0356927645, 1.0992652329, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_lower_dragbrace.inertia_frame')
inertia_frame.marker_name = '.turn.ger_lower_dragbrace.inertia_frame'
inertia_frame.adams_id = 140
inertia_frame.location = Base.Vector (0.0039348735476, -0.0068056064573, 0.024978613416)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_27 = MakeSceneNodeByType('Marker', '.turn.ger_lower_dragbrace.gralin_27')
gralin_27.marker_name = '.turn.ger_lower_dragbrace.gralin_27'
gralin_27.adams_id = 141
gralin_27.location = Base.Vector (0.0, 1.3320448911e-11, -0.4318055559)
gralin_27.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_i_14 = MakeSceneNodeByType('Marker', '.turn.ger_lower_dragbrace.jxr_joint_i_14')
jxr_joint_i_14.marker_name = '.turn.ger_lower_dragbrace.jxr_joint_i_14'
jxr_joint_i_14.adams_id = 142
jxr_joint_i_14.location = Base.Vector (0.0, 1.3319047254e-11, -0.4318055559)
jxr_joint_i_14.orientation = Base.Vector (346.9290323448, 90.2906925253, 46.3766345828)
jxr_joint_i_10 = MakeSceneNodeByType('Marker', '.turn.ger_lower_dragbrace.jxr_joint_i_10')
jxr_joint_i_10.marker_name = '.turn.ger_lower_dragbrace.jxr_joint_i_10'
jxr_joint_i_10.adams_id = 143
jxr_joint_i_10.location = Base.Vector (0.0, -1.3321316272e-11, 0.4318055559)
jxr_joint_i_10.orientation = Base.Vector (346.9290323448, 90.2906925253, 46.3766345828)
graarm_4 = MakeSceneNodeByType('Marker', '.turn.ger_lower_dragbrace.graarm_4')
graarm_4.marker_name = '.turn.ger_lower_dragbrace.graarm_4'
graarm_4.adams_id = 144
graarm_4.location = Base.Vector (0.070772384935, -0.1224052042, 0.1620383572)
graarm_4.orientation = Base.Vector (120.0356927562, 89.9999999999, 337.5559025676)
graarm_5 = MakeSceneNodeByType('Marker', '.turn.ger_lower_dragbrace.graarm_5')
graarm_5.marker_name = '.turn.ger_lower_dragbrace.graarm_5'
graarm_5.adams_id = 145
graarm_5.location = Base.Vector (0.0, 0.0, 0.1036333334)
graarm_5.orientation = Base.Vector (0.0, 0.0, 0.0)
graarm_6 = MakeSceneNodeByType('Marker', '.turn.ger_lower_dragbrace.graarm_6')
graarm_6.marker_name = '.turn.ger_lower_dragbrace.graarm_6'
graarm_6.adams_id = 146
graarm_6.location = Base.Vector (0.0, 0.0, 0.2072666668)
graarm_6.orientation = Base.Vector (0.0, 0.0, 0.0)
ger_lower_dragbrace = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.cm')
ger_lower_dragbrace.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.inertia_frame')
ger_lower_dragbrace.inertia_marker = inertia_marker
ger_lower_dragbrace.part_name = '.turn.ger_lower_dragbrace'
ger_lower_dragbrace.mass = 5.6992574801
ger_lower_dragbrace.ixx = 0.3211055352
ger_lower_dragbrace.iyy = 0.3193778028
ger_lower_dragbrace.izz = 0.005107174896
ger_lower_dragbrace.ixy = 0.0
ger_lower_dragbrace.izx = 0.0
ger_lower_dragbrace.iyz = 0.0
gralin_lower_dragbrace = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_lower_dragbrace.gralin_lower_dragbrace')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.gralin_27')
gralin_lower_dragbrace.center_marker = center_marker
gralin_lower_dragbrace.cylinder_name = '.turn.ger_lower_dragbrace.gralin_lower_dragbrace'
gralin_lower_dragbrace.adams_id = 14
gralin_lower_dragbrace.angle_extent = 360.0
gralin_lower_dragbrace.length = 0.8636111118
gralin_lower_dragbrace.radius = 0.0254
gralin_lower_dragbrace.side_count_for_body = 15
gralin_lower_dragbrace.segment_count_for_ends = 15


graarm_uplock_tab = MakeSceneNodeByType('ShapePlate', '.turn.ger_lower_dragbrace.graarm_uplock_tab')
# >>>[ERROR] CAN NOT find link prop(marker_name) from .turn.ger_lower_dragbrace.graarm_uplock_tab, Please DOUBLE CHECK!
# >>>[ERROR] CAN NOT find link prop(width) from .turn.ger_lower_dragbrace.graarm_uplock_tab, Please DOUBLE CHECK!
# >>>[ERROR] CAN NOT find link prop(radius) from .turn.ger_lower_dragbrace.graarm_uplock_tab, Please DOUBLE CHECK!
graarm_uplock_tab.plate_name = '.turn.ger_lower_dragbrace.graarm_uplock_tab'


gel_upper_torquearm = MakeSceneNodeByType('PartGeneral', '.turn.gel_upper_torquearm')
gel_upper_torquearm.part_name = '.turn.gel_upper_torquearm'
gel_upper_torquearm.adams_id = 12
gel_upper_torquearm.location = Base.Vector (12.0794524095, -1.4939074516, 0.6646292016)
gel_upper_torquearm.orientation = Base.Vector (264.4801161257, 168.6067018386, 84.5882371559)
cm = MakeSceneNodeByType('Marker', '.turn.gel_upper_torquearm.cm')
cm.marker_name = '.turn.gel_upper_torquearm.cm'
cm.adams_id = 147
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_upper_torquearm.inertia_frame')
inertia_frame.marker_name = '.turn.gel_upper_torquearm.inertia_frame'
inertia_frame.adams_id = 148
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_11 = MakeSceneNodeByType('Marker', '.turn.gel_upper_torquearm.gralin_11')
gralin_11.marker_name = '.turn.gel_upper_torquearm.gralin_11'
gralin_11.adams_id = 149
gralin_11.location = Base.Vector (0.0, 0.0, -0.1383335383)
gralin_11.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_i_2 = MakeSceneNodeByType('Marker', '.turn.gel_upper_torquearm.jxl_joint_i_2')
jxl_joint_i_2.marker_name = '.turn.gel_upper_torquearm.jxl_joint_i_2'
jxl_joint_i_2.adams_id = 150
jxl_joint_i_2.location = Base.Vector (0.0, 0.0, 0.1383335383)
jxl_joint_i_2.orientation = Base.Vector (273.4244432527, 89.9999731825, 177.0527623566)
jxl_joint_i_3 = MakeSceneNodeByType('Marker', '.turn.gel_upper_torquearm.jxl_joint_i_3')
jxl_joint_i_3.marker_name = '.turn.gel_upper_torquearm.jxl_joint_i_3'
jxl_joint_i_3.adams_id = 151
jxl_joint_i_3.location = Base.Vector (0.0, 0.0, -0.1383335383)
jxl_joint_i_3.orientation = Base.Vector (183.4245252295, 87.0529836943, 74.5991863345)
gel_upper_torquearm = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.cm')
gel_upper_torquearm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.inertia_frame')
gel_upper_torquearm.inertia_marker = inertia_marker
gel_upper_torquearm.part_name = '.turn.gel_upper_torquearm'
gel_upper_torquearm.mass = 1.5364744752
gel_upper_torquearm.ixx = 0.010048562438
gel_upper_torquearm.iyy = 0.010048562438
gel_upper_torquearm.izz = 0.00049563593622
gel_upper_torquearm.ixy = 0.0
gel_upper_torquearm.izx = 0.0
gel_upper_torquearm.iyz = 0.0
gralin_upper_torquearm = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_upper_torquearm.gralin_upper_torquearm')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.gralin_11')
gralin_upper_torquearm.center_marker = center_marker
gralin_upper_torquearm.cylinder_name = '.turn.gel_upper_torquearm.gralin_upper_torquearm'
gralin_upper_torquearm.adams_id = 15
gralin_upper_torquearm.angle_extent = 360.0
gralin_upper_torquearm.length = 0.2766670766
gralin_upper_torquearm.radius = 0.0254
gralin_upper_torquearm.side_count_for_body = 15
gralin_upper_torquearm.segment_count_for_ends = 15


ger_upper_torquearm = MakeSceneNodeByType('PartGeneral', '.turn.ger_upper_torquearm')
ger_upper_torquearm.part_name = '.turn.ger_upper_torquearm'
ger_upper_torquearm.adams_id = 13
ger_upper_torquearm.location = Base.Vector (12.0794524095, 1.4939074516, 0.6646292016)
ger_upper_torquearm.orientation = Base.Vector (275.5198838743, 168.6067018386, 95.4117628441)
cm = MakeSceneNodeByType('Marker', '.turn.ger_upper_torquearm.cm')
cm.marker_name = '.turn.ger_upper_torquearm.cm'
cm.adams_id = 152
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_upper_torquearm.inertia_frame')
inertia_frame.marker_name = '.turn.ger_upper_torquearm.inertia_frame'
inertia_frame.adams_id = 153
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_28 = MakeSceneNodeByType('Marker', '.turn.ger_upper_torquearm.gralin_28')
gralin_28.marker_name = '.turn.ger_upper_torquearm.gralin_28'
gralin_28.adams_id = 154
gralin_28.location = Base.Vector (0.0, 0.0, -0.1383335383)
gralin_28.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_i_2 = MakeSceneNodeByType('Marker', '.turn.ger_upper_torquearm.jxr_joint_i_2')
jxr_joint_i_2.marker_name = '.turn.ger_upper_torquearm.jxr_joint_i_2'
jxr_joint_i_2.adams_id = 155
jxr_joint_i_2.location = Base.Vector (0.0, 0.0, 0.1383335383)
jxr_joint_i_2.orientation = Base.Vector (266.5755567473, 89.9999731825, 2.9472376434)
jxr_joint_i_3 = MakeSceneNodeByType('Marker', '.turn.ger_upper_torquearm.jxr_joint_i_3')
jxr_joint_i_3.marker_name = '.turn.ger_upper_torquearm.jxr_joint_i_3'
jxr_joint_i_3.adams_id = 156
jxr_joint_i_3.location = Base.Vector (0.0, 0.0, -0.1383335383)
jxr_joint_i_3.orientation = Base.Vector (356.5754747705, 87.0529836943, 105.4008136655)
ger_upper_torquearm = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.cm')
ger_upper_torquearm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.inertia_frame')
ger_upper_torquearm.inertia_marker = inertia_marker
ger_upper_torquearm.part_name = '.turn.ger_upper_torquearm'
ger_upper_torquearm.mass = 1.5364744752
ger_upper_torquearm.ixx = 0.010048562438
ger_upper_torquearm.iyy = 0.010048562438
ger_upper_torquearm.izz = 0.00049563593622
ger_upper_torquearm.ixy = 0.0
ger_upper_torquearm.izx = 0.0
ger_upper_torquearm.iyz = 0.0
gralin_upper_torquearm = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_upper_torquearm.gralin_upper_torquearm')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.gralin_28')
gralin_upper_torquearm.center_marker = center_marker
gralin_upper_torquearm.cylinder_name = '.turn.ger_upper_torquearm.gralin_upper_torquearm'
gralin_upper_torquearm.adams_id = 16
gralin_upper_torquearm.angle_extent = 360.0
gralin_upper_torquearm.length = 0.2766670766
gralin_upper_torquearm.radius = 0.0254
gralin_upper_torquearm.side_count_for_body = 15
gralin_upper_torquearm.segment_count_for_ends = 15


gel_lower_torquearm = MakeSceneNodeByType('PartGeneral', '.turn.gel_lower_torquearm')
gel_lower_torquearm.part_name = '.turn.gel_lower_torquearm'
gel_lower_torquearm.adams_id = 14
gel_lower_torquearm.location = Base.Vector (12.0993426415, -1.5579375115, 0.4030923612)
gel_lower_torquearm.orientation = Base.Vector (274.806891489, 21.5573785759, 85.5279353352)
cm = MakeSceneNodeByType('Marker', '.turn.gel_lower_torquearm.cm')
cm.marker_name = '.turn.gel_lower_torquearm.cm'
cm.adams_id = 157
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_lower_torquearm.inertia_frame')
inertia_frame.marker_name = '.turn.gel_lower_torquearm.inertia_frame'
inertia_frame.adams_id = 158
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_29 = MakeSceneNodeByType('Marker', '.turn.gel_lower_torquearm.gralin_29')
gralin_29.marker_name = '.turn.gel_lower_torquearm.gralin_29'
gralin_29.adams_id = 159
gralin_29.location = Base.Vector (0.0, 0.0, -0.1387301713)
gralin_29.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_i_11 = MakeSceneNodeByType('Marker', '.turn.gel_lower_torquearm.jxl_joint_i_11')
jxl_joint_i_11.marker_name = '.turn.gel_lower_torquearm.jxl_joint_i_11'
jxl_joint_i_11.adams_id = 160
jxl_joint_i_11.location = Base.Vector (0.0, 0.0, -0.1387301713)
jxl_joint_i_11.orientation = Base.Vector (178.1282947989, 95.1813481522, 287.4366988554)
jxl_joint_i_1 = MakeSceneNodeByType('Marker', '.turn.gel_lower_torquearm.jxl_joint_i_1')
jxl_joint_i_1.marker_name = '.turn.gel_lower_torquearm.jxl_joint_i_1'
jxl_joint_i_1.adams_id = 161
jxl_joint_i_1.location = Base.Vector (0.0, 0.0, 0.1387301713)
jxl_joint_i_1.orientation = Base.Vector (178.1282565411, 95.1813639555, 331.2687567728)
gel_lower_torquearm = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.cm')
gel_lower_torquearm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.inertia_frame')
gel_lower_torquearm.inertia_marker = inertia_marker
gel_lower_torquearm.part_name = '.turn.gel_lower_torquearm'
gel_lower_torquearm.mass = 0.45359237
gel_lower_torquearm.ixx = 0.00029263965343
gel_lower_torquearm.iyy = 0.00029263965343
gel_lower_torquearm.izz = 0.00029263965343
gel_lower_torquearm.ixy = 0.0
gel_lower_torquearm.izx = 0.0
gel_lower_torquearm.iyz = 0.0
gralin_lower_torquearm = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_lower_torquearm.gralin_lower_torquearm')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.gralin_29')
gralin_lower_torquearm.center_marker = center_marker
gralin_lower_torquearm.cylinder_name = '.turn.gel_lower_torquearm.gralin_lower_torquearm'
gralin_lower_torquearm.adams_id = 17
gralin_lower_torquearm.angle_extent = 360.0
gralin_lower_torquearm.length = 0.2774603426
gralin_lower_torquearm.radius = 0.0254
gralin_lower_torquearm.side_count_for_body = 15
gralin_lower_torquearm.segment_count_for_ends = 15


ger_lower_torquearm = MakeSceneNodeByType('PartGeneral', '.turn.ger_lower_torquearm')
ger_lower_torquearm.part_name = '.turn.ger_lower_torquearm'
ger_lower_torquearm.adams_id = 15
ger_lower_torquearm.location = Base.Vector (12.0993426415, 1.5579375115, 0.4030923612)
ger_lower_torquearm.orientation = Base.Vector (265.193108511, 21.5573785759, 94.4720646648)
cm = MakeSceneNodeByType('Marker', '.turn.ger_lower_torquearm.cm')
cm.marker_name = '.turn.ger_lower_torquearm.cm'
cm.adams_id = 162
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_lower_torquearm.inertia_frame')
inertia_frame.marker_name = '.turn.ger_lower_torquearm.inertia_frame'
inertia_frame.adams_id = 163
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_30 = MakeSceneNodeByType('Marker', '.turn.ger_lower_torquearm.gralin_30')
gralin_30.marker_name = '.turn.ger_lower_torquearm.gralin_30'
gralin_30.adams_id = 164
gralin_30.location = Base.Vector (0.0, 0.0, -0.1387301713)
gralin_30.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_i_11 = MakeSceneNodeByType('Marker', '.turn.ger_lower_torquearm.jxr_joint_i_11')
jxr_joint_i_11.marker_name = '.turn.ger_lower_torquearm.jxr_joint_i_11'
jxr_joint_i_11.adams_id = 165
jxr_joint_i_11.location = Base.Vector (0.0, 0.0, -0.1387301713)
jxr_joint_i_11.orientation = Base.Vector (1.8717052011, 95.1813481522, 252.5633011446)
jxr_joint_i_1 = MakeSceneNodeByType('Marker', '.turn.ger_lower_torquearm.jxr_joint_i_1')
jxr_joint_i_1.marker_name = '.turn.ger_lower_torquearm.jxr_joint_i_1'
jxr_joint_i_1.adams_id = 166
jxr_joint_i_1.location = Base.Vector (0.0, 0.0, 0.1387301713)
jxr_joint_i_1.orientation = Base.Vector (1.8717434589, 95.1813639555, 208.7312432272)
ger_lower_torquearm = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.cm')
ger_lower_torquearm.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.inertia_frame')
ger_lower_torquearm.inertia_marker = inertia_marker
ger_lower_torquearm.part_name = '.turn.ger_lower_torquearm'
ger_lower_torquearm.mass = 0.45359237
ger_lower_torquearm.ixx = 0.00029263965343
ger_lower_torquearm.iyy = 0.00029263965343
ger_lower_torquearm.izz = 0.00029263965343
ger_lower_torquearm.ixy = 0.0
ger_lower_torquearm.izx = 0.0
ger_lower_torquearm.iyz = 0.0
gralin_lower_torquearm = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_lower_torquearm.gralin_lower_torquearm')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.gralin_30')
gralin_lower_torquearm.center_marker = center_marker
gralin_lower_torquearm.cylinder_name = '.turn.ger_lower_torquearm.gralin_lower_torquearm'
gralin_lower_torquearm.adams_id = 18
gralin_lower_torquearm.angle_extent = 360.0
gralin_lower_torquearm.length = 0.2774603426
gralin_lower_torquearm.radius = 0.0254
gralin_lower_torquearm.side_count_for_body = 15
gralin_lower_torquearm.segment_count_for_ends = 15


gel_connector = MakeSceneNodeByType('PartGeneral', '.turn.gel_connector')
gel_connector.part_name = '.turn.gel_connector'
gel_connector.adams_id = 17
gel_connector.location = Base.Vector (12.0491222568, -1.5512110073, 0.5316382052)
gel_connector.orientation = Base.Vector (177.0103140237, 92.4964937717, 309.8285622575)
cm = MakeSceneNodeByType('Marker', '.turn.gel_connector.cm')
cm.marker_name = '.turn.gel_connector.cm'
cm.adams_id = 169
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_connector.inertia_frame')
inertia_frame.marker_name = '.turn.gel_connector.inertia_frame'
inertia_frame.adams_id = 170
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_3 = MakeSceneNodeByType('Marker', '.turn.gel_connector.gralin_3')
gralin_3.marker_name = '.turn.gel_connector.gralin_3'
gralin_3.adams_id = 171
gralin_3.location = Base.Vector (0.0, 0.0, -0.060070847244)
gralin_3.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_1 = MakeSceneNodeByType('Marker', '.turn.gel_connector.jxl_joint_j_1')
jxl_joint_j_1.marker_name = '.turn.gel_connector.jxl_joint_j_1'
jxl_joint_j_1.adams_id = 172
jxl_joint_j_1.location = Base.Vector (-3.2030729616e-08, -3.9921403722e-08, -0.011023458626)
jxl_joint_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_2 = MakeSceneNodeByType('Marker', '.turn.gel_connector.jxl_joint_j_2')
jxl_joint_j_2.marker_name = '.turn.gel_connector.jxl_joint_j_2'
jxl_joint_j_2.adams_id = 173
jxl_joint_j_2.location = Base.Vector (0.0, 0.0, 0.060070847244)
jxl_joint_j_2.orientation = Base.Vector (331.5687748605, 89.9998761701, 89.9997712794)
gel_connector = Jusme.ActiveUSScene.getObject('.turn.gel_connector')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_connector.cm')
gel_connector.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_connector.inertia_frame')
gel_connector.inertia_marker = inertia_marker
gel_connector.part_name = '.turn.gel_connector'
gel_connector.mass = 0.45359237
gel_connector.ixx = 0.00029263965343
gel_connector.iyy = 0.00029263965343
gel_connector.izz = 0.00029263965343
gel_connector.ixy = 0.0
gel_connector.izx = 0.0
gel_connector.iyz = 0.0
gralin_connector = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_connector.gralin_connector')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_connector.gralin_3')
gralin_connector.center_marker = center_marker
gralin_connector.cylinder_name = '.turn.gel_connector.gralin_connector'
gralin_connector.adams_id = 19
gralin_connector.angle_extent = 360.0
gralin_connector.length = 0.1201416945
gralin_connector.radius = 0.0127
gralin_connector.side_count_for_body = 15
gralin_connector.segment_count_for_ends = 15


ger_connector = MakeSceneNodeByType('PartGeneral', '.turn.ger_connector')
ger_connector.part_name = '.turn.ger_connector'
ger_connector.adams_id = 18
ger_connector.location = Base.Vector (12.0491222568, 1.5512110073, 0.5316382052)
ger_connector.orientation = Base.Vector (2.9896859763, 92.4964937717, 230.1714377425)
cm = MakeSceneNodeByType('Marker', '.turn.ger_connector.cm')
cm.marker_name = '.turn.ger_connector.cm'
cm.adams_id = 174
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_connector.inertia_frame')
inertia_frame.marker_name = '.turn.ger_connector.inertia_frame'
inertia_frame.adams_id = 175
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_4 = MakeSceneNodeByType('Marker', '.turn.ger_connector.gralin_4')
gralin_4.marker_name = '.turn.ger_connector.gralin_4'
gralin_4.adams_id = 176
gralin_4.location = Base.Vector (0.0, 0.0, -0.060070847244)
gralin_4.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_j_1 = MakeSceneNodeByType('Marker', '.turn.ger_connector.jxr_joint_j_1')
jxr_joint_j_1.marker_name = '.turn.ger_connector.jxr_joint_j_1'
jxr_joint_j_1.adams_id = 177
jxr_joint_j_1.location = Base.Vector (-3.2030729618e-08, 3.9921403724e-08, -0.011023458626)
jxr_joint_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_j_2 = MakeSceneNodeByType('Marker', '.turn.ger_connector.jxr_joint_j_2')
jxr_joint_j_2.marker_name = '.turn.ger_connector.jxr_joint_j_2'
jxr_joint_j_2.adams_id = 178
jxr_joint_j_2.location = Base.Vector (0.0, 0.0, 0.060070847244)
jxr_joint_j_2.orientation = Base.Vector (208.4312251395, 89.9998761701, 90.0002287206)
ger_connector = Jusme.ActiveUSScene.getObject('.turn.ger_connector')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_connector.cm')
ger_connector.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_connector.inertia_frame')
ger_connector.inertia_marker = inertia_marker
ger_connector.part_name = '.turn.ger_connector'
ger_connector.mass = 0.45359237
ger_connector.ixx = 0.00029263965343
ger_connector.iyy = 0.00029263965343
ger_connector.izz = 0.00029263965343
ger_connector.ixy = 0.0
ger_connector.izx = 0.0
ger_connector.iyz = 0.0
gralin_connector = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_connector.gralin_connector')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_connector.gralin_4')
gralin_connector.center_marker = center_marker
gralin_connector.cylinder_name = '.turn.ger_connector.gralin_connector'
gralin_connector.adams_id = 20
gralin_connector.angle_extent = 360.0
gralin_connector.length = 0.1201416945
gralin_connector.radius = 0.0127
gralin_connector.side_count_for_body = 15
gralin_connector.segment_count_for_ends = 15


gel_uc_collar = MakeSceneNodeByType('PartGeneral', '.turn.gel_uc_collar')
gel_uc_collar.part_name = '.turn.gel_uc_collar'
gel_uc_collar.adams_id = 19
gel_uc_collar.location = Base.Vector (12.2235346711, -1.4991580222, 0.8799979074)
gel_uc_collar.orientation = Base.Vector (55.1145661544, 175.2828647294, 235.2057167569)
cm = MakeSceneNodeByType('Marker', '.turn.gel_uc_collar.cm')
cm.marker_name = '.turn.gel_uc_collar.cm'
cm.adams_id = 179
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_uc_collar.inertia_frame')
inertia_frame.marker_name = '.turn.gel_uc_collar.inertia_frame'
inertia_frame.adams_id = 180
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_5 = MakeSceneNodeByType('Marker', '.turn.gel_uc_collar.gralin_5')
gralin_5.marker_name = '.turn.gel_uc_collar.gralin_5'
gralin_5.adams_id = 181
gralin_5.location = Base.Vector (-5.4270445776e-11, 6.2140246074e-11, -0.1089542389)
gralin_5.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_3 = MakeSceneNodeByType('Marker', '.turn.gel_uc_collar.jxl_joint_j_3')
jxl_joint_j_3.marker_name = '.turn.gel_uc_collar.jxl_joint_j_3'
jxl_joint_j_3.adams_id = 182
jxl_joint_j_3.location = Base.Vector (0.1220018852, 0.0059907463311, 0.071482951808)
jxl_joint_j_3.orientation = Base.Vector (182.811221391, 89.9999933852, 90.0001347091)
jxl_joint_i_4 = MakeSceneNodeByType('Marker', '.turn.gel_uc_collar.jxl_joint_i_4')
jxl_joint_i_4.marker_name = '.turn.gel_uc_collar.jxl_joint_i_4'
jxl_joint_i_4.adams_id = 183
jxl_joint_i_4.location = Base.Vector (-1.720947864e-11, 4.273941026e-11, 1.8185791048e-11)
jxl_joint_i_4.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_10 = MakeSceneNodeByType('Marker', '.turn.gel_uc_collar.jxl_joint_j_10')
jxl_joint_j_10.marker_name = '.turn.gel_uc_collar.jxl_joint_j_10'
jxl_joint_j_10.adams_id = 184
jxl_joint_j_10.location = Base.Vector (0.1095796703, 0.0335667969, -0.04683031071)
jxl_joint_j_10.orientation = Base.Vector (199.444502672, 90.0, 92.2365720495)
gel_uc_collar = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.cm')
gel_uc_collar.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.inertia_frame')
gel_uc_collar.inertia_marker = inertia_marker
gel_uc_collar.part_name = '.turn.gel_uc_collar'
gel_uc_collar.mass = 30.2539444008
gel_uc_collar.ixx = 0.2417065893
gel_uc_collar.iyy = 0.2417065893
gel_uc_collar.izz = 0.2439829346
gel_uc_collar.ixy = 0.0
gel_uc_collar.izx = 0.0
gel_uc_collar.iyz = 0.0
gralin_uc_collar = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_uc_collar.gralin_uc_collar')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.gralin_5')
gralin_uc_collar.center_marker = center_marker
gralin_uc_collar.cylinder_name = '.turn.gel_uc_collar.gralin_uc_collar'
gralin_uc_collar.adams_id = 21
gralin_uc_collar.angle_extent = 360.0
gralin_uc_collar.length = 0.2179084778
gralin_uc_collar.radius = 0.127
gralin_uc_collar.side_count_for_body = 15
gralin_uc_collar.segment_count_for_ends = 15


ger_uc_collar = MakeSceneNodeByType('PartGeneral', '.turn.ger_uc_collar')
ger_uc_collar.part_name = '.turn.ger_uc_collar'
ger_uc_collar.adams_id = 20
ger_uc_collar.location = Base.Vector (12.2235346711, 1.4991580222, 0.8799979074)
ger_uc_collar.orientation = Base.Vector (124.8854338456, 175.2828647294, 304.7942832431)
cm = MakeSceneNodeByType('Marker', '.turn.ger_uc_collar.cm')
cm.marker_name = '.turn.ger_uc_collar.cm'
cm.adams_id = 185
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_uc_collar.inertia_frame')
inertia_frame.marker_name = '.turn.ger_uc_collar.inertia_frame'
inertia_frame.adams_id = 186
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_6 = MakeSceneNodeByType('Marker', '.turn.ger_uc_collar.gralin_6')
gralin_6.marker_name = '.turn.ger_uc_collar.gralin_6'
gralin_6.adams_id = 187
gralin_6.location = Base.Vector (-5.4270460521e-11, -6.2140235665e-11, -0.1089542389)
gralin_6.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_j_3 = MakeSceneNodeByType('Marker', '.turn.ger_uc_collar.jxr_joint_j_3')
jxr_joint_j_3.marker_name = '.turn.ger_uc_collar.jxr_joint_j_3'
jxr_joint_j_3.adams_id = 188
jxr_joint_j_3.location = Base.Vector (0.1220018852, -0.0059907463311, 0.071482951808)
jxr_joint_j_3.orientation = Base.Vector (357.188778609, 89.9999933852, 89.9998652909)
jxr_joint_i_4 = MakeSceneNodeByType('Marker', '.turn.ger_uc_collar.jxr_joint_i_4')
jxr_joint_i_4.marker_name = '.turn.ger_uc_collar.jxr_joint_i_4'
jxr_joint_i_4.adams_id = 189
jxr_joint_i_4.location = Base.Vector (-1.720947864e-11, -4.2738966662e-11, 1.8185811935e-11)
jxr_joint_i_4.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_j_10 = MakeSceneNodeByType('Marker', '.turn.ger_uc_collar.jxr_joint_j_10')
jxr_joint_j_10.marker_name = '.turn.ger_uc_collar.jxr_joint_j_10'
jxr_joint_j_10.adams_id = 190
jxr_joint_j_10.location = Base.Vector (0.1095796703, -0.0335667969, -0.04683031071)
jxr_joint_j_10.orientation = Base.Vector (340.555497328, 90.0, 87.7634279505)
ger_uc_collar = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.cm')
ger_uc_collar.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.inertia_frame')
ger_uc_collar.inertia_marker = inertia_marker
ger_uc_collar.part_name = '.turn.ger_uc_collar'
ger_uc_collar.mass = 30.2539444008
ger_uc_collar.ixx = 0.2417065893
ger_uc_collar.iyy = 0.2417065893
ger_uc_collar.izz = 0.2439829346
ger_uc_collar.ixy = 0.0
ger_uc_collar.izx = 0.0
ger_uc_collar.iyz = 0.0
gralin_uc_collar = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_uc_collar.gralin_uc_collar')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.gralin_6')
gralin_uc_collar.center_marker = center_marker
gralin_uc_collar.cylinder_name = '.turn.ger_uc_collar.gralin_uc_collar'
gralin_uc_collar.adams_id = 22
gralin_uc_collar.angle_extent = 360.0
gralin_uc_collar.length = 0.2179084778
gralin_uc_collar.radius = 0.127
gralin_uc_collar.side_count_for_body = 15
gralin_uc_collar.segment_count_for_ends = 15


gel_spindle = MakeSceneNodeByType('PartGeneral', '.turn.gel_spindle')
gel_spindle.part_name = '.turn.gel_spindle'
gel_spindle.adams_id = 21
gel_spindle.location = Base.Vector (10.870365356, -0.9895344548, 2.09911815)
gel_spindle.orientation = Base.Vector (70.4651745203, 87.687537877, 270.820189184)
cm = MakeSceneNodeByType('Marker', '.turn.gel_spindle.cm')
cm.marker_name = '.turn.gel_spindle.cm'
cm.adams_id = 191
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_spindle.inertia_frame')
inertia_frame.marker_name = '.turn.gel_spindle.inertia_frame'
inertia_frame.adams_id = 192
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_7 = MakeSceneNodeByType('Marker', '.turn.gel_spindle.gralin_7')
gralin_7.marker_name = '.turn.gel_spindle.gralin_7'
gralin_7.adams_id = 193
gralin_7.location = Base.Vector (0.0, 3.7493150599e-11, -0.098425002805)
gralin_7.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_5 = MakeSceneNodeByType('Marker', '.turn.gel_spindle.jxl_joint_j_5')
jxl_joint_j_5.marker_name = '.turn.gel_spindle.jxl_joint_j_5'
jxl_joint_j_5.adams_id = 194
jxl_joint_j_5.location = Base.Vector (0.0, 5.6759770251e-11, 0.098425002771)
jxl_joint_j_5.orientation = Base.Vector (357.8896246814, 0.0, 0.0)
gel_spindle = Jusme.ActiveUSScene.getObject('.turn.gel_spindle')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.cm')
gel_spindle.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.inertia_frame')
gel_spindle.inertia_marker = inertia_marker
gel_spindle.part_name = '.turn.gel_spindle'
gel_spindle.mass = 0.45359237
gel_spindle.ixx = 0.00029263965343
gel_spindle.iyy = 0.00029263965343
gel_spindle.izz = 0.00029263965343
gel_spindle.ixy = 0.0
gel_spindle.izx = 0.0
gel_spindle.iyz = 0.0
gralin_spindle = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_spindle.gralin_spindle')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.gralin_7')
gralin_spindle.center_marker = center_marker
gralin_spindle.cylinder_name = '.turn.gel_spindle.gralin_spindle'
gralin_spindle.adams_id = 23
gralin_spindle.angle_extent = 360.0
gralin_spindle.length = 0.1968500056
gralin_spindle.radius = 0.0254
gralin_spindle.side_count_for_body = 15
gralin_spindle.segment_count_for_ends = 15


ger_spindle = MakeSceneNodeByType('PartGeneral', '.turn.ger_spindle')
ger_spindle.part_name = '.turn.ger_spindle'
ger_spindle.adams_id = 22
ger_spindle.location = Base.Vector (10.870365356, 0.9895344548, 2.09911815)
ger_spindle.orientation = Base.Vector (109.5348254797, 87.687537877, 269.179810816)
cm = MakeSceneNodeByType('Marker', '.turn.ger_spindle.cm')
cm.marker_name = '.turn.ger_spindle.cm'
cm.adams_id = 196
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_spindle.inertia_frame')
inertia_frame.marker_name = '.turn.ger_spindle.inertia_frame'
inertia_frame.adams_id = 197
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_8 = MakeSceneNodeByType('Marker', '.turn.ger_spindle.gralin_8')
gralin_8.marker_name = '.turn.ger_spindle.gralin_8'
gralin_8.adams_id = 198
gralin_8.location = Base.Vector (0.0, -3.7493149149e-11, -0.098425002805)
gralin_8.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_j_5 = MakeSceneNodeByType('Marker', '.turn.ger_spindle.jxr_joint_j_5')
jxr_joint_j_5.marker_name = '.turn.ger_spindle.jxr_joint_j_5'
jxr_joint_j_5.adams_id = 199
jxr_joint_j_5.location = Base.Vector (0.0, -5.6759771708e-11, 0.098425002771)
jxr_joint_j_5.orientation = Base.Vector (2.1103753186, 0.0, 0.0)
ger_spindle = Jusme.ActiveUSScene.getObject('.turn.ger_spindle')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.cm')
ger_spindle.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.inertia_frame')
ger_spindle.inertia_marker = inertia_marker
ger_spindle.part_name = '.turn.ger_spindle'
ger_spindle.mass = 0.45359237
ger_spindle.ixx = 0.00029263965343
ger_spindle.iyy = 0.00029263965343
ger_spindle.izz = 0.00029263965343
ger_spindle.ixy = 0.0
ger_spindle.izx = 0.0
ger_spindle.iyz = 0.0
gralin_spindle = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_spindle.gralin_spindle')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.gralin_8')
gralin_spindle.center_marker = center_marker
gralin_spindle.cylinder_name = '.turn.ger_spindle.gralin_spindle'
gralin_spindle.adams_id = 24
gralin_spindle.angle_extent = 360.0
gralin_spindle.length = 0.1968500056
gralin_spindle.radius = 0.0254
gralin_spindle.side_count_for_body = 15
gralin_spindle.segment_count_for_ends = 15


gel_lwract = MakeSceneNodeByType('PartGeneral', '.turn.gel_lwract')
gel_lwract.part_name = '.turn.gel_lwract'
gel_lwract.adams_id = 23
gel_lwract.location = Base.Vector (12.3035450581, -1.3321655373, 1.6036216233)
gel_lwract.orientation = Base.Vector (182.4778087702, 7.7973026753, 177.4990974089)
cm = MakeSceneNodeByType('Marker', '.turn.gel_lwract.cm')
cm.marker_name = '.turn.gel_lwract.cm'
cm.adams_id = 201
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_lwract.inertia_frame')
inertia_frame.marker_name = '.turn.gel_lwract.inertia_frame'
inertia_frame.adams_id = 202
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_9 = MakeSceneNodeByType('Marker', '.turn.gel_lwract.gralin_9')
gralin_9.marker_name = '.turn.gel_lwract.gralin_9'
gralin_9.adams_id = 203
gralin_9.location = Base.Vector (-1.1798721722e-11, -4.3827205753e-11, -0.3002385778)
gralin_9.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_7 = MakeSceneNodeByType('Marker', '.turn.gel_lwract.jxl_joint_j_7')
jxl_joint_j_7.marker_name = '.turn.gel_lwract.jxl_joint_j_7'
jxl_joint_j_7.adams_id = 204
jxl_joint_j_7.location = Base.Vector (-1.1798721722e-11, -4.3827205753e-11, -0.3002385778)
jxl_joint_j_7.orientation = Base.Vector (2.5009025911, 7.7973026753, 357.5221912298)
jxl_joint_i_8 = MakeSceneNodeByType('Marker', '.turn.gel_lwract.jxl_joint_i_8')
jxl_joint_i_8.marker_name = '.turn.gel_lwract.jxl_joint_i_8'
jxl_joint_i_8.adams_id = 205
jxl_joint_i_8.location = Base.Vector (-1.1820562107e-11, -4.412834681e-11, 0.3002385778)
jxl_joint_i_8.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_stopper_i_2 = MakeSceneNodeByType('Marker', '.turn.gel_lwract.uel_stopper_i_2')
uel_stopper_i_2.marker_name = '.turn.gel_lwract.uel_stopper_i_2'
uel_stopper_i_2.adams_id = 206
uel_stopper_i_2.location = Base.Vector (-1.1798721722e-11, -4.3827205753e-11, -0.3002385778)
uel_stopper_i_2.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_actuator_j_1 = MakeSceneNodeByType('Marker', '.turn.gel_lwract.uel_actuator_j_1')
uel_actuator_j_1.marker_name = '.turn.gel_lwract.uel_actuator_j_1'
uel_actuator_j_1.adams_id = 207
uel_actuator_j_1.location = Base.Vector (-1.1798721722e-11, -4.3827205753e-11, -0.3002385778)
uel_actuator_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_actuator_i_2 = MakeSceneNodeByType('Marker', '.turn.gel_lwract.uel_actuator_i_2')
uel_actuator_i_2.marker_name = '.turn.gel_lwract.uel_actuator_i_2'
uel_actuator_i_2.adams_id = 208
uel_actuator_i_2.location = Base.Vector (-1.1818784666e-11, -4.4128145582e-11, 0.3002385778)
uel_actuator_i_2.orientation = Base.Vector (0.0, 0.0, 0.0)
gel_lwract = Jusme.ActiveUSScene.getObject('.turn.gel_lwract')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.cm')
gel_lwract.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.inertia_frame')
gel_lwract.inertia_marker = inertia_marker
gel_lwract.part_name = '.turn.gel_lwract'
gel_lwract.mass = 0.45359237
gel_lwract.ixx = 0.00029263965343
gel_lwract.iyy = 0.00029263965343
gel_lwract.izz = 0.00029263965343
gel_lwract.ixy = 0.0
gel_lwract.izx = 0.0
gel_lwract.iyz = 0.0
gralin_lwract = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_lwract.gralin_lwract')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.gralin_9')
gralin_lwract.center_marker = center_marker
gralin_lwract.cylinder_name = '.turn.gel_lwract.gralin_lwract'
gralin_lwract.adams_id = 25
gralin_lwract.angle_extent = 360.0
gralin_lwract.length = 0.6004771556
gralin_lwract.radius = 0.00762
gralin_lwract.side_count_for_body = 15
gralin_lwract.segment_count_for_ends = 15


ger_lwract = MakeSceneNodeByType('PartGeneral', '.turn.ger_lwract')
ger_lwract.part_name = '.turn.ger_lwract'
ger_lwract.adams_id = 24
ger_lwract.location = Base.Vector (12.3035450581, 1.3321655373, 1.6036216233)
ger_lwract.orientation = Base.Vector (357.5221912298, 7.7973026753, 2.5009025911)
cm = MakeSceneNodeByType('Marker', '.turn.ger_lwract.cm')
cm.marker_name = '.turn.ger_lwract.cm'
cm.adams_id = 209
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_lwract.inertia_frame')
inertia_frame.marker_name = '.turn.ger_lwract.inertia_frame'
inertia_frame.adams_id = 210
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_10 = MakeSceneNodeByType('Marker', '.turn.ger_lwract.gralin_10')
gralin_10.marker_name = '.turn.ger_lwract.gralin_10'
gralin_10.adams_id = 211
gralin_10.location = Base.Vector (-1.1798754898e-11, 4.3827212692e-11, -0.3002385778)
gralin_10.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_j_7 = MakeSceneNodeByType('Marker', '.turn.ger_lwract.jxr_joint_j_7')
jxr_joint_j_7.marker_name = '.turn.ger_lwract.jxr_joint_j_7'
jxr_joint_j_7.adams_id = 212
jxr_joint_j_7.location = Base.Vector (-1.1798754898e-11, 4.3827212692e-11, -0.3002385778)
jxr_joint_j_7.orientation = Base.Vector (177.4990974089, 7.7973026753, 182.4778087702)
jxr_joint_i_8 = MakeSceneNodeByType('Marker', '.turn.ger_lwract.jxr_joint_i_8')
jxr_joint_i_8.marker_name = '.turn.ger_lwract.jxr_joint_i_8'
jxr_joint_i_8.adams_id = 213
jxr_joint_i_8.location = Base.Vector (-1.1820528931e-11, 4.412878396e-11, 0.3002385778)
jxr_joint_i_8.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_stopper_i_2 = MakeSceneNodeByType('Marker', '.turn.ger_lwract.uer_stopper_i_2')
uer_stopper_i_2.marker_name = '.turn.ger_lwract.uer_stopper_i_2'
uer_stopper_i_2.adams_id = 214
uer_stopper_i_2.location = Base.Vector (-1.1798754898e-11, 4.3827212692e-11, -0.3002385778)
uer_stopper_i_2.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_actuator_i_2 = MakeSceneNodeByType('Marker', '.turn.ger_lwract.uer_actuator_i_2')
uer_actuator_i_2.marker_name = '.turn.ger_lwract.uer_actuator_i_2'
uer_actuator_i_2.adams_id = 215
uer_actuator_i_2.location = Base.Vector (-1.182052763e-11, 4.4129026822e-11, 0.3002385778)
uer_actuator_i_2.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_actuator_j_1 = MakeSceneNodeByType('Marker', '.turn.ger_lwract.uer_actuator_j_1')
uer_actuator_j_1.marker_name = '.turn.ger_lwract.uer_actuator_j_1'
uer_actuator_j_1.adams_id = 216
uer_actuator_j_1.location = Base.Vector (-1.1798754898e-11, 4.3827212692e-11, -0.3002385778)
uer_actuator_j_1.orientation = Base.Vector (0.0, 0.0, 0.0)
ger_lwract = Jusme.ActiveUSScene.getObject('.turn.ger_lwract')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.cm')
ger_lwract.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.inertia_frame')
ger_lwract.inertia_marker = inertia_marker
ger_lwract.part_name = '.turn.ger_lwract'
ger_lwract.mass = 0.45359237
ger_lwract.ixx = 0.00029263965343
ger_lwract.iyy = 0.00029263965343
ger_lwract.izz = 0.00029263965343
ger_lwract.ixy = 0.0
ger_lwract.izx = 0.0
ger_lwract.iyz = 0.0
gralin_lwract = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_lwract.gralin_lwract')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.gralin_10')
gralin_lwract.center_marker = center_marker
gralin_lwract.cylinder_name = '.turn.ger_lwract.gralin_lwract'
gralin_lwract.adams_id = 26
gralin_lwract.angle_extent = 360.0
gralin_lwract.length = 0.6004771556
gralin_lwract.radius = 0.00762
gralin_lwract.side_count_for_body = 15
gralin_lwract.segment_count_for_ends = 15


gel_upract = MakeSceneNodeByType('PartGeneral', '.turn.gel_upract')
gel_upract.part_name = '.turn.gel_upract'
gel_upract.adams_id = 25
gel_upract.location = Base.Vector (12.3026262812, -1.3109333827, 1.7588195227)
gel_upract.orientation = Base.Vector (182.4778087702, 7.7973026753, 177.4990974089)
uel_actuator_i_1 = MakeSceneNodeByType('Marker', '.turn.gel_upract.uel_actuator_i_1')
uel_actuator_i_1.marker_name = '.turn.gel_upract.uel_actuator_i_1'
uel_actuator_i_1.adams_id = 217
uel_actuator_i_1.location = Base.Vector (-3.9769937126e-11, 0.0, 0.1958077682)
uel_actuator_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.turn.gel_upract.cm')
cm.marker_name = '.turn.gel_upract.cm'
cm.adams_id = 218
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.gel_upract.inertia_frame')
inertia_frame.marker_name = '.turn.gel_upract.inertia_frame'
inertia_frame.adams_id = 219
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_18 = MakeSceneNodeByType('Marker', '.turn.gel_upract.gralin_18')
gralin_18.marker_name = '.turn.gel_upract.gralin_18'
gralin_18.adams_id = 220
gralin_18.location = Base.Vector (-3.9755074449e-11, 0.0, -0.1958077681)
gralin_18.orientation = Base.Vector (0.0, 0.0, 0.0)
jxl_joint_j_8 = MakeSceneNodeByType('Marker', '.turn.gel_upract.jxl_joint_j_8')
jxl_joint_j_8.marker_name = '.turn.gel_upract.jxl_joint_j_8'
jxl_joint_j_8.adams_id = 221
jxl_joint_j_8.location = Base.Vector (-3.976996846e-11, 0.0, 0.1435923633)
jxl_joint_j_8.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_stopper_j_2 = MakeSceneNodeByType('Marker', '.turn.gel_upract.uel_stopper_j_2')
uel_stopper_j_2.marker_name = '.turn.gel_upract.uel_stopper_j_2'
uel_stopper_j_2.adams_id = 223
uel_stopper_j_2.location = Base.Vector (-3.9769937126e-11, 0.0, 0.1958077682)
uel_stopper_j_2.orientation = Base.Vector (0.0, 0.0, 0.0)
uel_actuator_j_2 = MakeSceneNodeByType('Marker', '.turn.gel_upract.uel_actuator_j_2')
uel_actuator_j_2.marker_name = '.turn.gel_upract.uel_actuator_j_2'
uel_actuator_j_2.adams_id = 224
uel_actuator_j_2.location = Base.Vector (-3.9768190802e-11, 0.0, 0.1435923633)
uel_actuator_j_2.orientation = Base.Vector (0.0, 0.0, 0.0)
gel_upract = Jusme.ActiveUSScene.getObject('.turn.gel_upract')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upract.cm')
gel_upract.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upract.inertia_frame')
gel_upract.inertia_marker = inertia_marker
gel_upract.part_name = '.turn.gel_upract'
gel_upract.mass = 0.45359237
gel_upract.ixx = 0.00029263965343
gel_upract.iyy = 0.00029263965343
gel_upract.izz = 0.00029263965343
gel_upract.ixy = 0.0
gel_upract.izx = 0.0
gel_upract.iyz = 0.0
gralin_upract = MakeSceneNodeByType('ShapeCylinder', '.turn.gel_upract.gralin_upract')
center_marker = Jusme.ActiveUSScene.getObject('.turn.gel_upract.gralin_18')
gralin_upract.center_marker = center_marker
gralin_upract.cylinder_name = '.turn.gel_upract.gralin_upract'
gralin_upract.adams_id = 27
gralin_upract.angle_extent = 360.0
gralin_upract.length = 0.3916155363
gralin_upract.radius = 0.01778
gralin_upract.side_count_for_body = 15
gralin_upract.segment_count_for_ends = 15


ger_upract = MakeSceneNodeByType('PartGeneral', '.turn.ger_upract')
ger_upract.part_name = '.turn.ger_upract'
ger_upract.adams_id = 26
ger_upract.location = Base.Vector (12.3026262812, 1.3109333827, 1.7588195227)
ger_upract.orientation = Base.Vector (357.5221912298, 7.7973026753, 2.5009025911)
uer_actuator_i_1 = MakeSceneNodeByType('Marker', '.turn.ger_upract.uer_actuator_i_1')
uer_actuator_i_1.marker_name = '.turn.ger_upract.uer_actuator_i_1'
uer_actuator_i_1.adams_id = 225
uer_actuator_i_1.location = Base.Vector (-3.9769915442e-11, 0.0, 0.1958077682)
uer_actuator_i_1.orientation = Base.Vector (0.0, 0.0, 0.0)
cm = MakeSceneNodeByType('Marker', '.turn.ger_upract.cm')
cm.marker_name = '.turn.ger_upract.cm'
cm.adams_id = 226
cm.location = Base.Vector (0.0, 0.0, 0.0)
cm.orientation = Base.Vector (0.0, 0.0, 0.0)
inertia_frame = MakeSceneNodeByType('Marker', '.turn.ger_upract.inertia_frame')
inertia_frame.marker_name = '.turn.ger_upract.inertia_frame'
inertia_frame.adams_id = 227
inertia_frame.location = Base.Vector (0.0, 0.0, 0.0)
inertia_frame.orientation = Base.Vector (0.0, 0.0, 0.0)
gralin_19 = MakeSceneNodeByType('Marker', '.turn.ger_upract.gralin_19')
gralin_19.marker_name = '.turn.ger_upract.gralin_19'
gralin_19.adams_id = 228
gralin_19.location = Base.Vector (-3.975687249e-11, 0.0, -0.1958077681)
gralin_19.orientation = Base.Vector (0.0, 0.0, 0.0)
jxr_joint_j_8 = MakeSceneNodeByType('Marker', '.turn.ger_upract.jxr_joint_j_8')
jxr_joint_j_8.marker_name = '.turn.ger_upract.jxr_joint_j_8'
jxr_joint_j_8.adams_id = 229
jxr_joint_j_8.location = Base.Vector (-3.9769952631e-11, 0.0, 0.1435923633)
jxr_joint_j_8.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_stopper_j_2 = MakeSceneNodeByType('Marker', '.turn.ger_upract.uer_stopper_j_2')
uer_stopper_j_2.marker_name = '.turn.ger_upract.uer_stopper_j_2'
uer_stopper_j_2.adams_id = 231
uer_stopper_j_2.location = Base.Vector (-3.9769915442e-11, 0.0, 0.1958077682)
uer_stopper_j_2.orientation = Base.Vector (0.0, 0.0, 0.0)
uer_actuator_j_2 = MakeSceneNodeByType('Marker', '.turn.ger_upract.uer_actuator_j_2')
uer_actuator_j_2.marker_name = '.turn.ger_upract.uer_actuator_j_2'
uer_actuator_j_2.adams_id = 232
uer_actuator_j_2.location = Base.Vector (-3.9768174973e-11, 0.0, 0.1435923633)
uer_actuator_j_2.orientation = Base.Vector (0.0, 0.0, 0.0)
ger_upract = Jusme.ActiveUSScene.getObject('.turn.ger_upract')
center_of_mass_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upract.cm')
ger_upract.center_of_mass_marker = center_of_mass_marker
inertia_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upract.inertia_frame')
ger_upract.inertia_marker = inertia_marker
ger_upract.part_name = '.turn.ger_upract'
ger_upract.mass = 0.45359237
ger_upract.ixx = 0.00029263965343
ger_upract.iyy = 0.00029263965343
ger_upract.izz = 0.00029263965343
ger_upract.ixy = 0.0
ger_upract.izx = 0.0
ger_upract.iyz = 0.0
gralin_upract = MakeSceneNodeByType('ShapeCylinder', '.turn.ger_upract.gralin_upract')
center_marker = Jusme.ActiveUSScene.getObject('.turn.ger_upract.gralin_19')
gralin_upract.center_marker = center_marker
gralin_upract.cylinder_name = '.turn.ger_upract.gralin_upract'
gralin_upract.adams_id = 28
gralin_upract.angle_extent = 360.0
gralin_upract.length = 0.3916155363
gralin_upract.radius = 0.01778
gralin_upract.side_count_for_body = 15
gralin_upract.segment_count_for_ends = 15


jolrev_lta_lc_joint = MakeSceneNodeByType('JointRevolute', '.turn.jolrev_lta_lc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.jxl_joint_i_11')
jolrev_lta_lc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.jxl_joint_j_11')
jolrev_lta_lc_joint.j_marker_name = j_marker_name
jolrev_lta_lc_joint.joint_name = '.turn.jolrev_lta_lc_joint'
jolrev_lta_lc_joint.adams_id = 2


jorrev_lta_lc_joint = MakeSceneNodeByType('JointRevolute', '.turn.jorrev_lta_lc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.jxr_joint_i_11')
jorrev_lta_lc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.jxr_joint_j_11')
jorrev_lta_lc_joint.j_marker_name = j_marker_name
jorrev_lta_lc_joint.joint_name = '.turn.jorrev_lta_lc_joint'
jorrev_lta_lc_joint.adams_id = 3


jolcyl_lc_uc_joint = MakeSceneNodeByType('JointCylinder', '.turn.jolcyl_lc_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.jxl_joint_i_12')
jolcyl_lc_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.jxl_joint_j_12')
jolcyl_lc_uc_joint.j_marker_name = j_marker_name
jolcyl_lc_uc_joint.joint_name = '.turn.jolcyl_lc_uc_joint'
jolcyl_lc_uc_joint.adams_id = 4


jorcyl_lc_uc_joint = MakeSceneNodeByType('JointCylinder', '.turn.jorcyl_lc_uc_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.jxr_joint_i_12')
jorcyl_lc_uc_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.jxr_joint_j_12')
jorcyl_lc_uc_joint.j_marker_name = j_marker_name
jorcyl_lc_uc_joint.joint_name = '.turn.jorcyl_lc_uc_joint'
jorcyl_lc_uc_joint.adams_id = 5


jolrev_ldb_udb_joint = MakeSceneNodeByType('JointFixed', '.turn.jolrev_ldb_udb_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.jxl_joint_i_14')
jolrev_ldb_udb_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.jxl_joint_j_14')
jolrev_ldb_udb_joint.j_marker_name = j_marker_name
jolrev_ldb_udb_joint.joint_name = '.turn.jolrev_ldb_udb_joint'
jolrev_ldb_udb_joint.adams_id = 6


jorrev_ldb_udb_joint = MakeSceneNodeByType('JointFixed', '.turn.jorrev_ldb_udb_joint')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.jxr_joint_i_14')
jorrev_ldb_udb_joint.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.jxr_joint_j_14')
jorrev_ldb_udb_joint.j_marker_name = j_marker_name
jorrev_ldb_udb_joint.joint_name = '.turn.jorrev_ldb_udb_joint'
jorrev_ldb_udb_joint.adams_id = 7


jolcyl_lta_connect = MakeSceneNodeByType('JointCylinder', '.turn.jolcyl_lta_connect')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.jxl_joint_i_1')
jolcyl_lta_connect.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_connector.jxl_joint_j_1')
jolcyl_lta_connect.j_marker_name = j_marker_name
jolcyl_lta_connect.joint_name = '.turn.jolcyl_lta_connect'
jolcyl_lta_connect.adams_id = 12


jorcyl_lta_connect = MakeSceneNodeByType('JointCylinder', '.turn.jorcyl_lta_connect')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.jxr_joint_i_1')
jorcyl_lta_connect.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_connector.jxr_joint_j_1')
jorcyl_lta_connect.j_marker_name = j_marker_name
jorcyl_lta_connect.joint_name = '.turn.jorcyl_lta_connect'
jorcyl_lta_connect.adams_id = 13


jolrev_uta_connect = MakeSceneNodeByType('JointRevolute', '.turn.jolrev_uta_connect')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.jxl_joint_i_2')
jolrev_uta_connect.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_connector.jxl_joint_j_2')
jolrev_uta_connect.j_marker_name = j_marker_name
jolrev_uta_connect.joint_name = '.turn.jolrev_uta_connect'
jolrev_uta_connect.adams_id = 14


jorrev_uta_connect = MakeSceneNodeByType('JointRevolute', '.turn.jorrev_uta_connect')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.jxr_joint_i_2')
jorrev_uta_connect.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_connector.jxr_joint_j_2')
jorrev_uta_connect.j_marker_name = j_marker_name
jorrev_uta_connect.joint_name = '.turn.jorrev_uta_connect'
jorrev_uta_connect.adams_id = 15


jolrev_uta_collar = MakeSceneNodeByType('JointRevolute', '.turn.jolrev_uta_collar')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.jxl_joint_i_3')
jolrev_uta_collar.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_j_3')
jolrev_uta_collar.j_marker_name = j_marker_name
jolrev_uta_collar.joint_name = '.turn.jolrev_uta_collar'
jolrev_uta_collar.adams_id = 16


jorrev_uta_collar = MakeSceneNodeByType('JointRevolute', '.turn.jorrev_uta_collar')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.jxr_joint_i_3')
jorrev_uta_collar.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_j_3')
jorrev_uta_collar.j_marker_name = j_marker_name
jorrev_uta_collar.joint_name = '.turn.jorrev_uta_collar'
jorrev_uta_collar.adams_id = 17


jolrev_collar_uc = MakeSceneNodeByType('JointFixed', '.turn.jolrev_collar_uc')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_i_4')
jolrev_collar_uc.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.jxl_joint_j_4')
jolrev_collar_uc.j_marker_name = j_marker_name
jolrev_collar_uc.joint_name = '.turn.jolrev_collar_uc'
jolrev_collar_uc.adams_id = 18


jorrev_collar_uc = MakeSceneNodeByType('JointFixed', '.turn.jorrev_collar_uc')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_i_4')
jorrev_collar_uc.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.jxr_joint_j_4')
jorrev_collar_uc.j_marker_name = j_marker_name
jorrev_collar_uc.joint_name = '.turn.jorrev_collar_uc'
jorrev_collar_uc.adams_id = 19


jolhoo_udb_spndl = MakeSceneNodeByType('JointHooke', '.turn.jolhoo_udb_spndl')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.jxl_joint_i_5')
jolhoo_udb_spndl.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.jxl_joint_j_5')
jolhoo_udb_spndl.j_marker_name = j_marker_name
jolhoo_udb_spndl.joint_name = '.turn.jolhoo_udb_spndl'
jolhoo_udb_spndl.adams_id = 20


jorhoo_udb_spndl = MakeSceneNodeByType('JointHooke', '.turn.jorhoo_udb_spndl')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.jxr_joint_i_5')
jorhoo_udb_spndl.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.jxr_joint_j_5')
jorhoo_udb_spndl.j_marker_name = j_marker_name
jorhoo_udb_spndl.joint_name = '.turn.jorhoo_udb_spndl'
jorhoo_udb_spndl.adams_id = 21


jolsph_uc_lwract = MakeSceneNodeByType('JointSpherical', '.turn.jolsph_uc_lwract')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.jxl_joint_i_7')
jolsph_uc_lwract.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.jxl_joint_j_7')
jolsph_uc_lwract.j_marker_name = j_marker_name
jolsph_uc_lwract.joint_name = '.turn.jolsph_uc_lwract'
jolsph_uc_lwract.adams_id = 24


jorsph_uc_lwract = MakeSceneNodeByType('JointSpherical', '.turn.jorsph_uc_lwract')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.jxr_joint_i_7')
jorsph_uc_lwract.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.jxr_joint_j_7')
jorsph_uc_lwract.j_marker_name = j_marker_name
jorsph_uc_lwract.joint_name = '.turn.jorsph_uc_lwract'
jorsph_uc_lwract.adams_id = 25


joltra_lwract_upract = MakeSceneNodeByType('JointTranslational', '.turn.joltra_lwract_upract')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.jxl_joint_i_8')
joltra_lwract_upract.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_upract.jxl_joint_j_8')
joltra_lwract_upract.j_marker_name = j_marker_name
joltra_lwract_upract.joint_name = '.turn.joltra_lwract_upract'
joltra_lwract_upract.adams_id = 26


jortra_lwract_upract = MakeSceneNodeByType('JointTranslational', '.turn.jortra_lwract_upract')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.jxr_joint_i_8')
jortra_lwract_upract.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_upract.jxr_joint_j_8')
jortra_lwract_upract.j_marker_name = j_marker_name
jortra_lwract_upract.joint_name = '.turn.jortra_lwract_upract'
jortra_lwract_upract.adams_id = 27


jolrev_ldb_collar = MakeSceneNodeByType('JointRevolute', '.turn.jolrev_ldb_collar')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.jxl_joint_i_10')
jolrev_ldb_collar.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_j_10')
jolrev_ldb_collar.j_marker_name = j_marker_name
jolrev_ldb_collar.joint_name = '.turn.jolrev_ldb_collar'
jolrev_ldb_collar.adams_id = 30


jorrev_ldb_collar = MakeSceneNodeByType('JointRevolute', '.turn.jorrev_ldb_collar')
i_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.jxr_joint_i_10')
jorrev_ldb_collar.i_marker_name = i_marker_name
j_marker_name = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_j_10')
jorrev_ldb_collar.j_marker_name = j_marker_name
jorrev_ldb_collar.joint_name = '.turn.jorrev_ldb_collar'
jorrev_ldb_collar.adams_id = 31


cfl_spin_axis = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_spin_axis')
cfl_spin_axis.marker_name = '.turn.ground.cfl_spin_axis'
_turn_ground_cfl_spin_axis_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_spin_axis_1')
cfl_spin_axis.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_spin_axis_1))
_turn_ground_cfl_spin_axis_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_spin_axis_1')
cfl_spin_axis.orientation = (VecUtils.ORI_RELATIVE_TO([180.0, 180.0, 180.0], _turn_ground_cfl_spin_axis_1))


cfr_spin_axis = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_spin_axis')
cfr_spin_axis.marker_name = '.turn.ground.cfr_spin_axis'
_turn_ground_cfr_spin_axis_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_spin_axis_1')
cfr_spin_axis.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_spin_axis_1))
_turn_ground_cfr_spin_axis_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_spin_axis_1')
cfr_spin_axis.orientation = (VecUtils.ORI_RELATIVE_TO([-180.0, -180.0, -180.0], _turn_ground_cfr_spin_axis_1))


cfl_axial_reference = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_axial_reference')
cfl_axial_reference.marker_name = '.turn.ground.cfl_axial_reference'
_turn_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lc_bot')
cfl_axial_reference.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_lc_bot))
_turn_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lc_bot').location
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top').location
cfl_axial_reference.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_lc_bot, _turn_ground_hpl_uc_top, "Z"))


cfr_axial_reference = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_axial_reference')
cfr_axial_reference.marker_name = '.turn.ground.cfr_axial_reference'
_turn_ground_hpr_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lc_bot')
cfr_axial_reference.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_lc_bot))
_turn_ground_hpr_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lc_bot').location
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top').location
cfr_axial_reference.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_lc_bot, _turn_ground_hpr_uc_top, "Z"))


cfl_uc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_bot')
cfl_uc_bot.marker_name = '.turn.ground.cfl_uc_bot'
_turn_ground_cfl_axial_reference = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_axial_reference')
cfl_uc_bot.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 537.972], _turn_ground_cfl_axial_reference))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfl_uc_bot.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfr_uc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_bot')
cfr_uc_bot.marker_name = '.turn.ground.cfr_uc_bot'
_turn_ground_cfr_axial_reference = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_axial_reference')
cfr_uc_bot.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 537.972], _turn_ground_cfr_axial_reference))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfr_uc_bot.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_top')
cfl_uc_top.marker_name = '.turn.ground.cfl_uc_top'
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top')
cfl_uc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_uc_top))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfl_uc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_top')
cfr_uc_top.marker_name = '.turn.ground.cfr_uc_top'
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top')
cfr_uc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_uc_top))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfr_uc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfl_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lc_top')
cfl_lc_top.marker_name = '.turn.ground.cfl_lc_top'
_turn_ground_cfl_axial_reference = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_axial_reference')
cfl_lc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 966.724], _turn_ground_cfl_axial_reference))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfl_lc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfr_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lc_top')
cfr_lc_top.marker_name = '.turn.ground.cfr_lc_top'
_turn_ground_cfr_axial_reference = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_axial_reference')
cfr_lc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 966.724], _turn_ground_cfr_axial_reference))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfr_lc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfl_uta_uc_atch = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uta_uc_atch')
cfl_uta_uc_atch.marker_name = '.turn.ground.cfl_uta_uc_atch'
_turn_ground_cfl_uc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_bot')
cfl_uta_uc_atch.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_uc_bot))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfl_uta_uc_atch.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfr_uta_uc_atch = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uta_uc_atch')
cfr_uta_uc_atch.marker_name = '.turn.ground.cfr_uta_uc_atch'
_turn_ground_cfr_uc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_bot')
cfr_uta_uc_atch.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_uc_bot))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfr_uta_uc_atch.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfl_lta_lc_atch = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lta_lc_atch')
cfl_lta_lc_atch.marker_name = '.turn.ground.cfl_lta_lc_atch'
_turn_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lc_bot')
cfl_lta_lc_atch.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_lc_bot))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfl_lta_lc_atch.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfr_lta_lc_atch = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lta_lc_atch')
cfr_lta_lc_atch.marker_name = '.turn.ground.cfr_lta_lc_atch'
_turn_ground_hpr_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lc_bot')
cfr_lta_lc_atch.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_lc_bot))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfr_lta_lc_atch.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfl_collar_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_collar_top')
cfl_collar_top.marker_name = '.turn.ground.cfl_collar_top'
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top').location
_turn_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lc_bot').location
cfl_collar_top.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpl_uc_top, _turn_ground_hpl_lc_bot, 0.59 * VecUtils.DM(_turn_ground_hpl_uc_top, _turn_ground_hpl_lc_bot)))
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top').location
_turn_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lc_bot').location
cfl_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_uc_top, _turn_ground_hpl_lc_bot, "Z"))


cfr_collar_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_collar_top')
cfr_collar_top.marker_name = '.turn.ground.cfr_collar_top'
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top').location
_turn_ground_hpr_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lc_bot').location
cfr_collar_top.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpr_uc_top, _turn_ground_hpr_lc_bot, 0.59 * VecUtils.DM(_turn_ground_hpr_uc_top, _turn_ground_hpr_lc_bot)))
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top').location
_turn_ground_hpr_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lc_bot').location
cfr_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_uc_top, _turn_ground_hpr_lc_bot, "Z"))


cfl_collar_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_collar_bot')
cfl_collar_bot.marker_name = '.turn.ground.cfl_collar_bot'
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top').location
_turn_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lc_bot').location
cfl_collar_bot.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpl_uc_top, _turn_ground_hpl_lc_bot, 0.7 * VecUtils.DM(_turn_ground_hpl_uc_top, _turn_ground_hpl_lc_bot)))
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top').location
_turn_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lc_bot').location
cfl_collar_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_uc_top, _turn_ground_hpl_lc_bot, "Z"))


cfr_collar_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_collar_bot')
cfr_collar_bot.marker_name = '.turn.ground.cfr_collar_bot'
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top').location
_turn_ground_hpr_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lc_bot').location
cfr_collar_bot.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpr_uc_top, _turn_ground_hpr_lc_bot, 0.7 * VecUtils.DM(_turn_ground_hpr_uc_top, _turn_ground_hpr_lc_bot)))
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top').location
_turn_ground_hpr_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lc_bot').location
cfr_collar_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_uc_top, _turn_ground_hpr_lc_bot, "Z"))


cfl_plane_ref_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_plane_ref_2')
cfl_plane_ref_2.marker_name = '.turn.ground.cfl_plane_ref_2'
_turn_ground_cfl_plane_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_plane_ref')
cfl_plane_ref_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_plane_ref))
_turn_ground_cfl_plane_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_plane_ref')
cfl_plane_ref_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, -90.0, 0.0], _turn_ground_cfl_plane_ref))


cfr_plane_ref_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_plane_ref_2')
cfr_plane_ref_2.marker_name = '.turn.ground.cfr_plane_ref_2'
_turn_ground_cfr_plane_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_plane_ref')
cfr_plane_ref_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_plane_ref))
_turn_ground_cfr_plane_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_plane_ref')
cfr_plane_ref_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _turn_ground_cfr_plane_ref))


cfl_lwract_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lwract_top')
cfl_lwract_top.marker_name = '.turn.ground.cfl_lwract_top'
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1').location
_turn_ground_hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_upract_sf_atch_1').location
cfl_lwract_top.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpl_lwract_uc_atch_1, _turn_ground_hpl_upract_sf_atch_1, 0.92 * VecUtils.DM(_turn_ground_hpl_lwract_uc_atch_1, _turn_ground_hpl_upract_sf_atch_1)))
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1').location
_turn_ground_hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_upract_sf_atch_1').location
cfl_lwract_top.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_lwract_uc_atch_1, _turn_ground_hpl_upract_sf_atch_1, "Z"))


cfr_lwract_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lwract_top')
cfr_lwract_top.marker_name = '.turn.ground.cfr_lwract_top'
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1').location
_turn_ground_hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_upract_sf_atch_1').location
cfr_lwract_top.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpr_lwract_uc_atch_1, _turn_ground_hpr_upract_sf_atch_1, 0.92 * VecUtils.DM(_turn_ground_hpr_lwract_uc_atch_1, _turn_ground_hpr_upract_sf_atch_1)))
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1').location
_turn_ground_hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_upract_sf_atch_1').location
cfr_lwract_top.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_lwract_uc_atch_1, _turn_ground_hpr_upract_sf_atch_1, "Z"))


cfl_upract_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_upract_bot')
cfl_upract_bot.marker_name = '.turn.ground.cfl_upract_bot'
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1').location
_turn_ground_hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_upract_sf_atch_1').location
cfl_upract_bot.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpl_lwract_uc_atch_1, _turn_ground_hpl_upract_sf_atch_1, 0.4 * VecUtils.DM(_turn_ground_hpl_lwract_uc_atch_1, _turn_ground_hpl_upract_sf_atch_1)))
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1').location
_turn_ground_hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_upract_sf_atch_1').location
cfl_upract_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_lwract_uc_atch_1, _turn_ground_hpl_upract_sf_atch_1, "Z"))


cfr_upract_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_upract_bot')
cfr_upract_bot.marker_name = '.turn.ground.cfr_upract_bot'
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1').location
_turn_ground_hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_upract_sf_atch_1').location
cfr_upract_bot.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpr_lwract_uc_atch_1, _turn_ground_hpr_upract_sf_atch_1, 0.4 * VecUtils.DM(_turn_ground_hpr_lwract_uc_atch_1, _turn_ground_hpr_upract_sf_atch_1)))
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1').location
_turn_ground_hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_upract_sf_atch_1').location
cfr_upract_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_lwract_uc_atch_1, _turn_ground_hpr_upract_sf_atch_1, "Z"))


cfl_spin_axis_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_spin_axis_1')
cfl_spin_axis_1.marker_name = '.turn.ground.cfl_spin_axis_1'
_turn_ground_hpl_wheel_center = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_wheel_center')
cfl_spin_axis_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_wheel_center))
_turn_ground_hpl_wheel_center = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_wheel_center').location
_turn_ground_hpl_ob_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ob_axle').location
cfl_spin_axis_1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_wheel_center, _turn_ground_hpl_ob_axle, "Z"))


cfr_spin_axis_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_spin_axis_1')
cfr_spin_axis_1.marker_name = '.turn.ground.cfr_spin_axis_1'
_turn_ground_hpr_wheel_center = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_wheel_center')
cfr_spin_axis_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_wheel_center))
_turn_ground_hpr_wheel_center = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_wheel_center').location
_turn_ground_hpr_ob_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ob_axle').location
cfr_spin_axis_1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_wheel_center, _turn_ground_hpr_ob_axle, "Z"))


cfl_ldb_geompt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_ldb_geompt_1')
cfl_ldb_geompt_1.marker_name = '.turn.ground.cfl_ldb_geompt_1'
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1').location
_turn_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_collar_atch_1').location
cfl_ldb_geompt_1.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpl_ldb_udb_atch_1, _turn_ground_hpl_ldb_collar_atch_1, 0.62 * VecUtils.DM(_turn_ground_hpl_ldb_udb_atch_1, _turn_ground_hpl_ldb_collar_atch_1)))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfl_ldb_geompt_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfr_ldb_geompt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_ldb_geompt_1')
cfr_ldb_geompt_1.marker_name = '.turn.ground.cfr_ldb_geompt_1'
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1').location
_turn_ground_hpr_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_collar_atch_1').location
cfr_ldb_geompt_1.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpr_ldb_udb_atch_1, _turn_ground_hpr_ldb_collar_atch_1, 0.62 * VecUtils.DM(_turn_ground_hpr_ldb_udb_atch_1, _turn_ground_hpr_ldb_collar_atch_1)))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfr_ldb_geompt_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfl_ldb_geompt_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_ldb_geompt_2')
cfl_ldb_geompt_2.marker_name = '.turn.ground.cfl_ldb_geompt_2'
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1').location
_turn_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_collar_atch_1').location
cfl_ldb_geompt_2.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpl_ldb_udb_atch_1, _turn_ground_hpl_ldb_collar_atch_1, 0.74 * VecUtils.DM(_turn_ground_hpl_ldb_udb_atch_1, _turn_ground_hpl_ldb_collar_atch_1)))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfl_ldb_geompt_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfr_ldb_geompt_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_ldb_geompt_2')
cfr_ldb_geompt_2.marker_name = '.turn.ground.cfr_ldb_geompt_2'
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1').location
_turn_ground_hpr_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_collar_atch_1').location
cfr_ldb_geompt_2.location = (VecUtils.LOC_ALONG_LINE(_turn_ground_hpr_ldb_udb_atch_1, _turn_ground_hpr_ldb_collar_atch_1, 0.74 * VecUtils.DM(_turn_ground_hpr_ldb_udb_atch_1, _turn_ground_hpr_ldb_collar_atch_1)))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfr_ldb_geompt_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfl_aero_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_aero_ref')
cfl_aero_ref.marker_name = '.turn.ground.cfl_aero_ref'
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top')
cfl_aero_ref.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_uc_top))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfl_aero_ref.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


cfr_aero_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_aero_ref')
cfr_aero_ref.marker_name = '.turn.ground.cfr_aero_ref'
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top')
cfr_aero_ref.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_uc_top))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
cfr_aero_ref.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


uel_gearaero_origin_1 = Jusme.ActiveUSScene.getObject('.turn.ground.uel_gearaero_origin_1')
uel_gearaero_origin_1.marker_name = '.turn.ground.uel_gearaero_origin_1'
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
uel_gearaero_origin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
uel_gearaero_origin_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


uel_gearaero_rm_1 = Jusme.ActiveUSScene.getObject('.turn.ground.uel_gearaero_rm_1')
uel_gearaero_rm_1.marker_name = '.turn.ground.uel_gearaero_rm_1'
_turn_ground_cfl_aero_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_aero_ref')
uel_gearaero_rm_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_aero_ref))
_turn_ground_cfl_aero_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_aero_ref')
uel_gearaero_rm_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_aero_ref))


uer_gearaero_origin_1 = Jusme.ActiveUSScene.getObject('.turn.ground.uer_gearaero_origin_1')
uer_gearaero_origin_1.marker_name = '.turn.ground.uer_gearaero_origin_1'
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
uer_gearaero_origin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
uer_gearaero_origin_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))


uer_gearaero_rm_1 = Jusme.ActiveUSScene.getObject('.turn.ground.uer_gearaero_rm_1')
uer_gearaero_rm_1.marker_name = '.turn.ground.uer_gearaero_rm_1'
_turn_ground_cfr_aero_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_aero_ref')
uer_gearaero_rm_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_aero_ref))
_turn_ground_cfr_aero_ref = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_aero_ref')
uer_gearaero_rm_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_aero_ref))


aluminum = Jusme.ActiveUSScene.getObject('.turn.aluminum')
aluminum.material_name = '.turn.aluminum'


steel = Jusme.ActiveUSScene.getObject('.turn.steel')
steel.material_name = '.turn.steel'


steel_2 = Jusme.ActiveUSScene.getObject('.turn.steel_2')
steel_2.material_name = '.turn.steel_2'


aluminum_2 = Jusme.ActiveUSScene.getObject('.turn.aluminum_2')
aluminum_2.material_name = '.turn.aluminum_2'


uel_gearaero_i_1 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.uel_gearaero_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
uel_gearaero_i_1.relative_to = relative_to
uel_gearaero_i_1.marker_name = '.turn.gel_upper_cylinder.uel_gearaero_i_1'
_turn_ground_cfl_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lc_top')
uel_gearaero_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_gearaero_i_1.location, uel_gearaero_i_1.orientation)
uel_gearaero_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_upper_cylinder.inertia_frame'
_turn_gel_upper_cylinder_cm = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_cylinder_cm))
_turn_gel_upper_cylinder = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_12 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.gralin_12')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
gralin_12.relative_to = relative_to
gralin_12.marker_name = '.turn.gel_upper_cylinder.gralin_12'
_turn_ground_cfl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_top')
gralin_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_uc_top))
_turn_ground_cfl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_top').location
_turn_ground_cfl_uc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_bot').location
gralin_12.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_cfl_uc_top, _turn_ground_cfl_uc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_12.location, gralin_12.orientation)
gralin_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_16 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.gralin_16')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
gralin_16.relative_to = relative_to
gralin_16.marker_name = '.turn.gel_upper_cylinder.gralin_16'
_turn_ground_hpl_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ib_uc_sf_atch')
gralin_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_ib_uc_sf_atch))
_turn_ground_hpl_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ib_uc_sf_atch').location
_turn_ground_hpl_uc_geompt = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_geompt').location
gralin_16.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_ib_uc_sf_atch, _turn_ground_hpl_uc_geompt, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_16.location, gralin_16.orientation)
gralin_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_20 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.gralin_20')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
gralin_20.relative_to = relative_to
gralin_20.marker_name = '.turn.gel_upper_cylinder.gralin_20'
_turn_ground_hpl_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ib_uc_sf_atch')
gralin_20.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_ib_uc_sf_atch))
_turn_ground_hpl_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ib_uc_sf_atch').location
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top').location
gralin_20.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_ib_uc_sf_atch, _turn_ground_hpl_uc_top, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_20.location, gralin_20.orientation)
gralin_20.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_20.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uel_spring_j_1 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.uel_spring_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
uel_spring_j_1.relative_to = relative_to
uel_spring_j_1.marker_name = '.turn.gel_upper_cylinder.uel_spring_j_1'
_turn_ground_cfl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_top')
uel_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_spring_j_1.location, uel_spring_j_1.orientation)
uel_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uel_damper_j_1 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.uel_damper_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
uel_damper_j_1.relative_to = relative_to
uel_damper_j_1.marker_name = '.turn.gel_upper_cylinder.uel_damper_j_1'
_turn_ground_cfl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_top')
uel_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_damper_j_1.location, uel_damper_j_1.orientation)
uel_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uel_stopper_j_1 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.uel_stopper_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
uel_stopper_j_1.relative_to = relative_to
uel_stopper_j_1.marker_name = '.turn.gel_upper_cylinder.uel_stopper_j_1'
_turn_ground_cfl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_top')
uel_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_j_1.location, uel_stopper_j_1.orientation)
uel_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


jxl_joint_i_7 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.jxl_joint_i_7')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
jxl_joint_i_7.relative_to = relative_to
jxl_joint_i_7.marker_name = '.turn.gel_upper_cylinder.jxl_joint_i_7'
_turn_gel_lwract_jxl_joint_j_7 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.jxl_joint_j_7')
jxl_joint_i_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lwract_jxl_joint_j_7))
_turn_gel_lwract_jxl_joint_j_7 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.jxl_joint_j_7')
jxl_joint_i_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lwract_jxl_joint_j_7))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_7.location, jxl_joint_i_7.orientation)
jxl_joint_i_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uel_actuator_j_3 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.uel_actuator_j_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
uel_actuator_j_3.relative_to = relative_to
uel_actuator_j_3.marker_name = '.turn.gel_upper_cylinder.uel_actuator_j_3'
_turn_ground_cfl_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_sf_atch')
uel_actuator_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_uc_sf_atch))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_j_3.location, uel_actuator_j_3.orientation)
uel_actuator_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_267 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.MARKER_267')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder')
MARKER_267.relative_to = relative_to
MARKER_267.marker_name = '.turn.gel_upper_cylinder.MARKER_267'
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top')
MARKER_267.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_267.location, MARKER_267.orientation)
MARKER_267.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_upper_cylinder = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.gralin_upper_cylinder')
gralin_upper_cylinder.cylinder_name = '.turn.gel_upper_cylinder.gralin_upper_cylinder'
_turn_ground_cfl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_top').location
_turn_ground_cfl_uc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_uc_bot').location
gralin_upper_cylinder.length = (VecUtils.DM(_turn_ground_cfl_uc_top, _turn_ground_cfl_uc_bot))


gralin_geom = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.gralin_geom')
gralin_geom.cylinder_name = '.turn.gel_upper_cylinder.gralin_geom'
_turn_ground_hpl_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ib_uc_sf_atch').location
_turn_ground_hpl_uc_geompt = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_geompt').location
gralin_geom.length = (VecUtils.DM(_turn_ground_hpl_ib_uc_sf_atch, _turn_ground_hpl_uc_geompt))


gralin_geom3 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.gralin_geom3')
gralin_geom3.cylinder_name = '.turn.gel_upper_cylinder.gralin_geom3'
_turn_ground_hpl_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ib_uc_sf_atch').location
_turn_ground_hpl_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uc_top').location
gralin_geom3.length = (VecUtils.DM(_turn_ground_hpl_ib_uc_sf_atch, _turn_ground_hpl_uc_top))


uer_gearaero_i_1 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.uer_gearaero_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
uer_gearaero_i_1.relative_to = relative_to
uer_gearaero_i_1.marker_name = '.turn.ger_upper_cylinder.uer_gearaero_i_1'
_turn_ground_cfr_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lc_top')
uer_gearaero_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_gearaero_i_1.location, uer_gearaero_i_1.orientation)
uer_gearaero_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_upper_cylinder.inertia_frame'
_turn_ger_upper_cylinder_cm = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_cylinder_cm))
_turn_ger_upper_cylinder = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_13 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.gralin_13')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
gralin_13.relative_to = relative_to
gralin_13.marker_name = '.turn.ger_upper_cylinder.gralin_13'
_turn_ground_cfr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_top')
gralin_13.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_uc_top))
_turn_ground_cfr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_top').location
_turn_ground_cfr_uc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_bot').location
gralin_13.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_cfr_uc_top, _turn_ground_cfr_uc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_13.location, gralin_13.orientation)
gralin_13.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_13.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_17 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.gralin_17')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
gralin_17.relative_to = relative_to
gralin_17.marker_name = '.turn.ger_upper_cylinder.gralin_17'
_turn_ground_hpr_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ib_uc_sf_atch')
gralin_17.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_ib_uc_sf_atch))
_turn_ground_hpr_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ib_uc_sf_atch').location
_turn_ground_hpr_uc_geompt = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_geompt').location
gralin_17.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_ib_uc_sf_atch, _turn_ground_hpr_uc_geompt, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_17.location, gralin_17.orientation)
gralin_17.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_17.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_21 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.gralin_21')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
gralin_21.relative_to = relative_to
gralin_21.marker_name = '.turn.ger_upper_cylinder.gralin_21'
_turn_ground_hpr_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ib_uc_sf_atch')
gralin_21.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_ib_uc_sf_atch))
_turn_ground_hpr_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ib_uc_sf_atch').location
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top').location
gralin_21.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_ib_uc_sf_atch, _turn_ground_hpr_uc_top, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_21.location, gralin_21.orientation)
gralin_21.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_21.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uer_spring_j_1 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.uer_spring_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
uer_spring_j_1.relative_to = relative_to
uer_spring_j_1.marker_name = '.turn.ger_upper_cylinder.uer_spring_j_1'
_turn_ground_cfr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_top')
uer_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_spring_j_1.location, uer_spring_j_1.orientation)
uer_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uer_damper_j_1 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.uer_damper_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
uer_damper_j_1.relative_to = relative_to
uer_damper_j_1.marker_name = '.turn.ger_upper_cylinder.uer_damper_j_1'
_turn_ground_cfr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_top')
uer_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_damper_j_1.location, uer_damper_j_1.orientation)
uer_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uer_stopper_j_1 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.uer_stopper_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
uer_stopper_j_1.relative_to = relative_to
uer_stopper_j_1.marker_name = '.turn.ger_upper_cylinder.uer_stopper_j_1'
_turn_ground_cfr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_top')
uer_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_stopper_j_1.location, uer_stopper_j_1.orientation)
uer_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


jxr_joint_i_7 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.jxr_joint_i_7')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
jxr_joint_i_7.relative_to = relative_to
jxr_joint_i_7.marker_name = '.turn.ger_upper_cylinder.jxr_joint_i_7'
_turn_ger_lwract_jxr_joint_j_7 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.jxr_joint_j_7')
jxr_joint_i_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lwract_jxr_joint_j_7))
_turn_ger_lwract_jxr_joint_j_7 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.jxr_joint_j_7')
jxr_joint_i_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lwract_jxr_joint_j_7))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_7.location, jxr_joint_i_7.orientation)
jxr_joint_i_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uer_actuator_j_3 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.uer_actuator_j_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
uer_actuator_j_3.relative_to = relative_to
uer_actuator_j_3.marker_name = '.turn.ger_upper_cylinder.uer_actuator_j_3'
_turn_ground_cfr_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_sf_atch')
uer_actuator_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_uc_sf_atch))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_j_3.location, uer_actuator_j_3.orientation)
uer_actuator_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


MARKER_269 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.MARKER_269')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder')
MARKER_269.relative_to = relative_to
MARKER_269.marker_name = '.turn.ger_upper_cylinder.MARKER_269'
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top')
MARKER_269.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_uc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_269.location, MARKER_269.orientation)
MARKER_269.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_upper_cylinder = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.gralin_upper_cylinder')
gralin_upper_cylinder.cylinder_name = '.turn.ger_upper_cylinder.gralin_upper_cylinder'
_turn_ground_cfr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_top').location
_turn_ground_cfr_uc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_uc_bot').location
gralin_upper_cylinder.length = (VecUtils.DM(_turn_ground_cfr_uc_top, _turn_ground_cfr_uc_bot))


gralin_geom = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.gralin_geom')
gralin_geom.cylinder_name = '.turn.ger_upper_cylinder.gralin_geom'
_turn_ground_hpr_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ib_uc_sf_atch').location
_turn_ground_hpr_uc_geompt = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_geompt').location
gralin_geom.length = (VecUtils.DM(_turn_ground_hpr_ib_uc_sf_atch, _turn_ground_hpr_uc_geompt))


gralin_geom3 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.gralin_geom3')
gralin_geom3.cylinder_name = '.turn.ger_upper_cylinder.gralin_geom3'
_turn_ground_hpr_ib_uc_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ib_uc_sf_atch').location
_turn_ground_hpr_uc_top = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uc_top').location
gralin_geom3.length = (VecUtils.DM(_turn_ground_hpr_ib_uc_sf_atch, _turn_ground_hpr_uc_top))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_lower_cylinder.inertia_frame'
_turn_gel_lower_cylinder_cm = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lower_cylinder_cm))
_turn_gel_lower_cylinder = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lower_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_14 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.gralin_14')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
gralin_14.relative_to = relative_to
gralin_14.marker_name = '.turn.gel_lower_cylinder.gralin_14'
_turn_ground_cfl_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lc_top')
gralin_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_lc_top))
_turn_ground_cfl_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lc_top').location
_turn_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lc_bot').location
gralin_14.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_cfl_lc_top, _turn_ground_hpl_lc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_14.location, gralin_14.orientation)
gralin_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_22 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.gralin_22')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
gralin_22.relative_to = relative_to
gralin_22.marker_name = '.turn.gel_lower_cylinder.gralin_22'
_turn_ground_hpl_ib_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ib_axle')
gralin_22.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_ib_axle))
_turn_ground_hpl_ib_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ib_axle').location
_turn_ground_hpl_ob_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ob_axle').location
gralin_22.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_ib_axle, _turn_ground_hpl_ob_axle, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_22.location, gralin_22.orientation)
gralin_22.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_22.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_11 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.jxl_joint_j_11')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
jxl_joint_j_11.relative_to = relative_to
jxl_joint_j_11.marker_name = '.turn.gel_lower_cylinder.jxl_joint_j_11'
_turn_ground_hpl_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_lc_atch_1')
jxl_joint_j_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_lta_lc_atch_1))
_turn_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_connect_atch_1').location
_turn_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_1').location
jxl_joint_j_11.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_lta_connect_atch_1, _turn_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_11.location, jxl_joint_j_11.orientation)
jxl_joint_j_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_12 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.jxl_joint_i_12')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
jxl_joint_i_12.relative_to = relative_to
jxl_joint_i_12.marker_name = '.turn.gel_lower_cylinder.jxl_joint_i_12'
_turn_gel_upper_cylinder_jxl_joint_j_12 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.jxl_joint_j_12')
jxl_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_cylinder_jxl_joint_j_12))
_turn_gel_upper_cylinder_jxl_joint_j_12 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.jxl_joint_j_12')
jxl_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_cylinder_jxl_joint_j_12))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_12.location, jxl_joint_i_12.orientation)
jxl_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


coomarker_1 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.coomarker_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
coomarker_1.relative_to = relative_to
coomarker_1.marker_name = '.turn.gel_lower_cylinder.coomarker_1'
_turn_ground_cfl_spin_axis = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_spin_axis')
coomarker_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_spin_axis))
_turn_ground_cfl_spin_axis = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_spin_axis')
coomarker_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_spin_axis))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_1.location, coomarker_1.orientation)
coomarker_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
coomarker_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uel_spring_i_1 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.uel_spring_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
uel_spring_i_1.relative_to = relative_to
uel_spring_i_1.marker_name = '.turn.gel_lower_cylinder.uel_spring_i_1'
_turn_ground_cfl_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lc_top')
uel_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_spring_i_1.location, uel_spring_i_1.orientation)
uel_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uel_damper_i_1 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.uel_damper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
uel_damper_i_1.relative_to = relative_to
uel_damper_i_1.marker_name = '.turn.gel_lower_cylinder.uel_damper_i_1'
_turn_ground_cfl_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lc_top')
uel_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_damper_i_1.location, uel_damper_i_1.orientation)
uel_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uel_stopper_i_1 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.uel_stopper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder')
uel_stopper_i_1.relative_to = relative_to
uel_stopper_i_1.marker_name = '.turn.gel_lower_cylinder.uel_stopper_i_1'
_turn_ground_cfl_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lc_top')
uel_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_i_1.location, uel_stopper_i_1.orientation)
uel_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_lower_cylinder = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.gralin_lower_cylinder')
gralin_lower_cylinder.cylinder_name = '.turn.gel_lower_cylinder.gralin_lower_cylinder'
_turn_ground_cfl_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lc_top').location
_turn_ground_hpl_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lc_bot').location
gralin_lower_cylinder.length = (VecUtils.DM(_turn_ground_cfl_lc_top, _turn_ground_hpl_lc_bot))


gralin_geom = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.gralin_geom')
gralin_geom.cylinder_name = '.turn.gel_lower_cylinder.gralin_geom'
_turn_ground_hpl_ib_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ib_axle').location
_turn_ground_hpl_ob_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ob_axle').location
gralin_geom.length = (VecUtils.DM(_turn_ground_hpl_ib_axle, _turn_ground_hpl_ob_axle))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_lower_cylinder.inertia_frame'
_turn_ger_lower_cylinder_cm = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lower_cylinder_cm))
_turn_ger_lower_cylinder = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lower_cylinder))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_15 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.gralin_15')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
gralin_15.relative_to = relative_to
gralin_15.marker_name = '.turn.ger_lower_cylinder.gralin_15'
_turn_ground_cfr_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lc_top')
gralin_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_lc_top))
_turn_ground_cfr_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lc_top').location
_turn_ground_hpr_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lc_bot').location
gralin_15.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_cfr_lc_top, _turn_ground_hpr_lc_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_15.location, gralin_15.orientation)
gralin_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_23 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.gralin_23')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
gralin_23.relative_to = relative_to
gralin_23.marker_name = '.turn.ger_lower_cylinder.gralin_23'
_turn_ground_hpr_ib_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ib_axle')
gralin_23.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_ib_axle))
_turn_ground_hpr_ib_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ib_axle').location
_turn_ground_hpr_ob_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ob_axle').location
gralin_23.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_ib_axle, _turn_ground_hpr_ob_axle, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_23.location, gralin_23.orientation)
gralin_23.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_23.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_j_11 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.jxr_joint_j_11')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
jxr_joint_j_11.relative_to = relative_to
jxr_joint_j_11.marker_name = '.turn.ger_lower_cylinder.jxr_joint_j_11'
_turn_ground_hpr_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_lc_atch_1')
jxr_joint_j_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_lta_lc_atch_1))
_turn_ground_hpr_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_connect_atch_1').location
_turn_ground_hpr_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_1').location
jxr_joint_j_11.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_lta_connect_atch_1, _turn_ground_hpr_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_11.location, jxr_joint_j_11.orientation)
jxr_joint_j_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_j_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_12 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.jxr_joint_i_12')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
jxr_joint_i_12.relative_to = relative_to
jxr_joint_i_12.marker_name = '.turn.ger_lower_cylinder.jxr_joint_i_12'
_turn_ger_upper_cylinder_jxr_joint_j_12 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.jxr_joint_j_12')
jxr_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_cylinder_jxr_joint_j_12))
_turn_ger_upper_cylinder_jxr_joint_j_12 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.jxr_joint_j_12')
jxr_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_cylinder_jxr_joint_j_12))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_12.location, jxr_joint_i_12.orientation)
jxr_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


coomarker_2 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.coomarker_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
coomarker_2.relative_to = relative_to
coomarker_2.marker_name = '.turn.ger_lower_cylinder.coomarker_2'
_turn_ground_cfr_spin_axis = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_spin_axis')
coomarker_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_spin_axis))
_turn_ground_cfr_spin_axis = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_spin_axis')
coomarker_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_spin_axis))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_2.location, coomarker_2.orientation)
coomarker_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
coomarker_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uer_spring_i_1 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.uer_spring_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
uer_spring_i_1.relative_to = relative_to
uer_spring_i_1.marker_name = '.turn.ger_lower_cylinder.uer_spring_i_1'
_turn_ground_cfr_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lc_top')
uer_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_spring_i_1.location, uer_spring_i_1.orientation)
uer_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uer_damper_i_1 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.uer_damper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
uer_damper_i_1.relative_to = relative_to
uer_damper_i_1.marker_name = '.turn.ger_lower_cylinder.uer_damper_i_1'
_turn_ground_cfr_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lc_top')
uer_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_damper_i_1.location, uer_damper_i_1.orientation)
uer_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uer_stopper_i_1 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.uer_stopper_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder')
uer_stopper_i_1.relative_to = relative_to
uer_stopper_i_1.marker_name = '.turn.ger_lower_cylinder.uer_stopper_i_1'
_turn_ground_cfr_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lc_top')
uer_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_lc_top))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_stopper_i_1.location, uer_stopper_i_1.orientation)
uer_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_lower_cylinder = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.gralin_lower_cylinder')
gralin_lower_cylinder.cylinder_name = '.turn.ger_lower_cylinder.gralin_lower_cylinder'
_turn_ground_cfr_lc_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lc_top').location
_turn_ground_hpr_lc_bot = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lc_bot').location
gralin_lower_cylinder.length = (VecUtils.DM(_turn_ground_cfr_lc_top, _turn_ground_hpr_lc_bot))


gralin_geom = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.gralin_geom')
gralin_geom.cylinder_name = '.turn.ger_lower_cylinder.gralin_geom'
_turn_ground_hpr_ib_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ib_axle').location
_turn_ground_hpr_ob_axle = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ob_axle').location
gralin_geom.length = (VecUtils.DM(_turn_ground_hpr_ib_axle, _turn_ground_hpr_ob_axle))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_upper_dragbrace.inertia_frame'
_turn_gel_upper_dragbrace_cm = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_dragbrace_cm))
_turn_gel_upper_dragbrace = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_24 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.gralin_24')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace')
gralin_24.relative_to = relative_to
gralin_24.marker_name = '.turn.gel_upper_dragbrace.gralin_24'
_turn_ground_hpl_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_udb_spndl_atch_1')
gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_udb_spndl_atch_1))
_turn_ground_hpl_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_udb_spndl_atch_1').location
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1').location
gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_udb_spndl_atch_1, _turn_ground_hpl_ldb_udb_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_14 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.jxl_joint_j_14')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace')
jxl_joint_j_14.relative_to = relative_to
jxl_joint_j_14.marker_name = '.turn.gel_upper_dragbrace.jxl_joint_j_14'
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1')
jxl_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_ldb_udb_atch_1))
_turn_gel_upper_dragbrace = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace')
_turn_ground_cfl_plane_ref_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_plane_ref_2').global_loc
jxl_joint_j_14.orientation = (ORI_LOCAL(ORI_ALIGN_AXIS(_turn_ground_cfl_plane_ref_2, "Z+Z"), _turn_gel_upper_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_14.location, jxl_joint_j_14.orientation)
jxl_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_5 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.jxl_joint_i_5')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace')
jxl_joint_i_5.relative_to = relative_to
jxl_joint_i_5.marker_name = '.turn.gel_upper_dragbrace.jxl_joint_i_5'
_turn_gel_spindle_jxl_joint_j_5 = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.jxl_joint_j_5')
jxl_joint_i_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_spindle_jxl_joint_j_5))
_turn_gel_upper_dragbrace_jxl_joint_i_5 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.jxl_joint_i_5').global_loc
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1').global_loc
_turn_ground_hpl_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_spndl_sf_atch').location
jxl_joint_i_5.orientation = (VecUtils.ORI_IN_PLANE(_turn_gel_upper_dragbrace_jxl_joint_i_5, _turn_ground_hpl_ldb_udb_atch_1, _turn_ground_hpl_spndl_sf_atch, "Z_ZX"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_5.location, jxl_joint_i_5.orientation)
jxl_joint_i_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uel_actuator_i_3 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.uel_actuator_i_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace')
uel_actuator_i_3.relative_to = relative_to
uel_actuator_i_3.marker_name = '.turn.gel_upper_dragbrace.uel_actuator_i_3'
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1')
uel_actuator_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_ldb_udb_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_i_3.location, uel_actuator_i_3.orientation)
uel_actuator_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_upper_dragbrace = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.gralin_upper_dragbrace')
gralin_upper_dragbrace.cylinder_name = '.turn.gel_upper_dragbrace.gralin_upper_dragbrace'
_turn_ground_hpl_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_udb_spndl_atch_1').location
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1').location
gralin_upper_dragbrace.length = (VecUtils.DM(_turn_ground_hpl_udb_spndl_atch_1, _turn_ground_hpl_ldb_udb_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_upper_dragbrace.inertia_frame'
_turn_ger_upper_dragbrace_cm = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_dragbrace_cm))
_turn_ger_upper_dragbrace = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_25 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.gralin_25')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace')
gralin_25.relative_to = relative_to
gralin_25.marker_name = '.turn.ger_upper_dragbrace.gralin_25'
_turn_ground_hpr_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_udb_spndl_atch_1')
gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_udb_spndl_atch_1))
_turn_ground_hpr_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_udb_spndl_atch_1').location
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1').location
gralin_25.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_udb_spndl_atch_1, _turn_ground_hpr_ldb_udb_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_25.location, gralin_25.orientation)
gralin_25.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_25.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_j_14 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.jxr_joint_j_14')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace')
jxr_joint_j_14.relative_to = relative_to
jxr_joint_j_14.marker_name = '.turn.ger_upper_dragbrace.jxr_joint_j_14'
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1')
jxr_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_ldb_udb_atch_1))
_turn_ger_upper_dragbrace = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace')
_turn_ground_cfr_plane_ref_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_plane_ref_2').global_loc
jxr_joint_j_14.orientation = (ORI_LOCAL(ORI_ALIGN_AXIS(_turn_ground_cfr_plane_ref_2, "Z+Z"), _turn_ger_upper_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_14.location, jxr_joint_j_14.orientation)
jxr_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_5 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.jxr_joint_i_5')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace')
jxr_joint_i_5.relative_to = relative_to
jxr_joint_i_5.marker_name = '.turn.ger_upper_dragbrace.jxr_joint_i_5'
_turn_ger_spindle_jxr_joint_j_5 = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.jxr_joint_j_5')
jxr_joint_i_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_spindle_jxr_joint_j_5))
_turn_ger_upper_dragbrace_jxr_joint_i_5 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.jxr_joint_i_5').global_loc
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1').global_loc
_turn_ground_hpr_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_spndl_sf_atch').location
jxr_joint_i_5.orientation = (VecUtils.ORI_IN_PLANE(_turn_ger_upper_dragbrace_jxr_joint_i_5, _turn_ground_hpr_ldb_udb_atch_1, _turn_ground_hpr_spndl_sf_atch, "Z_ZX"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_5.location, jxr_joint_i_5.orientation)
jxr_joint_i_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uer_actuator_i_3 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.uer_actuator_i_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace')
uer_actuator_i_3.relative_to = relative_to
uer_actuator_i_3.marker_name = '.turn.ger_upper_dragbrace.uer_actuator_i_3'
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1')
uer_actuator_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_ldb_udb_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_i_3.location, uer_actuator_i_3.orientation)
uer_actuator_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_upper_dragbrace = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.gralin_upper_dragbrace')
gralin_upper_dragbrace.cylinder_name = '.turn.ger_upper_dragbrace.gralin_upper_dragbrace'
_turn_ground_hpr_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_udb_spndl_atch_1').location
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1').location
gralin_upper_dragbrace.length = (VecUtils.DM(_turn_ground_hpr_udb_spndl_atch_1, _turn_ground_hpr_ldb_udb_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_lower_dragbrace.inertia_frame'
_turn_gel_lower_dragbrace_cm = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lower_dragbrace_cm))
_turn_gel_lower_dragbrace = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lower_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_26 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.gralin_26')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace')
gralin_26.relative_to = relative_to
gralin_26.marker_name = '.turn.gel_lower_dragbrace.gralin_26'
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1')
gralin_26.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_ldb_udb_atch_1))
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1').location
_turn_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_collar_atch_1').location
gralin_26.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_ldb_udb_atch_1, _turn_ground_hpl_ldb_collar_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_26.location, gralin_26.orientation)
gralin_26.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_26.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_14 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.jxl_joint_i_14')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace')
jxl_joint_i_14.relative_to = relative_to
jxl_joint_i_14.marker_name = '.turn.gel_lower_dragbrace.jxl_joint_i_14'
_turn_gel_upper_dragbrace_jxl_joint_j_14 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.jxl_joint_j_14')
jxl_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_dragbrace_jxl_joint_j_14))
_turn_gel_upper_dragbrace_jxl_joint_j_14 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_dragbrace.jxl_joint_j_14')
jxl_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_dragbrace_jxl_joint_j_14))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_14.location, jxl_joint_i_14.orientation)
jxl_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_10 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.jxl_joint_i_10')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace')
jxl_joint_i_10.relative_to = relative_to
jxl_joint_i_10.marker_name = '.turn.gel_lower_dragbrace.jxl_joint_i_10'
_turn_gel_uc_collar_jxl_joint_j_10 = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_j_10')
jxl_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_uc_collar_jxl_joint_j_10))
_turn_gel_uc_collar_jxl_joint_j_10 = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_j_10')
jxl_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_uc_collar_jxl_joint_j_10))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_10.location, jxl_joint_i_10.orientation)
jxl_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


graarm_1 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.graarm_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace')
graarm_1.relative_to = relative_to
graarm_1.marker_name = '.turn.gel_lower_dragbrace.graarm_1'
_turn_ground_hpl_uplock_tab = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uplock_tab')
graarm_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_uplock_tab))
_turn_ground_hpl_uplock_tab = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uplock_tab').global_loc
_turn_ground_cfl_ldb_geompt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_ldb_geompt_1').global_loc
_turn_ground_cfl_ldb_geompt_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_ldb_geompt_2').location
graarm_1.orientation = (VecUtils.ORI_IN_PLANE(_turn_ground_hpl_uplock_tab, _turn_ground_cfl_ldb_geompt_1, _turn_ground_cfl_ldb_geompt_2, "X_XY"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_1.location, graarm_1.orientation)
graarm_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
graarm_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


graarm_2 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.graarm_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace')
graarm_2.relative_to = relative_to
graarm_2.marker_name = '.turn.gel_lower_dragbrace.graarm_2'
_turn_ground_cfl_ldb_geompt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_ldb_geompt_1')
graarm_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_ldb_geompt_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_2.location, graarm_2.orientation)
graarm_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


graarm_3 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.graarm_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace')
graarm_3.relative_to = relative_to
graarm_3.marker_name = '.turn.gel_lower_dragbrace.graarm_3'
_turn_ground_cfl_ldb_geompt_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_ldb_geompt_2')
graarm_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_ldb_geompt_2))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_3.location, graarm_3.orientation)
graarm_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_lower_dragbrace = Jusme.ActiveUSScene.getObject('.turn.gel_lower_dragbrace.gralin_lower_dragbrace')
gralin_lower_dragbrace.cylinder_name = '.turn.gel_lower_dragbrace.gralin_lower_dragbrace'
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1').location
_turn_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_collar_atch_1').location
gralin_lower_dragbrace.length = (VecUtils.DM(_turn_ground_hpl_ldb_udb_atch_1, _turn_ground_hpl_ldb_collar_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_lower_dragbrace.inertia_frame'
_turn_ger_lower_dragbrace_cm = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lower_dragbrace_cm))
_turn_ger_lower_dragbrace = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lower_dragbrace))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_27 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.gralin_27')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace')
gralin_27.relative_to = relative_to
gralin_27.marker_name = '.turn.ger_lower_dragbrace.gralin_27'
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1')
gralin_27.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_ldb_udb_atch_1))
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1').location
_turn_ground_hpr_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_collar_atch_1').location
gralin_27.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_ldb_udb_atch_1, _turn_ground_hpr_ldb_collar_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_27.location, gralin_27.orientation)
gralin_27.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_27.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_14 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.jxr_joint_i_14')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace')
jxr_joint_i_14.relative_to = relative_to
jxr_joint_i_14.marker_name = '.turn.ger_lower_dragbrace.jxr_joint_i_14'
_turn_ger_upper_dragbrace_jxr_joint_j_14 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.jxr_joint_j_14')
jxr_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_dragbrace_jxr_joint_j_14))
_turn_ger_upper_dragbrace_jxr_joint_j_14 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_dragbrace.jxr_joint_j_14')
jxr_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_dragbrace_jxr_joint_j_14))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_14.location, jxr_joint_i_14.orientation)
jxr_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_10 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.jxr_joint_i_10')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace')
jxr_joint_i_10.relative_to = relative_to
jxr_joint_i_10.marker_name = '.turn.ger_lower_dragbrace.jxr_joint_i_10'
_turn_ger_uc_collar_jxr_joint_j_10 = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_j_10')
jxr_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_uc_collar_jxr_joint_j_10))
_turn_ger_uc_collar_jxr_joint_j_10 = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_j_10')
jxr_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_uc_collar_jxr_joint_j_10))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_10.location, jxr_joint_i_10.orientation)
jxr_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


graarm_4 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.graarm_4')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace')
graarm_4.relative_to = relative_to
graarm_4.marker_name = '.turn.ger_lower_dragbrace.graarm_4'
_turn_ground_hpr_uplock_tab = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uplock_tab')
graarm_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_uplock_tab))
_turn_ground_hpr_uplock_tab = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uplock_tab').global_loc
_turn_ground_cfr_ldb_geompt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_ldb_geompt_1').global_loc
_turn_ground_cfr_ldb_geompt_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_ldb_geompt_2').location
graarm_4.orientation = (VecUtils.ORI_IN_PLANE(_turn_ground_hpr_uplock_tab, _turn_ground_cfr_ldb_geompt_1, _turn_ground_cfr_ldb_geompt_2, "X_XY"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_4.location, graarm_4.orientation)
graarm_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
graarm_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


graarm_5 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.graarm_5')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace')
graarm_5.relative_to = relative_to
graarm_5.marker_name = '.turn.ger_lower_dragbrace.graarm_5'
_turn_ground_cfr_ldb_geompt_1 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_ldb_geompt_1')
graarm_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_ldb_geompt_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_5.location, graarm_5.orientation)
graarm_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


graarm_6 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.graarm_6')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace')
graarm_6.relative_to = relative_to
graarm_6.marker_name = '.turn.ger_lower_dragbrace.graarm_6'
_turn_ground_cfr_ldb_geompt_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_ldb_geompt_2')
graarm_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_ldb_geompt_2))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_6.location, graarm_6.orientation)
graarm_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_lower_dragbrace = Jusme.ActiveUSScene.getObject('.turn.ger_lower_dragbrace.gralin_lower_dragbrace')
gralin_lower_dragbrace.cylinder_name = '.turn.ger_lower_dragbrace.gralin_lower_dragbrace'
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1').location
_turn_ground_hpr_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_collar_atch_1').location
gralin_lower_dragbrace.length = (VecUtils.DM(_turn_ground_hpr_ldb_udb_atch_1, _turn_ground_hpr_ldb_collar_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_upper_torquearm.inertia_frame'
_turn_gel_upper_torquearm_cm = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_torquearm_cm))
_turn_gel_upper_torquearm = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_torquearm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_11 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.gralin_11')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm')
gralin_11.relative_to = relative_to
gralin_11.marker_name = '.turn.gel_upper_torquearm.gralin_11'
_turn_ground_hpl_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_collar_atch_1')
gralin_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_uta_collar_atch_1))
_turn_ground_hpl_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_collar_atch_1').location
_turn_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_1').location
gralin_11.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_uta_collar_atch_1, _turn_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_11.location, gralin_11.orientation)
gralin_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_2 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.jxl_joint_i_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm')
jxl_joint_i_2.relative_to = relative_to
jxl_joint_i_2.marker_name = '.turn.gel_upper_torquearm.jxl_joint_i_2'
_turn_gel_connector_jxl_joint_j_2 = Jusme.ActiveUSScene.getObject('.turn.gel_connector.jxl_joint_j_2')
jxl_joint_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_connector_jxl_joint_j_2))
_turn_gel_connector_jxl_joint_j_2 = Jusme.ActiveUSScene.getObject('.turn.gel_connector.jxl_joint_j_2')
jxl_joint_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_connector_jxl_joint_j_2))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_2.location, jxl_joint_i_2.orientation)
jxl_joint_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_3 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.jxl_joint_i_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm')
jxl_joint_i_3.relative_to = relative_to
jxl_joint_i_3.marker_name = '.turn.gel_upper_torquearm.jxl_joint_i_3'
_turn_gel_uc_collar_jxl_joint_j_3 = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_j_3')
jxl_joint_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_uc_collar_jxl_joint_j_3))
_turn_gel_uc_collar_jxl_joint_j_3 = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_j_3')
jxl_joint_i_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_uc_collar_jxl_joint_j_3))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_3.location, jxl_joint_i_3.orientation)
jxl_joint_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_upper_torquearm = Jusme.ActiveUSScene.getObject('.turn.gel_upper_torquearm.gralin_upper_torquearm')
gralin_upper_torquearm.cylinder_name = '.turn.gel_upper_torquearm.gralin_upper_torquearm'
_turn_ground_hpl_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_collar_atch_1').location
_turn_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_1').location
gralin_upper_torquearm.length = (VecUtils.DM(_turn_ground_hpl_uta_collar_atch_1, _turn_ground_hpl_uta_connect_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_upper_torquearm.inertia_frame'
_turn_ger_upper_torquearm_cm = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_torquearm_cm))
_turn_ger_upper_torquearm = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_torquearm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_28 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.gralin_28')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm')
gralin_28.relative_to = relative_to
gralin_28.marker_name = '.turn.ger_upper_torquearm.gralin_28'
_turn_ground_hpr_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_collar_atch_1')
gralin_28.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_uta_collar_atch_1))
_turn_ground_hpr_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_collar_atch_1').location
_turn_ground_hpr_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_1').location
gralin_28.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_uta_collar_atch_1, _turn_ground_hpr_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_28.location, gralin_28.orientation)
gralin_28.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_28.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_2 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.jxr_joint_i_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm')
jxr_joint_i_2.relative_to = relative_to
jxr_joint_i_2.marker_name = '.turn.ger_upper_torquearm.jxr_joint_i_2'
_turn_ger_connector_jxr_joint_j_2 = Jusme.ActiveUSScene.getObject('.turn.ger_connector.jxr_joint_j_2')
jxr_joint_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_connector_jxr_joint_j_2))
_turn_ger_connector_jxr_joint_j_2 = Jusme.ActiveUSScene.getObject('.turn.ger_connector.jxr_joint_j_2')
jxr_joint_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_connector_jxr_joint_j_2))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_2.location, jxr_joint_i_2.orientation)
jxr_joint_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_3 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.jxr_joint_i_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm')
jxr_joint_i_3.relative_to = relative_to
jxr_joint_i_3.marker_name = '.turn.ger_upper_torquearm.jxr_joint_i_3'
_turn_ger_uc_collar_jxr_joint_j_3 = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_j_3')
jxr_joint_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_uc_collar_jxr_joint_j_3))
_turn_ger_uc_collar_jxr_joint_j_3 = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_j_3')
jxr_joint_i_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_uc_collar_jxr_joint_j_3))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_3.location, jxr_joint_i_3.orientation)
jxr_joint_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_upper_torquearm = Jusme.ActiveUSScene.getObject('.turn.ger_upper_torquearm.gralin_upper_torquearm')
gralin_upper_torquearm.cylinder_name = '.turn.ger_upper_torquearm.gralin_upper_torquearm'
_turn_ground_hpr_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_collar_atch_1').location
_turn_ground_hpr_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_1').location
gralin_upper_torquearm.length = (VecUtils.DM(_turn_ground_hpr_uta_collar_atch_1, _turn_ground_hpr_uta_connect_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_lower_torquearm.inertia_frame'
_turn_gel_lower_torquearm_cm = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lower_torquearm_cm))
_turn_gel_lower_torquearm = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lower_torquearm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_29 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.gralin_29')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm')
gralin_29.relative_to = relative_to
gralin_29.marker_name = '.turn.gel_lower_torquearm.gralin_29'
_turn_ground_hpl_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_lc_atch_1')
gralin_29.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_lta_lc_atch_1))
_turn_ground_hpl_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_lc_atch_1').location
_turn_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_connect_atch_1').location
gralin_29.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_lta_lc_atch_1, _turn_ground_hpl_lta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_29.location, gralin_29.orientation)
gralin_29.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_29.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_11 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.jxl_joint_i_11')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm')
jxl_joint_i_11.relative_to = relative_to
jxl_joint_i_11.marker_name = '.turn.gel_lower_torquearm.jxl_joint_i_11'
_turn_gel_lower_cylinder_jxl_joint_j_11 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.jxl_joint_j_11')
jxl_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lower_cylinder_jxl_joint_j_11))
_turn_gel_lower_cylinder_jxl_joint_j_11 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_cylinder.jxl_joint_j_11')
jxl_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lower_cylinder_jxl_joint_j_11))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_11.location, jxl_joint_i_11.orientation)
jxl_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_1 = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.jxl_joint_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm')
jxl_joint_i_1.relative_to = relative_to
jxl_joint_i_1.marker_name = '.turn.gel_lower_torquearm.jxl_joint_i_1'
_turn_gel_connector_jxl_joint_j_1 = Jusme.ActiveUSScene.getObject('.turn.gel_connector.jxl_joint_j_1')
jxl_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_connector_jxl_joint_j_1))
_turn_gel_connector_jxl_joint_j_1 = Jusme.ActiveUSScene.getObject('.turn.gel_connector.jxl_joint_j_1')
jxl_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_connector_jxl_joint_j_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_1.location, jxl_joint_i_1.orientation)
jxl_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_lower_torquearm = Jusme.ActiveUSScene.getObject('.turn.gel_lower_torquearm.gralin_lower_torquearm')
gralin_lower_torquearm.cylinder_name = '.turn.gel_lower_torquearm.gralin_lower_torquearm'
_turn_ground_hpl_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_lc_atch_1').location
_turn_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_connect_atch_1').location
gralin_lower_torquearm.length = (VecUtils.DM(_turn_ground_hpl_lta_lc_atch_1, _turn_ground_hpl_lta_connect_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_lower_torquearm.inertia_frame'
_turn_ger_lower_torquearm_cm = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lower_torquearm_cm))
_turn_ger_lower_torquearm = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lower_torquearm))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_30 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.gralin_30')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm')
gralin_30.relative_to = relative_to
gralin_30.marker_name = '.turn.ger_lower_torquearm.gralin_30'
_turn_ground_hpr_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_lc_atch_1')
gralin_30.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_lta_lc_atch_1))
_turn_ground_hpr_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_lc_atch_1').location
_turn_ground_hpr_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_connect_atch_1').location
gralin_30.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_lta_lc_atch_1, _turn_ground_hpr_lta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_30.location, gralin_30.orientation)
gralin_30.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_30.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_11 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.jxr_joint_i_11')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm')
jxr_joint_i_11.relative_to = relative_to
jxr_joint_i_11.marker_name = '.turn.ger_lower_torquearm.jxr_joint_i_11'
_turn_ger_lower_cylinder_jxr_joint_j_11 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.jxr_joint_j_11')
jxr_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lower_cylinder_jxr_joint_j_11))
_turn_ger_lower_cylinder_jxr_joint_j_11 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_cylinder.jxr_joint_j_11')
jxr_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lower_cylinder_jxr_joint_j_11))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_11.location, jxr_joint_i_11.orientation)
jxr_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_1 = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.jxr_joint_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm')
jxr_joint_i_1.relative_to = relative_to
jxr_joint_i_1.marker_name = '.turn.ger_lower_torquearm.jxr_joint_i_1'
_turn_ger_connector_jxr_joint_j_1 = Jusme.ActiveUSScene.getObject('.turn.ger_connector.jxr_joint_j_1')
jxr_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_connector_jxr_joint_j_1))
_turn_ger_connector_jxr_joint_j_1 = Jusme.ActiveUSScene.getObject('.turn.ger_connector.jxr_joint_j_1')
jxr_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_connector_jxr_joint_j_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_1.location, jxr_joint_i_1.orientation)
jxr_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_lower_torquearm = Jusme.ActiveUSScene.getObject('.turn.ger_lower_torquearm.gralin_lower_torquearm')
gralin_lower_torquearm.cylinder_name = '.turn.ger_lower_torquearm.gralin_lower_torquearm'
_turn_ground_hpr_lta_lc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_lc_atch_1').location
_turn_ground_hpr_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_connect_atch_1').location
gralin_lower_torquearm.length = (VecUtils.DM(_turn_ground_hpr_lta_lc_atch_1, _turn_ground_hpr_lta_connect_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_connector.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_connector')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_connector.inertia_frame'
_turn_gel_connector_cm = Jusme.ActiveUSScene.getObject('.turn.gel_connector.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_connector_cm))
_turn_gel_connector = Jusme.ActiveUSScene.getObject('.turn.gel_connector')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_connector))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_3 = Jusme.ActiveUSScene.getObject('.turn.gel_connector.gralin_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_connector')
gralin_3.relative_to = relative_to
gralin_3.marker_name = '.turn.gel_connector.gralin_3'
_turn_ground_hpl_connect_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_connect_1')
gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_connect_1))
_turn_ground_hpl_connect_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_connect_1').location
_turn_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_1').location
gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_connect_1, _turn_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_1 = Jusme.ActiveUSScene.getObject('.turn.gel_connector.jxl_joint_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_connector')
jxl_joint_j_1.relative_to = relative_to
jxl_joint_j_1.marker_name = '.turn.gel_connector.jxl_joint_j_1'
_turn_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_connect_atch_1')
jxl_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_lta_connect_atch_1))
_turn_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_connect_atch_1').location
_turn_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_1').location
jxl_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_lta_connect_atch_1, _turn_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_1.location, jxl_joint_j_1.orientation)
jxl_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_2 = Jusme.ActiveUSScene.getObject('.turn.gel_connector.jxl_joint_j_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_connector')
jxl_joint_j_2.relative_to = relative_to
jxl_joint_j_2.marker_name = '.turn.gel_connector.jxl_joint_j_2'
_turn_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_1')
jxl_joint_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_uta_connect_atch_1))
_turn_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_1').location
_turn_ground_hpl_uta_connect_atch_2 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_2').location
jxl_joint_j_2.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_uta_connect_atch_1, _turn_ground_hpl_uta_connect_atch_2, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_2.location, jxl_joint_j_2.orientation)
jxl_joint_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_connector = Jusme.ActiveUSScene.getObject('.turn.gel_connector.gralin_connector')
gralin_connector.cylinder_name = '.turn.gel_connector.gralin_connector'
_turn_ground_hpl_connect_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_connect_1').location
_turn_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_1').location
gralin_connector.length = (VecUtils.DM(_turn_ground_hpl_connect_1, _turn_ground_hpl_uta_connect_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_connector.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_connector')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_connector.inertia_frame'
_turn_ger_connector_cm = Jusme.ActiveUSScene.getObject('.turn.ger_connector.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_connector_cm))
_turn_ger_connector = Jusme.ActiveUSScene.getObject('.turn.ger_connector')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_connector))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_4 = Jusme.ActiveUSScene.getObject('.turn.ger_connector.gralin_4')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_connector')
gralin_4.relative_to = relative_to
gralin_4.marker_name = '.turn.ger_connector.gralin_4'
_turn_ground_hpr_connect_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_connect_1')
gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_connect_1))
_turn_ground_hpr_connect_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_connect_1').location
_turn_ground_hpr_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_1').location
gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_connect_1, _turn_ground_hpr_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_j_1 = Jusme.ActiveUSScene.getObject('.turn.ger_connector.jxr_joint_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_connector')
jxr_joint_j_1.relative_to = relative_to
jxr_joint_j_1.marker_name = '.turn.ger_connector.jxr_joint_j_1'
_turn_ground_hpr_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_connect_atch_1')
jxr_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_lta_connect_atch_1))
_turn_ground_hpr_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_connect_atch_1').location
_turn_ground_hpr_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_1').location
jxr_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_lta_connect_atch_1, _turn_ground_hpr_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_1.location, jxr_joint_j_1.orientation)
jxr_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_j_2 = Jusme.ActiveUSScene.getObject('.turn.ger_connector.jxr_joint_j_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_connector')
jxr_joint_j_2.relative_to = relative_to
jxr_joint_j_2.marker_name = '.turn.ger_connector.jxr_joint_j_2'
_turn_ground_hpr_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_1')
jxr_joint_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_uta_connect_atch_1))
_turn_ground_hpr_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_1').location
_turn_ground_hpr_uta_connect_atch_2 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_2').location
jxr_joint_j_2.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_uta_connect_atch_1, _turn_ground_hpr_uta_connect_atch_2, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_2.location, jxr_joint_j_2.orientation)
jxr_joint_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_connector = Jusme.ActiveUSScene.getObject('.turn.ger_connector.gralin_connector')
gralin_connector.cylinder_name = '.turn.ger_connector.gralin_connector'
_turn_ground_hpr_connect_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_connect_1').location
_turn_ground_hpr_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_1').location
gralin_connector.length = (VecUtils.DM(_turn_ground_hpr_connect_1, _turn_ground_hpr_uta_connect_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_uc_collar.inertia_frame'
_turn_gel_uc_collar_cm = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_uc_collar_cm))
_turn_gel_uc_collar = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_uc_collar))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_5 = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.gralin_5')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar')
gralin_5.relative_to = relative_to
gralin_5.marker_name = '.turn.gel_uc_collar.gralin_5'
_turn_ground_cfl_collar_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_collar_top')
gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_collar_top))
_turn_ground_cfl_collar_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_collar_top').location
_turn_ground_cfl_collar_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_collar_bot').location
gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_cfl_collar_top, _turn_ground_cfl_collar_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_3 = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_j_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar')
jxl_joint_j_3.relative_to = relative_to
jxl_joint_j_3.marker_name = '.turn.gel_uc_collar.jxl_joint_j_3'
_turn_ground_hpl_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_collar_atch_1')
jxl_joint_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_uta_collar_atch_1))
_turn_ground_hpl_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lta_connect_atch_1').location
_turn_ground_hpl_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_uta_connect_atch_1').location
jxl_joint_j_3.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_lta_connect_atch_1, _turn_ground_hpl_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_3.location, jxl_joint_j_3.orientation)
jxl_joint_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_4 = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_i_4')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar')
jxl_joint_i_4.relative_to = relative_to
jxl_joint_i_4.marker_name = '.turn.gel_uc_collar.jxl_joint_i_4'
_turn_gel_upper_cylinder_jxl_joint_j_4 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.jxl_joint_j_4')
jxl_joint_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_cylinder_jxl_joint_j_4))
_turn_gel_upper_cylinder_jxl_joint_j_4 = Jusme.ActiveUSScene.getObject('.turn.gel_upper_cylinder.jxl_joint_j_4')
jxl_joint_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upper_cylinder_jxl_joint_j_4))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_4.location, jxl_joint_i_4.orientation)
jxl_joint_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_10 = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.jxl_joint_j_10')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar')
jxl_joint_j_10.relative_to = relative_to
jxl_joint_j_10.marker_name = '.turn.gel_uc_collar.jxl_joint_j_10'
_turn_ground_hpl_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_collar_atch_1')
jxl_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_ldb_collar_atch_1))
_turn_gel_uc_collar = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar')
_turn_ground_cfl_plane_ref_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_plane_ref_2').global_loc
jxl_joint_j_10.orientation = (ORI_LOCAL(ORI_ALIGN_AXIS(_turn_ground_cfl_plane_ref_2, "Z+Z"), _turn_gel_uc_collar))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_10.location, jxl_joint_j_10.orientation)
jxl_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_uc_collar = Jusme.ActiveUSScene.getObject('.turn.gel_uc_collar.gralin_uc_collar')
gralin_uc_collar.cylinder_name = '.turn.gel_uc_collar.gralin_uc_collar'
_turn_ground_cfl_collar_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_collar_top').location
_turn_ground_cfl_collar_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_collar_bot').location
gralin_uc_collar.length = (VecUtils.DM(_turn_ground_cfl_collar_top, _turn_ground_cfl_collar_bot))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_uc_collar.inertia_frame'
_turn_ger_uc_collar_cm = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_uc_collar_cm))
_turn_ger_uc_collar = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_uc_collar))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_6 = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.gralin_6')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar')
gralin_6.relative_to = relative_to
gralin_6.marker_name = '.turn.ger_uc_collar.gralin_6'
_turn_ground_cfr_collar_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_collar_top')
gralin_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_collar_top))
_turn_ground_cfr_collar_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_collar_top').location
_turn_ground_cfr_collar_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_collar_bot').location
gralin_6.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_cfr_collar_top, _turn_ground_cfr_collar_bot, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_6.location, gralin_6.orientation)
gralin_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_6.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_j_3 = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_j_3')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar')
jxr_joint_j_3.relative_to = relative_to
jxr_joint_j_3.marker_name = '.turn.ger_uc_collar.jxr_joint_j_3'
_turn_ground_hpr_uta_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_collar_atch_1')
jxr_joint_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_uta_collar_atch_1))
_turn_ground_hpr_lta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lta_connect_atch_1').location
_turn_ground_hpr_uta_connect_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_uta_connect_atch_1').location
jxr_joint_j_3.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_lta_connect_atch_1, _turn_ground_hpr_uta_connect_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_3.location, jxr_joint_j_3.orientation)
jxr_joint_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_j_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_4 = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_i_4')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar')
jxr_joint_i_4.relative_to = relative_to
jxr_joint_i_4.marker_name = '.turn.ger_uc_collar.jxr_joint_i_4'
_turn_ger_upper_cylinder_jxr_joint_j_4 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.jxr_joint_j_4')
jxr_joint_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_cylinder_jxr_joint_j_4))
_turn_ger_upper_cylinder_jxr_joint_j_4 = Jusme.ActiveUSScene.getObject('.turn.ger_upper_cylinder.jxr_joint_j_4')
jxr_joint_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upper_cylinder_jxr_joint_j_4))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_4.location, jxr_joint_i_4.orientation)
jxr_joint_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_j_10 = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.jxr_joint_j_10')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar')
jxr_joint_j_10.relative_to = relative_to
jxr_joint_j_10.marker_name = '.turn.ger_uc_collar.jxr_joint_j_10'
_turn_ground_hpr_ldb_collar_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_collar_atch_1')
jxr_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_ldb_collar_atch_1))
_turn_ger_uc_collar = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar')
_turn_ground_cfr_plane_ref_2 = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_plane_ref_2').global_loc
jxr_joint_j_10.orientation = (ORI_LOCAL(ORI_ALIGN_AXIS(_turn_ground_cfr_plane_ref_2, "Z+Z"), _turn_ger_uc_collar))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_10.location, jxr_joint_j_10.orientation)
jxr_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_uc_collar = Jusme.ActiveUSScene.getObject('.turn.ger_uc_collar.gralin_uc_collar')
gralin_uc_collar.cylinder_name = '.turn.ger_uc_collar.gralin_uc_collar'
_turn_ground_cfr_collar_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_collar_top').location
_turn_ground_cfr_collar_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_collar_bot').location
gralin_uc_collar.length = (VecUtils.DM(_turn_ground_cfr_collar_top, _turn_ground_cfr_collar_bot))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_spindle')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_spindle.inertia_frame'
_turn_gel_spindle_cm = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_spindle_cm))
_turn_gel_spindle = Jusme.ActiveUSScene.getObject('.turn.gel_spindle')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_spindle))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_7 = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.gralin_7')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_spindle')
gralin_7.relative_to = relative_to
gralin_7.marker_name = '.turn.gel_spindle.gralin_7'
_turn_ground_hpl_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_spndl_sf_atch')
gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_spndl_sf_atch))
_turn_ground_hpl_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_spndl_sf_atch').location
_turn_ground_hpl_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_udb_spndl_atch_1').location
gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_spndl_sf_atch, _turn_ground_hpl_udb_spndl_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_5 = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.jxl_joint_j_5')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_spindle')
jxl_joint_j_5.relative_to = relative_to
jxl_joint_j_5.marker_name = '.turn.gel_spindle.jxl_joint_j_5'
_turn_ground_hpl_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_udb_spndl_atch_1')
jxl_joint_j_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_udb_spndl_atch_1))
_turn_ground_hpl_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_spndl_sf_atch').global_loc
_turn_gel_spindle_jxl_joint_j_5 = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.jxl_joint_j_5').global_loc
_turn_ground_hpl_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_ldb_udb_atch_1').location
jxl_joint_j_5.orientation = (VecUtils.ORI_IN_PLANE(_turn_ground_hpl_spndl_sf_atch, _turn_gel_spindle_jxl_joint_j_5, _turn_ground_hpl_ldb_udb_atch_1, "Z_ZX"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_5.location, jxl_joint_j_5.orientation)
jxl_joint_j_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_spindle = Jusme.ActiveUSScene.getObject('.turn.gel_spindle.gralin_spindle')
gralin_spindle.cylinder_name = '.turn.gel_spindle.gralin_spindle'
_turn_ground_hpl_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_spndl_sf_atch').location
_turn_ground_hpl_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_udb_spndl_atch_1').location
gralin_spindle.length = (VecUtils.DM(_turn_ground_hpl_spndl_sf_atch, _turn_ground_hpl_udb_spndl_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_spindle')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_spindle.inertia_frame'
_turn_ger_spindle_cm = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_spindle_cm))
_turn_ger_spindle = Jusme.ActiveUSScene.getObject('.turn.ger_spindle')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_spindle))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_8 = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.gralin_8')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_spindle')
gralin_8.relative_to = relative_to
gralin_8.marker_name = '.turn.ger_spindle.gralin_8'
_turn_ground_hpr_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_spndl_sf_atch')
gralin_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_spndl_sf_atch))
_turn_ground_hpr_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_spndl_sf_atch').location
_turn_ground_hpr_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_udb_spndl_atch_1').location
gralin_8.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_spndl_sf_atch, _turn_ground_hpr_udb_spndl_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_8.location, gralin_8.orientation)
gralin_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_j_5 = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.jxr_joint_j_5')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_spindle')
jxr_joint_j_5.relative_to = relative_to
jxr_joint_j_5.marker_name = '.turn.ger_spindle.jxr_joint_j_5'
_turn_ground_hpr_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_udb_spndl_atch_1')
jxr_joint_j_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_udb_spndl_atch_1))
_turn_ground_hpr_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_spndl_sf_atch').global_loc
_turn_ger_spindle_jxr_joint_j_5 = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.jxr_joint_j_5').global_loc
_turn_ground_hpr_ldb_udb_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_ldb_udb_atch_1').location
jxr_joint_j_5.orientation = (VecUtils.ORI_IN_PLANE(_turn_ground_hpr_spndl_sf_atch, _turn_ger_spindle_jxr_joint_j_5, _turn_ground_hpr_ldb_udb_atch_1, "Z_ZX"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_5.location, jxr_joint_j_5.orientation)
jxr_joint_j_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_j_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_spindle = Jusme.ActiveUSScene.getObject('.turn.ger_spindle.gralin_spindle')
gralin_spindle.cylinder_name = '.turn.ger_spindle.gralin_spindle'
_turn_ground_hpr_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_spndl_sf_atch').location
_turn_ground_hpr_udb_spndl_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_udb_spndl_atch_1').location
gralin_spindle.length = (VecUtils.DM(_turn_ground_hpr_spndl_sf_atch, _turn_ground_hpr_udb_spndl_atch_1))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lwract')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_lwract.inertia_frame'
_turn_gel_lwract_cm = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lwract_cm))
_turn_gel_lwract = Jusme.ActiveUSScene.getObject('.turn.gel_lwract')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lwract))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_9 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.gralin_9')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lwract')
gralin_9.relative_to = relative_to
gralin_9.marker_name = '.turn.gel_lwract.gralin_9'
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1')
gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_lwract_uc_atch_1))
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1').location
_turn_ground_cfl_lwract_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lwract_top').location
gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_lwract_uc_atch_1, _turn_ground_cfl_lwract_top, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_7 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.jxl_joint_j_7')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lwract')
jxl_joint_j_7.relative_to = relative_to
jxl_joint_j_7.marker_name = '.turn.gel_lwract.jxl_joint_j_7'
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1')
jxl_joint_j_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_lwract_uc_atch_1))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
jxl_joint_j_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_7.location, jxl_joint_j_7.orientation)
jxl_joint_j_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_i_8 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.jxl_joint_i_8')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lwract')
jxl_joint_i_8.relative_to = relative_to
jxl_joint_i_8.marker_name = '.turn.gel_lwract.jxl_joint_i_8'
_turn_gel_upract_jxl_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.gel_upract.jxl_joint_j_8')
jxl_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upract_jxl_joint_j_8))
_turn_gel_upract_jxl_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.gel_upract.jxl_joint_j_8')
jxl_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upract_jxl_joint_j_8))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_8.location, jxl_joint_i_8.orientation)
jxl_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uel_stopper_i_2 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.uel_stopper_i_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lwract')
uel_stopper_i_2.relative_to = relative_to
uel_stopper_i_2.marker_name = '.turn.gel_lwract.uel_stopper_i_2'
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1')
uel_stopper_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_lwract_uc_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_i_2.location, uel_stopper_i_2.orientation)
uel_stopper_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uel_actuator_j_1 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.uel_actuator_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lwract')
uel_actuator_j_1.relative_to = relative_to
uel_actuator_j_1.marker_name = '.turn.gel_lwract.uel_actuator_j_1'
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1')
uel_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_lwract_uc_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_j_1.location, uel_actuator_j_1.orientation)
uel_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uel_actuator_i_2 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.uel_actuator_i_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_lwract')
uel_actuator_i_2.relative_to = relative_to
uel_actuator_i_2.marker_name = '.turn.gel_lwract.uel_actuator_i_2'
_turn_gel_lwract_jxl_joint_i_8 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.jxl_joint_i_8')
uel_actuator_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lwract_jxl_joint_i_8))
_turn_gel_lwract_jxl_joint_i_8 = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.jxl_joint_i_8')
uel_actuator_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_lwract_jxl_joint_i_8))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_i_2.location, uel_actuator_i_2.orientation)
uel_actuator_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
uel_actuator_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_lwract = Jusme.ActiveUSScene.getObject('.turn.gel_lwract.gralin_lwract')
gralin_lwract.cylinder_name = '.turn.gel_lwract.gralin_lwract'
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1').location
_turn_ground_cfl_lwract_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lwract_top').location
gralin_lwract.length = (VecUtils.DM(_turn_ground_hpl_lwract_uc_atch_1, _turn_ground_cfl_lwract_top))


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lwract')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_lwract.inertia_frame'
_turn_ger_lwract_cm = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lwract_cm))
_turn_ger_lwract = Jusme.ActiveUSScene.getObject('.turn.ger_lwract')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lwract))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_10 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.gralin_10')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lwract')
gralin_10.relative_to = relative_to
gralin_10.marker_name = '.turn.ger_lwract.gralin_10'
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1')
gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_lwract_uc_atch_1))
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1').location
_turn_ground_cfr_lwract_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lwract_top').location
gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_lwract_uc_atch_1, _turn_ground_cfr_lwract_top, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_j_7 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.jxr_joint_j_7')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lwract')
jxr_joint_j_7.relative_to = relative_to
jxr_joint_j_7.marker_name = '.turn.ger_lwract.jxr_joint_j_7'
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1')
jxr_joint_j_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_lwract_uc_atch_1))
_turn_ground_origo = Jusme.ActiveUSScene.getObject('.turn.ground.origo')
jxr_joint_j_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_origo))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_7.location, jxr_joint_j_7.orientation)
jxr_joint_j_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_j_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_i_8 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.jxr_joint_i_8')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lwract')
jxr_joint_i_8.relative_to = relative_to
jxr_joint_i_8.marker_name = '.turn.ger_lwract.jxr_joint_i_8'
_turn_ger_upract_jxr_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.ger_upract.jxr_joint_j_8')
jxr_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upract_jxr_joint_j_8))
_turn_ger_upract_jxr_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.ger_upract.jxr_joint_j_8')
jxr_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upract_jxr_joint_j_8))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_8.location, jxr_joint_i_8.orientation)
jxr_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uer_stopper_i_2 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.uer_stopper_i_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lwract')
uer_stopper_i_2.relative_to = relative_to
uer_stopper_i_2.marker_name = '.turn.ger_lwract.uer_stopper_i_2'
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1')
uer_stopper_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_lwract_uc_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_stopper_i_2.location, uer_stopper_i_2.orientation)
uer_stopper_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uer_actuator_i_2 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.uer_actuator_i_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lwract')
uer_actuator_i_2.relative_to = relative_to
uer_actuator_i_2.marker_name = '.turn.ger_lwract.uer_actuator_i_2'
_turn_ger_lwract_jxr_joint_i_8 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.jxr_joint_i_8')
uer_actuator_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lwract_jxr_joint_i_8))
_turn_ger_lwract_jxr_joint_i_8 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.jxr_joint_i_8')
uer_actuator_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_lwract_jxr_joint_i_8))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_i_2.location, uer_actuator_i_2.orientation)
uer_actuator_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
uer_actuator_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uer_actuator_j_1 = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.uer_actuator_j_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_lwract')
uer_actuator_j_1.relative_to = relative_to
uer_actuator_j_1.marker_name = '.turn.ger_lwract.uer_actuator_j_1'
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1')
uer_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_lwract_uc_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_j_1.location, uer_actuator_j_1.orientation)
uer_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


gralin_lwract = Jusme.ActiveUSScene.getObject('.turn.ger_lwract.gralin_lwract')
gralin_lwract.cylinder_name = '.turn.ger_lwract.gralin_lwract'
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1').location
_turn_ground_cfr_lwract_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lwract_top').location
gralin_lwract.length = (VecUtils.DM(_turn_ground_hpr_lwract_uc_atch_1, _turn_ground_cfr_lwract_top))


uel_actuator_i_1 = Jusme.ActiveUSScene.getObject('.turn.gel_upract.uel_actuator_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upract')
uel_actuator_i_1.relative_to = relative_to
uel_actuator_i_1.marker_name = '.turn.gel_upract.uel_actuator_i_1'
_turn_ground_hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_upract_sf_atch_1')
uel_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_upract_sf_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_i_1.location, uel_actuator_i_1.orientation)
uel_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.gel_upract.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upract')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.gel_upract.inertia_frame'
_turn_gel_upract_cm = Jusme.ActiveUSScene.getObject('.turn.gel_upract.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upract_cm))
_turn_gel_upract = Jusme.ActiveUSScene.getObject('.turn.gel_upract')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upract))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_18 = Jusme.ActiveUSScene.getObject('.turn.gel_upract.gralin_18')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upract')
gralin_18.relative_to = relative_to
gralin_18.marker_name = '.turn.gel_upract.gralin_18'
_turn_ground_cfl_upract_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_upract_bot')
gralin_18.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_upract_bot))
_turn_ground_cfl_upract_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_upract_bot').location
_turn_ground_hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_upract_sf_atch_1').location
gralin_18.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_cfl_upract_bot, _turn_ground_hpl_upract_sf_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_18.location, gralin_18.orientation)
gralin_18.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_18.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxl_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.gel_upract.jxl_joint_j_8')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upract')
jxl_joint_j_8.relative_to = relative_to
jxl_joint_j_8.marker_name = '.turn.gel_upract.jxl_joint_j_8'
_turn_ground_cfl_lwract_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_lwract_top')
jxl_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfl_lwract_top))
_turn_ground_hpl_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_lwract_uc_atch_1').location
_turn_ground_hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_upract_sf_atch_1').location
jxl_joint_j_8.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpl_lwract_uc_atch_1, _turn_ground_hpl_upract_sf_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_8.location, jxl_joint_j_8.orientation)
jxl_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxl_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uel_stopper_j_2 = Jusme.ActiveUSScene.getObject('.turn.gel_upract.uel_stopper_j_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upract')
uel_stopper_j_2.relative_to = relative_to
uel_stopper_j_2.marker_name = '.turn.gel_upract.uel_stopper_j_2'
_turn_ground_hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_upract_sf_atch_1')
uel_stopper_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpl_upract_sf_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_j_2.location, uel_stopper_j_2.orientation)
uel_stopper_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uel_actuator_j_2 = Jusme.ActiveUSScene.getObject('.turn.gel_upract.uel_actuator_j_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.gel_upract')
uel_actuator_j_2.relative_to = relative_to
uel_actuator_j_2.marker_name = '.turn.gel_upract.uel_actuator_j_2'
_turn_gel_upract_jxl_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.gel_upract.jxl_joint_j_8')
uel_actuator_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upract_jxl_joint_j_8))
_turn_gel_upract_jxl_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.gel_upract.jxl_joint_j_8')
uel_actuator_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_gel_upract_jxl_joint_j_8))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_j_2.location, uel_actuator_j_2.orientation)
uel_actuator_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
uel_actuator_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_upract = Jusme.ActiveUSScene.getObject('.turn.gel_upract.gralin_upract')
gralin_upract.cylinder_name = '.turn.gel_upract.gralin_upract'
_turn_ground_cfl_upract_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfl_upract_bot').location
_turn_ground_hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpl_upract_sf_atch_1').location
gralin_upract.length = (VecUtils.DM(_turn_ground_cfl_upract_bot, _turn_ground_hpl_upract_sf_atch_1))


uer_actuator_i_1 = Jusme.ActiveUSScene.getObject('.turn.ger_upract.uer_actuator_i_1')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upract')
uer_actuator_i_1.relative_to = relative_to
uer_actuator_i_1.marker_name = '.turn.ger_upract.uer_actuator_i_1'
_turn_ground_hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_upract_sf_atch_1')
uer_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_upract_sf_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_i_1.location, uer_actuator_i_1.orientation)
uer_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


inertia_frame = Jusme.ActiveUSScene.getObject('.turn.ger_upract.inertia_frame')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upract')
inertia_frame.relative_to = relative_to
inertia_frame.marker_name = '.turn.ger_upract.inertia_frame'
_turn_ger_upract_cm = Jusme.ActiveUSScene.getObject('.turn.ger_upract.cm')
inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upract_cm))
_turn_ger_upract = Jusme.ActiveUSScene.getObject('.turn.ger_upract')
inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upract))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_19 = Jusme.ActiveUSScene.getObject('.turn.ger_upract.gralin_19')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upract')
gralin_19.relative_to = relative_to
gralin_19.marker_name = '.turn.ger_upract.gralin_19'
_turn_ground_cfr_upract_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_upract_bot')
gralin_19.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_upract_bot))
_turn_ground_cfr_upract_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_upract_bot').location
_turn_ground_hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_upract_sf_atch_1').location
gralin_19.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_cfr_upract_bot, _turn_ground_hpr_upract_sf_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_19.location, gralin_19.orientation)
gralin_19.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
gralin_19.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


jxr_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.ger_upract.jxr_joint_j_8')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upract')
jxr_joint_j_8.relative_to = relative_to
jxr_joint_j_8.marker_name = '.turn.ger_upract.jxr_joint_j_8'
_turn_ground_cfr_lwract_top = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_lwract_top')
jxr_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_cfr_lwract_top))
_turn_ground_hpr_lwract_uc_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_lwract_uc_atch_1').location
_turn_ground_hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_upract_sf_atch_1').location
jxr_joint_j_8.orientation = (VecUtils.ORI_ALONG_AXIS(_turn_ground_hpr_lwract_uc_atch_1, _turn_ground_hpr_upract_sf_atch_1, "Z"))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_8.location, jxr_joint_j_8.orientation)
jxr_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
jxr_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


uer_stopper_j_2 = Jusme.ActiveUSScene.getObject('.turn.ger_upract.uer_stopper_j_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upract')
uer_stopper_j_2.relative_to = relative_to
uer_stopper_j_2.marker_name = '.turn.ger_upract.uer_stopper_j_2'
_turn_ground_hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_upract_sf_atch_1')
uer_stopper_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ground_hpr_upract_sf_atch_1))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_stopper_j_2.location, uer_stopper_j_2.orientation)
uer_stopper_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


uer_actuator_j_2 = Jusme.ActiveUSScene.getObject('.turn.ger_upract.uer_actuator_j_2')
relative_to = Jusme.ActiveUSScene.getObject('.turn.ger_upract')
uer_actuator_j_2.relative_to = relative_to
uer_actuator_j_2.marker_name = '.turn.ger_upract.uer_actuator_j_2'
_turn_ger_upract_jxr_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.ger_upract.jxr_joint_j_8')
uer_actuator_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upract_jxr_joint_j_8))
_turn_ger_upract_jxr_joint_j_8 = Jusme.ActiveUSScene.getObject('.turn.ger_upract.jxr_joint_j_8')
uer_actuator_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _turn_ger_upract_jxr_joint_j_8))
loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_j_2.location, uer_actuator_j_2.orientation)
uer_actuator_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
uer_actuator_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


gralin_upract = Jusme.ActiveUSScene.getObject('.turn.ger_upract.gralin_upract')
gralin_upract.cylinder_name = '.turn.ger_upract.gralin_upract'
_turn_ground_cfr_upract_bot = Jusme.ActiveUSScene.getObject('.turn.ground.cfr_upract_bot').location
_turn_ground_hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.turn.ground.hpr_upract_sf_atch_1').location
gralin_upract.length = (VecUtils.DM(_turn_ground_cfr_upract_bot, _turn_ground_hpr_upract_sf_atch_1))



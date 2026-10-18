!
!-------------------------- Default Units for Model ---------------------------!
!
!
defaults units  &
   length = meter  &
   angle = deg  &
   force = newton  &
   mass = kg  &
   time = sec
!
defaults units  &
   coordinate_system_type = cartesian  &
   orientation_type = body313
!
!------------------------ Default Attributes for Model ------------------------!
!
!
defaults attributes  &
   inheritance = bottom_up  &
   icon_visibility = on  &
   grid_visibility = off  &
   size_of_icons = 5.0E-02  &
   spacing_for_grid = 2.54E-02
!
!------------------------------ Adams View Model ------------------------------!
!
!
model create  &
   model_name = turn  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .turn  &
   size_of_icons = 5.0E-02
!
view erase
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .turn.aluminum  &
   adams_id = 2  &
   density = 2740.0  &
   youngs_modulus = 7.1705E+10  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .turn.steel  &
   adams_id = 5  &
   density = 7801.0  &
   youngs_modulus = 2.07E+11  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .turn.steel_2  &
   adams_id = 3  &
   density = 7801.0  &
   youngs_modulus = 2.07E+11  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .turn.aluminum_2  &
   adams_id = 4  &
   density = 2740.0  &
   youngs_modulus = 7.1705E+10  &
   poissons_ratio = 0.33
!
!-------------------------------- Rigid Parts ---------------------------------!
!
! Create parts and their dependent markers and graphics
!
!----------------------------------- ground -----------------------------------!
!
!
! ****** Ground Part ******
!
defaults model  &
   part_name = ground
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ground.origo  &
   adams_id = 1  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.origo  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfs_subframe_ref  &
   adams_id = 3  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 180.0d, 90.0d, 177.5464650677d
!
marker attributes  &
   marker_name = .turn.ground.cfs_subframe_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_spin_axis  &
   adams_id = 4  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 179.9999064666d, 88.9999687773d, 5.3591761151E-03d
!
marker attributes  &
   marker_name = .turn.ground.cfl_spin_axis  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_spin_axis  &
   adams_id = 5  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 9.3533439964E-05d, 88.9999687773d, 179.9946408239d
!
marker attributes  &
   marker_name = .turn.ground.cfr_spin_axis  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_torque_arm_refplane  &
   adams_id = 6  &
   location = 12.5098362975, -1.6395888469, 0.5076864953  &
   orientation = 55.1145661544d, 175.2828647294d, 80.2814243968d
!
marker attributes  &
   marker_name = .turn.ground.cfl_torque_arm_refplane  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_torque_arm_refplane  &
   adams_id = 7  &
   location = 12.5098362975, 1.6395888469, 0.5076864953  &
   orientation = 124.8854338456d, 175.2828647294d, 99.7185756032d
!
marker attributes  &
   marker_name = .turn.ground.cfr_torque_arm_refplane  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_dragbrace_refplane  &
   adams_id = 8  &
   location = 12.070313934, -1.5107420843, 1.6281029812  &
   orientation = 238.6248285507d, 75.5183095506d, 100.5979151393d
!
marker attributes  &
   marker_name = .turn.ground.cfl_dragbrace_refplane  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_dragbrace_refplane  &
   adams_id = 9  &
   location = 12.070313934, 1.5107420843, 1.6281029812  &
   orientation = 301.3751714493d, 75.5183095506d, 79.4020848607d
!
marker attributes  &
   marker_name = .turn.ground.cfr_dragbrace_refplane  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_uc_sf_atch  &
   adams_id = 10  &
   location = 12.1457499909, -1.2447481722, 2.1230446312  &
   orientation = 357.5219193201d, 81.1274829118d, 15.673741043d
!
marker attributes  &
   marker_name = .turn.ground.cfl_uc_sf_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_uc_sf_atch  &
   adams_id = 11  &
   location = 12.1457499909, 1.2447481722, 2.1230446312  &
   orientation = 182.4780806799d, 81.1274829118d, 164.326258957d
!
marker attributes  &
   marker_name = .turn.ground.cfr_uc_sf_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_axial_reference  &
   adams_id = 13  &
   location = 12.2709748205, -1.5322348019, 0.1791298424  &
   orientation = 235.1145661682d, 4.7171352712d, 124.7942832293d
!
marker attributes  &
   marker_name = .turn.ground.cfl_axial_reference  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_axial_reference  &
   adams_id = 14  &
   location = 12.2709748205, 1.5322348019, 0.1791298424  &
   orientation = 304.8854338318d, 4.7171352712d, 55.2057167707d
!
marker attributes  &
   marker_name = .turn.ground.cfr_axial_reference  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_uc_bot  &
   adams_id = 15  &
   location = 12.2346840721, -1.5069317388, 0.7152796436  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfl_uc_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_uc_bot  &
   adams_id = 16  &
   location = 12.2346840721, 1.5069317388, 0.7152796436  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfr_uc_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_uc_top  &
   adams_id = 17  &
   location = 12.137340597, -1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfl_uc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_uc_top  &
   adams_id = 18  &
   location = 12.137340597, 1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfr_uc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_lc_top  &
   adams_id = 19  &
   location = 12.2057611337, -1.486765747, 1.1425793908  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfl_lc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_lc_top  &
   adams_id = 20  &
   location = 12.2057611337, 1.486765747, 1.1425793908  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfr_lc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_uta_uc_atch  &
   adams_id = 21  &
   location = 12.2346840721, -1.5069317388, 0.7152796436  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfl_uta_uc_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_uta_uc_atch  &
   adams_id = 22  &
   location = 12.2346840721, 1.5069317388, 0.7152796436  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfr_uta_uc_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_lta_lc_atch  &
   adams_id = 23  &
   location = 12.2709748205, -1.5322348019, 0.1791298424  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfl_lta_lc_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_lta_lc_atch  &
   adams_id = 24  &
   location = 12.2709748205, 1.5322348019, 0.1791298424  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfr_lta_lc_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_collar_top  &
   adams_id = 25  &
   location = 12.2161847889, -1.4940334506, 0.9885831006  &
   orientation = 55.1145661682d, 175.2828647288d, 235.2057167707d
!
marker attributes  &
   marker_name = .turn.ground.cfl_collar_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_collar_top  &
   adams_id = 26  &
   location = 12.2161847889, 1.4940334506, 0.9885831006  &
   orientation = 124.8854338318d, 175.2828647288d, 304.7942832293d
!
marker attributes  &
   marker_name = .turn.ground.cfr_collar_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_collar_bot  &
   adams_id = 27  &
   location = 12.2308845535, -1.5042825936, 0.7714127142  &
   orientation = 55.1145661682d, 175.2828647288d, 235.2057167707d
!
marker attributes  &
   marker_name = .turn.ground.cfl_collar_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_collar_bot  &
   adams_id = 28  &
   location = 12.2308845535, 1.5042825936, 0.7714127142  &
   orientation = 124.8854338318d, 175.2828647288d, 304.7942832293d
!
marker attributes  &
   marker_name = .turn.ground.cfr_collar_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_plane_ref  &
   adams_id = 29  &
   location = 11.7904549128, -1.3312381859, 1.4785418122  &
   orientation = 70.4651741872d, 87.6875364203d, 268.7516172662d
!
marker attributes  &
   marker_name = .turn.ground.cfl_plane_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_plane_ref  &
   adams_id = 30  &
   location = 11.7904549128, 1.3312381859, 1.4785418122  &
   orientation = 109.5348258128d, 87.6875364203d, 271.2483827338d
!
marker attributes  &
   marker_name = .turn.ground.cfr_plane_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_plane_ref_2  &
   adams_id = 31  &
   location = 11.7904549128, -1.3312381859, 1.4785418122  &
   orientation = 160.4147950495d, 91.2473659421d, 267.6869880055d
!
marker attributes  &
   marker_name = .turn.ground.cfl_plane_ref_2  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_plane_ref_2  &
   adams_id = 32  &
   location = 11.7904549128, 1.3312381859, 1.4785418122  &
   orientation = 19.5852049505d, 91.2473659421d, 272.3130119945d
!
marker attributes  &
   marker_name = .turn.ground.cfr_plane_ref_2  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_lwract_top  &
   adams_id = 33  &
   location = 12.301784069, -1.2914705743, 1.9010842639  &
   orientation = 182.4778087702d, 7.7973026753d, 177.4990974089d
!
marker attributes  &
   marker_name = .turn.ground.cfl_lwract_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_lwract_top  &
   adams_id = 34  &
   location = 12.301784069, 1.2914705743, 1.9010842639  &
   orientation = 357.5221912298d, 7.7973026753d, 2.5009025911d
!
marker attributes  &
   marker_name = .turn.ground.cfr_lwract_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_upract_bot  &
   adams_id = 35  &
   location = 12.3037747523, -1.337473576, 1.5648221485  &
   orientation = 182.4778087702d, 7.7973026753d, 177.4990974089d
!
marker attributes  &
   marker_name = .turn.ground.cfl_upract_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_upract_bot  &
   adams_id = 36  &
   location = 12.3037747523, 1.337473576, 1.5648221485  &
   orientation = 357.5221912298d, 7.7973026753d, 2.5009025911d
!
marker attributes  &
   marker_name = .turn.ground.cfr_upract_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_spin_axis_1  &
   adams_id = 37  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 359.9999064666d, 91.0000312227d, 179.9946408239d
!
marker attributes  &
   marker_name = .turn.ground.cfl_spin_axis_1  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_spin_axis_1  &
   adams_id = 38  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 180.0000935334d, 91.0000312227d, 5.3591761151E-03d
!
marker attributes  &
   marker_name = .turn.ground.cfr_spin_axis_1  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_ldb_geompt_1  &
   adams_id = 39  &
   location = 11.8912081251, -1.3781308467, 1.1458304614  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfl_ldb_geompt_1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_ldb_geompt_1  &
   adams_id = 40  &
   location = 11.8912081251, 1.3781308467, 1.1458304614  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfr_ldb_geompt_1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_ldb_geompt_2  &
   adams_id = 41  &
   location = 11.9606643032, -1.4050660792, 1.0737874161  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfl_ldb_geompt_2  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_ldb_geompt_2  &
   adams_id = 42  &
   location = 11.9606643032, 1.4050660792, 1.0737874161  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfr_ldb_geompt_2  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_aero_ref  &
   adams_id = 43  &
   location = 12.137340597, -1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfl_aero_ref  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_aero_ref  &
   adams_id = 44  &
   location = 12.137340597, 1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfr_aero_ref  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.uel_gearaero_origin_1  &
   adams_id = 45  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.uel_gearaero_origin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.uel_gearaero_rm_1  &
   adams_id = 46  &
   location = 12.137340597, -1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.uel_gearaero_rm_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.uer_gearaero_origin_1  &
   adams_id = 47  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.uer_gearaero_origin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.uer_gearaero_rm_1  &
   adams_id = 48  &
   location = 12.137340597, 1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.uer_gearaero_rm_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.origo1  &
   adams_id = 287  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.origo1  &
   size_of_icons = 5.0E-02
!
! ****** Points for current part ******
!
point create  &
   point_name = .turn.ground.hpl_udb_spndl_atch_1  &
   location = 10.963049321, -1.0224189813, 2.1030895124
!
point attributes  &
   point_name = .turn.ground.hpl_udb_spndl_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_udb_spndl_atch_1  &
   location = 10.963049321, 1.0224189813, 2.1030895124
!
point attributes  &
   point_name = .turn.ground.hpr_udb_spndl_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_ib_uc_sf_atch  &
   location = 12.1541593848, -1.0504355699, 2.0926831806
!
point attributes  &
   point_name = .turn.ground.hpl_ib_uc_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_ib_uc_sf_atch  &
   location = 12.1541593848, 1.0504355699, 2.0926831806
!
point attributes  &
   point_name = .turn.ground.hpr_ib_uc_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_wheel_center  &
   location = 12.2709739569, -1.8115919597, 0.1742595194
!
point attributes  &
   point_name = .turn.ground.hpl_wheel_center  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_wheel_center  &
   location = 12.2709739569, 1.8115919597, 0.1742595194
!
point attributes  &
   point_name = .turn.ground.hpr_wheel_center  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_lc_bot  &
   location = 12.2709748205, -1.5322348019, 0.1791298424
!
point attributes  &
   point_name = .turn.ground.hpl_lc_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_lc_bot  &
   location = 12.2709748205, 1.5322348019, 0.1791298424
!
point attributes  &
   point_name = .turn.ground.hpr_lc_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_ob_axle  &
   location = 12.2709737181, -1.9578736763, 0.1717060828
!
point attributes  &
   point_name = .turn.ground.hpl_ob_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_ob_axle  &
   location = 12.2709737181, 1.9578736763, 0.1717060828
!
point attributes  &
   point_name = .turn.ground.hpr_ob_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_ib_axle  &
   location = 12.2709748205, -1.532234807, 0.1791298424
!
point attributes  &
   point_name = .turn.ground.hpl_ib_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_ib_axle  &
   location = 12.2709748205, 1.532234807, 0.1791298424
!
point attributes  &
   point_name = .turn.ground.hpr_ib_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_uc_top  &
   location = 12.137340597, -1.4390607744, 2.1534060818
!
point attributes  &
   point_name = .turn.ground.hpl_uc_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_uc_top  &
   location = 12.137340597, 1.4390607744, 2.1534060818
!
point attributes  &
   point_name = .turn.ground.hpr_uc_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_uc_geompt  &
   location = 12.1670316222, -1.3594512257, 1.7617947238
!
point attributes  &
   point_name = .turn.ground.hpl_uc_geompt  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_uc_geompt  &
   location = 12.1670316222, 1.3594512257, 1.7617947238
!
point attributes  &
   point_name = .turn.ground.hpr_uc_geompt  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_stator_attach  &
   location = 12.2709740483, -1.7544506694, 0.175256952
!
point attributes  &
   point_name = .turn.ground.hpl_stator_attach  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_stator_attach  &
   location = 12.2709740483, 1.7544506694, 0.175256952
!
point attributes  &
   point_name = .turn.ground.hpr_stator_attach  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_ldb_uc_atch  &
   location = 12.54125, -1.8542, 1.21285
!
point attributes  &
   point_name = .turn.ground.hpl_ldb_uc_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_ldb_uc_atch  &
   location = 12.54125, 1.8542, 1.21285
!
point attributes  &
   point_name = .turn.ground.hpr_ldb_uc_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_ldb_udb_atch_1  &
   location = 11.532351205, -1.2389654784, 1.5180528618
!
point attributes  &
   point_name = .turn.ground.hpl_ldb_udb_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_ldb_udb_atch_1  &
   location = 11.532351205, 1.2389654784, 1.5180528618
!
point attributes  &
   point_name = .turn.ground.hpr_ldb_udb_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_lta_uta_atch  &
   location = 13.02385, -1.8796, 0.62865
!
point attributes  &
   point_name = .turn.ground.hpl_lta_uta_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_lta_uta_atch  &
   location = 13.02385, 1.8796, 0.62865
!
point attributes  &
   point_name = .turn.ground.hpr_lta_uta_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_lta_connect_atch_1  &
   location = 12.048547912, -1.5622090168, 0.5321183668
!
point attributes  &
   point_name = .turn.ground.hpl_lta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_lta_connect_atch_1  &
   location = 12.048547912, 1.5622090168, 0.5321183668
!
point attributes  &
   point_name = .turn.ground.hpr_lta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_uta_connect_atch_1  &
   location = 12.0522523496, -1.4912788564, 0.5290216242
!
point attributes  &
   point_name = .turn.ground.hpl_uta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_uta_connect_atch_1  &
   location = 12.0522523496, 1.4912788564, 0.5290216242
!
point attributes  &
   point_name = .turn.ground.hpr_uta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_uta_connect_atch_2  &
   location = 12.087047708, -1.4934025504, 0.5220012166
!
point attributes  &
   point_name = .turn.ground.hpl_uta_connect_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_uta_connect_atch_2  &
   location = 12.087047708, 1.4934025504, 0.5220012166
!
point attributes  &
   point_name = .turn.ground.hpr_uta_connect_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_lta_lc_atch_1  &
   location = 12.150137371, -1.5536660062, 0.2740663556
!
point attributes  &
   point_name = .turn.ground.hpl_lta_lc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_lta_lc_atch_1  &
   location = 12.150137371, 1.5536660062, 0.2740663556
!
point attributes  &
   point_name = .turn.ground.hpr_lta_lc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_lta_lc_atch_2  &
   location = 12.1525627408, -1.5072279736, 0.2720389276
!
point attributes  &
   point_name = .turn.ground.hpl_lta_lc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_lta_lc_atch_2  &
   location = 12.1525627408, 1.5072279736, 0.2720389276
!
point attributes  &
   point_name = .turn.ground.hpr_lta_lc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_uta_collar_atch_1  &
   location = 12.1066524694, -1.4965360468, 0.800236779
!
point attributes  &
   point_name = .turn.ground.hpl_uta_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_uta_collar_atch_1  &
   location = 12.1066524694, 1.4965360468, 0.800236779
!
point attributes  &
   point_name = .turn.ground.hpr_uta_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_uta_collar_atch_2  &
   location = 12.1102139304, -1.428342457, 0.797259518
!
point attributes  &
   point_name = .turn.ground.hpl_uta_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_uta_collar_atch_2  &
   location = 12.1102139304, 1.428342457, 0.797259518
!
point attributes  &
   point_name = .turn.ground.hpr_uta_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_collar_top  &
   location = 12.216682831, -1.4943808822, 0.9812211008
!
point attributes  &
   point_name = .turn.ground.hpl_collar_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_collar_top  &
   location = 12.216682831, 1.4943808822, 0.9812211008
!
point attributes  &
   point_name = .turn.ground.hpr_collar_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_collar_bot  &
   location = 12.2313550394, -1.5046108084, 0.7644576024
!
point attributes  &
   point_name = .turn.ground.hpl_collar_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_collar_bot  &
   location = 12.2313550394, 1.5046108084, 0.7644576024
!
point attributes  &
   point_name = .turn.ground.hpr_collar_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_upr_strt_bot  &
   location = 12.2327072846, -1.5055538596, 0.7444805024
!
point attributes  &
   point_name = .turn.ground.hpl_upr_strt_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_upr_strt_bot  &
   location = 12.2327072846, 1.5055538596, 0.7444805024
!
point attributes  &
   point_name = .turn.ground.hpr_upr_strt_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_upr_strt_top  &
   location = 12.1478181986, -1.4463662462, 1.9986101506
!
point attributes  &
   point_name = .turn.ground.hpl_upr_strt_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_upr_strt_top  &
   location = 12.1478181986, 1.4463662462, 1.9986101506
!
point attributes  &
   point_name = .turn.ground.hpr_upr_strt_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_lwract_uc_atch_1  &
   location = 12.3053060472, -1.3728605004, 1.3061589828
!
point attributes  &
   point_name = .turn.ground.hpl_lwract_uc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_lwract_uc_atch_1  &
   location = 12.3053060472, 1.3728605004, 1.3061589828
!
point attributes  &
   point_name = .turn.ground.hpr_lwract_uc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_lwract_uc_atch_2  &
   location = 12.306350165, -1.3555888052, 1.3038056982
!
point attributes  &
   point_name = .turn.ground.hpl_lwract_uc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_lwract_uc_atch_2  &
   location = 12.306350165, 1.3555888052, 1.3038056982
!
point attributes  &
   point_name = .turn.ground.hpr_lwract_uc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_upract_sf_atch_1  &
   location = 12.30147781, -1.2843931894, 1.952816897
!
point attributes  &
   point_name = .turn.ground.hpl_upract_sf_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_upract_sf_atch_1  &
   location = 12.30147781, 1.2843931894, 1.952816897
!
point attributes  &
   point_name = .turn.ground.hpr_upract_sf_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_upract_sf_atch_2  &
   location = 12.303675418, -1.2504491628, 1.9481928778
!
point attributes  &
   point_name = .turn.ground.hpl_upract_sf_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_upract_sf_atch_2  &
   location = 12.303675418, 1.2504491628, 1.9481928778
!
point attributes  &
   point_name = .turn.ground.hpr_upract_sf_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_spndl_sf_atch  &
   location = 10.777681391, -0.9566499282, 2.0951467876
!
point attributes  &
   point_name = .turn.ground.hpl_spndl_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_spndl_sf_atch  &
   location = 10.777681391, 0.9566499282, 2.0951467876
!
point attributes  &
   point_name = .turn.ground.hpr_spndl_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_connect_1  &
   location = 12.045992164, -1.6111431582, 0.5342547862
!
point attributes  &
   point_name = .turn.ground.hpl_connect_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_connect_1  &
   location = 12.045992164, 1.6111431582, 0.5342547862
!
point attributes  &
   point_name = .turn.ground.hpr_connect_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_ldb_udb_atch_2  &
   location = 11.5117089298, -1.2969830804, 1.51939371
!
point attributes  &
   point_name = .turn.ground.hpl_ldb_udb_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_ldb_udb_atch_2  &
   location = 11.5117089298, 1.2969830804, 1.51939371
!
point attributes  &
   point_name = .turn.ground.hpr_ldb_udb_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_ldb_collar_atch_1  &
   location = 12.111152689, -1.4634257498, 0.9176941514
!
point attributes  &
   point_name = .turn.ground.hpl_ldb_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_ldb_collar_atch_1  &
   location = 12.111152689, 1.4634257498, 0.9176941514
!
point attributes  &
   point_name = .turn.ground.hpr_ldb_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_ldb_collar_atch_2  &
   location = 12.0829855622, -1.5425928508, 0.9195237896
!
point attributes  &
   point_name = .turn.ground.hpl_ldb_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_ldb_collar_atch_2  &
   location = 12.0829855622, 1.5425928508, 0.9195237896
!
point attributes  &
   point_name = .turn.ground.hpr_ldb_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_uplock_tab  &
   location = 11.9014828772, -1.2751123164, 1.0332048729
!
point attributes  &
   point_name = .turn.ground.hpl_uplock_tab  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_uplock_tab  &
   location = 11.9014828772, 1.2751123164, 1.0332048729
!
point attributes  &
   point_name = .turn.ground.hpr_uplock_tab  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_origin_reference  &
   location = 0.0, 0.0, 0.0
!
point attributes  &
   point_name = .turn.ground.hps_origin_reference  &
   size_of_icons = 5.0E-02
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .turn.ground  &
   size_of_icons = 5.0E-02
!
!----------------------------- gel_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_upper_cylinder  &
   adams_id = 4  &
   location = 12.1860123345, -1.4729962566, 1.4343428627  &
   orientation = 55.1145661544d, 175.2828647294d, 235.2057167569d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.uel_gearaero_i_1  &
   adams_id = 69  &
   location = -3.3904410529E-11, 1.7865427887E-11, 0.2927550811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.uel_gearaero_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.cm  &
   adams_id = 71  &
   location = -2.0756301703E-04, 6.4023904007E-03, -1.4668262126E-02  &
   orientation = 1.8568667884d, 1.160957641d, 3.871847135E-06d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.inertia_frame  &
   adams_id = 72  &
   location = -2.0756301703E-04, 6.4023904007E-03, -1.4668262126E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.gralin_12  &
   adams_id = 73  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.gralin_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.gralin_16  &
   adams_id = 74  &
   location = -1.2679580771E-02, 0.391098059, -0.6781339507  &
   orientation = 1.8570008795d, 40.3514751572d, 357.5638844649d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.gralin_16  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.gralin_20  &
   adams_id = 75  &
   location = -1.2679580771E-02, 0.391098059, -0.6781339507  &
   orientation = 1.8569053817d, 96.3249984441d, 196.3982135132d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.gralin_20  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.jxl_joint_j_12  &
   adams_id = 76  &
   location = 0.0, 0.0, 0.5071310811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.jxl_joint_j_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.uel_spring_j_1  &
   adams_id = 78  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.uel_spring_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.uel_damper_j_1  &
   adams_id = 79  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.uel_damper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.uel_stopper_j_1  &
   adams_id = 80  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.uel_stopper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.jxl_joint_j_4  &
   adams_id = 81  &
   location = 0.0, 0.0, 0.5562289935  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.jxl_joint_j_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.jxl_joint_i_7  &
   adams_id = 82  &
   location = -0.1103647044, 0.1064191121, 0.1310872657  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.jxl_joint_i_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.uel_actuator_j_3  &
   adams_id = 83  &
   location = -6.3397903922E-03, 0.1955490294, -0.6998205159  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.uel_actuator_j_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.MARKER_267  &
   adams_id = 267  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.MARKER_267  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_cylinder.MARKER_272  &
   adams_id = 272  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .turn.gel_upper_cylinder.MARKER_272  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_upper_cylinder  &
   mass = 112.770857716  &
   center_of_mass_marker = .turn.gel_upper_cylinder.cm  &
   inertia_marker = .turn.gel_upper_cylinder.inertia_frame  &
   ixx = 20.3828607526  &
   iyy = 20.1915756173  &
   izz = 0.6770308822  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_upper_cylinder.gralin_upper_cylinder  &
   adams_id = 1  &
   center_marker = .turn.gel_upper_cylinder.gralin_12  &
   angle_extent = 360.0  &
   length = 1.4430141621  &
   radius = 9.398E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_upper_cylinder.gralin_upper_cylinder  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_upper_cylinder.gralin_geom  &
   adams_id = 2  &
   center_marker = .turn.gel_upper_cylinder.gralin_16  &
   angle_extent = 360.0  &
   length = 0.4529277435  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_upper_cylinder.gralin_geom  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_upper_cylinder.gralin_geom3  &
   adams_id = 3  &
   center_marker = .turn.gel_upper_cylinder.gralin_20  &
   angle_extent = 360.0  &
   length = 0.3937000024  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_upper_cylinder.gralin_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .turn.gel_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ger_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_upper_cylinder  &
   adams_id = 5  &
   location = 12.1860123345, 1.4729962566, 1.4343428627  &
   orientation = 124.8854338456d, 175.2828647294d, 304.7942832431d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.uer_gearaero_i_1  &
   adams_id = 84  &
   location = -3.3904427876E-11, -1.7865197169E-11, 0.2927550811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.uer_gearaero_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.cm  &
   adams_id = 85  &
   location = -2.0756301703E-04, -6.4023904007E-03, -1.4668262126E-02  &
   orientation = 178.1431332116d, 1.160957641d, 179.9999961282d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.inertia_frame  &
   adams_id = 86  &
   location = -2.0756301703E-04, -6.4023904007E-03, -1.4668262126E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.gralin_13  &
   adams_id = 87  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.gralin_13  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.gralin_17  &
   adams_id = 88  &
   location = -1.2679580771E-02, -0.391098059, -0.6781339507  &
   orientation = 178.1429991205d, 40.3514751572d, 182.4361155351d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.gralin_17  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.gralin_21  &
   adams_id = 89  &
   location = -1.2679580771E-02, -0.391098059, -0.6781339507  &
   orientation = 178.1430946183d, 96.3249984441d, 343.6017864868d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.gralin_21  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.jxr_joint_j_12  &
   adams_id = 90  &
   location = 0.0, 0.0, 0.5071310811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.jxr_joint_j_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.uer_spring_j_1  &
   adams_id = 92  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.uer_spring_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.uer_damper_j_1  &
   adams_id = 93  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.uer_damper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.uer_stopper_j_1  &
   adams_id = 94  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.uer_stopper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.jxr_joint_j_4  &
   adams_id = 95  &
   location = 0.0, 0.0, 0.5562289935  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.jxr_joint_j_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.jxr_joint_i_7  &
   adams_id = 96  &
   location = -0.1103647044, -0.1064191121, 0.1310872657  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.jxr_joint_i_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.uer_actuator_j_3  &
   adams_id = 97  &
   location = -6.3397903922E-03, -0.1955490294, -0.6998205159  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.uer_actuator_j_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.MARKER_269  &
   adams_id = 269  &
   location = -1.3212757277E-11, 0.0, -0.7215070811  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.MARKER_269  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_cylinder.MARKER_278  &
   adams_id = 278  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .turn.ger_upper_cylinder.MARKER_278  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_upper_cylinder  &
   mass = 112.770857716  &
   center_of_mass_marker = .turn.ger_upper_cylinder.cm  &
   inertia_marker = .turn.ger_upper_cylinder.inertia_frame  &
   ixx = 20.3828607526  &
   iyy = 20.1915756173  &
   izz = 0.6770308822  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_upper_cylinder.gralin_upper_cylinder  &
   adams_id = 4  &
   center_marker = .turn.ger_upper_cylinder.gralin_13  &
   angle_extent = 360.0  &
   length = 1.4430141621  &
   radius = 9.398E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_upper_cylinder.gralin_upper_cylinder  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_upper_cylinder.gralin_geom  &
   adams_id = 5  &
   center_marker = .turn.ger_upper_cylinder.gralin_17  &
   angle_extent = 360.0  &
   length = 0.4529277435  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_upper_cylinder.gralin_geom  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_upper_cylinder.gralin_geom3  &
   adams_id = 6  &
   center_marker = .turn.ger_upper_cylinder.gralin_21  &
   angle_extent = 360.0  &
   length = 0.3937000024  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_upper_cylinder.gralin_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .turn.ger_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- gel_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_lower_cylinder  &
   adams_id = 6  &
   location = 12.2383679771, -1.5095002745, 0.6608546166  &
   orientation = 55.1145661544d, 175.2828647294d, 235.2057167569d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.cm  &
   adams_id = 99  &
   location = 1.6535536877E-05, -1.3980732745E-02, 3.2717040657E-02  &
   orientation = 6.7765835809E-02d, 4.4745452767d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.inertia_frame  &
   adams_id = 100  &
   location = 1.6535536879E-05, -1.3980732745E-02, 3.2717040657E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.gralin_14  &
   adams_id = 101  &
   location = 0.0, 4.5291156242E-11, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.gralin_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.gralin_22  &
   adams_id = 102  &
   location = -2.2761403873E-11, -5.0394524422E-09, 0.4833620002  &
   orientation = 6.7765842413E-02d, 86.3072194254d, 358.9479604232d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.gralin_22  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.jxl_joint_j_11  &
   adams_id = 103  &
   location = 0.1141502171, -2.624637539E-02, 0.3816035459  &
   orientation = 182.811221391d, 89.9999933852d, 90.0001347091d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.jxl_joint_j_11  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.jxl_joint_i_12  &
   adams_id = 104  &
   location = 3.0868047701E-11, 2.7426356325E-11, -0.2689859999  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.jxl_joint_i_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.coomarker_1  &
   adams_id = 105  &
   location = 3.2976997546E-04, -0.2788194421, 0.5013550985  &
   orientation = 180.0677659365d, 93.6935934177d, 183.881448147d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.coomarker_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.uel_spring_i_1  &
   adams_id = 106  &
   location = 0.0, 4.5291156242E-11, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.uel_spring_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.uel_damper_i_1  &
   adams_id = 107  &
   location = 0.0, 4.5291156242E-11, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.uel_damper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.uel_stopper_i_1  &
   adams_id = 108  &
   location = 0.0, 4.5291156242E-11, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.uel_stopper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.MARKER_266  &
   adams_id = 266  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.MARKER_266  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_cylinder.MARKER_273  &
   adams_id = 273  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .turn.gel_lower_cylinder.MARKER_273  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_lower_cylinder  &
   mass = 217.3555691677  &
   center_of_mass_marker = .turn.gel_lower_cylinder.cm  &
   inertia_marker = .turn.gel_lower_cylinder.inertia_frame  &
   ixx = 3.3284494628  &
   iyy = 3.1936294  &
   izz = 0.2032330741  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_lower_cylinder.gralin_lower_cylinder  &
   adams_id = 7  &
   center_marker = .turn.gel_lower_cylinder.gralin_14  &
   angle_extent = 360.0  &
   length = 0.966724  &
   radius = 6.35E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_lower_cylinder.gralin_lower_cylinder  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_lower_cylinder.gralin_geom  &
   adams_id = 8  &
   center_marker = .turn.gel_lower_cylinder.gralin_22  &
   angle_extent = 360.0  &
   length = 0.4257036049  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_lower_cylinder.gralin_geom  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .turn.gel_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ger_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_lower_cylinder  &
   adams_id = 7  &
   location = 12.2383679771, 1.5095002745, 0.6608546166  &
   orientation = 124.8854338456d, 175.2828647294d, 304.7942832431d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.cm  &
   adams_id = 109  &
   location = 1.6535536877E-05, 1.3980732745E-02, 3.2717040657E-02  &
   orientation = 179.9322341642d, 4.4745452767d, 180.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.inertia_frame  &
   adams_id = 110  &
   location = 1.6535536881E-05, 1.3980732745E-02, 3.2717040657E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.gralin_15  &
   adams_id = 111  &
   location = 0.0, -4.5290927259E-11, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.gralin_15  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.gralin_23  &
   adams_id = 112  &
   location = -2.2761403873E-11, 5.0394524422E-09, 0.4833620002  &
   orientation = 179.9322341576d, 86.3072194254d, 181.0520395768d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.gralin_23  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.jxr_joint_j_11  &
   adams_id = 113  &
   location = 0.1141502171, 2.624637539E-02, 0.3816035459  &
   orientation = 357.188778609d, 89.9999933852d, 89.9998652909d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.jxr_joint_j_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.jxr_joint_i_12  &
   adams_id = 114  &
   location = 3.0868051171E-11, -2.742591397E-11, -0.2689859999  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.jxr_joint_i_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.coomarker_2  &
   adams_id = 115  &
   location = 3.2976997546E-04, 0.2788194421, 0.5013550985  &
   orientation = 359.9322340635d, 93.6935934177d, 356.118551853d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.coomarker_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.uer_spring_i_1  &
   adams_id = 116  &
   location = 0.0, -4.5290927259E-11, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.uer_spring_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.uer_damper_i_1  &
   adams_id = 117  &
   location = 0.0, -4.5290927259E-11, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.uer_damper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.uer_stopper_i_1  &
   adams_id = 118  &
   location = 0.0, -4.5290927259E-11, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.uer_stopper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.MARKER_268  &
   adams_id = 268  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.MARKER_268  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_cylinder.MARKER_279  &
   adams_id = 279  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .turn.ger_lower_cylinder.MARKER_279  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_lower_cylinder  &
   mass = 217.3555691677  &
   center_of_mass_marker = .turn.ger_lower_cylinder.cm  &
   inertia_marker = .turn.ger_lower_cylinder.inertia_frame  &
   ixx = 3.3284494628  &
   iyy = 3.1936294  &
   izz = 0.2032330741  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_lower_cylinder.gralin_lower_cylinder  &
   adams_id = 9  &
   center_marker = .turn.ger_lower_cylinder.gralin_15  &
   angle_extent = 360.0  &
   length = 0.966724  &
   radius = 6.35E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_lower_cylinder.gralin_lower_cylinder  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_lower_cylinder.gralin_geom  &
   adams_id = 10  &
   center_marker = .turn.ger_lower_cylinder.gralin_23  &
   angle_extent = 360.0  &
   length = 0.4257036049  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_lower_cylinder.gralin_geom  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .turn.ger_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_upper_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_upper_dragbrace  &
   adams_id = 8  &
   location = 11.247700263, -1.1306922298, 1.8105711871  &
   orientation = 69.1745865818d, 133.845797857d, 255.2385761183d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_upper_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_upper_dragbrace.cm  &
   adams_id = 119  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_dragbrace.inertia_frame  &
   adams_id = 120  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_dragbrace.gralin_24  &
   adams_id = 121  &
   location = 0.0, -2.7292432203E-11, -0.4222750594  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_dragbrace.gralin_24  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_dragbrace.jxl_joint_j_14  &
   adams_id = 122  &
   location = 0.0, -6.9364805566E-11, 0.4222750594  &
   orientation = 193.0027634258d, 90.0301580129d, 133.8272261428d
!
marker attributes  &
   marker_name = .turn.gel_upper_dragbrace.jxl_joint_j_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_dragbrace.jxl_joint_i_5  &
   adams_id = 123  &
   location = 0.0, -2.7292917926E-11, -0.4222750594  &
   orientation = 12.9738148964d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_dragbrace.jxl_joint_i_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_dragbrace.uel_actuator_i_3  &
   adams_id = 124  &
   location = 0.0, -6.9364805566E-11, 0.4222750594  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_dragbrace.uel_actuator_i_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_upper_dragbrace  &
   mass = 6.7539180723  &
   center_of_mass_marker = .turn.gel_upper_dragbrace.cm  &
   inertia_marker = .turn.gel_upper_dragbrace.inertia_frame  &
   ixx = 0.4030130421  &
   iyy = 0.4030130421  &
   izz = 3.1372976041E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_upper_dragbrace.gralin_upper_dragbrace  &
   adams_id = 11  &
   center_marker = .turn.gel_upper_dragbrace.gralin_24  &
   angle_extent = 360.0  &
   length = 0.8445501187  &
   radius = 3.048E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_upper_dragbrace.gralin_upper_dragbrace  &
   color = RED
!
part attributes  &
   part_name = .turn.gel_upper_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_upper_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_upper_dragbrace  &
   adams_id = 9  &
   location = 11.247700263, 1.1306922298, 1.8105711871  &
   orientation = 110.8254134182d, 133.845797857d, 284.7614238817d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_upper_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_upper_dragbrace.cm  &
   adams_id = 125  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_dragbrace.inertia_frame  &
   adams_id = 126  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_dragbrace.gralin_25  &
   adams_id = 127  &
   location = 0.0, 2.7292418325E-11, -0.4222750594  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_dragbrace.gralin_25  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_dragbrace.jxr_joint_j_14  &
   adams_id = 128  &
   location = 0.0, 6.9364819444E-11, 0.4222750594  &
   orientation = 346.9972365742d, 90.0301580129d, 46.1727738572d
!
marker attributes  &
   marker_name = .turn.ger_upper_dragbrace.jxr_joint_j_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_dragbrace.jxr_joint_i_5  &
   adams_id = 129  &
   location = 0.0, 2.7293250993E-11, -0.4222750594  &
   orientation = 347.0261851036d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_dragbrace.jxr_joint_i_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_dragbrace.uer_actuator_i_3  &
   adams_id = 130  &
   location = 0.0, 6.9364819444E-11, 0.4222750594  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_dragbrace.uer_actuator_i_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_upper_dragbrace  &
   mass = 6.7539180723  &
   center_of_mass_marker = .turn.ger_upper_dragbrace.cm  &
   inertia_marker = .turn.ger_upper_dragbrace.inertia_frame  &
   ixx = 0.4030130421  &
   iyy = 0.4030130421  &
   izz = 3.1372976041E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_upper_dragbrace.gralin_upper_dragbrace  &
   adams_id = 12  &
   center_marker = .turn.ger_upper_dragbrace.gralin_25  &
   angle_extent = 360.0  &
   length = 0.8445501187  &
   radius = 3.048E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_upper_dragbrace.gralin_upper_dragbrace  &
   color = RED
!
part attributes  &
   part_name = .turn.ger_upper_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_lower_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_lower_dragbrace  &
   adams_id = 10  &
   location = 11.821751947, -1.3511956141, 1.2178735066  &
   orientation = 68.8036164538d, 134.040966185d, 254.9123665662d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_lower_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_lower_dragbrace.cm  &
   adams_id = 131  &
   location = 3.9348735476E-03, 6.8056064573E-03, 2.4978613416E-02  &
   orientation = 149.9643072355d, 1.0992652329d, 180.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_dragbrace.inertia_frame  &
   adams_id = 132  &
   location = 3.9348735476E-03, 6.8056064573E-03, 2.4978613416E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_dragbrace.gralin_26  &
   adams_id = 133  &
   location = 0.0, -1.3320421155E-11, -0.4318055559  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_dragbrace.gralin_26  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_dragbrace.jxl_joint_i_14  &
   adams_id = 134  &
   location = 0.0, -1.33211428E-11, -0.4318055559  &
   orientation = 193.0709676552d, 90.2906925253d, 133.6233654172d
!
marker attributes  &
   marker_name = .turn.gel_lower_dragbrace.jxl_joint_i_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_dragbrace.jxl_joint_i_10  &
   adams_id = 135  &
   location = 0.0, 1.3321697911E-11, 0.4318055559  &
   orientation = 193.0709676552d, 90.2906925253d, 133.6233654172d
!
marker attributes  &
   marker_name = .turn.gel_lower_dragbrace.jxl_joint_i_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_dragbrace.graarm_1  &
   adams_id = 136  &
   location = 7.0772384935E-02, 0.1224052042, 0.1620383572  &
   orientation = 239.9643072438d, 90.0000000001d, 337.5559025676d
!
marker attributes  &
   marker_name = .turn.gel_lower_dragbrace.graarm_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_dragbrace.graarm_2  &
   adams_id = 137  &
   location = 0.0, 0.0, 0.1036333334  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_dragbrace.graarm_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_dragbrace.graarm_3  &
   adams_id = 138  &
   location = 0.0, 0.0, 0.2072666668  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_dragbrace.graarm_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_lower_dragbrace  &
   mass = 5.6992574801  &
   center_of_mass_marker = .turn.gel_lower_dragbrace.cm  &
   inertia_marker = .turn.gel_lower_dragbrace.inertia_frame  &
   ixx = 0.3211055352  &
   iyy = 0.3193778028  &
   izz = 5.107174896E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_lower_dragbrace.gralin_lower_dragbrace  &
   adams_id = 13  &
   center_marker = .turn.gel_lower_dragbrace.gralin_26  &
   angle_extent = 360.0  &
   length = 0.8636111118  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_lower_dragbrace.gralin_lower_dragbrace  &
   color = PEACH
!
geometry create shape plate  &
   plate_name = .turn.gel_lower_dragbrace.graarm_uplock_tab  &
   marker_name = .turn.gel_lower_dragbrace.graarm_1,  &
                 .turn.gel_lower_dragbrace.graarm_2,  &
                 .turn.gel_lower_dragbrace.graarm_3  &
   width = 2.54E-02  &
   radius = 1.27E-02
!
geometry attributes  &
   geometry_name = .turn.gel_lower_dragbrace.graarm_uplock_tab  &
   color = PEACH
!
part attributes  &
   part_name = .turn.gel_lower_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_lower_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_lower_dragbrace  &
   adams_id = 11  &
   location = 11.821751947, 1.3511956141, 1.2178735066  &
   orientation = 111.1963835462d, 134.040966185d, 285.0876334338d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_lower_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_lower_dragbrace.cm  &
   adams_id = 139  &
   location = 3.9348735476E-03, -6.8056064573E-03, 2.4978613416E-02  &
   orientation = 30.0356927645d, 1.0992652329d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_dragbrace.inertia_frame  &
   adams_id = 140  &
   location = 3.9348735476E-03, -6.8056064573E-03, 2.4978613416E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_dragbrace.gralin_27  &
   adams_id = 141  &
   location = 0.0, 1.3320448911E-11, -0.4318055559  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_dragbrace.gralin_27  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_dragbrace.jxr_joint_i_14  &
   adams_id = 142  &
   location = 0.0, 1.3319047254E-11, -0.4318055559  &
   orientation = 346.9290323448d, 90.2906925253d, 46.3766345828d
!
marker attributes  &
   marker_name = .turn.ger_lower_dragbrace.jxr_joint_i_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_dragbrace.jxr_joint_i_10  &
   adams_id = 143  &
   location = 0.0, -1.3321316272E-11, 0.4318055559  &
   orientation = 346.9290323448d, 90.2906925253d, 46.3766345828d
!
marker attributes  &
   marker_name = .turn.ger_lower_dragbrace.jxr_joint_i_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_dragbrace.graarm_4  &
   adams_id = 144  &
   location = 7.0772384935E-02, -0.1224052042, 0.1620383572  &
   orientation = 120.0356927562d, 89.9999999999d, 337.5559025676d
!
marker attributes  &
   marker_name = .turn.ger_lower_dragbrace.graarm_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_dragbrace.graarm_5  &
   adams_id = 145  &
   location = 0.0, 0.0, 0.1036333334  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_dragbrace.graarm_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_dragbrace.graarm_6  &
   adams_id = 146  &
   location = 0.0, 0.0, 0.2072666668  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_dragbrace.graarm_6  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_lower_dragbrace  &
   mass = 5.6992574801  &
   center_of_mass_marker = .turn.ger_lower_dragbrace.cm  &
   inertia_marker = .turn.ger_lower_dragbrace.inertia_frame  &
   ixx = 0.3211055352  &
   iyy = 0.3193778028  &
   izz = 5.107174896E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_lower_dragbrace.gralin_lower_dragbrace  &
   adams_id = 14  &
   center_marker = .turn.ger_lower_dragbrace.gralin_27  &
   angle_extent = 360.0  &
   length = 0.8636111118  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_lower_dragbrace.gralin_lower_dragbrace  &
   color = PEACH
!
geometry create shape plate  &
   plate_name = .turn.ger_lower_dragbrace.graarm_uplock_tab  &
   marker_name = .turn.ger_lower_dragbrace.graarm_4,  &
                 .turn.ger_lower_dragbrace.graarm_5,  &
                 .turn.ger_lower_dragbrace.graarm_6  &
   width = 2.54E-02  &
   radius = 1.27E-02
!
geometry attributes  &
   geometry_name = .turn.ger_lower_dragbrace.graarm_uplock_tab  &
   color = PEACH
!
part attributes  &
   part_name = .turn.ger_lower_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_upper_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_upper_torquearm  &
   adams_id = 12  &
   location = 12.0794524095, -1.4939074516, 0.6646292016  &
   orientation = 264.4801161257d, 168.6067018386d, 84.5882371559d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_upper_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_upper_torquearm.cm  &
   adams_id = 147  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_torquearm.inertia_frame  &
   adams_id = 148  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_torquearm.gralin_11  &
   adams_id = 149  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upper_torquearm.gralin_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_torquearm.jxl_joint_i_2  &
   adams_id = 150  &
   location = 0.0, 0.0, 0.1383335383  &
   orientation = 273.4244432527d, 89.9999731825d, 177.0527623566d
!
marker attributes  &
   marker_name = .turn.gel_upper_torquearm.jxl_joint_i_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upper_torquearm.jxl_joint_i_3  &
   adams_id = 151  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 183.4245252295d, 87.0529836943d, 74.5991863345d
!
marker attributes  &
   marker_name = .turn.gel_upper_torquearm.jxl_joint_i_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_upper_torquearm  &
   mass = 1.5364744752  &
   center_of_mass_marker = .turn.gel_upper_torquearm.cm  &
   inertia_marker = .turn.gel_upper_torquearm.inertia_frame  &
   ixx = 1.0048562438E-02  &
   iyy = 1.0048562438E-02  &
   izz = 4.9563593622E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_upper_torquearm.gralin_upper_torquearm  &
   adams_id = 15  &
   center_marker = .turn.gel_upper_torquearm.gralin_11  &
   angle_extent = 360.0  &
   length = 0.2766670766  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_upper_torquearm.gralin_upper_torquearm  &
   color = GREEN
!
part attributes  &
   part_name = .turn.gel_upper_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_upper_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_upper_torquearm  &
   adams_id = 13  &
   location = 12.0794524095, 1.4939074516, 0.6646292016  &
   orientation = 275.5198838743d, 168.6067018386d, 95.4117628441d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_upper_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_upper_torquearm.cm  &
   adams_id = 152  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_torquearm.inertia_frame  &
   adams_id = 153  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_torquearm.gralin_28  &
   adams_id = 154  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upper_torquearm.gralin_28  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_torquearm.jxr_joint_i_2  &
   adams_id = 155  &
   location = 0.0, 0.0, 0.1383335383  &
   orientation = 266.5755567473d, 89.9999731825d, 2.9472376434d
!
marker attributes  &
   marker_name = .turn.ger_upper_torquearm.jxr_joint_i_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upper_torquearm.jxr_joint_i_3  &
   adams_id = 156  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 356.5754747705d, 87.0529836943d, 105.4008136655d
!
marker attributes  &
   marker_name = .turn.ger_upper_torquearm.jxr_joint_i_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_upper_torquearm  &
   mass = 1.5364744752  &
   center_of_mass_marker = .turn.ger_upper_torquearm.cm  &
   inertia_marker = .turn.ger_upper_torquearm.inertia_frame  &
   ixx = 1.0048562438E-02  &
   iyy = 1.0048562438E-02  &
   izz = 4.9563593622E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_upper_torquearm.gralin_upper_torquearm  &
   adams_id = 16  &
   center_marker = .turn.ger_upper_torquearm.gralin_28  &
   angle_extent = 360.0  &
   length = 0.2766670766  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_upper_torquearm.gralin_upper_torquearm  &
   color = GREEN
!
part attributes  &
   part_name = .turn.ger_upper_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_lower_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_lower_torquearm  &
   adams_id = 14  &
   location = 12.0993426415, -1.5579375115, 0.4030923612  &
   orientation = 274.806891489d, 21.5573785759d, 85.5279353352d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_lower_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_lower_torquearm.cm  &
   adams_id = 157  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_torquearm.inertia_frame  &
   adams_id = 158  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_torquearm.gralin_29  &
   adams_id = 159  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lower_torquearm.gralin_29  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_torquearm.jxl_joint_i_11  &
   adams_id = 160  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 178.1282947989d, 95.1813481522d, 287.4366988554d
!
marker attributes  &
   marker_name = .turn.gel_lower_torquearm.jxl_joint_i_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lower_torquearm.jxl_joint_i_1  &
   adams_id = 161  &
   location = 0.0, 0.0, 0.1387301713  &
   orientation = 178.1282565411d, 95.1813639555d, 331.2687567728d
!
marker attributes  &
   marker_name = .turn.gel_lower_torquearm.jxl_joint_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_lower_torquearm  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.gel_lower_torquearm.cm  &
   inertia_marker = .turn.gel_lower_torquearm.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_lower_torquearm.gralin_lower_torquearm  &
   adams_id = 17  &
   center_marker = .turn.gel_lower_torquearm.gralin_29  &
   angle_extent = 360.0  &
   length = 0.2774603426  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_lower_torquearm.gralin_lower_torquearm  &
   color = MAGENTA
!
part attributes  &
   part_name = .turn.gel_lower_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_lower_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_lower_torquearm  &
   adams_id = 15  &
   location = 12.0993426415, 1.5579375115, 0.4030923612  &
   orientation = 265.193108511d, 21.5573785759d, 94.4720646648d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_lower_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_lower_torquearm.cm  &
   adams_id = 162  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_torquearm.inertia_frame  &
   adams_id = 163  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_torquearm.gralin_30  &
   adams_id = 164  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lower_torquearm.gralin_30  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_torquearm.jxr_joint_i_11  &
   adams_id = 165  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 1.8717052011d, 95.1813481522d, 252.5633011446d
!
marker attributes  &
   marker_name = .turn.ger_lower_torquearm.jxr_joint_i_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lower_torquearm.jxr_joint_i_1  &
   adams_id = 166  &
   location = 0.0, 0.0, 0.1387301713  &
   orientation = 1.8717434589d, 95.1813639555d, 208.7312432272d
!
marker attributes  &
   marker_name = .turn.ger_lower_torquearm.jxr_joint_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_lower_torquearm  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.ger_lower_torquearm.cm  &
   inertia_marker = .turn.ger_lower_torquearm.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_lower_torquearm.gralin_lower_torquearm  &
   adams_id = 18  &
   center_marker = .turn.ger_lower_torquearm.gralin_30  &
   angle_extent = 360.0  &
   length = 0.2774603426  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_lower_torquearm.gralin_lower_torquearm  &
   color = MAGENTA
!
part attributes  &
   part_name = .turn.ger_lower_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- gel_connector --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_connector  &
   adams_id = 17  &
   location = 12.0491222568, -1.5512110073, 0.5316382052  &
   orientation = 177.0103140237d, 92.4964937717d, 309.8285622575d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_connector
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_connector.cm  &
   adams_id = 169  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_connector.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_connector.inertia_frame  &
   adams_id = 170  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_connector.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_connector.gralin_3  &
   adams_id = 171  &
   location = 0.0, 0.0, -6.0070847244E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_connector.gralin_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_connector.jxl_joint_j_1  &
   adams_id = 172  &
   location = -3.2030729616E-08, -3.9921403722E-08, -1.1023458626E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_connector.jxl_joint_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_connector.jxl_joint_j_2  &
   adams_id = 173  &
   location = 0.0, 0.0, 6.0070847244E-02  &
   orientation = 331.5687748605d, 89.9998761701d, 89.9997712794d
!
marker attributes  &
   marker_name = .turn.gel_connector.jxl_joint_j_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_connector  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.gel_connector.cm  &
   inertia_marker = .turn.gel_connector.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_connector.gralin_connector  &
   adams_id = 19  &
   center_marker = .turn.gel_connector.gralin_3  &
   angle_extent = 360.0  &
   length = 0.1201416945  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_connector.gralin_connector  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .turn.gel_connector  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- ger_connector --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_connector  &
   adams_id = 18  &
   location = 12.0491222568, 1.5512110073, 0.5316382052  &
   orientation = 2.9896859763d, 92.4964937717d, 230.1714377425d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_connector
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_connector.cm  &
   adams_id = 174  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_connector.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_connector.inertia_frame  &
   adams_id = 175  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_connector.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_connector.gralin_4  &
   adams_id = 176  &
   location = 0.0, 0.0, -6.0070847244E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_connector.gralin_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_connector.jxr_joint_j_1  &
   adams_id = 177  &
   location = -3.2030729618E-08, 3.9921403724E-08, -1.1023458626E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_connector.jxr_joint_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_connector.jxr_joint_j_2  &
   adams_id = 178  &
   location = 0.0, 0.0, 6.0070847244E-02  &
   orientation = 208.4312251395d, 89.9998761701d, 90.0002287206d
!
marker attributes  &
   marker_name = .turn.ger_connector.jxr_joint_j_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_connector  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.ger_connector.cm  &
   inertia_marker = .turn.ger_connector.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_connector.gralin_connector  &
   adams_id = 20  &
   center_marker = .turn.ger_connector.gralin_4  &
   angle_extent = 360.0  &
   length = 0.1201416945  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_connector.gralin_connector  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .turn.ger_connector  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- gel_uc_collar --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_uc_collar  &
   adams_id = 19  &
   location = 12.2235346711, -1.4991580222, 0.8799979074  &
   orientation = 55.1145661544d, 175.2828647294d, 235.2057167569d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_uc_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_uc_collar.cm  &
   adams_id = 179  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_uc_collar.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_uc_collar.inertia_frame  &
   adams_id = 180  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_uc_collar.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_uc_collar.gralin_5  &
   adams_id = 181  &
   location = -5.4270445776E-11, 6.2140246074E-11, -0.1089542389  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_uc_collar.gralin_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_uc_collar.jxl_joint_j_3  &
   adams_id = 182  &
   location = 0.1220018852, 5.9907463311E-03, 7.1482951808E-02  &
   orientation = 182.811221391d, 89.9999933852d, 90.0001347091d
!
marker attributes  &
   marker_name = .turn.gel_uc_collar.jxl_joint_j_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_uc_collar.jxl_joint_i_4  &
   adams_id = 183  &
   location = -1.720947864E-11, 4.273941026E-11, 1.8185791048E-11  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_uc_collar.jxl_joint_i_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_uc_collar.jxl_joint_j_10  &
   adams_id = 184  &
   location = 0.1095796703, 3.35667969E-02, -4.683031071E-02  &
   orientation = 199.444502672d, 90.0d, 92.2365720495d
!
marker attributes  &
   marker_name = .turn.gel_uc_collar.jxl_joint_j_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_uc_collar  &
   mass = 30.2539444008  &
   center_of_mass_marker = .turn.gel_uc_collar.cm  &
   inertia_marker = .turn.gel_uc_collar.inertia_frame  &
   ixx = 0.2417065893  &
   iyy = 0.2417065893  &
   izz = 0.2439829346  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_uc_collar.gralin_uc_collar  &
   adams_id = 21  &
   center_marker = .turn.gel_uc_collar.gralin_5  &
   angle_extent = 360.0  &
   length = 0.2179084778  &
   radius = 0.127  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_uc_collar.gralin_uc_collar  &
   color = YELLOW
!
part attributes  &
   part_name = .turn.gel_uc_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- ger_uc_collar --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_uc_collar  &
   adams_id = 20  &
   location = 12.2235346711, 1.4991580222, 0.8799979074  &
   orientation = 124.8854338456d, 175.2828647294d, 304.7942832431d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_uc_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_uc_collar.cm  &
   adams_id = 185  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_uc_collar.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_uc_collar.inertia_frame  &
   adams_id = 186  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_uc_collar.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_uc_collar.gralin_6  &
   adams_id = 187  &
   location = -5.4270460521E-11, -6.2140235665E-11, -0.1089542389  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_uc_collar.gralin_6  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_uc_collar.jxr_joint_j_3  &
   adams_id = 188  &
   location = 0.1220018852, -5.9907463311E-03, 7.1482951808E-02  &
   orientation = 357.188778609d, 89.9999933852d, 89.9998652909d
!
marker attributes  &
   marker_name = .turn.ger_uc_collar.jxr_joint_j_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_uc_collar.jxr_joint_i_4  &
   adams_id = 189  &
   location = -1.720947864E-11, -4.2738966662E-11, 1.8185811935E-11  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_uc_collar.jxr_joint_i_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_uc_collar.jxr_joint_j_10  &
   adams_id = 190  &
   location = 0.1095796703, -3.35667969E-02, -4.683031071E-02  &
   orientation = 340.555497328d, 90.0d, 87.7634279505d
!
marker attributes  &
   marker_name = .turn.ger_uc_collar.jxr_joint_j_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_uc_collar  &
   mass = 30.2539444008  &
   center_of_mass_marker = .turn.ger_uc_collar.cm  &
   inertia_marker = .turn.ger_uc_collar.inertia_frame  &
   ixx = 0.2417065893  &
   iyy = 0.2417065893  &
   izz = 0.2439829346  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_uc_collar.gralin_uc_collar  &
   adams_id = 22  &
   center_marker = .turn.ger_uc_collar.gralin_6  &
   angle_extent = 360.0  &
   length = 0.2179084778  &
   radius = 0.127  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_uc_collar.gralin_uc_collar  &
   color = YELLOW
!
part attributes  &
   part_name = .turn.ger_uc_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!-------------------------------- gel_spindle ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_spindle  &
   adams_id = 21  &
   location = 10.870365356, -0.9895344548, 2.09911815  &
   orientation = 70.4651745203d, 87.687537877d, 270.820189184d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_spindle
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_spindle.cm  &
   adams_id = 191  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_spindle.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_spindle.inertia_frame  &
   adams_id = 192  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_spindle.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_spindle.gralin_7  &
   adams_id = 193  &
   location = 0.0, 3.7493150599E-11, -9.8425002805E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_spindle.gralin_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_spindle.jxl_joint_j_5  &
   adams_id = 194  &
   location = 0.0, 5.6759770251E-11, 9.8425002771E-02  &
   orientation = 357.8896246814d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_spindle.jxl_joint_j_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_spindle  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.gel_spindle.cm  &
   inertia_marker = .turn.gel_spindle.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_spindle.gralin_spindle  &
   adams_id = 23  &
   center_marker = .turn.gel_spindle.gralin_7  &
   angle_extent = 360.0  &
   length = 0.1968500056  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_spindle.gralin_spindle  &
   color = YELLOW
!
part attributes  &
   part_name = .turn.gel_spindle  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!-------------------------------- ger_spindle ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_spindle  &
   adams_id = 22  &
   location = 10.870365356, 0.9895344548, 2.09911815  &
   orientation = 109.5348254797d, 87.687537877d, 269.179810816d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_spindle
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_spindle.cm  &
   adams_id = 196  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_spindle.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_spindle.inertia_frame  &
   adams_id = 197  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_spindle.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_spindle.gralin_8  &
   adams_id = 198  &
   location = 0.0, -3.7493149149E-11, -9.8425002805E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_spindle.gralin_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_spindle.jxr_joint_j_5  &
   adams_id = 199  &
   location = 0.0, -5.6759771708E-11, 9.8425002771E-02  &
   orientation = 2.1103753186d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_spindle.jxr_joint_j_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_spindle  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.ger_spindle.cm  &
   inertia_marker = .turn.ger_spindle.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_spindle.gralin_spindle  &
   adams_id = 24  &
   center_marker = .turn.ger_spindle.gralin_8  &
   angle_extent = 360.0  &
   length = 0.1968500056  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_spindle.gralin_spindle  &
   color = YELLOW
!
part attributes  &
   part_name = .turn.ger_spindle  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- gel_lwract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_lwract  &
   adams_id = 23  &
   location = 12.3035450581, -1.3321655373, 1.6036216233  &
   orientation = 182.4778087702d, 7.7973026753d, 177.4990974089d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_lwract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_lwract.cm  &
   adams_id = 201  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lwract.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lwract.inertia_frame  &
   adams_id = 202  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lwract.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lwract.gralin_9  &
   adams_id = 203  &
   location = -1.1798721722E-11, -4.3827205753E-11, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lwract.gralin_9  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lwract.jxl_joint_j_7  &
   adams_id = 204  &
   location = -1.1798721722E-11, -4.3827205753E-11, -0.3002385778  &
   orientation = 2.5009025911d, 7.7973026753d, 357.5221912298d
!
marker attributes  &
   marker_name = .turn.gel_lwract.jxl_joint_j_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lwract.jxl_joint_i_8  &
   adams_id = 205  &
   location = -1.1820562107E-11, -4.412834681E-11, 0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lwract.jxl_joint_i_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lwract.uel_stopper_i_2  &
   adams_id = 206  &
   location = -1.1798721722E-11, -4.3827205753E-11, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lwract.uel_stopper_i_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lwract.uel_actuator_j_1  &
   adams_id = 207  &
   location = -1.1798721722E-11, -4.3827205753E-11, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lwract.uel_actuator_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_lwract.uel_actuator_i_2  &
   adams_id = 208  &
   location = -1.1818784666E-11, -4.4128145582E-11, 0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_lwract.uel_actuator_i_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_lwract  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.gel_lwract.cm  &
   inertia_marker = .turn.gel_lwract.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_lwract.gralin_lwract  &
   adams_id = 25  &
   center_marker = .turn.gel_lwract.gralin_9  &
   angle_extent = 360.0  &
   length = 0.6004771556  &
   radius = 7.62E-03  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_lwract.gralin_lwract  &
   color = YELLOW
!
part attributes  &
   part_name = .turn.gel_lwract  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- ger_lwract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_lwract  &
   adams_id = 24  &
   location = 12.3035450581, 1.3321655373, 1.6036216233  &
   orientation = 357.5221912298d, 7.7973026753d, 2.5009025911d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_lwract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_lwract.cm  &
   adams_id = 209  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lwract.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lwract.inertia_frame  &
   adams_id = 210  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lwract.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lwract.gralin_10  &
   adams_id = 211  &
   location = -1.1798754898E-11, 4.3827212692E-11, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lwract.gralin_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lwract.jxr_joint_j_7  &
   adams_id = 212  &
   location = -1.1798754898E-11, 4.3827212692E-11, -0.3002385778  &
   orientation = 177.4990974089d, 7.7973026753d, 182.4778087702d
!
marker attributes  &
   marker_name = .turn.ger_lwract.jxr_joint_j_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lwract.jxr_joint_i_8  &
   adams_id = 213  &
   location = -1.1820528931E-11, 4.412878396E-11, 0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lwract.jxr_joint_i_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lwract.uer_stopper_i_2  &
   adams_id = 214  &
   location = -1.1798754898E-11, 4.3827212692E-11, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lwract.uer_stopper_i_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lwract.uer_actuator_i_2  &
   adams_id = 215  &
   location = -1.182052763E-11, 4.4129026822E-11, 0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lwract.uer_actuator_i_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_lwract.uer_actuator_j_1  &
   adams_id = 216  &
   location = -1.1798754898E-11, 4.3827212692E-11, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_lwract.uer_actuator_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_lwract  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.ger_lwract.cm  &
   inertia_marker = .turn.ger_lwract.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_lwract.gralin_lwract  &
   adams_id = 26  &
   center_marker = .turn.ger_lwract.gralin_10  &
   angle_extent = 360.0  &
   length = 0.6004771556  &
   radius = 7.62E-03  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_lwract.gralin_lwract  &
   color = YELLOW
!
part attributes  &
   part_name = .turn.ger_lwract  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- gel_upract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.gel_upract  &
   adams_id = 25  &
   location = 12.3026262812, -1.3109333827, 1.7588195227  &
   orientation = 182.4778087702d, 7.7973026753d, 177.4990974089d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.gel_upract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.gel_upract.uel_actuator_i_1  &
   adams_id = 217  &
   location = -3.9769937126E-11, 0.0, 0.1958077682  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upract.uel_actuator_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upract.cm  &
   adams_id = 218  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upract.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upract.inertia_frame  &
   adams_id = 219  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upract.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upract.gralin_18  &
   adams_id = 220  &
   location = -3.9755074449E-11, 0.0, -0.1958077681  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upract.gralin_18  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upract.jxl_joint_j_8  &
   adams_id = 221  &
   location = -3.976996846E-11, 0.0, 0.1435923633  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upract.jxl_joint_j_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upract.uel_stopper_j_2  &
   adams_id = 223  &
   location = -3.9769937126E-11, 0.0, 0.1958077682  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upract.uel_stopper_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.gel_upract.uel_actuator_j_2  &
   adams_id = 224  &
   location = -3.9768190802E-11, 0.0, 0.1435923633  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.gel_upract.uel_actuator_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.gel_upract  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.gel_upract.cm  &
   inertia_marker = .turn.gel_upract.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.gel_upract.gralin_upract  &
   adams_id = 27  &
   center_marker = .turn.gel_upract.gralin_18  &
   angle_extent = 360.0  &
   length = 0.3916155363  &
   radius = 1.778E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.gel_upract.gralin_upract  &
   color = YELLOW
!
part attributes  &
   part_name = .turn.gel_upract  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- ger_upract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ger_upract  &
   adams_id = 26  &
   location = 12.3026262812, 1.3109333827, 1.7588195227  &
   orientation = 357.5221912298d, 7.7973026753d, 2.5009025911d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ger_upract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ger_upract.uer_actuator_i_1  &
   adams_id = 225  &
   location = -3.9769915442E-11, 0.0, 0.1958077682  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upract.uer_actuator_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upract.cm  &
   adams_id = 226  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upract.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upract.inertia_frame  &
   adams_id = 227  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upract.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upract.gralin_19  &
   adams_id = 228  &
   location = -3.975687249E-11, 0.0, -0.1958077681  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upract.gralin_19  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upract.jxr_joint_j_8  &
   adams_id = 229  &
   location = -3.9769952631E-11, 0.0, 0.1435923633  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upract.jxr_joint_j_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upract.uer_stopper_j_2  &
   adams_id = 231  &
   location = -3.9769915442E-11, 0.0, 0.1958077682  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upract.uer_stopper_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ger_upract.uer_actuator_j_2  &
   adams_id = 232  &
   location = -3.9768174973E-11, 0.0, 0.1435923633  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ger_upract.uer_actuator_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ger_upract  &
   mass = 0.45359237  &
   center_of_mass_marker = .turn.ger_upract.cm  &
   inertia_marker = .turn.ger_upract.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ger_upract.gralin_upract  &
   adams_id = 28  &
   center_marker = .turn.ger_upract.gralin_19  &
   angle_extent = 360.0  &
   length = 0.3916155363  &
   radius = 1.778E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ger_upract.gralin_upract  &
   color = YELLOW
!
part attributes  &
   part_name = .turn.ger_upract  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .turn.jolrev_lta_lc_joint  &
   adams_id = 2  &
   i_marker_name = .turn.gel_lower_torquearm.jxl_joint_i_11  &
   j_marker_name = .turn.gel_lower_cylinder.jxl_joint_j_11
!
constraint attributes  &
   constraint_name = .turn.jolrev_lta_lc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .turn.jorrev_lta_lc_joint  &
   adams_id = 3  &
   i_marker_name = .turn.ger_lower_torquearm.jxr_joint_i_11  &
   j_marker_name = .turn.ger_lower_cylinder.jxr_joint_j_11
!
constraint attributes  &
   constraint_name = .turn.jorrev_lta_lc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .turn.jolcyl_lc_uc_joint  &
   adams_id = 4  &
   i_marker_name = .turn.gel_lower_cylinder.jxl_joint_i_12  &
   j_marker_name = .turn.gel_upper_cylinder.jxl_joint_j_12
!
constraint attributes  &
   constraint_name = .turn.jolcyl_lc_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .turn.jorcyl_lc_uc_joint  &
   adams_id = 5  &
   i_marker_name = .turn.ger_lower_cylinder.jxr_joint_i_12  &
   j_marker_name = .turn.ger_upper_cylinder.jxr_joint_j_12
!
constraint attributes  &
   constraint_name = .turn.jorcyl_lc_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .turn.jolrev_ldb_udb_joint  &
   adams_id = 6  &
   i_marker_name = .turn.gel_lower_dragbrace.jxl_joint_i_14  &
   j_marker_name = .turn.gel_upper_dragbrace.jxl_joint_j_14
!
constraint attributes  &
   constraint_name = .turn.jolrev_ldb_udb_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .turn.jorrev_ldb_udb_joint  &
   adams_id = 7  &
   i_marker_name = .turn.ger_lower_dragbrace.jxr_joint_i_14  &
   j_marker_name = .turn.ger_upper_dragbrace.jxr_joint_j_14
!
constraint attributes  &
   constraint_name = .turn.jorrev_ldb_udb_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .turn.jolcyl_lta_connect  &
   adams_id = 12  &
   i_marker_name = .turn.gel_lower_torquearm.jxl_joint_i_1  &
   j_marker_name = .turn.gel_connector.jxl_joint_j_1
!
constraint attributes  &
   constraint_name = .turn.jolcyl_lta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .turn.jorcyl_lta_connect  &
   adams_id = 13  &
   i_marker_name = .turn.ger_lower_torquearm.jxr_joint_i_1  &
   j_marker_name = .turn.ger_connector.jxr_joint_j_1
!
constraint attributes  &
   constraint_name = .turn.jorcyl_lta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .turn.jolrev_uta_connect  &
   adams_id = 14  &
   i_marker_name = .turn.gel_upper_torquearm.jxl_joint_i_2  &
   j_marker_name = .turn.gel_connector.jxl_joint_j_2
!
constraint attributes  &
   constraint_name = .turn.jolrev_uta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .turn.jorrev_uta_connect  &
   adams_id = 15  &
   i_marker_name = .turn.ger_upper_torquearm.jxr_joint_i_2  &
   j_marker_name = .turn.ger_connector.jxr_joint_j_2
!
constraint attributes  &
   constraint_name = .turn.jorrev_uta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .turn.jolrev_uta_collar  &
   adams_id = 16  &
   i_marker_name = .turn.gel_upper_torquearm.jxl_joint_i_3  &
   j_marker_name = .turn.gel_uc_collar.jxl_joint_j_3
!
constraint attributes  &
   constraint_name = .turn.jolrev_uta_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .turn.jorrev_uta_collar  &
   adams_id = 17  &
   i_marker_name = .turn.ger_upper_torquearm.jxr_joint_i_3  &
   j_marker_name = .turn.ger_uc_collar.jxr_joint_j_3
!
constraint attributes  &
   constraint_name = .turn.jorrev_uta_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .turn.jolrev_collar_uc  &
   adams_id = 18  &
   i_marker_name = .turn.gel_uc_collar.jxl_joint_i_4  &
   j_marker_name = .turn.gel_upper_cylinder.jxl_joint_j_4
!
constraint attributes  &
   constraint_name = .turn.jolrev_collar_uc  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .turn.jorrev_collar_uc  &
   adams_id = 19  &
   i_marker_name = .turn.ger_uc_collar.jxr_joint_i_4  &
   j_marker_name = .turn.ger_upper_cylinder.jxr_joint_j_4
!
constraint attributes  &
   constraint_name = .turn.jorrev_collar_uc  &
   size_of_icons = 5.0E-02
!
constraint create joint hooke  &
   joint_name = .turn.jolhoo_udb_spndl  &
   adams_id = 20  &
   i_marker_name = .turn.gel_upper_dragbrace.jxl_joint_i_5  &
   j_marker_name = .turn.gel_spindle.jxl_joint_j_5
!
constraint attributes  &
   constraint_name = .turn.jolhoo_udb_spndl  &
   size_of_icons = 5.0E-02
!
constraint create joint hooke  &
   joint_name = .turn.jorhoo_udb_spndl  &
   adams_id = 21  &
   i_marker_name = .turn.ger_upper_dragbrace.jxr_joint_i_5  &
   j_marker_name = .turn.ger_spindle.jxr_joint_j_5
!
constraint attributes  &
   constraint_name = .turn.jorhoo_udb_spndl  &
   size_of_icons = 5.0E-02
!
constraint create joint spherical  &
   joint_name = .turn.jolsph_uc_lwract  &
   adams_id = 24  &
   i_marker_name = .turn.gel_upper_cylinder.jxl_joint_i_7  &
   j_marker_name = .turn.gel_lwract.jxl_joint_j_7
!
constraint attributes  &
   constraint_name = .turn.jolsph_uc_lwract  &
   size_of_icons = 5.0E-02
!
constraint create joint spherical  &
   joint_name = .turn.jorsph_uc_lwract  &
   adams_id = 25  &
   i_marker_name = .turn.ger_upper_cylinder.jxr_joint_i_7  &
   j_marker_name = .turn.ger_lwract.jxr_joint_j_7
!
constraint attributes  &
   constraint_name = .turn.jorsph_uc_lwract  &
   size_of_icons = 5.0E-02
!
constraint create joint translational  &
   joint_name = .turn.joltra_lwract_upract  &
   adams_id = 26  &
   i_marker_name = .turn.gel_lwract.jxl_joint_i_8  &
   j_marker_name = .turn.gel_upract.jxl_joint_j_8
!
constraint attributes  &
   constraint_name = .turn.joltra_lwract_upract  &
   size_of_icons = 5.0E-02
!
constraint create joint translational  &
   joint_name = .turn.jortra_lwract_upract  &
   adams_id = 27  &
   i_marker_name = .turn.ger_lwract.jxr_joint_i_8  &
   j_marker_name = .turn.ger_upract.jxr_joint_j_8
!
constraint attributes  &
   constraint_name = .turn.jortra_lwract_upract  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .turn.jolrev_ldb_collar  &
   adams_id = 30  &
   i_marker_name = .turn.gel_lower_dragbrace.jxl_joint_i_10  &
   j_marker_name = .turn.gel_uc_collar.jxl_joint_j_10
!
constraint attributes  &
   constraint_name = .turn.jolrev_ldb_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .turn.jorrev_ldb_collar  &
   adams_id = 31  &
   i_marker_name = .turn.ger_lower_dragbrace.jxr_joint_i_10  &
   j_marker_name = .turn.ger_uc_collar.jxr_joint_j_10
!
constraint attributes  &
   constraint_name = .turn.jorrev_ldb_collar  &
   size_of_icons = 5.0E-02
!
!----------------------------- Analysis settings ------------------------------!
!
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .turn.ground.cfl_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.cfl_spin_axis_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({180.0, 180.0, 180.0}degrees, .turn.ground.cfl_spin_axis_1))
!
marker modify  &
   marker_name = .turn.ground.cfr_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.cfr_spin_axis_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({-180.0, -180.0, -180.0}degrees, .turn.ground.cfr_spin_axis_1))
!
marker modify  &
   marker_name = .turn.ground.cfl_axial_reference  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_lc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_lc_bot, .turn.ground.hpl_uc_top, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfr_axial_reference  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_lc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_lc_bot, .turn.ground.hpr_uc_top, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfl_uc_bot  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 21.18}inch, .turn.ground.cfl_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfr_uc_bot  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 21.18}inch, .turn.ground.cfr_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfl_uc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfr_uc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfl_lc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 38.06}inch, .turn.ground.cfl_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfr_lc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 38.06}inch, .turn.ground.cfr_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfl_uta_uc_atch  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.cfl_uc_bot))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfr_uta_uc_atch  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.cfr_uc_bot))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfl_lta_lc_atch  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_lc_bot))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfr_lta_lc_atch  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_lc_bot))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfl_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpl_uc_top, .turn.ground.hpl_lc_bot, 0.59 * DM(.turn.ground.hpl_uc_top, .turn.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_uc_top, .turn.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfr_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpr_uc_top, .turn.ground.hpr_lc_bot, 0.59 * DM(.turn.ground.hpr_uc_top, .turn.ground.hpr_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_uc_top, .turn.ground.hpr_lc_bot, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfl_collar_bot  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpl_uc_top, .turn.ground.hpl_lc_bot, 0.7 * DM(.turn.ground.hpl_uc_top, .turn.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_uc_top, .turn.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfr_collar_bot  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpr_uc_top, .turn.ground.hpr_lc_bot, 0.7 * DM(.turn.ground.hpr_uc_top, .turn.ground.hpr_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_uc_top, .turn.ground.hpr_lc_bot, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfl_plane_ref_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.cfl_plane_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, -90.0, 0.0}degrees, .turn.ground.cfl_plane_ref))
!
marker modify  &
   marker_name = .turn.ground.cfr_plane_ref_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.cfr_plane_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .turn.ground.cfr_plane_ref))
!
marker modify  &
   marker_name = .turn.ground.cfl_lwract_top  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpl_lwract_uc_atch_1, .turn.ground.hpl_upract_sf_atch_1, 0.92 * DM(.turn.ground.hpl_lwract_uc_atch_1, .turn.ground.hpl_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_lwract_uc_atch_1, .turn.ground.hpl_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfr_lwract_top  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpr_lwract_uc_atch_1, .turn.ground.hpr_upract_sf_atch_1, 0.92 * DM(.turn.ground.hpr_lwract_uc_atch_1, .turn.ground.hpr_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_lwract_uc_atch_1, .turn.ground.hpr_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfl_upract_bot  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpl_lwract_uc_atch_1, .turn.ground.hpl_upract_sf_atch_1, 0.4 * DM(.turn.ground.hpl_lwract_uc_atch_1, .turn.ground.hpl_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_lwract_uc_atch_1, .turn.ground.hpl_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfr_upract_bot  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpr_lwract_uc_atch_1, .turn.ground.hpr_upract_sf_atch_1, 0.4 * DM(.turn.ground.hpr_lwract_uc_atch_1, .turn.ground.hpr_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_lwract_uc_atch_1, .turn.ground.hpr_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfl_spin_axis_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_wheel_center, .turn.ground.hpl_ob_axle, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfr_spin_axis_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_wheel_center, .turn.ground.hpr_ob_axle, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfl_ldb_geompt_1  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpl_ldb_udb_atch_1, .turn.ground.hpl_ldb_collar_atch_1, 0.62 * DM(.turn.ground.hpl_ldb_udb_atch_1, .turn.ground.hpl_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfr_ldb_geompt_1  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpr_ldb_udb_atch_1, .turn.ground.hpr_ldb_collar_atch_1, 0.62 * DM(.turn.ground.hpr_ldb_udb_atch_1, .turn.ground.hpr_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfl_ldb_geompt_2  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpl_ldb_udb_atch_1, .turn.ground.hpl_ldb_collar_atch_1, 0.74 * DM(.turn.ground.hpl_ldb_udb_atch_1, .turn.ground.hpl_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfr_ldb_geompt_2  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hpr_ldb_udb_atch_1, .turn.ground.hpr_ldb_collar_atch_1, 0.74 * DM(.turn.ground.hpr_ldb_udb_atch_1, .turn.ground.hpr_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfl_aero_ref  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.cfr_aero_ref  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.uel_gearaero_origin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.origo))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.uel_gearaero_rm_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_aero_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_aero_ref))
!
marker modify  &
   marker_name = .turn.ground.uer_gearaero_origin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.origo))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ground.origo))
!
marker modify  &
   marker_name = .turn.ground.uer_gearaero_rm_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_aero_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_aero_ref))
!
material modify  &
   material_name = .turn.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .turn.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .turn.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .turn.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.uel_gearaero_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_lc_top))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_cylinder))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.gralin_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.cfl_uc_top, .turn.ground.cfl_uc_bot, "Z"))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.gralin_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_ib_uc_sf_atch, .turn.ground.hpl_uc_geompt, "Z"))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.gralin_20  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_ib_uc_sf_atch, .turn.ground.hpl_uc_top, "Z"))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.uel_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_uc_top))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.uel_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_uc_top))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.uel_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_uc_top))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.jxl_joint_i_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_lwract.jxl_joint_j_7))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_lwract.jxl_joint_j_7))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.uel_actuator_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_uc_sf_atch))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_cylinder.MARKER_267  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_uc_top))  &
   relative_to = .turn.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_upper_cylinder.gralin_upper_cylinder  &
   length = (DM(.turn.ground.cfl_uc_top, .turn.ground.cfl_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_upper_cylinder.gralin_geom  &
   length = (DM(.turn.ground.hpl_ib_uc_sf_atch, .turn.ground.hpl_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_upper_cylinder.gralin_geom3  &
   length = (DM(.turn.ground.hpl_ib_uc_sf_atch, .turn.ground.hpl_uc_top))
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.uer_gearaero_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_lc_top))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_cylinder))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.gralin_13  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.cfr_uc_top, .turn.ground.cfr_uc_bot, "Z"))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.gralin_17  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_ib_uc_sf_atch, .turn.ground.hpr_uc_geompt, "Z"))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.gralin_21  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_ib_uc_sf_atch, .turn.ground.hpr_uc_top, "Z"))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.uer_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_uc_top))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.uer_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_uc_top))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.uer_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_uc_top))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.jxr_joint_i_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_lwract.jxr_joint_j_7))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_lwract.jxr_joint_j_7))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.uer_actuator_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_uc_sf_atch))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_cylinder.MARKER_269  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_uc_top))  &
   relative_to = .turn.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_upper_cylinder.gralin_upper_cylinder  &
   length = (DM(.turn.ground.cfr_uc_top, .turn.ground.cfr_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_upper_cylinder.gralin_geom  &
   length = (DM(.turn.ground.hpr_ib_uc_sf_atch, .turn.ground.hpr_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_upper_cylinder.gralin_geom3  &
   length = (DM(.turn.ground.hpr_ib_uc_sf_atch, .turn.ground.hpr_uc_top))
!
marker modify  &
   marker_name = .turn.gel_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_lower_cylinder))  &
   relative_to = .turn.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_cylinder.gralin_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.cfl_lc_top, .turn.ground.hpl_lc_bot, "Z"))  &
   relative_to = .turn.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_cylinder.gralin_22  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_ib_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_ib_axle, .turn.ground.hpl_ob_axle, "Z"))  &
   relative_to = .turn.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_cylinder.jxl_joint_j_11  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_lta_connect_atch_1, .turn.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_cylinder.jxl_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_cylinder.jxl_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_cylinder.jxl_joint_j_12))  &
   relative_to = .turn.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_cylinder.coomarker_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_spin_axis))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_spin_axis))  &
   relative_to = .turn.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_cylinder.uel_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_lc_top))  &
   relative_to = .turn.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_cylinder.uel_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_lc_top))  &
   relative_to = .turn.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_cylinder.uel_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_lc_top))  &
   relative_to = .turn.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_lower_cylinder.gralin_lower_cylinder  &
   length = (DM(.turn.ground.cfl_lc_top, .turn.ground.hpl_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_lower_cylinder.gralin_geom  &
   length = (DM(.turn.ground.hpl_ib_axle, .turn.ground.hpl_ob_axle))
!
marker modify  &
   marker_name = .turn.ger_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_lower_cylinder))  &
   relative_to = .turn.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_cylinder.gralin_15  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.cfr_lc_top, .turn.ground.hpr_lc_bot, "Z"))  &
   relative_to = .turn.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_cylinder.gralin_23  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_ib_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_ib_axle, .turn.ground.hpr_ob_axle, "Z"))  &
   relative_to = .turn.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_cylinder.jxr_joint_j_11  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_lta_connect_atch_1, .turn.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_cylinder.jxr_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_cylinder.jxr_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_cylinder.jxr_joint_j_12))  &
   relative_to = .turn.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_cylinder.coomarker_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_spin_axis))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_spin_axis))  &
   relative_to = .turn.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_cylinder.uer_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_lc_top))  &
   relative_to = .turn.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_cylinder.uer_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_lc_top))  &
   relative_to = .turn.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_cylinder.uer_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_lc_top))  &
   relative_to = .turn.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_lower_cylinder.gralin_lower_cylinder  &
   length = (DM(.turn.ground.cfr_lc_top, .turn.ground.hpr_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_lower_cylinder.gralin_geom  &
   length = (DM(.turn.ground.hpr_ib_axle, .turn.ground.hpr_ob_axle))
!
marker modify  &
   marker_name = .turn.gel_upper_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_dragbrace))  &
   relative_to = .turn.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_dragbrace.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_udb_spndl_atch_1, .turn.ground.hpl_ldb_udb_atch_1, "Z"))  &
   relative_to = .turn.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_dragbrace.jxl_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.turn.ground.cfl_plane_ref_2, "Z+Z"), .turn.gel_upper_dragbrace))  &
   relative_to = .turn.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_dragbrace.jxl_joint_i_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_spindle.jxl_joint_j_5))  &
   orientation =   &
      (ORI_IN_PLANE(.turn.gel_upper_dragbrace.jxl_joint_i_5, .turn.ground.hpl_ldb_udb_atch_1, .turn.ground.hpl_spndl_sf_atch, "Z_ZX"))  &
   relative_to = .turn.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_dragbrace.uel_actuator_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_ldb_udb_atch_1))  &
   relative_to = .turn.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_upper_dragbrace.gralin_upper_dragbrace  &
   length = (DM(.turn.ground.hpl_udb_spndl_atch_1, .turn.ground.hpl_ldb_udb_atch_1))
!
marker modify  &
   marker_name = .turn.ger_upper_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_dragbrace))  &
   relative_to = .turn.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_dragbrace.gralin_25  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_udb_spndl_atch_1, .turn.ground.hpr_ldb_udb_atch_1, "Z"))  &
   relative_to = .turn.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_dragbrace.jxr_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.turn.ground.cfr_plane_ref_2, "Z+Z"), .turn.ger_upper_dragbrace))  &
   relative_to = .turn.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_dragbrace.jxr_joint_i_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_spindle.jxr_joint_j_5))  &
   orientation =   &
      (ORI_IN_PLANE(.turn.ger_upper_dragbrace.jxr_joint_i_5, .turn.ground.hpr_ldb_udb_atch_1, .turn.ground.hpr_spndl_sf_atch, "Z_ZX"))  &
   relative_to = .turn.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_dragbrace.uer_actuator_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_ldb_udb_atch_1))  &
   relative_to = .turn.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_upper_dragbrace.gralin_upper_dragbrace  &
   length = (DM(.turn.ground.hpr_udb_spndl_atch_1, .turn.ground.hpr_ldb_udb_atch_1))
!
marker modify  &
   marker_name = .turn.gel_lower_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_lower_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_lower_dragbrace))  &
   relative_to = .turn.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_dragbrace.gralin_26  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_ldb_udb_atch_1, .turn.ground.hpl_ldb_collar_atch_1, "Z"))  &
   relative_to = .turn.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_dragbrace.jxl_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_dragbrace.jxl_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_dragbrace.jxl_joint_j_14))  &
   relative_to = .turn.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_dragbrace.jxl_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_uc_collar.jxl_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_uc_collar.jxl_joint_j_10))  &
   relative_to = .turn.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_dragbrace.graarm_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_uplock_tab))  &
   orientation =   &
      (ORI_IN_PLANE(.turn.ground.hpl_uplock_tab, .turn.ground.cfl_ldb_geompt_1, .turn.ground.cfl_ldb_geompt_2, "X_XY"))  &
   relative_to = .turn.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_dragbrace.graarm_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_ldb_geompt_1))  &
   relative_to = .turn.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_dragbrace.graarm_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_ldb_geompt_2))  &
   relative_to = .turn.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_lower_dragbrace.gralin_lower_dragbrace  &
   length = (DM(.turn.ground.hpl_ldb_udb_atch_1, .turn.ground.hpl_ldb_collar_atch_1))
!
marker modify  &
   marker_name = .turn.ger_lower_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_lower_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_lower_dragbrace))  &
   relative_to = .turn.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_dragbrace.gralin_27  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_ldb_udb_atch_1, .turn.ground.hpr_ldb_collar_atch_1, "Z"))  &
   relative_to = .turn.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_dragbrace.jxr_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_dragbrace.jxr_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_dragbrace.jxr_joint_j_14))  &
   relative_to = .turn.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_dragbrace.jxr_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_uc_collar.jxr_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_uc_collar.jxr_joint_j_10))  &
   relative_to = .turn.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_dragbrace.graarm_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_uplock_tab))  &
   orientation =   &
      (ORI_IN_PLANE(.turn.ground.hpr_uplock_tab, .turn.ground.cfr_ldb_geompt_1, .turn.ground.cfr_ldb_geompt_2, "X_XY"))  &
   relative_to = .turn.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_dragbrace.graarm_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_ldb_geompt_1))  &
   relative_to = .turn.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_dragbrace.graarm_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_ldb_geompt_2))  &
   relative_to = .turn.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_lower_dragbrace.gralin_lower_dragbrace  &
   length = (DM(.turn.ground.hpr_ldb_udb_atch_1, .turn.ground.hpr_ldb_collar_atch_1))
!
marker modify  &
   marker_name = .turn.gel_upper_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_torquearm))  &
   relative_to = .turn.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_torquearm.gralin_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_uta_collar_atch_1, .turn.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_torquearm.jxl_joint_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_connector.jxl_joint_j_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_connector.jxl_joint_j_2))  &
   relative_to = .turn.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upper_torquearm.jxl_joint_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_uc_collar.jxl_joint_j_3))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_uc_collar.jxl_joint_j_3))  &
   relative_to = .turn.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_upper_torquearm.gralin_upper_torquearm  &
   length = (DM(.turn.ground.hpl_uta_collar_atch_1, .turn.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .turn.ger_upper_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_torquearm))  &
   relative_to = .turn.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_torquearm.gralin_28  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_uta_collar_atch_1, .turn.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_torquearm.jxr_joint_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_connector.jxr_joint_j_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_connector.jxr_joint_j_2))  &
   relative_to = .turn.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upper_torquearm.jxr_joint_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_uc_collar.jxr_joint_j_3))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_uc_collar.jxr_joint_j_3))  &
   relative_to = .turn.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_upper_torquearm.gralin_upper_torquearm  &
   length = (DM(.turn.ground.hpr_uta_collar_atch_1, .turn.ground.hpr_uta_connect_atch_1))
!
marker modify  &
   marker_name = .turn.gel_lower_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_lower_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_lower_torquearm))  &
   relative_to = .turn.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_torquearm.gralin_29  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_lta_lc_atch_1, .turn.ground.hpl_lta_connect_atch_1, "Z"))  &
   relative_to = .turn.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_torquearm.jxl_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_lower_cylinder.jxl_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_lower_cylinder.jxl_joint_j_11))  &
   relative_to = .turn.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lower_torquearm.jxl_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_connector.jxl_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_connector.jxl_joint_j_1))  &
   relative_to = .turn.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_lower_torquearm.gralin_lower_torquearm  &
   length = (DM(.turn.ground.hpl_lta_lc_atch_1, .turn.ground.hpl_lta_connect_atch_1))
!
marker modify  &
   marker_name = .turn.ger_lower_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_lower_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_lower_torquearm))  &
   relative_to = .turn.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_torquearm.gralin_30  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_lta_lc_atch_1, .turn.ground.hpr_lta_connect_atch_1, "Z"))  &
   relative_to = .turn.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_torquearm.jxr_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_lower_cylinder.jxr_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_lower_cylinder.jxr_joint_j_11))  &
   relative_to = .turn.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lower_torquearm.jxr_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_connector.jxr_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_connector.jxr_joint_j_1))  &
   relative_to = .turn.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_lower_torquearm.gralin_lower_torquearm  &
   length = (DM(.turn.ground.hpr_lta_lc_atch_1, .turn.ground.hpr_lta_connect_atch_1))
!
marker modify  &
   marker_name = .turn.gel_connector.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_connector.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_connector))  &
   relative_to = .turn.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_connector.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_connect_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_connect_1, .turn.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_connector.jxl_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_lta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_lta_connect_atch_1, .turn.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_connector.jxl_joint_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_uta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_uta_connect_atch_1, .turn.ground.hpl_uta_connect_atch_2, "Z"))  &
   relative_to = .turn.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_connector.gralin_connector  &
   length = (DM(.turn.ground.hpl_connect_1, .turn.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .turn.ger_connector.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_connector.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_connector))  &
   relative_to = .turn.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_connector.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_connect_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_connect_1, .turn.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_connector.jxr_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_lta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_lta_connect_atch_1, .turn.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_connector.jxr_joint_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_uta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_uta_connect_atch_1, .turn.ground.hpr_uta_connect_atch_2, "Z"))  &
   relative_to = .turn.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_connector.gralin_connector  &
   length = (DM(.turn.ground.hpr_connect_1, .turn.ground.hpr_uta_connect_atch_1))
!
marker modify  &
   marker_name = .turn.gel_uc_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_uc_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_uc_collar))  &
   relative_to = .turn.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_uc_collar.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.cfl_collar_top, .turn.ground.cfl_collar_bot, "Z"))  &
   relative_to = .turn.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_uc_collar.jxl_joint_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_lta_connect_atch_1, .turn.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_uc_collar.jxl_joint_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_cylinder.jxl_joint_j_4))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_upper_cylinder.jxl_joint_j_4))  &
   relative_to = .turn.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_uc_collar.jxl_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_ldb_collar_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.turn.ground.cfl_plane_ref_2, "Z+Z"), .turn.gel_uc_collar))  &
   relative_to = .turn.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_uc_collar.gralin_uc_collar  &
   length = (DM(.turn.ground.cfl_collar_top, .turn.ground.cfl_collar_bot))
!
marker modify  &
   marker_name = .turn.ger_uc_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_uc_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_uc_collar))  &
   relative_to = .turn.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_uc_collar.gralin_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.cfr_collar_top, .turn.ground.cfr_collar_bot, "Z"))  &
   relative_to = .turn.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_uc_collar.jxr_joint_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_lta_connect_atch_1, .turn.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .turn.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_uc_collar.jxr_joint_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_cylinder.jxr_joint_j_4))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_upper_cylinder.jxr_joint_j_4))  &
   relative_to = .turn.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_uc_collar.jxr_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_ldb_collar_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.turn.ground.cfr_plane_ref_2, "Z+Z"), .turn.ger_uc_collar))  &
   relative_to = .turn.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_uc_collar.gralin_uc_collar  &
   length = (DM(.turn.ground.cfr_collar_top, .turn.ground.cfr_collar_bot))
!
marker modify  &
   marker_name = .turn.gel_spindle.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_spindle.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_spindle))  &
   relative_to = .turn.gel_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_spindle.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_spndl_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_spndl_sf_atch, .turn.ground.hpl_udb_spndl_atch_1, "Z"))  &
   relative_to = .turn.gel_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_spindle.jxl_joint_j_5  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_IN_PLANE(.turn.ground.hpl_spndl_sf_atch, .turn.gel_spindle.jxl_joint_j_5, .turn.ground.hpl_ldb_udb_atch_1, "Z_ZX"))  &
   relative_to = .turn.gel_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_spindle.gralin_spindle  &
   length = (DM(.turn.ground.hpl_spndl_sf_atch, .turn.ground.hpl_udb_spndl_atch_1))
!
marker modify  &
   marker_name = .turn.ger_spindle.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_spindle.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_spindle))  &
   relative_to = .turn.ger_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_spindle.gralin_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_spndl_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_spndl_sf_atch, .turn.ground.hpr_udb_spndl_atch_1, "Z"))  &
   relative_to = .turn.ger_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_spindle.jxr_joint_j_5  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_IN_PLANE(.turn.ground.hpr_spndl_sf_atch, .turn.ger_spindle.jxr_joint_j_5, .turn.ground.hpr_ldb_udb_atch_1, "Z_ZX"))  &
   relative_to = .turn.ger_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_spindle.gralin_spindle  &
   length = (DM(.turn.ground.hpr_spndl_sf_atch, .turn.ground.hpr_udb_spndl_atch_1))
!
marker modify  &
   marker_name = .turn.gel_lwract.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_lwract.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_lwract))  &
   relative_to = .turn.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lwract.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_lwract_uc_atch_1, .turn.ground.cfl_lwract_top, "Z"))  &
   relative_to = .turn.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lwract.jxl_joint_j_7  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))  &
   relative_to = .turn.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lwract.jxl_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_upract.jxl_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_upract.jxl_joint_j_8))  &
   relative_to = .turn.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lwract.uel_stopper_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_lwract_uc_atch_1))  &
   relative_to = .turn.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lwract.uel_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_lwract_uc_atch_1))  &
   relative_to = .turn.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_lwract.uel_actuator_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_lwract.jxl_joint_i_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_lwract.jxl_joint_i_8))  &
   relative_to = .turn.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_lwract.gralin_lwract  &
   length = (DM(.turn.ground.hpl_lwract_uc_atch_1, .turn.ground.cfl_lwract_top))
!
marker modify  &
   marker_name = .turn.ger_lwract.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_lwract.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_lwract))  &
   relative_to = .turn.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lwract.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_lwract_uc_atch_1, .turn.ground.cfr_lwract_top, "Z"))  &
   relative_to = .turn.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lwract.jxr_joint_j_7  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo))  &
   relative_to = .turn.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lwract.jxr_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_upract.jxr_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_upract.jxr_joint_j_8))  &
   relative_to = .turn.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lwract.uer_stopper_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_lwract_uc_atch_1))  &
   relative_to = .turn.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lwract.uer_actuator_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_lwract.jxr_joint_i_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_lwract.jxr_joint_i_8))  &
   relative_to = .turn.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_lwract.uer_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_lwract_uc_atch_1))  &
   relative_to = .turn.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_lwract.gralin_lwract  &
   length = (DM(.turn.ground.hpr_lwract_uc_atch_1, .turn.ground.cfr_lwract_top))
!
marker modify  &
   marker_name = .turn.gel_upract.uel_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_upract_sf_atch_1))  &
   relative_to = .turn.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upract.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_upract.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_upract))  &
   relative_to = .turn.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upract.gralin_18  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfl_upract_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.cfl_upract_bot, .turn.ground.hpl_upract_sf_atch_1, "Z"))  &
   relative_to = .turn.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upract.jxl_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.cfl_lwract_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_lwract_uc_atch_1, .turn.ground.hpl_upract_sf_atch_1, "Z"))  &
   relative_to = .turn.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upract.uel_stopper_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_upract_sf_atch_1))  &
   relative_to = .turn.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.gel_upract.uel_actuator_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.gel_upract.jxl_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.gel_upract.jxl_joint_j_8))  &
   relative_to = .turn.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.gel_upract.gralin_upract  &
   length = (DM(.turn.ground.cfl_upract_bot, .turn.ground.hpl_upract_sf_atch_1))
!
marker modify  &
   marker_name = .turn.ger_upract.uer_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_upract_sf_atch_1))  &
   relative_to = .turn.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upract.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_upract.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_upract))  &
   relative_to = .turn.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upract.gralin_19  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfr_upract_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.cfr_upract_bot, .turn.ground.hpr_upract_sf_atch_1, "Z"))  &
   relative_to = .turn.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upract.jxr_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.cfr_lwract_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_lwract_uc_atch_1, .turn.ground.hpr_upract_sf_atch_1, "Z"))  &
   relative_to = .turn.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upract.uer_stopper_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_upract_sf_atch_1))  &
   relative_to = .turn.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ger_upract.uer_actuator_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ger_upract.jxr_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ger_upract.jxr_joint_j_8))  &
   relative_to = .turn.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ger_upract.gralin_upract  &
   length = (DM(.turn.ground.cfr_upract_bot, .turn.ground.hpr_upract_sf_atch_1))
!
model display  &
   model_name = turn

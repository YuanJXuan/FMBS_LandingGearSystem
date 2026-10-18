!
!-------------------------- Default Units for Model ---------------------------!
!
!
defaults units  &
   length = mm  &
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
   icon_visibility = off  &
   grid_visibility = off  &
   size_of_icons = 25.4  &
   spacing_for_grid = 25.4
!
!------------------------------ Adams View Model ------------------------------!
!
!
model create  &
   model_name = template_6_motion  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_6_motion  &
   size_of_icons = 50.8
!
view erase
!
!-------------------------------- Data storage --------------------------------!
!
!
data_element create spline  &
   spline_name = .template_6_motion.SPLINE_angle_aeroforce_NLG  &
   adams_id = 2  &
   x = -20.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0,  &
       90.0, 100.0  &
   y = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0  &
   linear_extrapolate = no
!
data_element create spline  &
   spline_name = .template_6_motion.SPLINE_angle_aeroforce_MLG  &
   adams_id = 8  &
   x = -20.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0,  &
       90.0, 100.0  &
   y = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0  &
   linear_extrapolate = no
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .template_6_motion.steel  &
   adams_id = 2  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_motion.aluminum  &
   adams_id = 3  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_motion.steel_2  &
   adams_id = 1  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_motion.aluminum_2  &
   adams_id = 4  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
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
   default_coordinate_system = .template_6_motion.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ground.origo  &
   adams_id = 10  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.origo  &
   visibility = on  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ground.cfs_uc_sf_atch_mid  &
   adams_id = 12  &
   location = 6314.44, 0.0, 1691.64  &
   orientation = 0.0d, 90.0000000003d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfs_uc_sf_atch_mid  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfs_subframe_to_body_point  &
   adams_id = 13  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0000000003d, 356.6444799104d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfs_subframe_to_body_point  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.mts_mount_j_2  &
   adams_id = 14  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.mts_mount_j_2  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ground.cfs_wheel_centers_midpoint  &
   adams_id = 17  &
   location = 6229.096, 0.0, 508.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfs_wheel_centers_midpoint  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfs_nlg_axle_lowpoint  &
   adams_id = 18  &
   location = 6229.096, 0.0, 482.6  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfs_nlg_axle_lowpoint  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfs_collar_top  &
   adams_id = 19  &
   location = 6197.6, 0.0, 856.996  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfs_collar_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.origo1  &
   adams_id = 1  &
   location = 100.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.origo1  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfs_subframe_ref  &
   adams_id = 117  &
   location = 1.1650194959E+04, 0.0, 2128.24779709  &
   orientation = 180.0000000006d, 90.0000000003d, 177.5464650672d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfs_subframe_ref  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_uc_sf_atch  &
   adams_id = 120  &
   location = 1.2245749991E+04, -1244.74817217, 2123.04463122  &
   orientation = 357.5219193209d, 81.1274829137d, 15.6737410427d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_uc_sf_atch  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_uc_sf_atch  &
   adams_id = 11  &
   location = 1.2245749991E+04, 1244.74817217, 2123.04463122  &
   orientation = 182.4780806808d, 81.1274829137d, 164.3262589579d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_uc_sf_atch  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.mts_mount_j_4  &
   adams_id = 121  &
   location = 1.1750194959E+04, 0.0, 2128.24779709  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.mts_mount_j_4  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_axial_reference  &
   adams_id = 122  &
   location = 1.237097482E+04, -1532.23480192, 179.1298424  &
   orientation = 235.1145660619d, 4.7171352597d, 124.7942833359d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_axial_reference  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_axial_reference  &
   adams_id = 123  &
   location = 1.237097482E+04, 1532.23480192, 179.1298424  &
   orientation = 304.8854339381d, 4.7171352597d, 55.2057166641d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_axial_reference  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_uc_bot  &
   adams_id = 124  &
   location = 1.2334684072E+04, -1506.931738783, 715.2796436374  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_uc_bot  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_uc_bot  &
   adams_id = 125  &
   location = 1.2334684072E+04, 1506.931738783, 715.2796436374  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_uc_bot  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_uc_top  &
   adams_id = 126  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_uc_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_uc_top  &
   adams_id = 127  &
   location = 1.2237340597E+04, 1439.0607744, 2153.4060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_uc_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_lc_top  &
   adams_id = 128  &
   location = 1.2305761133E+04, -1486.7657470101, 1142.5793907993  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_lc_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_lc_top  &
   adams_id = 129  &
   location = 1.2305761133E+04, 1486.7657470101, 1142.5793907993  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_lc_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_collar_top  &
   adams_id = 134  &
   location = 1.2316184789E+04, -1494.0334506368, 988.583100554  &
   orientation = 55.1145660619d, 175.2828647403d, 235.2057166641d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_collar_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_collar_top  &
   adams_id = 135  &
   location = 1.2316184789E+04, 1494.0334506368, 988.583100554  &
   orientation = 124.8854339381d, 175.2828647403d, 304.7942833359d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_collar_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_collar_bot  &
   adams_id = 136  &
   location = 1.2330884553E+04, -1504.282593664, 771.41271422  &
   orientation = 55.1145660619d, 175.2828647403d, 235.2057166641d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_collar_bot  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_collar_bot  &
   adams_id = 137  &
   location = 1.2330884553E+04, 1504.282593664, 771.41271422  &
   orientation = 124.8854339381d, 175.2828647403d, 304.7942833359d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_collar_bot  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_plane_ref  &
   adams_id = 138  &
   location = 1.1890454913E+04, -1331.23818588, 1478.5418121942  &
   orientation = 70.4651741896d, 87.6875364205d, 268.7516172688d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_plane_ref  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_plane_ref  &
   adams_id = 139  &
   location = 1.1890454913E+04, 1331.23818588, 1478.5418121942  &
   orientation = 109.534825811d, 87.6875364205d, 271.248382733d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_plane_ref  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_plane_ref_2  &
   adams_id = 140  &
   location = 1.1890454913E+04, -1331.23818588, 1478.5418121942  &
   orientation = 160.414795052d, 91.2473659395d, 267.6869880057d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_plane_ref_2  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_plane_ref_2  &
   adams_id = 141  &
   location = 1.1890454913E+04, 1331.23818588, 1478.5418121942  &
   orientation = 19.5852049487d, 91.2473659413d, 272.3130119943d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_plane_ref_2  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_lwract_top  &
   adams_id = 142  &
   location = 1.2401784069E+04, -1291.47057428, 1901.084263864  &
   orientation = 182.4778086409d, 7.7973026745d, 177.4990975394d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_lwract_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_lwract_top  &
   adams_id = 143  &
   location = 1.2401784069E+04, 1291.47057428, 1901.084263864  &
   orientation = 357.5221913591d, 7.7973026745d, 2.5009024606d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_lwract_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_upract_bot  &
   adams_id = 144  &
   location = 1.2403774752E+04, -1337.473576, 1564.82214848  &
   orientation = 182.4778086409d, 7.7973026745d, 177.4990975394d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_upract_bot  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_upract_bot  &
   adams_id = 145  &
   location = 1.2403774752E+04, 1337.473576, 1564.82214848  &
   orientation = 357.5221913591d, 7.7973026745d, 2.5009024606d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_upract_bot  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfl_spin_axis_1  &
   adams_id = 146  &
   location = 1.2370973957E+04, -1811.59195974, 174.2595194  &
   orientation = 359.9999063882d, 91.0000312229d, 179.9946363355d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfl_spin_axis_1  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ground.cfr_spin_axis_1  &
   adams_id = 147  &
   location = 1.2370973957E+04, 1811.59195974, 174.2595194  &
   orientation = 180.0000936118d, 91.0000312229d, 5.3636645377E-03d
!
marker attributes  &
   marker_name = .template_6_motion.ground.cfr_spin_axis_1  &
   color = MAIZE  &
   visibility = on
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_6_motion.ground.uel_gearaero_jfloat_1  &
   adams_id = 158
!
floating_marker create  &
   floating_marker_name = .template_6_motion.ground.uer_gearaero_jfloat_1  &
   adams_id = 159
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_6_motion.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_6_motion.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_sf_atch_l  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_sf_atch_r  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_6_motion.ground.hps_lc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_6_motion.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uta_uc_atch  &
   location = 6324.6, 0.0, 838.2
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uta_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lta_lc_atch  &
   location = 6299.2, 0.0, 533.4
!
point attributes  &
   point_name = .template_6_motion.ground.hps_lta_lc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lta_uta_atch  &
   location = 6654.8, 0.0, 711.2
!
point attributes  &
   point_name = .template_6_motion.ground.hps_lta_uta_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_geompt  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_6_motion.ground.hps_lc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lb_uc_atch  &
   location = 6021.578, 0.0, 795.02
!
point create  &
   point_name = .template_6_motion.ground.hpl_wheel_center  &
   location = 6229.096, -209.55, 508.0
!
point create  &
   point_name = .template_6_motion.ground.hpr_wheel_center  &
   location = 6229.096, 209.55, 508.0
!
point create  &
   point_name = .template_6_motion.ground.hpl_ob_axle  &
   location = 6229.096, -285.75, 508.0
!
point create  &
   point_name = .template_6_motion.ground.hpr_ob_axle  &
   location = 6229.096, 285.75, 508.0
!
point create  &
   point_name = .template_6_motion.ground.hps_nlg_axle_lowpoint  &
   location = 6229.096, 0.0, 482.6
!
point create  &
   point_name = .template_6_motion.ground.hps_rod_bot  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point create  &
   point_name = .template_6_motion.ground.hps_rod_top  &
   location = 7227.4389033572, 0.0, 1472.1512863532
!
point create  &
   point_name = .template_6_motion.ground.hps_aeroforceN  &
   location = 6200.9167643494, 0.0, 1207.1824231157
!
point create  &
   point_name = .template_6_motion.ground.hpl_aeroforceL  &
   location = 1.2305761133E+04, -1486.7657470101, 1142.5793907993
!
point create  &
   point_name = .template_6_motion.ground.hpr_aerofoceR  &
   location = 1.2305761133E+04, 1486.7657470101, 1142.5793907993
!
point create  &
   point_name = .template_6_motion.ground.hpl_udb_spndl_atch_1  &
   location = 1.1063049321E+04, -1022.41898132, 2103.08951238
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_udb_spndl_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_udb_spndl_atch_1  &
   location = 1.1063049321E+04, 1022.41898132, 2103.08951238
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_udb_spndl_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ib_uc_sf_atch  &
   location = 1.2254159385E+04, -1050.43556994, 2092.68318064
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ib_uc_sf_atch  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ib_uc_sf_atch  &
   location = 1.2254159385E+04, 1050.43556994, 2092.68318064
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ib_uc_sf_atch  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_wheel_center1  &
   location = 1.2370973957E+04, -1811.59195974, 174.2595194
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_wheel_center1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_wheel_center1  &
   location = 1.2370973957E+04, 1811.59195974, 174.2595194
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_wheel_center1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lc_bot  &
   location = 1.237097482E+04, -1532.23480192, 179.1298424
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lc_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lc_bot  &
   location = 1.237097482E+04, 1532.23480192, 179.1298424
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lc_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ob_axle1  &
   location = 1.2370973718E+04, -1957.87367632, 171.7060828
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ob_axle1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ob_axle1  &
   location = 1.2370973718E+04, 1957.87367632, 171.7060828
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ob_axle1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ib_axle  &
   location = 1.237097482E+04, -1532.234807, 179.1298424
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ib_axle  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ib_axle  &
   location = 1.237097482E+04, 1532.234807, 179.1298424
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ib_axle  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uc_top  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uc_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uc_top  &
   location = 1.2237340597E+04, 1439.0607744, 2153.4060818
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uc_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uc_geompt  &
   location = 1.2267031622E+04, -1359.45122572, 1761.7947238
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uc_geompt  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uc_geompt  &
   location = 1.2267031622E+04, 1359.45122572, 1761.7947238
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uc_geompt  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_stator_attach  &
   location = 1.2370974048E+04, -1754.4506694, 175.256952
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_stator_attach  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_stator_attach  &
   location = 1.2370974048E+04, 1754.4506694, 175.256952
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_stator_attach  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ldb_udb_atch_1  &
   location = 1.1632351205E+04, -1238.965478376, 1518.05286178
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ldb_udb_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ldb_udb_atch_1  &
   location = 1.1632351205E+04, 1238.965478376, 1518.05286178
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ldb_udb_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lta_connect_atch_1  &
   location = 1.2148547912E+04, -1562.2090168, 532.1183668
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lta_connect_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lta_connect_atch_1  &
   location = 1.2148547912E+04, 1562.2090168, 532.1183668
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lta_connect_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uta_connect_atch_1  &
   location = 1.215225235E+04, -1491.2788564, 529.0216242
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uta_connect_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uta_connect_atch_1  &
   location = 1.215225235E+04, 1491.2788564, 529.0216242
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uta_connect_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uta_connect_atch_2  &
   location = 1.2187047708E+04, -1493.4025504, 522.0012166
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uta_connect_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uta_connect_atch_2  &
   location = 1.2187047708E+04, 1493.4025504, 522.0012166
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uta_connect_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lta_lc_atch_1  &
   location = 1.2250137371E+04, -1553.6660062, 274.0663556
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lta_lc_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lta_lc_atch_1  &
   location = 1.2250137371E+04, 1553.6660062, 274.0663556
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lta_lc_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lta_lc_atch_2  &
   location = 1.2252562741E+04, -1507.2279736, 272.0389276
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lta_lc_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lta_lc_atch_2  &
   location = 1.2252562741E+04, 1507.2279736, 272.0389276
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lta_lc_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uta_collar_atch_1  &
   location = 1.2206652469E+04, -1496.5360468, 800.236779
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uta_collar_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uta_collar_atch_1  &
   location = 1.2206652469E+04, 1496.5360468, 800.236779
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uta_collar_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uta_collar_atch_2  &
   location = 1.221021393E+04, -1428.342457, 797.259518
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uta_collar_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uta_collar_atch_2  &
   location = 1.221021393E+04, 1428.342457, 797.259518
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uta_collar_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_collar_top  &
   location = 1.2316682831E+04, -1494.3808822, 981.2211008
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_collar_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_collar_top  &
   location = 1.2316682831E+04, 1494.3808822, 981.2211008
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_collar_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_collar_bot  &
   location = 1.2331355039E+04, -1504.6108084, 764.4576024
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_collar_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_collar_bot  &
   location = 1.2331355039E+04, 1504.6108084, 764.4576024
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_collar_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_upr_strt_bot  &
   location = 1.2332707285E+04, -1505.5538596, 744.4805024
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_upr_strt_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_upr_strt_bot  &
   location = 1.2332707285E+04, 1505.5538596, 744.4805024
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_upr_strt_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_upr_strt_top  &
   location = 1.2247818199E+04, 1446.3662462, 1998.6101506
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_upr_strt_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lwract_uc_atch_1  &
   location = 1.2405306047E+04, -1372.8605004, 1306.1589828
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lwract_uc_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lwract_uc_atch_1  &
   location = 1.2405306047E+04, 1372.8605004, 1306.1589828
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lwract_uc_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lwract_uc_atch_2  &
   location = 1.2406350165E+04, 1355.5888052, 1303.8056982
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lwract_uc_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_upract_sf_atch_1  &
   location = 1.240147781E+04, -1284.3931894, 1952.816897
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_upract_sf_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_upract_sf_atch_1  &
   location = 1.240147781E+04, 1284.3931894, 1952.816897
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_upract_sf_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_upract_sf_atch_2  &
   location = 1.2403675418E+04, 1250.4491628, 1948.1928778
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_upract_sf_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_spndl_sf_atch  &
   location = 1.0877681391E+04, -956.6499282, 2095.1467876
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_spndl_sf_atch  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_spndl_sf_atch  &
   location = 1.0877681391E+04, 956.6499282, 2095.1467876
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_spndl_sf_atch  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_connect_1  &
   location = 1.2145992164E+04, -1611.1431582, 534.2547862
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_connect_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_connect_1  &
   location = 1.2145992164E+04, 1611.1431582, 534.2547862
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_connect_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ldb_collar_atch_1  &
   location = 1.2211152689E+04, -1463.4257498, 917.6941514
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ldb_collar_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ldb_collar_atch_1  &
   location = 1.2211152689E+04, 1463.4257498, 917.6941514
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ldb_collar_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ldb_collar_atch_2  &
   location = 1.2182985562E+04, -1542.5928508, 919.5237896
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ldb_collar_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ldb_collar_atch_2  &
   location = 1.2182985562E+04, 1542.5928508, 919.5237896
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ldb_collar_atch_2  &
   visibility = on
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_6_motion.ground  &
   size_of_icons = 50.8
!
!------------------------------ ges_sf_actuator -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ges_sf_actuator  &
   adams_id = 7  &
   location = 6967.855, 0.0, 1319.53  &
   orientation = 270.0000000009d, 120.4532239116d, 90.0000000003d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ges_sf_actuator
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ges_sf_actuator.cm  &
   adams_id = 21  &
   location = -2.6589288646E-08, -8.1094015533E-09, -25.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_actuator.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_sf_actuator.gralin_1  &
   adams_id = 23  &
   location = -2.6589286328E-08, -8.1094057298E-09, -598.873681109  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_actuator.gralin_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_sf_actuator.jxs_joint_i_14  &
   adams_id = 24  &
   location = -2.6589230817E-08, -8.1094057298E-09, -598.873681109  &
   orientation = 0.0d, 89.9999999991d, 239.5467760884d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_actuator.jxs_joint_i_14  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_sf_actuator.MARKER_85  &
   adams_id = 85  &
   location = 1.3451462166E-09, 0.0, 158.8736811071  &
   orientation = 90.0000000003d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_actuator.MARKER_85  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ges_sf_actuator.MARKER_97  &
   adams_id = 97  &
   location = -4.5918824298E-10, 0.0, -598.873681109  &
   orientation = 90.0000000003d, 120.4532239116d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_actuator.MARKER_97  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ges_sf_actuator  &
   material_type = .template_6_motion.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_sf_actuator.gralin_dragbrace_geom  &
   adams_id = 32  &
   center_marker = .template_6_motion.ges_sf_actuator.gralin_1  &
   angle_extent = 360.0  &
   length = 1147.7473622179  &
   radius = 50.8  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_sf_actuator.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .template_6_motion.ges_sf_actuator  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ges_upper_cylinder  &
   adams_id = 8  &
   location = 6197.6, 0.0, 1193.8  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ges_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ges_upper_cylinder.MARKER_4  &
   adams_id = 4  &
   location = -236.7591354821, -2.4792465641E-09, 187.9366952496  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_cylinder.MARKER_4  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ges_upper_cylinder.cm  &
   adams_id = 25  &
   location = -2.1926640514, -2.2900518287E-11, -14.5859826029  &
   orientation = 90.0000000006d, 0.8375931978d, 270.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_upper_cylinder.gralin_2  &
   adams_id = 27  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_cylinder.gralin_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_upper_cylinder.gralin_3  &
   adams_id = 28  &
   location = -116.8399999964, -340.3600000012, -497.84  &
   orientation = 161.0534953111d, 58.7414044414d, 213.4869581738d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_cylinder.gralin_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_upper_cylinder.gralin_4  &
   adams_id = 29  &
   location = -116.8400000036, 340.3599999988, -497.84  &
   orientation = 18.9465046901d, 58.7414044414d, 326.5130418244d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_cylinder.gralin_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_j_11  &
   adams_id = 30  &
   location = 0.0, 0.0, 114.3  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_j_11  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_i_15  &
   adams_id = 31  &
   location = -116.84, -1.2234292211E-09, -497.84  &
   orientation = 0.0d, 89.9999999997d, 180.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_i_15  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_j_1  &
   adams_id = 35  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_j_1  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_upper_cylinder.MARKER_aeroforce  &
   adams_id = 108  &
   location = -3.3167643494, 0.0, -13.3824231157  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_cylinder.MARKER_aeroforce  &
   visibility = on
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_6_motion.ges_upper_cylinder.FMARKER_107  &
   adams_id = 107
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ges_upper_cylinder  &
   material_type = .template_6_motion.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 33  &
   center_marker = .template_6_motion.ges_upper_cylinder.gralin_2  &
   angle_extent = 360.0000000012  &
   length = 863.6  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 34  &
   center_marker = .template_6_motion.ges_upper_cylinder.gralin_3  &
   angle_extent = 360.0000000012  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 35  &
   center_marker = .template_6_motion.ges_upper_cylinder.gralin_4  &
   angle_extent = 360.0000000012  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_6_motion.ges_upper_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ges_lower_cylinder  &
   adams_id = 9  &
   location = 6197.6, 0.0, 952.5  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ges_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ges_lower_cylinder.MARKER_106  &
   adams_id = 106  &
   location = -3.3167643494, -3.3820967206E-11, -254.6824231157  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_cylinder.MARKER_106  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ges_lower_cylinder.cm  &
   adams_id = 38  &
   location = -7.8736475458, -8.2416712344E-11, 111.1200258466  &
   orientation = 270.0000000006d, 1.780178135d, 90.0000000001d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_lower_cylinder.gralin_5  &
   adams_id = 40  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_cylinder.gralin_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_lower_cylinder.jxs_joint_j_9  &
   adams_id = 41  &
   location = -101.6, -1.0639558371E-09, 419.1  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_cylinder.jxs_joint_j_9  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_lower_cylinder.jxs_joint_i_11  &
   adams_id = 42  &
   location = 0.0, 0.0, -127.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_cylinder.jxs_joint_i_11  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_lower_cylinder.gralin_7  &
   adams_id = 43  &
   location = -31.4960000022, 209.5499999997, 444.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_cylinder.gralin_7  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_lower_cylinder.MARKER_350  &
   adams_id = 350  &
   location = -31.495999997, -285.7500000003, 444.5  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_6_motion.ges_lower_cylinder.MARKER_351  &
   adams_id = 351  &
   location = -31.496000003, 285.7499999997, 444.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ges_lower_cylinder  &
   material_type = .template_6_motion.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_lower_cylinder.gralin_geom1  &
   adams_id = 36  &
   center_marker = .template_6_motion.ges_lower_cylinder.gralin_5  &
   angle_extent = 360.0000000012  &
   length = 889.0  &
   radius = 101.6  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_lower_cylinder.gralin_geom2  &
   adams_id = 37  &
   center_marker = .template_6_motion.ges_lower_cylinder.gralin_7  &
   angle_extent = 360.0000000012  &
   length = 419.1  &
   radius = 30.48  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_lower_cylinder.gralin_geom2  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_lower_cylinder.CYLINDER_80  &
   adams_id = 80  &
   center_marker = .template_6_motion.ges_lower_cylinder.MARKER_350  &
   angle_extent = 360.0  &
   length = 90.0  &
   radius = 120.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_lower_cylinder.CYLINDER_82  &
   adams_id = 82  &
   center_marker = .template_6_motion.ges_lower_cylinder.MARKER_351  &
   angle_extent = 360.0  &
   length = 90.0  &
   radius = 120.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_motion.ges_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!---------------------------- ges_upper_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ges_upper_torque_arm  &
   adams_id = 10  &
   location = 6489.7, 0.0, 774.7  &
   orientation = 90.0000000003d, 111.0375110247d, 270.0000000009d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ges_upper_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ges_upper_torque_arm.cm  &
   adams_id = 49  &
   location = -2.2285994229E-09, 8.6446043838E-10, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_torque_arm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_upper_torque_arm.gralin_9  &
   adams_id = 51  &
   location = -2.2285992496E-09, 8.644590757E-10, -176.8905311202  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_torque_arm.gralin_9  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_upper_torque_arm.jxs_joint_j_8  &
   adams_id = 52  &
   location = 2.2282800605E-09, -8.644590757E-10, 176.8905311202  &
   orientation = 0.0d, 90.0000000003d, 111.0375110247d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_torque_arm.jxs_joint_j_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_upper_torque_arm.jxs_joint_i_10  &
   adams_id = 53  &
   location = -2.2285992496E-09, 8.644590757E-10, -176.8905311202  &
   orientation = 0.0d, 90.0000000003d, 111.0375110247d
!
marker attributes  &
   marker_name = .template_6_motion.ges_upper_torque_arm.jxs_joint_i_10  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ges_upper_torque_arm  &
   material_type = .template_6_motion.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   adams_id = 38  &
   center_marker = .template_6_motion.ges_upper_torque_arm.gralin_9  &
   angle_extent = 360.0000000012  &
   length = 353.7810622405  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   color = GREEN
!
part attributes  &
   part_name = .template_6_motion.ges_upper_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!---------------------------- ges_lower_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ges_lower_torque_arm  &
   adams_id = 11  &
   location = 6477.0, 0.0, 622.3  &
   orientation = 90.0000000003d, 63.4349488233d, 270.0000000009d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ges_lower_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ges_lower_torque_arm.cm  &
   adams_id = 54  &
   location = 1.3112007061E-09, 9.309558938E-10, 0.0  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_torque_arm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_lower_torque_arm.jxs_joint_i_8  &
   adams_id = 56  &
   location = -1.3110207364E-09, -9.3095592762E-10, 198.7864431997  &
   orientation = 0.0d, 90.0000000009d, 63.4349488233d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_torque_arm.jxs_joint_i_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_lower_torque_arm.gralin_10  &
   adams_id = 57  &
   location = 1.3112011477E-09, 9.3095592762E-10, -198.7864431997  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_torque_arm.gralin_10  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_lower_torque_arm.jxs_joint_i_9  &
   adams_id = 58  &
   location = 1.3112011477E-09, 9.3095592762E-10, -198.7864431997  &
   orientation = 269.9999999991d, 63.4349488233d, 89.9999999997d
!
marker attributes  &
   marker_name = .template_6_motion.ges_lower_torque_arm.jxs_joint_i_9  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ges_lower_torque_arm  &
   material_type = .template_6_motion.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   adams_id = 39  &
   center_marker = .template_6_motion.ges_lower_torque_arm.gralin_10  &
   angle_extent = 360.0000000012  &
   length = 397.5728863995  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_6_motion.ges_lower_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!-------------------------------- ges_subframe --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ges_subframe  &
   adams_id = 12  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0000000003d, 356.6444799104d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ges_subframe
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ges_subframe.cm  &
   adams_id = 59  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_subframe.inertia_frame  &
   adams_id = 60  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe.inertia_frame  &
   visibility = on  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_subframe.graout_1  &
   adams_id = 61  &
   location = -390.5595878991, 6.4598604244E-09, -340.3600000001  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe.graout_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_subframe.graout_2  &
   adams_id = 62  &
   location = -390.5595878993, 1.0017979502E-08, 340.3599999999  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe.graout_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_subframe.graout_3  &
   adams_id = 63  &
   location = 781.1191757984, -1.6477617881E-08, 2.3938866711E-10  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe.graout_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_6_motion.ges_subframe.jxs_joint_j_15  &
   adams_id = 64  &
   location = -390.5595878992, 8.2389199629E-09, -1.1969433355E-10  &
   orientation = 3.3555200896d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe.jxs_joint_j_15  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe.jxs_joint_i_16  &
   adams_id = 65  &
   location = 0.0, 0.0, 0.0  &
   orientation = 183.3555200896d, 90.0000000003d, 180.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe.jxs_joint_i_16  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe.jxs_joint_j_14  &
   adams_id = 66  &
   location = 781.1191757984, -1.6477617881E-08, 2.3938866711E-10  &
   orientation = 3.3555200896d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe.jxs_joint_j_14  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ges_subframe  &
   mass = 4.5359237E-03  &
   center_of_mass_marker = .template_6_motion.ges_subframe.cm  &
   inertia_marker = .template_6_motion.ges_subframe.inertia_frame  &
   ixx = 2.9263965343  &
   iyy = 2.9263965343  &
   izz = 2.9263965343  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create curve outline  &
   outline_name = .template_6_motion.ges_subframe.graout_subframe_geom  &
   adams_id = 41  &
   marker_name =  &
      .template_6_motion.ges_subframe.graout_1,  &
      .template_6_motion.ges_subframe.graout_2,  &
      .template_6_motion.ges_subframe.graout_3  &
   visibility_between_markers = on, on, on  &
   close = yes
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_subframe.graout_subframe_geom  &
   color = WHITE
!
part attributes  &
   part_name = .template_6_motion.ges_subframe  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!------------------------------- mts_body_mount -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.mts_body_mount  &
   adams_id = 13  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.mts_body_mount
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.mts_body_mount.mount_i  &
   adams_id = 67  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.mts_body_mount.mount_i  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.mts_body_mount.jxs_joint_j_16  &
   adams_id = 68  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.mts_body_mount.jxs_joint_j_16  &
   visibility = on  &
   name_visibility = off
!
part attributes  &
   part_name = .template_6_motion.mts_body_mount  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- ges_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ges_collar  &
   adams_id = 14  &
   location = 6197.6, 0.0, 809.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ges_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ges_collar.jxs_joint_j_10  &
   adams_id = 69  &
   location = 127.0, 0.0, 28.702  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_collar.jxs_joint_j_10  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_collar.cm  &
   adams_id = 70  &
   location = 0.0, 0.0, 0.0  &
   orientation = 180.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_collar.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_collar.gralin_24  &
   adams_id = 72  &
   location = 0.0, 0.0, -47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_collar.gralin_24  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_collar.jxs_joint_i_1  &
   adams_id = 73  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_collar.jxs_joint_i_1  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ges_collar  &
   material_type = .template_6_motion.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_collar.gralin_collar  &
   adams_id = 40  &
   center_marker = .template_6_motion.ges_collar.gralin_24  &
   angle_extent = 360.0000000012  &
   length = 94.996  &
   radius = 139.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .template_6_motion.ges_collar  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- ges_sf_rod ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ges_sf_rod  &
   adams_id = 5  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ges_sf_rod
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ges_sf_rod.MARKER_5  &
   adams_id = 5  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_rod.MARKER_5  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ges_sf_rod.gralin_25  &
   adams_id = 3  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 270.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_rod.gralin_25  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ges_sf_rod.cm  &
   adams_id = 76  &
   location = 6830.8990194197, 0.0, 1239.0072955518  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_rod.cm  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ges_sf_rod.MARKER_84  &
   adams_id = 84  &
   location = 6830.8990194192, 0.0, 1239.0072955517  &
   orientation = 90.0000000003d, 59.5467760889d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_rod.MARKER_84  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ges_sf_rod.MARKER_96  &
   adams_id = 96  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_sf_rod.MARKER_96  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ges_sf_rod  &
   material_type = .template_6_motion.steel
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_6_motion.ges_sf_rod.PT3  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point attributes  &
   point_name = .template_6_motion.ges_sf_rod.PT3  &
   visibility = off  &
   name_visibility = off
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ges_sf_rod.CYLINDER_30  &
   adams_id = 30  &
   center_marker = .template_6_motion.ges_sf_rod.gralin_25  &
   angle_extent = 360.0000000012  &
   length = 920.0  &
   radius = 27.5  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_motion.ges_sf_rod  &
   color = RED  &
   name_visibility = off
!
!------------------------------- ges_subframe_2 -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ges_subframe_2  &
   adams_id = 3  &
   location = 1.1650194959E+04, 0.0, 2128.24779709  &
   orientation = 180.0000000006d, 90.0000000003d, 177.5464650672d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ges_subframe_2
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.cm  &
   adams_id = 161  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.inertia_frame  &
   adams_id = 162  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.inertia_frame  &
   visibility = on
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.graout_5  &
   adams_id = 163  &
   location = -587.6843876817, -2.302082136E-10, -1022.4189813137  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.graout_5  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.graout_6  &
   adams_id = 164  &
   location = -587.6843876599, -1.0010454271E-08, 1022.4189813263  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.graout_6  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.graout_7  &
   adams_id = 165  &
   location = 587.6843876862, -1.7629162019E-09, 1439.0607743937  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.graout_7  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.graout_8  &
   adams_id = 166  &
   location = 601.8882599469, 61.3872329379, 1050.4355699339  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.graout_8  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.graout_9  &
   adams_id = 167  &
   location = 601.8882599244, 61.3872329479, -1050.4355699461  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.graout_9  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.graout_10  &
   adams_id = 168  &
   location = 587.6843876554, 1.2002843164E-08, -1439.0607744063  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.graout_10  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_16  &
   adams_id = 169  &
   location = 594.7863237899, 30.69361648, -1244.7481721762  &
   orientation = 346.9720791668d, 170.7905878307d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_16  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_16  &
   adams_id = 170  &
   location = 594.7863238165, 30.6936164681, 1244.7481721638  &
   orientation = 346.9720791648d, 9.20941217d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_16  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.jxs_joint_i_17  &
   adams_id = 171  &
   location = 0.0, 0.0, 0.0  &
   orientation = 2.4535349328d, 90.0000000003d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.jxs_joint_i_17  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_6  &
   adams_id = 172  &
   location = -773.2224062902, -5.0229377255E-06, -956.6499281917  &
   orientation = 90.000000212d, 109.5182717704d, 270.0000000708d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_6  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_6  &
   adams_id = 173  &
   location = -773.2224062697, -5.0320888359E-06, 956.6499282083  &
   orientation = 90.0000002118d, 70.4817282308d, 269.9999999292d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_6  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_17  &
   adams_id = 174  &
   location = 743.0840728289, 207.4318770183, -1284.3931894069  &
   orientation = 2.4535349328d, 90.0000000003d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_17  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_17  &
   adams_id = 175  &
   location = 743.0840728563, 207.431877006, 1284.3931893931  &
   orientation = 2.4535349328d, 90.0000000003d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_17  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.uel_gearaero_jjoint_1  &
   adams_id = 176  &
   location = 594.7863237899, 30.69361648, -1244.7481721762  &
   orientation = 346.9720791668d, 170.7905878307d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.uel_gearaero_jjoint_1  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ges_subframe_2.uer_gearaero_jjoint_1  &
   adams_id = 177  &
   location = 594.7863238165, 30.6936164681, 1244.7481721638  &
   orientation = 166.9720791648d, 170.79058783d, 180.0d
!
marker attributes  &
   marker_name = .template_6_motion.ges_subframe_2.uer_gearaero_jjoint_1  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ges_subframe_2  &
   mass = 4.5359237E-03  &
   center_of_mass_marker = .template_6_motion.ges_subframe_2.cm  &
   inertia_marker = .template_6_motion.ges_subframe_2.inertia_frame  &
   ixx = 2.9263965343  &
   iyy = 2.9263965343  &
   izz = 2.9263965343  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create curve outline  &
   outline_name = .template_6_motion.ges_subframe_2.graout_geom  &
   adams_id = 29  &
   marker_name =  &
      .template_6_motion.ges_subframe_2.graout_5,  &
      .template_6_motion.ges_subframe_2.graout_6,  &
      .template_6_motion.ges_subframe_2.graout_7,  &
      .template_6_motion.ges_subframe_2.graout_8,  &
      .template_6_motion.ges_subframe_2.graout_9,  &
      .template_6_motion.ges_subframe_2.graout_10  &
   visibility_between_markers = on, on, on, on, on, on  &
   close = yes
!
geometry attributes  &
   geometry_name = .template_6_motion.ges_subframe_2.graout_geom  &
   color = WHITE
!
part attributes  &
   part_name = .template_6_motion.ges_subframe_2  &
   visibility = off  &
   name_visibility = on
!
!----------------------------- gel_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_upper_cylinder  &
   adams_id = 4  &
   location = 1.2286012335E+04, -1472.9962565924, 1434.3428627157  &
   orientation = 55.1145661543d, 175.2828647319d, 235.2057167557d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_upper_cylinder.MARKER_343  &
   adams_id = 343  &
   location = 1.1796164248E-06, -1.0485166258E-08, 292.7550809696  &
   orientation = 304.7942832443d, 175.2828647319d, 124.8854338457d
!
marker create  &
   marker_name = .template_6_motion.gel_upper_cylinder.cm  &
   adams_id = 180  &
   location = -0.2075625052, 6.402390417, -14.6682621736  &
   orientation = 1.8568668039d, 1.1605595498d, 3.8737040848E-06d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_cylinder.gralin_12  &
   adams_id = 182  &
   location = 5.1261628276E-07, 1.721574272E-08, -721.5070810958  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_cylinder.gralin_12  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_cylinder.gralin_16  &
   adams_id = 183  &
   location = -12.6795804568, 391.0980589254, -678.1339506887  &
   orientation = 1.8570009567d, 40.3514751569d, 357.5638843637d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_cylinder.gralin_16  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_cylinder.gralin_20  &
   adams_id = 184  &
   location = -12.6795804568, 391.0980589254, -678.1339506887  &
   orientation = 1.8569054129d, 96.3249984425d, 196.3982137775d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_cylinder.gralin_20  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_j_12  &
   adams_id = 185  &
   location = 0.0, 0.0, 507.1310810647  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_j_12  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_i_16  &
   adams_id = 77  &
   location = -6.3397899721, 195.5490294713, -699.8205158923  &
   orientation = 1.856905383d, 96.3249984387d, 191.6681293622d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_i_16  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_j_4  &
   adams_id = 188  &
   location = 0.0, 0.0, 556.2289935088  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_j_4  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_i_7  &
   adams_id = 82  &
   location = -110.3647037077, 106.419112124, 131.0872656342  &
   orientation = 304.7942832443d, 175.2828647319d, 124.8854338457d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_i_7  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_upper_cylinder  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_cylinder.gralin_upper_cylinder  &
   adams_id = 1  &
   center_marker = .template_6_motion.gel_upper_cylinder.gralin_12  &
   angle_extent = 360.0000000012  &
   length = 1443.0141620972  &
   radius = 93.98  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_upper_cylinder.gralin_upper_cylinder  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_cylinder.gralin_geom  &
   adams_id = 2  &
   center_marker = .template_6_motion.gel_upper_cylinder.gralin_16  &
   angle_extent = 360.0000000012  &
   length = 452.9277435447  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_upper_cylinder.gralin_geom  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_cylinder.gralin_geom3  &
   adams_id = 3  &
   center_marker = .template_6_motion.gel_upper_cylinder.gralin_20  &
   angle_extent = 360.0000000012  &
   length = 393.7000024088  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_upper_cylinder.gralin_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_6_motion.gel_upper_cylinder  &
   visibility = on  &
   name_visibility = on
!
!----------------------------- ger_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_upper_cylinder  &
   adams_id = 16  &
   location = 1.2286012335E+04, 1472.9962565924, 1434.3428627157  &
   orientation = 124.8854338463d, 175.2828647319d, 304.7942832403d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_upper_cylinder.MARKER_347  &
   adams_id = 347  &
   location = 1.1794760724E-06, 1.0283551788E-08, 292.7550809696  &
   orientation = 235.2057167597d, 175.2828647319d, 55.1145661537d
!
marker create  &
   marker_name = .template_6_motion.ger_upper_cylinder.cm  &
   adams_id = 190  &
   location = -0.2075625043, -6.4023904165, -14.6682621736  &
   orientation = 178.1431332007d, 1.1605595498d, 179.9999961263d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_cylinder.gralin_13  &
   adams_id = 192  &
   location = 5.1297083942E-07, -1.6705477279E-08, -721.5070810958  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_cylinder.gralin_13  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_cylinder.gralin_17  &
   adams_id = 193  &
   location = -12.679580425, -391.098058926, -678.133950689  &
   orientation = 178.142999048d, 40.3514751568d, 182.4361156302d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_cylinder.gralin_17  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_cylinder.gralin_21  &
   adams_id = 194  &
   location = -12.679580425, -391.098058926, -678.133950689  &
   orientation = 178.1430945917d, 96.3249984425d, 343.6017862609d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_cylinder.gralin_21  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_j_12  &
   adams_id = 195  &
   location = 0.0, 0.0, 507.1310810647  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_j_12  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_i_16  &
   adams_id = 196  &
   location = -6.339789956, -195.5490294713, -699.8205158924  &
   orientation = 178.1430946199d, 96.3249984388d, 348.3318706358d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_i_16  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_j_4  &
   adams_id = 95  &
   location = 0.0, 0.0, 556.2289935088  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_j_4  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_i_7  &
   adams_id = 197  &
   location = -110.3647036992, -106.4191121329, 131.0872656341  &
   orientation = 235.2057167597d, 175.2828647319d, 55.1145661537d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_i_7  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_upper_cylinder  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_cylinder.gralin_upper_cylinder  &
   adams_id = 4  &
   center_marker = .template_6_motion.ger_upper_cylinder.gralin_13  &
   angle_extent = 360.0000000012  &
   length = 1443.0141620972  &
   radius = 93.98  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_upper_cylinder.gralin_upper_cylinder  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_cylinder.gralin_geom  &
   adams_id = 5  &
   center_marker = .template_6_motion.ger_upper_cylinder.gralin_17  &
   angle_extent = 360.0000000012  &
   length = 452.9277435447  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_upper_cylinder.gralin_geom  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_cylinder.gralin_geom3  &
   adams_id = 6  &
   center_marker = .template_6_motion.ger_upper_cylinder.gralin_21  &
   angle_extent = 360.0000000012  &
   length = 393.7000024088  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_upper_cylinder.gralin_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_6_motion.ger_upper_cylinder  &
   visibility = on  &
   name_visibility = on
!
!----------------------------- gel_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_lower_cylinder  &
   adams_id = 17  &
   location = 1.2338367977E+04, -1509.5002744656, 660.8546165914  &
   orientation = 55.1145661543d, 175.2828647319d, 235.2057167557d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_lower_cylinder.MARKER_344  &
   adams_id = 344  &
   location = 6.3843149631E-07, 1.0349051592E-08, -483.3620000578  &
   orientation = 304.7942832443d, 175.2828647319d, 124.8854338457d
!
marker create  &
   marker_name = .template_6_motion.gel_lower_cylinder.cm  &
   adams_id = 200  &
   location = 0.1955395801, -165.3276656918, 237.2067116265  &
   orientation = 6.7765910591E-02d, 24.9972742277d, 1.1756545836E-07d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_cylinder.gralin_14  &
   adams_id = 202  &
   location = 1.6938391662E-07, 1.1778859138E-08, -483.3620000261  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_cylinder.gralin_14  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_cylinder.gralin_22  &
   adams_id = 102  &
   location = 3.5838712553E-07, -5.0874665175E-06, 483.3620002128  &
   orientation = 6.7765789552E-02d, 86.3072194233d, 358.9479612442d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_cylinder.gralin_22  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_cylinder.jxl_joint_j_11  &
   adams_id = 103  &
   location = 114.1502169524, -26.2463754314, 381.6035459504  &
   orientation = 182.8112217133d, 89.9999933621d, 90.0001351788d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_cylinder.jxl_joint_j_11  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_cylinder.jxl_joint_i_12  &
   adams_id = 104  &
   location = -5.4152586929E-07, 2.0653468519E-08, -268.9859999627  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_cylinder.jxl_joint_i_12  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_cylinder.MARKER_352  &
   adams_id = 352  &
   location = 0.5024498973, -424.8194422366, 510.7801082549  &
   orientation = 180.0677652851d, 93.6935924781d, 1.0518000474d
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_6_motion.gel_lower_cylinder.FMARKER_345  &
   adams_id = 345
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_lower_cylinder  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_lower_cylinder.gralin_lower_cylinder  &
   adams_id = 7  &
   center_marker = .template_6_motion.gel_lower_cylinder.gralin_14  &
   angle_extent = 360.0000000012  &
   length = 966.724  &
   radius = 63.5  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_lower_cylinder.gralin_lower_cylinder  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_lower_cylinder.gralin_geom  &
   adams_id = 8  &
   center_marker = .template_6_motion.gel_lower_cylinder.gralin_22  &
   angle_extent = 360.0000000012  &
   length = 425.7036049693  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_lower_cylinder.gralin_geom  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_lower_cylinder.CYLINDER_84  &
   adams_id = 84  &
   center_marker = .template_6_motion.gel_lower_cylinder.MARKER_352  &
   angle_extent = 360.0  &
   length = 120.0  &
   radius = 160.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_motion.gel_lower_cylinder  &
   visibility = on  &
   name_visibility = on
!
!----------------------------- ger_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_lower_cylinder  &
   adams_id = 18  &
   location = 1.2338367977E+04, 1509.5002744656, 660.8546165914  &
   orientation = 124.8854338463d, 175.2828647319d, 304.7942832403d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_lower_cylinder.MARKER_348  &
   adams_id = 348  &
   location = 6.3866245625E-07, -1.001554395E-08, -483.3620000578  &
   orientation = 235.2057167597d, 175.2828647319d, 55.1145661537d
!
marker create  &
   marker_name = .template_6_motion.ger_lower_cylinder.cm  &
   adams_id = 109  &
   location = 0.1955395669, 165.3276656918, 237.2067116267  &
   orientation = 179.9322340941d, 24.9972742276d, 179.9999998824d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_cylinder.gralin_15  &
   adams_id = 111  &
   location = 1.6962145577E-07, -1.1437017999E-08, -483.3620000261  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_cylinder.gralin_15  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_cylinder.gralin_23  &
   adams_id = 112  &
   location = 3.5814959332E-07, 5.0871246729E-06, 483.3620002128  &
   orientation = 179.932234215d, 86.3072194232d, 181.0520386843d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_cylinder.gralin_23  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_cylinder.jxr_joint_j_11  &
   adams_id = 113  &
   location = 114.1502169501, 26.2463754403, 381.6035459505  &
   orientation = 357.1887782913d, 89.9999933622d, 89.9998648221d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_cylinder.jxr_joint_j_11  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_cylinder.jxr_joint_i_12  &
   adams_id = 114  &
   location = -5.4115088452E-07, -2.0105138041E-08, -268.9859999627  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_cylinder.jxr_joint_i_12  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_cylinder.MARKER_353  &
   adams_id = 353  &
   location = 0.502449863, 424.8194422362, 510.7801082552  &
   orientation = 359.9322347195d, 93.6935924781d, 178.948200024d
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_6_motion.ger_lower_cylinder.FMARKER_349  &
   adams_id = 349
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_lower_cylinder  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_lower_cylinder.gralin_lower_cylinder  &
   adams_id = 9  &
   center_marker = .template_6_motion.ger_lower_cylinder.gralin_15  &
   angle_extent = 360.0000000012  &
   length = 966.724  &
   radius = 63.5  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_lower_cylinder.gralin_lower_cylinder  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_lower_cylinder.gralin_geom  &
   adams_id = 10  &
   center_marker = .template_6_motion.ger_lower_cylinder.gralin_23  &
   angle_extent = 360.0000000012  &
   length = 425.7036049693  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_lower_cylinder.gralin_geom  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_lower_cylinder.CYLINDER_85  &
   adams_id = 85  &
   center_marker = .template_6_motion.ger_lower_cylinder.MARKER_353  &
   angle_extent = 360.0  &
   length = 120.0  &
   radius = 160.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_motion.ger_lower_cylinder  &
   visibility = on  &
   name_visibility = on
!
!---------------------------- gel_upper_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_upper_dragbrace  &
   adams_id = 19  &
   location = 1.1347700263E+04, -1130.692229848, 1810.57118708  &
   orientation = 69.1745865842d, 133.8457978591d, 255.2385761202d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_upper_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_upper_dragbrace.cm  &
   adams_id = 210  &
   location = 1.1488809085E-08, 1.605113282E-08, 0.0  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_dragbrace.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_dragbrace.gralin_24  &
   adams_id = 212  &
   location = 1.1488809903E-08, 1.6051132645E-08, -422.2750593684  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_dragbrace.gralin_24  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_dragbrace.jxl_joint_j_14  &
   adams_id = 213  &
   location = -1.1489920126E-08, -1.6050771823E-08, 422.2750593684  &
   orientation = 193.0027634257d, 90.0301580147d, 133.8272261409d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_dragbrace.jxl_joint_j_14  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_dragbrace.jxl_joint_i_5  &
   adams_id = 214  &
   location = 1.1488504592E-08, 1.6050619167E-08, -422.2750593684  &
   orientation = 12.9738149062d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_dragbrace.jxl_joint_i_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 127.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_upper_dragbrace  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_dragbrace.gralin_upper_dragbrace  &
   adams_id = 11  &
   center_marker = .template_6_motion.gel_upper_dragbrace.gralin_24  &
   angle_extent = 360.0000000012  &
   length = 844.5501187369  &
   radius = 30.48  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_upper_dragbrace.gralin_upper_dragbrace  &
   color = RED
!
part attributes  &
   part_name = .template_6_motion.gel_upper_dragbrace  &
   visibility = on  &
   name_visibility = on
!
!---------------------------- ger_upper_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_upper_dragbrace  &
   adams_id = 20  &
   location = 1.1347700263E+04, 1130.692229848, 1810.57118708  &
   orientation = 110.8254134164d, 133.8457978591d, 284.7614238815d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_upper_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_upper_dragbrace.cm  &
   adams_id = 216  &
   location = 1.2301381317E-08, -1.2967238219E-08, 0.0  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_dragbrace.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_dragbrace.gralin_25  &
   adams_id = 218  &
   location = 1.2301382135E-08, -1.2967238394E-08, -422.2750593684  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_dragbrace.gralin_25  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_dragbrace.jxr_joint_j_14  &
   adams_id = 219  &
   location = -1.2302492358E-08, 1.2966884511E-08, 422.2750593684  &
   orientation = 346.9972365738d, 90.0301580134d, 46.1727738591d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_dragbrace.jxr_joint_j_14  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_dragbrace.jxr_joint_i_5  &
   adams_id = 220  &
   location = 1.2301382135E-08, -1.2966377971E-08, -422.2750593684  &
   orientation = 347.0261850925d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_dragbrace.jxr_joint_i_5  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_upper_dragbrace  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_dragbrace.gralin_upper_dragbrace  &
   adams_id = 12  &
   center_marker = .template_6_motion.ger_upper_dragbrace.gralin_25  &
   angle_extent = 360.0000000012  &
   length = 844.5501187369  &
   radius = 30.48  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_upper_dragbrace.gralin_upper_dragbrace  &
   color = RED
!
part attributes  &
   part_name = .template_6_motion.ger_upper_dragbrace  &
   visibility = on  &
   name_visibility = on
!
!---------------------------- gel_lower_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_lower_dragbrace  &
   adams_id = 21  &
   location = 1.1921751947E+04, -1351.195614088, 1217.87350659  &
   orientation = 68.8036164539d, 134.040966186d, 254.9123665644d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_lower_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_lower_dragbrace.cm  &
   adams_id = 222  &
   location = 7.2486178034E-09, 2.6228538002E-09, 0.0  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_dragbrace.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_dragbrace.gralin_26  &
   adams_id = 224  &
   location = 7.2486183722E-09, 2.6228533234E-09, -431.8055559096  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_dragbrace.gralin_26  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_dragbrace.jxl_joint_i_14  &
   adams_id = 225  &
   location = 7.2484795943E-09, 2.6232419015E-09, -431.8055559096  &
   orientation = 193.0709676572d, 90.2906925288d, 133.6233654164d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_dragbrace.jxl_joint_i_14  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_dragbrace.jxl_joint_i_10  &
   adams_id = 226  &
   location = -7.2471195711E-09, -2.625691331E-09, 431.8055559096  &
   orientation = 193.0709676572d, 90.2906925288d, 133.6233654164d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_dragbrace.jxl_joint_i_10  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_lower_dragbrace  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_lower_dragbrace.gralin_lower_dragbrace  &
   adams_id = 13  &
   center_marker = .template_6_motion.gel_lower_dragbrace.gralin_26  &
   angle_extent = 360.0000000012  &
   length = 863.6111118191  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_lower_dragbrace.gralin_lower_dragbrace  &
   color = PEACH
!
part attributes  &
   part_name = .template_6_motion.gel_lower_dragbrace  &
   visibility = on  &
   name_visibility = on
!
!---------------------------- ger_lower_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_lower_dragbrace  &
   adams_id = 22  &
   location = 1.1921751947E+04, 1351.195614088, 1217.87350659  &
   orientation = 111.1963835467d, 134.040966186d, 285.0876334316d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_lower_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_lower_dragbrace.cm  &
   adams_id = 249  &
   location = 8.094746526E-09, 5.1568519392E-10, 0.0  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_dragbrace.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_dragbrace.gralin_27  &
   adams_id = 251  &
   location = 8.0947470948E-09, 5.1568471715E-10, -431.8055559096  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_dragbrace.gralin_27  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_dragbrace.jxr_joint_i_14  &
   adams_id = 252  &
   location = 8.0961626292E-09, 5.1596227291E-10, -431.8055559096  &
   orientation = 346.929032348d, 90.2906925275d, 46.3766345837d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_dragbrace.jxr_joint_i_14  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_dragbrace.jxr_joint_i_10  &
   adams_id = 253  &
   location = -8.0973283634E-09, -5.1589288397E-10, 431.8055559096  &
   orientation = 346.929032348d, 90.2906925275d, 46.3766345837d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_dragbrace.jxr_joint_i_10  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_lower_dragbrace  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_lower_dragbrace.gralin_lower_dragbrace  &
   adams_id = 14  &
   center_marker = .template_6_motion.ger_lower_dragbrace.gralin_27  &
   angle_extent = 360.0000000012  &
   length = 863.6111118191  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_lower_dragbrace.gralin_lower_dragbrace  &
   color = PEACH
!
part attributes  &
   part_name = .template_6_motion.ger_lower_dragbrace  &
   visibility = on  &
   name_visibility = on
!
!---------------------------- gel_upper_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_upper_torquearm  &
   adams_id = 23  &
   location = 1.2179452409E+04, -1493.9074516, 664.6292016  &
   orientation = 264.4801161285d, 168.6067018379d, 84.5882371543d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_upper_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_upper_torquearm.cm  &
   adams_id = 257  &
   location = -9.6342393338E-08, -8.1926566138E-10, -9.8313607255E-08  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_torquearm.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_torquearm.gralin_11  &
   adams_id = 259  &
   location = -9.6342392397E-08, -8.1926652962E-10, -138.3335383232  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_torquearm.gralin_11  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_torquearm.jxl_joint_i_2  &
   adams_id = 260  &
   location = -8.8413035226E-07, 4.5569242824E-09, 138.3335381266  &
   orientation = 273.4244432972d, 89.9999730565d, 177.0527624162d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_torquearm.jxl_joint_i_2  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upper_torquearm.jxl_joint_i_3  &
   adams_id = 261  &
   location = -9.6338909072E-08, -8.1972362925E-10, -138.3335383232  &
   orientation = 183.4245255497d, 87.0529837592d, 74.5991867893d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upper_torquearm.jxl_joint_i_3  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_upper_torquearm  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_torquearm.gralin_upper_torquearm  &
   adams_id = 15  &
   center_marker = .template_6_motion.gel_upper_torquearm.gralin_11  &
   angle_extent = 360.0000000012  &
   length = 276.6670764498  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_upper_torquearm.gralin_upper_torquearm  &
   color = GREEN
!
part attributes  &
   part_name = .template_6_motion.gel_upper_torquearm  &
   visibility = on  &
   name_visibility = on
!
!---------------------------- ger_upper_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_upper_torquearm  &
   adams_id = 24  &
   location = 1.2179452409E+04, 1493.9074516, 664.6292016  &
   orientation = 275.5198838732d, 168.6067018379d, 95.4117628463d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_upper_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_upper_torquearm.cm  &
   adams_id = 262  &
   location = -9.6418866888E-08, 1.2068905783E-11, -9.8313635011E-08  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_torquearm.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_torquearm.gralin_28  &
   adams_id = 264  &
   location = -9.6418865947E-08, 1.2068037542E-11, -138.3335383232  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_torquearm.gralin_28  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_torquearm.jxr_joint_i_2  &
   adams_id = 265  &
   location = -8.8405831961E-07, -3.7492045059E-09, 138.3335381266  &
   orientation = 266.5755567039d, 89.9999730565d, 2.9472375838d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_torquearm.jxr_joint_i_2  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upper_torquearm.jxr_joint_i_3  &
   adams_id = 266  &
   location = -9.6418865947E-08, 1.1845992937E-11, -138.3335383232  &
   orientation = 356.5754744514d, 87.0529837588d, 105.4008132115d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upper_torquearm.jxr_joint_i_3  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_upper_torquearm  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_torquearm.gralin_upper_torquearm  &
   adams_id = 16  &
   center_marker = .template_6_motion.ger_upper_torquearm.gralin_28  &
   angle_extent = 360.0000000012  &
   length = 276.6670764498  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_upper_torquearm.gralin_upper_torquearm  &
   color = GREEN
!
part attributes  &
   part_name = .template_6_motion.ger_upper_torquearm  &
   visibility = on  &
   name_visibility = on
!
!---------------------------- gel_lower_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_lower_torquearm  &
   adams_id = 25  &
   location = 1.2199342641E+04, -1557.9375115, 403.0923612  &
   orientation = 274.8068914916d, 21.5573785731d, 85.5279353334d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_lower_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_lower_torquearm.cm  &
   adams_id = 267  &
   location = 4.7209259312E-07, -7.4260276847E-09, -1.8307061422E-07  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_torquearm.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_torquearm.gralin_29  &
   adams_id = 269  &
   location = 4.7209259418E-07, -7.4260285421E-09, -138.7301714639  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_torquearm.gralin_29  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_torquearm.jxl_joint_i_11  &
   adams_id = 270  &
   location = 4.7208759818E-07, -7.4261937745E-09, -138.7301714639  &
   orientation = 178.1282944969d, 95.1813482698d, 287.4366992971d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_torquearm.jxl_joint_i_11  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lower_torquearm.jxl_joint_i_1  &
   adams_id = 271  &
   location = 4.5839965851E-07, -3.8524986153E-09, 138.7301710977  &
   orientation = 178.1282565407d, 95.1813639579d, 331.2687567692d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lower_torquearm.jxl_joint_i_1  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_lower_torquearm  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_lower_torquearm.gralin_lower_torquearm  &
   adams_id = 17  &
   center_marker = .template_6_motion.gel_lower_torquearm.gralin_29  &
   angle_extent = 360.0000000012  &
   length = 277.4603425616  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_lower_torquearm.gralin_lower_torquearm  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_6_motion.gel_lower_torquearm  &
   visibility = on  &
   name_visibility = on
!
!---------------------------- ger_lower_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_lower_torquearm  &
   adams_id = 26  &
   location = 1.2199342641E+04, 1557.9375115, 403.0923612  &
   orientation = 265.1931085101d, 21.5573785731d, 94.4720646672d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_lower_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_lower_torquearm.cm  &
   adams_id = 272  &
   location = 4.7197467356E-07, 5.9182298719E-09, -1.8307061422E-07  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_torquearm.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_torquearm.gralin_30  &
   adams_id = 274  &
   location = 4.7197467462E-07, 5.9182290145E-09, -138.7301714639  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_torquearm.gralin_30  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_torquearm.jxr_joint_i_11  &
   adams_id = 275  &
   location = 4.7197291214E-07, 5.9179943931E-09, -138.7301714639  &
   orientation = 1.8717055009d, 95.1813482692d, 252.5633007037d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_torquearm.jxr_joint_i_11  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lower_torquearm.jxr_joint_i_1  &
   adams_id = 276  &
   location = 4.5852151936E-07, 5.3608818773E-09, 138.7301710977  &
   orientation = 1.8717434569d, 95.1813639572d, 208.7312432325d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lower_torquearm.jxr_joint_i_1  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_lower_torquearm  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_lower_torquearm.gralin_lower_torquearm  &
   adams_id = 18  &
   center_marker = .template_6_motion.ger_lower_torquearm.gralin_30  &
   angle_extent = 360.0000000012  &
   length = 277.4603425616  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_lower_torquearm.gralin_lower_torquearm  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_6_motion.ger_lower_torquearm  &
   visibility = on  &
   name_visibility = on
!
!------------------------------ mts_body_mount_2 ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.mts_body_mount_2  &
   adams_id = 27  &
   location = 1.1750194959E+04, 0.0, 2128.24779709  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.mts_body_mount_2
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.mts_body_mount_2.mount_i  &
   adams_id = 277  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.mts_body_mount_2.mount_i  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.mts_body_mount_2.jxs_joint_j_17  &
   adams_id = 278  &
   location = -100.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.mts_body_mount_2.jxs_joint_j_17  &
   visibility = on  &
   name_visibility = off
!
part attributes  &
   part_name = .template_6_motion.mts_body_mount_2  &
   visibility = on  &
   name_visibility = on
!
!------------------------------- gel_connector --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_connector  &
   adams_id = 28  &
   location = 1.2149122257E+04, -1551.2110073, 531.6382052  &
   orientation = 177.0103140235d, 92.4964937736d, 309.8285622567d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_connector
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_connector.cm  &
   adams_id = 279  &
   location = 1.2967177626E-07, 1.5172074528E-07, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_connector.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_connector.gralin_3  &
   adams_id = 281  &
   location = 1.2967177679E-07, 1.5172074382E-07, -60.070847254  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_connector.gralin_3  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_connector.jxl_joint_j_1  &
   adams_id = 282  &
   location = -3.1902199251E-05, -3.9768573224E-05, -11.023458636  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_connector.jxl_joint_j_1  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_connector.jxl_joint_j_2  &
   adams_id = 283  &
   location = -1.2966941323E-07, -1.5171812483E-07, 60.070847254  &
   orientation = 331.5687749899d, 89.9998762031d, 89.9997713404d
!
marker attributes  &
   marker_name = .template_6_motion.gel_connector.jxl_joint_j_2  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_connector  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_connector.gralin_connector  &
   adams_id = 19  &
   center_marker = .template_6_motion.gel_connector.gralin_3  &
   angle_extent = 360.0000000012  &
   length = 120.1416945081  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_connector.gralin_connector  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_6_motion.gel_connector  &
   visibility = on  &
   name_visibility = on
!
!------------------------------- ger_connector --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_connector  &
   adams_id = 29  &
   location = 1.2149122257E+04, 1551.2110073, 531.6382052  &
   orientation = 2.9896859763d, 92.4964937736d, 230.171437745d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_connector
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_connector.cm  &
   adams_id = 284  &
   location = 1.2980595539E-07, -1.5188162475E-07, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_connector.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_connector.gralin_4  &
   adams_id = 286  &
   location = 1.2980595591E-07, -1.518816262E-07, -60.070847254  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_connector.gralin_4  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_connector.jxr_joint_j_1  &
   adams_id = 287  &
   location = -3.1902174627E-05, 3.9768543701E-05, -11.023458636  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_connector.jxr_joint_j_1  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_connector.jxr_joint_j_2  &
   adams_id = 288  &
   location = -1.2980359192E-07, 1.518790085E-07, 60.070847254  &
   orientation = 208.4312250084d, 89.9998762033d, 90.0002286592d
!
marker attributes  &
   marker_name = .template_6_motion.ger_connector.jxr_joint_j_2  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_connector  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_connector.gralin_connector  &
   adams_id = 20  &
   center_marker = .template_6_motion.ger_connector.gralin_4  &
   angle_extent = 360.0000000012  &
   length = 120.1416945081  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_connector.gralin_connector  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_6_motion.ger_connector  &
   visibility = on  &
   name_visibility = on
!
!------------------------------- gel_uc_collar --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_uc_collar  &
   adams_id = 30  &
   location = 1.2323534671E+04, -1499.1580221504, 879.997907387  &
   orientation = 55.1145661543d, 175.2828647319d, 235.2057167557d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_uc_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_uc_collar.cm  &
   adams_id = 289  &
   location = 1.4332251787E-07, 2.2791496906E-09, -1.11307491E-08  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_uc_collar.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_uc_collar.gralin_5  &
   adams_id = 291  &
   location = 1.4332251965E-07, 2.2791525611E-09, -108.9542389265  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_uc_collar.gralin_5  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_uc_collar.jxl_joint_j_3  &
   adams_id = 292  &
   location = 122.0018854948, 5.9907462805, 71.4829517815  &
   orientation = 182.8112217133d, 89.9999933621d, 90.0001351788d
!
marker attributes  &
   marker_name = .template_6_motion.gel_uc_collar.jxl_joint_j_3  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_uc_collar.jxl_joint_i_4  &
   adams_id = 293  &
   location = -5.9779835147E-07, 1.5128097042E-08, 4.0833567626E-08  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_uc_collar.jxl_joint_i_4  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_uc_collar.jxl_joint_j_10  &
   adams_id = 294  &
   location = 109.579670223, 33.566796853, -46.830310709  &
   orientation = 199.4445026708d, 90.0000000021d, 92.2365720472d
!
marker attributes  &
   marker_name = .template_6_motion.gel_uc_collar.jxl_joint_j_10  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_uc_collar  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_uc_collar.gralin_uc_collar  &
   adams_id = 21  &
   center_marker = .template_6_motion.gel_uc_collar.gralin_5  &
   angle_extent = 360.0000000012  &
   length = 217.9084778307  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_uc_collar.gralin_uc_collar  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_motion.gel_uc_collar  &
   visibility = on  &
   name_visibility = on
!
!------------------------------- ger_uc_collar --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_uc_collar  &
   adams_id = 31  &
   location = 1.2323534671E+04, 1499.1580221504, 879.997907387  &
   orientation = 124.8854338463d, 175.2828647319d, 304.7942832403d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_uc_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_uc_collar.cm  &
   adams_id = 295  &
   location = 1.4337606792E-07, -2.2021050864E-09, -1.1130638078E-08  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_uc_collar.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_uc_collar.gralin_6  &
   adams_id = 297  &
   location = 1.433760697E-07, -2.2021022159E-09, -108.9542389265  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_uc_collar.gralin_6  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_uc_collar.jxr_joint_j_3  &
   adams_id = 298  &
   location = 122.0018854952, -5.9907462708, 71.4829517815  &
   orientation = 357.1887782913d, 89.9999933622d, 89.9998648221d
!
marker attributes  &
   marker_name = .template_6_motion.ger_uc_collar.jxr_joint_j_3  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_uc_collar.jxr_joint_i_4  &
   adams_id = 299  &
   location = -5.9753074145E-07, -1.4735321291E-08, 4.0833816599E-08  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_uc_collar.jxr_joint_i_4  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_uc_collar.jxr_joint_j_10  &
   adams_id = 300  &
   location = 109.5796702257, -33.5667968442, -46.830310709  &
   orientation = 340.5554973333d, 90.0000000003d, 87.7634279528d
!
marker attributes  &
   marker_name = .template_6_motion.ger_uc_collar.jxr_joint_j_10  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_uc_collar  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_uc_collar.gralin_uc_collar  &
   adams_id = 22  &
   center_marker = .template_6_motion.ger_uc_collar.gralin_6  &
   angle_extent = 360.0000000012  &
   length = 217.9084778307  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_uc_collar.gralin_uc_collar  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_motion.ger_uc_collar  &
   visibility = on  &
   name_visibility = on
!
!-------------------------------- gel_spindle ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_spindle  &
   adams_id = 32  &
   location = 1.0970365356E+04, -989.53445476, 2099.11814999  &
   orientation = 70.4651745219d, 87.6875378758d, 270.820189182d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_spindle
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_spindle.cm  &
   adams_id = 301  &
   location = -2.0337021698E-09, 2.7104096439E-09, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_spindle.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_spindle.gralin_7  &
   adams_id = 303  &
   location = -2.0337013323E-09, 2.7104097097E-09, -98.4250027911  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_spindle.gralin_7  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_spindle.jxl_joint_j_5  &
   adams_id = 304  &
   location = 2.0332581105E-09, -2.7102992769E-09, 98.4250027911  &
   orientation = 357.8896246924d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_spindle.jxl_joint_j_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 127.0
!
marker create  &
   marker_name = .template_6_motion.gel_spindle.jxl_joint_i_6  &
   adams_id = 305  &
   location = -2.0337013323E-09, 2.7103056263E-09, -98.4250027911  &
   orientation = 270.0000005198d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_spindle.jxl_joint_i_6  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_spindle  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_spindle.gralin_spindle  &
   adams_id = 23  &
   center_marker = .template_6_motion.gel_spindle.gralin_7  &
   angle_extent = 360.0000000012  &
   length = 196.8500055822  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_spindle.gralin_spindle  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_motion.gel_spindle  &
   visibility = on  &
   name_visibility = on
!
!-------------------------------- ger_spindle ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_spindle  &
   adams_id = 33  &
   location = 1.0970365356E+04, 989.53445476, 2099.11814999  &
   orientation = 109.5348254787d, 87.6875378758d, 269.179810814d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_spindle
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_spindle.cm  &
   adams_id = 306  &
   location = -2.0484447173E-09, -1.6806593261E-09, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_spindle.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_spindle.gralin_8  &
   adams_id = 308  &
   location = -2.0484438798E-09, -1.6806592603E-09, -98.4250027911  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_spindle.gralin_8  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_spindle.jxr_joint_j_5  &
   adams_id = 309  &
   location = 2.0479997906E-09, 1.6805488275E-09, 98.4250027911  &
   orientation = 2.1103753116d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_spindle.jxr_joint_j_5  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_spindle.jxr_joint_i_6  &
   adams_id = 310  &
   location = -2.0484438798E-09, -1.6801353738E-09, -98.4250027911  &
   orientation = 269.9999994836d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_spindle.jxr_joint_i_6  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_spindle  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_spindle.gralin_spindle  &
   adams_id = 24  &
   center_marker = .template_6_motion.ger_spindle.gralin_8  &
   angle_extent = 360.0000000012  &
   length = 196.8500055822  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_spindle.gralin_spindle  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_motion.ger_spindle  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- gel_lwract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_lwract  &
   adams_id = 34  &
   location = 1.2403545058E+04, -1332.16553734, 1603.621623332  &
   orientation = 182.4778087722d, 7.7973026777d, 177.4990974087d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_lwract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_lwract.cm  &
   adams_id = 311  &
   location = -1.1395745624E-07, 1.2562562098E-08, 1.173505737E-10  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lwract.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lwract.gralin_9  &
   adams_id = 313  &
   location = -1.139574561E-07, 1.2562562102E-08, -300.2385778227  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lwract.gralin_9  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lwract.jxl_joint_j_7  &
   adams_id = 314  &
   location = -1.139574561E-07, 1.2562562102E-08, -300.2385778227  &
   orientation = 2.5009025913d, 7.7973026777d, 357.5221912278d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lwract.jxl_joint_j_7  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lwract.jxl_joint_i_8  &
   adams_id = 315  &
   location = 7.3965260349E-08, -1.2595334498E-08, 300.2385778229  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lwract.jxl_joint_i_8  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_lwract.MARKER_235  &
   adams_id = 235  &
   location = -1.1198686579E-07, 6.039613254E-11, -300.2385778227  &
   orientation = 2.5009025911d, 7.7973026777d, 357.5221912295d
!
marker attributes  &
   marker_name = .template_6_motion.gel_lwract.MARKER_235  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_lwract  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_lwract.gralin_lwract  &
   adams_id = 25  &
   center_marker = .template_6_motion.gel_lwract.gralin_9  &
   angle_extent = 360.0000000012  &
   length = 600.4771556456  &
   radius = 7.62  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_lwract.gralin_lwract  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_motion.gel_lwract  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- ger_lwract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_lwract  &
   adams_id = 35  &
   location = 1.2403545058E+04, 1332.16553734, 1603.621623332  &
   orientation = 357.5221912295d, 7.7973026777d, 2.5009025911d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_lwract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_lwract.cm  &
   adams_id = 321  &
   location = -1.1275005227E-07, -1.261529076E-08, 1.173505737E-10  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lwract.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lwract.gralin_10  &
   adams_id = 323  &
   location = -1.1275005213E-07, -1.2615290756E-08, -300.2385778227  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lwract.gralin_10  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lwract.jxr_joint_j_7  &
   adams_id = 324  &
   location = -1.1275005213E-07, -1.2615290756E-08, -300.2385778227  &
   orientation = 177.4990974089d, 7.7973026777d, 182.4778087705d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lwract.jxr_joint_j_7  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lwract.jxr_joint_i_8  &
   adams_id = 325  &
   location = 7.2752526009E-08, 1.2648701531E-08, 300.2385778229  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lwract.jxr_joint_i_8  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_lwract.MARKER_239  &
   adams_id = 239  &
   location = -1.1198508579E-07, -6.0568177378E-11, -300.2385778227  &
   orientation = 177.4990974087d, 7.7973026777d, 182.4778087722d
!
marker attributes  &
   marker_name = .template_6_motion.ger_lwract.MARKER_239  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_lwract  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_lwract.gralin_lwract  &
   adams_id = 26  &
   center_marker = .template_6_motion.ger_lwract.gralin_10  &
   angle_extent = 360.0000000012  &
   length = 600.4771556456  &
   radius = 7.62  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_lwract.gralin_lwract  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_motion.ger_lwract  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- gel_upract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.gel_upract  &
   adams_id = 36  &
   location = 1.2402626281E+04, -1310.9333827, 1758.81952274  &
   orientation = 182.4778087722d, 7.7973026777d, 177.4990974087d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.gel_upract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.gel_upract.cm  &
   adams_id = 330  &
   location = 3.8724207521E-08, 8.283765511E-09, -5.8633653488E-10  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upract.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upract.gralin_18  &
   adams_id = 332  &
   location = 3.8724208302E-08, 8.2837660342E-09, -195.8077681459  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upract.gralin_18  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upract.jxl_joint_j_8  &
   adams_id = 333  &
   location = 1.449393099E-07, -5.9360329152E-09, 143.592363306  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upract.jxl_joint_j_8  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upract.jxl_joint_i_17  &
   adams_id = 334  &
   location = 1.6127230497E-07, -8.1233179905E-09, 195.8077681447  &
   orientation = 2.5009025913d, 7.7973026777d, 357.5221912284d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upract.jxl_joint_i_17  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.gel_upract.MARKER_236  &
   adams_id = 236  &
   location = 1.5999113247E-07, 3.019806627E-11, 195.8077681447  &
   orientation = 2.5009025911d, 7.7973026777d, 357.5221912295d
!
marker attributes  &
   marker_name = .template_6_motion.gel_upract.MARKER_236  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.gel_upract  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.gel_upract.gralin_upract  &
   adams_id = 27  &
   center_marker = .template_6_motion.gel_upract.gralin_18  &
   angle_extent = 360.0000000012  &
   length = 391.6155362906  &
   radius = 17.78  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.gel_upract.gralin_upract  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_motion.gel_upract  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- ger_upract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_motion.ger_upract  &
   adams_id = 37  &
   location = 1.2402626281E+04, 1310.9333827, 1758.81952274  &
   orientation = 357.5221912295d, 7.7973026777d, 2.5009025911d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ger_upract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_motion.ger_upract.cm  &
   adams_id = 338  &
   location = 3.9509868554E-08, -8.3181591851E-09, -5.863087793E-10  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upract.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upract.gralin_19  &
   adams_id = 340  &
   location = 3.9509869335E-08, -8.3181586619E-09, -195.8077681459  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upract.gralin_19  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upract.jxr_joint_j_8  &
   adams_id = 341  &
   location = 1.443583019E-07, 5.9612245695E-09, 143.592363306  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upract.jxr_joint_j_8  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upract.jxr_joint_i_17  &
   adams_id = 230  &
   location = 1.6048486758E-07, 8.1574851041E-09, 195.8077681447  &
   orientation = 177.4990974089d, 7.7973026777d, 182.4778087711d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upract.jxr_joint_i_17  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_6_motion.ger_upract.MARKER_240  &
   adams_id = 240  &
   location = 1.5999113009E-07, -3.045271942E-11, 195.8077681447  &
   orientation = 177.4990974087d, 7.7973026777d, 182.4778087722d
!
marker attributes  &
   marker_name = .template_6_motion.ger_upract.MARKER_240  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .template_6_motion.ger_upract  &
   material_type = .template_6_motion.steel_2
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_motion.ger_upract.gralin_upract  &
   adams_id = 28  &
   center_marker = .template_6_motion.ger_upract.gralin_19  &
   angle_extent = 360.0000000012  &
   length = 391.6155362906  &
   radius = 17.78  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_motion.ger_upract.gralin_upract  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_motion.ger_upract  &
   visibility = on  &
   name_visibility = on
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_6_motion.josrev_lta_uta_joint  &
   adams_id = 4  &
   i_marker_name = .template_6_motion.ges_lower_torque_arm.jxs_joint_i_8  &
   j_marker_name = .template_6_motion.ges_upper_torque_arm.jxs_joint_j_8
!
constraint attributes  &
   constraint_name = .template_6_motion.josrev_lta_uta_joint  &
   visibility = on  &
   size_of_icons = 50.8
!
constraint create joint spherical  &
   joint_name = .template_6_motion.jossph_lta_lc_joint  &
   adams_id = 5  &
   i_marker_name = .template_6_motion.ges_lower_torque_arm.jxs_joint_i_9  &
   j_marker_name = .template_6_motion.ges_lower_cylinder.jxs_joint_j_9
!
constraint attributes  &
   constraint_name = .template_6_motion.jossph_lta_lc_joint  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.josrev_uta_uc_joint  &
   adams_id = 6  &
   i_marker_name = .template_6_motion.ges_upper_torque_arm.jxs_joint_i_10  &
   j_marker_name = .template_6_motion.ges_collar.jxs_joint_j_10
!
constraint attributes  &
   constraint_name = .template_6_motion.josrev_uta_uc_joint  &
   visibility = on
!
constraint create joint fixed  &
   joint_name = .template_6_motion.joscyl_lc_uc_joint  &
   adams_id = 7  &
   i_marker_name = .template_6_motion.ges_lower_cylinder.jxs_joint_i_11  &
   j_marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_j_11
!
constraint attributes  &
   constraint_name = .template_6_motion.joscyl_lc_uc_joint  &
   visibility = on
!
constraint create joint spherical  &
   joint_name = .template_6_motion.jossph_rd_uc  &
   adams_id = 1  &
   i_marker_name = .template_6_motion.ges_upper_cylinder.MARKER_4  &
   j_marker_name = .template_6_motion.ges_sf_rod.MARKER_5
!
constraint attributes  &
   constraint_name = .template_6_motion.jossph_rd_uc  &
   visibility = on  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_6_motion.josrev_uc_sf_joint  &
   adams_id = 8  &
   i_marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_i_15  &
   j_marker_name = .template_6_motion.ges_subframe.jxs_joint_j_15
!
constraint attributes  &
   constraint_name = .template_6_motion.josrev_uc_sf_joint  &
   visibility = on
!
constraint create joint fixed  &
   joint_name = .template_6_motion.mts_fixed_2  &
   adams_id = 9  &
   i_marker_name = .template_6_motion.mts_body_mount.mount_i  &
   j_marker_name = .template_6_motion.ground.mts_mount_j_2
!
constraint attributes  &
   constraint_name = .template_6_motion.mts_fixed_2  &
   visibility = on  &
   name_visibility = off
!
constraint create joint fixed  &
   joint_name = .template_6_motion.josfix_subframe_to_body  &
   adams_id = 10  &
   i_marker_name = .template_6_motion.ges_subframe.jxs_joint_i_16  &
   j_marker_name = .template_6_motion.mts_body_mount.jxs_joint_j_16
!
constraint attributes  &
   constraint_name = .template_6_motion.josfix_subframe_to_body  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.joscyl_db_sf  &
   adams_id = 11  &
   i_marker_name = .template_6_motion.ges_sf_actuator.jxs_joint_i_14  &
   j_marker_name = .template_6_motion.ges_subframe.jxs_joint_j_14
!
constraint attributes  &
   constraint_name = .template_6_motion.joscyl_db_sf  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.josrev_collar_uc_joint  &
   adams_id = 12  &
   i_marker_name = .template_6_motion.ges_collar.jxs_joint_i_1  &
   j_marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_j_1
!
constraint attributes  &
   constraint_name = .template_6_motion.josrev_collar_uc_joint  &
   visibility = on
!
constraint create joint cylindrical  &
   joint_name = .template_6_motion.joscly_ac_rd  &
   adams_id = 13  &
   i_marker_name = .template_6_motion.ges_sf_rod.MARKER_84  &
   j_marker_name = .template_6_motion.ges_sf_actuator.MARKER_85
!
constraint attributes  &
   constraint_name = .template_6_motion.joscly_ac_rd  &
   visibility = on  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jolrev_lta_lc_joint  &
   adams_id = 2  &
   i_marker_name = .template_6_motion.gel_lower_torquearm.jxl_joint_i_11  &
   j_marker_name = .template_6_motion.gel_lower_cylinder.jxl_joint_j_11
!
constraint attributes  &
   constraint_name = .template_6_motion.jolrev_lta_lc_joint  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jorrev_lta_lc_joint  &
   adams_id = 3  &
   i_marker_name = .template_6_motion.ger_lower_torquearm.jxr_joint_i_11  &
   j_marker_name = .template_6_motion.ger_lower_cylinder.jxr_joint_j_11
!
constraint attributes  &
   constraint_name = .template_6_motion.jorrev_lta_lc_joint  &
   visibility = on
!
constraint create joint cylindrical  &
   joint_name = .template_6_motion.jolcyl_lc_uc_joint  &
   adams_id = 15  &
   i_marker_name = .template_6_motion.gel_lower_cylinder.jxl_joint_i_12  &
   j_marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_j_12
!
constraint attributes  &
   constraint_name = .template_6_motion.jolcyl_lc_uc_joint  &
   visibility = on
!
constraint create joint cylindrical  &
   joint_name = .template_6_motion.jorcyl_lc_uc_joint  &
   adams_id = 16  &
   i_marker_name = .template_6_motion.ger_lower_cylinder.jxr_joint_i_12  &
   j_marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_j_12
!
constraint attributes  &
   constraint_name = .template_6_motion.jorcyl_lc_uc_joint  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jolrev_ldb_udb_joint  &
   adams_id = 17  &
   i_marker_name = .template_6_motion.gel_lower_dragbrace.jxl_joint_i_14  &
   j_marker_name = .template_6_motion.gel_upper_dragbrace.jxl_joint_j_14
!
constraint attributes  &
   constraint_name = .template_6_motion.jolrev_ldb_udb_joint  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jorrev_ldb_udb_joint  &
   adams_id = 18  &
   i_marker_name = .template_6_motion.ger_lower_dragbrace.jxr_joint_i_14  &
   j_marker_name = .template_6_motion.ger_upper_dragbrace.jxr_joint_j_14
!
constraint attributes  &
   constraint_name = .template_6_motion.jorrev_ldb_udb_joint  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jolrev_uc_sf_joint  &
   adams_id = 19  &
   i_marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_i_16  &
   j_marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_16
!
constraint attributes  &
   constraint_name = .template_6_motion.jolrev_uc_sf_joint  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jorrev_uc_sf_joint  &
   adams_id = 20  &
   i_marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_i_16  &
   j_marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_16
!
constraint attributes  &
   constraint_name = .template_6_motion.jorrev_uc_sf_joint  &
   visibility = on
!
constraint create joint fixed  &
   joint_name = .template_6_motion.mts_fixed_4  &
   adams_id = 21  &
   i_marker_name = .template_6_motion.mts_body_mount_2.mount_i  &
   j_marker_name = .template_6_motion.ground.mts_mount_j_4
!
constraint attributes  &
   constraint_name = .template_6_motion.mts_fixed_4  &
   visibility = on  &
   name_visibility = off
!
constraint create joint fixed  &
   joint_name = .template_6_motion.josfix_sf_body_joint  &
   adams_id = 22  &
   i_marker_name = .template_6_motion.ges_subframe_2.jxs_joint_i_17  &
   j_marker_name = .template_6_motion.mts_body_mount_2.jxs_joint_j_17
!
constraint attributes  &
   constraint_name = .template_6_motion.josfix_sf_body_joint  &
   visibility = on
!
constraint create joint fixed  &
   joint_name = .template_6_motion.jolcyl_lta_connect  &
   adams_id = 23  &
   i_marker_name = .template_6_motion.gel_lower_torquearm.jxl_joint_i_1  &
   j_marker_name = .template_6_motion.gel_connector.jxl_joint_j_1
!
constraint attributes  &
   constraint_name = .template_6_motion.jolcyl_lta_connect  &
   visibility = on
!
constraint create joint fixed  &
   joint_name = .template_6_motion.jorcyl_lta_connect  &
   adams_id = 24  &
   i_marker_name = .template_6_motion.ger_lower_torquearm.jxr_joint_i_1  &
   j_marker_name = .template_6_motion.ger_connector.jxr_joint_j_1
!
constraint attributes  &
   constraint_name = .template_6_motion.jorcyl_lta_connect  &
   visibility = on
!
constraint create joint fixed  &
   joint_name = .template_6_motion.jolrev_uta_connect  &
   adams_id = 25  &
   i_marker_name = .template_6_motion.gel_upper_torquearm.jxl_joint_i_2  &
   j_marker_name = .template_6_motion.gel_connector.jxl_joint_j_2
!
constraint attributes  &
   constraint_name = .template_6_motion.jolrev_uta_connect  &
   visibility = on
!
constraint create joint fixed  &
   joint_name = .template_6_motion.jorrev_uta_connect  &
   adams_id = 26  &
   i_marker_name = .template_6_motion.ger_upper_torquearm.jxr_joint_i_2  &
   j_marker_name = .template_6_motion.ger_connector.jxr_joint_j_2
!
constraint attributes  &
   constraint_name = .template_6_motion.jorrev_uta_connect  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jolrev_uta_collar  &
   adams_id = 27  &
   i_marker_name = .template_6_motion.gel_upper_torquearm.jxl_joint_i_3  &
   j_marker_name = .template_6_motion.gel_uc_collar.jxl_joint_j_3
!
constraint attributes  &
   constraint_name = .template_6_motion.jolrev_uta_collar  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jorrev_uta_collar  &
   adams_id = 28  &
   i_marker_name = .template_6_motion.ger_upper_torquearm.jxr_joint_i_3  &
   j_marker_name = .template_6_motion.ger_uc_collar.jxr_joint_j_3
!
constraint attributes  &
   constraint_name = .template_6_motion.jorrev_uta_collar  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jolrev_collar_uc  &
   adams_id = 29  &
   i_marker_name = .template_6_motion.gel_uc_collar.jxl_joint_i_4  &
   j_marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_j_4
!
constraint attributes  &
   constraint_name = .template_6_motion.jolrev_collar_uc  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jorrev_collar_uc  &
   adams_id = 30  &
   i_marker_name = .template_6_motion.ger_uc_collar.jxr_joint_i_4  &
   j_marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_j_4
!
constraint attributes  &
   constraint_name = .template_6_motion.jorrev_collar_uc  &
   visibility = on
!
constraint create joint spherical  &
   joint_name = .template_6_motion.jolhoo_udb_spndl  &
   adams_id = 31  &
   i_marker_name = .template_6_motion.gel_upper_dragbrace.jxl_joint_i_5  &
   j_marker_name = .template_6_motion.gel_spindle.jxl_joint_j_5
!
constraint attributes  &
   constraint_name = .template_6_motion.jolhoo_udb_spndl  &
   visibility = on
!
constraint create joint spherical  &
   joint_name = .template_6_motion.jorhoo_udb_spndl  &
   adams_id = 32  &
   i_marker_name = .template_6_motion.ger_upper_dragbrace.jxr_joint_i_5  &
   j_marker_name = .template_6_motion.ger_spindle.jxr_joint_j_5
!
constraint attributes  &
   constraint_name = .template_6_motion.jorhoo_udb_spndl  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jolrev_spndl_sf  &
   adams_id = 33  &
   i_marker_name = .template_6_motion.gel_spindle.jxl_joint_i_6  &
   j_marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_6
!
constraint attributes  &
   constraint_name = .template_6_motion.jolrev_spndl_sf  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jorrev_spndl_sf  &
   adams_id = 34  &
   i_marker_name = .template_6_motion.ger_spindle.jxr_joint_i_6  &
   j_marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_6
!
constraint attributes  &
   constraint_name = .template_6_motion.jorrev_spndl_sf  &
   visibility = on
!
constraint create joint spherical  &
   joint_name = .template_6_motion.jolsph_uc_lwract  &
   adams_id = 35  &
   i_marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_i_7  &
   j_marker_name = .template_6_motion.gel_lwract.jxl_joint_j_7
!
constraint attributes  &
   constraint_name = .template_6_motion.jolsph_uc_lwract  &
   visibility = on
!
constraint create joint spherical  &
   joint_name = .template_6_motion.jorsph_uc_lwract  &
   adams_id = 36  &
   i_marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_i_7  &
   j_marker_name = .template_6_motion.ger_lwract.jxr_joint_j_7
!
constraint attributes  &
   constraint_name = .template_6_motion.jorsph_uc_lwract  &
   visibility = on
!
constraint create joint translational  &
   joint_name = .template_6_motion.sf_left  &
   adams_id = 37  &
   i_marker_name = .template_6_motion.gel_lwract.jxl_joint_i_8  &
   j_marker_name = .template_6_motion.gel_upract.jxl_joint_j_8
!
constraint attributes  &
   constraint_name = .template_6_motion.sf_left  &
   visibility = on
!
constraint create joint translational  &
   joint_name = .template_6_motion.sf_right  &
   adams_id = 38  &
   i_marker_name = .template_6_motion.ger_lwract.jxr_joint_i_8  &
   j_marker_name = .template_6_motion.ger_upract.jxr_joint_j_8
!
constraint attributes  &
   constraint_name = .template_6_motion.sf_right  &
   visibility = on
!
constraint create joint spherical  &
   joint_name = .template_6_motion.jolsph_upract_sf  &
   adams_id = 39  &
   i_marker_name = .template_6_motion.gel_upract.jxl_joint_i_17  &
   j_marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_17
!
constraint attributes  &
   constraint_name = .template_6_motion.jolsph_upract_sf  &
   visibility = on
!
constraint create joint spherical  &
   joint_name = .template_6_motion.jorsph_upract_sf  &
   adams_id = 40  &
   i_marker_name = .template_6_motion.ger_upract.jxr_joint_i_17  &
   j_marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_17
!
constraint attributes  &
   constraint_name = .template_6_motion.jorsph_upract_sf  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jolrev_ldb_collar  &
   adams_id = 41  &
   i_marker_name = .template_6_motion.gel_lower_dragbrace.jxl_joint_i_10  &
   j_marker_name = .template_6_motion.gel_uc_collar.jxl_joint_j_10
!
constraint attributes  &
   constraint_name = .template_6_motion.jolrev_ldb_collar  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_6_motion.jorrev_ldb_collar  &
   adams_id = 42  &
   i_marker_name = .template_6_motion.ger_lower_dragbrace.jxr_joint_i_10  &
   j_marker_name = .template_6_motion.ger_uc_collar.jxr_joint_j_10
!
constraint attributes  &
   constraint_name = .template_6_motion.jorrev_ldb_collar  &
   visibility = on
!
!----------------------------------- Forces -----------------------------------!
!
!
force create direct general_force  &
   general_force_name = .template_6_motion.NLG_aeroforce  &
   adams_id = 2  &
   i_marker_name = .template_6_motion.ges_lower_cylinder.MARKER_106  &
   j_floating_marker_name =   &
                            .template_6_motion.ges_upper_cylinder.FMARKER_107  &
   ref_marker_name = .template_6_motion.ges_upper_cylinder.MARKER_aeroforce  &
   x_force_function = ""  &
   y_force_function = ""  &
   z_force_function = ""  &
   x_torque_function = ""  &
   y_torque_function = ""  &
   z_torque_function = ""
!
force create direct general_force  &
   general_force_name = .template_6_motion.aeroforce_MLG_L  &
   adams_id = 3  &
   i_marker_name = .template_6_motion.gel_upper_cylinder.MARKER_343  &
   j_floating_marker_name =   &
                            .template_6_motion.gel_lower_cylinder.FMARKER_345  &
   ref_marker_name = .template_6_motion.gel_lower_cylinder.MARKER_344  &
   x_force_function = ""  &
   y_force_function = ""  &
   z_force_function = ""  &
   x_torque_function = ""  &
   y_torque_function = ""  &
   z_torque_function = ""
!
force create direct general_force  &
   general_force_name = .template_6_motion.aeroforce_MLG_R  &
   adams_id = 4  &
   i_marker_name = .template_6_motion.ger_upper_cylinder.MARKER_347  &
   j_floating_marker_name =   &
                            .template_6_motion.ger_lower_cylinder.FMARKER_349  &
   ref_marker_name = .template_6_motion.ger_lower_cylinder.MARKER_348  &
   x_force_function = ""  &
   y_force_function = ""  &
   z_force_function = ""  &
   x_torque_function = ""  &
   y_torque_function = ""  &
   z_torque_function = ""
!
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .template_6_motion.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=10.0 step_size=1.0E-02 model_name=.gcmb6_motion"
!
simulation script create  &
   sim_script_name = .template_6_motion.Last_Sim_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry create shape force  &
   force_name = .template_6_motion.aeroforce_force_graphic_1  &
   adams_id = 42  &
   force_element_name = .template_6_motion.NLG_aeroforce  &
   applied_at_marker_name = .template_6_motion.ges_lower_cylinder.MARKER_106
!
geometry create shape force  &
   force_name = .template_6_motion.GFORCE_3_force_graphic_1  &
   adams_id = 43  &
   force_element_name = .template_6_motion.aeroforce_MLG_L  &
   applied_at_marker_name = .template_6_motion.gel_upper_cylinder.MARKER_343
!
geometry create shape force  &
   force_name = .template_6_motion.GFORCE_4_force_graphic_1  &
   adams_id = 44  &
   force_element_name = .template_6_motion.aeroforce_MLG_R  &
   applied_at_marker_name = .template_6_motion.ger_upper_cylinder.MARKER_347
!
!---------------------------------- Motions -----------------------------------!
!
!
constraint create motion_generator  &
   motion_name = .template_6_motion.MOTION_disp  &
   adams_id = 2  &
   type_of_freedom = translational  &
   joint_name = .template_6_motion.joscly_ac_rd  &
   function = ""
!
constraint attributes  &
   constraint_name = .template_6_motion.MOTION_disp  &
   visibility = off  &
   name_visibility = off
!
constraint create motion_generator  &
   motion_name = .template_6_motion.MOTION_LEFT  &
   adams_id = 4  &
   type_of_freedom = translational  &
   joint_name = .template_6_motion.sf_left  &
   function = ""
!
constraint attributes  &
   constraint_name = .template_6_motion.MOTION_LEFT  &
   visibility = off  &
   name_visibility = off
!
constraint create motion_generator  &
   motion_name = .template_6_motion.MOTION_RIGHT  &
   adams_id = 5  &
   type_of_freedom = translational  &
   joint_name = .template_6_motion.sf_right  &
   function = ""
!
constraint attributes  &
   constraint_name = .template_6_motion.MOTION_RIGHT  &
   visibility = off  &
   name_visibility = off
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   x_component_gravity = 0.0  &
   y_component_gravity = 0.0  &
   z_component_gravity = -9806.65
!
force attributes  &
   force_name = .template_6_motion.gravity  &
   visibility = off  &
   size_of_icons = 50.8
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------------- Measures ----------------------------------!
!
!
measure create object  &
   measure_name = .template_6_motion.NLG_sf_angle  &
   from_first = yes  &
   object = .template_6_motion.josrev_uc_sf_joint  &
   characteristic = ax_ay_az_projection_angles  &
   component = z_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_motion.NLG_sf_angle  &
   color = WHITE
!
measure create object  &
   measure_name = .template_6_motion.vel  &
   from_first = yes  &
   object = .template_6_motion.joscly_ac_rd  &
   characteristic = translational_velocity  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_motion.vel  &
   color = WHITE
!
measure create object  &
   measure_name = .template_6_motion.MLG_sf_angle  &
   from_first = yes  &
   object = .template_6_motion.jolrev_uc_sf_joint  &
   characteristic = ax_ay_az_projection_angles  &
   component = z_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_motion.MLG_sf_angle  &
   color = WHITE
!
measure create object  &
   measure_name = .template_6_motion.vel_left  &
   from_first = yes  &
   object = .template_6_motion.sf_left  &
   characteristic = translational_velocity  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_motion.vel_left  &
   color = WHITE
!
measure create object  &
   measure_name = .template_6_motion.vel_right  &
   from_first = yes  &
   object = .template_6_motion.sf_right  &
   characteristic = translational_velocity  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_motion.vel_right  &
   color = WHITE
!
measure create pt2pt  &
   measure_name = .template_6_motion.disp_sf  &
   from_point = .template_6_motion.ges_sf_rod.MARKER_96  &
   to_point = .template_6_motion.ges_sf_actuator.MARKER_97  &
   characteristic = translational_displacement  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_motion.disp_sf  &
   color = WHITE
!
measure create pt2pt  &
   measure_name = .template_6_motion.disp_sf_left  &
   from_point = .template_6_motion.gel_lwract.MARKER_235  &
   to_point = .template_6_motion.gel_upract.MARKER_236  &
   characteristic = translational_displacement  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_motion.disp_sf_left  &
   color = WHITE
!
measure create pt2pt  &
   measure_name = .template_6_motion.disp_sf_right  &
   from_point = .template_6_motion.ger_lwract.MARKER_239  &
   to_point = .template_6_motion.ger_upract.MARKER_240  &
   characteristic = translational_displacement  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_motion.disp_sf_right  &
   color = WHITE
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_6_motion.mts_body_mount.minor_role  &
   string_value = "inherit"
!
variable create  &
   variable_name = .template_6_motion.mts_body_mount_2.minor_role  &
   string_value = "inherit"
!
variable create  &
   variable_name = .template_6_motion.AIR_VELOCITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 55.0
!
variable create  &
   variable_name = .template_6_motion.AIR_DENSITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_6_motion.NLG_DRAG_COEFF  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.7
!
variable create  &
   variable_name = .template_6_motion.NLG_PROJ_AREA  &
   units = "area"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.3077
!
variable create  &
   variable_name = .template_6_motion.NLG_RETRACT_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 4.5
!
variable create  &
   variable_name = .template_6_motion.NLG_UP_HOLD_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_6_motion.NLG_EXTEND_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
variable create  &
   variable_name = .template_6_motion.MLG_RETRACT_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 4.5
!
variable create  &
   variable_name = .template_6_motion.MLG_UP_HOLD_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_6_motion.MLG_EXTEND_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
variable create  &
   variable_name = .template_6_motion.MLG_PROJ_AREA  &
   units = "area"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.418
!
variable create  &
   variable_name = .template_6_motion.MLG_DRAG_COEFF  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.7
!
variable create  &
   variable_name = .template_6_motion.NLG_ACTUATOR_STROKE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 635.0
!
variable create  &
   variable_name = .template_6_motion.MLG_ACTUATOR_STROKE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 345.0
!
!---------------------------- Function definitions ----------------------------!
!
!
constraint modify motion_generator  &
   motion_name = .template_6_motion.MOTION_disp  &
   function = "-STEP( time , 0 , 0 , .template_6_motion.NLG_RETRACT_TIME , .template_6_motion.NLG_ACTUATOR_STROKE )-STEP( time , .template_6_motion.NLG_RETRACT_TIME+.template_6_motion.NLG_UP_HOLD_TIME , 0 ,  .template_6_motion.NLG_RETRACT_TIME+.template_6_motion.NLG_UP_HOLD_TIME+.template_6_motion.NLG_EXTEND_TIME , -.template_6_motion.NLG_ACTUATOR_STROKE )"
!
constraint modify motion_generator  &
   motion_name = .template_6_motion.MOTION_LEFT  &
   function = "-STEP( time , 0 , 1 , .template_6_motion.MLG_RETRACT_TIME , .template_6_motion.MLG_ACTUATOR_STROKE )-STEP( time , .template_6_motion.MLG_RETRACT_TIME+.template_6_motion.MLG_UP_HOLD_TIME , 0 , .template_6_motion.MLG_RETRACT_TIME+.template_6_motion.MLG_UP_HOLD_TIME+.template_6_motion.MLG_EXTEND_TIME , -.template_6_motion.MLG_ACTUATOR_STROKE )"
!
constraint modify motion_generator  &
   motion_name = .template_6_motion.MOTION_RIGHT  &
   function = "-STEP( time , 0 , 1 , .template_6_motion.MLG_RETRACT_TIME , .template_6_motion.MLG_ACTUATOR_STROKE )-STEP( time , .template_6_motion.MLG_RETRACT_TIME+.template_6_motion.MLG_UP_HOLD_TIME , 0 , .template_6_motion.MLG_RETRACT_TIME+.template_6_motion.MLG_UP_HOLD_TIME+.template_6_motion.MLG_EXTEND_TIME , -.template_6_motion.MLG_ACTUATOR_STROKE )"
!
force modify direct general_force  &
   general_force_name = .template_6_motion.NLG_aeroforce  &
   x_force_function = ".template_6_motion.NLG_DRAG_COEFF*abs(IF( .template_6_motion.NLG_sf_angle-60 : COS( 1.225*.template_6_motion.NLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.NLG_sf_angle*pi/180 ) , COS( .template_6_motion.NLG_sf_angle*pi/180 ) ))*.template_6_motion.NLG_PROJ_AREA*cos(.template_6_motion.NLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*cos(.template_6_motion.NLG_sf_angle*pi/180) "  &
   y_force_function = "0"  &
   z_force_function = ".template_6_motion.NLG_DRAG_COEFF*abs(IF( .template_6_motion.NLG_sf_angle-60 : COS( 1.225*.template_6_motion.NLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.NLG_sf_angle*pi/180 ) , COS( .template_6_motion.NLG_sf_angle*pi/180 ) ))*.template_6_motion.NLG_PROJ_AREA*cos(.template_6_motion.NLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*sin(.template_6_motion.NLG_sf_angle*pi/180) "  &
   x_torque_function = "0"  &
   y_torque_function = "-1*CUBSPL( .template_6_motion.NLG_sf_angle, 0 , .template_6_motion.SPLINE_angle_aeroforce_NLG, 0 )"  &
   z_torque_function = "0"
!
force modify direct general_force  &
   general_force_name = .template_6_motion.aeroforce_MLG_L  &
   x_force_function = ".template_6_motion.MLG_DRAG_COEFF*abs(IF( .template_6_motion.MLG_sf_angle-60 : COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( .template_6_motion.MLG_sf_angle*pi/180 ) ))*.template_6_motion.MLG_PROJ_AREA*cos(.template_6_motion.MLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*cos(.template_6_motion.MLG_sf_angle*pi/180) "  &
   y_force_function = "0"  &
   z_force_function = ".template_6_motion.MLG_DRAG_COEFF*abs(IF( .template_6_motion.MLG_sf_angle-60 : COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( .template_6_motion.MLG_sf_angle*pi/180 ) ))*.template_6_motion.MLG_PROJ_AREA*cos(.template_6_motion.MLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*sin(.template_6_motion.MLG_sf_angle*pi/180) "  &
   x_torque_function = "0"  &
   y_torque_function = "-1*CUBSPL( .template_6_motion.MLG_sf_angle, 0 , .template_6_motion.SPLINE_angle_aeroforce_MLG, 0 )"  &
   z_torque_function = "0"
!
force modify direct general_force  &
   general_force_name = .template_6_motion.aeroforce_MLG_R  &
   x_force_function = ".template_6_motion.MLG_DRAG_COEFF*abs(IF( .template_6_motion.MLG_sf_angle-60 : COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( .template_6_motion.MLG_sf_angle*pi/180 ) ))*.template_6_motion.MLG_PROJ_AREA*cos(.template_6_motion.MLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*cos(.template_6_motion.MLG_sf_angle*pi/180) "  &
   y_force_function = "0"  &
   z_force_function = ".template_6_motion.MLG_DRAG_COEFF*abs(IF( .template_6_motion.MLG_sf_angle-60 : COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( .template_6_motion.MLG_sf_angle*pi/180 ) ))*.template_6_motion.MLG_PROJ_AREA*cos(.template_6_motion.MLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*sin(.template_6_motion.MLG_sf_angle*pi/180) "  &
   x_torque_function = "0"  &
   y_torque_function = "-1*CUBSPL( .template_6_motion.MLG_sf_angle, 0 , .template_6_motion.SPLINE_angle_aeroforce_MLG, 0 )"  &
   z_torque_function = "0"
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_6_motion.ground.mts_mount_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.mts_body_mount))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.mts_body_mount))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfs_nlg_axle_lowpoint  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hps_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_6_motion.ground.hps_uc_bot, .template_6_motion.ground.hps_uc_top, 0.11 * DM(.template_6_motion.ground.hps_uc_bot, .template_6_motion.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_uc_bot, .template_6_motion.ground.hps_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.mts_mount_j_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.mts_body_mount_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.mts_body_mount_2))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_axial_reference  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_lc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_lc_bot, .template_6_motion.ground.hpl_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_axial_reference  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_lc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_lc_bot, .template_6_motion.ground.hpr_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_uc_bot  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 21.18}inch, .template_6_motion.ground.cfl_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_uc_bot  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 21.18}inch, .template_6_motion.ground.cfr_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_uc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_uc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_lc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 38.06}inch, .template_6_motion.ground.cfl_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_lc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 38.06}inch, .template_6_motion.ground.cfr_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_6_motion.ground.hpl_uc_top, .template_6_motion.ground.hpl_lc_bot, 0.59 * DM(.template_6_motion.ground.hpl_uc_top, .template_6_motion.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_uc_top, .template_6_motion.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_6_motion.ground.hpr_uc_top, .template_6_motion.ground.hpr_lc_bot, 0.59 * DM(.template_6_motion.ground.hpr_uc_top, .template_6_motion.ground.hpr_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_uc_top, .template_6_motion.ground.hpr_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_collar_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_6_motion.ground.hpl_uc_top, .template_6_motion.ground.hpl_lc_bot, 0.7 * DM(.template_6_motion.ground.hpl_uc_top, .template_6_motion.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_uc_top, .template_6_motion.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_collar_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_6_motion.ground.hpr_uc_top, .template_6_motion.ground.hpr_lc_bot, 0.7 * DM(.template_6_motion.ground.hpr_uc_top, .template_6_motion.ground.hpr_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_uc_top, .template_6_motion.ground.hpr_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_plane_ref_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfl_plane_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, -90.0, 0.0}degrees, .template_6_motion.ground.cfl_plane_ref))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_plane_ref_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfr_plane_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_6_motion.ground.cfr_plane_ref))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_lwract_top  &
   location =   &
      (LOC_ALONG_LINE(.template_6_motion.ground.hpl_lwract_uc_atch_1, .template_6_motion.ground.hpl_upract_sf_atch_1, 0.92 * DM(.template_6_motion.ground.hpl_lwract_uc_atch_1, .template_6_motion.ground.hpl_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_lwract_uc_atch_1, .template_6_motion.ground.hpl_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_lwract_top  &
   location =   &
      (LOC_ALONG_LINE(.template_6_motion.ground.hpr_lwract_uc_atch_1, .template_6_motion.ground.hpr_upract_sf_atch_1, 0.92 * DM(.template_6_motion.ground.hpr_lwract_uc_atch_1, .template_6_motion.ground.hpr_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_lwract_uc_atch_1, .template_6_motion.ground.hpr_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_upract_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_6_motion.ground.hpl_lwract_uc_atch_1, .template_6_motion.ground.hpl_upract_sf_atch_1, 0.4 * DM(.template_6_motion.ground.hpl_lwract_uc_atch_1, .template_6_motion.ground.hpl_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_lwract_uc_atch_1, .template_6_motion.ground.hpl_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_upract_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_6_motion.ground.hpr_lwract_uc_atch_1, .template_6_motion.ground.hpr_upract_sf_atch_1, 0.4 * DM(.template_6_motion.ground.hpr_lwract_uc_atch_1, .template_6_motion.ground.hpr_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_lwract_uc_atch_1, .template_6_motion.ground.hpr_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfl_spin_axis_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_wheel_center1, .template_6_motion.ground.hpl_ob_axle1, "Z"))
!
marker modify  &
   marker_name = .template_6_motion.ground.cfr_spin_axis_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_wheel_center1, .template_6_motion.ground.hpr_ob_axle1, "Z"))
!
material modify  &
   material_name = .template_6_motion.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_motion.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_motion.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_motion.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .template_6_motion.ges_sf_actuator.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_db_sf_atch, .template_6_motion.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .template_6_motion.ges_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_sf_actuator.jxs_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe.jxs_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe.jxs_joint_j_14))  &
   relative_to = .template_6_motion.ges_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_sf_actuator.gralin_dragbrace_geom  &
   length = (DM(.template_6_motion.ground.hps_db_sf_atch, .template_6_motion.ground.hps_db_uc_atch) - 50)
!
marker modify  &
   marker_name = .template_6_motion.ges_upper_cylinder.MARKER_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_sf_rod.PT3))  &
   relative_to = .template_6_motion.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_uc_top, .template_6_motion.ground.hps_uc_bot, "Z"))  &
   relative_to = .template_6_motion.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_uc_sf_atch_l, .template_6_motion.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_6_motion.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_uc_sf_atch_r, .template_6_motion.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_6_motion.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_i_15  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe.jxs_joint_j_15))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe.jxs_joint_j_15))  &
   relative_to = .template_6_motion.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_uc_bot, .template_6_motion.ground.hps_uc_top, "Z"))  &
   relative_to = .template_6_motion.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.template_6_motion.ground.hps_uc_top, .template_6_motion.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.template_6_motion.ground.hps_uc_sf_atch_l, .template_6_motion.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.template_6_motion.ground.hps_uc_sf_atch_r, .template_6_motion.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .template_6_motion.ges_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_lc_top, .template_6_motion.ground.hps_lc_bot, "Z"))  &
   relative_to = .template_6_motion.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_lower_cylinder.jxs_joint_j_9  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo))  &
   relative_to = .template_6_motion.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .template_6_motion.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_lower_cylinder.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_wheel_center, .template_6_motion.ground.hpl_wheel_center, "Z"))  &
   relative_to = .template_6_motion.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_lower_cylinder.MARKER_350  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_ob_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_ob_axle, .template_6_motion.ground.hpl_wheel_center, "Z"))  &
   relative_to = .template_6_motion.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_lower_cylinder.MARKER_351  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_ob_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_ob_axle, .template_6_motion.ground.hpr_wheel_center, "Z"))  &
   relative_to = .template_6_motion.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_lower_cylinder.gralin_geom1  &
   length = (DM(.template_6_motion.ground.hps_lc_top, .template_6_motion.ground.hps_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_lower_cylinder.gralin_geom2  &
   length = (DM(.template_6_motion.ground.hpr_wheel_center, .template_6_motion.ground.hpl_wheel_center))
!
marker modify  &
   marker_name = .template_6_motion.ges_upper_torque_arm.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_uta_uc_atch, .template_6_motion.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_6_motion.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_upper_torque_arm.jxs_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hps_lta_uta_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_6_motion.ground.origo))  &
   relative_to = .template_6_motion.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_upper_torque_arm.jxs_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_collar.jxs_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_collar.jxs_joint_j_10))  &
   relative_to = .template_6_motion.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   length = (DM(.template_6_motion.ground.hps_uta_uc_atch, .template_6_motion.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_6_motion.ges_lower_torque_arm.jxs_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_upper_torque_arm.jxs_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_upper_torque_arm.jxs_joint_j_8))  &
   relative_to = .template_6_motion.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_lower_torque_arm.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_lta_lc_atch, .template_6_motion.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_6_motion.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_lower_torque_arm.jxs_joint_i_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_lower_cylinder.jxs_joint_j_9))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_lower_cylinder.jxs_joint_j_9))  &
   relative_to = .template_6_motion.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   length = (DM(.template_6_motion.ground.hps_lta_lc_atch, .template_6_motion.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe))  &
   relative_to = .template_6_motion.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe.graout_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_uc_sf_atch_r))  &
   relative_to = .template_6_motion.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe.graout_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_uc_sf_atch_l))  &
   relative_to = .template_6_motion.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe.graout_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_db_sf_atch))  &
   relative_to = .template_6_motion.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe.jxs_joint_j_15  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfs_uc_sf_atch_mid))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_6_motion.ground.cfs_uc_sf_atch_mid, "Z+Z"), .template_6_motion.ges_subframe))  &
   relative_to = .template_6_motion.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe.jxs_joint_i_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.mts_body_mount.jxs_joint_j_16))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.mts_body_mount.jxs_joint_j_16))  &
   relative_to = .template_6_motion.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe.jxs_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_6_motion.ground.origo))  &
   relative_to = .template_6_motion.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.mts_body_mount.jxs_joint_j_16  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo))  &
   relative_to = .template_6_motion.mts_body_mount
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part modify rigid_body name_and_position  &
   part_name = .template_6_motion.mts_body_mount  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.origo))
!
marker modify  &
   marker_name = .template_6_motion.ges_collar.jxs_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_6_motion.ground.origo))  &
   relative_to = .template_6_motion.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_collar.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hps_uc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hps_uc_bot, .template_6_motion.ground.cfs_collar_top, "Z"))  &
   relative_to = .template_6_motion.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_6_motion.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_collar.gralin_collar  &
   length = (DM(.template_6_motion.ground.hps_uc_bot, .template_6_motion.ground.cfs_collar_top))
!
marker modify  &
   marker_name = .template_6_motion.ges_sf_rod.MARKER_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_sf_rod.PT3))  &
   relative_to = .template_6_motion.ges_sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_sf_rod.gralin_25  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}, .template_6_motion.ground.hps_rod_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ges_sf_rod.PT3, .template_6_motion.ground.hps_db_sf_atch, "Z"))  &
   relative_to = .template_6_motion.ges_sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ges_sf_rod.CYLINDER_30  &
   length = (DM(.template_6_motion.ground.hps_rod_bot, .template_6_motion.ground.hps_rod_top))  &
   radius = (27.5mm)
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.graout_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_udb_spndl_atch_1))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.graout_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_udb_spndl_atch_1))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.graout_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_uc_top))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.graout_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_ib_uc_sf_atch))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.graout_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_ib_uc_sf_atch))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.graout_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_uc_top))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_16  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfl_uc_sf_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.cfl_uc_sf_atch))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_16  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfr_uc_sf_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.cfr_uc_sf_atch))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.jxs_joint_i_17  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.mts_body_mount_2.jxs_joint_j_17))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.mts_body_mount_2.jxs_joint_j_17))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_6  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_spndl_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_spndl_sf_atch, .template_6_motion.ground.hpl_uc_top, "Z"))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_6  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_spndl_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_spndl_sf_atch, .template_6_motion.ground.hpr_uc_top, "Z"))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.jxl_joint_j_17  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_upract_sf_atch_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.jxr_joint_j_17  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_upract_sf_atch_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.uel_gearaero_jjoint_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxl_joint_j_16))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxl_joint_j_16))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ges_subframe_2.uer_gearaero_jjoint_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxr_joint_j_16))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 180d, 0}, .template_6_motion.ges_subframe_2.jxr_joint_j_16))  &
   relative_to = .template_6_motion.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_cylinder.gralin_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.cfl_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.cfl_uc_top, .template_6_motion.ground.cfl_uc_bot, "Z"))  &
   relative_to = .template_6_motion.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_cylinder.gralin_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_ib_uc_sf_atch, .template_6_motion.ground.hpl_uc_geompt, "Z"))  &
   relative_to = .template_6_motion.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_cylinder.gralin_20  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_ib_uc_sf_atch, .template_6_motion.ground.hpl_uc_top, "Z"))  &
   relative_to = .template_6_motion.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_i_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxl_joint_j_16))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxl_joint_j_16))  &
   relative_to = .template_6_motion.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_cylinder.jxl_joint_i_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_lwract.jxl_joint_j_7))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_lwract.jxl_joint_j_7))  &
   relative_to = .template_6_motion.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_cylinder.gralin_upper_cylinder  &
   length = (DM(.template_6_motion.ground.cfl_uc_top, .template_6_motion.ground.cfl_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_cylinder.gralin_geom  &
   length = (DM(.template_6_motion.ground.hpl_ib_uc_sf_atch, .template_6_motion.ground.hpl_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_cylinder.gralin_geom3  &
   length = (DM(.template_6_motion.ground.hpl_ib_uc_sf_atch, .template_6_motion.ground.hpl_uc_top))
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_cylinder.gralin_13  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.cfr_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.cfr_uc_top, .template_6_motion.ground.cfr_uc_bot, "Z"))  &
   relative_to = .template_6_motion.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_cylinder.gralin_17  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_ib_uc_sf_atch, .template_6_motion.ground.hpr_uc_geompt, "Z"))  &
   relative_to = .template_6_motion.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_cylinder.gralin_21  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_ib_uc_sf_atch, .template_6_motion.ground.hpr_uc_top, "Z"))  &
   relative_to = .template_6_motion.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_i_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxr_joint_j_16))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxr_joint_j_16))  &
   relative_to = .template_6_motion.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_cylinder.jxr_joint_i_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_lwract.jxr_joint_j_7))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_lwract.jxr_joint_j_7))  &
   relative_to = .template_6_motion.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_cylinder.gralin_upper_cylinder  &
   length = (DM(.template_6_motion.ground.cfr_uc_top, .template_6_motion.ground.cfr_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_cylinder.gralin_geom  &
   length = (DM(.template_6_motion.ground.hpr_ib_uc_sf_atch, .template_6_motion.ground.hpr_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_cylinder.gralin_geom3  &
   length = (DM(.template_6_motion.ground.hpr_ib_uc_sf_atch, .template_6_motion.ground.hpr_uc_top))
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_cylinder.gralin_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.cfl_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.cfl_lc_top, .template_6_motion.ground.hpl_lc_bot, "Z"))  &
   relative_to = .template_6_motion.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_cylinder.gralin_22  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_ib_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_ib_axle, .template_6_motion.ground.hpl_ob_axle1, "Z"))  &
   relative_to = .template_6_motion.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_cylinder.jxl_joint_j_11  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_lta_connect_atch_1, .template_6_motion.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_cylinder.jxl_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_upper_cylinder.jxl_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_upper_cylinder.jxl_joint_j_12))  &
   relative_to = .template_6_motion.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_cylinder.MARKER_352  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_ob_axle1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_ob_axle1, .template_6_motion.ground.hpl_stator_attach, "Z"))  &
   relative_to = .template_6_motion.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_lower_cylinder.gralin_lower_cylinder  &
   length = (DM(.template_6_motion.ground.cfl_lc_top, .template_6_motion.ground.hpl_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_lower_cylinder.gralin_geom  &
   length = (DM(.template_6_motion.ground.hpl_ib_axle, .template_6_motion.ground.hpl_ob_axle1))
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_cylinder.gralin_15  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.cfr_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.cfr_lc_top, .template_6_motion.ground.hpr_lc_bot, "Z"))  &
   relative_to = .template_6_motion.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_cylinder.gralin_23  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_ib_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_ib_axle, .template_6_motion.ground.hpr_ob_axle1, "Z"))  &
   relative_to = .template_6_motion.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_cylinder.jxr_joint_j_11  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_lta_connect_atch_1, .template_6_motion.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_cylinder.jxr_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_upper_cylinder.jxr_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_upper_cylinder.jxr_joint_j_12))  &
   relative_to = .template_6_motion.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_cylinder.MARKER_353  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_ob_axle1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_ob_axle1, .template_6_motion.ground.hpr_stator_attach, "Z"))  &
   relative_to = .template_6_motion.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_lower_cylinder.gralin_lower_cylinder  &
   length = (DM(.template_6_motion.ground.cfr_lc_top, .template_6_motion.ground.hpr_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_lower_cylinder.gralin_geom  &
   length = (DM(.template_6_motion.ground.hpr_ib_axle, .template_6_motion.ground.hpr_ob_axle1))
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_dragbrace.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_udb_spndl_atch_1, .template_6_motion.ground.hpl_ldb_udb_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_dragbrace.jxl_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_6_motion.ground.cfl_plane_ref_2, "Z+Z"), .template_6_motion.gel_upper_dragbrace))  &
   relative_to = .template_6_motion.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_dragbrace.jxl_joint_i_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_spindle.jxl_joint_j_5))  &
   orientation =   &
      (ORI_IN_PLANE(.template_6_motion.gel_upper_dragbrace.jxl_joint_i_5, .template_6_motion.ground.hpl_ldb_udb_atch_1, .template_6_motion.ground.hpl_spndl_sf_atch, "Z_ZX"))  &
   relative_to = .template_6_motion.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_dragbrace.gralin_upper_dragbrace  &
   length = (DM(.template_6_motion.ground.hpl_udb_spndl_atch_1, .template_6_motion.ground.hpl_ldb_udb_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_dragbrace.gralin_25  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_udb_spndl_atch_1, .template_6_motion.ground.hpr_ldb_udb_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_dragbrace.jxr_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_6_motion.ground.cfr_plane_ref_2, "Z+Z"), .template_6_motion.ger_upper_dragbrace))  &
   relative_to = .template_6_motion.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_dragbrace.jxr_joint_i_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_spindle.jxr_joint_j_5))  &
   orientation =   &
      (ORI_IN_PLANE(.template_6_motion.ger_upper_dragbrace.jxr_joint_i_5, .template_6_motion.ground.hpr_ldb_udb_atch_1, .template_6_motion.ground.hpr_spndl_sf_atch, "Z_ZX"))  &
   relative_to = .template_6_motion.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_dragbrace.gralin_upper_dragbrace  &
   length = (DM(.template_6_motion.ground.hpr_udb_spndl_atch_1, .template_6_motion.ground.hpr_ldb_udb_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_dragbrace.gralin_26  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_ldb_udb_atch_1, .template_6_motion.ground.hpl_ldb_collar_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_dragbrace.jxl_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_upper_dragbrace.jxl_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_upper_dragbrace.jxl_joint_j_14))  &
   relative_to = .template_6_motion.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_dragbrace.jxl_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_uc_collar.jxl_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_uc_collar.jxl_joint_j_10))  &
   relative_to = .template_6_motion.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_lower_dragbrace.gralin_lower_dragbrace  &
   length = (DM(.template_6_motion.ground.hpl_ldb_udb_atch_1, .template_6_motion.ground.hpl_ldb_collar_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_dragbrace.gralin_27  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_ldb_udb_atch_1, .template_6_motion.ground.hpr_ldb_collar_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_dragbrace.jxr_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_upper_dragbrace.jxr_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_upper_dragbrace.jxr_joint_j_14))  &
   relative_to = .template_6_motion.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_dragbrace.jxr_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_uc_collar.jxr_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_uc_collar.jxr_joint_j_10))  &
   relative_to = .template_6_motion.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_lower_dragbrace.gralin_lower_dragbrace  &
   length = (DM(.template_6_motion.ground.hpr_ldb_udb_atch_1, .template_6_motion.ground.hpr_ldb_collar_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_torquearm.gralin_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_uta_collar_atch_1, .template_6_motion.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_torquearm.jxl_joint_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_connector.jxl_joint_j_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_connector.jxl_joint_j_2))  &
   relative_to = .template_6_motion.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upper_torquearm.jxl_joint_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_uc_collar.jxl_joint_j_3))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_uc_collar.jxl_joint_j_3))  &
   relative_to = .template_6_motion.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_upper_torquearm.gralin_upper_torquearm  &
   length = (DM(.template_6_motion.ground.hpl_uta_collar_atch_1, .template_6_motion.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_torquearm.gralin_28  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_uta_collar_atch_1, .template_6_motion.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_torquearm.jxr_joint_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_connector.jxr_joint_j_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_connector.jxr_joint_j_2))  &
   relative_to = .template_6_motion.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upper_torquearm.jxr_joint_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_uc_collar.jxr_joint_j_3))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_uc_collar.jxr_joint_j_3))  &
   relative_to = .template_6_motion.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_upper_torquearm.gralin_upper_torquearm  &
   length = (DM(.template_6_motion.ground.hpr_uta_collar_atch_1, .template_6_motion.ground.hpr_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_torquearm.gralin_29  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_lta_lc_atch_1, .template_6_motion.ground.hpl_lta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_torquearm.jxl_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_lower_cylinder.jxl_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_lower_cylinder.jxl_joint_j_11))  &
   relative_to = .template_6_motion.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lower_torquearm.jxl_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_connector.jxl_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_connector.jxl_joint_j_1))  &
   relative_to = .template_6_motion.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_lower_torquearm.gralin_lower_torquearm  &
   length = (DM(.template_6_motion.ground.hpl_lta_lc_atch_1, .template_6_motion.ground.hpl_lta_connect_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_torquearm.gralin_30  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_lta_lc_atch_1, .template_6_motion.ground.hpr_lta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_torquearm.jxr_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_lower_cylinder.jxr_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_lower_cylinder.jxr_joint_j_11))  &
   relative_to = .template_6_motion.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lower_torquearm.jxr_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_connector.jxr_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_connector.jxr_joint_j_1))  &
   relative_to = .template_6_motion.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_lower_torquearm.gralin_lower_torquearm  &
   length = (DM(.template_6_motion.ground.hpr_lta_lc_atch_1, .template_6_motion.ground.hpr_lta_connect_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.mts_body_mount_2.jxs_joint_j_17  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfs_subframe_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))  &
   relative_to = .template_6_motion.mts_body_mount_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
part modify rigid_body name_and_position  &
   part_name = .template_6_motion.mts_body_mount_2  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.origo1))
!
marker modify  &
   marker_name = .template_6_motion.gel_connector.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_connect_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_connect_1, .template_6_motion.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_connector.jxl_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_lta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_lta_connect_atch_1, .template_6_motion.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_connector.jxl_joint_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_uta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_uta_connect_atch_1, .template_6_motion.ground.hpl_uta_connect_atch_2, "Z"))  &
   relative_to = .template_6_motion.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_connector.gralin_connector  &
   length = (DM(.template_6_motion.ground.hpl_connect_1, .template_6_motion.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.ger_connector.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_connect_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_connect_1, .template_6_motion.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_connector.jxr_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_lta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_lta_connect_atch_1, .template_6_motion.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_connector.jxr_joint_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_uta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_uta_connect_atch_1, .template_6_motion.ground.hpr_uta_connect_atch_2, "Z"))  &
   relative_to = .template_6_motion.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_connector.gralin_connector  &
   length = (DM(.template_6_motion.ground.hpr_connect_1, .template_6_motion.ground.hpr_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.gel_uc_collar.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.cfl_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.cfl_collar_top, .template_6_motion.ground.cfl_collar_bot, "Z"))  &
   relative_to = .template_6_motion.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_uc_collar.jxl_joint_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_lta_connect_atch_1, .template_6_motion.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_uc_collar.jxl_joint_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_upper_cylinder.jxl_joint_j_4))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_upper_cylinder.jxl_joint_j_4))  &
   relative_to = .template_6_motion.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_uc_collar.jxl_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_ldb_collar_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_6_motion.ground.cfl_plane_ref_2, "Z+Z"), .template_6_motion.gel_uc_collar))  &
   relative_to = .template_6_motion.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_uc_collar.gralin_uc_collar  &
   length = (DM(.template_6_motion.ground.cfl_collar_top, .template_6_motion.ground.cfl_collar_bot))
!
marker modify  &
   marker_name = .template_6_motion.ger_uc_collar.gralin_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.cfr_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.cfr_collar_top, .template_6_motion.ground.cfr_collar_bot, "Z"))  &
   relative_to = .template_6_motion.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_uc_collar.jxr_joint_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_lta_connect_atch_1, .template_6_motion.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_uc_collar.jxr_joint_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_upper_cylinder.jxr_joint_j_4))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_upper_cylinder.jxr_joint_j_4))  &
   relative_to = .template_6_motion.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_uc_collar.jxr_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_ldb_collar_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_6_motion.ground.cfr_plane_ref_2, "Z+Z"), .template_6_motion.ger_uc_collar))  &
   relative_to = .template_6_motion.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_uc_collar.gralin_uc_collar  &
   length = (DM(.template_6_motion.ground.cfr_collar_top, .template_6_motion.ground.cfr_collar_bot))
!
marker modify  &
   marker_name = .template_6_motion.gel_spindle.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_spndl_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_spndl_sf_atch, .template_6_motion.ground.hpl_udb_spndl_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_spindle.jxl_joint_j_5  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_IN_PLANE(.template_6_motion.ground.hpl_spndl_sf_atch, .template_6_motion.gel_spindle.jxl_joint_j_5, .template_6_motion.ground.hpl_ldb_udb_atch_1, "Z_ZX"))  &
   relative_to = .template_6_motion.gel_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_spindle.jxl_joint_i_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxl_joint_j_6))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxl_joint_j_6))  &
   relative_to = .template_6_motion.gel_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_spindle.gralin_spindle  &
   length = (DM(.template_6_motion.ground.hpl_spndl_sf_atch, .template_6_motion.ground.hpl_udb_spndl_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.ger_spindle.gralin_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_spndl_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_spndl_sf_atch, .template_6_motion.ground.hpr_udb_spndl_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_spindle.jxr_joint_j_5  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_IN_PLANE(.template_6_motion.ground.hpr_spndl_sf_atch, .template_6_motion.ger_spindle.jxr_joint_j_5, .template_6_motion.ground.hpr_ldb_udb_atch_1, "Z_ZX"))  &
   relative_to = .template_6_motion.ger_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_spindle.jxr_joint_i_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxr_joint_j_6))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxr_joint_j_6))  &
   relative_to = .template_6_motion.ger_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_spindle.gralin_spindle  &
   length = (DM(.template_6_motion.ground.hpr_spndl_sf_atch, .template_6_motion.ground.hpr_udb_spndl_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.gel_lwract.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpl_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_lwract_uc_atch_1, .template_6_motion.ground.cfl_lwract_top, "Z"))  &
   relative_to = .template_6_motion.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lwract.jxl_joint_j_7  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpl_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))  &
   relative_to = .template_6_motion.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_lwract.jxl_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_upract.jxl_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.gel_upract.jxl_joint_j_8))  &
   relative_to = .template_6_motion.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_lwract.gralin_lwract  &
   length = (DM(.template_6_motion.ground.hpl_lwract_uc_atch_1, .template_6_motion.ground.cfl_lwract_top))
!
marker modify  &
   marker_name = .template_6_motion.ger_lwract.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.hpr_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_lwract_uc_atch_1, .template_6_motion.ground.cfr_lwract_top, "Z"))  &
   relative_to = .template_6_motion.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lwract.jxr_joint_j_7  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.hpr_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_motion.ground.origo1))  &
   relative_to = .template_6_motion.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_lwract.jxr_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_upract.jxr_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ger_upract.jxr_joint_j_8))  &
   relative_to = .template_6_motion.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_lwract.gralin_lwract  &
   length = (DM(.template_6_motion.ground.hpr_lwract_uc_atch_1, .template_6_motion.ground.cfr_lwract_top))
!
marker modify  &
   marker_name = .template_6_motion.gel_upract.gralin_18  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.cfl_upract_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.cfl_upract_bot, .template_6_motion.ground.hpl_upract_sf_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upract.jxl_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfl_lwract_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpl_lwract_uc_atch_1, .template_6_motion.ground.hpl_upract_sf_atch_1, "Z"))  &
   relative_to = .template_6_motion.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.gel_upract.jxl_joint_i_17  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxl_joint_j_17))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxl_joint_j_17))  &
   relative_to = .template_6_motion.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.gel_upract.gralin_upract  &
   length = (DM(.template_6_motion.ground.cfl_upract_bot, .template_6_motion.ground.hpl_upract_sf_atch_1))
!
marker modify  &
   marker_name = .template_6_motion.ger_upract.gralin_19  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ground.cfr_upract_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.cfr_upract_bot, .template_6_motion.ground.hpr_upract_sf_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upract.jxr_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_motion.ground.cfr_lwract_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_motion.ground.hpr_lwract_uc_atch_1, .template_6_motion.ground.hpr_upract_sf_atch_1, "Z"))  &
   relative_to = .template_6_motion.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
marker modify  &
   marker_name = .template_6_motion.ger_upract.jxr_joint_i_17  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxr_joint_j_17))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_motion.ges_subframe_2.jxr_joint_j_17))  &
   relative_to = .template_6_motion.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_motion.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_motion.ger_upract.gralin_upract  &
   length = (DM(.template_6_motion.ground.cfr_upract_bot, .template_6_motion.ground.hpr_upract_sf_atch_1))
!
geometry modify shape force  &
   force_name = .template_6_motion.aeroforce_force_graphic_1  &
   applied_at_marker_name = (.template_6_motion.NLG_aeroforce.i)
!
geometry modify shape force  &
   force_name = .template_6_motion.GFORCE_3_force_graphic_1  &
   applied_at_marker_name = (.template_6_motion.aeroforce_MLG_L.i)
!
geometry modify shape force  &
   force_name = .template_6_motion.GFORCE_4_force_graphic_1  &
   applied_at_marker_name = (.template_6_motion.aeroforce_MLG_R.i)
!
model display  &
   model_name = template_6_motion

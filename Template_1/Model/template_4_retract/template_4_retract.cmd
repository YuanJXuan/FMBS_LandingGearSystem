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
   icon_visibility = on  &
   grid_visibility = off  &
   size_of_icons = 25.0  &
   spacing_for_grid = 25.4
!
!------------------------------ Adams View Model ------------------------------!
!
!
model create  &
   model_name = template_4_retract  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_4_retract  &
   size_of_icons = 25.0
!
view erase
!
!-------------------------------- Data storage --------------------------------!
!
!
data_element create spline  &
   spline_name = .template_4_retract.SPLINE_angle_aeroforce  &
   adams_id = 1  &
   x = -20.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0,  &
       90.0, 100.0  &
   y = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0  &
   linear_extrapolate = no
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .template_4_retract.steel  &
   adams_id = 5  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_4_retract.aluminum  &
   adams_id = 3  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_4_retract.steel_2  &
   adams_id = 1  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_4_retract.aluminum_2  &
   adams_id = 4  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_4_retract.steel_3  &
   adams_id = 6  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_4_retract.aluminum_3  &
   adams_id = 7  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_4_retract.steel_2_2  &
   adams_id = 8  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_4_retract.aluminum_2_2  &
   adams_id = 9  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_4_retract.steel_3_2  &
   adams_id = 10  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_4_retract.aluminum_3_2  &
   adams_id = 11  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_4_retract.steel_2_2_2  &
   adams_id = 12  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_4_retract.aluminum_2_2_2  &
   adams_id = 13  &
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
   default_coordinate_system = .template_4_retract.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_4_retract.ground.origo  &
   adams_id = 10  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.origo  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.cfs_uc_sf_atch_mid  &
   adams_id = 12  &
   location = 6314.44, 0.0, 1691.64  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.cfs_uc_sf_atch_mid  &
   color = MAIZE  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.cfs_subframe_to_body_point  &
   adams_id = 13  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
marker attributes  &
   marker_name = .template_4_retract.ground.cfs_subframe_to_body_point  &
   color = MAIZE  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.mts_mount_j_2  &
   adams_id = 14  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.mts_mount_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.cfl_spin_axis  &
   adams_id = 15  &
   location = 6229.096, -209.55, 508.0  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.cfl_spin_axis  &
   color = MAIZE  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.cfr_spin_axis  &
   adams_id = 16  &
   location = 6229.096, 209.55, 508.0  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.cfr_spin_axis  &
   color = MAIZE  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.cfs_wheel_centers_midpoint  &
   adams_id = 17  &
   location = 6229.096, 0.0, 508.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.cfs_wheel_centers_midpoint  &
   color = MAIZE  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.cfs_nlg_axle_lowpoint  &
   adams_id = 18  &
   location = 6229.096, 0.0, 482.6  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.cfs_nlg_axle_lowpoint  &
   color = MAIZE  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.cfs_collar_top  &
   adams_id = 19  &
   location = 6197.6, 0.0, 856.996  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.cfs_collar_top  &
   color = MAIZE  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.origo3  &
   adams_id = 697  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.origo3  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.origo2  &
   adams_id = 687  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.origo2  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.origo11  &
   adams_id = 696  &
   location = 100.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.origo11  &
   visibility = on  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.origo12  &
   adams_id = 698  &
   location = 100.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.origo12  &
   visibility = on  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.origo1  &
   adams_id = 1  &
   location = 100.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.origo1  &
   visibility = on  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.uel_gearaero_origin_1  &
   adams_id = 171  &
   location = 100.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.uel_gearaero_origin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ground.uer_gearaero_origin_1  &
   adams_id = 173  &
   location = 100.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ground.uer_gearaero_origin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_4_retract.ground.uel_gearaero_jfloat_11  &
   adams_id = 699
!
floating_marker create  &
   floating_marker_name = .template_4_retract.ground.uel_gearaero_jfloat_1  &
   adams_id = 175
!
floating_marker create  &
   floating_marker_name = .template_4_retract.ground.uer_gearaero_jfloat_1  &
   adams_id = 176
!
floating_marker create  &
   floating_marker_name = .template_4_retract.ground.uer_gearaero_jfloat_11  &
   adams_id = 700
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_4_retract.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_4_retract.ground.hps_db_sf_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_sf_atch_l  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_sf_atch_r  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lc_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_4_retract.ground.hps_db_uc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uta_uc_atch  &
   location = 6324.6, 0.0, 838.2
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uta_uc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lta_lc_atch  &
   location = 6299.2, 0.0, 533.4
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lta_lc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lta_uta_atch  &
   location = 6654.8, 0.0, 711.2
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lta_uta_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_geompt  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lc_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_aeroforceN  &
   location = 6200.9167643494, 3.3850517933E-11, 1207.1824231157
!
point attributes  &
   point_name = .template_4_retract.ground.hps_aeroforceN  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lb_uc_atch  &
   location = 6021.578, 0.0, 795.02
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lb_uc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hpl_wheel_center  &
   location = 6229.096, -209.55, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hpl_wheel_center  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hpr_wheel_center  &
   location = 6229.096, 209.55, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hpr_wheel_center  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hpl_ob_axle  &
   location = 6229.096, -285.75, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hpl_ob_axle  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hpr_ob_axle  &
   location = 6229.096, 285.75, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hpr_ob_axle  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_nlg_axle_lowpoint  &
   location = 6229.096, 0.0, 482.6
!
point attributes  &
   point_name = .template_4_retract.ground.hps_nlg_axle_lowpoint  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_rod_bot  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point attributes  &
   point_name = .template_4_retract.ground.hps_rod_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_rod_top  &
   location = 7227.4389033572, 0.0, 1472.1512863532
!
point attributes  &
   point_name = .template_4_retract.ground.hps_rod_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lockroller_l  &
   location = 6116.051, 50.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lockroller_l  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lockroller_r  &
   location = 6116.051, -50.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lockroller_r  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lockroller_l_2  &
   location = 6051.051, 50.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lockroller_l_2  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lockroller_r_2  &
   location = 6051.051, -50.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lockroller_r_2  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.suo_qiu_point  &
   location = 6051.051, 0.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.suo_qiu_point  &
   size_of_icons = 25.0
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_4_retract.ground  &
   size_of_icons = 25.0
!
!------------------------------ ges_sf_actuator -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_4_retract.ges_sf_actuator  &
   adams_id = 7  &
   location = 6967.855, 0.0, 1319.53  &
   orientation = 270.0d, 120.4532239091d, 90.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ges_sf_actuator
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_4_retract.ges_sf_actuator.cm  &
   adams_id = 21  &
   location = -4.58524116E-10, 0.0, 0.0  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_actuator.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_actuator.gralin_1  &
   adams_id = 23  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_actuator.gralin_1  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_actuator.jxs_joint_i_14  &
   adams_id = 24  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 0.0d, 90.0d, 239.5467760909d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_actuator.jxs_joint_i_14  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_actuator.MARKER_85  &
   adams_id = 85  &
   location = 1.3451462166E-09, 0.0, 158.8736811071  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_actuator.MARKER_85  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_actuator.MARKER_97  &
   adams_id = 97  &
   location = -4.5918824298E-10, 0.0, -598.873681109  &
   orientation = 90.0d, 120.4532239091d, 270.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_actuator.MARKER_97  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_actuator.MARKER_512  &
   adams_id = 512  &
   location = -4.4586556669E-10, 0.0, 3.108624469E-11  &
   orientation = 90.0d, 120.4532239091d, 270.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_actuator.MARKER_512  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_actuator.MARKER_532  &
   adams_id = 532  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 180.0d, 89.9999999993d, 300.4532239097d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_actuator.MARKER_532  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_4_retract.ges_sf_actuator  &
   material_type = .template_4_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_sf_actuator.gralin_dragbrace_geom  &
   adams_id = 32  &
   center_marker = .template_4_retract.ges_sf_actuator.gralin_1  &
   angle_extent = 360.0  &
   length = 1197.7473622179  &
   radius = 50.8  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_sf_actuator.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .template_4_retract.ges_sf_actuator  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!----------------------------- ges_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_4_retract.ges_upper_cylinder  &
   adams_id = 8  &
   location = 6197.6, 0.0, 1193.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ges_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_4  &
   adams_id = 4  &
   location = -236.7591354821, 0.0, 187.9366952496  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_4  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.cm  &
   adams_id = 25  &
   location = -2.1926640514, 0.0, -14.5859826029  &
   orientation = 90.0d, 0.8375931978d, 270.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.gralin_2  &
   adams_id = 27  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.gralin_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.gralin_3  &
   adams_id = 28  &
   location = -116.84, -340.36, -497.84  &
   orientation = 161.0534953105d, 58.7414044414d, 213.4869581747d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.gralin_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.gralin_4  &
   adams_id = 29  &
   location = -116.84, 340.36, -497.84  &
   orientation = 18.9465046895d, 58.7414044414d, 326.5130418253d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.gralin_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.jxs_joint_j_11  &
   adams_id = 30  &
   location = 0.0, 0.0, 114.3  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.jxs_joint_j_11  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_516  &
   adams_id = 516  &
   location = -116.84, 0.0, -497.84  &
   orientation = 179.9999999994d, 89.9999999997d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_516  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.jxs_joint_j_1  &
   adams_id = 35  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.jxs_joint_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_526  &
   adams_id = 526  &
   location = -116.84, 0.0, -497.84  &
   orientation = 179.9999999994d, 89.9999999997d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_526  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_781  &
   adams_id = 781  &
   location = -3.3167643494, 3.3852562994E-11, -13.3824231157  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_781  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_4_retract.ges_upper_cylinder  &
   material_type = .template_4_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 33  &
   center_marker = .template_4_retract.ges_upper_cylinder.gralin_2  &
   angle_extent = 360.0  &
   length = 863.6  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 34  &
   center_marker = .template_4_retract.ges_upper_cylinder.gralin_3  &
   angle_extent = 360.0  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 35  &
   center_marker = .template_4_retract.ges_upper_cylinder.gralin_4  &
   angle_extent = 360.0000000012  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_4_retract.ges_upper_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!----------------------------- ges_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_4_retract.ges_lower_cylinder  &
   adams_id = 9  &
   location = 6197.6, 0.0, 952.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ges_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.cm  &
   adams_id = 38  &
   location = -10.4171178951, 0.0, 112.8903699545  &
   orientation = 270.0d, 2.0214888363d, 90.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_5  &
   adams_id = 40  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.jxs_joint_i_11  &
   adams_id = 42  &
   location = 0.0, 0.0, -127.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.jxs_joint_i_11  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_7  &
   adams_id = 43  &
   location = -31.496, 209.55, 444.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_7  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_9  &
   adams_id = 51  &
   location = -127.0, 0.0, 114.3  &
   orientation = 270.0d, 68.9624889746d, 90.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_9  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_10  &
   adams_id = 57  &
   location = -101.6, 0.0, 419.1  &
   orientation = 270.0d, 116.5650511771d, 90.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_359  &
   adams_id = 359  &
   location = 81.549, 50.0, 367.076  &
   orientation = 90.0d, 90.0d, 270.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_359  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_360  &
   adams_id = 360  &
   location = 81.549, -50.0, 367.076  &
   orientation = 90.0d, 90.0d, 270.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_360  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_361  &
   adams_id = 361  &
   location = 146.549, -50.0, 367.076  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_361  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_782  &
   adams_id = 782  &
   location = -3.3167643494, 3.3882113721E-11, -254.6824231157  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_782  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_436  &
   adams_id = 436  &
   location = 146.549, 0.0, 367.076  &
   orientation = 56.6067815944d, 108.7094912792d, 176.556099572d
!
marker attributes  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_436  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_786  &
   adams_id = 786  &
   location = -31.496, -285.75, 444.5  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_787  &
   adams_id = 787  &
   location = -31.496, 285.75, 444.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_4_retract.ges_lower_cylinder.FMARKER_783  &
   adams_id = 783
!
part create rigid_body mass_properties  &
   part_name = .template_4_retract.ges_lower_cylinder  &
   material_type = .template_4_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.gralin_geom1  &
   adams_id = 36  &
   center_marker = .template_4_retract.ges_lower_cylinder.gralin_5  &
   angle_extent = 360.0  &
   length = 889.0  &
   radius = 101.6  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.gralin_geom2  &
   adams_id = 37  &
   center_marker = .template_4_retract.ges_lower_cylinder.gralin_7  &
   angle_extent = 360.0  &
   length = 419.1  &
   radius = 30.48  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_lower_cylinder.gralin_geom2  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.CYLINDER_128  &
   adams_id = 128  &
   center_marker = .template_4_retract.ges_lower_cylinder.MARKER_359  &
   angle_extent = 360.0000000012  &
   length = 73.0  &
   radius = 8.125  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.CYLINDER_132  &
   adams_id = 132  &
   center_marker = .template_4_retract.ges_lower_cylinder.MARKER_360  &
   angle_extent = 360.0000000012  &
   length = 73.0  &
   radius = 8.125  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.CYLINDER_136  &
   adams_id = 136  &
   center_marker = .template_4_retract.ges_lower_cylinder.MARKER_361  &
   angle_extent = 360.0000000012  &
   length = 100.0  &
   radius = 7.5  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_4_retract.ges_lower_cylinder.suo_qiu  &
   adams_id = 164  &
   center_marker = .template_4_retract.ges_lower_cylinder.MARKER_436  &
   x_scale_factor = 8.5  &
   y_scale_factor = 8.5  &
   z_scale_factor = 8.5
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.gralin_lower_torque_arm_geom  &
   adams_id = 39  &
   center_marker = .template_4_retract.ges_lower_cylinder.gralin_10  &
   angle_extent = 360.0  &
   length = 397.5728863995  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_lower_cylinder.gralin_lower_torque_arm_geom  &
   color = MAGENTA
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.gralin_upper_torque_arm_geom  &
   adams_id = 38  &
   center_marker = .template_4_retract.ges_lower_cylinder.gralin_9  &
   angle_extent = 360.0  &
   length = 353.7810622405  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_lower_cylinder.gralin_upper_torque_arm_geom  &
   color = GREEN
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.CYLINDER_464  &
   adams_id = 464  &
   center_marker = .template_4_retract.ges_lower_cylinder.MARKER_786  &
   angle_extent = 360.0  &
   length = 90.0  &
   radius = 120.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.CYLINDER_474  &
   adams_id = 474  &
   center_marker = .template_4_retract.ges_lower_cylinder.MARKER_787  &
   angle_extent = 360.0  &
   length = 90.0  &
   radius = 120.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_4_retract.ges_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!-------------------------------- ges_subframe --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_4_retract.ges_subframe  &
   adams_id = 12  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ges_subframe
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.MARKER_517  &
   adams_id = 517  &
   location = -390.5595878992, 5.906386491E-11, 0.0  &
   orientation = 3.3555200902d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.MARKER_517  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.cm  &
   adams_id = 59  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.inertia_frame  &
   adams_id = 60  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.inertia_frame  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.graout_1  &
   adams_id = 61  &
   location = -390.5595878992, 5.9337951219E-11, -340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.graout_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.graout_2  &
   adams_id = 62  &
   location = -390.5595878992, 5.9337951219E-11, 340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.graout_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.graout_3  &
   adams_id = 63  &
   location = 781.1191757984, -1.1845385783E-10, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.graout_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.jxs_joint_i_16  &
   adams_id = 65  &
   location = 0.0, 0.0, 0.0  &
   orientation = 183.3555200908d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.jxs_joint_i_16  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.jxs_joint_j_14  &
   adams_id = 66  &
   location = 781.1191757984, -1.1845385783E-10, 0.0  &
   orientation = 3.3555200908d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.jxs_joint_j_14  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.MARKER_527  &
   adams_id = 527  &
   location = -390.5595878992, 5.906386491E-11, 0.0  &
   orientation = 3.3555200902d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.MARKER_527  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_subframe.MARKER_533  &
   adams_id = 533  &
   location = 781.1191757984, -1.1845385783E-10, 0.0  &
   orientation = 3.3555200902d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_subframe.MARKER_533  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_4_retract.ges_subframe  &
   mass = 4.5359237E-03  &
   center_of_mass_marker = .template_4_retract.ges_subframe.cm  &
   inertia_marker = .template_4_retract.ges_subframe.inertia_frame  &
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
   outline_name = .template_4_retract.ges_subframe.graout_subframe_geom  &
   adams_id = 41  &
   marker_name =  &
      .template_4_retract.ges_subframe.graout_1,  &
      .template_4_retract.ges_subframe.graout_2,  &
      .template_4_retract.ges_subframe.graout_3  &
   visibility_between_markers = on, on, on  &
   close = yes
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_subframe.graout_subframe_geom  &
   color = WHITE
!
part attributes  &
   part_name = .template_4_retract.ges_subframe  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!------------------------------- mts_body_mount -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_4_retract.mts_body_mount  &
   adams_id = 13  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.mts_body_mount
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_4_retract.mts_body_mount.mount_i  &
   adams_id = 67  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.mts_body_mount.mount_i  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.mts_body_mount.jxs_joint_j_16  &
   adams_id = 68  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.mts_body_mount.jxs_joint_j_16  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
part attributes  &
   part_name = .template_4_retract.mts_body_mount  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!--------------------------------- ges_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_4_retract.ges_collar  &
   adams_id = 14  &
   location = 6197.6, 0.0, 809.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ges_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_4_retract.ges_collar.cm  &
   adams_id = 70  &
   location = 0.0, 0.0, 0.0  &
   orientation = 180.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_collar.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_collar.gralin_24  &
   adams_id = 72  &
   location = 0.0, 0.0, -47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_collar.gralin_24  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_collar.jxs_joint_i_1  &
   adams_id = 73  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_collar.jxs_joint_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_4_retract.ges_collar  &
   material_type = .template_4_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_collar.gralin_collar  &
   adams_id = 40  &
   center_marker = .template_4_retract.ges_collar.gralin_24  &
   angle_extent = 360.0  &
   length = 94.996  &
   radius = 139.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_4_retract.ges_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .template_4_retract.ges_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!--------------------------------- ges_sf_rod ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_4_retract.ges_sf_rod  &
   adams_id = 5  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ges_sf_rod
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_784  &
   adams_id = 784  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_784  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_5  &
   adams_id = 5  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_5  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_785  &
   adams_id = 785  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_785  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.gralin_25  &
   adams_id = 3  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 270.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.gralin_25  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.cm  &
   adams_id = 76  &
   location = 6830.8990194197, 0.0, 1239.0072955518  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_79  &
   adams_id = 79  &
   location = 6830.8990194192, 0.0, 1239.0072955517  &
   orientation = 270.0d, 120.453223909d, 180.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_79  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_80  &
   adams_id = 80  &
   location = 6830.8990194192, 0.0, 1239.0072955517  &
   orientation = 270.0d, 120.453223909d, 180.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_80  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_84  &
   adams_id = 84  &
   location = 6830.8990194192, 0.0, 1239.0072955517  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_84  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_90  &
   adams_id = 90  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_90  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_91  &
   adams_id = 91  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_91  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_96  &
   adams_id = 96  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_96  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_511  &
   adams_id = 511  &
   location = 6830.8990194197, 0.0, 1239.0072955518  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_511  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_4_retract.ges_sf_rod  &
   material_type = .template_4_retract.steel
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_4_retract.ges_sf_rod.PT3  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point attributes  &
   point_name = .template_4_retract.ges_sf_rod.PT3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_4_retract.ges_sf_rod.CYLINDER_30  &
   adams_id = 30  &
   center_marker = .template_4_retract.ges_sf_rod.gralin_25  &
   angle_extent = 360.0  &
   length = 920.0  &
   radius = 27.5  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_4_retract.ges_sf_rod  &
   color = RED  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_4_retract.josrev_uc_sf_joint  &
   adams_id = 51  &
   i_marker_name = .template_4_retract.ges_upper_cylinder.MARKER_516  &
   j_marker_name = .template_4_retract.ges_subframe.MARKER_517
!
constraint attributes  &
   constraint_name = .template_4_retract.josrev_uc_sf_joint  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_4_retract.joscyl_lc_uc_joint  &
   adams_id = 7  &
   i_marker_name = .template_4_retract.ges_lower_cylinder.jxs_joint_i_11  &
   j_marker_name = .template_4_retract.ges_upper_cylinder.jxs_joint_j_11
!
constraint attributes  &
   constraint_name = .template_4_retract.joscyl_lc_uc_joint  &
   visibility = on  &
   size_of_icons = 25.0
!
constraint create joint spherical  &
   joint_name = .template_4_retract.jossph_rd_uc  &
   adams_id = 1  &
   i_marker_name = .template_4_retract.ges_upper_cylinder.MARKER_4  &
   j_marker_name = .template_4_retract.ges_sf_rod.MARKER_5
!
constraint attributes  &
   constraint_name = .template_4_retract.jossph_rd_uc  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_4_retract.mts_fixed_2  &
   adams_id = 9  &
   i_marker_name = .template_4_retract.mts_body_mount.mount_i  &
   j_marker_name = .template_4_retract.ground.mts_mount_j_2
!
constraint attributes  &
   constraint_name = .template_4_retract.mts_fixed_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_4_retract.josfix_subframe_to_body  &
   adams_id = 10  &
   i_marker_name = .template_4_retract.ges_subframe.jxs_joint_i_16  &
   j_marker_name = .template_4_retract.mts_body_mount.jxs_joint_j_16
!
constraint attributes  &
   constraint_name = .template_4_retract.josfix_subframe_to_body  &
   visibility = on  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_4_retract.joscyl_db_sf  &
   adams_id = 11  &
   i_marker_name = .template_4_retract.ges_sf_actuator.jxs_joint_i_14  &
   j_marker_name = .template_4_retract.ges_subframe.jxs_joint_j_14
!
constraint attributes  &
   constraint_name = .template_4_retract.joscyl_db_sf  &
   visibility = on  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_4_retract.josrev_collar_uc_joint  &
   adams_id = 12  &
   i_marker_name = .template_4_retract.ges_collar.jxs_joint_i_1  &
   j_marker_name = .template_4_retract.ges_upper_cylinder.jxs_joint_j_1
!
constraint attributes  &
   constraint_name = .template_4_retract.josrev_collar_uc_joint  &
   visibility = on  &
   size_of_icons = 25.0
!
constraint create joint cylindrical  &
   joint_name = .template_4_retract.joscly_ac_rd  &
   adams_id = 13  &
   i_marker_name = .template_4_retract.ges_sf_rod.MARKER_84  &
   j_marker_name = .template_4_retract.ges_sf_actuator.MARKER_85
!
constraint attributes  &
   constraint_name = .template_4_retract.joscly_ac_rd  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!----------------------------------- Forces -----------------------------------!
!
!
force create direct general_force  &
   general_force_name = .template_4_retract.NLG_aeroforce  &
   adams_id = 1  &
   i_marker_name = .template_4_retract.ges_upper_cylinder.MARKER_781  &
   j_floating_marker_name =   &
                            .template_4_retract.ges_lower_cylinder.FMARKER_783  &
   ref_marker_name = .template_4_retract.ges_lower_cylinder.MARKER_782  &
   x_force_function = ""  &
   y_force_function = ""  &
   z_force_function = ""  &
   x_torque_function = ""  &
   y_torque_function = ""  &
   z_torque_function = ""
!
force attributes  &
   force_name = .template_4_retract.NLG_aeroforce  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_4_retract.nlg_ZDT_FORCE  &
   adams_id = 3  &
   type_of_freedom = translational  &
   i_marker_name = .template_4_retract.ges_sf_rod.MARKER_79  &
   j_marker_name = .template_4_retract.ges_sf_rod.MARKER_80  &
   action_only = on  &
   function = ""
!
force attributes  &
   force_name = .template_4_retract.nlg_ZDT_FORCE  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_4_retract.NLG_stopper_up  &
   adams_id = 19  &
   type_of_freedom = translational  &
   i_marker_name = .template_4_retract.ges_sf_rod.MARKER_784  &
   j_marker_name = .template_4_retract.ges_sf_rod.MARKER_785  &
   action_only = on  &
   function = ""
!
force attributes  &
   force_name = .template_4_retract.NLG_stopper_up  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_4_retract.NLG_stopper_low  &
   adams_id = 5  &
   type_of_freedom = translational  &
   i_marker_name = .template_4_retract.ges_sf_rod.MARKER_90  &
   j_marker_name = .template_4_retract.ges_sf_rod.MARKER_91  &
   action_only = on  &
   function = ""
!
force attributes  &
   force_name = .template_4_retract.NLG_stopper_low  &
   size_of_icons = 25.0
!
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .template_4_retract.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=10.0 step_size=1.0E-02 model_name=.gcmb4_retract"
!
simulation script create  &
   sim_script_name = .template_4_retract.Last_Sim_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_4_retract.Last_Sim_3  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=.retract_mlg_force"
!
simulation script create  &
   sim_script_name = .template_4_retract.Last_Sim_2_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_4_retract.Last_Sim_3_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_nlg_post_2hubs"
!
simulation script create  &
   sim_script_name = .template_4_retract.Last_Sim_2_2_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
!-------------------------- Adams View UDE Instances --------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
undo begin_block suppress = yes
!
ude create instance  &
   instance_name = .template_4_retract.NLG_SPRING_nlg  &
   definition_name = .MDI.Forces.spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_4_retract.NLG_SPRING_nlg  &
   color = RED
!
ude create instance  &
   instance_name = .template_4_retract.NLG_TORSION_SPRING_2  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_4_retract.NLG_TORSION_SPRING_4  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.i_marker  &
   object_value = (.template_4_retract.ges_sf_rod.MARKER_511)
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.j_marker  &
   object_value = (.template_4_retract.ges_sf_actuator.MARKER_512)
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.stiffness_coefficient  &
   real_value = (0.36(newton/mm))
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.damping_coefficient  &
   real_value = 120.0
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.free_length_mode  &
   string_value = "Design_Length"
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.free_length  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.i_dynamic_visibility  &
   string_value = "On"
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.j_dynamic_visibility  &
   string_value = "Off"
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.spring_visibility  &
   string_value = "depends"
!
variable modify  &
   variable_name = .template_4_retract.NLG_SPRING_nlg.damper_visibility  &
   string_value = "depends"
!
ude modify instance  &
   instance_name = .template_4_retract.NLG_SPRING_nlg
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.i_marker  &
   object_value = (.template_4_retract.ges_upper_cylinder.MARKER_526)
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.j_marker  &
   object_value = (.template_4_retract.ges_subframe.MARKER_527)
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.stiffness_coefficient  &
   real_value = (9.7E+04(newton-mm/rad))
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.damping_coefficient  &
   real_value = 10.0
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_2.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_4_retract.NLG_TORSION_SPRING_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.i_marker  &
   object_value = (.template_4_retract.ges_sf_actuator.MARKER_532)
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.j_marker  &
   object_value = (.template_4_retract.ges_subframe.MARKER_533)
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.stiffness_coefficient  &
   real_value = (3.5E-05(newton-mm/rad))
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.damping_coefficient  &
   real_value = 30.0
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_4_retract.NLG_TORSION_SPRING_4.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_4_retract.NLG_TORSION_SPRING_4
!
undo end_block
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
geometry create shape force  &
   force_name = .template_4_retract.SFORCE_3_force_graphic_1  &
   adams_id = 44  &
   force_element_name = .template_4_retract.nlg_ZDT_FORCE  &
   applied_at_marker_name = .template_4_retract.ges_sf_rod.MARKER_79
!
geometry create shape force  &
   force_name = .template_4_retract.GFORCE_1_force_graphic_1  &
   adams_id = 463  &
   force_element_name = .template_4_retract.NLG_aeroforce  &
   applied_at_marker_name =   &
                            .template_4_retract.ges_upper_cylinder.MARKER_781
!
geometry create shape force  &
   force_name = .template_4_retract.SFORCE_5_force_graphic_1  &
   adams_id = 46  &
   force_element_name = .template_4_retract.NLG_stopper_low  &
   applied_at_marker_name = .template_4_retract.ges_sf_rod.MARKER_90
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
   force_name = .template_4_retract.gravity  &
   visibility = off  &
   size_of_icons = 25.0
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------------- Measures ----------------------------------!
!
!
measure create object  &
   measure_name = .template_4_retract.NLG_sf_angle  &
   from_first = yes  &
   object = .template_4_retract.josrev_uc_sf_joint  &
   characteristic = ax_ay_az_projection_angles  &
   component = z_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_4_retract.NLG_sf_angle  &
   color = WHITE
!
measure create object  &
   measure_name = .template_4_retract.NLG_vel  &
   from_first = yes  &
   object = .template_4_retract.joscly_ac_rd  &
   characteristic = translational_velocity  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_4_retract.NLG_vel  &
   color = WHITE
!
measure create pt2pt  &
   measure_name = .template_4_retract.NLG_disp_sf  &
   from_point = .template_4_retract.ges_sf_rod.MARKER_96  &
   to_point = .template_4_retract.ges_sf_actuator.MARKER_97  &
   characteristic = translational_displacement  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_4_retract.NLG_disp_sf  &
   color = WHITE
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_4_retract.mts_body_mount.minor_role  &
   string_value = "inherit"
!
variable create  &
   variable_name = .template_4_retract.AIR_VELOCITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 55.0
!
variable create  &
   variable_name = .template_4_retract.AIR_DENSITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_4_retract.NLG_DRAG_COEFF  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.7
!
variable create  &
   variable_name = .template_4_retract.NLG_PROJ_AREA  &
   units = "area"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.3077
!
variable create  &
   variable_name = .template_4_retract.NLG_RETRACT_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.7E+04
!
variable create  &
   variable_name = .template_4_retract.NLG_RETRACT_RAMP_UP  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_4_retract.NLG_RETRACT_RETRACT_RAMP_DOWN  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_4_retract.NLG_EXTEND_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.2E+04
!
variable create  &
   variable_name = .template_4_retract.NLG_EXTEND_RAMP_UP  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.2
!
variable create  &
   variable_name = .template_4_retract.NLG_ACTUATOR_STROKE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 632.0
!
variable create  &
   variable_name = .template_4_retract.NLG_RETRACT_HOLD_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
variable create  &
   variable_name = .template_4_retract.NLG_EXTEND_HOLD_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.0
!
variable create  &
   variable_name = .template_4_retract.NLG_EXTEND_RETRACT_RETRACT_RAMP_DOWN  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.2
!
!---------------------------- Function definitions ----------------------------!
!
!
force modify direct single_component_force  &
   single_component_force_name = .template_4_retract.nlg_ZDT_FORCE  &
   function = "STEP( time , 0 , 0 , .template_4_retract.NLG_RETRACT_RAMP_UP , .template_4_retract.NLG_RETRACT_FORCE )+",  &
              "STEP( time , .template_4_retract.NLG_RETRACT_RAMP_UP , 0 , .template_4_retract.NLG_RETRACT_RAMP_UP+.template_4_retract.NLG_RETRACT_HOLD_TIME , 0 )+",  &
              "STEP( time , .template_4_retract.NLG_RETRACT_RAMP_UP+.template_4_retract.NLG_RETRACT_HOLD_TIME , 0 , .template_4_retract.NLG_RETRACT_RAMP_UP+.template_4_retract.NLG_RETRACT_HOLD_TIME+.template_4_retract.NLG_RETRACT_RETRACT_RAMP_DOWN , -.template_4_retract.NLG_RETRACT_FORCE )+",  &
              "STEP( time , .template_4_retract.NLG_RETRACT_RAMP_UP+.template_4_retract.NLG_RETRACT_HOLD_TIME+.template_4_retract.NLG_RETRACT_RETRACT_RAMP_DOWN  , 0 , .template_4_retract.NLG_RETRACT_RAMP_UP+.template_4_retract.NLG_RETRACT_HOLD_TIME+.template_4_retract.NLG_RETRACT_RETRACT_RAMP_DOWN+.template_4_retract.NLG_EXTEND_RAMP_UP  , -.template_4_retract.NLG_EXTEND_FORCE )+",  &
              "STEP( time , .template_4_retract.NLG_RETRACT_RAMP_UP+.template_4_retract.NLG_RETRACT_HOLD_TIME+.template_4_retract.NLG_RETRACT_RETRACT_RAMP_DOWN+.template_4_retract.NLG_EXTEND_RAMP_UP  , 0 , .template_4_retract.NLG_RETRACT_RAMP_UP+.template_4_retract.NLG_RETRACT_HOLD_TIME+.template_4_retract.NLG_RETRACT_RETRACT_RAMP_DOWN+.template_4_retract.NLG_EXTEND_RAMP_UP+.template_4_retract.NLG_EXTEND_HOLD_TIME  , 0 )+",  &
              "STEP( time , .template_4_retract.NLG_RETRACT_RAMP_UP+.template_4_retract.NLG_RETRACT_HOLD_TIME+.template_4_retract.NLG_RETRACT_RETRACT_RAMP_DOWN+.template_4_retract.NLG_EXTEND_RAMP_UP+.template_4_retract.NLG_EXTEND_HOLD_TIME  , 0 , .template_4_retract.NLG_RETRACT_RAMP_UP+.template_4_retract.NLG_RETRACT_HOLD_TIME+.template_4_retract.NLG_RETRACT_RETRACT_RAMP_DOWN+.template_4_retract.NLG_EXTEND_RAMP_UP+.template_4_retract.NLG_EXTEND_HOLD_TIME+.template_4_retract.NLG_EXTEND_RETRACT_RETRACT_RAMP_DOWN  , .template_4_retract.NLG_EXTEND_FORCE )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_4_retract.NLG_stopper_up  &
   function = "abs(IF( .template_4_retract.NLG_disp_sf-1217.6474-.template_4_retract.NLG_ACTUATOR_STROKE :0, 0 ,10000000*abs(.template_4_retract.NLG_disp_sf-1217.6474-.template_4_retract.NLG_ACTUATOR_STROKE)))+abs(IF( .template_4_retract.NLG_disp_sf-1217.6474-.template_4_retract.NLG_ACTUATOR_STROKE :0, 0 ,100000000*abs(.template_4_retract.NLG_vel)))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_4_retract.NLG_stopper_low  &
   function = "-abs(IF( .template_4_retract.NLG_disp_sf-1217.6474 :50000000000*abs(.template_4_retract.NLG_disp_sf-1217.6474), 0 ,0 ))"
!
force modify direct general_force  &
   general_force_name = .template_4_retract.NLG_aeroforce  &
   x_force_function = ".template_4_retract.NLG_DRAG_COEFF*abs(IF( -.template_4_retract.NLG_sf_angle-60 : COS( 1.225*-.template_4_retract.NLG_sf_angle*pi/180 ) , COS( 1.225*-.template_4_retract.NLG_sf_angle*pi/180 ) , COS( -.template_4_retract.NLG_sf_angle*pi/180 ) ))*.template_4_retract.NLG_PROJ_AREA*cos(-.template_4_retract.NLG_sf_angle*pi/180)*0.5*.template_4_retract.AIR_DENSITY*.template_4_retract.AIR_VELOCITY*abs(.template_4_retract.AIR_VELOCITY)*cos(-.template_4_retract.NLG_sf_angle*pi/180) "  &
   y_force_function = "0"  &
   z_force_function = ".template_4_retract.NLG_DRAG_COEFF*abs(IF( -.template_4_retract.NLG_sf_angle-60 : COS( 1.225*-.template_4_retract.NLG_sf_angle*pi/180 ) , COS( 1.225*-.template_4_retract.NLG_sf_angle*pi/180 ) , COS( -.template_4_retract.NLG_sf_angle*pi/180 ) ))*.template_4_retract.NLG_PROJ_AREA*cos(-.template_4_retract.NLG_sf_angle*pi/180)*0.5*.template_4_retract.AIR_DENSITY*.template_4_retract.AIR_VELOCITY*abs(.template_4_retract.AIR_VELOCITY)*sin(-.template_4_retract.NLG_sf_angle*pi/180) "  &
   x_torque_function = "0"  &
   y_torque_function = "-1*CUBSPL( -1*.template_4_retract.NLG_sf_angle, 0 , .template_4_retract.SPLINE_angle_aeroforce, 0 )"  &
   z_torque_function = "0"
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_4_retract.NLG_SPRING_nlg
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_4_retract.NLG_TORSION_SPRING_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_4_retract.NLG_TORSION_SPRING_4
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_4_retract.ground.mts_mount_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.mts_body_mount))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_4_retract.mts_body_mount))
!
marker modify  &
   marker_name = .template_4_retract.ground.cfl_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_4_retract.ground.hpl_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hpl_wheel_center, .template_4_retract.ground.hpl_ob_axle, "Z"))
!
marker modify  &
   marker_name = .template_4_retract.ground.cfr_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_4_retract.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hpr_wheel_center, .template_4_retract.ground.hpr_ob_axle, "Z"))
!
marker modify  &
   marker_name = .template_4_retract.ground.cfs_nlg_axle_lowpoint  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_4_retract.ground.hps_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_4_retract.ground.origo))
!
marker modify  &
   marker_name = .template_4_retract.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_4_retract.ground.hps_uc_bot, .template_4_retract.ground.hps_uc_top, 0.11 * DM(.template_4_retract.ground.hps_uc_bot, .template_4_retract.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_uc_bot, .template_4_retract.ground.hps_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_4_retract.ground.uel_gearaero_origin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.origo1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.origo1))
!
marker modify  &
   marker_name = .template_4_retract.ground.uer_gearaero_origin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.origo1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.origo1))
!
material modify  &
   material_name = .template_4_retract.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.steel_3  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.aluminum_3  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.steel_2_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.aluminum_2_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.steel_3_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.aluminum_3_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.steel_2_2_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_4_retract.aluminum_2_2_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .template_4_retract.ges_sf_actuator.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_db_sf_atch, .template_4_retract.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .template_4_retract.ges_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_sf_actuator.jxs_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_subframe.jxs_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_subframe.jxs_joint_j_14))  &
   relative_to = .template_4_retract.ges_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_sf_actuator.MARKER_532  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_db_sf_atch))  &
   relative_to = .template_4_retract.ges_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_sf_actuator.gralin_dragbrace_geom  &
   length = (DM(.template_4_retract.ground.hps_db_sf_atch, .template_4_retract.ground.hps_db_uc_atch))
!
marker modify  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_sf_rod.PT3))  &
   relative_to = .template_4_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_uc_top, .template_4_retract.ground.hps_uc_bot, "Z"))  &
   relative_to = .template_4_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_uc_sf_atch_l, .template_4_retract.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_4_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_uc_sf_atch_r, .template_4_retract.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_4_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_4_retract.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_uc_bot, .template_4_retract.ground.hps_uc_top, "Z"))  &
   relative_to = .template_4_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_upper_cylinder.MARKER_781  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}, .template_4_retract.ground.hps_aeroforceN))  &
   relative_to = .template_4_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.template_4_retract.ground.hps_uc_top, .template_4_retract.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.template_4_retract.ground.hps_uc_sf_atch_l, .template_4_retract.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.template_4_retract.ground.hps_uc_sf_atch_r, .template_4_retract.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_lc_top, .template_4_retract.ground.hps_lc_bot, "Z"))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hpr_wheel_center, .template_4_retract.ground.hpl_wheel_center, "Z"))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_uta_uc_atch, .template_4_retract.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_lta_lc_atch, .template_4_retract.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_359  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_lockroller_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_lockroller_l, .template_4_retract.ground.hps_lockroller_l_2, "Z"))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_360  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_lockroller_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_lockroller_r, .template_4_retract.ground.hps_lockroller_r_2, "Z"))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_361  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_lockroller_r_2))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_lockroller_r_2, .template_4_retract.ground.hps_lockroller_l_2, "Z"))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_782  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}, .template_4_retract.ground.hps_aeroforceN))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_436  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.suo_qiu_point))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_786  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hpl_ob_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hpl_ob_axle, .template_4_retract.ground.hpl_wheel_center, "Z"))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_lower_cylinder.MARKER_787  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hpr_ob_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hpr_ob_axle, .template_4_retract.ground.hpr_wheel_center, "Z"))  &
   relative_to = .template_4_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.gralin_geom1  &
   length = (DM(.template_4_retract.ground.hps_lc_top, .template_4_retract.ground.hps_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.gralin_geom2  &
   length = (DM(.template_4_retract.ground.hpr_wheel_center, .template_4_retract.ground.hpl_wheel_center))
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.CYLINDER_128  &
   length = (73.0mm)  &
   radius = (8.125mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.CYLINDER_132  &
   length = (73.0mm)  &
   radius = (8.125mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.CYLINDER_136  &
   length = (100.0mm)  &
   radius = (7.5mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.gralin_lower_torque_arm_geom  &
   length = (DM(.template_4_retract.ground.hps_lta_lc_atch, .template_4_retract.ground.hps_lta_uta_atch))
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_lower_cylinder.gralin_upper_torque_arm_geom  &
   length = (DM(.template_4_retract.ground.hps_uta_uc_atch, .template_4_retract.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_4_retract.ges_subframe.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_subframe.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_subframe))  &
   relative_to = .template_4_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_subframe.graout_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_uc_sf_atch_r))  &
   relative_to = .template_4_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_subframe.graout_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_uc_sf_atch_l))  &
   relative_to = .template_4_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_subframe.graout_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_db_sf_atch))  &
   relative_to = .template_4_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_subframe.jxs_joint_i_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.mts_body_mount.jxs_joint_j_16))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_4_retract.mts_body_mount.jxs_joint_j_16))  &
   relative_to = .template_4_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_subframe.jxs_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_4_retract.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_4_retract.ground.origo))  &
   relative_to = .template_4_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_subframe.MARKER_533  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_db_sf_atch))  &
   relative_to = .template_4_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.mts_body_mount.jxs_joint_j_16  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_4_retract.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_4_retract.ground.origo))  &
   relative_to = .template_4_retract.mts_body_mount
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
part modify rigid_body name_and_position  &
   part_name = .template_4_retract.mts_body_mount  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.origo))
!
marker modify  &
   marker_name = .template_4_retract.ges_collar.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ground.hps_uc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ground.hps_uc_bot, .template_4_retract.ground.cfs_collar_top, "Z"))  &
   relative_to = .template_4_retract.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_4_retract.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_collar.gralin_collar  &
   length = (DM(.template_4_retract.ground.hps_uc_bot, .template_4_retract.ground.cfs_collar_top))
!
marker modify  &
   marker_name = .template_4_retract.ges_sf_rod.MARKER_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_4_retract.ges_sf_rod.PT3))  &
   relative_to = .template_4_retract.ges_sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
marker modify  &
   marker_name = .template_4_retract.ges_sf_rod.gralin_25  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}, .template_4_retract.ground.hps_rod_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_4_retract.ges_sf_rod.PT3, .template_4_retract.ground.hps_db_sf_atch, "Z"))  &
   relative_to = .template_4_retract.ges_sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_4_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_4_retract.ges_sf_rod.CYLINDER_30  &
   length = (DM(.template_4_retract.ground.hps_rod_bot, .template_4_retract.ground.hps_rod_top))  &
   radius = (27.5mm)
!
geometry modify shape force  &
   force_name = .template_4_retract.SFORCE_3_force_graphic_1  &
   applied_at_marker_name = (.template_4_retract.nlg_ZDT_FORCE.i)
!
geometry modify shape force  &
   force_name = .template_4_retract.GFORCE_1_force_graphic_1  &
   applied_at_marker_name = (.template_4_retract.NLG_aeroforce.i)
!
geometry modify shape force  &
   force_name = .template_4_retract.SFORCE_5_force_graphic_1  &
   applied_at_marker_name = (.template_4_retract.NLG_stopper_low.i)
!
model display  &
   model_name = template_4_retract

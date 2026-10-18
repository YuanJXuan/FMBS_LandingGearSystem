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
   size_of_icons = 25.4  &
   spacing_for_grid = 25.4
!
!------------------------------ Adams View Model ------------------------------!
!
!
model create  &
   model_name = template_2_retract  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_2_retract  &
   size_of_icons = 50.8
!
view erase
!
!-------------------------------- Data storage --------------------------------!
!
!
data_element create spline  &
   spline_name = .template_2_retract.SPLINE_angle_aeroforce  &
   adams_id = 2  &
   x = -20.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0,  &
       90.0, 100.0  &
   y = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0  &
   linear_extrapolate = no
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .template_2_retract.steel  &
   adams_id = 2  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_2_retract.aluminum  &
   adams_id = 3  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_2_retract.steel_2  &
   adams_id = 1  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_2_retract.aluminum_2  &
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
   default_coordinate_system = .template_2_retract.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract.ground.origo  &
   adams_id = 10  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ground.origo  &
   visibility = on  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ground.cfs_uc_sf_atch_mid  &
   adams_id = 12  &
   location = 6314.44, 0.0, 1691.64  &
   orientation = 0.0d, 90.0000000003d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ground.cfs_uc_sf_atch_mid  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_2_retract.ground.cfs_collar_top  &
   adams_id = 19  &
   location = 6197.6, 0.0, 856.996  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ground.cfs_collar_top  &
   color = MAIZE  &
   visibility = on
!
marker create  &
   marker_name = .template_2_retract.ground.MARKER_161  &
   adams_id = 161  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 327.8470327224d, 77.5794781674d, 2.8032019858d
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_2_retract.ground.uel_gearaero_jfloat_1  &
   adams_id = 158
!
floating_marker create  &
   floating_marker_name = .template_2_retract.ground.uer_gearaero_jfloat_1  &
   adams_id = 159
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_2_retract.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_2_retract.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_2_retract.ground.hps_uc_sf_atch_l  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_2_retract.ground.hps_uc_sf_atch_r  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_2_retract.ground.hps_lc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_2_retract.ground.hps_uc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_2_retract.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_uta_uc_atch  &
   location = 6324.6, 0.0, 838.2
!
point attributes  &
   point_name = .template_2_retract.ground.hps_uta_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_lta_lc_atch  &
   location = 6299.2, 0.0, 533.4
!
point attributes  &
   point_name = .template_2_retract.ground.hps_lta_lc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_lta_uta_atch  &
   location = 6654.8, 0.0, 711.2
!
point attributes  &
   point_name = .template_2_retract.ground.hps_lta_uta_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_2_retract.ground.hps_uc_geompt  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_2_retract.ground.hps_uc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_2_retract.ground.hps_lc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract.ground.hpl_wheel_center  &
   location = 6229.096, -209.55, 508.0
!
point create  &
   point_name = .template_2_retract.ground.hpr_wheel_center  &
   location = 6229.096, 209.55, 508.0
!
point create  &
   point_name = .template_2_retract.ground.hpl_ob_axle  &
   location = 6229.096, -285.75, 508.0
!
point create  &
   point_name = .template_2_retract.ground.hpr_ob_axle  &
   location = 6229.096, 285.75, 508.0
!
point create  &
   point_name = .template_2_retract.ground.hps_nlg_axle_lowpoint  &
   location = 6229.096, 0.0, 482.6
!
point create  &
   point_name = .template_2_retract.ground.hps_rod_bot  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point create  &
   point_name = .template_2_retract.ground.hps_rod_top  &
   location = 7227.4389033572, 0.0, 1472.1512863532
!
point create  &
   point_name = .template_2_retract.ground.hps_aeroforceN  &
   location = 6200.9167643494, 3.3850517933E-11, 1207.1824231157
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_2_retract.ground  &
   size_of_icons = 50.8
!
!------------------------------ ges_sf_actuator -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract.ges_sf_actuator  &
   adams_id = 7  &
   location = 6967.855, 0.0, 1319.53  &
   orientation = 270.0000000009d, 120.4532239116d, 90.0000000003d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ges_sf_actuator
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract.ges_sf_actuator.cm  &
   adams_id = 21  &
   location = -2.6589288646E-08, -8.1094015533E-09, -25.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_actuator.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_sf_actuator.gralin_1  &
   adams_id = 23  &
   location = -2.6589286328E-08, -8.1094057298E-09, -598.873681109  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_actuator.gralin_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_sf_actuator.jxs_joint_i_14  &
   adams_id = 24  &
   location = -2.6589230817E-08, -8.1094057298E-09, -598.873681109  &
   orientation = 0.0d, 89.9999999991d, 239.5467760884d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_actuator.jxs_joint_i_14  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_sf_actuator.MARKER_85  &
   adams_id = 85  &
   location = 1.3451462166E-09, 0.0, 158.8736811071  &
   orientation = 90.0000000003d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_actuator.MARKER_85  &
   visibility = on
!
marker create  &
   marker_name = .template_2_retract.ges_sf_actuator.MARKER_97  &
   adams_id = 97  &
   location = -4.5918824298E-10, 0.0, -598.873681109  &
   orientation = 90.0000000003d, 120.4532239116d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_actuator.MARKER_97  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract.ges_sf_actuator  &
   material_type = .template_2_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_sf_actuator.gralin_dragbrace_geom  &
   adams_id = 32  &
   center_marker = .template_2_retract.ges_sf_actuator.gralin_1  &
   angle_extent = 360.0000000012  &
   length = 1147.7473622179  &
   radius = 50.8  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_sf_actuator.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .template_2_retract.ges_sf_actuator  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract.ges_upper_cylinder  &
   adams_id = 8  &
   location = 6197.6, 0.0, 1193.8  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ges_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract.ges_upper_cylinder.MARKER_4  &
   adams_id = 4  &
   location = -236.7591354821, -2.4792465641E-09, 187.9366952496  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_cylinder.MARKER_4  &
   visibility = on
!
marker create  &
   marker_name = .template_2_retract.ges_upper_cylinder.cm  &
   adams_id = 25  &
   location = -2.1926640514, -2.2900518287E-11, -14.5859826029  &
   orientation = 90.0000000006d, 0.8375931978d, 270.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_upper_cylinder.gralin_2  &
   adams_id = 27  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_cylinder.gralin_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_upper_cylinder.gralin_3  &
   adams_id = 28  &
   location = -116.8399999964, -340.3600000012, -497.84  &
   orientation = 161.0534953111d, 58.7414044414d, 213.4869581738d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_cylinder.gralin_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_upper_cylinder.gralin_4  &
   adams_id = 29  &
   location = -116.8400000036, 340.3599999988, -497.84  &
   orientation = 18.9465046901d, 58.7414044414d, 326.5130418244d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_cylinder.gralin_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_j_11  &
   adams_id = 30  &
   location = 0.0, 0.0, 114.3  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_j_11  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_i_15  &
   adams_id = 31  &
   location = -116.84, -1.2234292211E-09, -497.84  &
   orientation = 0.0d, 89.9999999997d, 180.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_i_15  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_j_1  &
   adams_id = 35  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_j_1  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_upper_cylinder.MARKER_162  &
   adams_id = 162  &
   location = -3.3167643494, 0.0, -13.3824231157  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract.ges_upper_cylinder  &
   material_type = .template_2_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 33  &
   center_marker = .template_2_retract.ges_upper_cylinder.gralin_2  &
   angle_extent = 360.0000000012  &
   length = 863.6  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 34  &
   center_marker = .template_2_retract.ges_upper_cylinder.gralin_3  &
   angle_extent = 360.0000000012  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 35  &
   center_marker = .template_2_retract.ges_upper_cylinder.gralin_4  &
   angle_extent = 360.0000000012  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_2_retract.ges_upper_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract.ges_lower_cylinder  &
   adams_id = 9  &
   location = 6197.6, 0.0, 952.5  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ges_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract.ges_lower_cylinder.cm  &
   adams_id = 38  &
   location = -7.8736475458, -8.2416712344E-11, 111.1200258466  &
   orientation = 270.0000000006d, 1.780178135d, 90.0000000001d
!
marker attributes  &
   marker_name = .template_2_retract.ges_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_lower_cylinder.gralin_5  &
   adams_id = 40  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_lower_cylinder.gralin_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_lower_cylinder.jxs_joint_j_9  &
   adams_id = 41  &
   location = -101.6, -1.0639558371E-09, 419.1  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_lower_cylinder.jxs_joint_j_9  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_lower_cylinder.jxs_joint_i_11  &
   adams_id = 42  &
   location = 0.0, 0.0, -127.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_lower_cylinder.jxs_joint_i_11  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_lower_cylinder.gralin_7  &
   adams_id = 43  &
   location = -31.4960000022, 209.5499999997, 444.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_lower_cylinder.gralin_7  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_lower_cylinder.MARKER_163  &
   adams_id = 163  &
   location = -3.3167643494, 0.0, -254.6824231157  &
   orientation = 180.0000000006d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_retract.ges_lower_cylinder.MARKER_165  &
   adams_id = 165  &
   location = -31.495999997, -285.7500000003, 444.5  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_2_retract.ges_lower_cylinder.MARKER_166  &
   adams_id = 166  &
   location = -31.496000003, 285.7499999997, 444.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_2_retract.ges_lower_cylinder.FMARKER_164  &
   adams_id = 164
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract.ges_lower_cylinder  &
   material_type = .template_2_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_lower_cylinder.gralin_geom1  &
   adams_id = 36  &
   center_marker = .template_2_retract.ges_lower_cylinder.gralin_5  &
   angle_extent = 360.0000000012  &
   length = 889.0  &
   radius = 101.6  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_lower_cylinder.gralin_geom2  &
   adams_id = 37  &
   center_marker = .template_2_retract.ges_lower_cylinder.gralin_7  &
   angle_extent = 360.0000000012  &
   length = 419.1  &
   radius = 30.48  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_lower_cylinder.gralin_geom2  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_lower_cylinder.CYLINDER_44  &
   adams_id = 44  &
   center_marker = .template_2_retract.ges_lower_cylinder.MARKER_165  &
   angle_extent = 360.0  &
   length = 90.0  &
   radius = 120.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_lower_cylinder.CYLINDER_46  &
   adams_id = 46  &
   center_marker = .template_2_retract.ges_lower_cylinder.MARKER_166  &
   angle_extent = 360.0  &
   length = 90.0  &
   radius = 120.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_2_retract.ges_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!---------------------------- ges_upper_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract.ges_upper_torque_arm  &
   adams_id = 10  &
   location = 6489.7, 0.0, 774.7  &
   orientation = 90.0000000003d, 111.0375110247d, 270.0000000009d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ges_upper_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract.ges_upper_torque_arm.cm  &
   adams_id = 49  &
   location = -2.2285994229E-09, 8.6446043838E-10, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_torque_arm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_upper_torque_arm.gralin_9  &
   adams_id = 51  &
   location = -2.2285992496E-09, 8.644590757E-10, -176.8905311202  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_torque_arm.gralin_9  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_upper_torque_arm.jxs_joint_j_8  &
   adams_id = 52  &
   location = 2.2282800605E-09, -8.644590757E-10, 176.8905311202  &
   orientation = 0.0d, 90.0000000003d, 111.0375110247d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_torque_arm.jxs_joint_j_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_upper_torque_arm.jxs_joint_i_10  &
   adams_id = 53  &
   location = -2.2285992496E-09, 8.644590757E-10, -176.8905311202  &
   orientation = 0.0d, 90.0000000003d, 111.0375110247d
!
marker attributes  &
   marker_name = .template_2_retract.ges_upper_torque_arm.jxs_joint_i_10  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract.ges_upper_torque_arm  &
   material_type = .template_2_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   adams_id = 38  &
   center_marker = .template_2_retract.ges_upper_torque_arm.gralin_9  &
   angle_extent = 360.0000000012  &
   length = 353.7810622405  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   color = GREEN
!
part attributes  &
   part_name = .template_2_retract.ges_upper_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!---------------------------- ges_lower_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract.ges_lower_torque_arm  &
   adams_id = 11  &
   location = 6477.0, 0.0, 622.3  &
   orientation = 90.0000000003d, 63.4349488233d, 270.0000000009d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ges_lower_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract.ges_lower_torque_arm.cm  &
   adams_id = 54  &
   location = 1.3112007061E-09, 9.309558938E-10, 0.0  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_lower_torque_arm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_lower_torque_arm.jxs_joint_i_8  &
   adams_id = 56  &
   location = -1.3110207364E-09, -9.3095592762E-10, 198.7864431997  &
   orientation = 0.0d, 90.0000000009d, 63.4349488233d
!
marker attributes  &
   marker_name = .template_2_retract.ges_lower_torque_arm.jxs_joint_i_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_lower_torque_arm.gralin_10  &
   adams_id = 57  &
   location = 1.3112011477E-09, 9.3095592762E-10, -198.7864431997  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_lower_torque_arm.gralin_10  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_lower_torque_arm.jxs_joint_i_9  &
   adams_id = 58  &
   location = 1.3112011477E-09, 9.3095592762E-10, -198.7864431997  &
   orientation = 269.9999999991d, 63.4349488233d, 89.9999999997d
!
marker attributes  &
   marker_name = .template_2_retract.ges_lower_torque_arm.jxs_joint_i_9  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract.ges_lower_torque_arm  &
   material_type = .template_2_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   adams_id = 39  &
   center_marker = .template_2_retract.ges_lower_torque_arm.gralin_10  &
   angle_extent = 360.0000000012  &
   length = 397.5728863995  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_2_retract.ges_lower_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!-------------------------------- ges_subframe --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract.ges_subframe  &
   adams_id = 12  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0000000003d, 356.6444799104d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ges_subframe
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract.ges_subframe.MARKER_160  &
   adams_id = 160  &
   location = 0.0, 0.0, 0.0  &
   orientation = 250.8736266414d, 34.2270434235d, 111.6927114759d
!
marker create  &
   marker_name = .template_2_retract.ges_subframe.cm  &
   adams_id = 59  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_subframe.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_subframe.inertia_frame  &
   adams_id = 60  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_subframe.inertia_frame  &
   visibility = on  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_subframe.graout_1  &
   adams_id = 61  &
   location = -390.5595878991, 6.4598604244E-09, -340.3600000001  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_subframe.graout_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_subframe.graout_2  &
   adams_id = 62  &
   location = -390.5595878993, 1.0017979502E-08, 340.3599999999  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_subframe.graout_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_subframe.graout_3  &
   adams_id = 63  &
   location = 781.1191757984, -1.6477617881E-08, 2.3938866711E-10  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_subframe.graout_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract.ges_subframe.jxs_joint_j_15  &
   adams_id = 64  &
   location = -390.5595878992, 8.2389199629E-09, -1.1969433355E-10  &
   orientation = 3.3555200896d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_subframe.jxs_joint_j_15  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_subframe.jxs_joint_j_14  &
   adams_id = 66  &
   location = 781.1191757984, -1.6477617881E-08, 2.3938866711E-10  &
   orientation = 3.3555200896d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_subframe.jxs_joint_j_14  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract.ges_subframe  &
   mass = 4.5359237E-03  &
   center_of_mass_marker = .template_2_retract.ges_subframe.cm  &
   inertia_marker = .template_2_retract.ges_subframe.inertia_frame  &
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
   outline_name = .template_2_retract.ges_subframe.graout_subframe_geom  &
   adams_id = 41  &
   marker_name =  &
      .template_2_retract.ges_subframe.graout_1,  &
      .template_2_retract.ges_subframe.graout_2,  &
      .template_2_retract.ges_subframe.graout_3  &
   visibility_between_markers = on, on, on  &
   close = yes
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_subframe.graout_subframe_geom  &
   color = WHITE
!
part attributes  &
   part_name = .template_2_retract.ges_subframe  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!--------------------------------- ges_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract.ges_collar  &
   adams_id = 14  &
   location = 6197.6, 0.0, 809.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ges_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract.ges_collar.jxs_joint_j_10  &
   adams_id = 69  &
   location = 127.0, 0.0, 28.702  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_collar.jxs_joint_j_10  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_collar.cm  &
   adams_id = 70  &
   location = 0.0, 0.0, 0.0  &
   orientation = 180.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_collar.cm  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_collar.gralin_24  &
   adams_id = 72  &
   location = 0.0, 0.0, -47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_collar.gralin_24  &
   visibility = on  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract.ges_collar.jxs_joint_i_1  &
   adams_id = 73  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_collar.jxs_joint_i_1  &
   visibility = on  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract.ges_collar  &
   material_type = .template_2_retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_collar.gralin_collar  &
   adams_id = 40  &
   center_marker = .template_2_retract.ges_collar.gralin_24  &
   angle_extent = 360.0000000012  &
   length = 94.996  &
   radius = 139.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract.ges_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .template_2_retract.ges_collar  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- ges_sf_rod ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract.ges_sf_rod  &
   adams_id = 5  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ges_sf_rod
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract.ges_sf_rod.MARKER_5  &
   adams_id = 5  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_rod.MARKER_5  &
   visibility = on
!
marker create  &
   marker_name = .template_2_retract.ges_sf_rod.gralin_25  &
   adams_id = 3  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 270.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_rod.gralin_25  &
   visibility = on
!
marker create  &
   marker_name = .template_2_retract.ges_sf_rod.cm  &
   adams_id = 76  &
   location = 6830.8990194197, 0.0, 1239.0072955518  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_rod.cm  &
   visibility = on
!
marker create  &
   marker_name = .template_2_retract.ges_sf_rod.MARKER_84  &
   adams_id = 84  &
   location = 6830.8990194192, 0.0, 1239.0072955517  &
   orientation = 90.0000000003d, 59.5467760889d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_rod.MARKER_84  &
   visibility = on
!
marker create  &
   marker_name = .template_2_retract.ges_sf_rod.MARKER_96  &
   adams_id = 96  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_rod.MARKER_96  &
   visibility = on
!
marker create  &
   marker_name = .template_2_retract.ges_sf_rod.MARKER_101  &
   adams_id = 101  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract.ges_sf_rod.MARKER_101  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract.ges_sf_rod  &
   material_type = .template_2_retract.steel
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_2_retract.ges_sf_rod.PT3  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point attributes  &
   point_name = .template_2_retract.ges_sf_rod.PT3  &
   visibility = off  &
   name_visibility = off
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract.ges_sf_rod.CYLINDER_30  &
   adams_id = 30  &
   center_marker = .template_2_retract.ges_sf_rod.gralin_25  &
   angle_extent = 360.0000000012  &
   length = 920.0  &
   radius = 27.5  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_2_retract.ges_sf_rod  &
   color = RED  &
   name_visibility = off
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_2_retract.josrev_lta_uta_joint  &
   adams_id = 4  &
   i_marker_name = .template_2_retract.ges_lower_torque_arm.jxs_joint_i_8  &
   j_marker_name = .template_2_retract.ges_upper_torque_arm.jxs_joint_j_8
!
constraint attributes  &
   constraint_name = .template_2_retract.josrev_lta_uta_joint  &
   visibility = on  &
   size_of_icons = 50.8
!
constraint create joint spherical  &
   joint_name = .template_2_retract.jossph_lta_lc_joint  &
   adams_id = 5  &
   i_marker_name = .template_2_retract.ges_lower_torque_arm.jxs_joint_i_9  &
   j_marker_name = .template_2_retract.ges_lower_cylinder.jxs_joint_j_9
!
constraint attributes  &
   constraint_name = .template_2_retract.jossph_lta_lc_joint  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_2_retract.josrev_uta_uc_joint  &
   adams_id = 6  &
   i_marker_name = .template_2_retract.ges_upper_torque_arm.jxs_joint_i_10  &
   j_marker_name = .template_2_retract.ges_collar.jxs_joint_j_10
!
constraint attributes  &
   constraint_name = .template_2_retract.josrev_uta_uc_joint  &
   visibility = on
!
constraint create joint fixed  &
   joint_name = .template_2_retract.joscyl_lc_uc_joint  &
   adams_id = 7  &
   i_marker_name = .template_2_retract.ges_lower_cylinder.jxs_joint_i_11  &
   j_marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_j_11
!
constraint attributes  &
   constraint_name = .template_2_retract.joscyl_lc_uc_joint  &
   visibility = on
!
constraint create joint spherical  &
   joint_name = .template_2_retract.jossph_rd_uc  &
   adams_id = 1  &
   i_marker_name = .template_2_retract.ges_upper_cylinder.MARKER_4  &
   j_marker_name = .template_2_retract.ges_sf_rod.MARKER_5
!
constraint attributes  &
   constraint_name = .template_2_retract.jossph_rd_uc  &
   visibility = on  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_2_retract.josrev_uc_sf_joint  &
   adams_id = 8  &
   i_marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_i_15  &
   j_marker_name = .template_2_retract.ges_subframe.jxs_joint_j_15
!
constraint attributes  &
   constraint_name = .template_2_retract.josrev_uc_sf_joint  &
   visibility = on
!
constraint create joint fixed  &
   joint_name = .template_2_retract.JOINT_14  &
   adams_id = 14  &
   i_marker_name = .template_2_retract.ges_subframe.MARKER_160  &
   j_marker_name = .template_2_retract.ground.MARKER_161
!
constraint attributes  &
   constraint_name = .template_2_retract.JOINT_14  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_2_retract.joscyl_db_sf  &
   adams_id = 11  &
   i_marker_name = .template_2_retract.ges_sf_actuator.jxs_joint_i_14  &
   j_marker_name = .template_2_retract.ges_subframe.jxs_joint_j_14
!
constraint attributes  &
   constraint_name = .template_2_retract.joscyl_db_sf  &
   visibility = on
!
constraint create joint revolute  &
   joint_name = .template_2_retract.josrev_collar_uc_joint  &
   adams_id = 12  &
   i_marker_name = .template_2_retract.ges_collar.jxs_joint_i_1  &
   j_marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_j_1
!
constraint attributes  &
   constraint_name = .template_2_retract.josrev_collar_uc_joint  &
   visibility = on
!
constraint create joint cylindrical  &
   joint_name = .template_2_retract.joscly_ac_rd  &
   adams_id = 13  &
   i_marker_name = .template_2_retract.ges_sf_rod.MARKER_84  &
   j_marker_name = .template_2_retract.ges_sf_actuator.MARKER_85
!
constraint attributes  &
   constraint_name = .template_2_retract.joscly_ac_rd  &
   visibility = on  &
   name_visibility = off
!
!----------------------------------- Forces -----------------------------------!
!
!
force create direct general_force  &
   general_force_name = .template_2_retract.NLG_aeroforce  &
   adams_id = 3  &
   i_marker_name = .template_2_retract.ges_upper_cylinder.MARKER_162  &
   j_floating_marker_name =   &
                            .template_2_retract.ges_lower_cylinder.FMARKER_164  &
   ref_marker_name = .template_2_retract.ges_lower_cylinder.MARKER_163  &
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
   sim_script_name = .template_2_retract.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 number_of_steps=1200 model_name=.gcmb2_retract"
!
simulation script create  &
   sim_script_name = .template_2_retract.Last_Sim_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
geometry create shape force  &
   force_name = .template_2_retract.GFORCE_3_force_graphic_1  &
   adams_id = 43  &
   force_element_name = .template_2_retract.NLG_aeroforce  &
   applied_at_marker_name =   &
                            .template_2_retract.ges_upper_cylinder.MARKER_162
!
!---------------------------------- Motions -----------------------------------!
!
!
constraint create motion_generator  &
   motion_name = .template_2_retract.MOTION_disp  &
   adams_id = 2  &
   type_of_freedom = translational  &
   joint_name = .template_2_retract.joscly_ac_rd  &
   function = ""
!
constraint attributes  &
   constraint_name = .template_2_retract.MOTION_disp  &
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
   force_name = .template_2_retract.gravity  &
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
   measure_name = .template_2_retract.NLG_sf_angle  &
   from_first = yes  &
   object = .template_2_retract.josrev_uc_sf_joint  &
   characteristic = ax_ay_az_projection_angles  &
   component = z_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_2_retract.NLG_sf_angle  &
   color = WHITE
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_2_retract.AIR_VELOCITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 55.0
!
variable create  &
   variable_name = .template_2_retract.AIR_DENSITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_2_retract.NLG_DRAG_CORFF  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.7
!
variable create  &
   variable_name = .template_2_retract.NLG_PROJ_AREA  &
   units = "area"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.3077
!
variable create  &
   variable_name = .template_2_retract.NLG_RETRACT_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 4.5
!
variable create  &
   variable_name = .template_2_retract.NLG_UP_HOLD_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_2_retract.NLG_EXTEND_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
variable create  &
   variable_name = .template_2_retract.NLG_ACTUATOR_STROKE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 635.0
!
!---------------------------- Function definitions ----------------------------!
!
!
constraint modify motion_generator  &
   motion_name = .template_2_retract.MOTION_disp  &
   function = "-STEP( time , 0 , 0 , .template_2_retract.NLG_RETRACT_TIME , .template_2_retract.NLG_ACTUATOR_STROKE )-STEP( time , .template_2_retract.NLG_RETRACT_TIME+.template_2_retract.NLG_UP_HOLD_TIME , 0 ,  .template_2_retract.NLG_RETRACT_TIME+.template_2_retract.NLG_UP_HOLD_TIME+.template_2_retract.NLG_EXTEND_TIME , -.template_2_retract.NLG_ACTUATOR_STROKE )"
!
force modify direct general_force  &
   general_force_name = .template_2_retract.NLG_aeroforce  &
   x_force_function = ".template_2_retract.NLG_DRAG_CORFF*abs(IF( .template_2_retract.NLG_sf_angle-60 : COS( 1.225*.template_2_retract.NLG_sf_angle*pi/180 ) , COS( 1.225*.template_2_retract.NLG_sf_angle*pi/180 ) , COS( .template_2_retract.NLG_sf_angle*pi/180 ) ))*.template_2_retract.NLG_PROJ_AREA*cos(.template_2_retract.NLG_sf_angle*pi/180)*0.5*.template_2_retract.AIR_DENSITY*.template_2_retract.AIR_VELOCITY*abs(.template_2_retract.AIR_VELOCITY)*cos(.template_2_retract.NLG_sf_angle*pi/180) "  &
   y_force_function = "0"  &
   z_force_function = ".template_2_retract.NLG_DRAG_CORFF*abs(IF( .template_2_retract.NLG_sf_angle-60 : COS( 1.225*.template_2_retract.NLG_sf_angle*pi/180 ) , COS( 1.225*.template_2_retract.NLG_sf_angle*pi/180 ) , COS( .template_2_retract.NLG_sf_angle*pi/180 ) ))*.template_2_retract.NLG_PROJ_AREA*cos(.template_2_retract.NLG_sf_angle*pi/180)*0.5*.template_2_retract.AIR_DENSITY*.template_2_retract.AIR_VELOCITY*abs(.template_2_retract.AIR_VELOCITY)*sin(.template_2_retract.NLG_sf_angle*pi/180) "  &
   x_torque_function = "0"  &
   y_torque_function = "-1*CUBSPL( .template_2_retract.NLG_sf_angle, 0 , .template_2_retract.SPLINE_angle_aeroforce, 0 )"  &
   z_torque_function = "0"
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_2_retract.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_2_retract.ground.hps_uc_bot, .template_2_retract.ground.hps_uc_top, 0.11 * DM(.template_2_retract.ground.hps_uc_bot, .template_2_retract.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_uc_bot, .template_2_retract.ground.hps_uc_top, "Z"))
!
material modify  &
   material_name = .template_2_retract.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_2_retract.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_2_retract.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_2_retract.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .template_2_retract.ges_sf_actuator.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_db_sf_atch, .template_2_retract.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .template_2_retract.ges_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_sf_actuator.jxs_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_subframe.jxs_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_subframe.jxs_joint_j_14))  &
   relative_to = .template_2_retract.ges_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_sf_actuator.gralin_dragbrace_geom  &
   length = (DM(.template_2_retract.ground.hps_db_sf_atch, .template_2_retract.ground.hps_db_uc_atch) - 50)
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_cylinder.MARKER_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_sf_rod.PT3))  &
   relative_to = .template_2_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_uc_top, .template_2_retract.ground.hps_uc_bot, "Z"))  &
   relative_to = .template_2_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_uc_sf_atch_l, .template_2_retract.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_2_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_uc_sf_atch_r, .template_2_retract.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_2_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_i_15  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_subframe.jxs_joint_j_15))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_subframe.jxs_joint_j_15))  &
   relative_to = .template_2_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_uc_bot, .template_2_retract.ground.hps_uc_top, "Z"))  &
   relative_to = .template_2_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_cylinder.MARKER_162  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_aeroforceN))  &
   relative_to = .template_2_retract.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.template_2_retract.ground.hps_uc_top, .template_2_retract.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.template_2_retract.ground.hps_uc_sf_atch_l, .template_2_retract.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.template_2_retract.ground.hps_uc_sf_atch_r, .template_2_retract.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_lc_top, .template_2_retract.ground.hps_lc_bot, "Z"))  &
   relative_to = .template_2_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_cylinder.jxs_joint_j_9  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_2_retract.ground.origo))  &
   relative_to = .template_2_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .template_2_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_cylinder.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hpr_wheel_center, .template_2_retract.ground.hpl_wheel_center, "Z"))  &
   relative_to = .template_2_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_cylinder.MARKER_163  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_aeroforceN))  &
   relative_to = .template_2_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_cylinder.MARKER_165  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hpl_ob_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hpl_ob_axle, .template_2_retract.ground.hpl_wheel_center, "Z"))  &
   relative_to = .template_2_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_cylinder.MARKER_166  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hpr_ob_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hpr_ob_axle, .template_2_retract.ground.hpr_wheel_center, "Z"))  &
   relative_to = .template_2_retract.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_lower_cylinder.gralin_geom1  &
   length = (DM(.template_2_retract.ground.hps_lc_top, .template_2_retract.ground.hps_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_lower_cylinder.gralin_geom2  &
   length = (DM(.template_2_retract.ground.hpr_wheel_center, .template_2_retract.ground.hpl_wheel_center))
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_torque_arm.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_uta_uc_atch, .template_2_retract.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_2_retract.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_torque_arm.jxs_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract.ground.hps_lta_uta_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_2_retract.ground.origo))  &
   relative_to = .template_2_retract.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_upper_torque_arm.jxs_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_collar.jxs_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_collar.jxs_joint_j_10))  &
   relative_to = .template_2_retract.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   length = (DM(.template_2_retract.ground.hps_uta_uc_atch, .template_2_retract.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_torque_arm.jxs_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_upper_torque_arm.jxs_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_upper_torque_arm.jxs_joint_j_8))  &
   relative_to = .template_2_retract.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_torque_arm.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_lta_lc_atch, .template_2_retract.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_2_retract.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_lower_torque_arm.jxs_joint_i_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_lower_cylinder.jxs_joint_j_9))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_lower_cylinder.jxs_joint_j_9))  &
   relative_to = .template_2_retract.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   length = (DM(.template_2_retract.ground.hps_lta_lc_atch, .template_2_retract.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_2_retract.ges_subframe.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_subframe.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_subframe))  &
   relative_to = .template_2_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_subframe.graout_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_uc_sf_atch_r))  &
   relative_to = .template_2_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_subframe.graout_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_uc_sf_atch_l))  &
   relative_to = .template_2_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_subframe.graout_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_db_sf_atch))  &
   relative_to = .template_2_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_subframe.jxs_joint_j_15  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract.ground.cfs_uc_sf_atch_mid))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_2_retract.ground.cfs_uc_sf_atch_mid, "Z+Z"), .template_2_retract.ges_subframe))  &
   relative_to = .template_2_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_subframe.jxs_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_2_retract.ground.origo))  &
   relative_to = .template_2_retract.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_collar.jxs_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_2_retract.ground.origo))  &
   relative_to = .template_2_retract.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_collar.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ground.hps_uc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ground.hps_uc_bot, .template_2_retract.ground.cfs_collar_top, "Z"))  &
   relative_to = .template_2_retract.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_2_retract.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_collar.gralin_collar  &
   length = (DM(.template_2_retract.ground.hps_uc_bot, .template_2_retract.ground.cfs_collar_top))
!
marker modify  &
   marker_name = .template_2_retract.ges_sf_rod.MARKER_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract.ges_sf_rod.PT3))  &
   relative_to = .template_2_retract.ges_sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
marker modify  &
   marker_name = .template_2_retract.ges_sf_rod.gralin_25  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}, .template_2_retract.ground.hps_rod_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract.ges_sf_rod.PT3, .template_2_retract.ground.hps_db_sf_atch, "Z"))  &
   relative_to = .template_2_retract.ges_sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract.ges_sf_rod.CYLINDER_30  &
   length = (DM(.template_2_retract.ground.hps_rod_bot, .template_2_retract.ground.hps_rod_top))  &
   radius = (27.5mm)
!
geometry modify shape force  &
   force_name = .template_2_retract.GFORCE_3_force_graphic_1  &
   applied_at_marker_name = (.template_2_retract.NLG_aeroforce.i)
!
model display  &
   model_name = template_2_retract

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
   marker_name = .turn.ground.origo1  &
   adams_id = 287  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.origo1  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfs_uc_sf_atch_mid  &
   adams_id = 289  &
   location = 6.31444, 0.0, 1.69164  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfs_uc_sf_atch_mid  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfs_subframe_to_body_point  &
   adams_id = 290  &
   location = 6.70433, 0.0, 1.66878  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
marker attributes  &
   marker_name = .turn.ground.cfs_subframe_to_body_point  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfl_spin_axis1  &
   adams_id = 292  &
   location = 6.229096, -0.20955, 0.308  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfl_spin_axis1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfr_spin_axis1  &
   adams_id = 293  &
   location = 6.229096, 0.20955, 0.308  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .turn.ground.cfr_spin_axis1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfs_wheel_centers_midpoint  &
   adams_id = 294  &
   location = 6.229096, 0.0, 0.508  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfs_wheel_centers_midpoint  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfs_nlg_axle_lowpoint  &
   adams_id = 295  &
   location = 6.229096, 0.0, 0.4826  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfs_nlg_axle_lowpoint  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ground.cfs_collar_top  &
   adams_id = 296  &
   location = 6.1976, 0.0, 0.856996  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ground.cfs_collar_top  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
! ****** Points for current part ******
!
point create  &
   point_name = .turn.ground.hps_uc_sf_atch_l  &
   location = 6.31444, -0.34036, 1.69164
!
point attributes  &
   point_name = .turn.ground.hps_uc_sf_atch_l  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_uc_sf_atch_r  &
   location = 6.31444, 0.34036, 1.69164
!
point attributes  &
   point_name = .turn.ground.hps_uc_sf_atch_r  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_lc_bot  &
   location = 6.1976, 0.0, 0.308
!
point attributes  &
   point_name = .turn.ground.hps_lc_bot  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_uc_top  &
   location = 6.1976, 0.0, 1.6256
!
point attributes  &
   point_name = .turn.ground.hps_uc_top  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_uta_uc_atch  &
   location = 6.3246, 0.0, 0.8382
!
point attributes  &
   point_name = .turn.ground.hps_uta_uc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_lta_lc_atch  &
   location = 6.2992, 0.0, 0.3334
!
point attributes  &
   point_name = .turn.ground.hps_lta_lc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_lta_uta_atch  &
   location = 6.6548, 0.0, 0.6112
!
point attributes  &
   point_name = .turn.ground.hps_lta_uta_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_uc_geompt  &
   location = 6.1976, 0.0, 1.4732
!
point attributes  &
   point_name = .turn.ground.hps_uc_geompt  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_uc_bot  &
   location = 6.1976, 0.0, 0.762
!
point attributes  &
   point_name = .turn.ground.hps_uc_bot  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_lc_top  &
   location = 6.1976, 0.0, 1.197
!
point attributes  &
   point_name = .turn.ground.hps_lc_top  &
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
point create  &
   point_name = .turn.ground.hps_lb_uc_atch  &
   location = 6.021578, 0.0, 0.79502
!
point attributes  &
   point_name = .turn.ground.hps_lb_uc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_wheel_center1  &
   location = 6.229096, -0.20955, 0.308
!
point attributes  &
   point_name = .turn.ground.hpl_wheel_center1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_wheel_center1  &
   location = 6.229096, 0.20955, 0.308
!
point attributes  &
   point_name = .turn.ground.hpr_wheel_center1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpl_ob_axle1  &
   location = 6.229096, -0.28575, 0.308
!
point attributes  &
   point_name = .turn.ground.hpl_ob_axle1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hpr_ob_axle1  &
   location = 6.229096, 0.28575, 0.308
!
point attributes  &
   point_name = .turn.ground.hpr_ob_axle1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_nlg_axle_lowpoint  &
   location = 6.229096, 0.0, 0.4826
!
point attributes  &
   point_name = .turn.ground.hps_nlg_axle_lowpoint  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hsg_1  &
   location = 6.1976, 0.2, 0.8
!
point create  &
   point_name = .turn.ground.hsg_2  &
   location = 5.7328083759, -0.1123599625, 0.8
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .turn.ground  &
   size_of_icons = 5.0E-02
!
!----------------------------- ges_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ges_upper_cylinder  &
   adams_id = 34  &
   location = 6.1976, 0.0, 1.1938  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ges_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.MARKER_481  &
   adams_id = 481  &
   location = 0.0, 0.0, 0.384302  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.cm  &
   adams_id = 306  &
   location = -3.3167643494E-03, 0.0, -1.3382423116E-02  &
   orientation = 90.0d, 2.0673379194d, 270.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.cm  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.inertia_frame  &
   adams_id = 307  &
   location = -3.3167643494E-03, 0.0, -1.3382423116E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.gralin_2  &
   adams_id = 308  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.gralin_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.gralin_3  &
   adams_id = 309  &
   location = -0.11684, -0.34036, -0.49784  &
   orientation = 161.0534953105d, 58.7414044414d, 213.4869581747d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.gralin_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.gralin_4  &
   adams_id = 310  &
   location = -0.11684, 0.34036, -0.49784  &
   orientation = 18.9465046895d, 58.7414044414d, 326.5130418253d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.gralin_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.jxs_joint_j_11  &
   adams_id = 311  &
   location = 0.0, 0.0, 0.1143  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.jxs_joint_j_11  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.ues_spring_j_1  &
   adams_id = 314  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.ues_spring_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.ues_damper_j_1  &
   adams_id = 315  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.ues_damper_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.ues_stopper_j_1  &
   adams_id = 316  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.ues_stopper_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.jxs_joint_j_1  &
   adams_id = 317  &
   location = 0.0, 0.0, 0.336804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.jxs_joint_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.ues_actuator_j_1  &
   adams_id = 318  &
   location = 0.0, 0.0, 0.336804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.ues_actuator_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.ues_actuator_j_4  &
   adams_id = 319  &
   location = 0.0, 0.0, 0.336804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.ues_actuator_j_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.MARKER_2  &
   adams_id = 2  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.MARKER_2  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_cylinder.MARKER_116  &
   adams_id = 324  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_cylinder.MARKER_116  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ges_upper_cylinder  &
   mass = 82.2524279101  &
   center_of_mass_marker = .turn.ges_upper_cylinder.cm  &
   inertia_marker = .turn.ges_upper_cylinder.inertia_frame  &
   ixx = 2.7759040478  &
   iyy = 2.6163591859  &
   izz = 0.8272904746  &
   ixy = 0.0  &
   izx = 7.0431892224E-02  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 86  &
   center_marker = .turn.ges_upper_cylinder.gralin_2  &
   angle_extent = 360.0  &
   length = 0.8636  &
   radius = 0.127  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .turn.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 87  &
   center_marker = .turn.ges_upper_cylinder.gralin_3  &
   angle_extent = 360.0  &
   length = 0.4209662086  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .turn.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 88  &
   center_marker = .turn.ges_upper_cylinder.gralin_4  &
   angle_extent = 360.0  &
   length = 0.4209662086  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .turn.ges_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ges_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ges_lower_cylinder  &
   adams_id = 35  &
   location = 6.1976, 0.0, 0.9525  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ges_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.MARKER_378  &
   adams_id = 378  &
   location = -0.1016, 0.0, 0.6191  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.MARKER_378  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.MARKER_1  &
   adams_id = 325  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.MARKER_1  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.cm  &
   adams_id = 326  &
   location = -2.4871874502E-03, 0.0, 3.4740392449E-02  &
   orientation = 270.0d, 0.8125241803d, 90.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.inertia_frame  &
   adams_id = 327  &
   location = -2.4871874502E-03, 0.0, 3.4740392449E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.gralin_5  &
   adams_id = 328  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.gralin_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.jxs_joint_i_11  &
   adams_id = 330  &
   location = 0.0, 0.0, -0.127  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.jxs_joint_i_11  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.gralin_7  &
   adams_id = 331  &
   location = -3.1496E-02, 0.20955, 0.6445  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.gralin_7  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.ues_spring_i_1  &
   adams_id = 332  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.ues_spring_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.ues_damper_i_1  &
   adams_id = 51  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.ues_damper_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.ues_stopper_i_1  &
   adams_id = 333  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.ues_stopper_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.coomarker_2  &
   adams_id = 334  &
   location = -3.1496E-02, 0.0, 0.4445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.coomarker_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.coomarker_3  &
   adams_id = 335  &
   location = -3.1496E-02, 0.0, 0.4699  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.coomarker_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.MARKER_3  &
   adams_id = 336  &
   location = -3.1496E-02, -0.20955, 0.6445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.MARKER_3  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.MARKER_4  &
   adams_id = 337  &
   location = -3.1496E-02, 0.20955, 0.6445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.MARKER_4  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_cylinder.MARKER_115  &
   adams_id = 344  &
   location = 0.0, 0.0, -0.4445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_cylinder.MARKER_115  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ges_lower_cylinder  &
   mass = 84.8838172052  &
   center_of_mass_marker = .turn.ges_lower_cylinder.cm  &
   inertia_marker = .turn.ges_lower_cylinder.inertia_frame  &
   ixx = 6.8342355549  &
   iyy = 6.4494598026  &
   izz = 0.8036506432  &
   ixy = 0.0  &
   izx = -8.5544003848E-02  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ges_lower_cylinder.gralin_geom1  &
   adams_id = 89  &
   center_marker = .turn.ges_lower_cylinder.gralin_5  &
   angle_extent = 360.0  &
   length = 0.889  &
   radius = 0.1016  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ges_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .turn.ges_lower_cylinder.gralin_geom2  &
   adams_id = 90  &
   center_marker = .turn.ges_lower_cylinder.gralin_7  &
   angle_extent = 360.0  &
   length = 0.4191  &
   radius = 3.048E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ges_lower_cylinder.gralin_geom2  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .turn.ges_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ges_upper_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ges_upper_torque_arm  &
   adams_id = 36  &
   location = 6.4897, 0.0, 0.7747  &
   orientation = 90.0d, 111.0375110254d, 270.0d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ges_upper_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ges_upper_torque_arm.cm  &
   adams_id = 345  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_torque_arm.inertia_frame  &
   adams_id = 346  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_torque_arm.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_torque_arm.gralin_9  &
   adams_id = 347  &
   location = 0.0, 0.0, -0.1768905311  &
   orientation = 90.0d, 13.4695391009d, 270.0d
!
marker attributes  &
   marker_name = .turn.ges_upper_torque_arm.gralin_9  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_torque_arm.jxs_joint_j_8  &
   adams_id = 348  &
   location = 9.333456062E-02, 0.0, 0.2127884391  &
   orientation = 0.0d, 90.0d, 111.0375110254d
!
marker attributes  &
   marker_name = .turn.ges_upper_torque_arm.jxs_joint_j_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_upper_torque_arm.jxs_joint_i_10  &
   adams_id = 349  &
   location = 0.0, 0.0, -0.1768905311  &
   orientation = 0.0d, 90.0d, 111.0375110254d
!
marker attributes  &
   marker_name = .turn.ges_upper_torque_arm.jxs_joint_i_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ges_upper_torque_arm  &
   mass = 0.3898630024  &
   center_of_mass_marker = .turn.ges_upper_torque_arm.cm  &
   inertia_marker = .turn.ges_upper_torque_arm.inertia_frame  &
   ixx = 2.5774839559E-03  &
   iyy = 2.5774839559E-03  &
   izz = 3.1440501824E-05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   adams_id = 91  &
   center_marker = .turn.ges_upper_torque_arm.gralin_9  &
   angle_extent = 360.0  &
   length = 0.4007006863  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   color = GREEN
!
part attributes  &
   part_name = .turn.ges_upper_torque_arm  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ges_lower_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ges_lower_torque_arm  &
   adams_id = 37  &
   location = 6.477, 0.0, 0.6223  &
   orientation = 90.0d, 63.4349488229d, 270.0d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ges_lower_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ges_lower_torque_arm.MARKER_379  &
   adams_id = 379  &
   location = 0.1788854382, 0.0, -0.2882291623  &
   orientation = 0.0d, 90.0d, 63.4349488229d
!
marker attributes  &
   marker_name = .turn.ges_lower_torque_arm.MARKER_379  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_torque_arm.cm  &
   adams_id = 350  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_torque_arm.inertia_frame  &
   adams_id = 351  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_torque_arm.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_torque_arm.jxs_joint_i_8  &
   adams_id = 352  &
   location = 8.94427191E-02, 0.0, 0.1540650836  &
   orientation = 0.0d, 90.0d, 63.4349488229d
!
marker attributes  &
   marker_name = .turn.ges_lower_torque_arm.jxs_joint_i_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_lower_torque_arm.gralin_10  &
   adams_id = 353  &
   location = 0.1788854382, 0.0, -0.2882291623  &
   orientation = 270.0d, 11.4324305526d, 90.0d
!
marker attributes  &
   marker_name = .turn.ges_lower_torque_arm.gralin_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ges_lower_torque_arm  &
   mass = 0.3898630024  &
   center_of_mass_marker = .turn.ges_lower_torque_arm.cm  &
   inertia_marker = .turn.ges_lower_torque_arm.inertia_frame  &
   ixx = 2.5774839559E-03  &
   iyy = 2.5774839559E-03  &
   izz = 3.1440501824E-05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   adams_id = 92  &
   center_marker = .turn.ges_lower_torque_arm.gralin_10  &
   angle_extent = 360.0  &
   length = 0.4512473823  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   color = MAGENTA
!
part attributes  &
   part_name = .turn.ges_lower_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- ges_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ges_collar  &
   adams_id = 40  &
   location = 6.1976, 0.0, 0.809498  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ges_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ges_collar.MARKER_482  &
   adams_id = 482  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .turn.ges_collar.jxs_joint_j_10  &
   adams_id = 368  &
   location = 0.127, 0.0, 2.8702E-02  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_collar.jxs_joint_j_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_collar.cm  &
   adams_id = 369  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_collar.cm  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_collar.inertia_frame  &
   adams_id = 370  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_collar.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_collar.gralin_24  &
   adams_id = 371  &
   location = 0.0, 0.0, -4.7498E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_collar.gralin_24  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_collar.jxs_joint_i_1  &
   adams_id = 372  &
   location = 0.0, 0.0, 4.7498E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_collar.jxs_joint_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_collar.ues_actuator_i_1  &
   adams_id = 373  &
   location = 0.0, 0.0, 4.7498E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_collar.ues_actuator_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_collar.ues_actuator_i_4  &
   adams_id = 374  &
   location = 0.0, 0.0, 4.7498E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_collar.ues_actuator_i_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ges_collar  &
   mass = 6.4242828175  &
   center_of_mass_marker = .turn.ges_collar.cm  &
   inertia_marker = .turn.ges_collar.inertia_frame  &
   ixx = 8.5080541407E-02  &
   iyy = 8.5080541407E-02  &
   izz = 0.1468542831  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ges_collar.gralin_collar  &
   adams_id = 93  &
   center_marker = .turn.ges_collar.gralin_24  &
   angle_extent = 360.0  &
   length = 9.4996E-02  &
   radius = 0.1397  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ges_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .turn.ges_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .turn.JOINT_51  &
   adams_id = 51  &
   i_marker_name = .turn.ges_lower_cylinder.MARKER_378  &
   j_marker_name = .turn.ges_lower_torque_arm.MARKER_379
!
constraint attributes  &
   constraint_name = .turn.JOINT_51  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint spherical  &
   joint_name = .turn.josrev_lta_uta_joint  &
   adams_id = 39  &
   i_marker_name = .turn.ges_lower_torque_arm.jxs_joint_i_8  &
   j_marker_name = .turn.ges_upper_torque_arm.jxs_joint_j_8
!
constraint attributes  &
   constraint_name = .turn.josrev_lta_uta_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .turn.josrev_uta_uc_joint  &
   adams_id = 41  &
   i_marker_name = .turn.ges_upper_torque_arm.jxs_joint_i_10  &
   j_marker_name = .turn.ges_collar.jxs_joint_j_10
!
constraint attributes  &
   constraint_name = .turn.josrev_uta_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .turn.joscyl_lc_uc_joint  &
   adams_id = 42  &
   i_marker_name = .turn.ges_lower_cylinder.jxs_joint_i_11  &
   j_marker_name = .turn.ges_upper_cylinder.jxs_joint_j_11
!
constraint attributes  &
   constraint_name = .turn.joscyl_lc_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .turn.josrev_collar_uc_joint  &
   adams_id = 48  &
   i_marker_name = .turn.ges_collar.jxs_joint_i_1  &
   j_marker_name = .turn.ges_upper_cylinder.jxs_joint_j_1
!
constraint attributes  &
   constraint_name = .turn.josrev_collar_uc_joint  &
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
   marker_name = .turn.ground.cfl_spin_axis1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpl_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpl_wheel_center1, .turn.ground.hpl_ob_axle1, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfr_spin_axis1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hpr_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_wheel_center1, .turn.ground.hpr_ob_axle1, "Z"))
!
marker modify  &
   marker_name = .turn.ground.cfs_nlg_axle_lowpoint  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hps_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .turn.ground.origo1))
!
marker modify  &
   marker_name = .turn.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hps_uc_bot, .turn.ground.hps_uc_top, 0.11 * DM(.turn.ground.hps_uc_bot, .turn.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_uc_bot, .turn.ground.hps_uc_top, "Z"))
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
   marker_name = .turn.ges_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_uc_top, .turn.ground.hps_uc_bot, "Z"))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_uc_sf_atch_l, .turn.ground.hps_uc_geompt, "Z"))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_uc_sf_atch_r, .turn.ground.hps_uc_geompt, "Z"))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_cylinder.ues_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_uc_top))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_cylinder.ues_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_uc_top))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_cylinder.ues_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_uc_top))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_uc_bot, .turn.ground.hps_uc_top, "Z"))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_cylinder.ues_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_cylinder.ues_actuator_j_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .turn.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.turn.ground.hps_uc_top, .turn.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.turn.ground.hps_uc_sf_atch_l, .turn.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.turn.ground.hps_uc_sf_atch_r, .turn.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.MARKER_378  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_lta_lc_atch))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_lower_cylinder))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_lc_top, .turn.ground.hps_lc_bot, "Z"))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hpr_wheel_center1, .turn.ground.hpl_wheel_center1, "Z"))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.ues_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_lc_top))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.ues_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_lc_top))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.ues_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_lc_top))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.coomarker_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfs_wheel_centers_midpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ground.cfs_wheel_centers_midpoint))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.coomarker_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.cfs_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ground.cfs_nlg_axle_lowpoint))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.MARKER_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpl_wheel_center1))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_cylinder.MARKER_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hpr_wheel_center1))  &
   relative_to = .turn.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ges_lower_cylinder.gralin_geom1  &
   length = (DM(.turn.ground.hps_lc_top, .turn.ground.hps_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ges_lower_cylinder.gralin_geom2  &
   length = (DM(.turn.ground.hpr_wheel_center1, .turn.ground.hpl_wheel_center1))
!
marker modify  &
   marker_name = .turn.ges_upper_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_torque_arm))  &
   relative_to = .turn.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_torque_arm.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_uta_uc_atch, .turn.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .turn.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_torque_arm.jxs_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hps_lta_uta_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .turn.ground.origo1))  &
   relative_to = .turn.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_upper_torque_arm.jxs_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_collar.jxs_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_collar.jxs_joint_j_10))  &
   relative_to = .turn.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   length = (DM(.turn.ground.hps_uta_uc_atch, .turn.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .turn.ges_lower_torque_arm.MARKER_379  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_lta_lc_atch))  &
   relative_to = .turn.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_lower_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_lower_torque_arm))  &
   relative_to = .turn.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_torque_arm.jxs_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_torque_arm.jxs_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_torque_arm.jxs_joint_j_8))  &
   relative_to = .turn.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_lower_torque_arm.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_lta_lc_atch, .turn.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .turn.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   length = (DM(.turn.ground.hps_lta_lc_atch, .turn.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .turn.ges_collar.jxs_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .turn.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .turn.ground.origo1))  &
   relative_to = .turn.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_collar))  &
   relative_to = .turn.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_collar.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_uc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_uc_bot, .turn.ground.cfs_collar_top, "Z"))  &
   relative_to = .turn.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .turn.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_collar.ues_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_collar.jxs_joint_i_1))  &
   relative_to = .turn.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_collar.ues_actuator_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_collar.jxs_joint_i_1))  &
   relative_to = .turn.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ges_collar.gralin_collar  &
   length = (DM(.turn.ground.hps_uc_bot, .turn.ground.cfs_collar_top))
!
model display  &
   model_name = turn

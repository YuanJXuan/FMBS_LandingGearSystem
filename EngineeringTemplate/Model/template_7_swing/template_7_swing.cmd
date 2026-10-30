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
   model_name = template_7_swing  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_7_swing  &
   size_of_icons = 50.8
!
view erase
!
!-------------------------------- Data storage --------------------------------!
!
!
data_element create variable  &
   variable_name = .template_7_swing._cv_solver_variable  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   function = ""
!
data_element attributes  &
   data_element_name = .template_7_swing._cv_solver_variable  &
   visibility = off
!
data_element create array ic_array  &
   array_name = .template_7_swing._cv_array  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   size = 1  &
   numbers = 0.0
!
data_element attributes  &
   data_element_name = .template_7_swing._cv_array  &
   visibility = off
!
data_element create spline  &
   spline_name = .template_7_swing._cv_spline  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   x = 1.0, 2.0, 3.0, 4.0  &
   y = 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0  &
   z = 1.0, 2.0  &
   linear_extrapolate = no
!
data_element attributes  &
   data_element_name = .template_7_swing._cv_spline  &
   visibility = off
!
data_element create spline  &
   spline_name = .template_7_swing.jili  &
   adams_id = 2  &
   x = 0.0, 1.0, 2.0, 3.0, 3.1, 3.2, 4.1, 4.5, 5.0  &
   y = 0.0, 0.0, 0.0, 0.0, -8.3E+04, 0.0, 0.0, 0.0, 0.0  &
   linear_extrapolate = yes  &
   x_units = "time"  &
   y_units = "volume"
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .template_7_swing.steel  &
   adams_id = 2  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_7_swing.aluminum  &
   adams_id = 1  &
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
   default_coordinate_system = .template_7_swing.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.ground.origo  &
   adams_id = 5  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground.origo  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ground._cv_marker  &
   adams_id = 6  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground._cv_marker  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ground.cfs_uc_sf_atch_mid  &
   adams_id = 7  &
   location = 6314.44, 0.0, 1691.64  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground.cfs_uc_sf_atch_mid  &
   color = MAIZE
!
marker create  &
   marker_name = .template_7_swing.ground.cfs_subframe_to_body_point  &
   adams_id = 8  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
marker attributes  &
   marker_name = .template_7_swing.ground.cfs_subframe_to_body_point  &
   color = MAIZE
!
marker create  &
   marker_name = .template_7_swing.ground.mts_mount_j_2  &
   adams_id = 9  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground.mts_mount_j_2  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ground.cfl_spin_axis  &
   adams_id = 10  &
   location = 6229.096, -209.55, 508.0  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground.cfl_spin_axis  &
   color = MAIZE
!
marker create  &
   marker_name = .template_7_swing.ground.cfr_spin_axis  &
   adams_id = 11  &
   location = 6229.096, 209.55, 508.0  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground.cfr_spin_axis  &
   color = MAIZE
!
marker create  &
   marker_name = .template_7_swing.ground.cfs_wheel_centers_midpoint  &
   adams_id = 12  &
   location = 6229.096, 0.0, 508.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground.cfs_wheel_centers_midpoint  &
   color = MAIZE
!
marker create  &
   marker_name = .template_7_swing.ground.cfs_nlg_axle_lowpoint  &
   adams_id = 13  &
   location = 6229.096, 0.0, 482.6  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground.cfs_nlg_axle_lowpoint  &
   color = MAIZE
!
marker create  &
   marker_name = .template_7_swing.ground.cfs_collar_top  &
   adams_id = 14  &
   location = 6197.6, 0.0, 856.996  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground.cfs_collar_top  &
   color = MAIZE
!
marker create  &
   marker_name = .template_7_swing.ground.MARKER_174  &
   adams_id = 174  &
   location = 6197.6, 0.0, 1825.6  &
   orientation = 90.0d, 90.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ground.lm_ref_1  &
   adams_id = 89  &
   location = 0.0, 0.0, 327.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ground.lm_ref_1  &
   visibility = off
!
marker create  &
   marker_name = .template_7_swing.ground.MARKER_178  &
   adams_id = 178  &
   location = 6197.6, 0.0, 1825.6  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_7_swing.ground.zdt1  &
   adams_id = 171  &
   location = 5918.7250255242, 12.5840225297, 800.0  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_7_swing.ground.zdt2  &
   adams_id = 172  &
   location = 5779.2875382863, -81.1239662055, 800.0  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_7_swing.ground.lt1_tire_jf_1  &
   adams_id = 90
!
floating_marker create  &
   floating_marker_name = .template_7_swing.ground.lt_l_tire_jf_1  &
   adams_id = 135
!
floating_marker create  &
   floating_marker_name = .template_7_swing.ground.lt_r_tire_jf_1  &
   adams_id = 91
!
floating_marker create  &
   floating_marker_name = .template_7_swing.ground.lt_r_tire_jf_2  &
   adams_id = 136
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_7_swing.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_7_swing.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_7_swing.ground.hps_uc_sf_atch_l  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_7_swing.ground.hps_uc_sf_atch_r  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_7_swing.ground.hps_lc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_7_swing.ground.hps_uc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_7_swing.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_uta_uc_atch  &
   location = 6324.6, 0.0, 838.2
!
point attributes  &
   point_name = .template_7_swing.ground.hps_uta_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_lta_lc_atch  &
   location = 6299.2, 0.0, 533.4
!
point attributes  &
   point_name = .template_7_swing.ground.hps_lta_lc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_lta_uta_atch  &
   location = 6654.8, 0.0, 711.2
!
point attributes  &
   point_name = .template_7_swing.ground.hps_lta_uta_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_7_swing.ground.hps_uc_geompt  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_7_swing.ground.hps_uc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_7_swing.ground.hps_lc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_origin_reference  &
   location = 0.0, 0.0, 0.0
!
point attributes  &
   point_name = .template_7_swing.ground.hps_origin_reference  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_7_swing.ground.hps_lb_uc_atch  &
   location = 6021.578, 0.0, 795.02
!
point create  &
   point_name = .template_7_swing.ground.hpl_wheel_center  &
   location = 6229.096, -209.55, 508.0
!
point create  &
   point_name = .template_7_swing.ground.hpr_wheel_center  &
   location = 6229.096, 209.55, 508.0
!
point create  &
   point_name = .template_7_swing.ground.hpl_ob_axle  &
   location = 6229.096, -285.75, 508.0
!
point create  &
   point_name = .template_7_swing.ground.hpr_ob_axle  &
   location = 6229.096, 285.75, 508.0
!
point create  &
   point_name = .template_7_swing.ground.hps_nlg_axle_lowpoint  &
   location = 6229.096, 0.0, 482.6
!
point create  &
   point_name = .template_7_swing.ground.hsg_1  &
   location = 6197.6, 200.0, 800.0
!
point create  &
   point_name = .template_7_swing.ground.hsg_2  &
   location = 5732.8083758737, -112.3599624505, 800.0
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_7_swing.ground  &
   size_of_icons = 50.8
!
!------------------------------------ hsg -------------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.hsg  &
   adams_id = 11  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.hsg  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.hsg
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.hsg.gralin_73  &
   adams_id = 73  &
   location = 6197.6, 200.0, 800.0  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_7_swing.hsg.cm  &
   adams_id = 83  &
   location = 5965.2041879368, 43.8200187748, 800.0  &
   orientation = 303.9027984031d, 90.0d, 86.0678640598d
!
marker create  &
   marker_name = .template_7_swing.hsg.MARKER_76  &
   adams_id = 76  &
   location = 6197.6, 200.0, 800.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.hsg.MARKER_85  &
   adams_id = 85  &
   location = 5849.0062819053, -34.2699718379, 800.0  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_7_swing.hsg.MARKER_81  &
   adams_id = 81  &
   location = 5965.2041879368, 43.8200187747, 800.0  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_7_swing.hsg.MARKER_82  &
   adams_id = 82  &
   location = 5965.2041879368, 43.8200187747, 800.0  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.hsg  &
   mass = 0.0  &
   center_of_mass_marker = .template_7_swing.hsg.cm  &
   ixx = 0.0  &
   iyy = 0.0  &
   izz = 0.0  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.hsg.CYLINDER_50  &
   adams_id = 50  &
   center_marker = .template_7_swing.hsg.gralin_73  &
   angle_extent = 360.0  &
   length = 560.0  &
   radius = 15.084427744  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_7_swing.hsg  &
   color = GREEN  &
   name_visibility = off
!
!---------------------------------- _cv_part ----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing._cv_part  &
   adams_id = 2  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing._cv_part  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing._cv_part
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing._cv_part.marker  &
   adams_id = 15  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing._cv_part.marker  &
   name_visibility = off  &
   size_of_icons = 50.8
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing._cv_part  &
   mass = 0.0  &
   center_of_mass_marker = .template_7_swing._cv_part.marker  &
   ixx = 0.0  &
   iyy = 0.0  &
   izz = 0.0  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
part attributes  &
   part_name = .template_7_swing._cv_part  &
   name_visibility = off  &
   size_of_icons = 50.8
!
!------------------------------- ges_dragbrace --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.ges_dragbrace  &
   adams_id = 3  &
   location = 6967.855, 0.0, 1319.53  &
   orientation = 270.0d, 120.4532239091d, 90.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_dragbrace  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ges_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.ges_dragbrace.cm  &
   adams_id = 16  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_dragbrace.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_dragbrace.inertia_frame  &
   adams_id = 17  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_dragbrace.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_dragbrace.gralin_1  &
   adams_id = 18  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_dragbrace.gralin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_dragbrace.jxs_joint_i_12  &
   adams_id = 19  &
   location = 4.5791148651E-10, 0.0, 598.873681109  &
   orientation = 90.0d, 120.4532239091d, 270.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_dragbrace.jxs_joint_i_12  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_dragbrace.jxs_joint_i_14  &
   adams_id = 20  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 0.0d, 90.0d, 239.5467760909d
!
marker attributes  &
   marker_name = .template_7_swing.ges_dragbrace.jxs_joint_i_14  &
   visibility = off  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.ges_dragbrace  &
   mass = 27.373  &
   center_of_mass_marker = .template_7_swing.ges_dragbrace.cm  &
   inertia_marker = .template_7_swing.ges_dragbrace.inertia_frame  &
   ixx = 3.481E+06  &
   iyy = 3.481E+06  &
   izz = 3.5E+04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.ges_dragbrace.gralin_dragbrace_geom  &
   adams_id = 40  &
   center_marker = .template_7_swing.ges_dragbrace.gralin_1  &
   angle_extent = 360.0  &
   length = 1197.7473622179  &
   radius = 50.8  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_dragbrace.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .template_7_swing.ges_dragbrace  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.ges_upper_cylinder  &
   adams_id = 4  &
   location = 6197.6, 0.0, 1193.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_upper_cylinder  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ges_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.cm  &
   adams_id = 21  &
   location = -3.3167643494, 0.0, -13.3824231157  &
   orientation = 90.0d, 2.0673379194d, 270.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.cm  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.inertia_frame  &
   adams_id = 22  &
   location = -3.3167643494, 0.0, -13.3824231157  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.gralin_2  &
   adams_id = 23  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.gralin_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.gralin_3  &
   adams_id = 24  &
   location = -116.84, -340.36, -497.84  &
   orientation = 161.0534953105d, 58.7414044414d, 213.4869581747d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.gralin_3  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.gralin_4  &
   adams_id = 25  &
   location = -116.84, 340.36, -497.84  &
   orientation = 18.9465046895d, 58.7414044414d, 326.5130418253d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.gralin_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_11  &
   adams_id = 26  &
   location = 0.0, 0.0, 114.3  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_11  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_12  &
   adams_id = 27  &
   location = -254.0, 0.0, 177.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_12  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_i_15  &
   adams_id = 28  &
   location = -116.84, 0.0, -497.84  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_i_15  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_spring_j_1  &
   adams_id = 29  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_spring_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_damper_j_1  &
   adams_id = 30  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_damper_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_stopper_j_1  &
   adams_id = 31  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_stopper_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_1  &
   adams_id = 32  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_1  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_actuator_j_1  &
   adams_id = 33  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_actuator_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_actuator_j_4  &
   adams_id = 34  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_actuator_j_4  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_77  &
   adams_id = 77  &
   location = 278.8749744758, 12.5840225297, 393.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_119  &
   adams_id = 119  &
   location = 0.0, 0.0, -631.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_165  &
   adams_id = 165  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_123  &
   adams_id = 123  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_124  &
   adams_id = 124  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_126  &
   adams_id = 126  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_163  &
   adams_id = 163  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.ges_upper_cylinder  &
   mass = 82.252  &
   center_of_mass_marker = .template_7_swing.ges_upper_cylinder.cm  &
   inertia_marker = .template_7_swing.ges_upper_cylinder.inertia_frame  &
   ixx = 2.776E+06  &
   iyy = 2.616E+06  &
   izz = 8.27E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 41  &
   center_marker = .template_7_swing.ges_upper_cylinder.gralin_2  &
   angle_extent = 360.0  &
   length = 863.6  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 42  &
   center_marker = .template_7_swing.ges_upper_cylinder.gralin_3  &
   angle_extent = 360.0  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 43  &
   center_marker = .template_7_swing.ges_upper_cylinder.gralin_4  &
   angle_extent = 360.0  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_7_swing.ges_upper_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.ges_lower_cylinder  &
   adams_id = 5  &
   location = 6197.6, 0.0, 952.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_lower_cylinder  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ges_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.cm  &
   adams_id = 35  &
   location = -2.4871874502, 0.0, 34.7403924495  &
   orientation = 270.0d, 0.8125241803d, 90.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.cm  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.inertia_frame  &
   adams_id = 36  &
   location = -2.4871874502, 0.0, 34.7403924495  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.gralin_5  &
   adams_id = 37  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.gralin_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.jxs_joint_j_9  &
   adams_id = 38  &
   location = -101.6, 0.0, 419.1  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.jxs_joint_j_9  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.jxs_joint_i_11  &
   adams_id = 39  &
   location = 0.0, 0.0, -127.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.jxs_joint_i_11  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.gralin_7  &
   adams_id = 40  &
   location = -31.496, 209.55, 444.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.gralin_7  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.ues_spring_i_1  &
   adams_id = 41  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.ues_spring_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.ues_damper_i_1  &
   adams_id = 42  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.ues_damper_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.ues_stopper_i_1  &
   adams_id = 43  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.ues_stopper_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.coomarker_2  &
   adams_id = 44  &
   location = -31.496, 0.0, 444.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.coomarker_2  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.coomarker_3  &
   adams_id = 45  &
   location = -31.496, 0.0, 469.9  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_cylinder.coomarker_3  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_175  &
   adams_id = 175  &
   location = -31.496, 0.0, 469.9  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_176  &
   adams_id = 176  &
   location = -31.496, 0.0, 469.9  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_158  &
   adams_id = 158  &
   location = -31.496, -209.55, 444.5  &
   orientation = 180.0d, 90.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_160  &
   adams_id = 160  &
   location = -31.496, 209.55, 444.5  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_122  &
   adams_id = 122  &
   location = 0.0, 0.0, -444.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_125  &
   adams_id = 125  &
   location = 0.0, 0.0, -444.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_127  &
   adams_id = 127  &
   location = 0.0, 0.0, -444.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_164  &
   adams_id = 164  &
   location = 0.0, 0.0, -444.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.ges_lower_cylinder  &
   mass = 84.884  &
   center_of_mass_marker = .template_7_swing.ges_lower_cylinder.cm  &
   inertia_marker = .template_7_swing.ges_lower_cylinder.inertia_frame  &
   ixx = 6.834E+06  &
   iyy = 6.449E+06  &
   izz = 8.04E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.ges_lower_cylinder.gralin_geom1  &
   adams_id = 44  &
   center_marker = .template_7_swing.ges_lower_cylinder.gralin_5  &
   angle_extent = 360.0  &
   length = 889.0  &
   radius = 101.6  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.ges_lower_cylinder.gralin_geom2  &
   adams_id = 45  &
   center_marker = .template_7_swing.ges_lower_cylinder.gralin_7  &
   angle_extent = 360.0  &
   length = 419.1  &
   radius = 30.48  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_lower_cylinder.gralin_geom2  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_7_swing.ges_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!---------------------------- ges_upper_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.ges_upper_torque_arm  &
   adams_id = 6  &
   location = 6489.7, 0.0, 774.7  &
   orientation = 90.0d, 111.0375110254d, 270.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_upper_torque_arm  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ges_upper_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.ges_upper_torque_arm.cm  &
   adams_id = 46  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_upper_torque_arm.inertia_frame  &
   adams_id = 47  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_torque_arm.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_upper_torque_arm.gralin_9  &
   adams_id = 48  &
   location = -6.7140737414E-11, 0.0, -176.8905311202  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_torque_arm.gralin_9  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_upper_torque_arm.jxs_joint_j_8  &
   adams_id = 49  &
   location = 6.7459926534E-11, 0.0, 176.8905311202  &
   orientation = 0.0d, 90.0d, 111.0375110254d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_torque_arm.jxs_joint_j_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_upper_torque_arm.jxs_joint_i_10  &
   adams_id = 50  &
   location = -6.7140737414E-11, 0.0, -176.8905311202  &
   orientation = 0.0d, 90.0d, 111.0375110254d
!
marker attributes  &
   marker_name = .template_7_swing.ges_upper_torque_arm.jxs_joint_i_10  &
   visibility = off  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.ges_upper_torque_arm  &
   mass = 0.39  &
   center_of_mass_marker = .template_7_swing.ges_upper_torque_arm.cm  &
   inertia_marker = .template_7_swing.ges_upper_torque_arm.inertia_frame  &
   ixx = 3000.0  &
   iyy = 3000.0  &
   izz = 31.44  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   adams_id = 46  &
   center_marker = .template_7_swing.ges_upper_torque_arm.gralin_9  &
   angle_extent = 360.0  &
   length = 353.7810622405  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   color = GREEN
!
part attributes  &
   part_name = .template_7_swing.ges_upper_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!---------------------------- ges_lower_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.ges_lower_torque_arm  &
   adams_id = 7  &
   location = 6477.0, 0.0, 622.3  &
   orientation = 90.0d, 63.4349488229d, 270.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_lower_torque_arm  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ges_lower_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.ges_lower_torque_arm.cm  &
   adams_id = 51  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_lower_torque_arm.inertia_frame  &
   adams_id = 52  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_torque_arm.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_lower_torque_arm.jxs_joint_i_8  &
   adams_id = 53  &
   location = 7.6771922153E-11, 0.0, 198.7864431997  &
   orientation = 0.0d, 90.0d, 63.4349488229d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_torque_arm.jxs_joint_i_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_lower_torque_arm.gralin_10  &
   adams_id = 54  &
   location = -7.6189055065E-11, 0.0, -198.7864431997  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_torque_arm.gralin_10  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_lower_torque_arm.jxs_joint_i_9  &
   adams_id = 55  &
   location = -7.6189055065E-11, 0.0, -198.7864431997  &
   orientation = 270.0d, 63.4349488229d, 90.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_lower_torque_arm.jxs_joint_i_9  &
   visibility = off  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.ges_lower_torque_arm  &
   mass = 0.39  &
   center_of_mass_marker = .template_7_swing.ges_lower_torque_arm.cm  &
   inertia_marker = .template_7_swing.ges_lower_torque_arm.inertia_frame  &
   ixx = 3000.0  &
   iyy = 3000.0  &
   izz = 31.44  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   adams_id = 47  &
   center_marker = .template_7_swing.ges_lower_torque_arm.gralin_10  &
   angle_extent = 360.0  &
   length = 397.5728863995  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_7_swing.ges_lower_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!-------------------------------- ges_subframe --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.ges_subframe  &
   adams_id = 8  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_subframe  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ges_subframe
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.ges_subframe.cm  &
   adams_id = 56  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_subframe.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_subframe.inertia_frame  &
   adams_id = 57  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_subframe.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_subframe.graout_1  &
   adams_id = 58  &
   location = -390.5595878992, 5.9115906614E-11, -340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_subframe.graout_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_subframe.graout_2  &
   adams_id = 59  &
   location = -390.5595878992, 5.9115906614E-11, 340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_subframe.graout_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_subframe.graout_3  &
   adams_id = 60  &
   location = 781.1191757984, -1.1850243009E-10, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_subframe.graout_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_7_swing.ges_subframe.jxs_joint_j_15  &
   adams_id = 61  &
   location = -390.5595878992, 5.9115906614E-11, 0.0  &
   orientation = 3.3555200908d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_subframe.jxs_joint_j_15  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_subframe.jxs_joint_j_14  &
   adams_id = 63  &
   location = 781.1191757984, -1.1850243009E-10, 0.0  &
   orientation = 3.3555200908d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_subframe.jxs_joint_j_14  &
   visibility = off  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.ges_subframe  &
   mass = 0.0  &
   center_of_mass_marker = .template_7_swing.ges_subframe.cm  &
   inertia_marker = .template_7_swing.ges_subframe.inertia_frame  &
   ixx = 0.0  &
   iyy = 0.0  &
   izz = 0.0  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create curve outline  &
   outline_name = .template_7_swing.ges_subframe.graout_subframe_geom  &
   adams_id = 49  &
   marker_name =  &
      .template_7_swing.ges_subframe.graout_1,  &
      .template_7_swing.ges_subframe.graout_2,  &
      .template_7_swing.ges_subframe.graout_3  &
   visibility_between_markers = on, on, on  &
   close = yes
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_subframe.graout_subframe_geom  &
   color = WHITE
!
part attributes  &
   part_name = .template_7_swing.ges_subframe  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!------------------------------- mts_body_mount -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.mts_body_mount  &
   adams_id = 9  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.mts_body_mount  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.mts_body_mount
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.mts_body_mount.mount_i  &
   adams_id = 64  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.mts_body_mount.mount_i  &
   visibility = off  &
   name_visibility = off
!
part attributes  &
   part_name = .template_7_swing.mts_body_mount  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- ges_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.ges_collar  &
   adams_id = 10  &
   location = 6197.6, 0.0, 809.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_collar  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ges_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.ges_collar.jxs_joint_j_10  &
   adams_id = 66  &
   location = 127.0, 0.0, 28.702  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_collar.jxs_joint_j_10  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_collar.cm  &
   adams_id = 67  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_collar.cm  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_collar.inertia_frame  &
   adams_id = 68  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_collar.gralin_24  &
   adams_id = 69  &
   location = 0.0, 0.0, -47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_collar.gralin_24  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_collar.jxs_joint_i_1  &
   adams_id = 70  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_collar.jxs_joint_i_1  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_collar.ues_actuator_i_1  &
   adams_id = 71  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_collar.ues_actuator_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_collar.ues_actuator_i_4  &
   adams_id = 72  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_7_swing.ges_collar.ues_actuator_i_4  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_7_swing.ges_collar.MARKER_75  &
   adams_id = 75  &
   location = 0.0, 200.0, -9.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.ges_collar.MARKER_166  &
   adams_id = 166  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.ges_collar  &
   mass = 6.424  &
   center_of_mass_marker = .template_7_swing.ges_collar.cm  &
   inertia_marker = .template_7_swing.ges_collar.inertia_frame  &
   ixx = 8.5E+04  &
   iyy = 8.5E+04  &
   izz = 1.47E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.ges_collar.gralin_collar  &
   adams_id = 48  &
   center_marker = .template_7_swing.ges_collar.gralin_24  &
   angle_extent = 360.0  &
   length = 94.996  &
   radius = 139.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_7_swing.ges_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .template_7_swing.ges_collar  &
   visibility = on  &
   name_visibility = on
!
!------------------------------------ zdt -------------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.zdt  &
   adams_id = 12  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.zdt  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.zdt
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.zdt.gralin_74  &
   adams_id = 74  &
   location = 5918.7250255242, 12.5840225297, 800.0  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_7_swing.zdt.cm  &
   adams_id = 84  &
   location = 5849.0062819053, -34.2699718379, 800.0  &
   orientation = 303.9027984031d, 90.0d, 98.3803726002d
!
marker create  &
   marker_name = .template_7_swing.zdt.MARKER_78  &
   adams_id = 78  &
   location = 5918.7250255242, 12.5840225297, 800.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.zdt.MARKER_86  &
   adams_id = 86  &
   location = 5849.0062819053, -34.2699718379, 800.0  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.zdt  &
   mass = 0.0  &
   center_of_mass_marker = .template_7_swing.zdt.cm  &
   ixx = 0.0  &
   iyy = 0.0  &
   izz = 0.0  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_7_swing.zdt.CYLINDER_51  &
   adams_id = 51  &
   center_marker = .template_7_swing.zdt.gralin_74  &
   angle_extent = 360.0  &
   length = 168.0  &
   radius = 33.4634781504  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_7_swing.zdt  &
   color = MAIZE  &
   name_visibility = off
!
!------------------------------------- js -------------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part create rigid_body name_and_position  &
   part_name = .template_7_swing.js  &
   adams_id = 18  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body initial_velocity  &
   part_name = .template_7_swing.js  &
   vx = 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.js
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_7_swing.js.MARKER_173  &
   adams_id = 173  &
   location = 6197.6, 0.0, 1825.6  &
   orientation = 90.0d, 90.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.js.MARKER_177  &
   adams_id = 177  &
   location = 6197.6, 0.0, 1825.6  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_7_swing.js.MARKER_117  &
   adams_id = 117  &
   location = 6197.6, 0.0, 1825.6  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.js.cm  &
   adams_id = 128  &
   location = 6197.6, 0.0, 1825.6  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.js.MARKER_118  &
   adams_id = 118  &
   location = 6197.6, 0.0, 1825.6  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_7_swing.js.MARKER_132  &
   adams_id = 132  &
   location = 6197.6, 0.0, 1825.6  &
   orientation = 90.0d, 90.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_7_swing.js  &
   mass = 300.0  &
   center_of_mass_marker = .template_7_swing.js.cm  &
   ixx = 1.31E+05  &
   iyy = 1.31E+05  &
   izz = 1.31E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_7_swing.js.ELLIPSOID_77  &
   adams_id = 80  &
   center_marker = .template_7_swing.js.MARKER_117  &
   x_scale_factor = 200.0  &
   y_scale_factor = 200.0  &
   z_scale_factor = 200.0
!
part attributes  &
   part_name = .template_7_swing.js  &
   color = CYAN  &
   name_visibility = off
!
!--------------------------------- Equations ----------------------------------!
!
!
part create equation differential_equation  &
   differential_equation_name = .template_7_swing._cv_diff  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   initial_condition = 0.0  &
   function = ""  &
   implicit = off  &
   static_hold = off
!
part attributes  &
   equation_name = .template_7_swing._cv_diff  &
   visibility = off
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint cylindrical  &
   joint_name = .template_7_swing._cv_joint_for_motion  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   i_marker_name = .template_7_swing._cv_part.marker  &
   j_marker_name = .template_7_swing.ground._cv_marker
!
constraint attributes  &
   constraint_name = .template_7_swing._cv_joint_for_motion  &
   name_visibility = off  &
   size_of_icons = 50.8
!
constraint create joint revolute  &
   joint_name = .template_7_swing.josrev_lta_uta_joint  &
   adams_id = 2  &
   i_marker_name = .template_7_swing.ges_lower_torque_arm.jxs_joint_i_8  &
   j_marker_name = .template_7_swing.ges_upper_torque_arm.jxs_joint_j_8
!
constraint attributes  &
   constraint_name = .template_7_swing.josrev_lta_uta_joint  &
   size_of_icons = 50.8
!
constraint create joint spherical  &
   joint_name = .template_7_swing.jossph_lta_lc_joint  &
   adams_id = 3  &
   i_marker_name = .template_7_swing.ges_lower_torque_arm.jxs_joint_i_9  &
   j_marker_name = .template_7_swing.ges_lower_cylinder.jxs_joint_j_9
!
constraint create joint revolute  &
   joint_name = .template_7_swing.josrev_uta_uc_joint  &
   adams_id = 4  &
   i_marker_name = .template_7_swing.ges_upper_torque_arm.jxs_joint_i_10  &
   j_marker_name = .template_7_swing.ges_collar.jxs_joint_j_10
!
constraint create joint cylindrical  &
   joint_name = .template_7_swing.joscyl_lc_uc_joint  &
   adams_id = 5  &
   i_marker_name = .template_7_swing.ges_lower_cylinder.jxs_joint_i_11  &
   j_marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_11
!
constraint create joint spherical  &
   joint_name = .template_7_swing.jossph_db_uc_joint  &
   adams_id = 6  &
   i_marker_name = .template_7_swing.ges_dragbrace.jxs_joint_i_12  &
   j_marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_12
!
constraint create joint revolute  &
   joint_name = .template_7_swing.josrev_uc_sf_joint  &
   adams_id = 7  &
   i_marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_i_15  &
   j_marker_name = .template_7_swing.ges_subframe.jxs_joint_j_15
!
constraint create joint fixed  &
   joint_name = .template_7_swing.mts_fixed_2  &
   adams_id = 8  &
   i_marker_name = .template_7_swing.mts_body_mount.mount_i  &
   j_marker_name = .template_7_swing.ground.mts_mount_j_2
!
constraint attributes  &
   constraint_name = .template_7_swing.mts_fixed_2  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_7_swing.JOINT_21  &
   adams_id = 21  &
   i_marker_name = .template_7_swing.ges_collar.jxs_joint_i_1  &
   j_marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_1
!
constraint create joint cylindrical  &
   joint_name = .template_7_swing.joscyl_db_sf  &
   adams_id = 10  &
   i_marker_name = .template_7_swing.ges_dragbrace.jxs_joint_i_14  &
   j_marker_name = .template_7_swing.ges_subframe.jxs_joint_j_14
!
constraint create joint revolute  &
   joint_name = .template_7_swing.josrev_collar_uc_joint  &
   adams_id = 11  &
   i_marker_name = .template_7_swing.ges_collar.jxs_joint_i_1  &
   j_marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_1
!
constraint create joint revolute  &
   joint_name = .template_7_swing.hsg_collar  &
   adams_id = 12  &
   i_marker_name = .template_7_swing.ges_collar.MARKER_75  &
   j_marker_name = .template_7_swing.hsg.MARKER_76
!
constraint attributes  &
   constraint_name = .template_7_swing.hsg_collar  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_7_swing.zdt_upcylinder  &
   adams_id = 13  &
   i_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_77  &
   j_marker_name = .template_7_swing.zdt.MARKER_78
!
constraint attributes  &
   constraint_name = .template_7_swing.zdt_upcylinder  &
   name_visibility = off
!
constraint create joint translational  &
   joint_name = .template_7_swing.hsg_zdt  &
   adams_id = 14  &
   i_marker_name = .template_7_swing.hsg.MARKER_85  &
   j_marker_name = .template_7_swing.zdt.MARKER_86
!
constraint attributes  &
   constraint_name = .template_7_swing.hsg_zdt  &
   name_visibility = off
!
constraint create joint fixed  &
   joint_name = .template_7_swing.js_wt  &
   adams_id = 18  &
   i_marker_name = .template_7_swing.js.MARKER_118  &
   j_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_119
!
constraint attributes  &
   constraint_name = .template_7_swing.js_wt  &
   name_visibility = off
!
!------------------------------ Joint Primitives ------------------------------!
!
!
constraint create primitive_joint inplane  &
   jprim_name = .template_7_swing.JPRIM_3  &
   adams_id = 3  &
   i_marker_name = .template_7_swing.js.MARKER_177  &
   j_marker_name = .template_7_swing.ground.MARKER_178
!
constraint attributes  &
   constraint_name = .template_7_swing.JPRIM_3  &
   name_visibility = off
!
!----------------------------------- Forces -----------------------------------!
!
!
force create element_like field  &
   field_name = .template_7_swing._cv_bushing  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   i_marker_name = .template_7_swing._cv_part.marker  &
   j_marker_name = .template_7_swing.ground._cv_marker  &
   translation_at_preload = 0.0, 0.0, 0.0  &
   rotation_at_preload = 0.0d, 0.0d, 0.0d  &
   formulation = linear  &
   length_tolerance = 1.0E-05  &
   damping_ratio = 0.0  &
   stiffness_matrix =  &
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  &
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  &
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  &
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  &
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  &
      0.0, 0.0, 0.0, 0.0, 0.0, 0.0  &
   force_preload = 0.0, 0.0, 0.0  &
   torque_preload = 0.0, 0.0, 0.0
!
force attributes  &
   force_name = .template_7_swing._cv_bushing  &
   name_visibility = off  &
   size_of_icons = 50.8
!
force create direct single_component_force  &
   single_component_force_name = .template_7_swing.turning_force  &
   adams_id = 1  &
   type_of_freedom = translational  &
   i_marker_name = .template_7_swing.hsg.MARKER_81  &
   j_marker_name = .template_7_swing.hsg.MARKER_82  &
   action_only = on  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_7_swing.damping_force  &
   adams_id = 7  &
   type_of_freedom = rotational  &
   i_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_165  &
   j_marker_name = .template_7_swing.ges_collar.MARKER_166  &
   action_only = off  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_7_swing.NLG_AIR  &
   adams_id = 3  &
   type_of_freedom = translational  &
   i_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_124  &
   j_marker_name = .template_7_swing.ges_lower_cylinder.MARKER_125  &
   action_only = off  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_7_swing.NLG_STOP  &
   adams_id = 4  &
   type_of_freedom = translational  &
   i_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_126  &
   j_marker_name = .template_7_swing.ges_lower_cylinder.MARKER_127  &
   action_only = off  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_7_swing.excitation_torque  &
   adams_id = 8  &
   type_of_freedom = rotational  &
   i_marker_name = .template_7_swing.ges_lower_cylinder.MARKER_175  &
   j_marker_name = .template_7_swing.ges_lower_cylinder.MARKER_176  &
   action_only = on  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_7_swing.NLG_OIL  &
   adams_id = 6  &
   type_of_freedom = translational  &
   i_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_163  &
   j_marker_name = .template_7_swing.ges_lower_cylinder.MARKER_164  &
   action_only = off  &
   function = ""
!
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .template_7_swing.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=6.0 step_size=1.0E-03 model_name=.gcmb_2"
!
!-------------------------- Adams View UDE Instances --------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
undo begin_block suppress = yes
!
ude create instance  &
   instance_name = .template_7_swing.lm  &
   definition_name = .MDI.Forces.vpg_road  &
   location = 0.0, 0.0, 327.5  &
   orientation = 0.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_7_swing.lm  &
   color = DimGray  &
   visibility = off
!
ude create instance  &
   instance_name = .template_7_swing.lt_l  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 6229.096, -209.55, 508.0  &
   orientation = 0.0, 90.0, 0.0
!
ude create instance  &
   instance_name = .template_7_swing.lt_r  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 6229.096, 209.55, 508.0  &
   orientation = 0.0, 90.0, 90.0
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_7_swing.lm.ref_marker  &
   object_value = .template_7_swing.ground.lm_ref_1
!
variable modify  &
   variable_name = .template_7_swing.lm.road_property_file  &
   string_value = "2d_flat.rdf"
!
variable modify  &
   variable_name = .template_7_swing.lm.road_graphics  &
   string_value = "on"
!
ude modify instance  &
   instance_name = .template_7_swing.lm
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker create  &
   marker_name = .template_7_swing.lm.road_part.MARKER_131  &
   adams_id = 131  &
   location = 6197.6, 0.0, 2153.1  &
   orientation = 90.0d, 90.0d, 0.0d
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_7_swing.lt_l.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ic_vmode  &
   string_value = "standard"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_7_swing.lt_l.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_7_swing.lt_l.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ic_wz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ic_vm  &
   string_value = "ground"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ic_wm  &
   string_value = "cm"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.vmmrk  &
   object_value = (.template_7_swing.lt_l.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_7_swing.lt_l.wmmrk  &
   object_value = (.template_7_swing.lt_l.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_7_swing.lt_l.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.road_property_file  &
   string_value = (.template_7_swing.lm.road_property_file)
!
variable modify  &
   variable_name = .template_7_swing.lt_l.j_fmarker  &
   object_value = .template_7_swing.ground.lt_l_tire_jf_1
!
variable modify  &
   variable_name = .template_7_swing.lt_l.ref_marker  &
   object_value = (.template_7_swing.lm.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_7_swing.lt_l.wheel_tire_mass  &
   real_value = 5.5
!
variable modify  &
   variable_name = .template_7_swing.lt_l.Ixx_Iyy  &
   real_value = 3.0E+04
!
variable modify  &
   variable_name = .template_7_swing.lt_l.Izz  &
   real_value = 3.0E+04
!
variable modify  &
   variable_name = .template_7_swing.lt_l.property_file  &
   string_value = "uat_nlg.tir"
!
variable modify  &
   variable_name = .template_7_swing.lt_l.road_name  &
   string_value = (.template_7_swing.lm)
!
ude modify instance  &
   instance_name = .template_7_swing.lt_l
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker create  &
   marker_name = .template_7_swing.lt_l.wheel_part.MARKER_157  &
   adams_id = 157  &
   location = 0.0, 0.0, 0.0  &
   orientation = 180.0d, 90.0d, 180.0d
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_7_swing.lt_r.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ic_vmode  &
   string_value = "standard"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_7_swing.lt_r.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_7_swing.lt_r.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ic_wz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ic_vm  &
   string_value = "ground"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ic_wm  &
   string_value = "cm"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.vmmrk  &
   object_value = (.template_7_swing.lt_r.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_7_swing.lt_r.wmmrk  &
   object_value = (.template_7_swing.lt_r.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_7_swing.lt_r.side  &
   string_value = "right"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.road_property_file  &
   string_value = (.template_7_swing.lm.road_property_file)
!
variable modify  &
   variable_name = .template_7_swing.lt_r.j_fmarker  &
   object_value = .template_7_swing.ground.lt_r_tire_jf_2
!
variable modify  &
   variable_name = .template_7_swing.lt_r.ref_marker  &
   object_value = (.template_7_swing.lm.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_7_swing.lt_r.wheel_tire_mass  &
   real_value = 5.5
!
variable modify  &
   variable_name = .template_7_swing.lt_r.Ixx_Iyy  &
   real_value = 3.0E+04
!
variable modify  &
   variable_name = .template_7_swing.lt_r.Izz  &
   real_value = 3.0E+04
!
variable modify  &
   variable_name = .template_7_swing.lt_r.property_file  &
   string_value = "uat_nlg.tir"
!
variable modify  &
   variable_name = .template_7_swing.lt_r.road_name  &
   string_value = (.template_7_swing.lm)
!
ude modify instance  &
   instance_name = .template_7_swing.lt_r
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker create  &
   marker_name = .template_7_swing.lt_r.wheel_part.MARKER_159  &
   adams_id = 159  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 90.0d, 0.0d
!
undo end_block
!
!--------------------------- UDE Dependent Objects ----------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_7_swing.joint_lt_z  &
   adams_id = 19  &
   i_marker_name = .template_7_swing.lt_l.wheel_part.MARKER_157  &
   j_marker_name = .template_7_swing.ges_lower_cylinder.MARKER_158
!
constraint attributes  &
   constraint_name = .template_7_swing.joint_lt_z  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_7_swing.joint_lt_y  &
   adams_id = 20  &
   i_marker_name = .template_7_swing.lt_r.wheel_part.MARKER_159  &
   j_marker_name = .template_7_swing.ges_lower_cylinder.MARKER_160
!
constraint attributes  &
   constraint_name = .template_7_swing.joint_lt_y  &
   name_visibility = off
!
constraint create primitive_joint orientation  &
   jprim_name = .template_7_swing.JPRIM_2  &
   adams_id = 2  &
   i_marker_name = .template_7_swing.lm.road_part.MARKER_131  &
   j_marker_name = .template_7_swing.js.MARKER_132
!
constraint attributes  &
   constraint_name = .template_7_swing.JPRIM_2  &
   name_visibility = off
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry create shape force  &
   force_name = .template_7_swing.SFORCE_1_force_graphic_1  &
   adams_id = 52  &
   force_element_name = .template_7_swing.turning_force  &
   applied_at_marker_name = .template_7_swing.hsg.MARKER_81
!
geometry create shape force  &
   force_name = .template_7_swing.SFORCE_7_force_graphic_1  &
   adams_id = 108  &
   force_element_name = .template_7_swing.damping_force  &
   applied_at_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_165
!
geometry create shape force  &
   force_name = .template_7_swing.SFORCE_3_force_graphic_1  &
   adams_id = 78  &
   force_element_name = .template_7_swing.NLG_AIR  &
   applied_at_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_124
!
geometry create shape force  &
   force_name = .template_7_swing.SFORCE_4_force_graphic_1  &
   adams_id = 79  &
   force_element_name = .template_7_swing.NLG_STOP  &
   applied_at_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_126
!
geometry create shape force  &
   force_name = .template_7_swing.SFORCE_8_force_graphic_1  &
   adams_id = 133  &
   force_element_name = .template_7_swing.excitation_torque  &
   applied_at_marker_name = .template_7_swing.ges_lower_cylinder.MARKER_175
!
geometry create shape force  &
   force_name = .template_7_swing.SFORCE_6_force_graphic_1  &
   adams_id = 107  &
   force_element_name = .template_7_swing.NLG_OIL  &
   applied_at_marker_name = .template_7_swing.ges_upper_cylinder.MARKER_163
!
!---------------------------------- Motions -----------------------------------!
!
!
constraint create motion_generator  &
   motion_name = .template_7_swing.speed_setting  &
   adams_id = 1  &
   i_marker_name = .template_7_swing.js.MARKER_173  &
   j_marker_name = .template_7_swing.ground.MARKER_174  &
   axis = z  &
   time_derivative = velocity  &
   function = ""
!
constraint attributes  &
   constraint_name = .template_7_swing.speed_setting  &
   name_visibility = off
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   x_component_gravity = 0.0  &
   y_component_gravity = 0.0  &
   z_component_gravity = -9807.0
!
force attributes  &
   force_name = .template_7_swing.gravity  &
   size_of_icons = 50.8
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------------- Measures ----------------------------------!
!
!
measure create point  &
   measure_name = .template_7_swing.jscm_sd  &
   point = .template_7_swing.js.cm  &
   characteristic = translational_velocity  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_7_swing.jscm_sd  &
   color = WHITE
!
measure create function  &
   measure_name = .template_7_swing.jiaodu  &
   function = ""  &
   units = "no_units"  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_7_swing.jiaodu  &
   color = WHITE
!
measure create function  &
   measure_name = .template_7_swing.jsd  &
   function = ""  &
   units = "no_units"  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_7_swing.jsd  &
   color = WHITE
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_7_swing.mts_body_mount.minor_role  &
   string_value = "inherit"
!
variable create  &
   variable_name = .template_7_swing.initial_vel  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.0
!
variable create  &
   variable_name = .template_7_swing.stiffness_air  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1000.0
!
variable create  &
   variable_name = .template_7_swing.damping_air  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 10.0
!
variable create  &
   variable_name = .template_7_swing.stiffness_oil  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1000.0
!
variable create  &
   variable_name = .template_7_swing.damping_oil  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 10.0
!
variable create  &
   variable_name = .template_7_swing.stiffness_stop  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1000.0
!
variable create  &
   variable_name = .template_7_swing.damping_stop  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 10.0
!
variable create  &
   variable_name = .template_7_swing.vel  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.0E+04
!
variable create  &
   variable_name = .template_7_swing.damping_coefficient  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 525.0
!
variable create  &
   variable_name = .template_7_swing.angle  &
   units = "no_units"  &
   range = -0.1, 0.1  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 30.0
!
variable create  &
   variable_name = .template_7_swing.T_1  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_7_swing.T_2  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.5
!
!---------------------------- Function definitions ----------------------------!
!
!
constraint modify motion_generator  &
   motion_name = .template_7_swing.speed_setting  &
   function = "step(time,.template_7_swing.T_1,0,.template_7_swing.T_2,-.template_7_swing.vel)"
!
data_element modify variable  &
   variable_name = .template_7_swing._cv_solver_variable  &
   function = "0"
!
measure modify function  &
   measure_name = .template_7_swing.jiaodu  &
   function = "AZ(.template_7_swing.ges_collar.inertia_frame, .template_7_swing.ges_upper_cylinder.inertia_frame)*180/pi-180"
!
measure modify function  &
   measure_name = .template_7_swing.jsd  &
   function = "wz(.template_7_swing.ges_collar.inertia_frame, .template_7_swing.ges_upper_cylinder.inertia_frame)*30/pi"
!
part modify equation differential_equation  &
   differential_equation_name = .template_7_swing._cv_diff  &
   function = "0"
!
force modify direct single_component_force  &
   single_component_force_name = .template_7_swing.turning_force  &
   function = "step(time,2,0,4,1)*(5000/30)*(.template_7_swing.angle+.template_7_swing.jiaodu)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_7_swing.damping_force  &
   function = ".template_7_swing.jsd*.template_7_swing.damping_coefficient"
!
force modify direct single_component_force  &
   single_component_force_name = .template_7_swing.NLG_AIR  &
   function = "if((DM(.template_7_swing.ges_upper_cylinder.MARKER_124,.template_7_swing.ges_lower_cylinder.MARKER_125)-228.6):-.template_7_swing.stiffness_air*(DM(.template_7_swing.ges_upper_cylinder.MARKER_124,.template_7_swing.ges_lower_cylinder.MARKER_125)-228.6)-.template_7_swing.damping_air*VR(.template_7_swing.ges_upper_cylinder.MARKER_124,.template_7_swing.ges_lower_cylinder.MARKER_125),0,0)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_7_swing.NLG_STOP  &
   function = "-if((DM(.template_7_swing.ges_upper_cylinder.MARKER_126,.template_7_swing.ges_lower_cylinder.MARKER_127)-258.6):0,0,-.template_7_swing.stiffness_stop*(DM(.template_7_swing.ges_upper_cylinder.MARKER_126,.template_7_swing.ges_lower_cylinder.MARKER_127)-258.6)-.template_7_swing.damping_stop*VR(.template_7_swing.ges_upper_cylinder.MARKER_126,.template_7_swing.ges_lower_cylinder.MARKER_127))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_7_swing.excitation_torque  &
   function = "AKISPL(time,0,.template_7_swing.jili, 0)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_7_swing.NLG_OIL  &
   function = "if(DM(.template_7_swing.ges_upper_cylinder.MARKER_163,.template_7_swing.ges_lower_cylinder.MARKER_164)-228.6:-.template_7_swing.stiffness_oil*(DM(.template_7_swing.ges_upper_cylinder.MARKER_163,.template_7_swing.ges_lower_cylinder.MARKER_164)-228.6)-.template_7_swing.damping_oil*VR(.template_7_swing.ges_upper_cylinder.MARKER_163,.template_7_swing.ges_lower_cylinder.MARKER_164),0,0)"
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_7_swing.lm
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_7_swing.lt_l
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_7_swing.lt_r
!
!------------------------- Part IC Reference Markers --------------------------!
!
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.lt_l.wheel_part  &
   vm = .template_7_swing.lt_l.wheel_part.wheel_cm  &
   wm = .template_7_swing.lt_l.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.lt_l.belt_part  &
   vm = .template_7_swing.lt_l.wheel_part.wheel_cm  &
   wm = .template_7_swing.lt_l.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.lt_r.wheel_part  &
   vm = .template_7_swing.lt_r.wheel_part.wheel_cm  &
   wm = .template_7_swing.lt_r.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.lt_r.belt_part  &
   vm = .template_7_swing.lt_r.wheel_part.wheel_cm  &
   wm = .template_7_swing.lt_r.wheel_part.wheel_cm
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_7_swing.ground.mts_mount_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.mts_body_mount))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.mts_body_mount))
!
marker modify  &
   marker_name = .template_7_swing.ground.cfl_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.hpl_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hpl_wheel_center, .template_7_swing.ground.hpl_ob_axle, "Z"))
!
marker modify  &
   marker_name = .template_7_swing.ground.cfr_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hpr_wheel_center, .template_7_swing.ground.hpr_ob_axle, "Z"))
!
marker modify  &
   marker_name = .template_7_swing.ground.cfs_nlg_axle_lowpoint  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.hps_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_7_swing.ground.origo))
!
marker modify  &
   marker_name = .template_7_swing.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_7_swing.ground.hps_uc_bot, .template_7_swing.ground.hps_uc_top, 0.11 * DM(.template_7_swing.ground.hps_uc_bot, .template_7_swing.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_uc_bot, .template_7_swing.ground.hps_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_7_swing.ground.lm_ref_1  &
   location =   &
      (.template_7_swing.lm.location)  &
   orientation =   &
      (.template_7_swing.lm.orientation)
!
marker modify  &
   marker_name = .template_7_swing.ground.zdt1  &
   location =   &
      (LOC_ALONG_LINE(.template_7_swing.ground.hsg_1, .template_7_swing.ground.hsg_2, 0.6 * DM(.template_7_swing.ground.hsg_1, .template_7_swing.ground.hsg_2)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hsg_1, .template_7_swing.ground.hsg_2, "Z"))
!
marker modify  &
   marker_name = .template_7_swing.ground.zdt2  &
   location =   &
      (LOC_ALONG_LINE(.template_7_swing.ground.hsg_1, .template_7_swing.ground.hsg_2, 0.9 * DM(.template_7_swing.ground.hsg_1, .template_7_swing.ground.hsg_2)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hsg_1, .template_7_swing.ground.hsg_2, "Z"))
!
material modify  &
   material_name = .template_7_swing.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing._cv_part  &
   vx = (.template_7_swing.initial_vel)
!
marker modify  &
   marker_name = .template_7_swing.ges_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_dragbrace))  &
   relative_to = .template_7_swing.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_dragbrace.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_db_sf_atch, .template_7_swing.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .template_7_swing.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_dragbrace.jxs_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_12))  &
   relative_to = .template_7_swing.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_dragbrace.jxs_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_subframe.jxs_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_subframe.jxs_joint_j_14))  &
   relative_to = .template_7_swing.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.ges_dragbrace.gralin_dragbrace_geom  &
   length = (DM(.template_7_swing.ground.hps_db_sf_atch, .template_7_swing.ground.hps_db_uc_atch))
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_dragbrace  &
   vx = (.template_7_swing.initial_vel)
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_uc_top, .template_7_swing.ground.hps_uc_bot, "Z"))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_uc_sf_atch_l, .template_7_swing.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_uc_sf_atch_r, .template_7_swing.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_12  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.hps_db_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_7_swing.ground.origo))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_i_15  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_subframe.jxs_joint_j_15))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_subframe.jxs_joint_j_15))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_top))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_top))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_top))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_uc_bot, .template_7_swing.ground.hps_uc_top, "Z"))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.ues_actuator_j_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.template_7_swing.ground.hps_uc_top, .template_7_swing.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.template_7_swing.ground.hps_uc_sf_atch_l, .template_7_swing.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.template_7_swing.ground.hps_uc_sf_atch_r, .template_7_swing.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_77  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.zdt1))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_123  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_top))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_cylinder.MARKER_163  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_top))  &
   relative_to = .template_7_swing.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_upper_cylinder  &
   vx = (.template_7_swing.initial_vel)
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_lower_cylinder))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_lc_top, .template_7_swing.ground.hps_lc_bot, "Z"))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.jxs_joint_j_9  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_7_swing.ground.origo))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hpr_wheel_center, .template_7_swing.ground.hpl_wheel_center, "Z"))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.ues_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_lc_top))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.ues_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_lc_top))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.ues_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_lc_top))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.coomarker_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.cfs_wheel_centers_midpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.cfs_wheel_centers_midpoint))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.coomarker_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.cfs_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.cfs_nlg_axle_lowpoint))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.ges_lower_cylinder.gralin_geom1  &
   length = (DM(.template_7_swing.ground.hps_lc_top, .template_7_swing.ground.hps_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.ges_lower_cylinder.gralin_geom2  &
   length = (DM(.template_7_swing.ground.hpr_wheel_center, .template_7_swing.ground.hpl_wheel_center))
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_122  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_lc_top))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_158  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hpl_wheel_center))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_160  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hpr_wheel_center))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_164  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_lc_top))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_lower_cylinder  &
   vx = (.template_7_swing.initial_vel)
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_175  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_nlg_axle_lowpoint))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_cylinder.MARKER_176  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_nlg_axle_lowpoint))  &
   relative_to = .template_7_swing.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_torque_arm))  &
   relative_to = .template_7_swing.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_torque_arm.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_uta_uc_atch, .template_7_swing.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_7_swing.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_torque_arm.jxs_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.hps_lta_uta_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_7_swing.ground.origo))  &
   relative_to = .template_7_swing.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_upper_torque_arm.jxs_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_collar.jxs_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_collar.jxs_joint_j_10))  &
   relative_to = .template_7_swing.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   length = (DM(.template_7_swing.ground.hps_uta_uc_atch, .template_7_swing.ground.hps_lta_uta_atch))
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_upper_torque_arm  &
   vx = (.template_7_swing.initial_vel)
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_lower_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_lower_torque_arm))  &
   relative_to = .template_7_swing.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_torque_arm.jxs_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_torque_arm.jxs_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_torque_arm.jxs_joint_j_8))  &
   relative_to = .template_7_swing.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_torque_arm.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_lta_lc_atch, .template_7_swing.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_7_swing.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_lower_torque_arm.jxs_joint_i_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_lower_cylinder.jxs_joint_j_9))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_lower_cylinder.jxs_joint_j_9))  &
   relative_to = .template_7_swing.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   length = (DM(.template_7_swing.ground.hps_lta_lc_atch, .template_7_swing.ground.hps_lta_uta_atch))
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_lower_torque_arm  &
   vx = (.template_7_swing.initial_vel)
!
marker modify  &
   marker_name = .template_7_swing.ges_subframe.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_subframe.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_subframe))  &
   relative_to = .template_7_swing.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_subframe.graout_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_sf_atch_r))  &
   relative_to = .template_7_swing.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_subframe.graout_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_sf_atch_l))  &
   relative_to = .template_7_swing.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_subframe.graout_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_db_sf_atch))  &
   relative_to = .template_7_swing.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_subframe.jxs_joint_j_15  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.cfs_uc_sf_atch_mid))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_7_swing.ground.cfs_uc_sf_atch_mid, "Z+Z"), .template_7_swing.ges_subframe))  &
   relative_to = .template_7_swing.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_subframe.jxs_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_7_swing.ground.origo))  &
   relative_to = .template_7_swing.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_subframe  &
   vx = (.template_7_swing.initial_vel)
!
part modify rigid_body name_and_position  &
   part_name = .template_7_swing.mts_body_mount  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.origo))
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.mts_body_mount  &
   vx = (.template_7_swing.initial_vel)
!
marker modify  &
   marker_name = .template_7_swing.ges_collar.jxs_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_7_swing.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_7_swing.ground.origo))  &
   relative_to = .template_7_swing.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_collar))  &
   relative_to = .template_7_swing.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_collar.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hps_uc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hps_uc_bot, .template_7_swing.ground.cfs_collar_top, "Z"))  &
   relative_to = .template_7_swing.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_7_swing.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_collar.ues_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_7_swing.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.ges_collar.ues_actuator_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_7_swing.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_7_swing.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.ges_collar.gralin_collar  &
   length = (DM(.template_7_swing.ground.hps_uc_bot, .template_7_swing.ground.cfs_collar_top))
!
marker modify  &
   marker_name = .template_7_swing.ges_collar.MARKER_75  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hsg_1))  &
   relative_to = .template_7_swing.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.ges_collar  &
   vx = (.template_7_swing.initial_vel)
!
marker modify  &
   marker_name = .template_7_swing.hsg.gralin_73  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hsg_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hsg_1, .template_7_swing.ground.hsg_2, "Z"))  &
   relative_to = .template_7_swing.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.hsg.CYLINDER_50  &
   length = (DM(.template_7_swing.ground.hsg_1, .template_7_swing.ground.hsg_2))  &
   radius = (15.084427744mm)
!
marker modify  &
   marker_name = .template_7_swing.hsg.MARKER_76  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hsg_1))  &
   relative_to = .template_7_swing.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.hsg.MARKER_81  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.hsg.cm))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hsg_1, .template_7_swing.ground.zdt1, "Z"))  &
   relative_to = .template_7_swing.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.hsg.MARKER_82  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.hsg.cm))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hsg_1, .template_7_swing.ground.zdt1, "Z"))  &
   relative_to = .template_7_swing.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.hsg.MARKER_85  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.zdt.cm))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hsg_1, .template_7_swing.ground.zdt1, "Z"))  &
   relative_to = .template_7_swing.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.hsg  &
   vx = (.template_7_swing.initial_vel)
!
marker modify  &
   marker_name = .template_7_swing.zdt.gralin_74  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.zdt1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.zdt1, .template_7_swing.ground.zdt2, "Z"))  &
   relative_to = .template_7_swing.zdt
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_7_swing.zdt.CYLINDER_51  &
   length = (DM(.template_7_swing.ground.zdt1, .template_7_swing.ground.zdt2))  &
   radius = (33.4634781504mm)
!
marker modify  &
   marker_name = .template_7_swing.zdt.MARKER_78  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.zdt1))  &
   relative_to = .template_7_swing.zdt
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.zdt.MARKER_86  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.zdt.cm))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_7_swing.ground.hsg_1, .template_7_swing.ground.zdt1, "Z"))  &
   relative_to = .template_7_swing.zdt
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.zdt  &
   vx = (.template_7_swing.initial_vel)
!
geometry modify shape force  &
   force_name = .template_7_swing.SFORCE_1_force_graphic_1  &
   applied_at_marker_name = (.template_7_swing.turning_force.i)
!
marker modify  &
   marker_name = .template_7_swing.js.MARKER_117  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 200}, .template_7_swing.ground.hps_uc_top))  &
   relative_to = .template_7_swing.js
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
geometry modify shape ellipsoid  &
   ellipsoid_name = .template_7_swing.js.ELLIPSOID_77  &
   x_scale_factor = (2 * 10.0cm)  &
   y_scale_factor = (2 * 10.0cm)  &
   z_scale_factor = (2 * 10.0cm)
!
part modify rigid_body initial_velocity  &
   part_name = .template_7_swing.js  &
   vx = (.template_7_swing.initial_vel)
!
material modify  &
   material_name = .template_7_swing.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
geometry modify shape force  &
   force_name = .template_7_swing.SFORCE_3_force_graphic_1  &
   applied_at_marker_name = (.template_7_swing.NLG_AIR.i)
!
geometry modify shape force  &
   force_name = .template_7_swing.SFORCE_4_force_graphic_1  &
   applied_at_marker_name = (.template_7_swing.NLG_STOP.i)
!
marker modify  &
   marker_name = .template_7_swing.lt_l.wheel_part.MARKER_157  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hpl_wheel_center))  &
   relative_to = .template_7_swing.lt_l.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.lt_l.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_7_swing.lt_l.wheel_part.wheel_cm))  &
   relative_to = .template_7_swing.lt_l.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
ude modify instance  &
   instance_name = .template_7_swing.lt_l  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hpl_wheel_center))
!
marker modify  &
   marker_name = .template_7_swing.lt_r.wheel_part.MARKER_159  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hpr_wheel_center))  &
   relative_to = .template_7_swing.lt_r.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
marker modify  &
   marker_name = .template_7_swing.lt_r.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_7_swing.lt_r.wheel_part.wheel_cm))  &
   relative_to = .template_7_swing.lt_r.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_7_swing.ground
!
ude modify instance  &
   instance_name = .template_7_swing.lt_r  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_7_swing.ground.hpr_wheel_center))
!
geometry modify shape force  &
   force_name = .template_7_swing.SFORCE_6_force_graphic_1  &
   applied_at_marker_name = (.template_7_swing.NLG_OIL.i)
!
geometry modify shape force  &
   force_name = .template_7_swing.SFORCE_7_force_graphic_1  &
   applied_at_marker_name = (.template_7_swing.damping_force.i)
!
geometry modify shape force  &
   force_name = .template_7_swing.SFORCE_8_force_graphic_1  &
   applied_at_marker_name = (.template_7_swing.excitation_torque.i)
!
model display  &
   model_name = template_7_swing

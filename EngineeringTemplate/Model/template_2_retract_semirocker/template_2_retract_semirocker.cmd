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
   model_name = template_2_retract_semirocker  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_2_retract_semirocker  &
   size_of_icons = 50.8
!
view erase
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .template_2_retract_semirocker.aluminum  &
   adams_id = 2  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_2_retract_semirocker.steel  &
   adams_id = 3  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
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
   default_coordinate_system = .template_2_retract_semirocker.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.ground.origo  &
   adams_id = 1  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ground.origo  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ground.cfs_uc_sf_atch_mid  &
   adams_id = 3  &
   location = 6314.44, 0.0, 1691.64  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ground.cfs_uc_sf_atch_mid  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_retract_semirocker.ground.cfs_subframe_to_body_point  &
   adams_id = 4  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ground.cfs_subframe_to_body_point  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_retract_semirocker.ground.mts_mount_j_2  &
   adams_id = 5  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ground.mts_mount_j_2  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ground.cfs_wheel_centers_midpoint  &
   adams_id = 8  &
   location = 6229.096, 0.0, 508.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ground.cfs_wheel_centers_midpoint  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_retract_semirocker.ground.cfs_collar_top  &
   adams_id = 10  &
   location = 6197.6, 0.0, 856.996  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ground.cfs_collar_top  &
   color = MAIZE
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_sf_atch_l  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_sf_atch_r  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_lc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_geompt  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_lc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_origin_reference  &
   location = 0.0, 0.0, 0.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_origin_reference  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_lb_uc_atch  &
   location = 6021.578, 0.0, 795.02
!
point create  &
   point_name = .template_2_retract_semirocker.ground.POINT_12  &
   location = 5947.600000001, 0.0, 657.9999999994
!
point create  &
   point_name = .template_2_retract_semirocker.ground.POINT  &
   location = 5947.600000001, -120.0, 657.9999999994
!
point create  &
   point_name = .template_2_retract_semirocker.ground.POINT_2  &
   location = 5947.600000001, 120.0, 657.9999999994
!
point create  &
   point_name = .template_2_retract_semirocker.ground.POINT_27  &
   location = 6197.6, 0.0, 478.0
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_2_retract_semirocker.ground  &
   size_of_icons = 50.8
!
!------------------------------- ges_dragbrace --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.ges_dragbrace  &
   adams_id = 3  &
   location = 6967.855, 0.0, 1319.53  &
   orientation = 270.0d, 120.4532239091d, 90.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ges_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.cm  &
   adams_id = 12  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.inertia_frame  &
   adams_id = 13  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.gralin_1  &
   adams_id = 14  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.gralin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.jxs_joint_i_14  &
   adams_id = 16  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 0.0d, 90.0d, 239.5467760909d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.jxs_joint_i_14  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.MARKER_95  &
   adams_id = 95  &
   location = 0.0, 0.0, 0.0  &
   orientation = 202.2692735065d, 0.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract_semirocker.ges_dragbrace  &
   mass = 27.3726690382  &
   center_of_mass_marker = .template_2_retract_semirocker.ges_dragbrace.cm  &
   inertia_marker =   &
                    .template_2_retract_semirocker.ges_dragbrace.inertia_frame  &
   ixx = 3.4811540175E+06  &
   iyy = 3.4811540175E+06  &
   izz = 3.5319502313E+04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_dragbrace.gralin_dragbrace_geom  &
   adams_id = 1  &
   center_marker = .template_2_retract_semirocker.ges_dragbrace.gralin_1  &
   angle_extent = 360.0  &
   length = 1097.7473622179  &
   radius = 50.8  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract_semirocker.ges_dragbrace.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .template_2_retract_semirocker.ges_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.ges_upper_cylinder  &
   adams_id = 4  &
   location = 6197.6, 0.0, 1193.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ges_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.cm  &
   adams_id = 17  &
   location = -3.3167643494, 0.0, -13.3824231157  &
   orientation = 90.0d, 2.0673379194d, 270.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.inertia_frame  &
   adams_id = 18  &
   location = -3.3167643494, 0.0, -13.3824231157  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_2  &
   adams_id = 19  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_3  &
   adams_id = 20  &
   location = -116.84, -340.36, -497.84  &
   orientation = 161.0534953105d, 58.7414044414d, 213.4869581747d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_4  &
   adams_id = 21  &
   location = -116.84, 340.36, -497.84  &
   orientation = 18.9465046895d, 58.7414044414d, 326.5130418253d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_11  &
   adams_id = 22  &
   location = 0.0, 0.0, 114.3  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_11  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_i_15  &
   adams_id = 24  &
   location = -116.84, 0.0, -497.84  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_i_15  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_spring_j_1  &
   adams_id = 25  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_spring_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_damper_j_1  &
   adams_id = 26  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_damper_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_stopper_j_1  &
   adams_id = 27  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_stopper_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1  &
   adams_id = 28  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_1  &
   adams_id = 29  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_4  &
   adams_id = 30  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_4  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.MARKER_69  &
   adams_id = 69  &
   location = 0.0, 0.0, -203.2  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.MARKER_97  &
   adams_id = 97  &
   location = -254.0, 0.0, 177.8  &
   orientation = 16.0079658047d, 93.7961313686d, 180.4845927388d
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract_semirocker.ges_upper_cylinder  &
   mass = 82.2524279101  &
   center_of_mass_marker =   &
                           .template_2_retract_semirocker.ges_upper_cylinder.cm  &
   inertia_marker =   &
                    .template_2_retract_semirocker.ges_upper_cylinder.inertia_frame  &
   ixx = 2.7759040478E+06  &
   iyy = 2.6163591859E+06  &
   izz = 8.2729047458E+05  &
   ixy = 0.0  &
   izx = 7.0431892224E+04  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 2  &
   center_marker =   &
                   .template_2_retract_semirocker.ges_upper_cylinder.gralin_2  &
   angle_extent = 360.0  &
   length = 863.6  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 3  &
   center_marker =   &
                   .template_2_retract_semirocker.ges_upper_cylinder.gralin_3  &
   angle_extent = 360.0  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 4  &
   center_marker =   &
                   .template_2_retract_semirocker.ges_upper_cylinder.gralin_4  &
   angle_extent = 360.0  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_2_retract_semirocker.ges_upper_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.ges_lower_cylinder  &
   adams_id = 5  &
   location = 6197.6, 0.0, 952.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ges_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.cm  &
   adams_id = 31  &
   location = 1.1218962957, 0.0, 37.9433699695  &
   orientation = 270.0d, 0.2455310467d, 90.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.inertia_frame  &
   adams_id = 32  &
   location = 1.1218962957, 0.0, 37.9433699695  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.gralin_5  &
   adams_id = 33  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.gralin_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.jxs_joint_i_11  &
   adams_id = 35  &
   location = 0.0, 0.0, -127.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.jxs_joint_i_11  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.ues_spring_i_1  &
   adams_id = 37  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.ues_spring_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.ues_damper_i_1  &
   adams_id = 38  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.ues_damper_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.ues_stopper_i_1  &
   adams_id = 39  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.ues_stopper_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.coomarker_2  &
   adams_id = 40  &
   location = -31.496, 0.0, 444.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.coomarker_2  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.MARKER_70  &
   adams_id = 70  &
   location = 0.0, 0.0, 190.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.MARKER_71  &
   adams_id = 20  &
   location = 176.022, 0.0, 157.48  &
   orientation = 90.0d, 28.3649021228d, 270.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.MARKER_81  &
   adams_id = 81  &
   location = 0.0, 0.0, -4.496  &
   orientation = 180.0d, 90.0d, 0.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.MARKER_82  &
   adams_id = 82  &
   location = 249.999999999, 0.0, 294.5000000006  &
   orientation = 180.0d, 90.0d, 0.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.MARKER_89  &
   adams_id = 89  &
   location = 0.0, 0.0, 474.5  &
   orientation = 180.0d, 90.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract_semirocker.ges_lower_cylinder  &
   mass = 86.3296339065  &
   center_of_mass_marker =   &
                           .template_2_retract_semirocker.ges_lower_cylinder.cm  &
   ixx = 6.8887730894E+06  &
   iyy = 6.5705337651E+06  &
   izz = 8.7046095448E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_lower_cylinder.gralin_geom1  &
   adams_id = 5  &
   center_marker =   &
                   .template_2_retract_semirocker.ges_lower_cylinder.gralin_5  &
   angle_extent = 360.0  &
   length = 919.0  &
   radius = 80.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract_semirocker.ges_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_lower_cylinder.CYLINDER_14  &
   adams_id = 14  &
   center_marker =   &
                   .template_2_retract_semirocker.ges_lower_cylinder.MARKER_71  &
   angle_extent = 360.0  &
   length = 155.7152044084  &
   radius = 25.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_2_retract_semirocker.ges_lower_cylinder.CYLINDER_14  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_2_retract_semirocker.ges_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!-------------------------------- ges_subframe --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.ges_subframe  &
   adams_id = 8  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ges_subframe
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_subframe.cm  &
   adams_id = 52  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_subframe.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_subframe.inertia_frame  &
   adams_id = 53  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_subframe.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_subframe.graout_1  &
   adams_id = 54  &
   location = -390.5595878992, 5.9115906614E-11, -340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_subframe.graout_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_subframe.graout_2  &
   adams_id = 55  &
   location = -390.5595878992, 5.9115906614E-11, 340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_subframe.graout_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_subframe.graout_3  &
   adams_id = 56  &
   location = 781.1191757984, -1.1850243009E-10, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_subframe.graout_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_subframe.jxs_joint_j_15  &
   adams_id = 57  &
   location = -390.5595878992, 5.9115906614E-11, 0.0  &
   orientation = 3.3555200908d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_subframe.jxs_joint_j_15  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_subframe.jxs_joint_i_16  &
   adams_id = 58  &
   location = 0.0, 0.0, 0.0  &
   orientation = 183.3555200908d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_subframe.jxs_joint_i_16  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_subframe.jxs_joint_j_14  &
   adams_id = 59  &
   location = 781.1191757984, -1.1850243009E-10, 0.0  &
   orientation = 3.3555200908d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_subframe.jxs_joint_j_14  &
   visibility = off  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract_semirocker.ges_subframe  &
   mass = 4.5359237E-03  &
   center_of_mass_marker = .template_2_retract_semirocker.ges_subframe.cm  &
   inertia_marker =   &
                    .template_2_retract_semirocker.ges_subframe.inertia_frame  &
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
   outline_name = .template_2_retract_semirocker.ges_subframe.graout_subframe_geom  &
   adams_id = 10  &
   marker_name =  &
      .template_2_retract_semirocker.ges_subframe.graout_1,  &
      .template_2_retract_semirocker.ges_subframe.graout_2,  &
      .template_2_retract_semirocker.ges_subframe.graout_3  &
   visibility_between_markers = on, on, on  &
   close = yes
!
geometry attributes  &
   geometry_name = .template_2_retract_semirocker.ges_subframe.graout_subframe_geom  &
   color = WHITE
!
part attributes  &
   part_name = .template_2_retract_semirocker.ges_subframe  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!------------------------------- mts_body_mount -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.mts_body_mount  &
   adams_id = 9  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.mts_body_mount
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.mts_body_mount.mount_i  &
   adams_id = 60  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.mts_body_mount.mount_i  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16  &
   adams_id = 61  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16  &
   visibility = off  &
   name_visibility = off
!
part attributes  &
   part_name = .template_2_retract_semirocker.mts_body_mount  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- ges_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.ges_collar  &
   adams_id = 10  &
   location = 6197.6, 0.0, 809.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ges_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_collar.cm  &
   adams_id = 63  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_collar.cm  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_collar.inertia_frame  &
   adams_id = 64  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_collar.gralin_24  &
   adams_id = 65  &
   location = 0.0, 0.0, 52.502  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_collar.gralin_24  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_collar.jxs_joint_i_1  &
   adams_id = 66  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_collar.jxs_joint_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_collar.ues_actuator_i_1  &
   adams_id = 67  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_collar.ues_actuator_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_collar.ues_actuator_i_4  &
   adams_id = 68  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_retract_semirocker.ges_collar.ues_actuator_i_4  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_retract_semirocker.ges_collar.MARKER_80  &
   adams_id = 80  &
   location = 0.0, 0.0, 147.498  &
   orientation = 180.0d, 90.0d, 180.0d
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract_semirocker.ges_collar  &
   mass = 6.4242828175  &
   center_of_mass_marker = .template_2_retract_semirocker.ges_collar.cm  &
   inertia_marker = .template_2_retract_semirocker.ges_collar.inertia_frame  &
   ixx = 8.5080541407E+04  &
   iyy = 8.5080541407E+04  &
   izz = 1.4685428308E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_collar.gralin_collar  &
   adams_id = 9  &
   center_marker = .template_2_retract_semirocker.ges_collar.gralin_24  &
   angle_extent = 360.0  &
   length = 94.996  &
   radius = 139.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_retract_semirocker.ges_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .template_2_retract_semirocker.ges_collar  &
   visibility = on  &
   name_visibility = on
!
!---------------------------------- lunzhou -----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.lunzhou  &
   adams_id = 12  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.lunzhou
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_73  &
   adams_id = 73  &
   location = 5947.600000001, -120.0, 657.9999999994  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.lunzhou.cm  &
   adams_id = 78  &
   location = 6210.8434059227, 0.0, 468.4647477354  &
   orientation = 270.0d, 54.2461127455d, 90.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_83  &
   adams_id = 83  &
   location = 5947.600000001, 0.0, 657.9999999994  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_84  &
   adams_id = 84  &
   location = 6197.6, -120.0, 478.0  &
   orientation = 180.0d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_85  &
   adams_id = 85  &
   location = 5947.600000001, -120.0, 657.9999999994  &
   orientation = 90.0d, 125.7538872545d, 0.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_86  &
   adams_id = 86  &
   location = 5947.600000001, 120.0, 657.9999999994  &
   orientation = 90.0d, 125.7538872545d, 0.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_87  &
   adams_id = 87  &
   location = 6434.5206048715, 120.0, 307.4171644918  &
   orientation = 0.0d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_88  &
   adams_id = 88  &
   location = 6197.6, 0.0, 478.0  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_92  &
   adams_id = 92  &
   location = 6434.5206048715, 0.0, 307.4171644918  &
   orientation = 180.0d, 90.0d, 180.0d
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract_semirocker.lunzhou  &
   material_type = .template_2_retract_semirocker.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.lunzhou.CYLINDER_20  &
   adams_id = 20  &
   center_marker = .template_2_retract_semirocker.lunzhou.MARKER_73  &
   angle_extent = 360.0  &
   length = 240.0  &
   radius = 12.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.lunzhou.CYLINDER_21  &
   adams_id = 21  &
   center_marker = .template_2_retract_semirocker.lunzhou.MARKER_84  &
   angle_extent = 360.0  &
   length = 240.0  &
   radius = 12.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.lunzhou.CYLINDER_22  &
   adams_id = 22  &
   center_marker = .template_2_retract_semirocker.lunzhou.MARKER_85  &
   angle_extent = 360.0  &
   length = 600.0  &
   radius = 30.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.lunzhou.CYLINDER_23  &
   adams_id = 23  &
   center_marker = .template_2_retract_semirocker.lunzhou.MARKER_86  &
   angle_extent = 360.0  &
   length = 600.0  &
   radius = 30.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.lunzhou.CYLINDER_24  &
   adams_id = 24  &
   center_marker = .template_2_retract_semirocker.lunzhou.MARKER_87  &
   angle_extent = 360.0  &
   length = 240.0  &
   radius = 24.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_2_retract_semirocker.lunzhou  &
   color = GREEN  &
   name_visibility = off
!
!----------------------------------- luntai -----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.luntai  &
   adams_id = 13  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.luntai
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.luntai.MARKER_90  &
   adams_id = 90  &
   location = 6434.5206048715, -50.0, 307.4171644918  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.luntai.cm  &
   adams_id = 93  &
   location = 6434.5206048715, 0.0, 307.4171644918  &
   orientation = 90.0d, 90.0d, 0.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.luntai.MARKER_91  &
   adams_id = 91  &
   location = 6434.5206048715, 0.0, 307.4171644918  &
   orientation = 180.0d, 90.0d, 180.0d
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract_semirocker.luntai  &
   material_type = .template_2_retract_semirocker.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.luntai.CYLINDER_25  &
   adams_id = 25  &
   center_marker = .template_2_retract_semirocker.luntai.MARKER_90  &
   angle_extent = 360.0  &
   length = 100.0  &
   radius = 220.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_2_retract_semirocker.luntai  &
   color = MAGENTA  &
   name_visibility = off
!
!----------------------------------- sf_rod -----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.sf_rod  &
   adams_id = 14  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.sf_rod
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_retract_semirocker.sf_rod.MARKER_94  &
   adams_id = 94  &
   location = 6451.6, 0.0, 1016.0  &
   orientation = 90.0d, 59.5467760909d, 270.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.sf_rod.cm  &
   adams_id = 99  &
   location = 6796.4172903802, 0.0, 1218.7339050452  &
   orientation = 270.0d, 120.4532239091d, 90.0d
!
marker create  &
   marker_name = .template_2_retract_semirocker.sf_rod.MARKER_96  &
   adams_id = 96  &
   location = 6967.855, 0.0, 1319.53  &
   orientation = 270.0d, 120.4532239091d, 292.2692735065d
!
marker create  &
   marker_name = .template_2_retract_semirocker.sf_rod.MARKER_98  &
   adams_id = 98  &
   location = 6451.6, 0.0, 1016.0  &
   orientation = 343.9920341953d, 86.2038686314d, 0.4845927388d
!
part create rigid_body mass_properties  &
   part_name = .template_2_retract_semirocker.sf_rod  &
   material_type = .template_2_retract_semirocker.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.sf_rod.CYLINDER_26  &
   adams_id = 26  &
   center_marker = .template_2_retract_semirocker.sf_rod.MARKER_94  &
   angle_extent = 360.0  &
   length = 800.0  &
   radius = 30.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_2_retract_semirocker.sf_rod  &
   color = RED  &
   name_visibility = off
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint cylindrical  &
   joint_name = .template_2_retract_semirocker.joscyl_lc_uc_joint  &
   adams_id = 5  &
   i_marker_name =   &
                   .template_2_retract_semirocker.ges_lower_cylinder.jxs_joint_i_11  &
   j_marker_name =   &
                   .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_11
!
constraint create joint revolute  &
   joint_name = .template_2_retract_semirocker.josrev_uc_sf_joint  &
   adams_id = 7  &
   i_marker_name =   &
                   .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_i_15  &
   j_marker_name =   &
                   .template_2_retract_semirocker.ges_subframe.jxs_joint_j_15
!
constraint create joint fixed  &
   joint_name = .template_2_retract_semirocker.mts_fixed_2  &
   adams_id = 8  &
   i_marker_name = .template_2_retract_semirocker.mts_body_mount.mount_i  &
   j_marker_name = .template_2_retract_semirocker.ground.mts_mount_j_2
!
constraint attributes  &
   constraint_name = .template_2_retract_semirocker.mts_fixed_2  &
   visibility = off  &
   name_visibility = off
!
constraint create joint fixed  &
   joint_name = .template_2_retract_semirocker.josfix_subframe_to_body  &
   adams_id = 9  &
   i_marker_name =   &
                   .template_2_retract_semirocker.ges_subframe.jxs_joint_i_16  &
   j_marker_name =   &
                   .template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16
!
constraint create joint cylindrical  &
   joint_name = .template_2_retract_semirocker.joscyl_db_sf  &
   adams_id = 10  &
   i_marker_name =   &
                   .template_2_retract_semirocker.ges_dragbrace.jxs_joint_i_14  &
   j_marker_name =   &
                   .template_2_retract_semirocker.ges_subframe.jxs_joint_j_14
!
constraint create joint revolute  &
   joint_name = .template_2_retract_semirocker.josrev_collar_uc_joint  &
   adams_id = 11  &
   i_marker_name = .template_2_retract_semirocker.ges_collar.jxs_joint_i_1  &
   j_marker_name =   &
                   .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1
!
constraint create joint fixed  &
   joint_name = .template_2_retract_semirocker.JOINT_12  &
   adams_id = 12  &
   i_marker_name = .template_2_retract_semirocker.ges_collar.MARKER_80  &
   j_marker_name =   &
                   .template_2_retract_semirocker.ges_lower_cylinder.MARKER_81
!
constraint attributes  &
   constraint_name = .template_2_retract_semirocker.JOINT_12  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_2_retract_semirocker.JOINT_13  &
   adams_id = 13  &
   i_marker_name =   &
                   .template_2_retract_semirocker.ges_lower_cylinder.MARKER_82  &
   j_marker_name = .template_2_retract_semirocker.lunzhou.MARKER_83
!
constraint attributes  &
   constraint_name = .template_2_retract_semirocker.JOINT_13  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_2_retract_semirocker.JOINT_14  &
   adams_id = 14  &
   i_marker_name = .template_2_retract_semirocker.lunzhou.MARKER_88  &
   j_marker_name =   &
                   .template_2_retract_semirocker.ges_lower_cylinder.MARKER_89
!
constraint attributes  &
   constraint_name = .template_2_retract_semirocker.JOINT_14  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_2_retract_semirocker.JOINT_15  &
   adams_id = 15  &
   i_marker_name = .template_2_retract_semirocker.luntai.MARKER_91  &
   j_marker_name = .template_2_retract_semirocker.lunzhou.MARKER_92
!
constraint attributes  &
   constraint_name = .template_2_retract_semirocker.JOINT_15  &
   name_visibility = off
!
constraint create joint translational  &
   joint_name = .template_2_retract_semirocker.JOINT_16  &
   adams_id = 16  &
   i_marker_name = .template_2_retract_semirocker.ges_dragbrace.MARKER_95  &
   j_marker_name = .template_2_retract_semirocker.sf_rod.MARKER_96
!
constraint attributes  &
   constraint_name = .template_2_retract_semirocker.JOINT_16  &
   name_visibility = off
!
constraint create joint spherical  &
   joint_name = .template_2_retract_semirocker.JOINT_17  &
   adams_id = 17  &
   i_marker_name =   &
                   .template_2_retract_semirocker.ges_upper_cylinder.MARKER_97  &
   j_marker_name = .template_2_retract_semirocker.sf_rod.MARKER_98
!
constraint attributes  &
   constraint_name = .template_2_retract_semirocker.JOINT_17  &
   name_visibility = off
!
!----------------------------------- Forces -----------------------------------!
!
!
force create direct single_component_force  &
   single_component_force_name = .template_2_retract_semirocker.SFORCE_1  &
   adams_id = 1  &
   type_of_freedom = translational  &
   i_marker_name =   &
                   .template_2_retract_semirocker.ges_upper_cylinder.MARKER_69  &
   j_marker_name =   &
                   .template_2_retract_semirocker.ges_lower_cylinder.MARKER_70  &
   action_only = off  &
   function = ""
!
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .template_2_retract_semirocker.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=5.0 number_of_steps=500 model_name=._AA_nlg_post_2hubs"
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
geometry create shape force  &
   force_name = .template_2_retract_semirocker.SFORCE_1_force_graphic_1  &
   adams_id = 11  &
   force_element_name = .template_2_retract_semirocker.SFORCE_1  &
   applied_at_marker_name =   &
                            .template_2_retract_semirocker.ges_upper_cylinder.MARKER_69
!
!---------------------------------- Motions -----------------------------------!
!
!
constraint create motion_generator  &
   motion_name = .template_2_retract_semirocker.MOTION_1  &
   adams_id = 1  &
   type_of_freedom = translational  &
   joint_name = .template_2_retract_semirocker.JOINT_16  &
   function = ""
!
constraint attributes  &
   constraint_name = .template_2_retract_semirocker.MOTION_1  &
   name_visibility = off
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   z_component_gravity = -9809.9999999989
!
force attributes  &
   force_name = .template_2_retract_semirocker.gravity  &
   size_of_icons = 50.8
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_2_retract_semirocker.mts_body_mount.minor_role  &
   string_value = "inherit"
!
!---------------------------- Function definitions ----------------------------!
!
!
constraint modify motion_generator  &
   motion_name = .template_2_retract_semirocker.MOTION_1  &
   function = "STEP( time , 0 , 0 , 1 , -635 )-STEP( time , 2 , 0 , 3, -635 )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_2_retract_semirocker.SFORCE_1  &
   function = "-100.0*(DM(.template_2_retract_semirocker.ges_upper_cylinder.MARKER_69,.template_2_retract_semirocker.ges_lower_cylinder.MARKER_70)-25.0)-10.0*VR(.template_2_retract_semirocker.ges_upper_cylinder.MARKER_69,.template_2_retract_semirocker.ges_lower_cylinder.MARKER_70)"
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ground.mts_mount_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.mts_body_mount))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.mts_body_mount))
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_2_retract_semirocker.ground.hps_uc_bot, .template_2_retract_semirocker.ground.hps_uc_top, 0.11 * DM(.template_2_retract_semirocker.ground.hps_uc_bot, .template_2_retract_semirocker.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_uc_bot, .template_2_retract_semirocker.ground.hps_uc_top, "Z"))
!
material modify  &
   material_name = .template_2_retract_semirocker.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_dragbrace))  &
   relative_to = .template_2_retract_semirocker.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_db_sf_atch, .template_2_retract_semirocker.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .template_2_retract_semirocker.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_dragbrace.jxs_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_subframe.jxs_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_subframe.jxs_joint_j_14))  &
   relative_to = .template_2_retract_semirocker.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_dragbrace.gralin_dragbrace_geom  &
   length = (DM(.template_2_retract_semirocker.ground.hps_db_sf_atch, .template_2_retract_semirocker.ground.hps_db_uc_atch) - 100)
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_uc_top, .template_2_retract_semirocker.ground.hps_uc_bot, "Z"))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_uc_sf_atch_l, .template_2_retract_semirocker.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_uc_sf_atch_r, .template_2_retract_semirocker.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_i_15  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_subframe.jxs_joint_j_15))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_subframe.jxs_joint_j_15))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_uc_top))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_uc_top))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_uc_top))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract_semirocker.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_uc_bot, .template_2_retract_semirocker.ground.hps_uc_top, "Z"))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.template_2_retract_semirocker.ground.hps_uc_top, .template_2_retract_semirocker.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.template_2_retract_semirocker.ground.hps_uc_sf_atch_l, .template_2_retract_semirocker.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.template_2_retract_semirocker.ground.hps_uc_sf_atch_r, .template_2_retract_semirocker.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.MARKER_69  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_lc_top))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_upper_cylinder.MARKER_97  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_db_uc_atch))  &
   relative_to = .template_2_retract_semirocker.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_lower_cylinder))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_lc_top, .template_2_retract_semirocker.ground.hps_lc_bot, "Z"))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.ues_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_lc_top))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.ues_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_lc_top))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.ues_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_lc_top))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.coomarker_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.cfs_wheel_centers_midpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.cfs_wheel_centers_midpoint))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_lower_cylinder.gralin_geom1  &
   length = (DM(.template_2_retract_semirocker.ground.hps_lc_top, .template_2_retract_semirocker.ground.hps_lc_bot) + 30)
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.MARKER_70  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_uc_bot))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.MARKER_71  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_lb_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_lb_uc_atch, .template_2_retract_semirocker.ground.POINT_12, "Z"))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_lower_cylinder.CYLINDER_14  &
   length = (6.1305198586inch)
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.MARKER_82  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.POINT_12))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_lower_cylinder.MARKER_89  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.POINT_27))  &
   relative_to = .template_2_retract_semirocker.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_subframe.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_subframe.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_subframe))  &
   relative_to = .template_2_retract_semirocker.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_subframe.graout_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_uc_sf_atch_r))  &
   relative_to = .template_2_retract_semirocker.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_subframe.graout_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_uc_sf_atch_l))  &
   relative_to = .template_2_retract_semirocker.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_subframe.graout_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_db_sf_atch))  &
   relative_to = .template_2_retract_semirocker.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_subframe.jxs_joint_j_15  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract_semirocker.ground.cfs_uc_sf_atch_mid))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_2_retract_semirocker.ground.cfs_uc_sf_atch_mid, "Z+Z"), .template_2_retract_semirocker.ges_subframe))  &
   relative_to = .template_2_retract_semirocker.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_subframe.jxs_joint_i_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16))  &
   relative_to = .template_2_retract_semirocker.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_subframe.jxs_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract_semirocker.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_2_retract_semirocker.ground.origo))  &
   relative_to = .template_2_retract_semirocker.ges_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_retract_semirocker.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_2_retract_semirocker.ground.origo))  &
   relative_to = .template_2_retract_semirocker.mts_body_mount
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
part modify rigid_body name_and_position  &
   part_name = .template_2_retract_semirocker.mts_body_mount  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.origo))
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_collar))  &
   relative_to = .template_2_retract_semirocker.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_collar.gralin_24  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_uc_bot, .template_2_retract_semirocker.ground.cfs_collar_top, "Z"))  &
   relative_to = .template_2_retract_semirocker.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_2_retract_semirocker.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_collar.ues_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_2_retract_semirocker.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.ges_collar.ues_actuator_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_2_retract_semirocker.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.ges_collar.gralin_collar  &
   length = (DM(.template_2_retract_semirocker.ground.hps_uc_bot, .template_2_retract_semirocker.ground.cfs_collar_top))
!
geometry modify shape force  &
   force_name = .template_2_retract_semirocker.SFORCE_1_force_graphic_1  &
   applied_at_marker_name = (.template_2_retract_semirocker.SFORCE_1.i)
!
marker modify  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_73  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.POINT))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.POINT, .template_2_retract_semirocker.ground.POINT_2, "Z"))  &
   relative_to = .template_2_retract_semirocker.lunzhou
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_83  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.POINT_12))  &
   relative_to = .template_2_retract_semirocker.lunzhou
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_85  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.POINT))  &
   relative_to = .template_2_retract_semirocker.lunzhou
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_retract_semirocker.lunzhou.CYLINDER_24  &
   length = (240.0mm)
!
marker modify  &
   marker_name = .template_2_retract_semirocker.lunzhou.MARKER_88  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.POINT_27))  &
   relative_to = .template_2_retract_semirocker.lunzhou
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.sf_rod.MARKER_94  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_db_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_retract_semirocker.ground.hps_db_uc_atch, .template_2_retract_semirocker.ground.hps_db_sf_atch, "Z"))  &
   relative_to = .template_2_retract_semirocker.sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
marker modify  &
   marker_name = .template_2_retract_semirocker.sf_rod.MARKER_98  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_retract_semirocker.ground.hps_db_uc_atch))  &
   relative_to = .template_2_retract_semirocker.sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_retract_semirocker.ground
!
material modify  &
   material_name = .template_2_retract_semirocker.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
model display  &
   model_name = template_2_retract_semirocker

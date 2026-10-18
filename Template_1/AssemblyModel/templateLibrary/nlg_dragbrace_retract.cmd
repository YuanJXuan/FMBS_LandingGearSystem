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
   model_name = retract  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .retract  &
   size_of_icons = 50.8
!
view erase
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .retract.steel  &
   adams_id = 2  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .retract.aluminum  &
   adams_id = 3  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .retract.steel_2  &
   adams_id = 1  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .retract.aluminum_2  &
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
   default_coordinate_system = .retract.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .retract.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .retract.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .retract.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .retract.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .retract.ground.hps_rod_bot  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point create  &
   point_name = .retract.ground.hps_rod_top  &
   location = 7227.4389033572, 0.0, 1472.1512863532
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .retract.ground  &
   size_of_icons = 50.8
!
!------------------------------ ges_sf_actuator -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .retract.ground
!
part create rigid_body name_and_position  &
   part_name = .retract.ges_sf_actuator  &
   adams_id = 7  &
   location = 6967.855, 0.0, 1319.53  &
   orientation = 270.0000000009d, 120.4532239116d, 90.0000000003d
!
defaults coordinate_system  &
   default_coordinate_system = .retract.ges_sf_actuator
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .retract.ges_sf_actuator.cm  &
   adams_id = 21  &
   location = -2.6589288646E-08, -8.1094015533E-09, -25.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_actuator.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .retract.ges_sf_actuator.inertia_frame  &
   adams_id = 22  &
   location = -2.6588904689E-08, -8.1094015533E-09, -25.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_actuator.inertia_frame  &
   visibility = on  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .retract.ges_sf_actuator.gralin_1  &
   adams_id = 23  &
   location = -2.6589286328E-08, -8.1094057298E-09, -598.873681109  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_actuator.gralin_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .retract.ges_sf_actuator.stopper_actuator  &
   adams_id = 87  &
   location = 2.2026824809E-09, 0.0, 618.8736811067  &
   orientation = 90.0000000003d, 120.4532239116d, 270.0000000009d
!
marker attributes  &
   marker_name = .retract.ges_sf_actuator.stopper_actuator  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_actuator.MARKER_85  &
   adams_id = 85  &
   location = 1.3451462166E-09, 0.0, 158.8736811071  &
   orientation = 90.0000000003d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_actuator.MARKER_85  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_actuator.MARKER_89  &
   adams_id = 89  &
   location = 2.2026824809E-09, 0.0, 618.8736811067  &
   orientation = 90.0000000003d, 120.4532239116d, 270.0000000009d
!
marker attributes  &
   marker_name = .retract.ges_sf_actuator.MARKER_89  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_actuator.MARKER_97  &
   adams_id = 97  &
   location = -4.5918824298E-10, 0.0, -598.873681109  &
   orientation = 90.0000000003d, 120.4532239116d, 270.0000000009d
!
marker attributes  &
   marker_name = .retract.ges_sf_actuator.MARKER_97  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_actuator.MARKER_100  &
   adams_id = 100  &
   location = 2.2026824809E-09, 0.0, 618.8736811067  &
   orientation = 90.0000000003d, 120.4532239116d, 270.0000000009d
!
marker attributes  &
   marker_name = .retract.ges_sf_actuator.MARKER_100  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .retract.ges_sf_actuator  &
   material_type = .retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .retract.ges_sf_actuator.gralin_dragbrace_geom  &
   adams_id = 32  &
   center_marker = .retract.ges_sf_actuator.gralin_1  &
   angle_extent = 360.0000000012  &
   length = 1147.7473622179  &
   radius = 50.8  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .retract.ges_sf_actuator.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .retract.ges_sf_actuator  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!--------------------------------- ges_sf_rod ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .retract.ground
!
part create rigid_body name_and_position  &
   part_name = .retract.ges_sf_rod  &
   adams_id = 5  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .retract.ges_sf_rod
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .retract.ges_sf_rod.MARKER_stopper_rod  &
   adams_id = 86  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_rod.MARKER_stopper_rod  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_rod.gralin_25  &
   adams_id = 3  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.5467760909d, 270.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_rod.gralin_25  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_rod.cm  &
   adams_id = 76  &
   location = 6830.8990194193, 0.0, 1239.0072955524  &
   orientation = 90.0d, 59.5467760909d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_rod.cm  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_rod.MARKER_84  &
   adams_id = 84  &
   location = 6830.8990194192, 0.0, 1239.0072955517  &
   orientation = 90.0000000003d, 59.5467760889d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_rod.MARKER_84  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_rod.MARKER_88  &
   adams_id = 88  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_rod.MARKER_88  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_rod.MARKER_96  &
   adams_id = 96  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_rod.MARKER_96  &
   visibility = on
!
marker create  &
   marker_name = .retract.ges_sf_rod.MARKER_101  &
   adams_id = 101  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .retract.ges_sf_rod.MARKER_101  &
   visibility = on
!
part create rigid_body mass_properties  &
   part_name = .retract.ges_sf_rod  &
   material_type = .retract.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .retract.ges_sf_rod.CYLINDER_30  &
   adams_id = 30  &
   center_marker = .retract.ges_sf_rod.gralin_25  &
   angle_extent = 360.0000000012  &
   length = 920.0  &
   radius = 27.5  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .retract.ges_sf_rod  &
   color = RED  &
   name_visibility = off
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint cylindrical  &
   joint_name = .retract.joscly_ac_rd  &
   adams_id = 13  &
   i_marker_name = .retract.ges_sf_rod.MARKER_84  &
   j_marker_name = .retract.ges_sf_actuator.MARKER_85
!
constraint attributes  &
   constraint_name = .retract.joscly_ac_rd  &
   visibility = on  &
   name_visibility = off
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
material modify  &
   material_name = .retract.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .retract.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .retract.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .retract.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .retract.ges_sf_actuator.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .retract.ges_sf_actuator.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .retract.ges_sf_actuator))  &
   relative_to = .retract.ges_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .retract.ground
!
marker modify  &
   marker_name = .retract.ges_sf_actuator.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .retract.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.retract.ground.hps_db_sf_atch, .retract.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .retract.ges_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .retract.ges_sf_actuator.gralin_dragbrace_geom  &
   length = (DM(.retract.ground.hps_db_sf_atch, .retract.ground.hps_db_uc_atch) - 50)
!
marker modify  &
   marker_name = .retract.ges_sf_rod.gralin_25  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}, .retract.ground.hps_rod_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.retract.ground.hps_db_uc_atch, .retract.ground.hps_db_sf_atch, "Z"))  &
   relative_to = .retract.ges_sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .retract.ground
!
geometry modify shape cylinder  &
   cylinder_name = .retract.ges_sf_rod.CYLINDER_30  &
   length = (DM(.retract.ground.hps_rod_bot, .retract.ground.hps_rod_top))  &
   radius = (27.5mm)
!
model display  &
   model_name = retract

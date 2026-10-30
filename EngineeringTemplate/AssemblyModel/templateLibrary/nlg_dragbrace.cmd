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
! ****** Points for current part ******
!
point create  &
   point_name = .turn.ground.hps_db_sf_atch  &
   location = 7.48411, 0.0, 1.62306
!
point attributes  &
   point_name = .turn.ground.hps_db_sf_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .turn.ground.hps_db_uc_atch  &
   location = 6.4516, 0.0, 1.016
!
point attributes  &
   point_name = .turn.ground.hps_db_uc_atch  &
   size_of_icons = 5.0E-02
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .turn.ground  &
   size_of_icons = 5.0E-02
!
!------------------------------- ges_dragbrace --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.ges_dragbrace  &
   adams_id = 33  &
   location = 6.967855, 0.0, 1.31953  &
   orientation = 270.0d, 120.4532239091d, 90.0d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ges_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.ges_dragbrace.cm  &
   adams_id = 301  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_dragbrace.cm  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_dragbrace.inertia_frame  &
   adams_id = 302  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_dragbrace.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .turn.ges_dragbrace.gralin_1  &
   adams_id = 303  &
   location = 0.0, 0.0, -0.5988736811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .turn.ges_dragbrace.gralin_1  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .turn.ges_dragbrace  &
   mass = 27.3726690382  &
   center_of_mass_marker = .turn.ges_dragbrace.cm  &
   inertia_marker = .turn.ges_dragbrace.inertia_frame  &
   ixx = 3.4811540175  &
   iyy = 3.4811540175  &
   izz = 3.5319502313E-02  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.ges_dragbrace.gralin_dragbrace_geom  &
   adams_id = 85  &
   center_marker = .turn.ges_dragbrace.gralin_1  &
   angle_extent = 360.0  &
   length = 1.1977473622  &
   radius = 5.08E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .turn.ges_dragbrace.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .turn.ges_dragbrace  &
   visibility = on  &
   name_visibility = on  &
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
   marker_name = .turn.ges_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ges_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .turn.ges_dragbrace))  &
   relative_to = .turn.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.ges_dragbrace.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hps_db_sf_atch, .turn.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .turn.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.ges_dragbrace.gralin_dragbrace_geom  &
   length = (DM(.turn.ground.hps_db_sf_atch, .turn.ground.hps_db_uc_atch))
!
model display  &
   model_name = turn

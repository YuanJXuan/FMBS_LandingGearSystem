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
   marker_name = .turn.ground.zdt_1  &
   adams_id = 461  &
   location = 5.9187250255, 1.25840225E-02, 0.8  &
   orientation = 303.9027984088d, 90.0d, 90.0d
!
marker create  &
   marker_name = .turn.ground.zdt_2  &
   adams_id = 462  &
   location = 5.7792875383, -8.112396625E-02, 0.8  &
   orientation = 303.9027984088d, 90.0d, 90.0d
!
! ****** Points for current part ******
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
!------------------------------------ hsg -------------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.hsg  &
   adams_id = 47  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.hsg
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.hsg.gralin_463  &
   adams_id = 463  &
   location = 6.1976, 0.2, 0.8  &
   orientation = 303.9027984088d, 90.0d, 90.0d
!
marker create  &
   marker_name = .turn.hsg.cm  &
   adams_id = 473  &
   location = 5.965204188, 4.382001875E-02, 0.8  &
   orientation = 303.9027984088d, 90.0d, 89.8631118907d
!
marker create  &
   marker_name = .turn.hsg.MARKER_469  &
   adams_id = 469  &
   location = 5.8490062819, -3.4269971868E-02, 0.8  &
   orientation = 303.9027984088d, 90.0d, 90.0d
!
part create rigid_body mass_properties  &
   part_name = .turn.hsg  &
   material_type = .turn.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.hsg.CYLINDER_213  &
   adams_id = 213  &
   center_marker = .turn.hsg.gralin_463  &
   angle_extent = 360.0  &
   length = 0.56  &
   radius = 2.2E-02  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .turn.hsg  &
   color = RED  &
   name_visibility = off
!
!------------------------------------ zdt -------------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
part create rigid_body name_and_position  &
   part_name = .turn.zdt  &
   adams_id = 48  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .turn.zdt
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .turn.zdt.gralin_464  &
   adams_id = 464  &
   location = 5.9187250255, 1.25840225E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 0.0d
!
marker create  &
   marker_name = .turn.zdt.cm  &
   adams_id = 474  &
   location = 5.8490062819, -3.4269971868E-02, 0.8  &
   orientation = 123.9027984031d, 90.0d, 34.4641635531d
!
marker create  &
   marker_name = .turn.zdt.MARKER_470  &
   adams_id = 470  &
   location = 5.8490062819, -3.4269971868E-02, 0.8  &
   orientation = 303.9027984088d, 90.0d, 90.0d
!
part create rigid_body mass_properties  &
   part_name = .turn.zdt  &
   material_type = .turn.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .turn.zdt.CYLINDER_214  &
   adams_id = 214  &
   center_marker = .turn.zdt.gralin_464  &
   angle_extent = 360.0  &
   length = 0.168  &
   radius = 4.2E-02  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .turn.zdt  &
   color = GREEN  &
   name_visibility = off
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint translational  &
   joint_name = .turn.hsg_zdt  &
   adams_id = 66  &
   i_marker_name = .turn.hsg.MARKER_469  &
   j_marker_name = .turn.zdt.MARKER_470
!
constraint attributes  &
   constraint_name = .turn.hsg_zdt  &
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
marker modify  &
   marker_name = .turn.ground.zdt_1  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hsg_1, .turn.ground.hsg_2, 0.6 * DM(.turn.ground.hsg_1, .turn.ground.hsg_2)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hsg_1, .turn.ground.hsg_2, "Z"))
!
marker modify  &
   marker_name = .turn.ground.zdt_2  &
   location =   &
      (LOC_ALONG_LINE(.turn.ground.hsg_1, .turn.ground.hsg_2, 0.9 * DM(.turn.ground.hsg_1, .turn.ground.hsg_2)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hsg_1, .turn.ground.hsg_2, "Z"))
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
   marker_name = .turn.hsg.gralin_463  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.hsg_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hsg_1, .turn.ground.hsg_2, "Z"))  &
   relative_to = .turn.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.hsg.MARKER_469  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.zdt.cm))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hsg_1, .turn.ground.zdt_1, "Z"))  &
   relative_to = .turn.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.hsg.CYLINDER_213  &
   length = (DM(.turn.ground.hsg_1, .turn.ground.hsg_2))  &
   radius = (2.2E-02meter)
!
marker modify  &
   marker_name = .turn.zdt.gralin_464  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.ground.zdt_1))  &
   relative_to = .turn.zdt
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
marker modify  &
   marker_name = .turn.zdt.MARKER_470  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .turn.zdt.cm))  &
   orientation =   &
      (ORI_ALONG_AXIS(.turn.ground.hsg_1, .turn.ground.zdt_1, "Z"))  &
   relative_to = .turn.zdt
!
defaults coordinate_system  &
   default_coordinate_system = .turn.ground
!
geometry modify shape cylinder  &
   cylinder_name = .turn.zdt.CYLINDER_214  &
   length = (DM(.turn.ground.zdt_1, .turn.ground.zdt_2))  &
   radius = (4.2E-02meter)
!
model display  &
   model_name = turn

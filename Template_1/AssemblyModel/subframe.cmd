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
   model_name = Unknown  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .Unknown  &
   size_of_icons = 5.0E-02
!
view erase
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .Unknown.aluminum  &
   adams_id = 2  &
   density = 2740.0  &
   youngs_modulus = 7.1705E+10  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .Unknown.steel  &
   adams_id = 5  &
   density = 7801.0  &
   youngs_modulus = 2.07E+11  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .Unknown.steel_2  &
   adams_id = 3  &
   density = 7801.0  &
   youngs_modulus = 2.07E+11  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .Unknown.aluminum_2  &
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
   default_coordinate_system = .Unknown.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .Unknown.ground.origo  &
   adams_id = 1  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .Unknown.ground.origo  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
part attributes  &
   part_name = .Unknown.ground  &
   size_of_icons = 5.0E-02
!
!---------------------------------- PART_46 -----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .Unknown.ground
!
part create rigid_body name_and_position  &
   part_name = .Unknown.PART_46  &
   adams_id = 46  &
   location = -0.92679, 0.0, 0.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .Unknown.PART_46
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .Unknown.PART_46.MARKER_433  &
   adams_id = 433  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .Unknown.PART_46.MARKER_433  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .Unknown.PART_46.cm  &
   adams_id = 438  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .Unknown.PART_46.cm  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .Unknown.PART_46  &
   mass = 3.4246223935E+04  &
   center_of_mass_marker = .Unknown.PART_46.cm  &
   ixx = 1.307070096E+05  &
   iyy = 2.307070095E+05  &
   izz = 1.307070095E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape ellipsoid  &
   ellipsoid_name = .Unknown.PART_46.ELLIPSOID_156  &
   adams_id = 150  &
   center_marker = .Unknown.PART_46.MARKER_433  &
   x_scale_factor = 0.2  &
   y_scale_factor = 0.2  &
   z_scale_factor = 0.2
!
part attributes  &
   part_name = .Unknown.PART_46  &
   color = GREEN  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
!---------------------------------- _cv_part ----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .Unknown.ground
!
part create rigid_body name_and_position  &
   part_name = .Unknown._cv_part  &
   adams_id = 2  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .Unknown._cv_part
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .Unknown._cv_part.marker  &
   adams_id = 300  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .Unknown._cv_part.marker  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .Unknown._cv_part  &
   mass = 0.0  &
   center_of_mass_marker = .Unknown._cv_part.marker  &
   ixx = 0.0  &
   iyy = 0.0  &
   izz = 0.0  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
part attributes  &
   part_name = .Unknown._cv_part  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
!----------------------------------- Forces -----------------------------------!
!
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   z_component_gravity = -9.81
!
force attributes  &
   force_name = .Unknown.gravity  &
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
   material_name = .Unknown.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .Unknown.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .Unknown.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .Unknown.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
geometry modify shape ellipsoid  &
   ellipsoid_name = .Unknown.PART_46.ELLIPSOID_156  &
   x_scale_factor = (2 * 10.0cm)  &
   y_scale_factor = (2 * 10.0cm)  &
   z_scale_factor = (2 * 10.0cm)
!
model display  &
   model_name = Unknown

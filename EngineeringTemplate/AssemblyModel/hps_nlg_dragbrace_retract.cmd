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
   model_name = Unknown  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .Unknown  &
   size_of_icons = 50.8
!
view erase
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .Unknown.steel  &
   adams_id = 2  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .Unknown.aluminum  &
   adams_id = 3  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .Unknown.steel_2  &
   adams_id = 1  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .Unknown.aluminum_2  &
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
   default_coordinate_system = .Unknown.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .Unknown.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .Unknown.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .Unknown.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .Unknown.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .Unknown.ground.hps_rod_bot  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point create  &
   point_name = .Unknown.ground.hps_rod_top  &
   location = 7227.4389033572, 0.0, 1472.1512863532
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .Unknown.ground  &
   size_of_icons = 50.8
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
   material_name = .Unknown.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .Unknown.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
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
model display  &
   model_name = Unknown

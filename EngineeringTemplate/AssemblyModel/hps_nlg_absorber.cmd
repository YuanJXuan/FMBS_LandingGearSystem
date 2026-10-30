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
! ****** Points for current part ******
!
point create  &
   point_name = .Unknown.ground.hps_uc_sf_atch_l  &
   location = 6.31444, -0.34036, 1.69164
!
point attributes  &
   point_name = .Unknown.ground.hps_uc_sf_atch_l  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_uc_sf_atch_r  &
   location = 6.31444, 0.34036, 1.69164
!
point attributes  &
   point_name = .Unknown.ground.hps_uc_sf_atch_r  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_lc_bot  &
   location = 6.1976, 0.0, 0.308
!
point attributes  &
   point_name = .Unknown.ground.hps_lc_bot  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_uc_top  &
   location = 6.1976, 0.0, 1.6256
!
point attributes  &
   point_name = .Unknown.ground.hps_uc_top  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_uta_uc_atch  &
   location = 6.3246, 0.0, 0.8382
!
point attributes  &
   point_name = .Unknown.ground.hps_uta_uc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_lta_lc_atch  &
   location = 6.2992, 0.0, 0.3334
!
point attributes  &
   point_name = .Unknown.ground.hps_lta_lc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_lta_uta_atch  &
   location = 6.6548, 0.0, 0.6112
!
point attributes  &
   point_name = .Unknown.ground.hps_lta_uta_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_uc_geompt  &
   location = 6.1976, 0.0, 1.4732
!
point attributes  &
   point_name = .Unknown.ground.hps_uc_geompt  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_uc_bot  &
   location = 6.1976, 0.0, 0.762
!
point attributes  &
   point_name = .Unknown.ground.hps_uc_bot  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_lc_top  &
   location = 6.1976, 0.0, 1.197
!
point attributes  &
   point_name = .Unknown.ground.hps_lc_top  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_origin_reference  &
   location = 0.0, 0.0, 0.0
!
point attributes  &
   point_name = .Unknown.ground.hps_origin_reference  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_lb_uc_atch  &
   location = 6.021578, 0.0, 0.79502
!
point attributes  &
   point_name = .Unknown.ground.hps_lb_uc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_wheel_center1  &
   location = 6.229096, -0.20955, 0.308
!
point attributes  &
   point_name = .Unknown.ground.hpl_wheel_center1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_wheel_center1  &
   location = 6.229096, 0.20955, 0.308
!
point attributes  &
   point_name = .Unknown.ground.hpr_wheel_center1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_ob_axle1  &
   location = 6.229096, -0.28575, 0.308
!
point attributes  &
   point_name = .Unknown.ground.hpl_ob_axle1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_ob_axle1  &
   location = 6.229096, 0.28575, 0.308
!
point attributes  &
   point_name = .Unknown.ground.hpr_ob_axle1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hps_nlg_axle_lowpoint  &
   location = 6.229096, 0.0, 0.4826
!
point attributes  &
   point_name = .Unknown.ground.hps_nlg_axle_lowpoint  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hsg_1  &
   location = 6.1976, 0.2, 0.8
!
point create  &
   point_name = .Unknown.ground.hsg_2  &
   location = 5.7328083759, -0.1123599625, 0.8
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .Unknown.ground  &
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
model display  &
   model_name = Unknown

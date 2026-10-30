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
   icon_visibility = off  &
   grid_visibility = off  &
   size_of_icons = 25.4  &
   spacing_for_grid = 25.4
!
!------------------------------ Adams View Model ------------------------------!
!
!
model create  &
   model_name = template_2_turn  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_2_turn  &
   size_of_icons = 50.8
!
view erase
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
   default_coordinate_system = .template_2_turn.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_2_turn.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_2_turn.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_2_turn.ground.hps_uc_sf_atch_l  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_2_turn.ground.hps_uc_sf_atch_r  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_2_turn.ground.hps_lc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_2_turn.ground.hps_uc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_2_turn.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_uta_uc_atch  &
   location = 6324.6, 0.0, 838.2
!
point attributes  &
   point_name = .template_2_turn.ground.hps_uta_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_lta_lc_atch  &
   location = 6299.2, 0.0, 533.4
!
point attributes  &
   point_name = .template_2_turn.ground.hps_lta_lc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_lta_uta_atch  &
   location = 6654.8, 0.0, 711.2
!
point attributes  &
   point_name = .template_2_turn.ground.hps_lta_uta_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_2_turn.ground.hps_uc_geompt  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_2_turn.ground.hps_uc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_2_turn.ground.hps_lc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_origin_reference  &
   location = 0.0, 0.0, 0.0
!
point attributes  &
   point_name = .template_2_turn.ground.hps_origin_reference  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_turn.ground.hps_lb_uc_atch  &
   location = 6021.578, 0.0, 795.02
!
point create  &
   point_name = .template_2_turn.ground.hpl_wheel_center  &
   location = 6229.096, -209.55, 508.0
!
point create  &
   point_name = .template_2_turn.ground.hpr_wheel_center  &
   location = 6229.096, 209.55, 508.0
!
point create  &
   point_name = .template_2_turn.ground.hpl_ob_axle  &
   location = 6229.096, -285.75, 508.0
!
point create  &
   point_name = .template_2_turn.ground.hpr_ob_axle  &
   location = 6229.096, 285.75, 508.0
!
point create  &
   point_name = .template_2_turn.ground.hps_nlg_axle_lowpoint  &
   location = 6229.096, 0.0, 482.6
!
point create  &
   point_name = .template_2_turn.ground.hsg_1  &
   location = 6197.6, 200.0, 800.0
!
point create  &
   point_name = .template_2_turn.ground.hsg_2  &
   location = 5732.8083758737, -112.3599624505, 800.0
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_2_turn.ground  &
   size_of_icons = 50.8
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_2_turn.initial_vel  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.0
!
variable create  &
   variable_name = .template_2_turn.stiffness_air  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1000.0
!
variable create  &
   variable_name = .template_2_turn.damping_air  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 10.0
!
variable create  &
   variable_name = .template_2_turn.stiffness_oil  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1000.0
!
variable create  &
   variable_name = .template_2_turn.damping_oil  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 10.0
!
variable create  &
   variable_name = .template_2_turn.stiffness_stop  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1000.0
!
variable create  &
   variable_name = .template_2_turn.damping_stop  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 10.0
!
variable create  &
   variable_name = .template_2_turn.vel  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5000.0
!
variable create  &
   variable_name = .template_2_turn.damping_coefficient  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0E+04
!
variable create  &
   variable_name = .template_2_turn.angle  &
   units = "no_units"  &
   range = -0.1, 0.1  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 30.0
!
variable create  &
   variable_name = .template_2_turn.T_1  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.0
!
variable create  &
   variable_name = .template_2_turn.T_2  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
model display  &
   model_name = template_2_turn

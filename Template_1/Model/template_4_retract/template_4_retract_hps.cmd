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
   size_of_icons = 25.0  &
   spacing_for_grid = 25.4
!
!------------------------------ Adams View Model ------------------------------!
!
!
model create  &
   model_name = template_4_retract  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_4_retract  &
   size_of_icons = 25.0
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
   default_coordinate_system = .template_4_retract.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_4_retract.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_4_retract.ground.hps_db_sf_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_sf_atch_l  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_sf_atch_r  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lc_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_4_retract.ground.hps_db_uc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uta_uc_atch  &
   location = 6324.6, 0.0, 838.2
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uta_uc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lta_lc_atch  &
   location = 6299.2, 0.0, 533.4
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lta_lc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lta_uta_atch  &
   location = 6654.8, 0.0, 711.2
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lta_uta_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_geompt  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_4_retract.ground.hps_uc_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lc_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_aeroforceN  &
   location = 6200.9167643494, 3.3850517933E-11, 1207.1824231157
!
point attributes  &
   point_name = .template_4_retract.ground.hps_aeroforceN  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lb_uc_atch  &
   location = 6021.578, 0.0, 795.02
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lb_uc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hpl_wheel_center  &
   location = 6229.096, -209.55, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hpl_wheel_center  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hpr_wheel_center  &
   location = 6229.096, 209.55, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hpr_wheel_center  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hpl_ob_axle  &
   location = 6229.096, -285.75, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hpl_ob_axle  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hpr_ob_axle  &
   location = 6229.096, 285.75, 508.0
!
point attributes  &
   point_name = .template_4_retract.ground.hpr_ob_axle  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_nlg_axle_lowpoint  &
   location = 6229.096, 0.0, 482.6
!
point attributes  &
   point_name = .template_4_retract.ground.hps_nlg_axle_lowpoint  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_rod_bot  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point attributes  &
   point_name = .template_4_retract.ground.hps_rod_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_rod_top  &
   location = 7227.4389033572, 0.0, 1472.1512863532
!
point attributes  &
   point_name = .template_4_retract.ground.hps_rod_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lockroller_l  &
   location = 6116.051, 50.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lockroller_l  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lockroller_r  &
   location = 6116.051, -50.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lockroller_r  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lockroller_l_2  &
   location = 6051.051, 50.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lockroller_l_2  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.hps_lockroller_r_2  &
   location = 6051.051, -50.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.hps_lockroller_r_2  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_4_retract.ground.suo_qiu_point  &
   location = 6051.051, 0.0, 585.424
!
point attributes  &
   point_name = .template_4_retract.ground.suo_qiu_point  &
   size_of_icons = 25.0
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_4_retract.ground  &
   size_of_icons = 25.0
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_4_retract.AIR_VELOCITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 55.0
!
variable create  &
   variable_name = .template_4_retract.AIR_DENSITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_4_retract.NLG_DRAG_COEFF  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.7
!
variable create  &
   variable_name = .template_4_retract.NLG_PROJ_AREA  &
   units = "area"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.3077
!
variable create  &
   variable_name = .template_4_retract.NLG_RETRACT_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.7E+04
!
variable create  &
   variable_name = .template_4_retract.NLG_RETRACT_RAMP_UP  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_4_retract.NLG_RETRACT_RETRACT_RAMP_DOWN  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_4_retract.NLG_EXTEND_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.2E+04
!
variable create  &
   variable_name = .template_4_retract.NLG_EXTEND_RAMP_UP  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.2
!
variable create  &
   variable_name = .template_4_retract.NLG_ACTUATOR_STROKE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 632.0
!
variable create  &
   variable_name = .template_4_retract.NLG_RETRACT_HOLD_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
variable create  &
   variable_name = .template_4_retract.NLG_EXTEND_HOLD_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.0
!
variable create  &
   variable_name = .template_4_retract.NLG_EXTEND_RETRACT_RETRACT_RAMP_DOWN  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.2
!
model display  &
   model_name = template_4_retract

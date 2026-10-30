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
   model_name = template_2_drop  &
   title = "ADAMS/Aircraft template"
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
   default_coordinate_system = .template_2_drop.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_2_drop.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_2_drop.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_2_drop.ground.hps_uc_sf_atch_l  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_2_drop.ground.hps_uc_sf_atch_r  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 308.0
!
point attributes  &
   point_name = .template_2_drop.ground.hps_lc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_2_drop.ground.hps_uc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_2_drop.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_uta_uc_atch  &
   location = 6324.6, 0.0, 838.2
!
point attributes  &
   point_name = .template_2_drop.ground.hps_uta_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_lta_lc_atch  &
   location = 6299.2, 0.0, 333.4
!
point attributes  &
   point_name = .template_2_drop.ground.hps_lta_lc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_lta_uta_atch  &
   location = 6654.8, 0.0, 611.2
!
point attributes  &
   point_name = .template_2_drop.ground.hps_lta_uta_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_2_drop.ground.hps_uc_geompt  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_2_drop.ground.hps_uc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1197.0
!
point attributes  &
   point_name = .template_2_drop.ground.hps_lc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_origin_reference  &
   location = 0.0, 0.0, 0.0
!
point attributes  &
   point_name = .template_2_drop.ground.hps_origin_reference  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_drop.ground.hps_lb_uc_atch  &
   location = 6021.578, 0.0, 795.02
!
point create  &
   point_name = .template_2_drop.ground.hpl_wheel_center1  &
   location = 6229.096, -209.55, 308.0
!
point create  &
   point_name = .template_2_drop.ground.hpr_wheel_center1  &
   location = 6229.096, 209.55, 308.0
!
point create  &
   point_name = .template_2_drop.ground.hpl_ob_axle1  &
   location = 6229.096, -285.75, 308.0
!
point create  &
   point_name = .template_2_drop.ground.hpr_ob_axle1  &
   location = 6229.096, 285.75, 308.0
!
point create  &
   point_name = .template_2_drop.ground.hps_nlg_axle_lowpoint  &
   location = 6229.096, 0.0, 482.6
!
! ****** Graphics for current part ******
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_2_drop.NLG_m  &
   units = "mass"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 15.6077711
!
variable create  &
   variable_name = .template_2_drop.NLG_Ixx_Iyy  &
   units = "inertia"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.511675841E+05
!
variable create  &
   variable_name = .template_2_drop.NLG_Izz  &
   units = "inertia"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.560153415E+05
!
variable create  &
   variable_name = .template_2_drop.NLG_A_LOW  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.680717E+04
!
variable create  &
   variable_name = .template_2_drop.NLG_A_HIGH  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.0
!
variable create  &
   variable_name = .template_2_drop.NLG_V_LOW  &
   units = "volume"  &
   range = -6.4516E+05, 6.4516E+05  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.028E+07
!
variable create  &
   variable_name = .template_2_drop.NLG_V_HIGH  &
   units = "volume"  &
   range = -6.4516E+05, 6.4516E+05  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.0
!
variable create  &
   variable_name = .template_2_drop.NLG_P_LOW  &
   units = "pressure"  &
   range = -6.4516E-10, 6.4516E-10  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.3
!
variable create  &
   variable_name = .template_2_drop.NLG_P_HIGH  &
   units = "pressure"  &
   range = -6.4516E-10, 6.4516E-10  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.0
!
variable create  &
   variable_name = .template_2_drop.NLG_n_Poly  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.1
!
variable create  &
   variable_name = .template_2_drop.Patm  &
   units = "pressure"  &
   range = -6.4516E-10, 6.4516E-10  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.101325
!
variable create  &
   variable_name = .template_2_drop.NLG_rho_Oil  &
   units = "density"  &
   range = 0.0, 0.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 8.6E-07
!
variable create  &
   variable_name = .template_2_drop.NLG_A_MAIN_OIL  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.953E+04
!
variable create  &
   variable_name = .template_2_drop.NLG_A_RET_OIL  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 6139.0
!
variable create  &
   variable_name = .template_2_drop.NLG_A_MAIN_POS  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 514.0
!
variable create  &
   variable_name = .template_2_drop.NLG_A_MAIN_NEG  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 514.0
!
variable create  &
   variable_name = .template_2_drop.NLG_A_RET_POS  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2313.0
!
variable create  &
   variable_name = .template_2_drop.NLG_A_RET_NEG  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 100.0
!
variable create  &
   variable_name = .template_2_drop.NLG_MAIN_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_2_drop.NLG_RET_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
model display  &
   model_name = template_2_drop

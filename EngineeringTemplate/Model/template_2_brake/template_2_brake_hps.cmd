!
!-------------------------- Default Units for Model ---------------------------!
!
!
defaults units  &
   length = mm  &
   angle = rad  &
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
   size_of_icons = 40.0  &
   spacing_for_grid = 25.4
!
!------------------------------ Adams View Model ------------------------------!
!
!
model create  &
   model_name = template_2_brake  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_2_brake  &
   size_of_icons = 40.0
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
   default_coordinate_system = .template_2_brake.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_2_brake.ground.hpl_udb_spndl_atch_1  &
   location = 1.0963049321E+04, -1022.41898132, 2103.08951238
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_udb_spndl_atch_1  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.POINT_48  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818
!
point attributes  &
   point_name = .template_2_brake.ground.POINT_48  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_lc_top  &
   location = 1.2205761134E+04, -1486.7657470108, 1142.5793907842
!
point create  &
   point_name = .template_2_brake.ground.hpl_wheel_center  &
   location = 1.2270973957E+04, -1811.59195974, 174.2595194
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_wheel_center  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_uc_bot  &
   location = 1.2234684072E+04, -1506.9317387834, 715.279643629
!
point create  &
   point_name = .template_2_brake.ground.hpl_lc_bot  &
   location = 1.227097482E+04, -1532.23480192, 179.1298424
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_lc_bot  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_ob_axle  &
   location = 1.2270973718E+04, -1957.87367632, 171.7060828
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_ob_axle  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_ib_axle  &
   location = 1.227097482E+04, -1532.234807, 179.1298424
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_ib_axle  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_uc_top  &
   location = 1.2137340597E+04, -1439.0607744, 2153.4060818
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_uc_top  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_ldb_udb_atch_1  &
   location = 1.1532351205E+04, -1238.965478376, 1518.05286178
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_ldb_udb_atch_1  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_lta_connect_atch_1  &
   location = 1.2048547912E+04, -1562.2090168, 532.1183668
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_lta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_uta_connect_atch_1  &
   location = 1.205225235E+04, -1491.2788564, 529.0216242
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_uta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_uta_connect_atch_2  &
   location = 1.2087047708E+04, -1493.4025504, 522.0012166
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_uta_connect_atch_2  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_lta_lc_atch_1  &
   location = 1.2150137371E+04, -1553.6660062, 274.0663556
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_lta_lc_atch_1  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_uta_collar_atch_1  &
   location = 1.2106652469E+04, -1496.5360468, 800.236779
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_uta_collar_atch_1  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_connect_1  &
   location = 1.2045992164E+04, -1611.1431582, 534.2547862
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_connect_1  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_ldb_collar_atch_1  &
   location = 1.2111152689E+04, -1463.4257498, 917.6941514
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_ldb_collar_atch_1  &
   visibility = on  &
   size_of_icons = 40.0
!
point create  &
   point_name = .template_2_brake.ground.hpl_uplock_tab  &
   location = 1.1901482877E+04, -1275.11231642, 1033.20487288
!
point attributes  &
   point_name = .template_2_brake.ground.hpl_uplock_tab  &
   size_of_icons = 40.0
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_2_brake.ground  &
   size_of_icons = 40.0
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_2_brake.MLG_n_Poly  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.1
!
variable create  &
   variable_name = .template_2_brake.Patm  &
   units = "pressure"  &
   range = -6.4516E-10, 6.4516E-10  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.101325
!
variable create  &
   variable_name = .template_2_brake.MLG_rho_Oil  &
   units = "density"  &
   range = 0.0, 0.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 8.6E-07
!
variable create  &
   variable_name = .template_2_brake.MLG_A_LOW  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 8921.0
!
variable create  &
   variable_name = .template_2_brake.MLG_V_LOW  &
   units = "volume"  &
   range = -6.4516E+05, 6.4516E+05  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.931E+06
!
variable create  &
   variable_name = .template_2_brake.MLG_P_LOW  &
   units = "pressure"  &
   range = -6.4516E-10, 6.4516E-10  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.45
!
variable create  &
   variable_name = .template_2_brake.MLG_A_MAIN_OIL  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.5571E+04
!
variable create  &
   variable_name = .template_2_brake.MLG_A_RET_OIL  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.4961E+04
!
variable create  &
   variable_name = .template_2_brake.MLG_A_MAIN_POS  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1960.0
!
variable create  &
   variable_name = .template_2_brake.MLG_A_MAIN_NEG  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1960.0
!
variable create  &
   variable_name = .template_2_brake.MLG_A_RET_POS  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3798.0
!
variable create  &
   variable_name = .template_2_brake.MLG_A_RET_NEG  &
   units = "area"  &
   range = -645.16, 645.16  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 157.0
!
variable create  &
   variable_name = .template_2_brake.MLG_RET_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_2_brake.MLG_MAIN_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_2_brake.MLG_Tb  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = -2.0E+06
!
variable create  &
   variable_name = .template_2_brake.MLG_S0  &
   units = "length"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1014.262
!
variable create  &
   variable_name = .template_2_brake.MLG_Vx  &
   units = "velocity"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5000.0
!
variable create  &
   variable_name = .template_2_brake.MLG_m  &
   units = "mass"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 45.359237
!
variable create  &
   variable_name = .template_2_brake.MLG_Ixx_Iyy  &
   units = "inertia"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.7215487769E+06
!
variable create  &
   variable_name = .template_2_brake.MLG_lzz  &
   units = "inertia"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 4.6822344549E+06
!
model display  &
   model_name = template_2_brake

!
!-------------------------- Default Units for Model ---------------------------!
!
!
defaults units  &
   length = meter  &
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
   size_of_icons = 5.0E-02  &
   spacing_for_grid = 2.54E-02
!
!------------------------------ Adams View Model ------------------------------!
!
!
model create  &
   model_name = template_5_brake  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_5_brake  &
   size_of_icons = 5.0E-02
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
   default_coordinate_system = .template_5_brake.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_5_brake.ground.hpl_udb_spndl_atch_1  &
   location = 10.963049321, -1.0224189813, 2.1030895124
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_udb_spndl_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_udb_spndl_atch_1  &
   location = 10.963049321, 1.0224189813, 2.1030895124
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_udb_spndl_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_ib_uc_sf_atch  &
   location = 12.1541593848, -1.0504355699, 2.0926831806
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_ib_uc_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_ib_uc_sf_atch  &
   location = 12.1541593848, 1.0504355699, 2.0926831806
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_ib_uc_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_wheel_center  &
   location = 12.2709739569, -1.8115919597, 0.1742595194
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_wheel_center  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_wheel_center  &
   location = 12.2709739569, 1.8115919597, 0.1742595194
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_wheel_center  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_lc_bot  &
   location = 12.2709748205, -1.5322348019, 0.1791298424
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_lc_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_lc_bot  &
   location = 12.2709748205, 1.5322348019, 0.1791298424
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_lc_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_ob_axle  &
   location = 12.2709737181, -1.9578736763, 0.1717060828
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_ob_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_ob_axle  &
   location = 12.2709737181, 1.9578736763, 0.1717060828
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_ob_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_ib_axle  &
   location = 12.2709748205, -1.532234807, 0.1791298424
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_ib_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_ib_axle  &
   location = 12.2709748205, 1.532234807, 0.1791298424
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_ib_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_uc_top  &
   location = 12.137340597, -1.4390607744, 2.1534060818
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_uc_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_uc_top  &
   location = 12.137340597, 1.4390607744, 2.1534060818
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_uc_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_uc_geompt  &
   location = 12.1670316222, -1.3594512257, 1.7617947238
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_uc_geompt  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_uc_geompt  &
   location = 12.1670316222, 1.3594512257, 1.7617947238
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_uc_geompt  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_ldb_udb_atch_1  &
   location = 11.532351205, -1.2389654784, 1.5180528618
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_ldb_udb_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_ldb_udb_atch_1  &
   location = 11.532351205, 1.2389654784, 1.5180528618
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_ldb_udb_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_lta_connect_atch_1  &
   location = 12.048547912, -1.5622090168, 0.5321183668
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_lta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_lta_connect_atch_1  &
   location = 12.048547912, 1.5622090168, 0.5321183668
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_lta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_uta_connect_atch_1  &
   location = 12.0522523496, -1.4912788564, 0.5290216242
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_uta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_uta_connect_atch_1  &
   location = 12.0522523496, 1.4912788564, 0.5290216242
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_uta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_uta_connect_atch_2  &
   location = 12.087047708, -1.4934025504, 0.5220012166
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_uta_connect_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_uta_connect_atch_2  &
   location = 12.087047708, 1.4934025504, 0.5220012166
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_uta_connect_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_lta_lc_atch_1  &
   location = 12.150137371, -1.5536660062, 0.2740663556
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_lta_lc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_lta_lc_atch_1  &
   location = 12.150137371, 1.5536660062, 0.2740663556
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_lta_lc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_uta_collar_atch_1  &
   location = 12.1066524694, -1.4965360468, 0.800236779
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_uta_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_uta_collar_atch_1  &
   location = 12.1066524694, 1.4965360468, 0.800236779
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_uta_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_connect_1  &
   location = 12.045992164, -1.6111431582, 0.5342547862
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_connect_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_connect_1  &
   location = 12.045992164, 1.6111431582, 0.5342547862
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_connect_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_ldb_collar_atch_1  &
   location = 12.111152689, -1.4634257498, 0.9176941514
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_ldb_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_ldb_collar_atch_1  &
   location = 12.111152689, 1.4634257498, 0.9176941514
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_ldb_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_uplock_tab  &
   location = 11.9014828772, -1.2751123164, 1.0332048729
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_uplock_tab  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_uplock_tab  &
   location = 11.9014828772, 1.2751123164, 1.0332048729
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_uplock_tab  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_db_sf_atch  &
   location = 7.48411, 0.0, 1.62306
!
point attributes  &
   point_name = .template_5_brake.ground.hps_db_sf_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_uc_sf_atch_l  &
   location = 6.31444, -0.34036, 1.69164
!
point attributes  &
   point_name = .template_5_brake.ground.hps_uc_sf_atch_l  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_uc_sf_atch_r  &
   location = 6.31444, 0.34036, 1.69164
!
point attributes  &
   point_name = .template_5_brake.ground.hps_uc_sf_atch_r  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_lc_bot  &
   location = 6.1976, 0.0, 0.308
!
point attributes  &
   point_name = .template_5_brake.ground.hps_lc_bot  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_uc_top  &
   location = 6.1976, 0.0, 1.6256
!
point attributes  &
   point_name = .template_5_brake.ground.hps_uc_top  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_db_uc_atch  &
   location = 6.4516, 0.0, 1.016
!
point attributes  &
   point_name = .template_5_brake.ground.hps_db_uc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_uta_uc_atch  &
   location = 6.3246, 0.0, 0.8382
!
point attributes  &
   point_name = .template_5_brake.ground.hps_uta_uc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_lta_lc_atch  &
   location = 6.2992, 0.0, 0.3334
!
point attributes  &
   point_name = .template_5_brake.ground.hps_lta_lc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_lta_uta_atch  &
   location = 6.6548, 0.0, 0.6112
!
point attributes  &
   point_name = .template_5_brake.ground.hps_lta_uta_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_uc_geompt  &
   location = 6.1976, 0.0, 1.4732
!
point attributes  &
   point_name = .template_5_brake.ground.hps_uc_geompt  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_uc_bot  &
   location = 6.1976, 0.0, 0.762
!
point attributes  &
   point_name = .template_5_brake.ground.hps_uc_bot  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_lc_top  &
   location = 6.1976, 0.0, 1.197
!
point attributes  &
   point_name = .template_5_brake.ground.hps_lc_top  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_wheel_center1  &
   location = 6.229096, -0.20955, 0.308
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_wheel_center1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_wheel_center1  &
   location = 6.229096, 0.20955, 0.308
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_wheel_center1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpl_ob_axle1  &
   location = 6.229096, -0.28575, 0.308
!
point attributes  &
   point_name = .template_5_brake.ground.hpl_ob_axle1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hpr_ob_axle1  &
   location = 6.229096, 0.28575, 0.308
!
point attributes  &
   point_name = .template_5_brake.ground.hpr_ob_axle1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_brake.ground.hps_nlg_axle_lowpoint  &
   location = 6.229096, 0.0, 0.4826
!
point attributes  &
   point_name = .template_5_brake.ground.hps_nlg_axle_lowpoint  &
   size_of_icons = 5.0E-02
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_5_brake.ground  &
   size_of_icons = 5.0E-02
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_5_brake.NLG_A_LOW  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.480717E-02
!
variable create  &
   variable_name = .template_5_brake.NLG_V_LOW  &
   units = "volume"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.028E-02
!
variable create  &
   variable_name = .template_5_brake.NLG_P_LOW  &
   units = "pressure"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.3E+06
!
variable create  &
   variable_name = .template_5_brake.MLG_n_Poly  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.1
!
variable create  &
   variable_name = .template_5_brake.Patm  &
   units = "pressure"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.01325E+05
!
variable create  &
   variable_name = .template_5_brake.MLG_rho_Oil  &
   units = "density"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 860.0
!
variable create  &
   variable_name = .template_5_brake.NLG_A_MAIN_OIL  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.953E-02
!
variable create  &
   variable_name = .template_5_brake.NLG_A_RET_OIL  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 6.139E-03
!
variable create  &
   variable_name = .template_5_brake.NLG_A_MAIN_POS  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.14E-04
!
variable create  &
   variable_name = .template_5_brake.NLG_A_MAIN_NEG  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.14E-04
!
variable create  &
   variable_name = .template_5_brake.NLG_A_RET_POS  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.313E-03
!
variable create  &
   variable_name = .template_5_brake.NLG_A_RET_NEG  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0E-04
!
variable create  &
   variable_name = .template_5_brake.NLG_RET_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_5_brake.NLG_MAIN_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_5_brake.MLG_A_LOW  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 8.921E-03
!
variable create  &
   variable_name = .template_5_brake.MLG_V_LOW  &
   units = "volume"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.931E-03
!
variable create  &
   variable_name = .template_5_brake.MLG_P_LOW  &
   units = "pressure"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.45E+06
!
variable create  &
   variable_name = .template_5_brake.MLG_A_MAIN_OIL  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.5571E-02
!
variable create  &
   variable_name = .template_5_brake.MLG_A_RET_OIL  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.4961E-02
!
variable create  &
   variable_name = .template_5_brake.MLG_A_MAIN_POS  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.96E-03
!
variable create  &
   variable_name = .template_5_brake.MLG_A_MAIN_NEG  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.96E-03
!
variable create  &
   variable_name = .template_5_brake.MLG_A_RET_POS  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.798E-03
!
variable create  &
   variable_name = .template_5_brake.MLG_A_RET_NEG  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.57E-04
!
variable create  &
   variable_name = .template_5_brake.MLG_RET_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_5_brake.MLG_MAIN_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_5_brake.MLG_Tb  &
   units = "torque"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = -2000.0
!
variable create  &
   variable_name = .template_5_brake.Vx  &
   units = "velocity"  &
   range = -1.0E-03, 1.0E-03  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = -10.0
!
variable create  &
   variable_name = .template_5_brake.NLG_S0  &
   units = "length"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.4286
!
variable create  &
   variable_name = .template_5_brake.MLG_S0  &
   units = "length"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.014262
!
model display  &
   model_name = template_5_brake

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
   model_name = template_6_force  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_6_force  &
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
   default_coordinate_system = .template_6_force.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_6_force.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_6_force.ground.hps_db_sf_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_6_force.ground.hps_uc_sf_atch_l  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_6_force.ground.hps_uc_sf_atch_r  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_6_force.ground.hps_lc_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_6_force.ground.hps_uc_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_6_force.ground.hps_db_uc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_uta_uc_atch  &
   location = 6324.6, 0.0, 838.2
!
point attributes  &
   point_name = .template_6_force.ground.hps_uta_uc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_lta_lc_atch  &
   location = 6299.2, 0.0, 533.4
!
point attributes  &
   point_name = .template_6_force.ground.hps_lta_lc_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_lta_uta_atch  &
   location = 6654.8, 0.0, 711.2
!
point attributes  &
   point_name = .template_6_force.ground.hps_lta_uta_atch  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_6_force.ground.hps_uc_geompt  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_6_force.ground.hps_uc_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_6_force.ground.hps_lc_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.POINT_483  &
   location = 5126.9408283745, 0.0, 1962.3668617453
!
point attributes  &
   point_name = .template_6_force.ground.POINT_483  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_wheel_center  &
   location = 6229.096, -209.55, 508.0
!
point attributes  &
   point_name = .template_6_force.ground.hpl_wheel_center  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpr_wheel_center  &
   location = 6229.096, 209.55, 508.0
!
point attributes  &
   point_name = .template_6_force.ground.hpr_wheel_center  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_ob_axle  &
   location = 6229.096, -285.75, 508.0
!
point attributes  &
   point_name = .template_6_force.ground.hpl_ob_axle  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpr_ob_axle  &
   location = 6229.096, 285.75, 508.0
!
point attributes  &
   point_name = .template_6_force.ground.hpr_ob_axle  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_nlg_axle_lowpoint  &
   location = 6229.096, 0.0, 482.6
!
point attributes  &
   point_name = .template_6_force.ground.hps_nlg_axle_lowpoint  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_rod_bot  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point attributes  &
   point_name = .template_6_force.ground.hps_rod_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_rod_top  &
   location = 7227.4389033572, 0.0, 1472.1512863532
!
point attributes  &
   point_name = .template_6_force.ground.hps_rod_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_lockroller_l  &
   location = 6116.051, 50.0, 585.424
!
point attributes  &
   point_name = .template_6_force.ground.hps_lockroller_l  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_lockroller_r  &
   location = 6116.051, -50.0, 585.424
!
point attributes  &
   point_name = .template_6_force.ground.hps_lockroller_r  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_lockroller_l_2  &
   location = 6051.051, 50.0, 585.424
!
point attributes  &
   point_name = .template_6_force.ground.hps_lockroller_l_2  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_spring_slg1  &
   location = 5098.8134765625, -8.0, 1911.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.hps_spring_slg1  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.POINT_3  &
   location = 5098.8134765625, 0.0, 1911.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.POINT_3  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_spring_slg2  &
   location = 5098.8134765625, 8.0, 1911.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.hps_spring_slg2  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_spring_sg1  &
   location = 5152.4833225976, -8.0, 1917.8107177028
!
point attributes  &
   point_name = .template_6_force.ground.hps_spring_sg1  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_spring_sg2  &
   location = 5152.4833225976, 8.0, 1917.8107177028
!
point attributes  &
   point_name = .template_6_force.ground.hps_spring_sg2  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hps_lockroller_r_2  &
   location = 6051.051, -50.0, 585.424
!
point attributes  &
   point_name = .template_6_force.ground.hps_lockroller_r_2  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.suo_qiu_point  &
   location = 6051.051, 0.0, 585.424
!
point attributes  &
   point_name = .template_6_force.ground.suo_qiu_point  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.POINT_636  &
   location = 1.0337216477E+04, -527.0, 1721.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.POINT_636  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.mlg_suo_spring_lg2  &
   location = 1.0345216477E+04, -527.0, 1721.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.mlg_suo_spring_lg2  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.mlg_suo_spring_lg1  &
   location = 1.0329216477E+04, -527.0, 1721.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.mlg_suo_spring_lg1  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.mlg_suo_spring_sg1  &
   location = 1.0329216477E+04, -587.0, 1718.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.mlg_suo_spring_sg1  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.mlg_suo_spring_sg2  &
   location = 1.0345216477E+04, -587.0, 1718.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.mlg_suo_spring_sg2  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_db_top1_2  &
   location = 9537.340597, 1639.0607744, 1652.406081799
!
point attributes  &
   point_name = .template_6_force.ground.hpl_db_top1_2  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.POINT_4832  &
   location = 1.0337216477E+04, -555.127351812, 1772.3668617453
!
point attributes  &
   point_name = .template_6_force.ground.POINT_4832  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_db_top  &
   location = 9537.340597, -1639.0607744, 1652.406081799
!
point attributes  &
   point_name = .template_6_force.ground.hpl_db_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_rod_top  &
   location = 1.0487340597E+04, -889.0607744005, 1752.4060817966
!
point attributes  &
   point_name = .template_6_force.ground.hpl_rod_top  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.POINT_6361  &
   location = 1.0337464717E+04, 527.0, 1721.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.POINT_6361  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.mlg_suo_spring_lg21  &
   location = 1.0329464717E+04, 527.0, 1721.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.mlg_suo_spring_lg21  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.mlg_suo_spring_lg11  &
   location = 1.0345464717E+04, 527.0, 1721.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.mlg_suo_spring_lg11  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.mlg_suo_spring_sg11  &
   location = 1.0345464717E+04, 587.0, 1718.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.mlg_suo_spring_sg11  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.mlg_suo_spring_sg21  &
   location = 1.0329464717E+04, 587.0, 1718.4468383789
!
point attributes  &
   point_name = .template_6_force.ground.mlg_suo_spring_sg21  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.POINT_4831  &
   location = 1.0337464717E+04, 555.127351812, 1772.3668617453
!
point attributes  &
   point_name = .template_6_force.ground.POINT_4831  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpr_rod_topr  &
   location = 1.0487340597E+04, 889.0607744005, 1752.4060817966
!
point attributes  &
   point_name = .template_6_force.ground.hpr_rod_topr  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_lc_top1  &
   location = 1.0337340597E+04, 1639.0607743967, 1202.406081799
!
point attributes  &
   point_name = .template_6_force.ground.hpl_lc_top1  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_tire_axle1  &
   location = 1.0337340597E+04, 1639.0607743967, 452.406081799
!
point attributes  &
   point_name = .template_6_force.ground.hpl_tire_axle1  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpr_rod_bot  &
   location = 1.0487340597E+04, 1489.0607744005, 1752.4060817997
!
point attributes  &
   point_name = .template_6_force.ground.hpr_rod_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpr_actuator_bot  &
   location = 1.0487340597E+04, 1389.0607744005, 1752.4060818003
!
point attributes  &
   point_name = .template_6_force.ground.hpr_actuator_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpr_actuator_top  &
   location = 1.0487340597E+04, 739.0607744005, 1752.406081798
!
point attributes  &
   point_name = .template_6_force.ground.hpr_actuator_top  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_uc_top1  &
   location = 1.0337340597E+04, 1639.0607744, 1652.406081799
!
point attributes  &
   point_name = .template_6_force.ground.hpl_uc_top1  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_lc_top  &
   location = 1.0337340597E+04, -1639.0607743967, 1202.406081799
!
point attributes  &
   point_name = .template_6_force.ground.hpl_lc_top  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_tire_axle  &
   location = 1.0337340597E+04, -1639.0607743967, 452.406081799
!
point attributes  &
   point_name = .template_6_force.ground.hpl_tire_axle  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_rod_bot  &
   location = 1.0487340597E+04, -1489.0607744005, 1752.4060817997
!
point attributes  &
   point_name = .template_6_force.ground.hpl_rod_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_actuator_bot  &
   location = 1.0487340597E+04, -1389.0607744005, 1752.4060818003
!
point attributes  &
   point_name = .template_6_force.ground.hpl_actuator_bot  &
   visibility = on  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_actuator_top  &
   location = 1.0487340597E+04, -739.0607744005, 1752.406081798
!
point attributes  &
   point_name = .template_6_force.ground.hpl_actuator_top  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.ground.hpl_uc_top  &
   location = 1.0337340597E+04, -1639.0607744, 1652.406081799
!
point attributes  &
   point_name = .template_6_force.ground.hpl_uc_top  &
   visibility = on  &
   size_of_icons = 25.0
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_6_force.ground  &
   size_of_icons = 25.0
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_6_force.AIR_VELOCITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 56.0
!
variable create  &
   variable_name = .template_6_force.AIR_DENSITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_6_force.NLG_DRAG_COEFF  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.7
!
variable create  &
   variable_name = .template_6_force.NLG_PROJ_AREA  &
   units = "area"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.25
!
variable create  &
   variable_name = .template_6_force.NLG_LOCK_SPRING_K  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 650.0
!
variable create  &
   variable_name = .template_6_force.NLG_LOCK_SPRING_C  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 11.0
!
variable create  &
   variable_name = .template_6_force.NLG_LOCK_UNLOCK_TIME  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
variable create  &
   variable_name = .template_6_force.NLG_UNLOCK_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1500.0
!
variable create  &
   variable_name = .template_6_force.MLG_LOCK_UNLOCK_TIME  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
variable create  &
   variable_name = .template_6_force.MLG_UNLOCK_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3200.0
!
variable create  &
   variable_name = .template_6_force.MLG_LOCK_SPRING_K  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 600.0
!
variable create  &
   variable_name = .template_6_force.MLG_LOCK_SPRING_C  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 10.0
!
variable create  &
   variable_name = .template_6_force.nlg_zdtup_t1  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_6_force.NLG_RETRACT_HOLD_TIME  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.2
!
variable create  &
   variable_name = .template_6_force.nlg_zdtup_t3  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_6_force.nlg_zdt_t0  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.1
!
variable create  &
   variable_name = .template_6_force.nlg_zdtdown_t1  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_6_force.NLG_EXTEND_HOLD_TIME  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.4
!
variable create  &
   variable_name = .template_6_force.nlg_zdtdown_t3  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_6_force.NLG_RETRACT_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.9E+04
!
variable create  &
   variable_name = .template_6_force.NLG_EXTEND_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.2E+04
!
variable create  &
   variable_name = .template_6_force.mlg_zdtup_t1  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_6_force.MLG_RETRACT_HOLD_TIME  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.1
!
variable create  &
   variable_name = .template_6_force.mlg_zdtup_t3  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_6_force.mlg_zdt_t0  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.2
!
variable create  &
   variable_name = .template_6_force.mlg_zdtdown_t1  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_6_force.MLG_EXTEND_HOLD_TIME  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 4.4
!
variable create  &
   variable_name = .template_6_force.mlg_zdtdown_t3  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.1
!
variable create  &
   variable_name = .template_6_force.MLG_RETRACT_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.9E+04
!
variable create  &
   variable_name = .template_6_force.MLG_EXTEND_FORCE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.2E+04
!
variable create  &
   variable_name = .template_6_force.MLG_DRAG_COEFF  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.7
!
variable create  &
   variable_name = .template_6_force.MLG_PROJ_AREA  &
   units = "area"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.25
!
model display  &
   model_name = template_6_force

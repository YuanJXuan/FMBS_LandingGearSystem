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
   model_name = template_6_motion  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_6_motion  &
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
   default_coordinate_system = .template_6_motion.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_6_motion.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_6_motion.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_sf_atch_l  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_sf_atch_r  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_6_motion.ground.hps_lc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_6_motion.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uta_uc_atch  &
   location = 6324.6, 0.0, 838.2
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uta_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lta_lc_atch  &
   location = 6299.2, 0.0, 533.4
!
point attributes  &
   point_name = .template_6_motion.ground.hps_lta_lc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lta_uta_atch  &
   location = 6654.8, 0.0, 711.2
!
point attributes  &
   point_name = .template_6_motion.ground.hps_lta_uta_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_geompt  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_6_motion.ground.hps_uc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_6_motion.ground.hps_lc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_6_motion.ground.hps_lb_uc_atch  &
   location = 6021.578, 0.0, 795.02
!
point create  &
   point_name = .template_6_motion.ground.hpl_wheel_center  &
   location = 6229.096, -209.55, 508.0
!
point create  &
   point_name = .template_6_motion.ground.hpr_wheel_center  &
   location = 6229.096, 209.55, 508.0
!
point create  &
   point_name = .template_6_motion.ground.hpl_ob_axle  &
   location = 6229.096, -285.75, 508.0
!
point create  &
   point_name = .template_6_motion.ground.hpr_ob_axle  &
   location = 6229.096, 285.75, 508.0
!
point create  &
   point_name = .template_6_motion.ground.hps_nlg_axle_lowpoint  &
   location = 6229.096, 0.0, 482.6
!
point create  &
   point_name = .template_6_motion.ground.hps_rod_bot  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point create  &
   point_name = .template_6_motion.ground.hps_rod_top  &
   location = 7227.4389033572, 0.0, 1472.1512863532
!
point create  &
   point_name = .template_6_motion.ground.hps_aeroforceN  &
   location = 6200.9167643494, 0.0, 1207.1824231157
!
point create  &
   point_name = .template_6_motion.ground.hpl_aeroforceL  &
   location = 1.2305761133E+04, -1486.7657470101, 1142.5793907993
!
point create  &
   point_name = .template_6_motion.ground.hpr_aerofoceR  &
   location = 1.2305761133E+04, 1486.7657470101, 1142.5793907993
!
point create  &
   point_name = .template_6_motion.ground.hpl_udb_spndl_atch_1  &
   location = 1.1063049321E+04, -1022.41898132, 2103.08951238
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_udb_spndl_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_udb_spndl_atch_1  &
   location = 1.1063049321E+04, 1022.41898132, 2103.08951238
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_udb_spndl_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ib_uc_sf_atch  &
   location = 1.2254159385E+04, -1050.43556994, 2092.68318064
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ib_uc_sf_atch  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ib_uc_sf_atch  &
   location = 1.2254159385E+04, 1050.43556994, 2092.68318064
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ib_uc_sf_atch  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_wheel_center1  &
   location = 1.2370973957E+04, -1811.59195974, 174.2595194
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_wheel_center1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_wheel_center1  &
   location = 1.2370973957E+04, 1811.59195974, 174.2595194
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_wheel_center1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lc_bot  &
   location = 1.237097482E+04, -1532.23480192, 179.1298424
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lc_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lc_bot  &
   location = 1.237097482E+04, 1532.23480192, 179.1298424
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lc_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ob_axle1  &
   location = 1.2370973718E+04, -1957.87367632, 171.7060828
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ob_axle1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ob_axle1  &
   location = 1.2370973718E+04, 1957.87367632, 171.7060828
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ob_axle1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ib_axle  &
   location = 1.237097482E+04, -1532.234807, 179.1298424
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ib_axle  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ib_axle  &
   location = 1.237097482E+04, 1532.234807, 179.1298424
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ib_axle  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uc_top  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uc_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uc_top  &
   location = 1.2237340597E+04, 1439.0607744, 2153.4060818
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uc_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uc_geompt  &
   location = 1.2267031622E+04, -1359.45122572, 1761.7947238
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uc_geompt  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uc_geompt  &
   location = 1.2267031622E+04, 1359.45122572, 1761.7947238
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uc_geompt  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_stator_attach  &
   location = 1.2370974048E+04, -1754.4506694, 175.256952
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_stator_attach  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_stator_attach  &
   location = 1.2370974048E+04, 1754.4506694, 175.256952
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_stator_attach  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ldb_udb_atch_1  &
   location = 1.1632351205E+04, -1238.965478376, 1518.05286178
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ldb_udb_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ldb_udb_atch_1  &
   location = 1.1632351205E+04, 1238.965478376, 1518.05286178
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ldb_udb_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lta_connect_atch_1  &
   location = 1.2148547912E+04, -1562.2090168, 532.1183668
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lta_connect_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lta_connect_atch_1  &
   location = 1.2148547912E+04, 1562.2090168, 532.1183668
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lta_connect_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uta_connect_atch_1  &
   location = 1.215225235E+04, -1491.2788564, 529.0216242
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uta_connect_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uta_connect_atch_1  &
   location = 1.215225235E+04, 1491.2788564, 529.0216242
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uta_connect_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uta_connect_atch_2  &
   location = 1.2187047708E+04, -1493.4025504, 522.0012166
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uta_connect_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uta_connect_atch_2  &
   location = 1.2187047708E+04, 1493.4025504, 522.0012166
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uta_connect_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lta_lc_atch_1  &
   location = 1.2250137371E+04, -1553.6660062, 274.0663556
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lta_lc_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lta_lc_atch_1  &
   location = 1.2250137371E+04, 1553.6660062, 274.0663556
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lta_lc_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lta_lc_atch_2  &
   location = 1.2252562741E+04, -1507.2279736, 272.0389276
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lta_lc_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lta_lc_atch_2  &
   location = 1.2252562741E+04, 1507.2279736, 272.0389276
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lta_lc_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uta_collar_atch_1  &
   location = 1.2206652469E+04, -1496.5360468, 800.236779
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uta_collar_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uta_collar_atch_1  &
   location = 1.2206652469E+04, 1496.5360468, 800.236779
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uta_collar_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_uta_collar_atch_2  &
   location = 1.221021393E+04, -1428.342457, 797.259518
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_uta_collar_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_uta_collar_atch_2  &
   location = 1.221021393E+04, 1428.342457, 797.259518
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_uta_collar_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_collar_top  &
   location = 1.2316682831E+04, -1494.3808822, 981.2211008
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_collar_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_collar_top  &
   location = 1.2316682831E+04, 1494.3808822, 981.2211008
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_collar_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_collar_bot  &
   location = 1.2331355039E+04, -1504.6108084, 764.4576024
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_collar_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_collar_bot  &
   location = 1.2331355039E+04, 1504.6108084, 764.4576024
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_collar_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_upr_strt_bot  &
   location = 1.2332707285E+04, -1505.5538596, 744.4805024
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_upr_strt_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_upr_strt_bot  &
   location = 1.2332707285E+04, 1505.5538596, 744.4805024
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_upr_strt_bot  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_upr_strt_top  &
   location = 1.2247818199E+04, 1446.3662462, 1998.6101506
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_upr_strt_top  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_lwract_uc_atch_1  &
   location = 1.2405306047E+04, -1372.8605004, 1306.1589828
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_lwract_uc_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lwract_uc_atch_1  &
   location = 1.2405306047E+04, 1372.8605004, 1306.1589828
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lwract_uc_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_lwract_uc_atch_2  &
   location = 1.2406350165E+04, 1355.5888052, 1303.8056982
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_lwract_uc_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_upract_sf_atch_1  &
   location = 1.240147781E+04, -1284.3931894, 1952.816897
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_upract_sf_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_upract_sf_atch_1  &
   location = 1.240147781E+04, 1284.3931894, 1952.816897
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_upract_sf_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_upract_sf_atch_2  &
   location = 1.2403675418E+04, 1250.4491628, 1948.1928778
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_upract_sf_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_spndl_sf_atch  &
   location = 1.0877681391E+04, -956.6499282, 2095.1467876
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_spndl_sf_atch  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_spndl_sf_atch  &
   location = 1.0877681391E+04, 956.6499282, 2095.1467876
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_spndl_sf_atch  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_connect_1  &
   location = 1.2145992164E+04, -1611.1431582, 534.2547862
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_connect_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_connect_1  &
   location = 1.2145992164E+04, 1611.1431582, 534.2547862
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_connect_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ldb_collar_atch_1  &
   location = 1.2211152689E+04, -1463.4257498, 917.6941514
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ldb_collar_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ldb_collar_atch_1  &
   location = 1.2211152689E+04, 1463.4257498, 917.6941514
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ldb_collar_atch_1  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpl_ldb_collar_atch_2  &
   location = 1.2182985562E+04, -1542.5928508, 919.5237896
!
point attributes  &
   point_name = .template_6_motion.ground.hpl_ldb_collar_atch_2  &
   visibility = on
!
point create  &
   point_name = .template_6_motion.ground.hpr_ldb_collar_atch_2  &
   location = 1.2182985562E+04, 1542.5928508, 919.5237896
!
point attributes  &
   point_name = .template_6_motion.ground.hpr_ldb_collar_atch_2  &
   visibility = on
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_6_motion.ground  &
   size_of_icons = 50.8
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_6_motion.AIR_VELOCITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 55.0
!
variable create  &
   variable_name = .template_6_motion.AIR_DENSITY  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_6_motion.NLG_DRAG_COEFF  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.7
!
variable create  &
   variable_name = .template_6_motion.NLG_PROJ_AREA  &
   units = "area"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.3077
!
variable create  &
   variable_name = .template_6_motion.NLG_RETRACT_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 4.5
!
variable create  &
   variable_name = .template_6_motion.NLG_UP_HOLD_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_6_motion.NLG_EXTEND_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
variable create  &
   variable_name = .template_6_motion.MLG_RETRACT_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 4.5
!
variable create  &
   variable_name = .template_6_motion.MLG_UP_HOLD_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0
!
variable create  &
   variable_name = .template_6_motion.MLG_EXTEND_TIME  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.0
!
variable create  &
   variable_name = .template_6_motion.MLG_PROJ_AREA  &
   units = "area"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.418
!
variable create  &
   variable_name = .template_6_motion.MLG_DRAG_COEFF  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.7
!
variable create  &
   variable_name = .template_6_motion.NLG_ACTUATOR_STROKE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 635.0
!
variable create  &
   variable_name = .template_6_motion.MLG_ACTUATOR_STROKE  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 345.0
!
model display  &
   model_name = template_6_motion

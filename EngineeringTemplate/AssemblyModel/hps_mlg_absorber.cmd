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
   point_name = .Unknown.ground.hpl_udb_spndl_atch_1  &
   location = 10.963049321, -1.0224189813, 2.1030895124
!
point attributes  &
   point_name = .Unknown.ground.hpl_udb_spndl_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_udb_spndl_atch_1  &
   location = 10.963049321, 1.0224189813, 2.1030895124
!
point attributes  &
   point_name = .Unknown.ground.hpr_udb_spndl_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_ib_uc_sf_atch  &
   location = 12.1541593848, -1.0504355699, 2.0926831806
!
point attributes  &
   point_name = .Unknown.ground.hpl_ib_uc_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_ib_uc_sf_atch  &
   location = 12.1541593848, 1.0504355699, 2.0926831806
!
point attributes  &
   point_name = .Unknown.ground.hpr_ib_uc_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_wheel_center  &
   location = 12.2709739569, -1.8115919597, 0.1742595194
!
point attributes  &
   point_name = .Unknown.ground.hpl_wheel_center  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_wheel_center  &
   location = 12.2709739569, 1.8115919597, 0.1742595194
!
point attributes  &
   point_name = .Unknown.ground.hpr_wheel_center  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_lc_bot  &
   location = 12.2709748205, -1.5322348019, 0.1791298424
!
point attributes  &
   point_name = .Unknown.ground.hpl_lc_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_lc_bot  &
   location = 12.2709748205, 1.5322348019, 0.1791298424
!
point attributes  &
   point_name = .Unknown.ground.hpr_lc_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_ob_axle  &
   location = 12.2709737181, -1.9578736763, 0.1717060828
!
point attributes  &
   point_name = .Unknown.ground.hpl_ob_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_ob_axle  &
   location = 12.2709737181, 1.9578736763, 0.1717060828
!
point attributes  &
   point_name = .Unknown.ground.hpr_ob_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_ib_axle  &
   location = 12.2709748205, -1.532234807, 0.1791298424
!
point attributes  &
   point_name = .Unknown.ground.hpl_ib_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_ib_axle  &
   location = 12.2709748205, 1.532234807, 0.1791298424
!
point attributes  &
   point_name = .Unknown.ground.hpr_ib_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_uc_top  &
   location = 12.137340597, -1.4390607744, 2.1534060818
!
point attributes  &
   point_name = .Unknown.ground.hpl_uc_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_uc_top  &
   location = 12.137340597, 1.4390607744, 2.1534060818
!
point attributes  &
   point_name = .Unknown.ground.hpr_uc_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_uc_geompt  &
   location = 12.1670316222, -1.3594512257, 1.7617947238
!
point attributes  &
   point_name = .Unknown.ground.hpl_uc_geompt  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_uc_geompt  &
   location = 12.1670316222, 1.3594512257, 1.7617947238
!
point attributes  &
   point_name = .Unknown.ground.hpr_uc_geompt  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_stator_attach  &
   location = 12.2709740483, -1.7544506694, 0.175256952
!
point attributes  &
   point_name = .Unknown.ground.hpl_stator_attach  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_stator_attach  &
   location = 12.2709740483, 1.7544506694, 0.175256952
!
point attributes  &
   point_name = .Unknown.ground.hpr_stator_attach  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_ldb_uc_atch  &
   location = 12.54125, -1.8542, 1.21285
!
point attributes  &
   point_name = .Unknown.ground.hpl_ldb_uc_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_ldb_uc_atch  &
   location = 12.54125, 1.8542, 1.21285
!
point attributes  &
   point_name = .Unknown.ground.hpr_ldb_uc_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_ldb_udb_atch_1  &
   location = 11.532351205, -1.2389654784, 1.5180528618
!
point attributes  &
   point_name = .Unknown.ground.hpl_ldb_udb_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_ldb_udb_atch_1  &
   location = 11.532351205, 1.2389654784, 1.5180528618
!
point attributes  &
   point_name = .Unknown.ground.hpr_ldb_udb_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_lta_uta_atch  &
   location = 13.02385, -1.8796, 0.62865
!
point attributes  &
   point_name = .Unknown.ground.hpl_lta_uta_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_lta_uta_atch  &
   location = 13.02385, 1.8796, 0.62865
!
point attributes  &
   point_name = .Unknown.ground.hpr_lta_uta_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_lta_connect_atch_1  &
   location = 12.048547912, -1.5622090168, 0.5321183668
!
point attributes  &
   point_name = .Unknown.ground.hpl_lta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_lta_connect_atch_1  &
   location = 12.048547912, 1.5622090168, 0.5321183668
!
point attributes  &
   point_name = .Unknown.ground.hpr_lta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_uta_connect_atch_1  &
   location = 12.0522523496, -1.4912788564, 0.5290216242
!
point attributes  &
   point_name = .Unknown.ground.hpl_uta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_uta_connect_atch_1  &
   location = 12.0522523496, 1.4912788564, 0.5290216242
!
point attributes  &
   point_name = .Unknown.ground.hpr_uta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_uta_connect_atch_2  &
   location = 12.087047708, -1.4934025504, 0.5220012166
!
point attributes  &
   point_name = .Unknown.ground.hpl_uta_connect_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_uta_connect_atch_2  &
   location = 12.087047708, 1.4934025504, 0.5220012166
!
point attributes  &
   point_name = .Unknown.ground.hpr_uta_connect_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_lta_lc_atch_1  &
   location = 12.150137371, -1.5536660062, 0.2740663556
!
point attributes  &
   point_name = .Unknown.ground.hpl_lta_lc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_lta_lc_atch_1  &
   location = 12.150137371, 1.5536660062, 0.2740663556
!
point attributes  &
   point_name = .Unknown.ground.hpr_lta_lc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_lta_lc_atch_2  &
   location = 12.1525627408, -1.5072279736, 0.2720389276
!
point attributes  &
   point_name = .Unknown.ground.hpl_lta_lc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_lta_lc_atch_2  &
   location = 12.1525627408, 1.5072279736, 0.2720389276
!
point attributes  &
   point_name = .Unknown.ground.hpr_lta_lc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_uta_collar_atch_1  &
   location = 12.1066524694, -1.4965360468, 0.800236779
!
point attributes  &
   point_name = .Unknown.ground.hpl_uta_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_uta_collar_atch_1  &
   location = 12.1066524694, 1.4965360468, 0.800236779
!
point attributes  &
   point_name = .Unknown.ground.hpr_uta_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_uta_collar_atch_2  &
   location = 12.1102139304, -1.428342457, 0.797259518
!
point attributes  &
   point_name = .Unknown.ground.hpl_uta_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_uta_collar_atch_2  &
   location = 12.1102139304, 1.428342457, 0.797259518
!
point attributes  &
   point_name = .Unknown.ground.hpr_uta_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_collar_top  &
   location = 12.216682831, -1.4943808822, 0.9812211008
!
point attributes  &
   point_name = .Unknown.ground.hpl_collar_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_collar_top  &
   location = 12.216682831, 1.4943808822, 0.9812211008
!
point attributes  &
   point_name = .Unknown.ground.hpr_collar_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_collar_bot  &
   location = 12.2313550394, -1.5046108084, 0.7644576024
!
point attributes  &
   point_name = .Unknown.ground.hpl_collar_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_collar_bot  &
   location = 12.2313550394, 1.5046108084, 0.7644576024
!
point attributes  &
   point_name = .Unknown.ground.hpr_collar_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_upr_strt_bot  &
   location = 12.2327072846, -1.5055538596, 0.7444805024
!
point attributes  &
   point_name = .Unknown.ground.hpl_upr_strt_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_upr_strt_bot  &
   location = 12.2327072846, 1.5055538596, 0.7444805024
!
point attributes  &
   point_name = .Unknown.ground.hpr_upr_strt_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_upr_strt_top  &
   location = 12.1478181986, -1.4463662462, 1.9986101506
!
point attributes  &
   point_name = .Unknown.ground.hpl_upr_strt_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_upr_strt_top  &
   location = 12.1478181986, 1.4463662462, 1.9986101506
!
point attributes  &
   point_name = .Unknown.ground.hpr_upr_strt_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_lwract_uc_atch_1  &
   location = 12.3053060472, -1.3728605004, 1.3061589828
!
point attributes  &
   point_name = .Unknown.ground.hpl_lwract_uc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_lwract_uc_atch_1  &
   location = 12.3053060472, 1.3728605004, 1.3061589828
!
point attributes  &
   point_name = .Unknown.ground.hpr_lwract_uc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_lwract_uc_atch_2  &
   location = 12.306350165, -1.3555888052, 1.3038056982
!
point attributes  &
   point_name = .Unknown.ground.hpl_lwract_uc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_lwract_uc_atch_2  &
   location = 12.306350165, 1.3555888052, 1.3038056982
!
point attributes  &
   point_name = .Unknown.ground.hpr_lwract_uc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_upract_sf_atch_1  &
   location = 12.30147781, -1.2843931894, 1.952816897
!
point attributes  &
   point_name = .Unknown.ground.hpl_upract_sf_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_upract_sf_atch_1  &
   location = 12.30147781, 1.2843931894, 1.952816897
!
point attributes  &
   point_name = .Unknown.ground.hpr_upract_sf_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_upract_sf_atch_2  &
   location = 12.303675418, -1.2504491628, 1.9481928778
!
point attributes  &
   point_name = .Unknown.ground.hpl_upract_sf_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_upract_sf_atch_2  &
   location = 12.303675418, 1.2504491628, 1.9481928778
!
point attributes  &
   point_name = .Unknown.ground.hpr_upract_sf_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_spndl_sf_atch  &
   location = 10.777681391, -0.9566499282, 2.0951467876
!
point attributes  &
   point_name = .Unknown.ground.hpl_spndl_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_spndl_sf_atch  &
   location = 10.777681391, 0.9566499282, 2.0951467876
!
point attributes  &
   point_name = .Unknown.ground.hpr_spndl_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_connect_1  &
   location = 12.045992164, -1.6111431582, 0.5342547862
!
point attributes  &
   point_name = .Unknown.ground.hpl_connect_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_connect_1  &
   location = 12.045992164, 1.6111431582, 0.5342547862
!
point attributes  &
   point_name = .Unknown.ground.hpr_connect_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_ldb_udb_atch_2  &
   location = 11.5117089298, -1.2969830804, 1.51939371
!
point attributes  &
   point_name = .Unknown.ground.hpl_ldb_udb_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_ldb_udb_atch_2  &
   location = 11.5117089298, 1.2969830804, 1.51939371
!
point attributes  &
   point_name = .Unknown.ground.hpr_ldb_udb_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_ldb_collar_atch_1  &
   location = 12.111152689, -1.4634257498, 0.9176941514
!
point attributes  &
   point_name = .Unknown.ground.hpl_ldb_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_ldb_collar_atch_1  &
   location = 12.111152689, 1.4634257498, 0.9176941514
!
point attributes  &
   point_name = .Unknown.ground.hpr_ldb_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_ldb_collar_atch_2  &
   location = 12.0829855622, -1.5425928508, 0.9195237896
!
point attributes  &
   point_name = .Unknown.ground.hpl_ldb_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_ldb_collar_atch_2  &
   location = 12.0829855622, 1.5425928508, 0.9195237896
!
point attributes  &
   point_name = .Unknown.ground.hpr_ldb_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpl_uplock_tab  &
   location = 11.9014828772, -1.2751123164, 1.0332048729
!
point attributes  &
   point_name = .Unknown.ground.hpl_uplock_tab  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .Unknown.ground.hpr_uplock_tab  &
   location = 11.9014828772, 1.2751123164, 1.0332048729
!
point attributes  &
   point_name = .Unknown.ground.hpr_uplock_tab  &
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

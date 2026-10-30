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
!-------------------------------- Data storage --------------------------------!
!
!
data_element create variable  &
   variable_name = .template_5_brake.NLG_V  &
   adams_id = 115  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_brake.LMLG_S  &
   adams_id = 116  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_brake.RMLG_S  &
   adams_id = 117  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_brake.LMLG_V  &
   adams_id = 118  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_brake.RMLG_V  &
   adams_id = 119  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_brake.NLG_S  &
   adams_id = 120  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_brake.slip_ratio  &
   adams_id = 127  &
   initial_condition = 0.0  &
   function = ""
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .template_5_brake.aluminum  &
   adams_id = 2  &
   density = 2740.0  &
   youngs_modulus = 7.1705E+10  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_5_brake.steel  &
   adams_id = 5  &
   density = 7801.0  &
   youngs_modulus = 2.07E+11  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_5_brake.steel_2  &
   adams_id = 3  &
   density = 7801.0  &
   youngs_modulus = 2.07E+11  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_5_brake.aluminum_2  &
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
   default_coordinate_system = .template_5_brake.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ground.origo  &
   adams_id = 1  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.origo  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfs_subframe_ref  &
   adams_id = 3  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 3.1415926536, 1.5707963268, 3.0987703907
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfs_subframe_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_spin_axis  &
   adams_id = 4  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 3.1415910214, 1.5533424893, 9.3519600853E-05
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_spin_axis  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_spin_axis  &
   adams_id = 5  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 1.6321930433E-06, 1.5533424893, 3.141499134
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_spin_axis  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_uc_sf_atch  &
   adams_id = 10  &
   location = 12.1457499909, -1.2447481722, 2.1230446312  &
   orientation = 6.2399346402, 1.4159416907, 0.2735583873
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_uc_sf_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_uc_sf_atch  &
   adams_id = 11  &
   location = 12.1457499909, 1.2447481722, 2.1230446312  &
   orientation = 3.1848433206, 1.4159416907, 2.8680342663
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_uc_sf_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_axial_reference  &
   adams_id = 13  &
   location = 12.2709748205, -1.5322348019, 0.1791298424  &
   orientation = 4.1035232988, 8.2329541734E-02, 2.1780711303
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_axial_reference  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_axial_reference  &
   adams_id = 14  &
   location = 12.2709748205, 1.5322348019, 0.1791298424  &
   orientation = 5.321254662, 8.2329541734E-02, 0.9635215233
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_axial_reference  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_uc_bot  &
   adams_id = 15  &
   location = 12.234684072, -1.5069317388, 0.7152796436  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_uc_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_uc_bot  &
   adams_id = 16  &
   location = 12.234684072, 1.5069317388, 0.7152796436  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_uc_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_uc_top  &
   adams_id = 17  &
   location = 12.137340597, -1.4390607744, 2.1534060818  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_uc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_uc_top  &
   adams_id = 18  &
   location = 12.137340597, 1.4390607744, 2.1534060818  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_uc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_lc_top  &
   adams_id = 19  &
   location = 12.2057611337, -1.486765747, 1.1425793908  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_lc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_lc_top  &
   adams_id = 20  &
   location = 12.2057611337, 1.486765747, 1.1425793908  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_lc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_collar_top  &
   adams_id = 25  &
   location = 12.2161847888, -1.4940334506, 0.9885831006  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_collar_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_collar_top  &
   adams_id = 26  &
   location = 12.2161847888, 1.4940334506, 0.9885831006  &
   orientation = 2.1796620084, 3.0592631119, 5.3196637838
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_collar_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_collar_bot  &
   adams_id = 27  &
   location = 12.2308845534, -1.5042825937, 0.7714127142  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_collar_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_collar_bot  &
   adams_id = 28  &
   location = 12.2308845534, 1.5042825937, 0.7714127142  &
   orientation = 2.1796620084, 3.0592631119, 5.3196637838
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_collar_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_plane_ref  &
   adams_id = 29  &
   location = 11.7904549128, -1.3312381859, 1.4785418122  &
   orientation = 1.2298492976, 1.5304362235, 4.6906005914
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_plane_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_plane_ref  &
   adams_id = 30  &
   location = 11.7904549128, 1.3312381859, 1.4785418122  &
   orientation = 1.911743356, 1.5304362235, 4.7341773694
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_plane_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_plane_ref_2  &
   adams_id = 31  &
   location = 11.7904549128, -1.3312381859, 1.4785418122  &
   orientation = 2.7997663425, 1.5925669695, 4.6720193054
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_plane_ref_2  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_plane_ref_2  &
   adams_id = 32  &
   location = 11.7904549128, 1.3312381859, 1.4785418122  &
   orientation = 0.3418263111, 1.5925669695, 4.7527586553
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_plane_ref_2  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_spin_axis_1  &
   adams_id = 37  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 6.283183675, 1.5882501643, 3.141499134
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_spin_axis_1  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_spin_axis_1  &
   adams_id = 38  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 3.1415942858, 1.5882501643, 9.3519600853E-05
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_spin_axis_1  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_ldb_geompt_1  &
   adams_id = 39  &
   location = 11.8912081251, -1.3781308467, 1.1458304613  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_ldb_geompt_1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_ldb_geompt_1  &
   adams_id = 40  &
   location = 11.8912081251, 1.3781308467, 1.1458304613  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_ldb_geompt_1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_ldb_geompt_2  &
   adams_id = 41  &
   location = 11.9606643032, -1.4050660792, 1.0737874161  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_ldb_geompt_2  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_ldb_geompt_2  &
   adams_id = 42  &
   location = 11.9606643032, 1.4050660792, 1.0737874161  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_ldb_geompt_2  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.lumian_ref_1  &
   adams_id = 239  &
   location = 12.2383679771, 1.5095002745, -0.282740481  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.lumian_ref_1  &
   visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.MARKER_456  &
   adams_id = 456  &
   location = 10.623404959, 0.0, 2.6282477971  &
   orientation = 4.7123889804, 1.5707028214, 3.1415926536
!
marker create  &
   marker_name = .template_5_brake.ground.MARKER_460  &
   adams_id = 460  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 1.6321930438E-06, 1.5533424893, 0.0
!
marker create  &
   marker_name = .template_5_brake.ground.origo1  &
   adams_id = 287  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.origo1  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfs_subframe_to_body_point  &
   adams_id = 290  &
   location = 6.70433, 0.0, 1.66878  &
   orientation = 0.0, 1.5707963268, 6.2246204335
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfs_subframe_to_body_point  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfl_spin_axis1  &
   adams_id = 292  &
   location = 6.229096, -0.20955, 0.308  &
   orientation = 0.0, 1.5707963268, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfl_spin_axis1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfr_spin_axis1  &
   adams_id = 293  &
   location = 6.229096, 0.20955, 0.308  &
   orientation = 3.1415926536, 1.5707963268, 3.1415926536
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfr_spin_axis1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfs_wheel_centers_midpoint  &
   adams_id = 294  &
   location = 6.229096, 0.0, 0.508  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfs_wheel_centers_midpoint  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfs_nlg_axle_lowpoint  &
   adams_id = 295  &
   location = 6.229096, 0.0, 0.4826  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfs_nlg_axle_lowpoint  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ground.cfs_collar_top  &
   adams_id = 296  &
   location = 6.1976, 0.0, 0.856996  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ground.cfs_collar_top  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_5_brake.ground.luntai1_tire_jf_1  &
   adams_id = 240
!
floating_marker create  &
   floating_marker_name = .template_5_brake.ground.luntai2_tire_jf_1  &
   adams_id = 241
!
floating_marker create  &
   floating_marker_name = .template_5_brake.ground.luntai1_tire_jf_11  &
   adams_id = 298
!
floating_marker create  &
   floating_marker_name = .template_5_brake.ground.luntai2_tire_jf_11  &
   adams_id = 299
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
!---------------------------------- PART_46 -----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.PART_46  &
   adams_id = 46  &
   location = -0.92679, 0.0, 0.5  &
   orientation = 0.0, 0.0, 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.PART_46
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.PART_46.MARKER_461  &
   adams_id = 461  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 4.7123889804, 1.5707028214, 3.1415926536
!
marker create  &
   marker_name = .template_5_brake.PART_46.MARKER_462  &
   adams_id = 462  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 4.7123889804, 1.5707028214, 3.1415926536
!
marker create  &
   marker_name = .template_5_brake.PART_46.MARKER_439  &
   adams_id = 439  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.PART_46.MARKER_439  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.PART_46.MARKER_433  &
   adams_id = 433  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.PART_46.MARKER_433  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.PART_46.cm  &
   adams_id = 438  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.PART_46.cm  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.PART_46.MARKER_443  &
   adams_id = 443  &
   location = 13.064130597, 1.4390607744, 1.6534060818  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.PART_46.MARKER_443  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.PART_46.MARKER_445  &
   adams_id = 445  &
   location = 13.064130597, -1.4390607744, 1.6534060818  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.PART_46.MARKER_445  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.PART_46.MARKER_449  &
   adams_id = 449  &
   location = 11.889839321, -1.0224189813, 1.6030895124  &
   orientation = 2.7997368955, 1.5932959819, 3.1415926536
!
marker create  &
   marker_name = .template_5_brake.PART_46.MARKER_451  &
   adams_id = 451  &
   location = 11.889839321, 1.0224189813, 1.6030895124  &
   orientation = 3.4834484117, 1.5482966717, 3.1415926536
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.PART_46  &
   mass = 3.4246223935E+04  &
   center_of_mass_marker = .template_5_brake.PART_46.cm  &
   ixx = 1.307070096E+05  &
   iyy = 2.307070095E+05  &
   izz = 1.307070095E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_5_brake.PART_46.ELLIPSOID_156  &
   adams_id = 150  &
   center_marker = .template_5_brake.PART_46.MARKER_433  &
   x_scale_factor = 0.2  &
   y_scale_factor = 0.2  &
   z_scale_factor = 0.2
!
part attributes  &
   part_name = .template_5_brake.PART_46  &
   color = GREEN  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
!----------------------------- gel_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.gel_upper_cylinder  &
   adams_id = 4  &
   location = 12.1860123345, -1.4729962566, 1.4343428627  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.gel_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.cm  &
   adams_id = 71  &
   location = -2.0756301703E-04, 6.4023904007E-03, -1.4668262126E-02  &
   orientation = 3.2408439229E-02, 2.0262533312E-02, 6.7576477157E-08
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.inertia_frame  &
   adams_id = 72  &
   location = -2.0756301702E-04, 6.4023904007E-03, -1.4668262126E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.gralin_12  &
   adams_id = 73  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.gralin_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.gralin_16  &
   adams_id = 74  &
   location = -1.267958076E-02, 0.3910980589, -0.6781339507  &
   orientation = 3.2410779571E-02, 0.7042660994, 6.2406670701
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.gralin_16  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.gralin_20  &
   adams_id = 75  &
   location = -1.267958076E-02, 0.3910980589, -0.6781339507  &
   orientation = 3.240911282E-02, 1.6811883747, 3.4277954711
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.gralin_20  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.jxl_joint_j_12  &
   adams_id = 76  &
   location = 0.0, 0.0, 0.5071310811  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.jxl_joint_j_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.jxl_joint_j_4  &
   adams_id = 81  &
   location = 0.0, 0.0, 0.5562289935  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.jxl_joint_j_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.uel_actuator_j_3  &
   adams_id = 83  &
   location = -6.3397903797E-03, 0.1955490295, -0.6998205159  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.uel_actuator_j_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_272  &
   adams_id = 272  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_272  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_411  &
   adams_id = 411  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_411  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_413  &
   adams_id = 413  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_413  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_415  &
   adams_id = 415  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_415  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_446  &
   adams_id = 446  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_446  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.gel_upper_cylinder  &
   mass = 112.770857716  &
   center_of_mass_marker = .template_5_brake.gel_upper_cylinder.cm  &
   inertia_marker = .template_5_brake.gel_upper_cylinder.inertia_frame  &
   ixx = 20.3828607526  &
   iyy = 20.1915756173  &
   izz = 0.6770308822  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_cylinder.gralin_upper_cylinder  &
   adams_id = 1  &
   center_marker = .template_5_brake.gel_upper_cylinder.gralin_12  &
   angle_extent = 6.2831853072  &
   length = 1.4430141621  &
   radius = 9.398E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_upper_cylinder.gralin_upper_cylinder  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_cylinder.gralin_geom  &
   adams_id = 2  &
   center_marker = .template_5_brake.gel_upper_cylinder.gralin_16  &
   angle_extent = 6.2831853072  &
   length = 0.4529277436  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_upper_cylinder.gralin_geom  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_cylinder.gralin_geom3  &
   adams_id = 3  &
   center_marker = .template_5_brake.gel_upper_cylinder.gralin_20  &
   angle_extent = 6.2831853072  &
   length = 0.3937000024  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_upper_cylinder.gralin_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_brake.gel_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ger_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ger_upper_cylinder  &
   adams_id = 5  &
   location = 12.1860123345, 1.4729962566, 1.4343428627  &
   orientation = 2.1796620084, 3.0592631119, 5.3196637838
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ger_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_gearaero_i_1  &
   adams_id = 84  &
   location = 0.0, 0.0, 0.2927550811  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_gearaero_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.cm  &
   adams_id = 85  &
   location = -2.0756301703E-04, -6.4023904007E-03, -1.4668262126E-02  &
   orientation = 3.1091842144, 2.0262533312E-02, 3.141592586
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.inertia_frame  &
   adams_id = 86  &
   location = -2.0756301702E-04, -6.4023904007E-03, -1.4668262126E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.gralin_13  &
   adams_id = 87  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.gralin_13  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.gralin_17  &
   adams_id = 88  &
   location = -1.267958076E-02, -0.3910980589, -0.6781339507  &
   orientation = 3.109181874, 0.7042660994, 3.1841108906
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.gralin_17  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.gralin_21  &
   adams_id = 89  &
   location = -1.267958076E-02, -0.3910980589, -0.6781339507  &
   orientation = 3.1091835408, 1.6811883747, 5.9969824896
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.gralin_21  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.jxr_joint_j_12  &
   adams_id = 90  &
   location = 0.0, 0.0, 0.5071310811  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.jxr_joint_j_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_spring_j_1  &
   adams_id = 92  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_spring_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_damper_j_1  &
   adams_id = 93  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_damper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_stopper_j_1  &
   adams_id = 94  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_stopper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.jxr_joint_j_4  &
   adams_id = 95  &
   location = 0.0, 0.0, 0.5562289935  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.jxr_joint_j_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_actuator_j_3  &
   adams_id = 97  &
   location = -6.3397903797E-03, -0.1955490295, -0.6998205159  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_actuator_j_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_269  &
   adams_id = 269  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_269  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_278  &
   adams_id = 278  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_278  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_417  &
   adams_id = 417  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_417  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_419  &
   adams_id = 419  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_419  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_421  &
   adams_id = 421  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_421  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_444  &
   adams_id = 444  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_444  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ger_upper_cylinder  &
   mass = 112.770857716  &
   center_of_mass_marker = .template_5_brake.ger_upper_cylinder.cm  &
   inertia_marker = .template_5_brake.ger_upper_cylinder.inertia_frame  &
   ixx = 20.3828607526  &
   iyy = 20.1915756173  &
   izz = 0.6770308822  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_cylinder.gralin_upper_cylinder  &
   adams_id = 4  &
   center_marker = .template_5_brake.ger_upper_cylinder.gralin_13  &
   angle_extent = 6.2831853072  &
   length = 1.4430141621  &
   radius = 9.398E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_upper_cylinder.gralin_upper_cylinder  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_cylinder.gralin_geom  &
   adams_id = 5  &
   center_marker = .template_5_brake.ger_upper_cylinder.gralin_17  &
   angle_extent = 6.2831853072  &
   length = 0.4529277436  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_upper_cylinder.gralin_geom  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_cylinder.gralin_geom3  &
   adams_id = 6  &
   center_marker = .template_5_brake.ger_upper_cylinder.gralin_21  &
   angle_extent = 6.2831853072  &
   length = 0.3937000024  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_upper_cylinder.gralin_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_brake.ger_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- gel_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.gel_lower_cylinder  &
   adams_id = 6  &
   location = 12.2383679771, -1.5095002745, 0.6608546166  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.gel_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_463  &
   adams_id = 463  &
   location = 3.2976999835E-04, -0.2788194422, 0.5013550985  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_465  &
   adams_id = 465  &
   location = 3.2976995844E-04, -0.2788194421, 0.5013550985  &
   orientation = 3.1415926536, 1.6178478494, 6.7584612879E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.cm  &
   adams_id = 99  &
   location = 1.6535536877E-05, -1.3980732745E-02, 3.2717040657E-02  &
   orientation = 1.1827369552E-03, 7.8095547608E-02, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.inertia_frame  &
   adams_id = 100  &
   location = 1.653553688E-05, -1.3980732745E-02, 3.2717040657E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.gralin_14  &
   adams_id = 101  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.gralin_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.gralin_22  &
   adams_id = 102  &
   location = 0.0, -5.0742924723E-09, 0.4833620002  &
   orientation = 1.1827369765E-03, 1.5063451472, 6.2648237542
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.gralin_22  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.jxl_joint_j_11  &
   adams_id = 103  &
   location = 0.114150217, -2.6246375424E-02, 0.3816035459  &
   orientation = 3.1906577229, 1.5707962113, 1.5707986779
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.jxl_joint_j_11  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.jxl_joint_i_12  &
   adams_id = 104  &
   location = 0.0, 0.0, -0.268986  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.jxl_joint_i_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.coomarker_1  &
   adams_id = 105  &
   location = 3.2976999835E-04, -0.2788194422, 0.5013550985  &
   orientation = 3.142775392, 1.6352616932, 3.2093366878
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.coomarker_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.uel_spring_i_1  &
   adams_id = 106  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.uel_spring_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.uel_damper_i_1  &
   adams_id = 107  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.uel_damper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.uel_stopper_i_1  &
   adams_id = 108  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.uel_stopper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_266  &
   adams_id = 266  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_266  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_273  &
   adams_id = 273  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_273  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_412  &
   adams_id = 412  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_412  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_414  &
   adams_id = 414  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_414  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_416  &
   adams_id = 416  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_416  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.gel_lower_cylinder  &
   mass = 217.3555691677  &
   center_of_mass_marker = .template_5_brake.gel_lower_cylinder.cm  &
   inertia_marker = .template_5_brake.gel_lower_cylinder.inertia_frame  &
   ixx = 3.3284494628  &
   iyy = 3.1936294  &
   izz = 0.2032330741  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_lower_cylinder.gralin_lower_cylinder  &
   adams_id = 7  &
   center_marker = .template_5_brake.gel_lower_cylinder.gralin_14  &
   angle_extent = 6.2831853072  &
   length = 0.966724  &
   radius = 6.35E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_lower_cylinder.gralin_lower_cylinder  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_lower_cylinder.gralin_geom  &
   adams_id = 8  &
   center_marker = .template_5_brake.gel_lower_cylinder.gralin_22  &
   angle_extent = 6.2831853072  &
   length = 0.425703605  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_lower_cylinder.gralin_geom  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_5_brake.gel_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ger_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ger_lower_cylinder  &
   adams_id = 7  &
   location = 12.2383679771, 1.5095002745, 0.6608546166  &
   orientation = 2.1796620084, 3.0592631119, 5.3196637838
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ger_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_464  &
   adams_id = 464  &
   location = 3.2976999835E-04, 0.2788194422, 0.5013550985  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_467  &
   adams_id = 467  &
   location = 3.2976995844E-04, 0.2788194421, 0.5013550985  &
   orientation = 3.1415926536, 1.5237448042, 6.7584612879E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.cm  &
   adams_id = 109  &
   location = 1.6535536877E-05, 1.3980732745E-02, 3.2717040657E-02  &
   orientation = 3.1404099166, 7.8095547608E-02, 3.1415926536
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.inertia_frame  &
   adams_id = 110  &
   location = 1.653553688E-05, 1.3980732745E-02, 3.2717040657E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.gralin_15  &
   adams_id = 111  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.gralin_15  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.gralin_23  &
   adams_id = 112  &
   location = 0.0, 5.0742924688E-09, 0.4833620002  &
   orientation = 3.1404099166, 1.5063451472, 3.1599542066
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.gralin_23  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.jxr_joint_j_11  &
   adams_id = 113  &
   location = 0.114150217, 2.6246375424E-02, 0.3816035459  &
   orientation = 6.2341202379, 1.5707962113, 1.5707939757
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.jxr_joint_j_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.jxr_joint_i_12  &
   adams_id = 114  &
   location = 0.0, 0.0, -0.268986  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.jxr_joint_i_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.coomarker_2  &
   adams_id = 115  &
   location = 3.2976999835E-04, 0.2788194422, 0.5013550985  &
   orientation = 6.2820025687, 1.6352616932, 6.2154412729
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.coomarker_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.uer_spring_i_1  &
   adams_id = 116  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.uer_spring_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.uer_damper_i_1  &
   adams_id = 117  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.uer_damper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.uer_stopper_i_1  &
   adams_id = 118  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.uer_stopper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_268  &
   adams_id = 268  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_268  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_279  &
   adams_id = 279  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_279  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_418  &
   adams_id = 418  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_418  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_420  &
   adams_id = 420  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_420  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_422  &
   adams_id = 422  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 4.1051141769, 3.0592631119, 0.9619306452
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_422  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ger_lower_cylinder  &
   mass = 217.3555691677  &
   center_of_mass_marker = .template_5_brake.ger_lower_cylinder.cm  &
   inertia_marker = .template_5_brake.ger_lower_cylinder.inertia_frame  &
   ixx = 3.3284494628  &
   iyy = 3.1936294  &
   izz = 0.2032330741  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_lower_cylinder.gralin_lower_cylinder  &
   adams_id = 9  &
   center_marker = .template_5_brake.ger_lower_cylinder.gralin_15  &
   angle_extent = 6.2831853072  &
   length = 0.966724  &
   radius = 6.35E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_lower_cylinder.gralin_lower_cylinder  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_lower_cylinder.gralin_geom  &
   adams_id = 10  &
   center_marker = .template_5_brake.ger_lower_cylinder.gralin_23  &
   angle_extent = 6.2831853072  &
   length = 0.425703605  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_lower_cylinder.gralin_geom  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_5_brake.ger_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_upper_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.gel_upper_dragbrace  &
   adams_id = 8  &
   location = 11.247700263, -1.1306922298, 1.8105711871  &
   orientation = 1.2073242946, 2.3360498626, 4.4547535314
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.gel_upper_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.gel_upper_dragbrace.cm  &
   adams_id = 119  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_dragbrace.inertia_frame  &
   adams_id = 120  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_dragbrace.gralin_24  &
   adams_id = 121  &
   location = 0.0, 0.0, -0.4222750594  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_dragbrace.gralin_24  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_dragbrace.jxl_joint_j_14  &
   adams_id = 122  &
   location = 0.0, 0.0, 0.4222750594  &
   orientation = 3.3685336872, 1.5713226834, 2.335725725
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_dragbrace.jxl_joint_j_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_dragbrace.uel_actuator_i_3  &
   adams_id = 124  &
   location = 0.0, 0.0, 0.4222750594  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_dragbrace.uel_actuator_i_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_dragbrace.MARKER_450  &
   adams_id = 450  &
   location = 0.0, 0.0, -0.4222750594  &
   orientation = 3.3680284403, 1.5707963268, 0.8052995919
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.gel_upper_dragbrace  &
   mass = 6.7539180723  &
   center_of_mass_marker = .template_5_brake.gel_upper_dragbrace.cm  &
   inertia_marker = .template_5_brake.gel_upper_dragbrace.inertia_frame  &
   ixx = 0.4030130421  &
   iyy = 0.4030130421  &
   izz = 3.1372976041E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_dragbrace.gralin_upper_dragbrace  &
   adams_id = 11  &
   center_marker = .template_5_brake.gel_upper_dragbrace.gralin_24  &
   angle_extent = 6.2831853072  &
   length = 0.8445501187  &
   radius = 3.048E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_upper_dragbrace.gralin_upper_dragbrace  &
   color = RED
!
part attributes  &
   part_name = .template_5_brake.gel_upper_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_upper_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ger_upper_dragbrace  &
   adams_id = 9  &
   location = 11.247700263, 1.1306922298, 1.8105711871  &
   orientation = 1.934268359, 2.3360498626, 4.9700244294
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ger_upper_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ger_upper_dragbrace.cm  &
   adams_id = 125  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_dragbrace.inertia_frame  &
   adams_id = 126  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_dragbrace.gralin_25  &
   adams_id = 127  &
   location = 0.0, 0.0, -0.4222750594  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_dragbrace.gralin_25  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_dragbrace.jxr_joint_j_14  &
   adams_id = 128  &
   location = 0.0, 0.0, 0.4222750594  &
   orientation = 6.0562442735, 1.5713226834, 0.8058669286
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_dragbrace.jxr_joint_j_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_dragbrace.uer_actuator_i_3  &
   adams_id = 130  &
   location = 0.0, 0.0, 0.4222750594  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_dragbrace.uer_actuator_i_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_dragbrace.MARKER_452  &
   adams_id = 452  &
   location = 0.0, 0.0, -0.4222750594  &
   orientation = 2.9151568669, 1.5707963268, 0.8052995919
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ger_upper_dragbrace  &
   mass = 6.7539180723  &
   center_of_mass_marker = .template_5_brake.ger_upper_dragbrace.cm  &
   inertia_marker = .template_5_brake.ger_upper_dragbrace.inertia_frame  &
   ixx = 0.4030130421  &
   iyy = 0.4030130421  &
   izz = 3.1372976041E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_dragbrace.gralin_upper_dragbrace  &
   adams_id = 12  &
   center_marker = .template_5_brake.ger_upper_dragbrace.gralin_25  &
   angle_extent = 6.2831853072  &
   length = 0.8445501187  &
   radius = 3.048E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_upper_dragbrace.gralin_upper_dragbrace  &
   color = RED
!
part attributes  &
   part_name = .template_5_brake.ger_upper_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_lower_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.gel_lower_dragbrace  &
   adams_id = 10  &
   location = 11.821751947, -1.3511956141, 1.2178735066  &
   orientation = 1.2008496444, 2.3394561925, 4.4490601006
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.gel_lower_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.gel_lower_dragbrace.cm  &
   adams_id = 131  &
   location = 3.9348735476E-03, 6.8056064573E-03, 2.4978613416E-02  &
   orientation = 2.6173709217, 1.9185797667E-02, 3.1415926536
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_dragbrace.inertia_frame  &
   adams_id = 132  &
   location = 3.9348735476E-03, 6.8056064573E-03, 2.4978613416E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_dragbrace.gralin_26  &
   adams_id = 133  &
   location = 0.0, 0.0, -0.4318055559  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_dragbrace.gralin_26  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_dragbrace.jxl_joint_i_14  &
   adams_id = 134  &
   location = 0.0, 0.0, -0.4318055559  &
   orientation = 3.3697240756, 1.5758698685, 2.3321676841
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_dragbrace.jxl_joint_i_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_dragbrace.jxl_joint_i_10  &
   adams_id = 135  &
   location = 0.0, 0.0, 0.4318055559  &
   orientation = 3.3697240756, 1.5758698685, 2.3321676841
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_dragbrace.jxl_joint_i_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_1  &
   adams_id = 136  &
   location = 7.0772384942E-02, 0.1224052041, 0.1620383572  &
   orientation = 4.1881672485, 1.5707963268, 5.8914619092
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_2  &
   adams_id = 137  &
   location = 0.0, 0.0, 0.1036333334  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_3  &
   adams_id = 138  &
   location = 0.0, 0.0, 0.2072666668  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.gel_lower_dragbrace  &
   mass = 5.6992574801  &
   center_of_mass_marker = .template_5_brake.gel_lower_dragbrace.cm  &
   inertia_marker = .template_5_brake.gel_lower_dragbrace.inertia_frame  &
   ixx = 0.3211055352  &
   iyy = 0.3193778028  &
   izz = 5.107174896E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_lower_dragbrace.gralin_lower_dragbrace  &
   adams_id = 13  &
   center_marker = .template_5_brake.gel_lower_dragbrace.gralin_26  &
   angle_extent = 6.2831853072  &
   length = 0.8636111118  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_lower_dragbrace.gralin_lower_dragbrace  &
   color = PEACH
!
geometry create shape plate  &
   plate_name = .template_5_brake.gel_lower_dragbrace.graarm_uplock_tab  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_1,  &
                 .template_5_brake.gel_lower_dragbrace.graarm_2,  &
                 .template_5_brake.gel_lower_dragbrace.graarm_3  &
   width = 2.54E-02  &
   radius = 1.27E-02
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_lower_dragbrace.graarm_uplock_tab  &
   color = PEACH
!
part attributes  &
   part_name = .template_5_brake.gel_lower_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_lower_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ger_lower_dragbrace  &
   adams_id = 11  &
   location = 11.821751947, 1.3511956141, 1.2178735066  &
   orientation = 1.9407430092, 2.3394561925, 4.9757178601
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ger_lower_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ger_lower_dragbrace.cm  &
   adams_id = 139  &
   location = 3.9348735476E-03, -6.8056064573E-03, 2.4978613416E-02  &
   orientation = 0.5242217319, 1.9185797667E-02, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_dragbrace.inertia_frame  &
   adams_id = 140  &
   location = 3.9348735476E-03, -6.8056064573E-03, 2.4978613416E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_dragbrace.gralin_27  &
   adams_id = 141  &
   location = 0.0, 0.0, -0.4318055559  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_dragbrace.gralin_27  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_dragbrace.jxr_joint_i_14  &
   adams_id = 142  &
   location = 0.0, 0.0, -0.4318055559  &
   orientation = 6.0550538852, 1.5758698685, 0.8094249695
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_dragbrace.jxr_joint_i_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_dragbrace.jxr_joint_i_10  &
   adams_id = 143  &
   location = 0.0, 0.0, 0.4318055559  &
   orientation = 6.0550538852, 1.5758698685, 0.8094249695
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_dragbrace.jxr_joint_i_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_4  &
   adams_id = 144  &
   location = 7.0772384942E-02, -0.1224052041, 0.1620383572  &
   orientation = 2.0950180587, 1.5707963268, 5.8914619092
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_5  &
   adams_id = 145  &
   location = 0.0, 0.0, 0.1036333334  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_6  &
   adams_id = 146  &
   location = 0.0, 0.0, 0.2072666668  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_6  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ger_lower_dragbrace  &
   mass = 5.6992574801  &
   center_of_mass_marker = .template_5_brake.ger_lower_dragbrace.cm  &
   inertia_marker = .template_5_brake.ger_lower_dragbrace.inertia_frame  &
   ixx = 0.3211055352  &
   iyy = 0.3193778028  &
   izz = 5.107174896E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_lower_dragbrace.gralin_lower_dragbrace  &
   adams_id = 14  &
   center_marker = .template_5_brake.ger_lower_dragbrace.gralin_27  &
   angle_extent = 6.2831853072  &
   length = 0.8636111118  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_lower_dragbrace.gralin_lower_dragbrace  &
   color = PEACH
!
geometry create shape plate  &
   plate_name = .template_5_brake.ger_lower_dragbrace.graarm_uplock_tab  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_4,  &
                 .template_5_brake.ger_lower_dragbrace.graarm_5,  &
                 .template_5_brake.ger_lower_dragbrace.graarm_6  &
   width = 2.54E-02  &
   radius = 1.27E-02
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_lower_dragbrace.graarm_uplock_tab  &
   color = PEACH
!
part attributes  &
   part_name = .template_5_brake.ger_lower_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_upper_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.gel_upper_torquearm  &
   adams_id = 12  &
   location = 12.0794524095, -1.4939074516, 0.6646292016  &
   orientation = 4.6160488325, 2.942742088, 1.4763432468
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.gel_upper_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.gel_upper_torquearm.cm  &
   adams_id = 147  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_torquearm.inertia_frame  &
   adams_id = 148  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_torquearm.gralin_11  &
   adams_id = 149  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_torquearm.gralin_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_torquearm.jxl_joint_i_2  &
   adams_id = 150  &
   location = 0.0, 0.0, 0.1383335383  &
   orientation = 4.7721567902, 1.5707958587, 3.0901536529
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_torquearm.jxl_joint_i_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_upper_torquearm.jxl_joint_i_3  &
   adams_id = 151  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 3.2013618942, 1.5193611892, 1.3020014208
!
marker attributes  &
   marker_name = .template_5_brake.gel_upper_torquearm.jxl_joint_i_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.gel_upper_torquearm  &
   mass = 1.5364744752  &
   center_of_mass_marker = .template_5_brake.gel_upper_torquearm.cm  &
   inertia_marker = .template_5_brake.gel_upper_torquearm.inertia_frame  &
   ixx = 1.0048562438E-02  &
   iyy = 1.0048562438E-02  &
   izz = 4.9563593622E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_torquearm.gralin_upper_torquearm  &
   adams_id = 15  &
   center_marker = .template_5_brake.gel_upper_torquearm.gralin_11  &
   angle_extent = 6.2831853072  &
   length = 0.2766670766  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_upper_torquearm.gralin_upper_torquearm  &
   color = GREEN
!
part attributes  &
   part_name = .template_5_brake.gel_upper_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_upper_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ger_upper_torquearm  &
   adams_id = 13  &
   location = 12.0794524095, 1.4939074516, 0.6646292016  &
   orientation = 4.8087291283, 2.942742088, 1.6652494068
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ger_upper_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ger_upper_torquearm.cm  &
   adams_id = 152  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_torquearm.inertia_frame  &
   adams_id = 153  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_torquearm.gralin_28  &
   adams_id = 154  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_torquearm.gralin_28  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_torquearm.jxr_joint_i_2  &
   adams_id = 155  &
   location = 0.0, 0.0, 0.1383335383  &
   orientation = 4.6526211706, 1.5707958587, 5.1439000717E-02
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_torquearm.jxr_joint_i_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_upper_torquearm.jxr_joint_i_3  &
   adams_id = 156  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 6.2234160666, 1.5193611892, 1.8395912327
!
marker attributes  &
   marker_name = .template_5_brake.ger_upper_torquearm.jxr_joint_i_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ger_upper_torquearm  &
   mass = 1.5364744752  &
   center_of_mass_marker = .template_5_brake.ger_upper_torquearm.cm  &
   inertia_marker = .template_5_brake.ger_upper_torquearm.inertia_frame  &
   ixx = 1.0048562438E-02  &
   iyy = 1.0048562438E-02  &
   izz = 4.9563593622E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_torquearm.gralin_upper_torquearm  &
   adams_id = 16  &
   center_marker = .template_5_brake.ger_upper_torquearm.gralin_28  &
   angle_extent = 6.2831853072  &
   length = 0.2766670766  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_upper_torquearm.gralin_upper_torquearm  &
   color = GREEN
!
part attributes  &
   part_name = .template_5_brake.ger_upper_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_lower_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.gel_lower_torquearm  &
   adams_id = 14  &
   location = 12.0993426415, -1.5579375115, 0.4030923612  &
   orientation = 4.7962850637, 0.3762472342, 1.492744074
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.gel_lower_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.gel_lower_torquearm.cm  &
   adams_id = 157  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_torquearm.inertia_frame  &
   adams_id = 158  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_torquearm.gralin_29  &
   adams_id = 159  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_torquearm.gralin_29  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_torquearm.jxl_joint_i_11  &
   adams_id = 160  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 3.1089252352, 1.6612279117, 5.0167167861
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_torquearm.jxl_joint_i_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_lower_torquearm.jxl_joint_i_1  &
   adams_id = 161  &
   location = 0.0, 0.0, 0.1387301713  &
   orientation = 3.1089245675, 1.6612281876, 5.7817305147
!
marker attributes  &
   marker_name = .template_5_brake.gel_lower_torquearm.jxl_joint_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.gel_lower_torquearm  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_brake.gel_lower_torquearm.cm  &
   inertia_marker = .template_5_brake.gel_lower_torquearm.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_lower_torquearm.gralin_lower_torquearm  &
   adams_id = 17  &
   center_marker = .template_5_brake.gel_lower_torquearm.gralin_29  &
   angle_extent = 6.2831853072  &
   length = 0.2774603426  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_lower_torquearm.gralin_lower_torquearm  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_5_brake.gel_lower_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_lower_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ger_lower_torquearm  &
   adams_id = 15  &
   location = 12.0993426415, 1.5579375115, 0.4030923612  &
   orientation = 4.6284928971, 0.3762472342, 1.6488485796
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ger_lower_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ger_lower_torquearm.cm  &
   adams_id = 162  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_torquearm.inertia_frame  &
   adams_id = 163  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_torquearm.gralin_30  &
   adams_id = 164  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_torquearm.gralin_30  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_torquearm.jxr_joint_i_11  &
   adams_id = 165  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 3.2667418385E-02, 1.6612279117, 4.4080611747
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_torquearm.jxr_joint_i_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_lower_torquearm.jxr_joint_i_1  &
   adams_id = 166  &
   location = 0.0, 0.0, 0.1387301713  &
   orientation = 3.266808611E-02, 1.6612281876, 3.6430474461
!
marker attributes  &
   marker_name = .template_5_brake.ger_lower_torquearm.jxr_joint_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ger_lower_torquearm  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_brake.ger_lower_torquearm.cm  &
   inertia_marker = .template_5_brake.ger_lower_torquearm.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_lower_torquearm.gralin_lower_torquearm  &
   adams_id = 18  &
   center_marker = .template_5_brake.ger_lower_torquearm.gralin_30  &
   angle_extent = 6.2831853072  &
   length = 0.2774603426  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_lower_torquearm.gralin_lower_torquearm  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_5_brake.ger_lower_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- gel_connector --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.gel_connector  &
   adams_id = 17  &
   location = 12.0491222568, -1.5512110073, 0.5316382052  &
   orientation = 3.0894127897, 1.6143683629, 5.4075285281
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.gel_connector
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.gel_connector.cm  &
   adams_id = 169  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_connector.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_connector.inertia_frame  &
   adams_id = 170  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_connector.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_connector.gralin_3  &
   adams_id = 171  &
   location = 0.0, 0.0, -6.0070847244E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_connector.gralin_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_connector.jxl_joint_j_1  &
   adams_id = 172  &
   location = -3.2030730841E-08, -3.9921405011E-08, -1.1023458626E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_connector.jxl_joint_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_connector.jxl_joint_j_2  &
   adams_id = 173  &
   location = 0.0, 0.0, 6.0070847244E-02  &
   orientation = 5.7869668181, 1.5707941656, 1.5707923349
!
marker attributes  &
   marker_name = .template_5_brake.gel_connector.jxl_joint_j_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.gel_connector  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_brake.gel_connector.cm  &
   inertia_marker = .template_5_brake.gel_connector.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_connector.gralin_connector  &
   adams_id = 19  &
   center_marker = .template_5_brake.gel_connector.gralin_3  &
   angle_extent = 6.2831853072  &
   length = 0.1201416945  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_connector.gralin_connector  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_brake.gel_connector  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- ger_connector --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ger_connector  &
   adams_id = 18  &
   location = 12.0491222568, 1.5512110073, 0.5316382052  &
   orientation = 5.2179863887E-02, 1.6143683629, 4.0172494327
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ger_connector
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ger_connector.cm  &
   adams_id = 174  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_connector.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_connector.inertia_frame  &
   adams_id = 175  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_connector.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_connector.gralin_4  &
   adams_id = 176  &
   location = 0.0, 0.0, -6.0070847244E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_connector.gralin_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_connector.jxr_joint_j_1  &
   adams_id = 177  &
   location = -3.2030730842E-08, 3.9921405013E-08, -1.1023458626E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_connector.jxr_joint_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_connector.jxr_joint_j_2  &
   adams_id = 178  &
   location = 0.0, 0.0, 6.0070847244E-02  &
   orientation = 3.6378111426, 1.5707941656, 1.5708003187
!
marker attributes  &
   marker_name = .template_5_brake.ger_connector.jxr_joint_j_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ger_connector  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_brake.ger_connector.cm  &
   inertia_marker = .template_5_brake.ger_connector.inertia_frame  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_connector.gralin_connector  &
   adams_id = 20  &
   center_marker = .template_5_brake.ger_connector.gralin_4  &
   angle_extent = 6.2831853072  &
   length = 0.1201416945  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_connector.gralin_connector  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_brake.ger_connector  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- gel_uc_collar --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.gel_uc_collar  &
   adams_id = 19  &
   location = 12.2235346711, -1.4991580222, 0.8799979074  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.gel_uc_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.gel_uc_collar.cm  &
   adams_id = 179  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_uc_collar.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_uc_collar.inertia_frame  &
   adams_id = 180  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_uc_collar.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_uc_collar.gralin_5  &
   adams_id = 181  &
   location = 0.0, 0.0, -0.1089542389  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_uc_collar.gralin_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_uc_collar.jxl_joint_j_3  &
   adams_id = 182  &
   location = 0.1220018852, 5.9907462808E-03, 7.1482951795E-02  &
   orientation = 3.1906577229, 1.5707962113, 1.5707986779
!
marker attributes  &
   marker_name = .template_5_brake.gel_uc_collar.jxl_joint_j_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_uc_collar.jxl_joint_i_4  &
   adams_id = 183  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.gel_uc_collar.jxl_joint_i_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.gel_uc_collar.jxl_joint_j_10  &
   adams_id = 184  &
   location = 0.1095796704, 3.3566796849E-02, -4.6830310723E-02  &
   orientation = 3.4809632466, 1.5707963268, 1.609831873
!
marker attributes  &
   marker_name = .template_5_brake.gel_uc_collar.jxl_joint_j_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.gel_uc_collar  &
   mass = 30.2539444008  &
   center_of_mass_marker = .template_5_brake.gel_uc_collar.cm  &
   inertia_marker = .template_5_brake.gel_uc_collar.inertia_frame  &
   ixx = 0.2417065893  &
   iyy = 0.2417065893  &
   izz = 0.2439829346  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.gel_uc_collar.gralin_uc_collar  &
   adams_id = 21  &
   center_marker = .template_5_brake.gel_uc_collar.gralin_5  &
   angle_extent = 6.2831853072  &
   length = 0.2179084778  &
   radius = 0.127  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.gel_uc_collar.gralin_uc_collar  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_brake.gel_uc_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- ger_uc_collar --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ger_uc_collar  &
   adams_id = 20  &
   location = 12.2235346711, 1.4991580222, 0.8799979074  &
   orientation = 2.1796620084, 3.0592631119, 5.3196637838
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ger_uc_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ger_uc_collar.cm  &
   adams_id = 185  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_uc_collar.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_uc_collar.inertia_frame  &
   adams_id = 186  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_uc_collar.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_uc_collar.gralin_6  &
   adams_id = 187  &
   location = 0.0, 0.0, -0.1089542389  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_uc_collar.gralin_6  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_uc_collar.jxr_joint_j_3  &
   adams_id = 188  &
   location = 0.1220018852, -5.9907462808E-03, 7.1482951795E-02  &
   orientation = 6.2341202379, 1.5707962113, 1.5707939757
!
marker attributes  &
   marker_name = .template_5_brake.ger_uc_collar.jxr_joint_j_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_uc_collar.jxr_joint_i_4  &
   adams_id = 189  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ger_uc_collar.jxr_joint_i_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ger_uc_collar.jxr_joint_j_10  &
   adams_id = 190  &
   location = 0.1095796704, -3.3566796849E-02, -4.6830310723E-02  &
   orientation = 5.9438147141, 1.5707963268, 1.5317607806
!
marker attributes  &
   marker_name = .template_5_brake.ger_uc_collar.jxr_joint_j_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ger_uc_collar  &
   mass = 30.2539444008  &
   center_of_mass_marker = .template_5_brake.ger_uc_collar.cm  &
   inertia_marker = .template_5_brake.ger_uc_collar.inertia_frame  &
   ixx = 0.2417065893  &
   iyy = 0.2417065893  &
   izz = 0.2439829346  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ger_uc_collar.gralin_uc_collar  &
   adams_id = 22  &
   center_marker = .template_5_brake.ger_uc_collar.gralin_6  &
   angle_extent = 6.2831853072  &
   length = 0.2179084778  &
   radius = 0.127  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ger_uc_collar.gralin_uc_collar  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_brake.ger_uc_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------------- _cv_part ----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake._cv_part  &
   adams_id = 2  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake._cv_part
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake._cv_part.marker  &
   adams_id = 300  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake._cv_part.marker  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake._cv_part  &
   mass = 0.0  &
   center_of_mass_marker = .template_5_brake._cv_part.marker  &
   ixx = 0.0  &
   iyy = 0.0  &
   izz = 0.0  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
part attributes  &
   part_name = .template_5_brake._cv_part  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
!------------------------------- ges_dragbrace --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ges_dragbrace  &
   adams_id = 33  &
   location = 6.967855, 0.0, 1.31953  &
   orientation = 4.7123889804, 2.1023053519, 1.5707963268
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ges_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ges_dragbrace.MARKER_448  &
   adams_id = 448  &
   location = 0.0, 0.0, -0.5988736811  &
   orientation = 1.5707963268, 2.1023053519, 4.7123889804
!
marker create  &
   marker_name = .template_5_brake.ges_dragbrace.cm  &
   adams_id = 301  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_dragbrace.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_dragbrace.inertia_frame  &
   adams_id = 302  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_dragbrace.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_dragbrace.gralin_1  &
   adams_id = 303  &
   location = 0.0, 0.0, -0.5988736811  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_dragbrace.gralin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_dragbrace.jxs_joint_i_12  &
   adams_id = 304  &
   location = 0.0, 0.0, 0.5988736811  &
   orientation = 1.5707963268, 2.1023053519, 4.7123889804
!
marker attributes  &
   marker_name = .template_5_brake.ges_dragbrace.jxs_joint_i_12  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ges_dragbrace  &
   mass = 27.3726690382  &
   center_of_mass_marker = .template_5_brake.ges_dragbrace.cm  &
   inertia_marker = .template_5_brake.ges_dragbrace.inertia_frame  &
   ixx = 3.4811540175  &
   iyy = 3.4811540175  &
   izz = 3.5319502313E-02  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ges_dragbrace.gralin_dragbrace_geom  &
   adams_id = 85  &
   center_marker = .template_5_brake.ges_dragbrace.gralin_1  &
   angle_extent = 6.2831853072  &
   length = 1.1977473622  &
   radius = 5.08E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ges_dragbrace.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .template_5_brake.ges_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ges_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ges_upper_cylinder  &
   adams_id = 34  &
   location = 6.1976, 0.0, 1.1938  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ges_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_405  &
   adams_id = 405  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_405  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_407  &
   adams_id = 407  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_407  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_409  &
   adams_id = 409  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_409  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_428  &
   adams_id = 428  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_428  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.cm  &
   adams_id = 306  &
   location = -3.3167643494E-03, 0.0, -1.3382423116E-02  &
   orientation = 1.5707963268, 3.6081853445E-02, 4.7123889804
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.inertia_frame  &
   adams_id = 307  &
   location = -3.3167643494E-03, 0.0, -1.3382423116E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.gralin_2  &
   adams_id = 308  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.gralin_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.gralin_3  &
   adams_id = 309  &
   location = -0.11684, -0.34036, -0.49784  &
   orientation = 2.810913765, 1.0252309147, 3.7260503302
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.gralin_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.gralin_4  &
   adams_id = 310  &
   location = -0.11684, 0.34036, -0.49784  &
   orientation = 0.3306788886, 1.0252309147, 5.6987276306
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.gralin_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_11  &
   adams_id = 311  &
   location = 0.0, 0.0, 0.1143  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_11  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_12  &
   adams_id = 312  &
   location = -0.254, 0.0, 0.1778  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_12  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_spring_j_1  &
   adams_id = 314  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_spring_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_damper_j_1  &
   adams_id = 315  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_damper_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_stopper_j_1  &
   adams_id = 316  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_stopper_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_1  &
   adams_id = 317  &
   location = 0.0, 0.0, 0.336804  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_actuator_j_1  &
   adams_id = 318  &
   location = 0.0, 0.0, 0.336804  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_actuator_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_actuator_j_4  &
   adams_id = 319  &
   location = 0.0, 0.0, 0.336804  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_actuator_j_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_2  &
   adams_id = 2  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_2  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_116  &
   adams_id = 324  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_116  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ges_upper_cylinder  &
   mass = 82.2524279101  &
   center_of_mass_marker = .template_5_brake.ges_upper_cylinder.cm  &
   inertia_marker = .template_5_brake.ges_upper_cylinder.inertia_frame  &
   ixx = 2.7759040478  &
   iyy = 2.6163591859  &
   izz = 0.8272904746  &
   ixy = 0.0  &
   izx = 7.0431892224E-02  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 86  &
   center_marker = .template_5_brake.ges_upper_cylinder.gralin_2  &
   angle_extent = 6.2831853072  &
   length = 0.8636  &
   radius = 0.127  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 87  &
   center_marker = .template_5_brake.ges_upper_cylinder.gralin_3  &
   angle_extent = 6.2831853072  &
   length = 0.4209662086  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 88  &
   center_marker = .template_5_brake.ges_upper_cylinder.gralin_4  &
   angle_extent = 6.2831853072  &
   length = 0.4209662086  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_brake.ges_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ges_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ges_lower_cylinder  &
   adams_id = 35  &
   location = 6.1976, 0.0, 0.9525  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ges_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_378  &
   adams_id = 378  &
   location = -0.1016, 0.0, 0.6191  &
   orientation = 0.0, 1.5707963268, 3.1415926536
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_378  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_406  &
   adams_id = 406  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_406  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_408  &
   adams_id = 408  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_408  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_410  &
   adams_id = 410  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_410  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_1  &
   adams_id = 325  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_1  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.cm  &
   adams_id = 326  &
   location = -2.4871874502E-03, 0.0, 3.4740392449E-02  &
   orientation = 4.7123889804, 1.4181222198E-02, 1.5707963268
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.inertia_frame  &
   adams_id = 327  &
   location = -2.4871874502E-03, 0.0, 3.4740392449E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.gralin_5  &
   adams_id = 328  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.gralin_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.jxs_joint_i_11  &
   adams_id = 330  &
   location = 0.0, 0.0, -0.127  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.jxs_joint_i_11  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.gralin_7  &
   adams_id = 331  &
   location = -3.1496E-02, 0.20955, 0.6445  &
   orientation = 0.0, 1.5707963268, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.gralin_7  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.ues_spring_i_1  &
   adams_id = 332  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.ues_spring_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.ues_damper_i_1  &
   adams_id = 51  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.ues_damper_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.ues_stopper_i_1  &
   adams_id = 333  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.ues_stopper_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.coomarker_2  &
   adams_id = 334  &
   location = -3.1496E-02, 0.0, 0.4445  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.coomarker_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.coomarker_3  &
   adams_id = 335  &
   location = -3.1496E-02, 0.0, 0.4699  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.coomarker_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_3  &
   adams_id = 336  &
   location = -3.1496E-02, -0.20955, 0.6445  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_3  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_4  &
   adams_id = 337  &
   location = -3.1496E-02, 0.20955, 0.6445  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_4  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_6  &
   adams_id = 338  &
   location = -3.1496E-02, 0.20955, 0.6445  &
   orientation = 0.0, 1.5707963268, 3.1415926536
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_6  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_8  &
   adams_id = 339  &
   location = -3.1496E-02, -0.20955, 0.6445  &
   orientation = 0.0, 1.5707963268, 3.1415926536
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_8  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_115  &
   adams_id = 344  &
   location = 0.0, 0.0, -0.4445  &
   orientation = 3.1415926536, 3.1415926536, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_115  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ges_lower_cylinder  &
   mass = 84.8838172052  &
   center_of_mass_marker = .template_5_brake.ges_lower_cylinder.cm  &
   inertia_marker = .template_5_brake.ges_lower_cylinder.inertia_frame  &
   ixx = 6.8342355549  &
   iyy = 6.4494598026  &
   izz = 0.8036506432  &
   ixy = 0.0  &
   izx = -8.5544003848E-02  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ges_lower_cylinder.gralin_geom1  &
   adams_id = 89  &
   center_marker = .template_5_brake.ges_lower_cylinder.gralin_5  &
   angle_extent = 6.2831853072  &
   length = 0.889  &
   radius = 0.1016  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ges_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ges_lower_cylinder.gralin_geom2  &
   adams_id = 90  &
   center_marker = .template_5_brake.ges_lower_cylinder.gralin_7  &
   angle_extent = 6.2831853072  &
   length = 0.4191  &
   radius = 3.048E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ges_lower_cylinder.gralin_geom2  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_5_brake.ges_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ges_upper_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ges_upper_torque_arm  &
   adams_id = 36  &
   location = 6.4897, 0.0, 0.7747  &
   orientation = 1.5707963268, 1.9379701606, 4.7123889804
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ges_upper_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ges_upper_torque_arm.cm  &
   adams_id = 345  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_torque_arm.inertia_frame  &
   adams_id = 346  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_torque_arm.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_torque_arm.gralin_9  &
   adams_id = 347  &
   location = 0.0, 0.0, -0.1768905311  &
   orientation = 1.5707963268, 0.235087806, 4.7123889804
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_torque_arm.gralin_9  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_torque_arm.jxs_joint_j_8  &
   adams_id = 348  &
   location = 9.333456062E-02, 0.0, 0.2127884391  &
   orientation = 0.0, 1.5707963268, 1.9379701606
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_torque_arm.jxs_joint_j_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_upper_torque_arm.jxs_joint_i_10  &
   adams_id = 349  &
   location = 0.0, 0.0, -0.1768905311  &
   orientation = 0.0, 1.5707963268, 1.9379701606
!
marker attributes  &
   marker_name = .template_5_brake.ges_upper_torque_arm.jxs_joint_i_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ges_upper_torque_arm  &
   mass = 0.3898630024  &
   center_of_mass_marker = .template_5_brake.ges_upper_torque_arm.cm  &
   inertia_marker = .template_5_brake.ges_upper_torque_arm.inertia_frame  &
   ixx = 2.5774839559E-03  &
   iyy = 2.5774839559E-03  &
   izz = 3.1440501824E-05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   adams_id = 91  &
   center_marker = .template_5_brake.ges_upper_torque_arm.gralin_9  &
   angle_extent = 6.2831853072  &
   length = 0.4007006863  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   color = GREEN
!
part attributes  &
   part_name = .template_5_brake.ges_upper_torque_arm  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ges_lower_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ges_lower_torque_arm  &
   adams_id = 37  &
   location = 6.477, 0.0, 0.6223  &
   orientation = 1.5707963268, 1.1071487178, 4.7123889804
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ges_lower_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ges_lower_torque_arm.MARKER_379  &
   adams_id = 379  &
   location = 0.1788854382, 0.0, -0.2882291623  &
   orientation = 0.0, 1.5707963268, 1.1071487178
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_torque_arm.MARKER_379  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_torque_arm.cm  &
   adams_id = 350  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_torque_arm.inertia_frame  &
   adams_id = 351  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_torque_arm.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_torque_arm.jxs_joint_i_8  &
   adams_id = 352  &
   location = 8.94427191E-02, 0.0, 0.1540650836  &
   orientation = 0.0, 1.5707963268, 1.1071487178
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_torque_arm.jxs_joint_i_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_lower_torque_arm.gralin_10  &
   adams_id = 353  &
   location = 0.1788854382, 0.0, -0.2882291623  &
   orientation = 4.7123889804, 0.1995335546, 1.5707963268
!
marker attributes  &
   marker_name = .template_5_brake.ges_lower_torque_arm.gralin_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ges_lower_torque_arm  &
   mass = 0.3898630024  &
   center_of_mass_marker = .template_5_brake.ges_lower_torque_arm.cm  &
   inertia_marker = .template_5_brake.ges_lower_torque_arm.inertia_frame  &
   ixx = 2.5774839559E-03  &
   iyy = 2.5774839559E-03  &
   izz = 3.1440501824E-05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   adams_id = 92  &
   center_marker = .template_5_brake.ges_lower_torque_arm.gralin_10  &
   angle_extent = 6.2831853072  &
   length = 0.4512473823  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_5_brake.ges_lower_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------ mts_body_mount_2 ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.mts_body_mount_2  &
   adams_id = 39  &
   location = 6.70433, 0.0, 1.66878  &
   orientation = 0.0, 0.0, 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.mts_body_mount_2
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.mts_body_mount_2.MARKER_427  &
   adams_id = 427  &
   location = -0.50673, 0.0, -4.318E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.mts_body_mount_2.MARKER_427  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.mts_body_mount_2.MARKER_440  &
   adams_id = 440  &
   location = 3.919074959, 0.0, 0.9594677971  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.mts_body_mount_2.MARKER_440  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.mts_body_mount_2.MARKER_447  &
   adams_id = 447  &
   location = 0.77978, 0.0, -4.572E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker create  &
   marker_name = .template_5_brake.mts_body_mount_2.MARKER_109  &
   adams_id = 365  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.mts_body_mount_2.MARKER_109  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.mts_body_mount_2.cm  &
   adams_id = 366  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.mts_body_mount_2.cm  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.mts_body_mount_2  &
   mass = 5000.0  &
   center_of_mass_marker = .template_5_brake.mts_body_mount_2.cm  &
   ixx = 2.9263965343E-04  &
   iyy = 2.9263965343E-04  &
   izz = 2.9263965343E-04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_5_brake.mts_body_mount_2.ELLIPSOID_38  &
   adams_id = 38  &
   center_marker = .template_5_brake.mts_body_mount_2.MARKER_109  &
   x_scale_factor = 0.2  &
   y_scale_factor = 0.2  &
   z_scale_factor = 0.2
!
part attributes  &
   part_name = .template_5_brake.mts_body_mount_2  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- ges_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_brake.ges_collar  &
   adams_id = 40  &
   location = 6.1976, 0.0, 0.809498  &
   orientation = 0.0, 0.0, 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ges_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_brake.ges_collar.jxs_joint_j_10  &
   adams_id = 368  &
   location = 0.127, 0.0, 2.8702E-02  &
   orientation = 0.0, 1.5707963268, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_collar.jxs_joint_j_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_collar.cm  &
   adams_id = 369  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_collar.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_collar.inertia_frame  &
   adams_id = 370  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_collar.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_collar.gralin_24  &
   adams_id = 371  &
   location = 0.0, 0.0, -4.7498E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_collar.gralin_24  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_collar.jxs_joint_i_1  &
   adams_id = 372  &
   location = 0.0, 0.0, 4.7498E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_collar.jxs_joint_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_collar.ues_actuator_i_1  &
   adams_id = 373  &
   location = 0.0, 0.0, 4.7498E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_collar.ues_actuator_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_brake.ges_collar.ues_actuator_i_4  &
   adams_id = 374  &
   location = 0.0, 0.0, 4.7498E-02  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.ges_collar.ues_actuator_i_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_brake.ges_collar  &
   mass = 6.4242828175  &
   center_of_mass_marker = .template_5_brake.ges_collar.cm  &
   inertia_marker = .template_5_brake.ges_collar.inertia_frame  &
   ixx = 8.5080541407E-02  &
   iyy = 8.5080541407E-02  &
   izz = 0.1468542831  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_brake.ges_collar.gralin_collar  &
   adams_id = 93  &
   center_marker = .template_5_brake.ges_collar.gralin_24  &
   angle_extent = 6.2831853072  &
   length = 9.4996E-02  &
   radius = 0.1397  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_brake.ges_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .template_5_brake.ges_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_5_brake.JOINT_51  &
   adams_id = 51  &
   i_marker_name = .template_5_brake.ges_lower_cylinder.MARKER_378  &
   j_marker_name = .template_5_brake.ges_lower_torque_arm.MARKER_379
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_51  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.jolrev_lta_lc_joint  &
   adams_id = 2  &
   i_marker_name = .template_5_brake.gel_lower_torquearm.jxl_joint_i_11  &
   j_marker_name = .template_5_brake.gel_lower_cylinder.jxl_joint_j_11
!
constraint attributes  &
   constraint_name = .template_5_brake.jolrev_lta_lc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.jorrev_lta_lc_joint  &
   adams_id = 3  &
   i_marker_name = .template_5_brake.ger_lower_torquearm.jxr_joint_i_11  &
   j_marker_name = .template_5_brake.ger_lower_cylinder.jxr_joint_j_11
!
constraint attributes  &
   constraint_name = .template_5_brake.jorrev_lta_lc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_brake.jolcyl_lc_uc_joint  &
   adams_id = 4  &
   i_marker_name = .template_5_brake.gel_lower_cylinder.jxl_joint_i_12  &
   j_marker_name = .template_5_brake.gel_upper_cylinder.jxl_joint_j_12
!
constraint attributes  &
   constraint_name = .template_5_brake.jolcyl_lc_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_brake.jorcyl_lc_uc_joint  &
   adams_id = 5  &
   i_marker_name = .template_5_brake.ger_lower_cylinder.jxr_joint_i_12  &
   j_marker_name = .template_5_brake.ger_upper_cylinder.jxr_joint_j_12
!
constraint attributes  &
   constraint_name = .template_5_brake.jorcyl_lc_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_brake.jolrev_ldb_udb_joint  &
   adams_id = 6  &
   i_marker_name = .template_5_brake.gel_lower_dragbrace.jxl_joint_i_14  &
   j_marker_name = .template_5_brake.gel_upper_dragbrace.jxl_joint_j_14
!
constraint attributes  &
   constraint_name = .template_5_brake.jolrev_ldb_udb_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_brake.jorrev_ldb_udb_joint  &
   adams_id = 7  &
   i_marker_name = .template_5_brake.ger_lower_dragbrace.jxr_joint_i_14  &
   j_marker_name = .template_5_brake.ger_upper_dragbrace.jxr_joint_j_14
!
constraint attributes  &
   constraint_name = .template_5_brake.jorrev_ldb_udb_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_brake.jolcyl_lta_connect  &
   adams_id = 12  &
   i_marker_name = .template_5_brake.gel_lower_torquearm.jxl_joint_i_1  &
   j_marker_name = .template_5_brake.gel_connector.jxl_joint_j_1
!
constraint attributes  &
   constraint_name = .template_5_brake.jolcyl_lta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_brake.jorcyl_lta_connect  &
   adams_id = 13  &
   i_marker_name = .template_5_brake.ger_lower_torquearm.jxr_joint_i_1  &
   j_marker_name = .template_5_brake.ger_connector.jxr_joint_j_1
!
constraint attributes  &
   constraint_name = .template_5_brake.jorcyl_lta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.jolrev_uta_connect  &
   adams_id = 14  &
   i_marker_name = .template_5_brake.gel_upper_torquearm.jxl_joint_i_2  &
   j_marker_name = .template_5_brake.gel_connector.jxl_joint_j_2
!
constraint attributes  &
   constraint_name = .template_5_brake.jolrev_uta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.jorrev_uta_connect  &
   adams_id = 15  &
   i_marker_name = .template_5_brake.ger_upper_torquearm.jxr_joint_i_2  &
   j_marker_name = .template_5_brake.ger_connector.jxr_joint_j_2
!
constraint attributes  &
   constraint_name = .template_5_brake.jorrev_uta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.jolrev_uta_collar  &
   adams_id = 16  &
   i_marker_name = .template_5_brake.gel_upper_torquearm.jxl_joint_i_3  &
   j_marker_name = .template_5_brake.gel_uc_collar.jxl_joint_j_3
!
constraint attributes  &
   constraint_name = .template_5_brake.jolrev_uta_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.jorrev_uta_collar  &
   adams_id = 17  &
   i_marker_name = .template_5_brake.ger_upper_torquearm.jxr_joint_i_3  &
   j_marker_name = .template_5_brake.ger_uc_collar.jxr_joint_j_3
!
constraint attributes  &
   constraint_name = .template_5_brake.jorrev_uta_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_brake.jolrev_collar_uc  &
   adams_id = 18  &
   i_marker_name = .template_5_brake.gel_uc_collar.jxl_joint_i_4  &
   j_marker_name = .template_5_brake.gel_upper_cylinder.jxl_joint_j_4
!
constraint attributes  &
   constraint_name = .template_5_brake.jolrev_collar_uc  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_brake.jorrev_collar_uc  &
   adams_id = 19  &
   i_marker_name = .template_5_brake.ger_uc_collar.jxr_joint_i_4  &
   j_marker_name = .template_5_brake.ger_upper_cylinder.jxr_joint_j_4
!
constraint attributes  &
   constraint_name = .template_5_brake.jorrev_collar_uc  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.jolrev_ldb_collar  &
   adams_id = 30  &
   i_marker_name = .template_5_brake.gel_lower_dragbrace.jxl_joint_i_10  &
   j_marker_name = .template_5_brake.gel_uc_collar.jxl_joint_j_10
!
constraint attributes  &
   constraint_name = .template_5_brake.jolrev_ldb_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.jorrev_ldb_collar  &
   adams_id = 31  &
   i_marker_name = .template_5_brake.ger_lower_dragbrace.jxr_joint_i_10  &
   j_marker_name = .template_5_brake.ger_uc_collar.jxr_joint_j_10
!
constraint attributes  &
   constraint_name = .template_5_brake.jorrev_ldb_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_brake.JOINT_56  &
   adams_id = 56  &
   i_marker_name = .template_5_brake.mts_body_mount_2.MARKER_427  &
   j_marker_name = .template_5_brake.ges_upper_cylinder.MARKER_428
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_56  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_brake.JOINT_57  &
   adams_id = 57  &
   i_marker_name = .template_5_brake.PART_46.MARKER_439  &
   j_marker_name = .template_5_brake.mts_body_mount_2.MARKER_440
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_57  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_brake.JOINT_59  &
   adams_id = 59  &
   i_marker_name = .template_5_brake.PART_46.MARKER_443  &
   j_marker_name = .template_5_brake.ger_upper_cylinder.MARKER_444
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_59  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_brake.JOINT_60  &
   adams_id = 60  &
   i_marker_name = .template_5_brake.PART_46.MARKER_445  &
   j_marker_name = .template_5_brake.gel_upper_cylinder.MARKER_446
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_60  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint spherical  &
   joint_name = .template_5_brake.JOINT_61  &
   adams_id = 61  &
   i_marker_name = .template_5_brake.mts_body_mount_2.MARKER_447  &
   j_marker_name = .template_5_brake.ges_dragbrace.MARKER_448
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_61  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_5_brake.JOINT_62  &
   adams_id = 62  &
   i_marker_name = .template_5_brake.PART_46.MARKER_449  &
   j_marker_name = .template_5_brake.gel_upper_dragbrace.MARKER_450
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_62  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_5_brake.JOINT_63  &
   adams_id = 63  &
   i_marker_name = .template_5_brake.PART_46.MARKER_451  &
   j_marker_name = .template_5_brake.ger_upper_dragbrace.MARKER_452
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_63  &
   name_visibility = off
!
constraint create joint spherical  &
   joint_name = .template_5_brake.josrev_lta_uta_joint  &
   adams_id = 39  &
   i_marker_name = .template_5_brake.ges_lower_torque_arm.jxs_joint_i_8  &
   j_marker_name = .template_5_brake.ges_upper_torque_arm.jxs_joint_j_8
!
constraint attributes  &
   constraint_name = .template_5_brake.josrev_lta_uta_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.josrev_uta_uc_joint  &
   adams_id = 41  &
   i_marker_name = .template_5_brake.ges_upper_torque_arm.jxs_joint_i_10  &
   j_marker_name = .template_5_brake.ges_collar.jxs_joint_j_10
!
constraint attributes  &
   constraint_name = .template_5_brake.josrev_uta_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_brake.joscyl_lc_uc_joint  &
   adams_id = 42  &
   i_marker_name = .template_5_brake.ges_lower_cylinder.jxs_joint_i_11  &
   j_marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_11
!
constraint attributes  &
   constraint_name = .template_5_brake.joscyl_lc_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint spherical  &
   joint_name = .template_5_brake.jossph_db_uc_joint  &
   adams_id = 43  &
   i_marker_name = .template_5_brake.ges_dragbrace.jxs_joint_i_12  &
   j_marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_12
!
constraint attributes  &
   constraint_name = .template_5_brake.jossph_db_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_brake.josrev_collar_uc_joint  &
   adams_id = 48  &
   i_marker_name = .template_5_brake.ges_collar.jxs_joint_i_1  &
   j_marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_1
!
constraint attributes  &
   constraint_name = .template_5_brake.josrev_collar_uc_joint  &
   size_of_icons = 5.0E-02
!
!----------------------------------- Forces -----------------------------------!
!
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.thrust  &
   adams_id = 22  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.PART_46.MARKER_461  &
   j_marker_name = .template_5_brake.PART_46.MARKER_462  &
   action_only = on  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.NLG_AIR  &
   adams_id = 11  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.ges_upper_cylinder.MARKER_405  &
   j_marker_name = .template_5_brake.ges_lower_cylinder.MARKER_406  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_brake.NLG_AIR  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.NLG_OIL  &
   adams_id = 12  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.ges_upper_cylinder.MARKER_407  &
   j_marker_name = .template_5_brake.ges_lower_cylinder.MARKER_408  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_brake.NLG_OIL  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.NLG_STOP  &
   adams_id = 13  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.ges_upper_cylinder.MARKER_409  &
   j_marker_name = .template_5_brake.ges_lower_cylinder.MARKER_410  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_brake.NLG_STOP  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.LMLG_AIR  &
   adams_id = 14  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.gel_upper_cylinder.MARKER_411  &
   j_marker_name = .template_5_brake.gel_lower_cylinder.MARKER_412  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_brake.LMLG_AIR  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.LMLG_OIL  &
   adams_id = 15  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.gel_upper_cylinder.MARKER_413  &
   j_marker_name = .template_5_brake.gel_lower_cylinder.MARKER_414  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_brake.LMLG_OIL  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.LMLG_STOP  &
   adams_id = 16  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.gel_upper_cylinder.MARKER_415  &
   j_marker_name = .template_5_brake.gel_lower_cylinder.MARKER_416  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_brake.LMLG_STOP  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.RMLG_AIR  &
   adams_id = 17  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.ger_upper_cylinder.MARKER_417  &
   j_marker_name = .template_5_brake.ger_lower_cylinder.MARKER_418  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_brake.RMLG_AIR  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.RMLG_OIL  &
   adams_id = 18  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.ger_upper_cylinder.MARKER_419  &
   j_marker_name = .template_5_brake.ger_lower_cylinder.MARKER_420  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_brake.RMLG_OIL  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.RMLG_STOP  &
   adams_id = 19  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_brake.ger_upper_cylinder.MARKER_421  &
   j_marker_name = .template_5_brake.ger_lower_cylinder.MARKER_422  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_brake.RMLG_STOP  &
   size_of_icons = 5.0E-02
!
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .template_5_brake.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=30.0 step_size=1.0E-02 model_name=.GCMB"
!
!-------------------------- Adams View UDE Instances --------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
undo begin_block suppress = yes
!
ude create instance  &
   instance_name = .template_5_brake.lumian  &
   definition_name = .MDI.Forces.vpg_road  &
   location = 12.2383679771, 1.5095002745, -0.282740481  &
   orientation = 0.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_5_brake.lumian  &
   color = DimGray  &
   visibility = on
!
ude create instance  &
   instance_name = .template_5_brake.luntai1  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 0.0, 1.5707963268, 0.0
!
ude create instance  &
   instance_name = .template_5_brake.luntai2  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 0.0, 1.5707963268, 0.0
!
ude create instance  &
   instance_name = .template_5_brake.luntai1_2  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 6.229096, -0.20955, 0.308  &
   orientation = 0.0, 1.5707963268, 0.0
!
ude create instance  &
   instance_name = .template_5_brake.luntai2_2  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 6.229096, 0.20955, 0.308  &
   orientation = 0.0, 1.5707963268, 0.0
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_brake.lumian.ref_marker  &
   object_value = .template_5_brake.ground.lumian_ref_1
!
variable modify  &
   variable_name = .template_5_brake.lumian.road_property_file  &
   string_value = "2d_flat.rdf"
!
variable modify  &
   variable_name = .template_5_brake.lumian.road_graphics  &
   string_value = "on"
!
ude modify instance  &
   instance_name = .template_5_brake.lumian
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_brake.luntai1.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_brake.luntai1.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_brake.luntai1.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.vmmrk  &
   object_value = (.template_5_brake.luntai1.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_brake.luntai1.wmmrk  &
   object_value = (.template_5_brake.luntai1.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_brake.luntai1.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.road_property_file  &
   string_value = (.template_5_brake.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_5_brake.luntai1.j_fmarker  &
   object_value = .template_5_brake.ground.luntai1_tire_jf_1
!
variable modify  &
   variable_name = .template_5_brake.luntai1.ref_marker  &
   object_value = (.template_5_brake.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_5_brake.luntai1.wheel_tire_mass  &
   real_value = 45.359237
!
variable modify  &
   variable_name = .template_5_brake.luntai1.Ixx_Iyy  &
   real_value = 2.7215487769
!
variable modify  &
   variable_name = .template_5_brake.luntai1.Izz  &
   real_value = 4.6822344549
!
variable modify  &
   variable_name = .template_5_brake.luntai1.property_file  &
   string_value = "MLG.tir"
!
variable modify  &
   variable_name = .template_5_brake.luntai1.road_name  &
   string_value = (.template_5_brake.lumian)
!
ude modify instance  &
   instance_name = .template_5_brake.luntai1
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker create  &
   marker_name = .template_5_brake.luntai1.wheel_part.MARKER_459  &
   adams_id = 459  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 1.6321930438E-06, 1.5533424893, 0.0
!
marker create  &
   marker_name = .template_5_brake.luntai1.wheel_part.MARKER_468  &
   adams_id = 468  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 3.1415926536, 1.5707963268, 3.1415926536
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_brake.luntai2.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_brake.luntai2.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_brake.luntai2.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.vmmrk  &
   object_value = (.template_5_brake.luntai2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_brake.luntai2.wmmrk  &
   object_value = (.template_5_brake.luntai2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_brake.luntai2.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.road_property_file  &
   string_value = (.template_5_brake.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_5_brake.luntai2.j_fmarker  &
   object_value = .template_5_brake.ground.luntai2_tire_jf_1
!
variable modify  &
   variable_name = .template_5_brake.luntai2.ref_marker  &
   object_value = (.template_5_brake.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_5_brake.luntai2.wheel_tire_mass  &
   real_value = 45.359237
!
variable modify  &
   variable_name = .template_5_brake.luntai2.Ixx_Iyy  &
   real_value = 2.7215487769
!
variable modify  &
   variable_name = .template_5_brake.luntai2.Izz  &
   real_value = 4.6822344549
!
variable modify  &
   variable_name = .template_5_brake.luntai2.property_file  &
   string_value = "MLG.tir"
!
variable modify  &
   variable_name = .template_5_brake.luntai2.road_name  &
   string_value = (.template_5_brake.lumian)
!
ude modify instance  &
   instance_name = .template_5_brake.luntai2
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker create  &
   marker_name = .template_5_brake.luntai2.wheel_part.MARKER_457  &
   adams_id = 457  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 0.0, 1.5707963268, 0.0
!
marker create  &
   marker_name = .template_5_brake.luntai2.wheel_part.MARKER_458  &
   adams_id = 458  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 0.0, 1.5707963268, 0.0
!
marker create  &
   marker_name = .template_5_brake.luntai2.wheel_part.MARKER_466  &
   adams_id = 466  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 3.1415926536, 1.5707963268, 3.1415926536
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.vmmrk  &
   object_value = (.template_5_brake.luntai1_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.wmmrk  &
   object_value = (.template_5_brake.luntai1_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.road_property_file  &
   string_value = (.template_5_brake.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.j_fmarker  &
   object_value = .template_5_brake.ground.luntai1_tire_jf_11
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.ref_marker  &
   object_value = (.template_5_brake.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.wheel_tire_mass  &
   real_value = 13.6077711
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.Ixx_Iyy  &
   real_value = 0.3511675841
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.Izz  &
   real_value = 0.5560153415
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.property_file  &
   string_value = "NLG.tir"
!
variable modify  &
   variable_name = .template_5_brake.luntai1_2.road_name  &
   string_value = (.template_5_brake.lumian)
!
ude modify instance  &
   instance_name = .template_5_brake.luntai1_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker create  &
   marker_name = .template_5_brake.luntai1_2.wheel_part.MARKER_7  &
   adams_id = 376  &
   location = 6.229096, -0.20955, 0.308  &
   orientation = 0.0, 1.5707963268, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.luntai1_2.wheel_part.MARKER_7  &
   size_of_icons = 5.0E-02
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.vmmrk  &
   object_value = (.template_5_brake.luntai2_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.wmmrk  &
   object_value = (.template_5_brake.luntai2_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.road_property_file  &
   string_value = (.template_5_brake.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.j_fmarker  &
   object_value = .template_5_brake.ground.luntai2_tire_jf_11
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.ref_marker  &
   object_value = (.template_5_brake.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.wheel_tire_mass  &
   real_value = 13.6077711
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.Ixx_Iyy  &
   real_value = 0.3511675841
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.Izz  &
   real_value = 0.5560153415
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.property_file  &
   string_value = "NLG.tir"
!
variable modify  &
   variable_name = .template_5_brake.luntai2_2.road_name  &
   string_value = (.template_5_brake.lumian)
!
ude modify instance  &
   instance_name = .template_5_brake.luntai2_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker create  &
   marker_name = .template_5_brake.luntai2_2.wheel_part.MARKER_5  &
   adams_id = 377  &
   location = 6.229096, 0.20955, 0.308  &
   orientation = 0.0, 1.5707963268, 0.0
!
marker attributes  &
   marker_name = .template_5_brake.luntai2_2.wheel_part.MARKER_5  &
   size_of_icons = 5.0E-02
!
undo end_block
!
!--------------------------- UDE Dependent Objects ----------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_5_brake.JOINT_64  &
   adams_id = 64  &
   i_marker_name = .template_5_brake.gel_lower_cylinder.MARKER_465  &
   j_marker_name = .template_5_brake.luntai2.wheel_part.MARKER_466
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_64  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_5_brake.JOINT_65  &
   adams_id = 65  &
   i_marker_name = .template_5_brake.ger_lower_cylinder.MARKER_467  &
   j_marker_name = .template_5_brake.luntai1.wheel_part.MARKER_468
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_65  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_5_brake.JOINT_1  &
   adams_id = 1  &
   i_marker_name = .template_5_brake.luntai2_2.wheel_part.MARKER_5  &
   j_marker_name = .template_5_brake.ges_lower_cylinder.MARKER_6
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_1  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_brake.JOINT_2  &
   adams_id = 49  &
   i_marker_name = .template_5_brake.luntai1_2.wheel_part.MARKER_7  &
   j_marker_name = .template_5_brake.ges_lower_cylinder.MARKER_8
!
constraint attributes  &
   constraint_name = .template_5_brake.JOINT_2  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.LMLG_Tb  &
   adams_id = 20  &
   type_of_freedom = rotational  &
   i_marker_name = .template_5_brake.luntai2.wheel_part.MARKER_457  &
   j_marker_name = .template_5_brake.luntai2.wheel_part.MARKER_458  &
   action_only = on  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_5_brake.RLMG_Tb  &
   adams_id = 21  &
   type_of_freedom = rotational  &
   i_marker_name = .template_5_brake.luntai1.wheel_part.MARKER_459  &
   j_marker_name = .template_5_brake.ground.MARKER_460  &
   action_only = on  &
   function = ""
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry create shape force  &
   force_name = .template_5_brake.Driving_force_force_graphic_1  &
   adams_id = 261  &
   force_element_name = .template_5_brake.thrust  &
   applied_at_marker_name = .template_5_brake.PART_46.MARKER_461
!
geometry create shape force  &
   force_name = .template_5_brake.SFORCE_20_force_graphic_1  &
   adams_id = 211  &
   force_element_name = .template_5_brake.LMLG_Tb  &
   applied_at_marker_name = .template_5_brake.luntai2.wheel_part.MARKER_457
!
geometry create shape force  &
   force_name = .template_5_brake.SFORCE_21_force_graphic_1  &
   adams_id = 212  &
   force_element_name = .template_5_brake.RLMG_Tb  &
   applied_at_marker_name = .template_5_brake.luntai1.wheel_part.MARKER_459
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   z_component_gravity = -9.81
!
force attributes  &
   force_name = .template_5_brake.gravity  &
   size_of_icons = 5.0E-02
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------------- Measures ----------------------------------!
!
!
measure create object  &
   measure_name = .template_5_brake.Vw  &
   from_first = yes  &
   object = .template_5_brake.JOINT_64  &
   characteristic = angular_velocity  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_5_brake.Vw  &
   color = WHITE
!
measure create point  &
   measure_name = .template_5_brake.js_sd  &
   point = .template_5_brake.PART_46.cm  &
   characteristic = translational_velocity  &
   component = x_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_5_brake.js_sd  &
   color = WHITE
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_5_brake.mts_body_mount_2.minor_role  &
   string_value = "inherit"
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
!---------------------------- Function definitions ----------------------------!
!
!
data_element modify variable  &
   variable_name = .template_5_brake.NLG_V  &
   function = "-1*VR(.template_5_brake.ges_upper_cylinder.MARKER_2,.template_5_brake.ges_lower_cylinder.MARKER_1)"
!
data_element modify variable  &
   variable_name = .template_5_brake.LMLG_S  &
   function = ".template_5_brake.MLG_S0-DM(.template_5_brake.gel_upper_cylinder.MARKER_272,.template_5_brake.gel_lower_cylinder.MARKER_273)"
!
data_element modify variable  &
   variable_name = .template_5_brake.RMLG_S  &
   function = ".template_5_brake.MLG_S0-DM(.template_5_brake.ger_upper_cylinder.MARKER_278,.template_5_brake.ger_lower_cylinder.MARKER_279)"
!
data_element modify variable  &
   variable_name = .template_5_brake.LMLG_V  &
   function = "-1*VR(.template_5_brake.gel_upper_cylinder.MARKER_272,.template_5_brake.gel_lower_cylinder.MARKER_273)"
!
data_element modify variable  &
   variable_name = .template_5_brake.RMLG_V  &
   function = "-1*VR(.template_5_brake.ger_upper_cylinder.MARKER_278,.template_5_brake.ger_lower_cylinder.MARKER_279)"
!
data_element modify variable  &
   variable_name = .template_5_brake.NLG_S  &
   function = ".template_5_brake.NLG_S0-DM(.template_5_brake.ges_upper_cylinder.MARKER_2,.template_5_brake.ges_lower_cylinder.MARKER_1)"
!
data_element modify variable  &
   variable_name = .template_5_brake.slip_ratio  &
   function = "1-((-.template_5_brake.Vw*0.457)/.template_5_brake.js_sd)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.thrust  &
   function = "-300000*2/3.14*atan(.template_5_brake.Vx-.template_5_brake.js_sd)*(STEP(TIME,0,0,1.2,1)-STEP(TIME,3.3,0,3.5,1))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.NLG_AIR  &
   function = "1*.template_5_brake.NLG_A_LOW*(.template_5_brake.NLG_P_LOW*(.template_5_brake.NLG_V_LOW/(.template_5_brake.NLG_V_LOW-.template_5_brake.NLG_A_LOW*(.template_5_brake.NLG_S0-DM(.template_5_brake.ges_upper_cylinder.MARKER_2,.template_5_brake.ges_lower_cylinder.MARKER_1))))**1.1-.template_5_brake.Patm)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.NLG_OIL  &
   function = "IF(VARVAL(.template_5_brake.NLG_V):1*-1*(VARVAL(.template_5_brake.NLG_V)*0.5*(VARVAL(.template_5_brake.NLG_V)-ABS(VARVAL(.template_5_brake.NLG_V)))*((.template_5_brake.MLG_rho_Oil*.template_5_brake.NLG_A_MAIN_OIL**3/(2*.template_5_brake.NLG_RET_Cd**2*.template_5_brake.NLG_A_MAIN_NEG**2))+(.template_5_brake.MLG_rho_Oil*.template_5_brake.NLG_A_RET_OIL**3/(2*.template_5_brake.NLG_MAIN_Cd**2*.template_5_brake.NLG_A_RET_NEG**2)))),0,1*VARVAL(.template_5_brake.NLG_V)*0.5*(VARVAL(.template_5_brake.NLG_V)+ABS(VARVAL(.template_5_brake.NLG_V)))*((.template_5_brake.MLG_rho_Oil*.template_5_brake.NLG_A_MAIN_OIL**3/(2*.template_5_brake.NLG_RET_Cd**2*.template_5_brake.NLG_A_MAIN_POS**2))+(.template_5_brake.MLG_rho_Oil*.template_5_brake.NLG_A_RET_OIL**3/(2*.template_5_brake.NLG_MAIN_Cd**2*.template_5_brake.NLG_A_RET_POS**2))))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.NLG_STOP  &
   function = "IF(.template_5_brake.NLG_S0-DM(.template_5_brake.ges_upper_cylinder.MARKER_2,.template_5_brake.ges_lower_cylinder.MARKER_1) :1.0E+09*(.template_5_brake.NLG_S0-DM(.template_5_brake.ges_upper_cylinder.MARKER_2,.template_5_brake.ges_lower_cylinder.MARKER_1)), 0 , 0 )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.LMLG_AIR  &
   function = ".template_5_brake.MLG_A_LOW*(.template_5_brake.MLG_P_LOW*(.template_5_brake.MLG_V_LOW/(.template_5_brake.MLG_V_LOW-.template_5_brake.MLG_A_LOW*VARVAL(.template_5_brake.LMLG_S)))**1.1-.template_5_brake.Patm)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.LMLG_OIL  &
   function = "IF(VARVAL(.template_5_brake.LMLG_V):2*-1*(VARVAL(.template_5_brake.LMLG_V)*0.5*(VARVAL(.template_5_brake.LMLG_V)-ABS(VARVAL(.template_5_brake.LMLG_V)))*((.template_5_brake.MLG_rho_Oil*.template_5_brake.MLG_A_MAIN_OIL**3/(2*.template_5_brake.MLG_RET_Cd**2*.template_5_brake.MLG_A_MAIN_NEG**2))+(.template_5_brake.MLG_rho_Oil*.template_5_brake.MLG_A_RET_OIL**3/(2*.template_5_brake.MLG_MAIN_Cd**2*.template_5_brake.MLG_A_RET_NEG**2)))),0,2*VARVAL(.template_5_brake.LMLG_V)*0.5*(VARVAL(.template_5_brake.LMLG_V)+ABS(VARVAL(.template_5_brake.LMLG_V)))*((.template_5_brake.MLG_rho_Oil*.template_5_brake.MLG_A_MAIN_OIL**3/(2*.template_5_brake.MLG_RET_Cd**2*.template_5_brake.MLG_A_MAIN_POS**2))+(.template_5_brake.MLG_rho_Oil*.template_5_brake.MLG_A_RET_OIL**3/(2*.template_5_brake.MLG_MAIN_Cd**2*.template_5_brake.MLG_A_RET_POS**2))))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.LMLG_STOP  &
   function = "IF(.template_5_brake.MLG_S0-DM(.template_5_brake.gel_upper_cylinder.MARKER_272,.template_5_brake.gel_lower_cylinder.MARKER_273) :1.0E+09*(.template_5_brake.MLG_S0-DM(.template_5_brake.gel_upper_cylinder.MARKER_272,.template_5_brake.gel_lower_cylinder.MARKER_273)) , 0 , 0 )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.RMLG_AIR  &
   function = ".template_5_brake.MLG_A_LOW*(.template_5_brake.MLG_P_LOW*(.template_5_brake.MLG_V_LOW/(.template_5_brake.MLG_V_LOW-.template_5_brake.MLG_A_LOW*VARVAL(.template_5_brake.RMLG_S)))**1.1-.template_5_brake.Patm)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.RMLG_OIL  &
   function = "IF(VARVAL(.template_5_brake.RMLG_V):2*-1*(VARVAL(.template_5_brake.RMLG_V)*0.5*(VARVAL(.template_5_brake.RMLG_V)-ABS(VARVAL(.template_5_brake.RMLG_V)))*((.template_5_brake.MLG_rho_Oil*.template_5_brake.MLG_A_MAIN_OIL**3/(2*.template_5_brake.MLG_RET_Cd**2*.template_5_brake.MLG_A_MAIN_NEG**2))+(.template_5_brake.MLG_rho_Oil*.template_5_brake.MLG_A_RET_OIL**3/(2*.template_5_brake.MLG_MAIN_Cd**2*.template_5_brake.MLG_A_RET_NEG**2)))),0,2*VARVAL(.template_5_brake.RMLG_V)*0.5*(VARVAL(.template_5_brake.RMLG_V)+ABS(VARVAL(.template_5_brake.RMLG_V)))*((.template_5_brake.MLG_rho_Oil*.template_5_brake.MLG_A_MAIN_OIL**3/(2*.template_5_brake.MLG_RET_Cd**2*.template_5_brake.MLG_A_MAIN_POS**2))+(.template_5_brake.MLG_rho_Oil*.template_5_brake.MLG_A_RET_OIL**3/(2*.template_5_brake.MLG_MAIN_Cd**2*.template_5_brake.MLG_A_RET_POS**2))))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.RMLG_STOP  &
   function = "IF(.template_5_brake.MLG_S0-DM(.template_5_brake.ger_upper_cylinder.MARKER_278,.template_5_brake.ger_lower_cylinder.MARKER_279) :1.0E+09*(.template_5_brake.MLG_S0-DM(.template_5_brake.ger_upper_cylinder.MARKER_278,.template_5_brake.ger_lower_cylinder.MARKER_279)) , 0 ,0 )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.LMLG_Tb  &
   function = "if(vx(.template_5_brake.PART_46.cm,.template_5_brake.ground.MARKER_456):if(time-8:0,0,.template_5_brake.MLG_Tb),0,0)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_brake.RLMG_Tb  &
   function = "if(vx(.template_5_brake.PART_46.cm,.template_5_brake.ground.MARKER_456):if(time-8:0,0,.template_5_brake.MLG_Tb),0,0)"
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_brake.lumian
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_brake.luntai1
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_brake.luntai2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_brake.luntai1_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_brake.luntai2_2
!
!------------------------- Part IC Reference Markers --------------------------!
!
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_brake.luntai1.wheel_part  &
   vm = .template_5_brake.luntai1.wheel_part.wheel_cm  &
   wm = .template_5_brake.luntai1.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_brake.luntai1.belt_part  &
   vm = .template_5_brake.luntai1.wheel_part.wheel_cm  &
   wm = .template_5_brake.luntai1.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_brake.luntai2.wheel_part  &
   vm = .template_5_brake.luntai2.wheel_part.wheel_cm  &
   wm = .template_5_brake.luntai2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_brake.luntai2.belt_part  &
   vm = .template_5_brake.luntai2.wheel_part.wheel_cm  &
   wm = .template_5_brake.luntai2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_brake.luntai1_2.wheel_part  &
   vm = .template_5_brake.luntai1_2.wheel_part.wheel_cm  &
   wm = .template_5_brake.luntai1_2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_brake.luntai1_2.belt_part  &
   vm = .template_5_brake.luntai1_2.wheel_part.wheel_cm  &
   wm = .template_5_brake.luntai1_2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_brake.luntai2_2.wheel_part  &
   vm = .template_5_brake.luntai2_2.wheel_part.wheel_cm  &
   wm = .template_5_brake.luntai2_2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_brake.luntai2_2.belt_part  &
   vm = .template_5_brake.luntai2_2.wheel_part.wheel_cm  &
   wm = .template_5_brake.luntai2_2.wheel_part.wheel_cm
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.cfl_spin_axis_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({180.0, 180.0, 180.0}degrees, .template_5_brake.ground.cfl_spin_axis_1))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.cfr_spin_axis_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({-180.0, -180.0, -180.0}degrees, .template_5_brake.ground.cfr_spin_axis_1))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_axial_reference  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_lc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_lc_bot, .template_5_brake.ground.hpl_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_axial_reference  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_lc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_lc_bot, .template_5_brake.ground.hpr_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_uc_bot  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 21.18}inch, .template_5_brake.ground.cfl_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_uc_bot  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 21.18}inch, .template_5_brake.ground.cfr_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_uc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_uc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_lc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 38.06}inch, .template_5_brake.ground.cfl_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_lc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 38.06}inch, .template_5_brake.ground.cfr_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_5_brake.ground.hpl_uc_top, .template_5_brake.ground.hpl_lc_bot, 0.59 * DM(.template_5_brake.ground.hpl_uc_top, .template_5_brake.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_uc_top, .template_5_brake.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_5_brake.ground.hpr_uc_top, .template_5_brake.ground.hpr_lc_bot, 0.59 * DM(.template_5_brake.ground.hpr_uc_top, .template_5_brake.ground.hpr_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_uc_top, .template_5_brake.ground.hpr_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_collar_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_5_brake.ground.hpl_uc_top, .template_5_brake.ground.hpl_lc_bot, 0.7 * DM(.template_5_brake.ground.hpl_uc_top, .template_5_brake.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_uc_top, .template_5_brake.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_collar_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_5_brake.ground.hpr_uc_top, .template_5_brake.ground.hpr_lc_bot, 0.7 * DM(.template_5_brake.ground.hpr_uc_top, .template_5_brake.ground.hpr_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_uc_top, .template_5_brake.ground.hpr_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_plane_ref_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.cfl_plane_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, -90.0, 0.0}degrees, .template_5_brake.ground.cfl_plane_ref))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_plane_ref_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.cfr_plane_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_5_brake.ground.cfr_plane_ref))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_spin_axis_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_wheel_center, .template_5_brake.ground.hpl_ob_axle, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_spin_axis_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_wheel_center, .template_5_brake.ground.hpr_ob_axle, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_ldb_geompt_1  &
   location =   &
      (LOC_ALONG_LINE(.template_5_brake.ground.hpl_ldb_udb_atch_1, .template_5_brake.ground.hpl_ldb_collar_atch_1, 0.62 * DM(.template_5_brake.ground.hpl_ldb_udb_atch_1, .template_5_brake.ground.hpl_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_ldb_geompt_1  &
   location =   &
      (LOC_ALONG_LINE(.template_5_brake.ground.hpr_ldb_udb_atch_1, .template_5_brake.ground.hpr_ldb_collar_atch_1, 0.62 * DM(.template_5_brake.ground.hpr_ldb_udb_atch_1, .template_5_brake.ground.hpr_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_ldb_geompt_2  &
   location =   &
      (LOC_ALONG_LINE(.template_5_brake.ground.hpl_ldb_udb_atch_1, .template_5_brake.ground.hpl_ldb_collar_atch_1, 0.74 * DM(.template_5_brake.ground.hpl_ldb_udb_atch_1, .template_5_brake.ground.hpl_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_ldb_geompt_2  &
   location =   &
      (LOC_ALONG_LINE(.template_5_brake.ground.hpr_ldb_udb_atch_1, .template_5_brake.ground.hpr_ldb_collar_atch_1, 0.74 * DM(.template_5_brake.ground.hpr_ldb_udb_atch_1, .template_5_brake.ground.hpr_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo))
!
marker modify  &
   marker_name = .template_5_brake.ground.lumian_ref_1  &
   location =   &
      (.template_5_brake.lumian.location)  &
   orientation =   &
      (.template_5_brake.lumian.orientation)
!
marker modify  &
   marker_name = .template_5_brake.ground.cfl_spin_axis1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_wheel_center1, .template_5_brake.ground.hpl_ob_axle1, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfr_spin_axis1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_wheel_center1, .template_5_brake.ground.hpr_ob_axle1, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfs_nlg_axle_lowpoint  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hps_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo1))
!
marker modify  &
   marker_name = .template_5_brake.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_5_brake.ground.hps_uc_bot, .template_5_brake.ground.hps_uc_top, 0.11 * DM(.template_5_brake.ground.hps_uc_bot, .template_5_brake.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_uc_bot, .template_5_brake.ground.hps_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_cylinder))  &
   relative_to = .template_5_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_cylinder.gralin_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.cfl_uc_top, .template_5_brake.ground.cfl_uc_bot, "Z"))  &
   relative_to = .template_5_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_cylinder.gralin_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_ib_uc_sf_atch, .template_5_brake.ground.hpl_uc_geompt, "Z"))  &
   relative_to = .template_5_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_cylinder.gralin_20  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_ib_uc_sf_atch, .template_5_brake.ground.hpl_uc_top, "Z"))  &
   relative_to = .template_5_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_cylinder.uel_actuator_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_uc_sf_atch))  &
   relative_to = .template_5_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_cylinder.gralin_upper_cylinder  &
   length = (DM(.template_5_brake.ground.cfl_uc_top, .template_5_brake.ground.cfl_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_cylinder.gralin_geom  &
   length = (DM(.template_5_brake.ground.hpl_ib_uc_sf_atch, .template_5_brake.ground.hpl_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_cylinder.gralin_geom3  &
   length = (DM(.template_5_brake.ground.hpl_ib_uc_sf_atch, .template_5_brake.ground.hpl_uc_top))
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_cylinder.MARKER_446  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_uc_top))  &
   relative_to = .template_5_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_gearaero_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_lc_top))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_cylinder))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.gralin_13  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.cfr_uc_top, .template_5_brake.ground.cfr_uc_bot, "Z"))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.gralin_17  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_ib_uc_sf_atch, .template_5_brake.ground.hpr_uc_geompt, "Z"))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.gralin_21  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_ib_uc_sf_atch, .template_5_brake.ground.hpr_uc_top, "Z"))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_uc_top))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_uc_top))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_uc_top))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.uer_actuator_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_uc_sf_atch))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_cylinder.gralin_upper_cylinder  &
   length = (DM(.template_5_brake.ground.cfr_uc_top, .template_5_brake.ground.cfr_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_cylinder.gralin_geom  &
   length = (DM(.template_5_brake.ground.hpr_ib_uc_sf_atch, .template_5_brake.ground.hpr_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_cylinder.gralin_geom3  &
   length = (DM(.template_5_brake.ground.hpr_ib_uc_sf_atch, .template_5_brake.ground.hpr_uc_top))
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_269  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_uc_top))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_cylinder.MARKER_444  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_uc_top))  &
   relative_to = .template_5_brake.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_lower_cylinder))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.gralin_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.cfl_lc_top, .template_5_brake.ground.hpl_lc_bot, "Z"))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.gralin_22  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_ib_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_ib_axle, .template_5_brake.ground.hpl_ob_axle, "Z"))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.jxl_joint_j_11  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_lta_connect_atch_1, .template_5_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.jxl_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_cylinder.jxl_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_cylinder.jxl_joint_j_12))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.coomarker_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_spin_axis))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_spin_axis))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.uel_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_lc_top))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.uel_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_lc_top))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.uel_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_lc_top))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_lower_cylinder.gralin_lower_cylinder  &
   length = (DM(.template_5_brake.ground.cfl_lc_top, .template_5_brake.ground.hpl_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_lower_cylinder.gralin_geom  &
   length = (DM(.template_5_brake.ground.hpl_ib_axle, .template_5_brake.ground.hpl_ob_axle))
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_cylinder.MARKER_463  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_wheel_center))  &
   relative_to = .template_5_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_lower_cylinder))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.gralin_15  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.cfr_lc_top, .template_5_brake.ground.hpr_lc_bot, "Z"))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.gralin_23  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_ib_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_ib_axle, .template_5_brake.ground.hpr_ob_axle, "Z"))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.jxr_joint_j_11  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_lta_connect_atch_1, .template_5_brake.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.jxr_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_cylinder.jxr_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_cylinder.jxr_joint_j_12))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.coomarker_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_spin_axis))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_spin_axis))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.uer_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_lc_top))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.uer_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_lc_top))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.uer_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_lc_top))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_lower_cylinder.gralin_lower_cylinder  &
   length = (DM(.template_5_brake.ground.cfr_lc_top, .template_5_brake.ground.hpr_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_lower_cylinder.gralin_geom  &
   length = (DM(.template_5_brake.ground.hpr_ib_axle, .template_5_brake.ground.hpr_ob_axle))
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_cylinder.MARKER_464  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_wheel_center))  &
   relative_to = .template_5_brake.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_dragbrace))  &
   relative_to = .template_5_brake.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_dragbrace.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_udb_spndl_atch_1, .template_5_brake.ground.hpl_ldb_udb_atch_1, "Z"))  &
   relative_to = .template_5_brake.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_dragbrace.jxl_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_5_brake.ground.cfl_plane_ref_2, "Z+Z"), .template_5_brake.gel_upper_dragbrace))  &
   relative_to = .template_5_brake.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_dragbrace.uel_actuator_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_ldb_udb_atch_1))  &
   relative_to = .template_5_brake.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_dragbrace.gralin_upper_dragbrace  &
   length = (DM(.template_5_brake.ground.hpl_udb_spndl_atch_1, .template_5_brake.ground.hpl_ldb_udb_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_dragbrace.MARKER_450  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_udb_spndl_atch_1))  &
   relative_to = .template_5_brake.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_dragbrace))  &
   relative_to = .template_5_brake.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_dragbrace.gralin_25  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_udb_spndl_atch_1, .template_5_brake.ground.hpr_ldb_udb_atch_1, "Z"))  &
   relative_to = .template_5_brake.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_dragbrace.jxr_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_5_brake.ground.cfr_plane_ref_2, "Z+Z"), .template_5_brake.ger_upper_dragbrace))  &
   relative_to = .template_5_brake.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_dragbrace.uer_actuator_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_ldb_udb_atch_1))  &
   relative_to = .template_5_brake.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_dragbrace.gralin_upper_dragbrace  &
   length = (DM(.template_5_brake.ground.hpr_udb_spndl_atch_1, .template_5_brake.ground.hpr_ldb_udb_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_dragbrace.MARKER_452  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_udb_spndl_atch_1))  &
   relative_to = .template_5_brake.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_lower_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_lower_dragbrace))  &
   relative_to = .template_5_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_dragbrace.gralin_26  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_ldb_udb_atch_1, .template_5_brake.ground.hpl_ldb_collar_atch_1, "Z"))  &
   relative_to = .template_5_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_dragbrace.jxl_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_dragbrace.jxl_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_dragbrace.jxl_joint_j_14))  &
   relative_to = .template_5_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_dragbrace.jxl_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_uc_collar.jxl_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_uc_collar.jxl_joint_j_10))  &
   relative_to = .template_5_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_uplock_tab))  &
   orientation =   &
      (ORI_IN_PLANE(.template_5_brake.ground.hpl_uplock_tab, .template_5_brake.ground.cfl_ldb_geompt_1, .template_5_brake.ground.cfl_ldb_geompt_2, "X_XY"))  &
   relative_to = .template_5_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_ldb_geompt_1))  &
   relative_to = .template_5_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_dragbrace.graarm_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_ldb_geompt_2))  &
   relative_to = .template_5_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_lower_dragbrace.gralin_lower_dragbrace  &
   length = (DM(.template_5_brake.ground.hpl_ldb_udb_atch_1, .template_5_brake.ground.hpl_ldb_collar_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_lower_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_lower_dragbrace))  &
   relative_to = .template_5_brake.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_dragbrace.gralin_27  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_ldb_udb_atch_1, .template_5_brake.ground.hpr_ldb_collar_atch_1, "Z"))  &
   relative_to = .template_5_brake.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_dragbrace.jxr_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_dragbrace.jxr_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_dragbrace.jxr_joint_j_14))  &
   relative_to = .template_5_brake.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_dragbrace.jxr_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_uc_collar.jxr_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_uc_collar.jxr_joint_j_10))  &
   relative_to = .template_5_brake.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_uplock_tab))  &
   orientation =   &
      (ORI_IN_PLANE(.template_5_brake.ground.hpr_uplock_tab, .template_5_brake.ground.cfr_ldb_geompt_1, .template_5_brake.ground.cfr_ldb_geompt_2, "X_XY"))  &
   relative_to = .template_5_brake.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_ldb_geompt_1))  &
   relative_to = .template_5_brake.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_dragbrace.graarm_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_ldb_geompt_2))  &
   relative_to = .template_5_brake.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_lower_dragbrace.gralin_lower_dragbrace  &
   length = (DM(.template_5_brake.ground.hpr_ldb_udb_atch_1, .template_5_brake.ground.hpr_ldb_collar_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_torquearm))  &
   relative_to = .template_5_brake.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_torquearm.gralin_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_uta_collar_atch_1, .template_5_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_torquearm.jxl_joint_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_connector.jxl_joint_j_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_connector.jxl_joint_j_2))  &
   relative_to = .template_5_brake.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_upper_torquearm.jxl_joint_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_uc_collar.jxl_joint_j_3))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_uc_collar.jxl_joint_j_3))  &
   relative_to = .template_5_brake.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_upper_torquearm.gralin_upper_torquearm  &
   length = (DM(.template_5_brake.ground.hpl_uta_collar_atch_1, .template_5_brake.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_torquearm))  &
   relative_to = .template_5_brake.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_torquearm.gralin_28  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_uta_collar_atch_1, .template_5_brake.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_torquearm.jxr_joint_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_connector.jxr_joint_j_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_connector.jxr_joint_j_2))  &
   relative_to = .template_5_brake.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_upper_torquearm.jxr_joint_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_uc_collar.jxr_joint_j_3))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_uc_collar.jxr_joint_j_3))  &
   relative_to = .template_5_brake.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_upper_torquearm.gralin_upper_torquearm  &
   length = (DM(.template_5_brake.ground.hpr_uta_collar_atch_1, .template_5_brake.ground.hpr_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_lower_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_lower_torquearm))  &
   relative_to = .template_5_brake.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_torquearm.gralin_29  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_lta_lc_atch_1, .template_5_brake.ground.hpl_lta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_torquearm.jxl_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_lower_cylinder.jxl_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_lower_cylinder.jxl_joint_j_11))  &
   relative_to = .template_5_brake.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_lower_torquearm.jxl_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_connector.jxl_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_connector.jxl_joint_j_1))  &
   relative_to = .template_5_brake.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_lower_torquearm.gralin_lower_torquearm  &
   length = (DM(.template_5_brake.ground.hpl_lta_lc_atch_1, .template_5_brake.ground.hpl_lta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_lower_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_lower_torquearm))  &
   relative_to = .template_5_brake.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_torquearm.gralin_30  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_lta_lc_atch_1, .template_5_brake.ground.hpr_lta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_torquearm.jxr_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_lower_cylinder.jxr_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_lower_cylinder.jxr_joint_j_11))  &
   relative_to = .template_5_brake.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_lower_torquearm.jxr_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_connector.jxr_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_connector.jxr_joint_j_1))  &
   relative_to = .template_5_brake.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_lower_torquearm.gralin_lower_torquearm  &
   length = (DM(.template_5_brake.ground.hpr_lta_lc_atch_1, .template_5_brake.ground.hpr_lta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.gel_connector.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_connector.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_connector))  &
   relative_to = .template_5_brake.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_connector.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_connect_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_connect_1, .template_5_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_connector.jxl_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_lta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_lta_connect_atch_1, .template_5_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_connector.jxl_joint_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_uta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_uta_connect_atch_1, .template_5_brake.ground.hpl_uta_connect_atch_2, "Z"))  &
   relative_to = .template_5_brake.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_connector.gralin_connector  &
   length = (DM(.template_5_brake.ground.hpl_connect_1, .template_5_brake.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.ger_connector.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_connector.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_connector))  &
   relative_to = .template_5_brake.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_connector.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_connect_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_connect_1, .template_5_brake.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_connector.jxr_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_lta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_lta_connect_atch_1, .template_5_brake.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_connector.jxr_joint_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_uta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_uta_connect_atch_1, .template_5_brake.ground.hpr_uta_connect_atch_2, "Z"))  &
   relative_to = .template_5_brake.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_connector.gralin_connector  &
   length = (DM(.template_5_brake.ground.hpr_connect_1, .template_5_brake.ground.hpr_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_brake.gel_uc_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_uc_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_uc_collar))  &
   relative_to = .template_5_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_uc_collar.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfl_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.cfl_collar_top, .template_5_brake.ground.cfl_collar_bot, "Z"))  &
   relative_to = .template_5_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_uc_collar.jxl_joint_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpl_lta_connect_atch_1, .template_5_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_uc_collar.jxl_joint_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_cylinder.jxl_joint_j_4))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.gel_upper_cylinder.jxl_joint_j_4))  &
   relative_to = .template_5_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.gel_uc_collar.jxl_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_ldb_collar_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_5_brake.ground.cfl_plane_ref_2, "Z+Z"), .template_5_brake.gel_uc_collar))  &
   relative_to = .template_5_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.gel_uc_collar.gralin_uc_collar  &
   length = (DM(.template_5_brake.ground.cfl_collar_top, .template_5_brake.ground.cfl_collar_bot))
!
marker modify  &
   marker_name = .template_5_brake.ger_uc_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_uc_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_uc_collar))  &
   relative_to = .template_5_brake.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_uc_collar.gralin_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfr_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.cfr_collar_top, .template_5_brake.ground.cfr_collar_bot, "Z"))  &
   relative_to = .template_5_brake.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_uc_collar.jxr_joint_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_lta_connect_atch_1, .template_5_brake.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_brake.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_uc_collar.jxr_joint_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_cylinder.jxr_joint_j_4))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ger_upper_cylinder.jxr_joint_j_4))  &
   relative_to = .template_5_brake.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ger_uc_collar.jxr_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_ldb_collar_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_5_brake.ground.cfr_plane_ref_2, "Z+Z"), .template_5_brake.ger_uc_collar))  &
   relative_to = .template_5_brake.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ger_uc_collar.gralin_uc_collar  &
   length = (DM(.template_5_brake.ground.cfr_collar_top, .template_5_brake.ground.cfr_collar_bot))
!
marker modify  &
   marker_name = .template_5_brake.luntai1.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_5_brake.luntai1.wheel_part.wheel_cm))  &
   relative_to = .template_5_brake.luntai1.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
ude modify instance  &
   instance_name = .template_5_brake.luntai1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpr_wheel_center))
!
marker modify  &
   marker_name = .template_5_brake.luntai2.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_5_brake.luntai2.wheel_part.wheel_cm))  &
   relative_to = .template_5_brake.luntai2.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
ude modify instance  &
   instance_name = .template_5_brake.luntai2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hpl_wheel_center))
!
material modify  &
   material_name = .template_5_brake.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_5_brake.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_5_brake.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .template_5_brake.ges_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_dragbrace))  &
   relative_to = .template_5_brake.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_dragbrace.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_db_sf_atch, .template_5_brake.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .template_5_brake.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_dragbrace.jxs_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_12))  &
   relative_to = .template_5_brake.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ges_dragbrace.gralin_dragbrace_geom  &
   length = (DM(.template_5_brake.ground.hps_db_sf_atch, .template_5_brake.ground.hps_db_uc_atch))
!
marker modify  &
   marker_name = .template_5_brake.ges_dragbrace.MARKER_448  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_db_sf_atch))  &
   relative_to = .template_5_brake.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_uc_top, .template_5_brake.ground.hps_uc_bot, "Z"))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_uc_sf_atch_l, .template_5_brake.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_uc_sf_atch_r, .template_5_brake.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_12  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hps_db_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_brake.ground.origo1))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uc_top))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uc_top))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uc_top))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_uc_bot, .template_5_brake.ground.hps_uc_top, "Z"))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.ues_actuator_j_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.template_5_brake.ground.hps_uc_top, .template_5_brake.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.template_5_brake.ground.hps_uc_sf_atch_l, .template_5_brake.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.template_5_brake.ground.hps_uc_sf_atch_r, .template_5_brake.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_cylinder.MARKER_428  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uc_top))  &
   relative_to = .template_5_brake.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_lower_cylinder))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_lc_top, .template_5_brake.ground.hps_lc_bot, "Z"))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hpr_wheel_center1, .template_5_brake.ground.hpl_wheel_center1, "Z"))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.ues_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_lc_top))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.ues_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_lc_top))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.ues_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_lc_top))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.coomarker_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfs_wheel_centers_midpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfs_wheel_centers_midpoint))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.coomarker_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfs_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfs_nlg_axle_lowpoint))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_wheel_center1))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_wheel_center1))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ges_lower_cylinder.gralin_geom1  &
   length = (DM(.template_5_brake.ground.hps_lc_top, .template_5_brake.ground.hps_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ges_lower_cylinder.gralin_geom2  &
   length = (DM(.template_5_brake.ground.hpr_wheel_center1, .template_5_brake.ground.hpl_wheel_center1))
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_cylinder.MARKER_378  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_lta_lc_atch))  &
   relative_to = .template_5_brake.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_torque_arm))  &
   relative_to = .template_5_brake.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_torque_arm.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_uta_uc_atch, .template_5_brake.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_5_brake.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_torque_arm.jxs_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hps_lta_uta_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_5_brake.ground.origo1))  &
   relative_to = .template_5_brake.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_upper_torque_arm.jxs_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_collar.jxs_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_collar.jxs_joint_j_10))  &
   relative_to = .template_5_brake.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   length = (DM(.template_5_brake.ground.hps_uta_uc_atch, .template_5_brake.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_lower_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_lower_torque_arm))  &
   relative_to = .template_5_brake.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_torque_arm.jxs_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_torque_arm.jxs_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_torque_arm.jxs_joint_j_8))  &
   relative_to = .template_5_brake.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_torque_arm.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_lta_lc_atch, .template_5_brake.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_5_brake.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   length = (DM(.template_5_brake.ground.hps_lta_lc_atch, .template_5_brake.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_5_brake.ges_lower_torque_arm.MARKER_379  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_lta_lc_atch))  &
   relative_to = .template_5_brake.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape ellipsoid  &
   ellipsoid_name = .template_5_brake.mts_body_mount_2.ELLIPSOID_38  &
   x_scale_factor = (2 * 10.0cm)  &
   y_scale_factor = (2 * 10.0cm)  &
   z_scale_factor = (2 * 10.0cm)
!
part modify rigid_body name_and_position  &
   part_name = .template_5_brake.mts_body_mount_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.origo1))
!
marker modify  &
   marker_name = .template_5_brake.mts_body_mount_2.MARKER_427  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uc_top))  &
   relative_to = .template_5_brake.mts_body_mount_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.mts_body_mount_2.MARKER_447  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_db_sf_atch))  &
   relative_to = .template_5_brake.mts_body_mount_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_collar.jxs_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_brake.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_5_brake.ground.origo1))  &
   relative_to = .template_5_brake.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_collar))  &
   relative_to = .template_5_brake.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_collar.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hps_uc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_brake.ground.hps_uc_bot, .template_5_brake.ground.cfs_collar_top, "Z"))  &
   relative_to = .template_5_brake.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_5_brake.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_collar.ues_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_5_brake.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.ges_collar.ues_actuator_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_brake.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_5_brake.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_brake.ges_collar.gralin_collar  &
   length = (DM(.template_5_brake.ground.hps_uc_bot, .template_5_brake.ground.cfs_collar_top))
!
marker modify  &
   marker_name = .template_5_brake.luntai1_2.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_5_brake.luntai1_2.wheel_part.wheel_cm))  &
   relative_to = .template_5_brake.luntai1_2.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
ude modify instance  &
   instance_name = .template_5_brake.luntai1_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_wheel_center1))
!
marker modify  &
   marker_name = .template_5_brake.luntai2_2.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_5_brake.luntai2_2.wheel_part.wheel_cm))  &
   relative_to = .template_5_brake.luntai2_2.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
ude modify instance  &
   instance_name = .template_5_brake.luntai2_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_wheel_center1))
!
geometry modify shape ellipsoid  &
   ellipsoid_name = .template_5_brake.PART_46.ELLIPSOID_156  &
   x_scale_factor = (2 * 10.0cm)  &
   y_scale_factor = (2 * 10.0cm)  &
   z_scale_factor = (2 * 10.0cm)
!
marker modify  &
   marker_name = .template_5_brake.PART_46.MARKER_443  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_uc_top))  &
   relative_to = .template_5_brake.PART_46
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.PART_46.MARKER_445  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_uc_top))  &
   relative_to = .template_5_brake.PART_46
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.PART_46.MARKER_449  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpl_udb_spndl_atch_1))  &
   relative_to = .template_5_brake.PART_46
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
marker modify  &
   marker_name = .template_5_brake.PART_46.MARKER_451  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_brake.ground.hpr_udb_spndl_atch_1))  &
   relative_to = .template_5_brake.PART_46
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_brake.ground
!
material modify  &
   material_name = .template_5_brake.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
geometry modify shape force  &
   force_name = .template_5_brake.SFORCE_20_force_graphic_1  &
   applied_at_marker_name = (.template_5_brake.LMLG_Tb.i)
!
geometry modify shape force  &
   force_name = .template_5_brake.SFORCE_21_force_graphic_1  &
   applied_at_marker_name = (.template_5_brake.RLMG_Tb.i)
!
geometry modify shape force  &
   force_name = .template_5_brake.Driving_force_force_graphic_1  &
   applied_at_marker_name = (.template_5_brake.thrust.i)
!
model display  &
   model_name = template_5_brake

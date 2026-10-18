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
!-------------------------------- Data storage --------------------------------!
!
!
data_element create variable  &
   variable_name = .template_2_brake.MLG_Vw  &
   adams_id = 34  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_2_brake.LMLG_S  &
   adams_id = 30  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_2_brake.LMLG_V  &
   adams_id = 31  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_2_brake.MLG_slip_ratio  &
   adams_id = 35  &
   initial_condition = 0.0  &
   function = ""
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .template_2_brake.steel  &
   adams_id = 3  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_2_brake.aluminum  &
   adams_id = 2  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
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
   default_coordinate_system = .template_2_brake.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.ground.origo  &
   adams_id = 1  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.ground.origo  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.lumian_1_ref_1  &
   adams_id = 186  &
   location = 1.2270973957E+04, 1811.5919597, -282.740481  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.ground.lumian_1_ref_1  &
   visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.cfl_spin_axis  &
   adams_id = 4  &
   location = 1.2270973957E+04, -1811.59195974, 174.2595194  &
   orientation = 3.1415910214, 1.5533424893, 9.3519600853E-05
!
marker attributes  &
   marker_name = .template_2_brake.ground.cfl_spin_axis  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.cfl_uc_top  &
   adams_id = 17  &
   location = 1.2137340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.ground.cfl_uc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.cfl_collar_top  &
   adams_id = 25  &
   location = 1.2216184789E+04, -1494.0334506368, 988.583100554  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
marker attributes  &
   marker_name = .template_2_brake.ground.cfl_collar_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.cfl_collar_bot  &
   adams_id = 27  &
   location = 1.2230884553E+04, -1504.282593664, 771.41271422  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
marker attributes  &
   marker_name = .template_2_brake.ground.cfl_collar_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.cfl_plane_ref  &
   adams_id = 29  &
   location = 1.1790454913E+04, -1331.23818588, 1478.5418121942  &
   orientation = 1.2298492976, 1.5304362235, 4.6906005914
!
marker attributes  &
   marker_name = .template_2_brake.ground.cfl_plane_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.cfl_plane_ref_2  &
   adams_id = 31  &
   location = 1.1790454913E+04, -1331.23818588, 1478.5418121942  &
   orientation = 2.7997663425, 1.5925669695, 4.6720193054
!
marker attributes  &
   marker_name = .template_2_brake.ground.cfl_plane_ref_2  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.cfl_spin_axis_1  &
   adams_id = 37  &
   location = 1.2270973957E+04, -1811.59195974, 174.2595194  &
   orientation = 6.283183675, 1.5882501643, 3.141499134
!
marker attributes  &
   marker_name = .template_2_brake.ground.cfl_spin_axis_1  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.cfl_ldb_geompt_1  &
   adams_id = 39  &
   location = 1.1891208125E+04, -1378.1308466589, 1145.8304613444  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.ground.cfl_ldb_geompt_1  &
   color = MAIZE  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.cfl_ldb_geompt_2  &
   adams_id = 41  &
   location = 1.1960664303E+04, -1405.0660792298, 1073.7874160988  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.ground.cfl_ldb_geompt_2  &
   color = MAIZE  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.ground.MARKER_211  &
   adams_id = 211  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 3.1415926536, 1.5707963268, 3.1415926536
!
marker create  &
   marker_name = .template_2_brake.ground.MARKER_215  &
   adams_id = 215  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 0.0, 0.0, 0.0
!
marker create  &
   marker_name = .template_2_brake.ground.MARKER_226  &
   adams_id = 226  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 0.0, 0.0, 0.0
!
marker create  &
   marker_name = .template_2_brake.ground.MARKER_240  &
   adams_id = 240  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 1.5707963268, 1.5707963268, 4.7123889804
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_2_brake.ground.luntai_tire_jf_1  &
   adams_id = 187
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
!---------------------------------- zhiliang ----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_brake.zhiliang  &
   adams_id = 23  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.zhiliang
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.zhiliang.MARKER_199  &
   adams_id = 199  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.zhiliang.MARKER_199  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.zhiliang.cm  &
   adams_id = 204  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 0.0, 1.5707963268, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.zhiliang.cm  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.zhiliang.MARKER_207  &
   adams_id = 207  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 0.0, 0.0, 0.0
!
marker create  &
   marker_name = .template_2_brake.zhiliang.MARKER_210  &
   adams_id = 210  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 3.1415926536, 1.5707963268, 3.1415926536
!
marker create  &
   marker_name = .template_2_brake.zhiliang.MARKER_212  &
   adams_id = 212  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 0.0, 0.0, 0.0
!
marker create  &
   marker_name = .template_2_brake.zhiliang.MARKER_214  &
   adams_id = 214  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 1.5707963268, 1.5707963268, 4.7123889804
!
marker create  &
   marker_name = .template_2_brake.zhiliang.MARKER_228  &
   adams_id = 228  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 0.0, 0.0, 0.0
!
marker create  &
   marker_name = .template_2_brake.zhiliang.MARKER_229  &
   adams_id = 229  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 1.5707963268, 1.5707963268, 4.7123889804
!
marker create  &
   marker_name = .template_2_brake.zhiliang.MARKER_233  &
   adams_id = 233  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 3.1415926536, 1.5707963268, 3.1415926536
!
marker create  &
   marker_name = .template_2_brake.zhiliang.MARKER_239  &
   adams_id = 239  &
   location = 1.2137340597E+04, -1439.0607744, 2253.4060818  &
   orientation = 1.5707963268, 1.5707963268, 4.7123889804
!
part create rigid_body mass_properties  &
   part_name = .template_2_brake.zhiliang  &
   mass = 1.2E+04  &
   center_of_mass_marker = .template_2_brake.zhiliang.cm  &
   ixx = 4084.5940484395  &
   iyy = 4084.594048436  &
   izz = 4084.5940483223  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_2_brake.zhiliang.ELLIPSOID_49  &
   adams_id = 26  &
   center_marker = .template_2_brake.zhiliang.MARKER_199  &
   x_scale_factor = 100.0  &
   y_scale_factor = 100.0  &
   z_scale_factor = 100.0
!
part attributes  &
   part_name = .template_2_brake.zhiliang  &
   color = RED  &
   name_visibility = off  &
   size_of_icons = 40.0
!
!----------------------------- gel_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_brake.gel_upper_cylinder  &
   adams_id = 4  &
   location = 1.2186012335E+04, -1472.9962565924, 1434.3428627157  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.gel_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.MARKER_216  &
   adams_id = 216  &
   location = 6.3643534887E-10, 8.8382773322E-10, -721.507081063  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.MARKER_218  &
   adams_id = 218  &
   location = 6.3643534887E-10, 8.8382773322E-10, -721.507081063  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.MARKER_220  &
   adams_id = 220  &
   location = 6.3643534887E-10, 8.8382773322E-10, -721.507081063  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.MARKER_222  &
   adams_id = 222  &
   location = 6.4170973204E-10, 8.8445958447E-10, -721.507081063  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.cm  &
   adams_id = 71  &
   location = -0.207563017, 6.4023904007, -14.6682621265  &
   orientation = 3.2408439229E-02, 2.0262533312E-02, 6.7576477157E-08
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.inertia_frame  &
   adams_id = 72  &
   location = -0.207563017, 6.4023904007, -14.6682621265  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.gralin_12  &
   adams_id = 73  &
   location = 6.3823252239E-10, 8.838485499E-10, -721.507081063  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_cylinder.gralin_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.jxl_joint_j_12  &
   adams_id = 76  &
   location = 0.0, 0.0, 507.1310810647  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_cylinder.jxl_joint_j_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.MARKER_234  &
   adams_id = 234  &
   location = -6.7533173809, -4.6926786112, -821.1683647783  &
   orientation = 3.1415926536, 1.6178478494, 6.7584612879E-02
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.uel_spring_j_1  &
   adams_id = 78  &
   location = 6.3823252239E-10, 8.838485499E-10, -721.507081063  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_cylinder.uel_spring_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_cylinder.jxl_joint_j_4  &
   adams_id = 81  &
   location = 0.0, 0.0, 556.2289935088  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_cylinder.jxl_joint_j_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
part create rigid_body mass_properties  &
   part_name = .template_2_brake.gel_upper_cylinder  &
   mass = 112.770857716  &
   center_of_mass_marker = .template_2_brake.gel_upper_cylinder.cm  &
   inertia_marker = .template_2_brake.gel_upper_cylinder.inertia_frame  &
   ixx = 2.0382860753E+07  &
   iyy = 2.0191575617E+07  &
   izz = 6.7703088217E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_brake.gel_upper_cylinder.gralin_upper_cylinder  &
   adams_id = 1  &
   center_marker = .template_2_brake.gel_upper_cylinder.gralin_12  &
   angle_extent = 6.2831853072  &
   length = 1443.0141621266  &
   radius = 93.98  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_upper_cylinder.gralin_upper_cylinder  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_2_brake.gel_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 40.0
!
!----------------------------- gel_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_brake.gel_lower_cylinder  &
   adams_id = 6  &
   location = 1.2238367977E+04, -1509.5002744656, 660.8546165914  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.gel_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.MARKER_203  &
   adams_id = 203  &
   location = 0.3297699984, -278.8194421688, 501.3550984684  &
   orientation = 1.1827384397E-03, 1.5063309604, 3.0739421105
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.MARKER_203  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.MARKER_217  &
   adams_id = 217  &
   location = -2.9251268745E-07, 1.1790534982E-09, -483.3619999809  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.MARKER_219  &
   adams_id = 219  &
   location = -2.9251268745E-07, 1.1790534982E-09, -483.3619999809  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.MARKER_221  &
   adams_id = 221  &
   location = -2.9251268745E-07, 1.1790534982E-09, -483.3619999809  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.MARKER_223  &
   adams_id = 223  &
   location = -2.925109068E-07, 1.1796038176E-09, -483.3619999809  &
   orientation = 5.3196637838, 3.0592631119, 2.1796620084
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.cm  &
   adams_id = 99  &
   location = 1.6535536877E-02, -13.9807327446, 32.7170406567  &
   orientation = 1.1827369552E-03, 7.8095547608E-02, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.inertia_frame  &
   adams_id = 100  &
   location = 1.653553688E-02, -13.9807327446, 32.7170406567  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.gralin_14  &
   adams_id = 101  &
   location = -2.9251091826E-07, 1.1789319521E-09, -483.3619999809  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.gralin_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.gralin_22  &
   adams_id = 102  &
   location = 1.2485845691E-10, -5.0742924723E-06, 483.3620002382  &
   orientation = 1.1827369765E-03, 1.5063451472, 6.2648237542
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.gralin_22  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.jxl_joint_j_11  &
   adams_id = 103  &
   location = 114.1502170489, -26.2463754244, 381.6035459414  &
   orientation = 3.1906577229, 1.5707962113, 1.5707986779
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.jxl_joint_j_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.jxl_joint_i_12  &
   adams_id = 104  &
   location = 0.0, -3.9134147312E-10, -268.9860000012  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.jxl_joint_i_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.coomarker_1  &
   adams_id = 105  &
   location = 0.3297699984, -278.8194421688, 501.3550984684  &
   orientation = 3.142775392, 1.6352616932, 3.2093366878
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.coomarker_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.uel_spring_i_1  &
   adams_id = 106  &
   location = -2.9251091826E-07, 1.1789319521E-09, -483.3619999809  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.uel_spring_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.uel_damper_i_1  &
   adams_id = 107  &
   location = -2.9251091826E-07, 1.1789319521E-09, -483.3619999809  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.uel_damper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_cylinder.uel_stopper_i_1  &
   adams_id = 108  &
   location = -2.9251091826E-07, 1.1789319521E-09, -483.3619999809  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_cylinder.uel_stopper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
part create rigid_body mass_properties  &
   part_name = .template_2_brake.gel_lower_cylinder  &
   mass = 217.3555691677  &
   center_of_mass_marker = .template_2_brake.gel_lower_cylinder.cm  &
   inertia_marker = .template_2_brake.gel_lower_cylinder.inertia_frame  &
   ixx = 3.3284494628E+06  &
   iyy = 3.1936294E+06  &
   izz = 2.0323307411E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_brake.gel_lower_cylinder.gralin_lower_cylinder  &
   adams_id = 7  &
   center_marker = .template_2_brake.gel_lower_cylinder.gralin_14  &
   angle_extent = 6.2831853072  &
   length = 966.7239999802  &
   radius = 63.5  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_lower_cylinder.gralin_lower_cylinder  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_brake.gel_lower_cylinder.gralin_geom  &
   adams_id = 8  &
   center_marker = .template_2_brake.gel_lower_cylinder.gralin_22  &
   angle_extent = 6.2831853072  &
   length = 425.7036049693  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_lower_cylinder.gralin_geom  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_2_brake.gel_lower_cylinder  &
   name_visibility = on  &
   size_of_icons = 40.0
!
!---------------------------- gel_upper_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_brake.gel_upper_dragbrace  &
   adams_id = 8  &
   location = 1.1247700263E+04, -1130.692229848, 1810.57118708  &
   orientation = 1.2073242946, 2.3360498626, 4.4547535314
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.gel_upper_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.gel_upper_dragbrace.MARKER_208  &
   adams_id = 208  &
   location = -946.420910472, -220.3516670374, 372.0032663641  &
   orientation = 4.9700244294, 2.3360498626, 1.934268359
!
marker create  &
   marker_name = .template_2_brake.gel_upper_dragbrace.cm  &
   adams_id = 119  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_dragbrace.inertia_frame  &
   adams_id = 120  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_dragbrace.gralin_24  &
   adams_id = 121  &
   location = -2.2706836411E-10, -2.2812307598E-10, -422.2750593684  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_dragbrace.gralin_24  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_dragbrace.jxl_joint_j_14  &
   adams_id = 122  &
   location = 2.2595814109E-10, 2.2848389847E-10, 422.2750593684  &
   orientation = 3.3685336872, 1.5713226834, 2.335725725
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_dragbrace.jxl_joint_j_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_dragbrace.uel_actuator_i_3  &
   adams_id = 124  &
   location = 2.2595814109E-10, 2.2848389847E-10, 422.2750593684  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_dragbrace.uel_actuator_i_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 40.0
!
part create rigid_body mass_properties  &
   part_name = .template_2_brake.gel_upper_dragbrace  &
   mass = 6.7539180723  &
   center_of_mass_marker = .template_2_brake.gel_upper_dragbrace.cm  &
   inertia_marker = .template_2_brake.gel_upper_dragbrace.inertia_frame  &
   ixx = 4.0301304206E+05  &
   iyy = 4.0301304206E+05  &
   izz = 3137.2976041438  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_brake.gel_upper_dragbrace.gralin_upper_dragbrace  &
   adams_id = 11  &
   center_marker = .template_2_brake.gel_upper_dragbrace.gralin_24  &
   angle_extent = 6.2831853072  &
   length = 844.5501187369  &
   radius = 30.48  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_upper_dragbrace.gralin_upper_dragbrace  &
   color = RED
!
part attributes  &
   part_name = .template_2_brake.gel_upper_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 40.0
!
!---------------------------- gel_lower_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_brake.gel_lower_dragbrace  &
   adams_id = 10  &
   location = 1.1821751947E+04, -1351.195614088, 1217.87350659  &
   orientation = 1.2008496444, 2.3394561925, 4.4490601006
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.gel_lower_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.gel_lower_dragbrace.cm  &
   adams_id = 131  &
   location = 3.9348735476, 6.8056064573, 24.9786134158  &
   orientation = 2.6173709217, 1.9185797667E-02, 3.1415926536
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_dragbrace.inertia_frame  &
   adams_id = 132  &
   location = 3.9348735476, 6.8056064573, 24.9786134158  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_dragbrace.gralin_26  &
   adams_id = 133  &
   location = 1.1418643808E-10, 1.377231662E-10, -431.8055559096  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_dragbrace.gralin_26  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_dragbrace.jxl_joint_i_14  &
   adams_id = 134  &
   location = 1.1352030427E-10, 1.3820888878E-10, -431.8055559096  &
   orientation = 3.3697240756, 1.5758698685, 2.3321676841
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_dragbrace.jxl_joint_i_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_dragbrace.jxl_joint_i_10  &
   adams_id = 135  &
   location = -1.1024514635E-10, -1.3866685578E-10, 431.8055559096  &
   orientation = 3.3697240756, 1.5758698685, 2.3321676841
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_dragbrace.jxl_joint_i_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_1  &
   adams_id = 136  &
   location = 70.772384942, 122.4052041467, 162.0383572441  &
   orientation = 4.1881672485, 1.5707963268, 5.8914619092
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_2  &
   adams_id = 137  &
   location = -2.5562885142E-11, -3.3655370157E-11, 103.6333334183  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_3  &
   adams_id = 138  &
   location = -5.3526627575E-11, -6.6412153554E-11, 207.2666668366  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 40.0
!
part create rigid_body mass_properties  &
   part_name = .template_2_brake.gel_lower_dragbrace  &
   mass = 5.6992574801  &
   center_of_mass_marker = .template_2_brake.gel_lower_dragbrace.cm  &
   inertia_marker = .template_2_brake.gel_lower_dragbrace.inertia_frame  &
   ixx = 3.2110553519E+05  &
   iyy = 3.1937780276E+05  &
   izz = 5107.1748959849  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_brake.gel_lower_dragbrace.gralin_lower_dragbrace  &
   adams_id = 13  &
   center_marker = .template_2_brake.gel_lower_dragbrace.gralin_26  &
   angle_extent = 6.2831853072  &
   length = 863.6111118191  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_lower_dragbrace.gralin_lower_dragbrace  &
   color = PEACH
!
geometry create shape plate  &
   plate_name = .template_2_brake.gel_lower_dragbrace.graarm_uplock_tab  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_1,  &
                 .template_2_brake.gel_lower_dragbrace.graarm_2,  &
                 .template_2_brake.gel_lower_dragbrace.graarm_3  &
   width = 25.4  &
   radius = 12.7
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_lower_dragbrace.graarm_uplock_tab  &
   color = PEACH
!
part attributes  &
   part_name = .template_2_brake.gel_lower_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 40.0
!
!---------------------------- gel_upper_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_brake.gel_upper_torquearm  &
   adams_id = 12  &
   location = 1.2079452409E+04, -1493.9074516, 664.6292016  &
   orientation = 4.6160488325, 2.942742088, 1.4763432468
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.gel_upper_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.gel_upper_torquearm.cm  &
   adams_id = 147  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_torquearm.inertia_frame  &
   adams_id = 148  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_torquearm.gralin_11  &
   adams_id = 149  &
   location = -1.0365666658E-10, -2.3080929529E-11, -138.3335383036  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_torquearm.gralin_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_torquearm.jxl_joint_i_2  &
   adams_id = 150  &
   location = 9.8605151821E-11, 2.2895314117E-11, 138.3335383036  &
   orientation = 4.7721567902, 1.5707958587, 3.0901536529
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_torquearm.jxl_joint_i_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_upper_torquearm.jxl_joint_i_3  &
   adams_id = 151  &
   location = -1.0023926134E-10, -2.1990222143E-11, -138.3335383036  &
   orientation = 3.2013618942, 1.5193611892, 1.3020014208
!
marker attributes  &
   marker_name = .template_2_brake.gel_upper_torquearm.jxl_joint_i_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
part create rigid_body mass_properties  &
   part_name = .template_2_brake.gel_upper_torquearm  &
   mass = 1.5364744752  &
   center_of_mass_marker = .template_2_brake.gel_upper_torquearm.cm  &
   inertia_marker = .template_2_brake.gel_upper_torquearm.inertia_frame  &
   ixx = 1.0048562438E+04  &
   iyy = 1.0048562438E+04  &
   izz = 495.6359362218  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_brake.gel_upper_torquearm.gralin_upper_torquearm  &
   adams_id = 15  &
   center_marker = .template_2_brake.gel_upper_torquearm.gralin_11  &
   angle_extent = 6.2831853072  &
   length = 276.6670766071  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_upper_torquearm.gralin_upper_torquearm  &
   color = GREEN
!
part attributes  &
   part_name = .template_2_brake.gel_upper_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 40.0
!
!---------------------------- gel_lower_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_brake.gel_lower_torquearm  &
   adams_id = 14  &
   location = 1.2099342641E+04, -1557.9375115, 403.0923612  &
   orientation = 4.7962850637, 0.3762472342, 1.492744074
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.gel_lower_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.gel_lower_torquearm.cm  &
   adams_id = 157  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_torquearm.inertia_frame  &
   adams_id = 158  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_torquearm.gralin_29  &
   adams_id = 159  &
   location = -9.4070584655E-11, 0.0, -138.7301712808  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_torquearm.gralin_29  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_torquearm.jxl_joint_i_11  &
   adams_id = 160  &
   location = -9.5902452646E-11, 0.0, -138.7301712808  &
   orientation = 3.1089252352, 1.6612279117, 5.0167167861
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_torquearm.jxl_joint_i_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_lower_torquearm.jxl_joint_i_1  &
   adams_id = 161  &
   location = 9.2766072601E-11, 0.0, 138.7301712808  &
   orientation = 3.1089245675, 1.6612281876, 5.7817305147
!
marker attributes  &
   marker_name = .template_2_brake.gel_lower_torquearm.jxl_joint_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
part create rigid_body mass_properties  &
   part_name = .template_2_brake.gel_lower_torquearm  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_2_brake.gel_lower_torquearm.cm  &
   inertia_marker = .template_2_brake.gel_lower_torquearm.inertia_frame  &
   ixx = 292.6396534292  &
   iyy = 292.6396534292  &
   izz = 292.6396534292  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_brake.gel_lower_torquearm.gralin_lower_torquearm  &
   adams_id = 17  &
   center_marker = .template_2_brake.gel_lower_torquearm.gralin_29  &
   angle_extent = 6.2831853072  &
   length = 277.4603425616  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_lower_torquearm.gralin_lower_torquearm  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_2_brake.gel_lower_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 40.0
!
!------------------------------- gel_connector --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_brake.gel_connector  &
   adams_id = 17  &
   location = 1.2049122257E+04, -1551.2110073, 531.6382052  &
   orientation = 3.0894127897, 1.6143683629, 5.4075285281
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.gel_connector
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.gel_connector.cm  &
   adams_id = 169  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_connector.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_connector.inertia_frame  &
   adams_id = 170  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_connector.inertia_frame  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_connector.gralin_3  &
   adams_id = 171  &
   location = 0.0, 6.2061467077E-11, -60.0708472436  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_connector.gralin_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_connector.jxl_joint_j_1  &
   adams_id = 172  &
   location = -3.2030730841E-05, -3.9921405011E-05, -11.0234586256  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_connector.jxl_joint_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_connector.jxl_joint_j_2  &
   adams_id = 173  &
   location = 0.0, -6.333583831E-11, 60.0708472436  &
   orientation = 5.7869668181, 1.5707941656, 1.5707923349
!
marker attributes  &
   marker_name = .template_2_brake.gel_connector.jxl_joint_j_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
part create rigid_body mass_properties  &
   part_name = .template_2_brake.gel_connector  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_2_brake.gel_connector.cm  &
   inertia_marker = .template_2_brake.gel_connector.inertia_frame  &
   ixx = 292.6396534292  &
   iyy = 292.6396534292  &
   izz = 292.6396534292  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_brake.gel_connector.gralin_connector  &
   adams_id = 19  &
   center_marker = .template_2_brake.gel_connector.gralin_3  &
   angle_extent = 6.2831853072  &
   length = 120.1416944872  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_connector.gralin_connector  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_2_brake.gel_connector  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 40.0
!
!------------------------------- gel_uc_collar --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_brake.gel_uc_collar  &
   adams_id = 19  &
   location = 1.2223534671E+04, -1499.1580221504, 879.997907387  &
   orientation = 0.9619306452, 3.0592631119, 4.1051141769
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.gel_uc_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_brake.gel_uc_collar.cm  &
   adams_id = 179  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_uc_collar.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_uc_collar.inertia_frame  &
   adams_id = 180  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_uc_collar.inertia_frame  &
   visibility = on  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_uc_collar.gralin_5  &
   adams_id = 181  &
   location = 2.6924643071E-11, 2.2060478444E-11, -108.9542389171  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_uc_collar.gralin_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_uc_collar.jxl_joint_j_3  &
   adams_id = 182  &
   location = 122.0018852298, 5.9907462808, 71.4829517951  &
   orientation = 3.1906577229, 1.5707962113, 1.5707986779
!
marker attributes  &
   marker_name = .template_2_brake.gel_uc_collar.jxl_joint_j_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_uc_collar.jxl_joint_i_4  &
   adams_id = 183  &
   location = -3.0778026931E-10, -6.2083140958E-10, -9.1530054394E-10  &
   orientation = 0.0, 0.0, 0.0
!
marker attributes  &
   marker_name = .template_2_brake.gel_uc_collar.jxl_joint_i_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.gel_uc_collar.jxl_joint_j_10  &
   adams_id = 184  &
   location = 109.5796703534, 33.5667968494, -46.8303107227  &
   orientation = 3.4809632466, 1.5707963268, 1.609831873
!
marker attributes  &
   marker_name = .template_2_brake.gel_uc_collar.jxl_joint_j_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 40.0
!
part create rigid_body mass_properties  &
   part_name = .template_2_brake.gel_uc_collar  &
   mass = 30.2539444008  &
   center_of_mass_marker = .template_2_brake.gel_uc_collar.cm  &
   inertia_marker = .template_2_brake.gel_uc_collar.inertia_frame  &
   ixx = 2.417065893E+05  &
   iyy = 2.417065893E+05  &
   izz = 2.4398293462E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_brake.gel_uc_collar.gralin_uc_collar  &
   adams_id = 21  &
   center_marker = .template_2_brake.gel_uc_collar.gralin_5  &
   angle_extent = 6.2831853072  &
   length = 217.9084778341  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_brake.gel_uc_collar.gralin_uc_collar  &
   color = YELLOW
!
part attributes  &
   part_name = .template_2_brake.gel_uc_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 40.0
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_2_brake.jolrev_lta_lc_joint  &
   adams_id = 2  &
   i_marker_name = .template_2_brake.gel_lower_torquearm.jxl_joint_i_11  &
   j_marker_name = .template_2_brake.gel_lower_cylinder.jxl_joint_j_11
!
constraint attributes  &
   constraint_name = .template_2_brake.jolrev_lta_lc_joint  &
   size_of_icons = 40.0
!
constraint create joint cylindrical  &
   joint_name = .template_2_brake.jolcyl_lc_uc_joint  &
   adams_id = 4  &
   i_marker_name = .template_2_brake.gel_lower_cylinder.jxl_joint_i_12  &
   j_marker_name = .template_2_brake.gel_upper_cylinder.jxl_joint_j_12
!
constraint attributes  &
   constraint_name = .template_2_brake.jolcyl_lc_uc_joint  &
   size_of_icons = 40.0
!
constraint create joint fixed  &
   joint_name = .template_2_brake.jolrev_ldb_udb_joint  &
   adams_id = 6  &
   i_marker_name = .template_2_brake.gel_lower_dragbrace.jxl_joint_i_14  &
   j_marker_name = .template_2_brake.gel_upper_dragbrace.jxl_joint_j_14
!
constraint attributes  &
   constraint_name = .template_2_brake.jolrev_ldb_udb_joint  &
   size_of_icons = 40.0
!
constraint create joint fixed  &
   joint_name = .template_2_brake.JOINT_58  &
   adams_id = 35  &
   i_marker_name = .template_2_brake.zhiliang.MARKER_207  &
   j_marker_name = .template_2_brake.gel_upper_dragbrace.MARKER_208
!
constraint attributes  &
   constraint_name = .template_2_brake.JOINT_58  &
   name_visibility = off
!
constraint create joint planar  &
   joint_name = .template_2_brake.JOINT_56  &
   adams_id = 36  &
   i_marker_name = .template_2_brake.zhiliang.MARKER_210  &
   j_marker_name = .template_2_brake.ground.MARKER_211
!
constraint attributes  &
   constraint_name = .template_2_brake.JOINT_56  &
   name_visibility = off
!
constraint create joint fixed  &
   joint_name = .template_2_brake.JOINT_37  &
   adams_id = 37  &
   i_marker_name = .template_2_brake.zhiliang.MARKER_233  &
   j_marker_name = .template_2_brake.gel_upper_cylinder.MARKER_234
!
constraint attributes  &
   constraint_name = .template_2_brake.JOINT_37  &
   name_visibility = off
!
constraint create joint cylindrical  &
   joint_name = .template_2_brake.jolcyl_lta_connect  &
   adams_id = 12  &
   i_marker_name = .template_2_brake.gel_lower_torquearm.jxl_joint_i_1  &
   j_marker_name = .template_2_brake.gel_connector.jxl_joint_j_1
!
constraint attributes  &
   constraint_name = .template_2_brake.jolcyl_lta_connect  &
   size_of_icons = 40.0
!
constraint create joint revolute  &
   joint_name = .template_2_brake.jolrev_uta_connect  &
   adams_id = 14  &
   i_marker_name = .template_2_brake.gel_upper_torquearm.jxl_joint_i_2  &
   j_marker_name = .template_2_brake.gel_connector.jxl_joint_j_2
!
constraint attributes  &
   constraint_name = .template_2_brake.jolrev_uta_connect  &
   size_of_icons = 40.0
!
constraint create joint revolute  &
   joint_name = .template_2_brake.jolrev_uta_collar  &
   adams_id = 16  &
   i_marker_name = .template_2_brake.gel_upper_torquearm.jxl_joint_i_3  &
   j_marker_name = .template_2_brake.gel_uc_collar.jxl_joint_j_3
!
constraint attributes  &
   constraint_name = .template_2_brake.jolrev_uta_collar  &
   size_of_icons = 40.0
!
constraint create joint fixed  &
   joint_name = .template_2_brake.jolrev_collar_uc  &
   adams_id = 18  &
   i_marker_name = .template_2_brake.gel_uc_collar.jxl_joint_i_4  &
   j_marker_name = .template_2_brake.gel_upper_cylinder.jxl_joint_j_4
!
constraint attributes  &
   constraint_name = .template_2_brake.jolrev_collar_uc  &
   size_of_icons = 40.0
!
constraint create joint revolute  &
   joint_name = .template_2_brake.jolrev_ldb_collar  &
   adams_id = 30  &
   i_marker_name = .template_2_brake.gel_lower_dragbrace.jxl_joint_i_10  &
   j_marker_name = .template_2_brake.gel_uc_collar.jxl_joint_j_10
!
constraint attributes  &
   constraint_name = .template_2_brake.jolrev_ldb_collar  &
   size_of_icons = 40.0
!
!------------------------------ Joint Primitives ------------------------------!
!
!
constraint create primitive_joint perpendicular  &
   jprim_name = .template_2_brake.JPRIM_3  &
   adams_id = 1  &
   i_marker_name = .template_2_brake.zhiliang.MARKER_214  &
   j_marker_name = .template_2_brake.ground.MARKER_215
!
constraint attributes  &
   constraint_name = .template_2_brake.JPRIM_3  &
   name_visibility = off
!
!----------------------------------- Forces -----------------------------------!
!
!
force create direct single_component_force  &
   single_component_force_name = .template_2_brake.LMLG_AIR  &
   adams_id = 1  &
   type_of_freedom = translational  &
   i_marker_name = .template_2_brake.gel_upper_cylinder.MARKER_218  &
   j_marker_name = .template_2_brake.gel_lower_cylinder.MARKER_219  &
   action_only = off  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_2_brake.LMLG_OIL  &
   adams_id = 2  &
   type_of_freedom = translational  &
   i_marker_name = .template_2_brake.gel_upper_cylinder.MARKER_220  &
   j_marker_name = .template_2_brake.gel_lower_cylinder.MARKER_221  &
   action_only = off  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_2_brake.LMLG_STOP  &
   adams_id = 3  &
   type_of_freedom = translational  &
   i_marker_name = .template_2_brake.gel_upper_cylinder.MARKER_222  &
   j_marker_name = .template_2_brake.gel_lower_cylinder.MARKER_223  &
   action_only = off  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_2_brake.thrust  &
   adams_id = 7  &
   type_of_freedom = translational  &
   i_marker_name = .template_2_brake.zhiliang.MARKER_239  &
   j_marker_name = .template_2_brake.ground.MARKER_240  &
   action_only = on  &
   function = ""
!
!---------------------------- Adams View Variables ----------------------------!
!
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
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .template_2_brake.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=30.0 step_size=1.0E-02 model_name=.GCMB"
!
!-------------------------- Adams View UDE Instances --------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
undo begin_block suppress = yes
!
ude create instance  &
   instance_name = .template_2_brake.lumian_1  &
   definition_name = .MDI.Forces.vpg_road  &
   location = 1.2270973957E+04, 1811.5919597, -282.740481  &
   orientation = 0.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_2_brake.lumian_1  &
   color = DimGray  &
   visibility = on
!
ude create instance  &
   instance_name = .template_2_brake.luntai  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 1.2270973957E+04, -1811.5919597, 174.2595194  &
   orientation = 0.0, 1.5707963268, 0.0
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_2_brake.lumian_1.ref_marker  &
   object_value = .template_2_brake.ground.lumian_1_ref_1
!
variable modify  &
   variable_name = .template_2_brake.lumian_1.road_property_file  &
   string_value = "C:/Users/Administrator/Desktop/GCMB2/GCMB2_Brake/2d_flat.rdf"
!
variable modify  &
   variable_name = .template_2_brake.lumian_1.road_graphics  &
   string_value = "on"
!
ude modify instance  &
   instance_name = .template_2_brake.lumian_1
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_2_brake.luntai.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.ic_vmode  &
   string_value = "standard"
!
variable modify  &
   variable_name = .template_2_brake.luntai.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_2_brake.luntai.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_2_brake.luntai.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_brake.luntai.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_brake.luntai.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_brake.luntai.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_brake.luntai.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_brake.luntai.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_brake.luntai.ic_wz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_brake.luntai.ic_vm  &
   string_value = "ground"
!
variable modify  &
   variable_name = .template_2_brake.luntai.ic_wm  &
   string_value = "cm"
!
variable modify  &
   variable_name = .template_2_brake.luntai.vmmrk  &
   object_value = (.template_2_brake.luntai.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_2_brake.luntai.wmmrk  &
   object_value = (.template_2_brake.luntai.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_2_brake.luntai.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_2_brake.luntai.road_property_file  &
   string_value = (.template_2_brake.lumian_1.road_property_file)
!
variable modify  &
   variable_name = .template_2_brake.luntai.j_fmarker  &
   object_value = .template_2_brake.ground.luntai_tire_jf_1
!
variable modify  &
   variable_name = .template_2_brake.luntai.ref_marker  &
   object_value = (.template_2_brake.lumian_1.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_2_brake.luntai.wheel_tire_mass  &
   real_value = (.template_2_brake.MLG_m)
!
variable modify  &
   variable_name = .template_2_brake.luntai.Ixx_Iyy  &
   real_value = (.template_2_brake.MLG_Ixx_Iyy)
!
variable modify  &
   variable_name = .template_2_brake.luntai.Izz  &
   real_value = (.template_2_brake.MLG_lzz)
!
variable modify  &
   variable_name = .template_2_brake.luntai.property_file  &
   string_value = "C:/Users/Administrator/Desktop/GCMB2/GCMB2_Brake/MLG.tir"
!
variable modify  &
   variable_name = .template_2_brake.luntai.road_name  &
   string_value = (.template_2_brake.lumian_1)
!
ude modify instance  &
   instance_name = .template_2_brake.luntai
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker create  &
   marker_name = .template_2_brake.luntai.wheel_part.MARKER_202  &
   adams_id = 202  &
   location = -1.4000178794E-07, 0.0, 3.9999781265E-08  &
   orientation = 6.283183675, 1.5882501643, 6.2831852787
!
marker attributes  &
   marker_name = .template_2_brake.luntai.wheel_part.MARKER_202  &
   size_of_icons = 40.0
!
marker create  &
   marker_name = .template_2_brake.luntai.wheel_part.MARKER_224  &
   adams_id = 224  &
   location = -1.4000178794E-07, 0.0, 3.9999781265E-08  &
   orientation = 0.0, 1.5707963268, 0.0
!
marker create  &
   marker_name = .template_2_brake.luntai.wheel_part.MARKER_225  &
   adams_id = 225  &
   location = -1.4000178794E-07, 0.0, 3.9999781265E-08  &
   orientation = 0.0, 1.5707963268, 0.0
!
undo end_block
!
!--------------------------- UDE Dependent Objects ----------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_2_brake.JOINT_33  &
   adams_id = 33  &
   i_marker_name = .template_2_brake.luntai.wheel_part.MARKER_202  &
   j_marker_name = .template_2_brake.gel_lower_cylinder.MARKER_203
!
constraint attributes  &
   constraint_name = .template_2_brake.JOINT_33  &
   name_visibility = off  &
   size_of_icons = 40.0
!
force create direct single_component_force  &
   single_component_force_name = .template_2_brake.LMLG_Tb  &
   adams_id = 4  &
   type_of_freedom = rotational  &
   i_marker_name = .template_2_brake.luntai.wheel_part.MARKER_224  &
   j_marker_name = .template_2_brake.luntai.wheel_part.MARKER_225  &
   action_only = on  &
   function = ""
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry create shape force  &
   force_name = .template_2_brake.SFORCE_1_force_graphic_1  &
   adams_id = 35  &
   force_element_name = .template_2_brake.LMLG_AIR  &
   applied_at_marker_name = .template_2_brake.gel_upper_cylinder.MARKER_218
!
geometry attributes  &
   geometry_name = .template_2_brake.SFORCE_1_force_graphic_1  &
   active = off
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   z_component_gravity = -9809.9999999989
!
force attributes  &
   force_name = .template_2_brake.gravity  &
   size_of_icons = 40.0
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------------- Measures ----------------------------------!
!
!
measure create object  &
   measure_name = .template_2_brake.MLG_w  &
   from_first = yes  &
   object = .template_2_brake.JOINT_33  &
   characteristic = angular_velocity  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_2_brake.MLG_w  &
   color = WHITE
!
measure create point  &
   measure_name = .template_2_brake.js_sd  &
   point = .template_2_brake.zhiliang.cm  &
   characteristic = translational_velocity  &
   component = x_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_2_brake.js_sd  &
   color = WHITE
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
!---------------------------- Function definitions ----------------------------!
!
!
data_element modify variable  &
   variable_name = .template_2_brake.MLG_Vw  &
   function = "-.template_2_brake.MLG_w*0.457"
!
data_element modify variable  &
   variable_name = .template_2_brake.LMLG_S  &
   function = ".template_2_brake.MLG_S0-DM(.template_2_brake.gel_upper_cylinder.MARKER_216,.template_2_brake.gel_lower_cylinder.MARKER_217)"
!
data_element modify variable  &
   variable_name = .template_2_brake.LMLG_V  &
   function = "-1*VR(.template_2_brake.gel_upper_cylinder.MARKER_216,.template_2_brake.gel_lower_cylinder.MARKER_217)"
!
data_element modify variable  &
   variable_name = .template_2_brake.MLG_slip_ratio  &
   function = "1-(VARVAL(.template_2_brake.MLG_Vw))/((.template_2_brake.js_sd)/1000)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_2_brake.LMLG_AIR  &
   function = "3*.template_2_brake.MLG_A_LOW*(.template_2_brake.MLG_P_LOW*(.template_2_brake.MLG_V_LOW/(.template_2_brake.MLG_V_LOW-.template_2_brake.MLG_A_LOW*VARVAL(.template_2_brake.LMLG_S)))**1.1-.template_2_brake.Patm)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_2_brake.LMLG_OIL  &
   function = "IF(VARVAL(.template_2_brake.LMLG_V):0.003*-1*(VARVAL(.template_2_brake.LMLG_V)*0.5*(VARVAL(.template_2_brake.LMLG_V)-ABS(VARVAL(.template_2_brake.LMLG_V)))*((.template_2_brake.MLG_rho_Oil*.template_2_brake.MLG_A_MAIN_OIL**3/(2*.template_2_brake.MLG_RET_Cd**2*.template_2_brake.MLG_A_MAIN_NEG**2))+(.template_2_brake.MLG_rho_Oil*.template_2_brake.MLG_A_RET_OIL**3/(2*.template_2_brake.MLG_MAIN_Cd**2*.template_2_brake.MLG_A_RET_NEG**2)))),0,0.003*VARVAL(.template_2_brake.LMLG_V)*0.5*(VARVAL(.template_2_brake.LMLG_V)+ABS(VARVAL(.template_2_brake.LMLG_V)))*((.template_2_brake.MLG_rho_Oil*.template_2_brake.MLG_A_MAIN_OIL**3/(2*.template_2_brake.MLG_RET_Cd**2*.template_2_brake.MLG_A_MAIN_POS**2))+(.template_2_brake.MLG_rho_Oil*.template_2_brake.MLG_A_RET_OIL**3/(2*.template_2_brake.MLG_MAIN_Cd**2*.template_2_brake.MLG_A_RET_POS**2))))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_2_brake.LMLG_STOP  &
   function = "IF(.template_2_brake.MLG_S0-DM(.template_2_brake.gel_upper_cylinder.MARKER_216,.template_2_brake.gel_lower_cylinder.MARKER_217) :1.0E+09*(.template_2_brake.MLG_S0-DM(.template_2_brake.gel_upper_cylinder.MARKER_216,.template_2_brake.gel_lower_cylinder.MARKER_217)) , 0 , 0 )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_2_brake.LMLG_Tb  &
   function = "if(vx(.template_2_brake.zhiliang.cm,.template_2_brake.ground.MARKER_226):if(time-6:0,0,.template_2_brake.MLG_Tb),0,0)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_2_brake.thrust  &
   function = "-30000*2/3.14*atan(.template_2_brake.MLG_Vx-.template_2_brake.js_sd)*(STEP (TIME,0,0,1.2,1)-STEP (TIME,4.8,0,5.0,1))"
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_2_brake.lumian_1
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_2_brake.luntai
!
!------------------------- Part IC Reference Markers --------------------------!
!
!
part modify rigid_body initial_velocity  &
   part_name = .template_2_brake.luntai.wheel_part  &
   vm = .template_2_brake.luntai.wheel_part.wheel_cm  &
   wm = .template_2_brake.luntai.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_2_brake.luntai.belt_part  &
   vm = .template_2_brake.luntai.wheel_part.wheel_cm  &
   wm = .template_2_brake.luntai.wheel_part.wheel_cm
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_2_brake.ground.cfl_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.cfl_spin_axis_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({180.0, 180.0, 180.0}degrees, .template_2_brake.ground.cfl_spin_axis_1))
!
marker modify  &
   marker_name = .template_2_brake.ground.cfl_uc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.hpl_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_2_brake.ground.origo))
!
marker modify  &
   marker_name = .template_2_brake.ground.cfl_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_2_brake.ground.hpl_uc_top, .template_2_brake.ground.hpl_lc_bot, 0.59 * DM(.template_2_brake.ground.hpl_uc_top, .template_2_brake.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_uc_top, .template_2_brake.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_2_brake.ground.cfl_collar_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_2_brake.ground.hpl_uc_top, .template_2_brake.ground.hpl_lc_bot, 0.7 * DM(.template_2_brake.ground.hpl_uc_top, .template_2_brake.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_uc_top, .template_2_brake.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_2_brake.ground.cfl_plane_ref_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.cfl_plane_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, -90.0, 0.0}degrees, .template_2_brake.ground.cfl_plane_ref))
!
marker modify  &
   marker_name = .template_2_brake.ground.cfl_spin_axis_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.hpl_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_wheel_center, .template_2_brake.ground.hpl_ob_axle, "Z"))
!
marker modify  &
   marker_name = .template_2_brake.ground.cfl_ldb_geompt_1  &
   location =   &
      (LOC_ALONG_LINE(.template_2_brake.ground.hpl_ldb_udb_atch_1, .template_2_brake.ground.hpl_ldb_collar_atch_1, 0.62 * DM(.template_2_brake.ground.hpl_ldb_udb_atch_1, .template_2_brake.ground.hpl_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_2_brake.ground.origo))
!
marker modify  &
   marker_name = .template_2_brake.ground.cfl_ldb_geompt_2  &
   location =   &
      (LOC_ALONG_LINE(.template_2_brake.ground.hpl_ldb_udb_atch_1, .template_2_brake.ground.hpl_ldb_collar_atch_1, 0.74 * DM(.template_2_brake.ground.hpl_ldb_udb_atch_1, .template_2_brake.ground.hpl_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_2_brake.ground.origo))
!
marker modify  &
   marker_name = .template_2_brake.ground.lumian_1_ref_1  &
   location =   &
      (.template_2_brake.lumian_1.location)  &
   orientation =   &
      (.template_2_brake.lumian_1.orientation)
!
marker modify  &
   marker_name = .template_2_brake.ground.MARKER_240  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.POINT_48))
!
material modify  &
   material_name = .template_2_brake.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_cylinder))  &
   relative_to = .template_2_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_cylinder.gralin_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.cfl_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.cfl_uc_top, .template_2_brake.ground.hpl_uc_bot, "Z"))  &
   relative_to = .template_2_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_cylinder.uel_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.cfl_uc_top))  &
   relative_to = .template_2_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_brake.gel_upper_cylinder.gralin_upper_cylinder  &
   length = (DM(.template_2_brake.ground.hpl_uc_top, .template_2_brake.ground.hpl_uc_bot))
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_cylinder.MARKER_216  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_uc_top))  &
   relative_to = .template_2_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_cylinder.MARKER_218  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_uc_top))  &
   relative_to = .template_2_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_cylinder.MARKER_220  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_uc_top))  &
   relative_to = .template_2_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_cylinder.MARKER_234  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.POINT_48))  &
   relative_to = .template_2_brake.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_lower_cylinder))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.gralin_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_lc_top, .template_2_brake.ground.hpl_lc_bot, "Z"))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.gralin_22  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_ib_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_ib_axle, .template_2_brake.ground.hpl_ob_axle, "Z"))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.jxl_joint_j_11  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_lta_connect_atch_1, .template_2_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.jxl_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_cylinder.jxl_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_cylinder.jxl_joint_j_12))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.coomarker_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.cfl_spin_axis))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.cfl_spin_axis))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.uel_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_lc_top))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.uel_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_lc_top))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.uel_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_lc_top))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_brake.gel_lower_cylinder.gralin_lower_cylinder  &
   length = (DM(.template_2_brake.ground.hpl_lc_top, .template_2_brake.ground.hpl_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_brake.gel_lower_cylinder.gralin_geom  &
   length = (DM(.template_2_brake.ground.hpl_ib_axle, .template_2_brake.ground.hpl_ob_axle))
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_cylinder.MARKER_203  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_wheel_center))  &
   relative_to = .template_2_brake.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_dragbrace))  &
   relative_to = .template_2_brake.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_dragbrace.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_udb_spndl_atch_1, .template_2_brake.ground.hpl_ldb_udb_atch_1, "Z"))  &
   relative_to = .template_2_brake.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_dragbrace.jxl_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_2_brake.ground.cfl_plane_ref_2, "Z+Z"), .template_2_brake.gel_upper_dragbrace))  &
   relative_to = .template_2_brake.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_dragbrace.uel_actuator_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_ldb_udb_atch_1))  &
   relative_to = .template_2_brake.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_brake.gel_upper_dragbrace.gralin_upper_dragbrace  &
   length = (DM(.template_2_brake.ground.hpl_udb_spndl_atch_1, .template_2_brake.ground.hpl_ldb_udb_atch_1))
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_lower_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_lower_dragbrace))  &
   relative_to = .template_2_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_dragbrace.gralin_26  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_ldb_udb_atch_1, .template_2_brake.ground.hpl_ldb_collar_atch_1, "Z"))  &
   relative_to = .template_2_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_dragbrace.jxl_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_dragbrace.jxl_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_dragbrace.jxl_joint_j_14))  &
   relative_to = .template_2_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_dragbrace.jxl_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_uc_collar.jxl_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_uc_collar.jxl_joint_j_10))  &
   relative_to = .template_2_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_uplock_tab))  &
   orientation =   &
      (ORI_IN_PLANE(.template_2_brake.ground.hpl_uplock_tab, .template_2_brake.ground.cfl_ldb_geompt_1, .template_2_brake.ground.cfl_ldb_geompt_2, "X_XY"))  &
   relative_to = .template_2_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.cfl_ldb_geompt_1))  &
   relative_to = .template_2_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_dragbrace.graarm_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.cfl_ldb_geompt_2))  &
   relative_to = .template_2_brake.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_brake.gel_lower_dragbrace.gralin_lower_dragbrace  &
   length = (DM(.template_2_brake.ground.hpl_ldb_udb_atch_1, .template_2_brake.ground.hpl_ldb_collar_atch_1))
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_torquearm))  &
   relative_to = .template_2_brake.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_torquearm.gralin_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_uta_collar_atch_1, .template_2_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_2_brake.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_torquearm.jxl_joint_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_connector.jxl_joint_j_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_connector.jxl_joint_j_2))  &
   relative_to = .template_2_brake.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_upper_torquearm.jxl_joint_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_uc_collar.jxl_joint_j_3))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_uc_collar.jxl_joint_j_3))  &
   relative_to = .template_2_brake.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_brake.gel_upper_torquearm.gralin_upper_torquearm  &
   length = (DM(.template_2_brake.ground.hpl_uta_collar_atch_1, .template_2_brake.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_lower_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_lower_torquearm))  &
   relative_to = .template_2_brake.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_torquearm.gralin_29  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_lta_lc_atch_1, .template_2_brake.ground.hpl_lta_connect_atch_1, "Z"))  &
   relative_to = .template_2_brake.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_torquearm.jxl_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_lower_cylinder.jxl_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_lower_cylinder.jxl_joint_j_11))  &
   relative_to = .template_2_brake.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_lower_torquearm.jxl_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_connector.jxl_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_connector.jxl_joint_j_1))  &
   relative_to = .template_2_brake.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_brake.gel_lower_torquearm.gralin_lower_torquearm  &
   length = (DM(.template_2_brake.ground.hpl_lta_lc_atch_1, .template_2_brake.ground.hpl_lta_connect_atch_1))
!
marker modify  &
   marker_name = .template_2_brake.gel_connector.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_connector.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_connector))  &
   relative_to = .template_2_brake.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_connector.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_connect_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_connect_1, .template_2_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_2_brake.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_connector.jxl_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.hpl_lta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_lta_connect_atch_1, .template_2_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_2_brake.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_connector.jxl_joint_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.hpl_uta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_uta_connect_atch_1, .template_2_brake.ground.hpl_uta_connect_atch_2, "Z"))  &
   relative_to = .template_2_brake.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_brake.gel_connector.gralin_connector  &
   length = (DM(.template_2_brake.ground.hpl_connect_1, .template_2_brake.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_2_brake.gel_uc_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_uc_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_uc_collar))  &
   relative_to = .template_2_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_uc_collar.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.cfl_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.cfl_collar_top, .template_2_brake.ground.cfl_collar_bot, "Z"))  &
   relative_to = .template_2_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_uc_collar.jxl_joint_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_brake.ground.hpl_lta_connect_atch_1, .template_2_brake.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_2_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_uc_collar.jxl_joint_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_cylinder.jxl_joint_j_4))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_brake.gel_upper_cylinder.jxl_joint_j_4))  &
   relative_to = .template_2_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.gel_uc_collar.jxl_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_brake.ground.hpl_ldb_collar_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_2_brake.ground.cfl_plane_ref_2, "Z+Z"), .template_2_brake.gel_uc_collar))  &
   relative_to = .template_2_brake.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_brake.gel_uc_collar.gralin_uc_collar  &
   length = (DM(.template_2_brake.ground.cfl_collar_top, .template_2_brake.ground.cfl_collar_bot))
!
marker modify  &
   marker_name = .template_2_brake.luntai.wheel_part.MARKER_202  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_wheel_center))  &
   relative_to = .template_2_brake.luntai.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.luntai.wheel_part.MARKER_209  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_wheel_center))  &
   relative_to = .template_2_brake.luntai.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.luntai.wheel_part.MARKER_224  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_wheel_center))  &
   relative_to = .template_2_brake.luntai.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.luntai.wheel_part.MARKER_225  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.hpl_wheel_center))  &
   relative_to = .template_2_brake.luntai.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.luntai.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_2_brake.luntai.wheel_part.wheel_cm))  &
   relative_to = .template_2_brake.luntai.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.zhiliang.MARKER_199  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.POINT_48))  &
   relative_to = .template_2_brake.zhiliang
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
geometry modify shape ellipsoid  &
   ellipsoid_name = .template_2_brake.zhiliang.ELLIPSOID_49  &
   x_scale_factor = (100mm)  &
   y_scale_factor = (100mm)  &
   z_scale_factor = (100mm)
!
marker modify  &
   marker_name = .template_2_brake.zhiliang.MARKER_229  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.POINT_48))  &
   relative_to = .template_2_brake.zhiliang
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.zhiliang.MARKER_233  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.POINT_48))  &
   relative_to = .template_2_brake.zhiliang
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
marker modify  &
   marker_name = .template_2_brake.zhiliang.MARKER_239  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_brake.ground.POINT_48))  &
   relative_to = .template_2_brake.zhiliang
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_brake.ground
!
material modify  &
   material_name = .template_2_brake.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
geometry modify shape force  &
   force_name = .template_2_brake.SFORCE_1_force_graphic_1  &
   applied_at_marker_name = (.template_2_brake.LMLG_AIR.i)
!
model display  &
   model_name = template_2_brake

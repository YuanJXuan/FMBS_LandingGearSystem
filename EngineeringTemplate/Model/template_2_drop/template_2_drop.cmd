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
!-------------------------------- Data storage --------------------------------!
!
!
data_element create variable  &
   variable_name = .template_2_drop.NLG_V  &
   adams_id = 115  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_2_drop.NLG_S  &
   adams_id = 120  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_2_drop.x1  &
   adams_id = 121  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_2_drop.x2  &
   adams_id = 122  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_2_drop.VARIABLE_123  &
   adams_id = 123  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_2_drop.VARIABLE_124  &
   adams_id = 124  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_2_drop._cv_solver_variable  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   function = ""
!
data_element attributes  &
   data_element_name = .template_2_drop._cv_solver_variable  &
   visibility = off
!
data_element create array ic_array  &
   array_name = .template_2_drop._cv_array  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   size = 1  &
   numbers = 0.0
!
data_element attributes  &
   data_element_name = .template_2_drop._cv_array  &
   visibility = off
!
data_element create spline  &
   spline_name = .template_2_drop.SPLINE_airspring  &
   adams_id = 4  &
   x = -127.0, -101.6, -76.2, -50.8, -25.4, 0.0, 25.4, 50.8, 76.2, 101.6,  &
       127.0, 152.4, 177.8, 203.2, 228.6, 254.0, 279.4, 304.8, 330.2, 355.6,  &
       381.0, 406.4, 431.8, 457.2, 482.6  &
   y = 7.1171545844E+04, 7.1171545844E+04, 7.1171545844E+04,  &
       7.1171545844E+04, 7.1171545844E+04, 7.1171545844E+04,  &
       7.2061190167E+04, 7.4730123136E+04, 7.9178344752E+04,  &
       8.5405855013E+04, 9.341265392E+04, 1.0319874147E+05, 1.1476411767E+05,  &
       1.2810878252E+05, 1.4323273601E+05, 1.6013597815E+05,  &
       1.7881850893E+05, 1.9928032836E+05, 2.2152143644E+05,  &
       2.4554183316E+05, 2.7134151853E+05, 2.9892049255E+05,  &
       3.2827875521E+05, 3.5941630651E+05, 4.0033994537E+05  &
   linear_extrapolate = no  &
   x_units = "length"  &
   y_units = "force"
!
data_element create spline  &
   spline_name = .template_2_drop.SPLINE_stopper  &
   adams_id = 3  &
   x = 0.0, 2.54E-03, 5.08E-03, 7.62E-03, 1.016E-02, 1.27E-02, 1.524E-02,  &
       1.778E-02, 2.032E-02, 2.286E-02, 2.54E-02, 2.794E-02, 3.048E-02,  &
       3.302E-02, 3.556E-02, 3.81E-02, 4.064E-02, 4.318E-02, 4.572E-02,  &
       4.826E-02, 5.08E-02, 5.334E-02, 5.588E-02, 5.842E-02, 6.096E-02,  &
       6.35E-02, 6.604E-02, 6.858E-02, 7.112E-02, 7.366E-02, 7.62E-02,  &
       7.874E-02, 8.128E-02, 8.382E-02, 8.636E-02, 8.89E-02, 9.144E-02,  &
       9.398E-02, 9.652E-02, 9.906E-02, 0.1016, 0.10414, 0.10668, 0.10922,  &
       0.11176, 0.1143, 0.11684, 0.11938, 0.12192, 0.12446, 0.127, 0.12954,  &
       0.13208, 0.13462, 0.13716, 0.1397, 0.14224, 0.14478, 0.14732, 0.14986,  &
       0.1524, 0.15494, 0.15748, 0.16002, 0.16256, 0.1651, 0.16764, 0.17018,  &
       0.17272, 0.17526, 0.1778, 0.18034, 0.18288, 0.18542, 0.18796, 0.1905,  &
       0.19304, 0.19558, 0.19812, 0.20066, 0.2032, 0.20574, 0.20828, 0.21082,  &
       0.21336, 0.2159, 0.21844, 0.22098, 0.22352, 0.22606, 0.2286, 0.23114,  &
       0.23368, 0.23622, 0.23876, 0.2413, 0.24384, 0.24638, 0.24892, 0.25146,  &
       0.254, 0.508, 0.762, 1.016, 1.27, 1.524, 1.778, 2.032, 2.286, 2.54,  &
       5.08, 7.62, 10.16, 12.7, 15.24, 17.78, 20.32, 22.86, 25.4, 50.8, 76.2,  &
       101.6, 127.0, 152.4, 177.8, 203.2, 228.6, 254.0  &
   y = 0.0, 44.4822161526, 105.7971256484, 175.6256644225, 251.6294023717,  &
       332.5821427257, 417.7106066388, 506.4762924022, 598.4788600706,  &
       693.4092472062, 791.0179085764, 891.1015604533, 993.4889463047,  &
       1098.0337196395, 1204.609995786, 1313.1083484925, 1423.4309168834,  &
       1535.4922951036, 1649.2141944529, 1764.527222674, 1881.368659842,  &
       1999.6802342539, 2119.4090120724, 2240.5065076819, 2362.9277940442,  &
       2486.6315026981, 2611.5784892935, 2737.7331680574, 2865.0612876834,  &
       2993.5321554424, 3123.1150786052, 3253.7824781978, 3385.5081097127,  &
       3518.2675079309, 3652.0362076337, 3786.7919677129, 3922.514326349,  &
       4059.1823769006, 4196.7769920147, 4335.2799339826, 4474.6751892065,  &
       4614.9409614005, 4756.0696885878, 4898.0346814389, 5040.831491732,  &
       5184.4423265806, 5328.8538413201, 5474.0482430638, 5620.0210835902,  &
       5766.7545700128, 5914.2398058884, 6062.4634465521, 6211.4165955607,  &
       6361.0859082494, 6511.4624881749, 6662.5374388939, 6814.3018639634,  &
       6966.74686694, 7119.8591031589, 7273.6341243984, 7428.0630342154,  &
       7583.132487945, 7738.8424855872, 7895.1796824772, 8052.1396303932,  &
       8209.7134328922, 8367.8966417525, 8526.6803605309, 8686.055692784,  &
       8846.0181902904, 9006.5589566068, 9167.6779917331, 9329.3619510046,  &
       9491.6108344212, 9654.4157455398, 9817.7722361386, 9981.6758579961,  &
       1.0146117715E+04, 1.0311093358E+04, 1.047659834E+04, 1.0642628211E+04,  &
       1.0809178525E+04, 1.0976244833E+04, 1.1143818237E+04,  &
       1.1311898739E+04, 1.148048189E+04, 1.1649558794E+04, 1.181912945E+04,  &
       1.1989189411E+04, 1.2159729779E+04, 1.2330750555E+04,  &
       1.2502247292E+04, 1.2674219987E+04, 1.2846655298E+04,  &
       1.3019557673E+04, 1.3192918214E+04, 1.3366736921E+04,  &
       1.3541009348E+04, 1.3715731045E+04, 1.3890902012E+04,  &
       1.4066513353E+04, 3.3455991102E+04, 5.5537692709E+04,  &
       7.9572190293E+04, 1.0517170569E+05, 1.3209167567E+05,  &
       1.6016182232E+05, 1.8925568268E+05, 2.1927521797E+05,  &
       2.5014187258E+05, 5.9494118942E+05, 9.8761551448E+05,  &
       1.4150162161E+06, 1.8702467713E+06, 2.3489594885E+06,  &
       2.8481246839E+06, 3.365494671E+06, 3.8993261919E+06, 4.4482216153E+06,  &
       1.0579712565E+07, 1.7562566442E+07, 2.5162940237E+07,  &
       3.3258214273E+07, 4.1771056216E+07, 5.064762924E+07, 5.9847886007E+07,  &
       6.9340924721E+07, 7.9101790858E+07  &
   linear_extrapolate = no  &
   x_units = "length"  &
   y_units = "force"
!
data_element create spline  &
   spline_name = .template_2_drop._cv_spline  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   x = 1.0, 2.0, 3.0, 4.0  &
   y = 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0  &
   z = 1.0, 2.0  &
   linear_extrapolate = no
!
data_element attributes  &
   data_element_name = .template_2_drop._cv_spline  &
   visibility = off
!
data_element create spline  &
   spline_name = .template_2_drop.airspring  &
   adams_id = 2  &
   x = -127.0, -101.6, -76.2, -50.8, -25.4, 0.0, 25.4, 50.8, 76.2, 101.6,  &
       127.0, 152.4, 177.8, 203.2, 228.6, 254.0, 279.4, 304.8, 330.2, 355.6,  &
       381.0, 406.4, 431.8, 457.2, 482.6, 508.0, 533.4  &
   y = 1.7792886461E+04, 1.7792886461E+04, 1.7792886461E+04,  &
       1.7792886461E+04, 1.7792886461E+04, 1.7792886461E+04,  &
       1.8015297542E+04, 1.8682530784E+04, 1.9794586188E+04,  &
       2.1351463753E+04, 2.335316348E+04, 2.5799685369E+04, 2.8691029418E+04,  &
       3.202719563E+04, 3.5808184003E+04, 4.0033994537E+04, 4.4704627233E+04,  &
       4.9820082091E+04, 5.538035911E+04, 6.1385458291E+04, 6.7835379633E+04,  &
       7.4730123136E+04, 8.2069688802E+04, 8.9854076628E+04,  &
       9.7860875536E+04, 1.0675731877E+05, 1.1654340632E+05  &
   linear_extrapolate = no  &
   x_units = "length"  &
   y_units = "force"
!
data_element create spline  &
   spline_name = .template_2_drop.stopper  &
   adams_id = 5  &
   x = 0.0, 2.54E-03, 5.08E-03, 7.62E-03, 1.016E-02, 1.27E-02, 1.524E-02,  &
       1.778E-02, 2.032E-02, 2.286E-02, 2.54E-02, 2.794E-02, 3.048E-02,  &
       3.302E-02, 3.556E-02, 3.81E-02, 4.064E-02, 4.318E-02, 4.572E-02,  &
       4.826E-02, 5.08E-02, 5.334E-02, 5.588E-02, 5.842E-02, 6.096E-02,  &
       6.35E-02, 6.604E-02, 6.858E-02, 7.112E-02, 7.366E-02, 7.62E-02,  &
       7.874E-02, 8.128E-02, 8.382E-02, 8.636E-02, 8.89E-02, 9.144E-02,  &
       9.398E-02, 9.652E-02, 9.906E-02, 0.1016, 0.10414, 0.10668, 0.10922,  &
       0.11176, 0.1143, 0.11684, 0.11938, 0.12192, 0.12446, 0.127, 0.12954,  &
       0.13208, 0.13462, 0.13716, 0.1397, 0.14224, 0.14478, 0.14732, 0.14986,  &
       0.1524, 0.15494, 0.15748, 0.16002, 0.16256, 0.1651, 0.16764, 0.17018,  &
       0.17272, 0.17526, 0.1778, 0.18034, 0.18288, 0.18542, 0.18796, 0.1905,  &
       0.19304, 0.19558, 0.19812, 0.20066, 0.2032, 0.20574, 0.20828, 0.21082,  &
       0.21336, 0.2159, 0.21844, 0.22098, 0.22352, 0.22606, 0.2286, 0.23114,  &
       0.23368, 0.23622, 0.23876, 0.2413, 0.24384, 0.24638, 0.24892, 0.25146,  &
       0.254, 0.508, 0.762, 1.016, 1.27, 1.524, 1.778, 2.032, 2.286, 2.54,  &
       5.08, 7.62, 10.16, 12.7, 15.24, 17.78, 20.32, 22.86, 25.4, 50.8, 76.2,  &
       101.6, 127.0, 152.4, 177.8, 203.2, 228.6, 254.0  &
   y = 0.0, 44.4822161526, 105.7971256484, 175.6256644225, 251.6294023717,  &
       332.5821427257, 417.7106066388, 506.4762924022, 598.4788600706,  &
       693.4092472062, 791.0179085764, 891.1015604533, 993.4889463047,  &
       1098.0337196395, 1204.609995786, 1313.1083484925, 1423.4309168834,  &
       1535.4922951036, 1649.2141944529, 1764.527222674, 1881.368659842,  &
       1999.6802342539, 2119.4090120724, 2240.5065076819, 2362.9277940442,  &
       2486.6315026981, 2611.5784892935, 2737.7331680574, 2865.0612876834,  &
       2993.5321554424, 3123.1150786052, 3253.7824781978, 3385.5081097127,  &
       3518.2675079309, 3652.0362076337, 3786.7919677129, 3922.514326349,  &
       4059.1823769006, 4196.7769920147, 4335.2799339826, 4474.6751892065,  &
       4614.9409614005, 4756.0696885878, 4898.0346814389, 5040.831491732,  &
       5184.4423265806, 5328.8538413201, 5474.0482430638, 5620.0210835902,  &
       5766.7545700128, 5914.2398058884, 6062.4634465521, 6211.4165955607,  &
       6361.0859082494, 6511.4624881749, 6662.5374388939, 6814.3018639634,  &
       6966.74686694, 7119.8591031589, 7273.6341243984, 7428.0630342154,  &
       7583.132487945, 7738.8424855872, 7895.1796824772, 8052.1396303932,  &
       8209.7134328922, 8367.8966417525, 8526.6803605309, 8686.055692784,  &
       8846.0181902904, 9006.5589566068, 9167.6779917331, 9329.3619510046,  &
       9491.6108344212, 9654.4157455398, 9817.7722361386, 9981.6758579961,  &
       1.0146117715E+04, 1.0311093358E+04, 1.047659834E+04, 1.0642628211E+04,  &
       1.0809178525E+04, 1.0976244833E+04, 1.1143818237E+04,  &
       1.1311898739E+04, 1.148048189E+04, 1.1649558794E+04, 1.181912945E+04,  &
       1.1989189411E+04, 1.2159729779E+04, 1.2330750555E+04,  &
       1.2502247292E+04, 1.2674219987E+04, 1.2846655298E+04,  &
       1.3019557673E+04, 1.3192918214E+04, 1.3366736921E+04,  &
       1.3541009348E+04, 1.3715731045E+04, 1.3890902012E+04,  &
       1.4066513353E+04, 3.3455991102E+04, 5.5537692709E+04,  &
       7.9572190293E+04, 1.0517170569E+05, 1.3209167567E+05,  &
       1.6016182232E+05, 1.8925568268E+05, 2.1927521797E+05,  &
       2.5014187258E+05, 5.9494118942E+05, 9.8761551448E+05,  &
       1.4150162161E+06, 1.8702467713E+06, 2.3489594885E+06,  &
       2.8481246839E+06, 3.365494671E+06, 3.8993261919E+06, 4.4482216153E+06,  &
       1.0579712565E+07, 1.7562566442E+07, 2.5162940237E+07,  &
       3.3258214273E+07, 4.1771056216E+07, 5.064762924E+07, 5.9847886007E+07,  &
       6.9340924721E+07, 7.9101790858E+07  &
   linear_extrapolate = no  &
   x_units = "length"  &
   y_units = "force"
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .template_2_drop.aluminum  &
   adams_id = 2  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_2_drop.steel  &
   adams_id = 5  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_2_drop.steel_2  &
   adams_id = 3  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_2_drop.aluminum_2  &
   adams_id = 4  &
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
   default_coordinate_system = .template_2_drop.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop.ground.origo  &
   adams_id = 1  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.origo  &
   visibility = on
!
marker create  &
   marker_name = .template_2_drop.ground.uel_gearaero_origin_1  &
   adams_id = 45  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.uel_gearaero_origin_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ground.uer_gearaero_origin_1  &
   adams_id = 47  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.uer_gearaero_origin_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ground.lumian_ref_1  &
   adams_id = 239  &
   location = 1.2238367977E+04, 1509.5002745, -560.8546166  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.lumian_ref_1  &
   visibility = off
!
marker create  &
   marker_name = .template_2_drop.ground.origo1  &
   adams_id = 287  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.origo1  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ground.cfs_uc_sf_atch_mid  &
   adams_id = 289  &
   location = 6314.44, 0.0, 1691.64  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.cfs_uc_sf_atch_mid  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_drop.ground.cfs_subframe_to_body_point  &
   adams_id = 290  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
marker attributes  &
   marker_name = .template_2_drop.ground.cfs_subframe_to_body_point  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_drop.ground.cfl_spin_axis1  &
   adams_id = 292  &
   location = 6229.096, -209.55, 308.0  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.cfl_spin_axis1  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_drop.ground.cfr_spin_axis1  &
   adams_id = 293  &
   location = 6229.096, 209.55, 308.0  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.cfr_spin_axis1  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_drop.ground.cfs_wheel_centers_midpoint  &
   adams_id = 294  &
   location = 6229.096, 0.0, 508.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.cfs_wheel_centers_midpoint  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_drop.ground.cfs_nlg_axle_lowpoint  &
   adams_id = 295  &
   location = 6229.096, 0.0, 482.6  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.cfs_nlg_axle_lowpoint  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_drop.ground.cfs_collar_top  &
   adams_id = 296  &
   location = 6197.6, 0.0, 856.996  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.cfs_collar_top  &
   color = MAIZE
!
marker create  &
   marker_name = .template_2_drop.ground.lumian_ref_11  &
   adams_id = 297  &
   location = 7484.11, 0.0, 48.26  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ground.lumian_ref_11  &
   visibility = off
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_2_drop.ground.luntai1_tire_jf_11  &
   adams_id = 298
!
floating_marker create  &
   floating_marker_name = .template_2_drop.ground.luntai2_tire_jf_11  &
   adams_id = 299
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
!---------------------------------- _cv_part ----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_drop._cv_part  &
   adams_id = 2  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop._cv_part
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop._cv_part.marker  &
   adams_id = 300  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop._cv_part.marker  &
   name_visibility = off  &
   size_of_icons = 50.8
!
part create rigid_body mass_properties  &
   part_name = .template_2_drop._cv_part  &
   mass = 0.0  &
   center_of_mass_marker = .template_2_drop._cv_part.marker  &
   ixx = 0.0  &
   iyy = 0.0  &
   izz = 0.0  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
part attributes  &
   part_name = .template_2_drop._cv_part  &
   name_visibility = off  &
   size_of_icons = 50.8
!
!------------------------------- ges_dragbrace --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_drop.ges_dragbrace  &
   adams_id = 33  &
   location = 6967.855, 0.0, 1319.53  &
   orientation = 270.0d, 120.4532239091d, 90.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ges_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop.ges_dragbrace.MARKER_429  &
   adams_id = 429  &
   location = -4.5918824298E-10, 0.0, -598.873681109  &
   orientation = 90.0d, 120.4532239091d, 270.0d
!
marker create  &
   marker_name = .template_2_drop.ges_dragbrace.cm  &
   adams_id = 301  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_dragbrace.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_dragbrace.inertia_frame  &
   adams_id = 302  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_dragbrace.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_dragbrace.gralin_1  &
   adams_id = 303  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_dragbrace.gralin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_dragbrace.jxs_joint_i_12  &
   adams_id = 304  &
   location = 4.5791148651E-10, 0.0, 598.873681109  &
   orientation = 90.0d, 120.4532239091d, 270.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_dragbrace.jxs_joint_i_12  &
   visibility = off  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_2_drop.ges_dragbrace  &
   mass = 27.3726690382  &
   center_of_mass_marker = .template_2_drop.ges_dragbrace.cm  &
   inertia_marker = .template_2_drop.ges_dragbrace.inertia_frame  &
   ixx = 3.4811540175E+06  &
   iyy = 3.4811540175E+06  &
   izz = 3.5319502313E+04  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_drop.ges_dragbrace.gralin_dragbrace_geom  &
   adams_id = 85  &
   center_marker = .template_2_drop.ges_dragbrace.gralin_1  &
   angle_extent = 360.0  &
   length = 1197.7473622179  &
   radius = 50.8  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_dragbrace.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .template_2_drop.ges_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_drop.ges_upper_cylinder  &
   adams_id = 34  &
   location = 6197.6, 0.0, 1193.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ges_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.MARKER_405  &
   adams_id = 405  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.MARKER_407  &
   adams_id = 407  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.MARKER_409  &
   adams_id = 409  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.MARKER_428  &
   adams_id = 428  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.cm  &
   adams_id = 306  &
   location = -3.3167643494, 0.0, -13.3824231157  &
   orientation = 90.0d, 2.0673379194d, 270.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.inertia_frame  &
   adams_id = 307  &
   location = -3.3167643494, 0.0, -13.3824231157  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.gralin_2  &
   adams_id = 308  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.gralin_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.gralin_3  &
   adams_id = 309  &
   location = -116.84, -340.36, -497.84  &
   orientation = 161.0534953105d, 58.7414044414d, 213.4869581747d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.gralin_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.gralin_4  &
   adams_id = 310  &
   location = -116.84, 340.36, -497.84  &
   orientation = 18.9465046895d, 58.7414044414d, 326.5130418253d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.gralin_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_11  &
   adams_id = 311  &
   location = 0.0, 0.0, 114.3  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_11  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_12  &
   adams_id = 312  &
   location = -254.0, 0.0, 177.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_12  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_spring_j_1  &
   adams_id = 314  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_spring_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_damper_j_1  &
   adams_id = 315  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_damper_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_stopper_j_1  &
   adams_id = 316  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_stopper_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_1  &
   adams_id = 317  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_actuator_j_1  &
   adams_id = 318  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_actuator_j_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_actuator_j_4  &
   adams_id = 319  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_actuator_j_4  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.MARKER_2  &
   adams_id = 2  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_upper_cylinder.MARKER_116  &
   adams_id = 324  &
   location = 0.0, 0.0, -431.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_2_drop.ges_upper_cylinder  &
   mass = 82.2524279101  &
   center_of_mass_marker = .template_2_drop.ges_upper_cylinder.cm  &
   inertia_marker = .template_2_drop.ges_upper_cylinder.inertia_frame  &
   ixx = 2.7759040478E+06  &
   iyy = 2.6163591859E+06  &
   izz = 8.2729047458E+05  &
   ixy = 0.0  &
   izx = 7.0431892224E+04  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 86  &
   center_marker = .template_2_drop.ges_upper_cylinder.gralin_2  &
   angle_extent = 360.0  &
   length = 863.6  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 87  &
   center_marker = .template_2_drop.ges_upper_cylinder.gralin_3  &
   angle_extent = 360.0  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 88  &
   center_marker = .template_2_drop.ges_upper_cylinder.gralin_4  &
   angle_extent = 360.0  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_2_drop.ges_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!----------------------------- ges_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_drop.ges_lower_cylinder  &
   adams_id = 35  &
   location = 6197.6, 0.0, 952.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ges_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_378  &
   adams_id = 378  &
   location = -101.6, 0.0, 619.1  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_406  &
   adams_id = 406  &
   location = 0.0, 0.0, -244.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_408  &
   adams_id = 408  &
   location = 0.0, 0.0, -244.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_410  &
   adams_id = 410  &
   location = 0.0, 0.0, -244.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_1  &
   adams_id = 325  &
   location = 0.0, 0.0, -244.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.cm  &
   adams_id = 326  &
   location = -2.4871874502, 0.0, 34.7403924495  &
   orientation = 270.0d, 0.8125241803d, 90.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.inertia_frame  &
   adams_id = 327  &
   location = -2.4871874502, 0.0, 34.7403924495  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.gralin_5  &
   adams_id = 328  &
   location = 0.0, 0.0, -244.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.gralin_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.jxs_joint_i_11  &
   adams_id = 330  &
   location = 0.0, 0.0, -127.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.jxs_joint_i_11  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.gralin_7  &
   adams_id = 331  &
   location = -31.496, 209.55, 644.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.gralin_7  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.ues_spring_i_1  &
   adams_id = 332  &
   location = 0.0, 0.0, -244.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.ues_spring_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.ues_damper_i_1  &
   adams_id = 51  &
   location = 0.0, 0.0, -244.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.ues_damper_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.ues_stopper_i_1  &
   adams_id = 333  &
   location = 0.0, 0.0, -244.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.ues_stopper_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.coomarker_2  &
   adams_id = 334  &
   location = -31.496, 0.0, 444.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.coomarker_2  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.coomarker_3  &
   adams_id = 335  &
   location = -31.496, 0.0, 469.9  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_cylinder.coomarker_3  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_3  &
   adams_id = 336  &
   location = -31.496, -209.55, 644.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_4  &
   adams_id = 337  &
   location = -31.496, 209.55, 644.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_6  &
   adams_id = 338  &
   location = -31.496, 209.55, 644.5  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_8  &
   adams_id = 339  &
   location = -31.496, -209.55, 644.5  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_115  &
   adams_id = 344  &
   location = 0.0, 0.0, -444.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_2_drop.ges_lower_cylinder  &
   mass = 84.8838172052  &
   center_of_mass_marker = .template_2_drop.ges_lower_cylinder.cm  &
   inertia_marker = .template_2_drop.ges_lower_cylinder.inertia_frame  &
   ixx = 6.8342355549E+06  &
   iyy = 6.4494598026E+06  &
   izz = 8.0365064324E+05  &
   ixy = 0.0  &
   izx = -8.5544003848E+04  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_drop.ges_lower_cylinder.gralin_geom1  &
   adams_id = 89  &
   center_marker = .template_2_drop.ges_lower_cylinder.gralin_5  &
   angle_extent = 360.0  &
   length = 889.0  &
   radius = 101.6  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_2_drop.ges_lower_cylinder.gralin_geom2  &
   adams_id = 90  &
   center_marker = .template_2_drop.ges_lower_cylinder.gralin_7  &
   angle_extent = 360.0  &
   length = 419.1  &
   radius = 30.48  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_lower_cylinder.gralin_geom2  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_2_drop.ges_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!---------------------------- ges_upper_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_drop.ges_upper_torque_arm  &
   adams_id = 36  &
   location = 6489.7, 0.0, 774.7  &
   orientation = 90.0d, 111.0375110254d, 270.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ges_upper_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop.ges_upper_torque_arm.cm  &
   adams_id = 345  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_upper_torque_arm.inertia_frame  &
   adams_id = 346  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_torque_arm.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_upper_torque_arm.gralin_9  &
   adams_id = 347  &
   location = -6.7459926534E-11, 0.0, -176.8905311202  &
   orientation = 90.0d, 13.4695391009d, 270.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_torque_arm.gralin_9  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_upper_torque_arm.jxs_joint_j_8  &
   adams_id = 348  &
   location = 93.3345606204, 0.0, 212.7884390511  &
   orientation = 0.0d, 90.0d, 111.0375110254d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_torque_arm.jxs_joint_j_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_upper_torque_arm.jxs_joint_i_10  &
   adams_id = 349  &
   location = -6.7459926534E-11, 0.0, -176.8905311202  &
   orientation = 0.0d, 90.0d, 111.0375110254d
!
marker attributes  &
   marker_name = .template_2_drop.ges_upper_torque_arm.jxs_joint_i_10  &
   visibility = off  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_2_drop.ges_upper_torque_arm  &
   mass = 0.3898630024  &
   center_of_mass_marker = .template_2_drop.ges_upper_torque_arm.cm  &
   inertia_marker = .template_2_drop.ges_upper_torque_arm.inertia_frame  &
   ixx = 2577.4839558745  &
   iyy = 2577.4839558745  &
   izz = 31.4405018244  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_drop.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   adams_id = 91  &
   center_marker = .template_2_drop.ges_upper_torque_arm.gralin_9  &
   angle_extent = 360.0  &
   length = 400.7006862984  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   color = GREEN
!
part attributes  &
   part_name = .template_2_drop.ges_upper_torque_arm  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!---------------------------- ges_lower_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_drop.ges_lower_torque_arm  &
   adams_id = 37  &
   location = 6477.0, 0.0, 622.3  &
   orientation = 90.0d, 63.4349488229d, 270.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ges_lower_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop.ges_lower_torque_arm.MARKER_379  &
   adams_id = 379  &
   location = 178.8854381999, 0.0, -288.2291622998  &
   orientation = 0.0d, 90.0d, 63.4349488229d
!
marker create  &
   marker_name = .template_2_drop.ges_lower_torque_arm.cm  &
   adams_id = 350  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_lower_torque_arm.inertia_frame  &
   adams_id = 351  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_torque_arm.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_lower_torque_arm.jxs_joint_i_8  &
   adams_id = 352  &
   location = 89.4427191001, 0.0, 154.0650836497  &
   orientation = 0.0d, 90.0d, 63.4349488229d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_torque_arm.jxs_joint_i_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_lower_torque_arm.gralin_10  &
   adams_id = 353  &
   location = 178.8854381999, 0.0, -288.2291622998  &
   orientation = 270.0d, 11.4324305526d, 90.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_lower_torque_arm.gralin_10  &
   visibility = off  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_2_drop.ges_lower_torque_arm  &
   mass = 0.3898630024  &
   center_of_mass_marker = .template_2_drop.ges_lower_torque_arm.cm  &
   inertia_marker = .template_2_drop.ges_lower_torque_arm.inertia_frame  &
   ixx = 2577.4839558745  &
   iyy = 2577.4839558745  &
   izz = 31.4405018244  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_drop.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   adams_id = 92  &
   center_marker = .template_2_drop.ges_lower_torque_arm.gralin_10  &
   angle_extent = 360.0  &
   length = 451.2473822639  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_2_drop.ges_lower_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!------------------------------- ges_subframe_2 -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_drop.ges_subframe_2  &
   adams_id = 38  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ges_subframe_2
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop.ges_subframe_2.cm  &
   adams_id = 355  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_subframe_2.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_subframe_2.inertia_frame  &
   adams_id = 356  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_subframe_2.inertia_frame  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_subframe_2.graout_1  &
   adams_id = 357  &
   location = -390.5595878992, 5.9337951219E-11, -340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_subframe_2.graout_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_subframe_2.graout_2  &
   adams_id = 358  &
   location = -390.5595878992, 5.9337951219E-11, 340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_subframe_2.graout_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
marker create  &
   marker_name = .template_2_drop.ges_subframe_2.graout_3  &
   adams_id = 359  &
   location = 781.1191757984, -1.1845385783E-10, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_subframe_2.graout_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 50.8
!
part create rigid_body mass_properties  &
   part_name = .template_2_drop.ges_subframe_2  &
   mass = 4.5359237E-03  &
   center_of_mass_marker = .template_2_drop.ges_subframe_2.cm  &
   inertia_marker = .template_2_drop.ges_subframe_2.inertia_frame  &
   ixx = 2.9263965343  &
   iyy = 2.9263965343  &
   izz = 2.9263965343  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create curve outline  &
   outline_name = .template_2_drop.ges_subframe_2.graout_subframe_geom  &
   adams_id = 34  &
   marker_name =  &
      .template_2_drop.ges_subframe_2.graout_1,  &
      .template_2_drop.ges_subframe_2.graout_2,  &
      .template_2_drop.ges_subframe_2.graout_3  &
   visibility_between_markers = on, on, on  &
   close = yes
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_subframe_2.graout_subframe_geom  &
   color = WHITE
!
part attributes  &
   part_name = .template_2_drop.ges_subframe_2  &
   active = off  &
   visibility = off  &
   name_visibility = on  &
   size_of_icons = 50.8
!
!------------------------------ mts_body_mount_2 ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_drop.mts_body_mount_2  &
   adams_id = 39  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.mts_body_mount_2
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop.mts_body_mount_2.MARKER_430  &
   adams_id = 430  &
   location = 779.78, 0.0, -45.72  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.mts_body_mount_2.MARKER_427  &
   adams_id = 427  &
   location = -506.73, 0.0, -43.18  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.mts_body_mount_2.MARKER_109  &
   adams_id = 365  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.mts_body_mount_2.cm  &
   adams_id = 366  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.mts_body_mount_2.MARKER_111  &
   adams_id = 367  &
   location = 0.0, 0.0, 0.0  &
   orientation = 90.0d, 3.3555200908d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_2_drop.mts_body_mount_2  &
   mass = 5000.0  &
   center_of_mass_marker = .template_2_drop.mts_body_mount_2.cm  &
   ixx = 292.63965343  &
   iyy = 292.63965343  &
   izz = 292.63965343  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_2_drop.mts_body_mount_2.ELLIPSOID_38  &
   adams_id = 38  &
   center_marker = .template_2_drop.mts_body_mount_2.MARKER_109  &
   x_scale_factor = 200.0  &
   y_scale_factor = 200.0  &
   z_scale_factor = 200.0
!
part attributes  &
   part_name = .template_2_drop.mts_body_mount_2  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- ges_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
part create rigid_body name_and_position  &
   part_name = .template_2_drop.ges_collar  &
   adams_id = 40  &
   location = 6197.6, 0.0, 809.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ges_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_2_drop.ges_collar.jxs_joint_j_10  &
   adams_id = 368  &
   location = 127.0, 0.0, 28.702  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_collar.jxs_joint_j_10  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_collar.cm  &
   adams_id = 369  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_collar.cm  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_collar.inertia_frame  &
   adams_id = 370  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_2_drop.ges_collar.gralin_24  &
   adams_id = 371  &
   location = 0.0, 0.0, -47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_collar.gralin_24  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_collar.jxs_joint_i_1  &
   adams_id = 372  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_collar.jxs_joint_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_collar.ues_actuator_i_1  &
   adams_id = 373  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_collar.ues_actuator_i_1  &
   visibility = off  &
   name_visibility = off
!
marker create  &
   marker_name = .template_2_drop.ges_collar.ues_actuator_i_4  &
   adams_id = 374  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_2_drop.ges_collar.ues_actuator_i_4  &
   visibility = off  &
   name_visibility = off
!
part create rigid_body mass_properties  &
   part_name = .template_2_drop.ges_collar  &
   mass = 6.4242828175  &
   center_of_mass_marker = .template_2_drop.ges_collar.cm  &
   inertia_marker = .template_2_drop.ges_collar.inertia_frame  &
   ixx = 8.5080541407E+04  &
   iyy = 8.5080541407E+04  &
   izz = 1.4685428308E+05  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_2_drop.ges_collar.gralin_collar  &
   adams_id = 93  &
   center_marker = .template_2_drop.ges_collar.gralin_24  &
   angle_extent = 360.0  &
   length = 94.996  &
   radius = 139.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_2_drop.ges_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .template_2_drop.ges_collar  &
   visibility = on  &
   name_visibility = on
!
!--------------------------------- Equations ----------------------------------!
!
!
part create equation differential_equation  &
   differential_equation_name = .template_2_drop._cv_diff  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   initial_condition = 0.0  &
   function = ""  &
   implicit = off  &
   static_hold = off
!
part attributes  &
   equation_name = .template_2_drop._cv_diff  &
   visibility = off
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_2_drop.JOINT_51  &
   adams_id = 51  &
   i_marker_name = .template_2_drop.ges_lower_cylinder.MARKER_378  &
   j_marker_name = .template_2_drop.ges_lower_torque_arm.MARKER_379
!
constraint attributes  &
   constraint_name = .template_2_drop.JOINT_51  &
   name_visibility = off
!
constraint create joint spherical  &
   joint_name = .template_2_drop.JOINT_57  &
   adams_id = 57  &
   i_marker_name = .template_2_drop.ges_dragbrace.MARKER_429  &
   j_marker_name = .template_2_drop.mts_body_mount_2.MARKER_430
!
constraint attributes  &
   constraint_name = .template_2_drop.JOINT_57  &
   name_visibility = off
!
constraint create joint fixed  &
   joint_name = .template_2_drop.JOINT_56  &
   adams_id = 56  &
   i_marker_name = .template_2_drop.mts_body_mount_2.MARKER_427  &
   j_marker_name = .template_2_drop.ges_upper_cylinder.MARKER_428
!
constraint attributes  &
   constraint_name = .template_2_drop.JOINT_56  &
   name_visibility = off
!
constraint create joint spherical  &
   joint_name = .template_2_drop.josrev_lta_uta_joint  &
   adams_id = 39  &
   i_marker_name = .template_2_drop.ges_lower_torque_arm.jxs_joint_i_8  &
   j_marker_name = .template_2_drop.ges_upper_torque_arm.jxs_joint_j_8
!
constraint attributes  &
   constraint_name = .template_2_drop.josrev_lta_uta_joint  &
   size_of_icons = 50.8
!
constraint create joint revolute  &
   joint_name = .template_2_drop.josrev_uta_uc_joint  &
   adams_id = 41  &
   i_marker_name = .template_2_drop.ges_upper_torque_arm.jxs_joint_i_10  &
   j_marker_name = .template_2_drop.ges_collar.jxs_joint_j_10
!
constraint create joint cylindrical  &
   joint_name = .template_2_drop.joscyl_lc_uc_joint  &
   adams_id = 42  &
   i_marker_name = .template_2_drop.ges_lower_cylinder.jxs_joint_i_11  &
   j_marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_11
!
constraint create joint spherical  &
   joint_name = .template_2_drop.jossph_db_uc_joint  &
   adams_id = 43  &
   i_marker_name = .template_2_drop.ges_dragbrace.jxs_joint_i_12  &
   j_marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_12
!
constraint create joint fixed  &
   joint_name = .template_2_drop.josrev_collar_uc_joint  &
   adams_id = 48  &
   i_marker_name = .template_2_drop.ges_collar.jxs_joint_i_1  &
   j_marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_1
!
!----------------------------------- Forces -----------------------------------!
!
!
force create direct single_component_force  &
   single_component_force_name = .template_2_drop.NLG_AIR  &
   adams_id = 11  &
   type_of_freedom = translational  &
   i_marker_name = .template_2_drop.ges_upper_cylinder.MARKER_405  &
   j_marker_name = .template_2_drop.ges_lower_cylinder.MARKER_406  &
   action_only = off  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_2_drop.NLG_OIL  &
   adams_id = 12  &
   type_of_freedom = translational  &
   i_marker_name = .template_2_drop.ges_upper_cylinder.MARKER_407  &
   j_marker_name = .template_2_drop.ges_lower_cylinder.MARKER_408  &
   action_only = off  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_2_drop.NLG_STOP  &
   adams_id = 13  &
   type_of_freedom = translational  &
   i_marker_name = .template_2_drop.ges_upper_cylinder.MARKER_409  &
   j_marker_name = .template_2_drop.ges_lower_cylinder.MARKER_410  &
   action_only = off  &
   function = ""
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
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .template_2_drop.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=2.0 number_of_steps=400 model_name=.GCMB"
!
!-------------------------- Adams View UDE Instances --------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
undo begin_block suppress = yes
!
ude create instance  &
   instance_name = .template_2_drop.lumian  &
   definition_name = .MDI.Forces.vpg_road  &
   location = 1.2238367977E+04, 1509.5002745, -560.8546166  &
   orientation = 0.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_2_drop.lumian  &
   color = DimGray  &
   visibility = off
!
ude create instance  &
   instance_name = .template_2_drop.lumian_2  &
   definition_name = .MDI.Forces.vpg_road  &
   location = 7484.11, 0.0, 48.26  &
   orientation = 0.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_2_drop.lumian_2  &
   active = off  &
   color = DimGray  &
   visibility = off
!
ude create instance  &
   instance_name = .template_2_drop.luntai1_2  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 6229.096, -209.55, 308.0  &
   orientation = 0.0, 90.0, 0.0
!
ude create instance  &
   instance_name = .template_2_drop.luntai2_2  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 6229.096, 209.55, 308.0  &
   orientation = 0.0, 90.0, 0.0
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_2_drop.lumian.ref_marker  &
   object_value = .template_2_drop.ground.lumian_ref_1
!
variable modify  &
   variable_name = .template_2_drop.lumian.road_property_file  &
   string_value = "D:/shuoshi/program/GCMB2_DROP/drop_qianqi/2d_flat.rdf"
!
variable modify  &
   variable_name = .template_2_drop.lumian.road_graphics  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_2_drop.lumian
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker create  &
   marker_name = .template_2_drop.lumian.road_part.MARKER_112  &
   adams_id = 375  &
   location = 6704.3299999, 0.0, 2146.3  &
   orientation = 90.0d, 3.3555200908d, 0.0d
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_2_drop.lumian_2.ref_marker  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_2_drop.lumian_2.road_property_file  &
   string_value = "C:/Users/D4/Desktop/quanji/DM/2d_flat.rdf"
!
variable modify  &
   variable_name = .template_2_drop.lumian_2.road_graphics  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_2_drop.lumian_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.vmmrk  &
   object_value = (.template_2_drop.luntai1_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.wmmrk  &
   object_value = (.template_2_drop.luntai1_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.road_property_file  &
   string_value = (.template_2_drop.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.j_fmarker  &
   object_value = .template_2_drop.ground.luntai1_tire_jf_11
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.ref_marker  &
   object_value = (.template_2_drop.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.wheel_tire_mass  &
   real_value = (.template_2_drop.NLG_m)
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.Ixx_Iyy  &
   real_value = (.template_2_drop.NLG_Ixx_Iyy)
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.Izz  &
   real_value = (.template_2_drop.NLG_Izz)
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.property_file  &
   string_value = "D:/shuoshi/program/GCMB2_DROP/drop_qianqi/NLG.tir"
!
variable modify  &
   variable_name = .template_2_drop.luntai1_2.road_name  &
   string_value = (.template_2_drop.lumian)
!
ude modify instance  &
   instance_name = .template_2_drop.luntai1_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker create  &
   marker_name = .template_2_drop.luntai1_2.wheel_part.MARKER_7  &
   adams_id = 376  &
   location = 6229.096, -209.55, 308.0  &
   orientation = 0.0d, 90.0d, 0.0d
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.vmmrk  &
   object_value = (.template_2_drop.luntai2_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.wmmrk  &
   object_value = (.template_2_drop.luntai2_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.road_property_file  &
   string_value = (.template_2_drop.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.j_fmarker  &
   object_value = .template_2_drop.ground.luntai2_tire_jf_11
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.ref_marker  &
   object_value = (.template_2_drop.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.wheel_tire_mass  &
   real_value = (.template_2_drop.NLG_m)
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.Ixx_Iyy  &
   real_value = (.template_2_drop.NLG_Ixx_Iyy)
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.Izz  &
   real_value = (.template_2_drop.NLG_Izz)
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.property_file  &
   string_value = "D:/shuoshi/program/GCMB2_DROP/drop_qianqi/NLG.tir"
!
variable modify  &
   variable_name = .template_2_drop.luntai2_2.road_name  &
   string_value = (.template_2_drop.lumian)
!
ude modify instance  &
   instance_name = .template_2_drop.luntai2_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker create  &
   marker_name = .template_2_drop.luntai2_2.wheel_part.MARKER_5  &
   adams_id = 377  &
   location = 6229.096, 209.55, 308.0  &
   orientation = 0.0d, 90.0d, 0.0d
!
undo end_block
!
!--------------------------- UDE Dependent Objects ----------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_2_drop.JOINT_1  &
   adams_id = 1  &
   i_marker_name = .template_2_drop.luntai2_2.wheel_part.MARKER_5  &
   j_marker_name = .template_2_drop.ges_lower_cylinder.MARKER_6
!
constraint attributes  &
   constraint_name = .template_2_drop.JOINT_1  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_2_drop.JOINT_2  &
   adams_id = 49  &
   i_marker_name = .template_2_drop.luntai1_2.wheel_part.MARKER_7  &
   j_marker_name = .template_2_drop.ges_lower_cylinder.MARKER_8
!
constraint attributes  &
   constraint_name = .template_2_drop.JOINT_2  &
   name_visibility = off
!
constraint create joint translational  &
   joint_name = .template_2_drop.JOINT_15  &
   adams_id = 50  &
   i_marker_name = .template_2_drop.mts_body_mount_2.MARKER_111  &
   j_marker_name = .template_2_drop.lumian.road_part.MARKER_112
!
constraint attributes  &
   constraint_name = .template_2_drop.JOINT_15  &
   name_visibility = off
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
geometry create shape force  &
   force_name = .template_2_drop.NLG_OIL_force_graphic_2  &
   adams_id = 210  &
   force_element_name = .template_2_drop.NLG_OIL  &
   applied_at_marker_name = .template_2_drop.ges_lower_cylinder.MARKER_408
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   z_component_gravity = -9809.9999999989
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------------- Measures ----------------------------------!
!
!
measure create function  &
   measure_name = .template_2_drop.hcqwy  &
   function = ""  &
   units = "length"  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_2_drop.hcqwy  &
   color = WHITE
!
measure create function  &
   measure_name = .template_2_drop.cxzh  &
   function = ""  &
   units = "force"  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_2_drop.cxzh  &
   color = WHITE
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_2_drop.mts_body_mount_2.minor_role  &
   string_value = "inherit"
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
   variable_name = .template_2_drop.NLG_V_LOW  &
   units = "volume"  &
   range = -6.4516E+05, 6.4516E+05  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.028E+07
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
!---------------------------- Function definitions ----------------------------!
!
!
data_element modify variable  &
   variable_name = .template_2_drop.NLG_V  &
   function = "-1*VR(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1)"
!
data_element modify variable  &
   variable_name = .template_2_drop.NLG_S  &
   function = "428.6-DM(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1)"
!
data_element modify variable  &
   variable_name = .template_2_drop.x1  &
   function = "-1*(VARVAL(.template_2_drop.NLG_V)*0.5*(VARVAL(.template_2_drop.NLG_V)-ABS(VARVAL(.template_2_drop.NLG_V)))*((.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_MAIN_OIL**3/(2*.template_2_drop.NLG_MAIN_Cd**2*.template_2_drop.NLG_A_MAIN_NEG**2))+(.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_RET_OIL**3/(2*.template_2_drop.NLG_RET_Cd**2*.template_2_drop.NLG_A_RET_NEG**2))))"
!
data_element modify variable  &
   variable_name = .template_2_drop.x2  &
   function = "0.00001*VARVAL(.template_2_drop.NLG_V)*0.5*(VARVAL(.template_2_drop.NLG_V)+ABS(VARVAL(.template_2_drop.NLG_V)))*((.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_MAIN_OIL**3/(2*.template_2_drop.NLG_MAIN_Cd**2*.template_2_drop.NLG_A_MAIN_POS**2))+(.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_RET_OIL**3/(2*.template_2_drop.NLG_RET_Cd**2*.template_2_drop.NLG_A_RET_POS**2)))"
!
data_element modify variable  &
   variable_name = .template_2_drop.VARIABLE_123  &
   function = "IF(TIME:0,1,2)"
!
data_element modify variable  &
   variable_name = .template_2_drop.VARIABLE_124  &
   function = "VARVAL(.template_2_drop.NLG_V)-ABS(VARVAL(.template_2_drop.NLG_V))"
!
data_element modify variable  &
   variable_name = .template_2_drop._cv_solver_variable  &
   function = "0"
!
measure modify function  &
   measure_name = .template_2_drop.hcqwy  &
   function = "428.6-DZ(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1)"
!
measure modify function  &
   measure_name = .template_2_drop.cxzh  &
   function = ".template_2_drop.luntai1_2.vertical_force_iso+.template_2_drop.luntai2_2.vertical_force_iso"
!
part modify equation differential_equation  &
   differential_equation_name = .template_2_drop._cv_diff  &
   function = "0"
!
force modify direct single_component_force  &
   single_component_force_name = .template_2_drop.NLG_AIR  &
   function = "1*.template_2_drop.NLG_A_LOW*(.template_2_drop.NLG_P_LOW*(.template_2_drop.NLG_V_LOW/(.template_2_drop.NLG_V_LOW-.template_2_drop.NLG_A_LOW*(428.6-DM(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1))))**1.1-.template_2_drop.Patm)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_2_drop.NLG_OIL  &
   function = "IF(VARVAL(.template_2_drop.NLG_V):-0.001*(VARVAL(.template_2_drop.NLG_V)*0.5*(VARVAL(.template_2_drop.NLG_V)-ABS(VARVAL(.template_2_drop.NLG_V)))*((.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_MAIN_OIL**3/(2*.template_2_drop.NLG_MAIN_Cd**2*.template_2_drop.NLG_A_MAIN_NEG**2))+(.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_RET_OIL**3/(2*.template_2_drop.NLG_RET_Cd**2*.template_2_drop.NLG_A_RET_NEG**2)))),0,0.001*VARVAL(.template_2_drop.NLG_V)*0.5*(VARVAL(.template_2_drop.NLG_V)+ABS(VARVAL(.template_2_drop.NLG_V)))*((.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_MAIN_OIL**3/(2*.template_2_drop.NLG_MAIN_Cd**2*.template_2_drop.NLG_A_MAIN_POS**2))+(.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_RET_OIL**3/(2*.template_2_drop.NLG_RET_Cd**2*.template_2_drop.NLG_A_RET_POS**2))))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_2_drop.NLG_STOP  &
   function = "IF(428.6-DM(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1) :1.0E+09*(428.6-DM(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1)), 0 , 0 )"
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_2_drop.lumian
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_2_drop.lumian_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_2_drop.luntai1_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_2_drop.luntai2_2
!
!------------------------- Part IC Reference Markers --------------------------!
!
!
part modify rigid_body initial_velocity  &
   part_name = .template_2_drop.luntai1_2.wheel_part  &
   vm = .template_2_drop.luntai1_2.wheel_part.wheel_cm  &
   wm = .template_2_drop.luntai1_2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_2_drop.luntai1_2.belt_part  &
   vm = .template_2_drop.luntai1_2.wheel_part.wheel_cm  &
   wm = .template_2_drop.luntai1_2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_2_drop.luntai2_2.wheel_part  &
   vm = .template_2_drop.luntai2_2.wheel_part.wheel_cm  &
   wm = .template_2_drop.luntai2_2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_2_drop.luntai2_2.belt_part  &
   vm = .template_2_drop.luntai2_2.wheel_part.wheel_cm  &
   wm = .template_2_drop.luntai2_2.wheel_part.wheel_cm
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_2_drop.ground.uel_gearaero_origin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.origo))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.origo))
!
marker modify  &
   marker_name = .template_2_drop.ground.uer_gearaero_origin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.origo))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.origo))
!
marker modify  &
   marker_name = .template_2_drop.ground.lumian_ref_1  &
   location =   &
      (.template_2_drop.lumian.location)  &
   orientation =   &
      (.template_2_drop.lumian.orientation)
!
marker modify  &
   marker_name = .template_2_drop.ground.cfl_spin_axis1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_drop.ground.hpl_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hpl_wheel_center1, .template_2_drop.ground.hpl_ob_axle1, "Z"))
!
marker modify  &
   marker_name = .template_2_drop.ground.cfr_spin_axis1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_drop.ground.hpr_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hpr_wheel_center1, .template_2_drop.ground.hpr_ob_axle1, "Z"))
!
marker modify  &
   marker_name = .template_2_drop.ground.cfs_nlg_axle_lowpoint  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_drop.ground.hps_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_2_drop.ground.origo1))
!
marker modify  &
   marker_name = .template_2_drop.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_2_drop.ground.hps_uc_bot, .template_2_drop.ground.hps_uc_top, 0.11 * DM(.template_2_drop.ground.hps_uc_bot, .template_2_drop.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_uc_bot, .template_2_drop.ground.hps_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_2_drop.ground.lumian_ref_11  &
   location =   &
      (.template_2_drop.lumian_2.location)  &
   orientation =   &
      (.template_2_drop.lumian_2.orientation)
!
material modify  &
   material_name = .template_2_drop.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_2_drop.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_2_drop.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_2_drop.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .template_2_drop.ges_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_dragbrace))  &
   relative_to = .template_2_drop.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_dragbrace.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_db_sf_atch, .template_2_drop.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .template_2_drop.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_dragbrace.jxs_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_12))  &
   relative_to = .template_2_drop.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_drop.ges_dragbrace.gralin_dragbrace_geom  &
   length = (DM(.template_2_drop.ground.hps_db_sf_atch, .template_2_drop.ground.hps_db_uc_atch))
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.MARKER_428  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_top))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_uc_top, .template_2_drop.ground.hps_uc_bot, "Z"))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_uc_sf_atch_l, .template_2_drop.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_uc_sf_atch_r, .template_2_drop.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_12  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_drop.ground.hps_db_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_2_drop.ground.origo1))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_top))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_top))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_top))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_drop.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_uc_bot, .template_2_drop.ground.hps_uc_top, "Z"))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_cylinder.ues_actuator_j_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_2_drop.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.template_2_drop.ground.hps_uc_top, .template_2_drop.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.template_2_drop.ground.hps_uc_sf_atch_l, .template_2_drop.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.template_2_drop.ground.hps_uc_sf_atch_r, .template_2_drop.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_378  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_lta_lc_atch))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_lower_cylinder))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_lc_top, .template_2_drop.ground.hps_lc_bot, "Z"))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hpr_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hpr_wheel_center1, .template_2_drop.ground.hpl_wheel_center1, "Z"))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.ues_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_lc_top))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.ues_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_lc_top))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.ues_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_lc_top))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.coomarker_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.cfs_wheel_centers_midpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.cfs_wheel_centers_midpoint))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.coomarker_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.cfs_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.cfs_nlg_axle_lowpoint))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hpl_wheel_center1))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_cylinder.MARKER_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hpr_wheel_center1))  &
   relative_to = .template_2_drop.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_drop.ges_lower_cylinder.gralin_geom1  &
   length = (DM(.template_2_drop.ground.hps_lc_top, .template_2_drop.ground.hps_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_drop.ges_lower_cylinder.gralin_geom2  &
   length = (DM(.template_2_drop.ground.hpr_wheel_center1, .template_2_drop.ground.hpl_wheel_center1))
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_torque_arm))  &
   relative_to = .template_2_drop.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_torque_arm.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_uta_uc_atch, .template_2_drop.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_2_drop.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_torque_arm.jxs_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_drop.ground.hps_lta_uta_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_2_drop.ground.origo1))  &
   relative_to = .template_2_drop.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_upper_torque_arm.jxs_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_collar.jxs_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_collar.jxs_joint_j_10))  &
   relative_to = .template_2_drop.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_drop.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   length = (DM(.template_2_drop.ground.hps_uta_uc_atch, .template_2_drop.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_torque_arm.MARKER_379  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_lta_lc_atch))  &
   relative_to = .template_2_drop.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_lower_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_lower_torque_arm))  &
   relative_to = .template_2_drop.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_torque_arm.jxs_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_torque_arm.jxs_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_torque_arm.jxs_joint_j_8))  &
   relative_to = .template_2_drop.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_lower_torque_arm.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_lta_lc_atch, .template_2_drop.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_2_drop.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_drop.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   length = (DM(.template_2_drop.ground.hps_lta_lc_atch, .template_2_drop.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_2_drop.ges_subframe_2.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_subframe_2.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_subframe_2))  &
   relative_to = .template_2_drop.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_subframe_2.graout_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_sf_atch_r))  &
   relative_to = .template_2_drop.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_subframe_2.graout_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_sf_atch_l))  &
   relative_to = .template_2_drop.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_subframe_2.graout_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_db_sf_atch))  &
   relative_to = .template_2_drop.ges_subframe_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.mts_body_mount_2.MARKER_427  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_top))  &
   relative_to = .template_2_drop.mts_body_mount_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
geometry modify shape ellipsoid  &
   ellipsoid_name = .template_2_drop.mts_body_mount_2.ELLIPSOID_38  &
   x_scale_factor = (2 * 10.0cm)  &
   y_scale_factor = (2 * 10.0cm)  &
   z_scale_factor = (2 * 10.0cm)
!
part modify rigid_body name_and_position  &
   part_name = .template_2_drop.mts_body_mount_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.origo1))
!
marker modify  &
   marker_name = .template_2_drop.ges_collar.jxs_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_2_drop.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_2_drop.ground.origo1))  &
   relative_to = .template_2_drop.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_collar))  &
   relative_to = .template_2_drop.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_collar.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hps_uc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_2_drop.ground.hps_uc_bot, .template_2_drop.ground.cfs_collar_top, "Z"))  &
   relative_to = .template_2_drop.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_2_drop.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_collar.ues_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_2_drop.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
marker modify  &
   marker_name = .template_2_drop.ges_collar.ues_actuator_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_2_drop.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_2_drop.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_2_drop.ges_collar.gralin_collar  &
   length = (DM(.template_2_drop.ground.hps_uc_bot, .template_2_drop.ground.cfs_collar_top))
!
marker modify  &
   marker_name = .template_2_drop.luntai1_2.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_2_drop.luntai1_2.wheel_part.wheel_cm))  &
   relative_to = .template_2_drop.luntai1_2.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
ude modify instance  &
   instance_name = .template_2_drop.luntai1_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hpl_wheel_center1))
!
marker modify  &
   marker_name = .template_2_drop.luntai2_2.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_2_drop.luntai2_2.wheel_part.wheel_cm))  &
   relative_to = .template_2_drop.luntai2_2.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_2_drop.ground
!
ude modify instance  &
   instance_name = .template_2_drop.luntai2_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_2_drop.ground.hpr_wheel_center1))
!
geometry modify shape force  &
   force_name = .template_2_drop.NLG_OIL_force_graphic_2  &
   applied_at_marker_name = (.template_2_drop.NLG_OIL.j)
!
model display  &
   model_name = template_2_drop

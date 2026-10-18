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
   model_name = template_5_turn_force  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_5_turn_force  &
   size_of_icons = 5.0E-02
!
view erase
!
!-------------------------------- Data storage --------------------------------!
!
!
data_element create variable  &
   variable_name = .template_5_turn_force.NLG_V  &
   adams_id = 115  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force.LMLG_S  &
   adams_id = 116  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force.RMLG_S  &
   adams_id = 117  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force.LMLG_V  &
   adams_id = 118  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force.RMLG_V  &
   adams_id = 119  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force.NLG_S  &
   adams_id = 120  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force.x1  &
   adams_id = 121  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force.x2  &
   adams_id = 122  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force.VARIABLE_123  &
   adams_id = 123  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force.VARIABLE_124  &
   adams_id = 124  &
   initial_condition = 0.0  &
   function = ""
!
data_element create variable  &
   variable_name = .template_5_turn_force._cv_solver_variable  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   function = ""
!
data_element attributes  &
   data_element_name = .template_5_turn_force._cv_solver_variable  &
   visibility = off
!
data_element create array ic_array  &
   array_name = .template_5_turn_force._cv_array  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   size = 1  &
   numbers = 0.0
!
data_element attributes  &
   data_element_name = .template_5_turn_force._cv_array  &
   visibility = off
!
data_element create spline  &
   spline_name = .template_5_turn_force.SPLINE_airspring  &
   adams_id = 4  &
   x = -0.127, -0.1016, -7.62E-02, -5.08E-02, -2.54E-02, 0.0, 2.54E-02,  &
       5.08E-02, 7.62E-02, 0.1016, 0.127, 0.1524, 0.1778, 0.2032, 0.2286,  &
       0.254, 0.2794, 0.3048, 0.3302, 0.3556, 0.381, 0.4064, 0.4318, 0.4572,  &
       0.4826  &
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
   spline_name = .template_5_turn_force.SPLINE_stopper  &
   adams_id = 3  &
   x = 0.0, 2.54E-06, 5.08E-06, 7.62E-06, 1.016E-05, 1.27E-05, 1.524E-05,  &
       1.778E-05, 2.032E-05, 2.286E-05, 2.54E-05, 2.794E-05, 3.048E-05,  &
       3.302E-05, 3.556E-05, 3.81E-05, 4.064E-05, 4.318E-05, 4.572E-05,  &
       4.826E-05, 5.08E-05, 5.334E-05, 5.588E-05, 5.842E-05, 6.096E-05,  &
       6.35E-05, 6.604E-05, 6.858E-05, 7.112E-05, 7.366E-05, 7.62E-05,  &
       7.874E-05, 8.128E-05, 8.382E-05, 8.636E-05, 8.89E-05, 9.144E-05,  &
       9.398E-05, 9.652E-05, 9.906E-05, 1.016E-04, 1.0414E-04, 1.0668E-04,  &
       1.0922E-04, 1.1176E-04, 1.143E-04, 1.1684E-04, 1.1938E-04, 1.2192E-04,  &
       1.2446E-04, 1.27E-04, 1.2954E-04, 1.3208E-04, 1.3462E-04, 1.3716E-04,  &
       1.397E-04, 1.4224E-04, 1.4478E-04, 1.4732E-04, 1.4986E-04, 1.524E-04,  &
       1.5494E-04, 1.5748E-04, 1.6002E-04, 1.6256E-04, 1.651E-04, 1.6764E-04,  &
       1.7018E-04, 1.7272E-04, 1.7526E-04, 1.778E-04, 1.8034E-04, 1.8288E-04,  &
       1.8542E-04, 1.8796E-04, 1.905E-04, 1.9304E-04, 1.9558E-04, 1.9812E-04,  &
       2.0066E-04, 2.032E-04, 2.0574E-04, 2.0828E-04, 2.1082E-04, 2.1336E-04,  &
       2.159E-04, 2.1844E-04, 2.2098E-04, 2.2352E-04, 2.2606E-04, 2.286E-04,  &
       2.3114E-04, 2.3368E-04, 2.3622E-04, 2.3876E-04, 2.413E-04, 2.4384E-04,  &
       2.4638E-04, 2.4892E-04, 2.5146E-04, 2.54E-04, 5.08E-04, 7.62E-04,  &
       1.016E-03, 1.27E-03, 1.524E-03, 1.778E-03, 2.032E-03, 2.286E-03,  &
       2.54E-03, 5.08E-03, 7.62E-03, 1.016E-02, 1.27E-02, 1.524E-02,  &
       1.778E-02, 2.032E-02, 2.286E-02, 2.54E-02, 5.08E-02, 7.62E-02, 0.1016,  &
       0.127, 0.1524, 0.1778, 0.2032, 0.2286, 0.254  &
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
   spline_name = .template_5_turn_force.airspring  &
   adams_id = 2  &
   x = -0.127, -0.1016, -7.62E-02, -5.08E-02, -2.54E-02, 0.0, 2.54E-02,  &
       5.08E-02, 7.62E-02, 0.1016, 0.127, 0.1524, 0.1778, 0.2032, 0.2286,  &
       0.254, 0.2794, 0.3048, 0.3302, 0.3556, 0.381, 0.4064, 0.4318, 0.4572,  &
       0.4826, 0.508, 0.5334  &
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
   spline_name = .template_5_turn_force.stopper  &
   adams_id = 5  &
   x = 0.0, 2.54E-06, 5.08E-06, 7.62E-06, 1.016E-05, 1.27E-05, 1.524E-05,  &
       1.778E-05, 2.032E-05, 2.286E-05, 2.54E-05, 2.794E-05, 3.048E-05,  &
       3.302E-05, 3.556E-05, 3.81E-05, 4.064E-05, 4.318E-05, 4.572E-05,  &
       4.826E-05, 5.08E-05, 5.334E-05, 5.588E-05, 5.842E-05, 6.096E-05,  &
       6.35E-05, 6.604E-05, 6.858E-05, 7.112E-05, 7.366E-05, 7.62E-05,  &
       7.874E-05, 8.128E-05, 8.382E-05, 8.636E-05, 8.89E-05, 9.144E-05,  &
       9.398E-05, 9.652E-05, 9.906E-05, 1.016E-04, 1.0414E-04, 1.0668E-04,  &
       1.0922E-04, 1.1176E-04, 1.143E-04, 1.1684E-04, 1.1938E-04, 1.2192E-04,  &
       1.2446E-04, 1.27E-04, 1.2954E-04, 1.3208E-04, 1.3462E-04, 1.3716E-04,  &
       1.397E-04, 1.4224E-04, 1.4478E-04, 1.4732E-04, 1.4986E-04, 1.524E-04,  &
       1.5494E-04, 1.5748E-04, 1.6002E-04, 1.6256E-04, 1.651E-04, 1.6764E-04,  &
       1.7018E-04, 1.7272E-04, 1.7526E-04, 1.778E-04, 1.8034E-04, 1.8288E-04,  &
       1.8542E-04, 1.8796E-04, 1.905E-04, 1.9304E-04, 1.9558E-04, 1.9812E-04,  &
       2.0066E-04, 2.032E-04, 2.0574E-04, 2.0828E-04, 2.1082E-04, 2.1336E-04,  &
       2.159E-04, 2.1844E-04, 2.2098E-04, 2.2352E-04, 2.2606E-04, 2.286E-04,  &
       2.3114E-04, 2.3368E-04, 2.3622E-04, 2.3876E-04, 2.413E-04, 2.4384E-04,  &
       2.4638E-04, 2.4892E-04, 2.5146E-04, 2.54E-04, 5.08E-04, 7.62E-04,  &
       1.016E-03, 1.27E-03, 1.524E-03, 1.778E-03, 2.032E-03, 2.286E-03,  &
       2.54E-03, 5.08E-03, 7.62E-03, 1.016E-02, 1.27E-02, 1.524E-02,  &
       1.778E-02, 2.032E-02, 2.286E-02, 2.54E-02, 5.08E-02, 7.62E-02, 0.1016,  &
       0.127, 0.1524, 0.1778, 0.2032, 0.2286, 0.254  &
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
   material_name = .template_5_turn_force.aluminum  &
   adams_id = 2  &
   density = 2740.0  &
   youngs_modulus = 7.1705E+10  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_5_turn_force.steel  &
   adams_id = 5  &
   density = 7801.0  &
   youngs_modulus = 2.07E+11  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_5_turn_force.steel_2  &
   adams_id = 3  &
   density = 7801.0  &
   youngs_modulus = 2.07E+11  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_5_turn_force.aluminum_2  &
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
   default_coordinate_system = .template_5_turn_force.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ground.origo  &
   adams_id = 1  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.origo  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfs_subframe_ref  &
   adams_id = 3  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 180.0d, 90.0d, 177.5464650677d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfs_subframe_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_spin_axis  &
   adams_id = 4  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 179.9999064822d, 88.9999687771d, 5.3582784306E-03d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_spin_axis  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_spin_axis  &
   adams_id = 5  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 9.351777273E-05d, 88.9999687771d, 179.9946417216d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_spin_axis  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_torque_arm_refplane  &
   adams_id = 6  &
   location = 12.5098362975, -1.6395888469, 0.5076864953  &
   orientation = 55.1145661544d, 175.2828647294d, 80.2814243968d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_torque_arm_refplane  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_torque_arm_refplane  &
   adams_id = 7  &
   location = 12.5098362975, 1.6395888469, 0.5076864953  &
   orientation = 124.8854338456d, 175.2828647294d, 99.7185756032d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_torque_arm_refplane  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_dragbrace_refplane  &
   adams_id = 8  &
   location = 12.070313934, -1.5107420843, 1.6281029812  &
   orientation = 238.6248285507d, 75.5183095506d, 100.5979151393d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_dragbrace_refplane  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_dragbrace_refplane  &
   adams_id = 9  &
   location = 12.070313934, 1.5107420843, 1.6281029812  &
   orientation = 301.3751714493d, 75.5183095506d, 79.4020848607d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_dragbrace_refplane  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_uc_sf_atch  &
   adams_id = 10  &
   location = 12.1457499909, -1.2447481722, 2.1230446312  &
   orientation = 357.5219193201d, 81.1274829118d, 15.673741043d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_uc_sf_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_uc_sf_atch  &
   adams_id = 11  &
   location = 12.1457499909, 1.2447481722, 2.1230446312  &
   orientation = 182.4780806799d, 81.1274829118d, 164.326258957d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_uc_sf_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_axial_reference  &
   adams_id = 13  &
   location = 12.2709748205, -1.5322348019, 0.1791298424  &
   orientation = 235.1145661544d, 4.7171352706d, 124.7942832431d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_axial_reference  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_axial_reference  &
   adams_id = 14  &
   location = 12.2709748205, 1.5322348019, 0.1791298424  &
   orientation = 304.8854338456d, 4.7171352706d, 55.2057167569d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_axial_reference  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_uc_bot  &
   adams_id = 15  &
   location = 12.234684072, -1.5069317388, 0.7152796436  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_uc_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_uc_bot  &
   adams_id = 16  &
   location = 12.234684072, 1.5069317388, 0.7152796436  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_uc_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_uc_top  &
   adams_id = 17  &
   location = 12.137340597, -1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_uc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_uc_top  &
   adams_id = 18  &
   location = 12.137340597, 1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_uc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_lc_top  &
   adams_id = 19  &
   location = 12.2057611337, -1.486765747, 1.1425793908  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_lc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_lc_top  &
   adams_id = 20  &
   location = 12.2057611337, 1.486765747, 1.1425793908  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_lc_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_uta_uc_atch  &
   adams_id = 21  &
   location = 12.234684072, -1.5069317388, 0.7152796436  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_uta_uc_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_uta_uc_atch  &
   adams_id = 22  &
   location = 12.234684072, 1.5069317388, 0.7152796436  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_uta_uc_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_lta_lc_atch  &
   adams_id = 23  &
   location = 12.2709748205, -1.5322348019, 0.1791298424  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_lta_lc_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_lta_lc_atch  &
   adams_id = 24  &
   location = 12.2709748205, 1.5322348019, 0.1791298424  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_lta_lc_atch  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_collar_top  &
   adams_id = 25  &
   location = 12.2161847888, -1.4940334506, 0.9885831006  &
   orientation = 55.1145661544d, 175.2828647294d, 235.2057167569d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_collar_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_collar_top  &
   adams_id = 26  &
   location = 12.2161847888, 1.4940334506, 0.9885831006  &
   orientation = 124.8854338456d, 175.2828647294d, 304.7942832431d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_collar_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_collar_bot  &
   adams_id = 27  &
   location = 12.2308845534, -1.5042825937, 0.7714127142  &
   orientation = 55.1145661544d, 175.2828647294d, 235.2057167569d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_collar_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_collar_bot  &
   adams_id = 28  &
   location = 12.2308845534, 1.5042825937, 0.7714127142  &
   orientation = 124.8854338456d, 175.2828647294d, 304.7942832431d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_collar_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_plane_ref  &
   adams_id = 29  &
   location = 11.7904549128, -1.3312381859, 1.4785418122  &
   orientation = 70.4651741872d, 87.6875364203d, 268.7516172662d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_plane_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_plane_ref  &
   adams_id = 30  &
   location = 11.7904549128, 1.3312381859, 1.4785418122  &
   orientation = 109.5348258128d, 87.6875364203d, 271.2483827338d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_plane_ref  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_plane_ref_2  &
   adams_id = 31  &
   location = 11.7904549128, -1.3312381859, 1.4785418122  &
   orientation = 160.4147950495d, 91.2473659421d, 267.6869880055d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_plane_ref_2  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_plane_ref_2  &
   adams_id = 32  &
   location = 11.7904549128, 1.3312381859, 1.4785418122  &
   orientation = 19.5852049505d, 91.2473659421d, 272.3130119945d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_plane_ref_2  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_lwract_top  &
   adams_id = 33  &
   location = 12.301784069, -1.2914705743, 1.9010842639  &
   orientation = 182.4778087702d, 7.7973026753d, 177.4990974089d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_lwract_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_lwract_top  &
   adams_id = 34  &
   location = 12.301784069, 1.2914705743, 1.9010842639  &
   orientation = 357.5221912298d, 7.7973026753d, 2.5009025911d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_lwract_top  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_upract_bot  &
   adams_id = 35  &
   location = 12.3037747523, -1.337473576, 1.5648221485  &
   orientation = 182.4778087702d, 7.7973026753d, 177.4990974089d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_upract_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_upract_bot  &
   adams_id = 36  &
   location = 12.3037747523, 1.337473576, 1.5648221485  &
   orientation = 357.5221912298d, 7.7973026753d, 2.5009025911d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_upract_bot  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_spin_axis_1  &
   adams_id = 37  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 359.9999064822d, 91.0000312229d, 179.9946417216d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_spin_axis_1  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_spin_axis_1  &
   adams_id = 38  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 180.0000935178d, 91.0000312229d, 5.3582784306E-03d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_spin_axis_1  &
   color = MAIZE  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_ldb_geompt_1  &
   adams_id = 39  &
   location = 11.8912081251, -1.3781308467, 1.1458304613  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_ldb_geompt_1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_ldb_geompt_1  &
   adams_id = 40  &
   location = 11.8912081251, 1.3781308467, 1.1458304613  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_ldb_geompt_1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_ldb_geompt_2  &
   adams_id = 41  &
   location = 11.9606643032, -1.4050660792, 1.0737874161  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_ldb_geompt_2  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_ldb_geompt_2  &
   adams_id = 42  &
   location = 11.9606643032, 1.4050660792, 1.0737874161  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_ldb_geompt_2  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_aero_ref  &
   adams_id = 43  &
   location = 12.137340597, -1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_aero_ref  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_aero_ref  &
   adams_id = 44  &
   location = 12.137340597, 1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_aero_ref  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.uel_gearaero_origin_1  &
   adams_id = 45  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.uel_gearaero_origin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.uel_gearaero_rm_1  &
   adams_id = 46  &
   location = 12.137340597, -1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.uel_gearaero_rm_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.uer_gearaero_origin_1  &
   adams_id = 47  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.uer_gearaero_origin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.uer_gearaero_rm_1  &
   adams_id = 48  &
   location = 12.137340597, 1.4390607744, 2.1534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.uer_gearaero_rm_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.lumian_ref_1  &
   adams_id = 239  &
   location = 12.2383679771, 1.5095002745, -0.5608546166  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.lumian_ref_1  &
   visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.zdt1  &
   adams_id = 461  &
   location = 5.9187250255, 1.258402253E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_5_turn_force.ground.zdt2  &
   adams_id = 462  &
   location = 5.7792875383, -8.1123966205E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_5_turn_force.ground.origo1  &
   adams_id = 287  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.origo1  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfs_uc_sf_atch_mid  &
   adams_id = 289  &
   location = 6.31444, 0.0, 1.69164  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfs_uc_sf_atch_mid  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfs_subframe_to_body_point  &
   adams_id = 290  &
   location = 6.70433, 0.0, 1.66878  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfs_subframe_to_body_point  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfl_spin_axis1  &
   adams_id = 292  &
   location = 6.229096, -0.20955, 0.308  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfl_spin_axis1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfr_spin_axis1  &
   adams_id = 293  &
   location = 6.229096, 0.20955, 0.308  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfr_spin_axis1  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfs_wheel_centers_midpoint  &
   adams_id = 294  &
   location = 6.229096, 0.0, 0.508  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfs_wheel_centers_midpoint  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfs_nlg_axle_lowpoint  &
   adams_id = 295  &
   location = 6.229096, 0.0, 0.4826  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfs_nlg_axle_lowpoint  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ground.cfs_collar_top  &
   adams_id = 296  &
   location = 6.1976, 0.0, 0.856996  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ground.cfs_collar_top  &
   color = MAIZE  &
   size_of_icons = 5.0E-02
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_5_turn_force.ground.luntai1_tire_jf_1  &
   adams_id = 240
!
floating_marker create  &
   floating_marker_name = .template_5_turn_force.ground.uel_gearaero_jfloat_1  &
   adams_id = 49
!
floating_marker create  &
   floating_marker_name = .template_5_turn_force.ground.uer_gearaero_jfloat_1  &
   adams_id = 50
!
floating_marker create  &
   floating_marker_name = .template_5_turn_force.ground.luntai2_tire_jf_1  &
   adams_id = 241
!
floating_marker create  &
   floating_marker_name = .template_5_turn_force.ground.luntai1_tire_jf_11  &
   adams_id = 298
!
floating_marker create  &
   floating_marker_name = .template_5_turn_force.ground.luntai2_tire_jf_11  &
   adams_id = 299
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_udb_spndl_atch_1  &
   location = 10.963049321, -1.0224189813, 2.1030895124
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_udb_spndl_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_udb_spndl_atch_1  &
   location = 10.963049321, 1.0224189813, 2.1030895124
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_udb_spndl_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_ib_uc_sf_atch  &
   location = 12.1541593848, -1.0504355699, 2.0926831806
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_ib_uc_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_ib_uc_sf_atch  &
   location = 12.1541593848, 1.0504355699, 2.0926831806
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_ib_uc_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_wheel_center  &
   location = 12.2709739569, -1.8115919597, 0.1742595194
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_wheel_center  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_wheel_center  &
   location = 12.2709739569, 1.8115919597, 0.1742595194
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_wheel_center  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_lc_bot  &
   location = 12.2709748205, -1.5322348019, 0.1791298424
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_lc_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_lc_bot  &
   location = 12.2709748205, 1.5322348019, 0.1791298424
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_lc_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_ob_axle  &
   location = 12.2709737181, -1.9578736763, 0.1717060828
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_ob_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_ob_axle  &
   location = 12.2709737181, 1.9578736763, 0.1717060828
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_ob_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_ib_axle  &
   location = 12.2709748205, -1.532234807, 0.1791298424
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_ib_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_ib_axle  &
   location = 12.2709748205, 1.532234807, 0.1791298424
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_ib_axle  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_uc_top  &
   location = 12.137340597, -1.4390607744, 2.1534060818
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_uc_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_uc_top  &
   location = 12.137340597, 1.4390607744, 2.1534060818
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_uc_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_uc_geompt  &
   location = 12.1670316222, -1.3594512257, 1.7617947238
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_uc_geompt  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_uc_geompt  &
   location = 12.1670316222, 1.3594512257, 1.7617947238
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_uc_geompt  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_stator_attach  &
   location = 12.2709740483, -1.7544506694, 0.175256952
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_stator_attach  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_stator_attach  &
   location = 12.2709740483, 1.7544506694, 0.175256952
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_stator_attach  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_ldb_uc_atch  &
   location = 12.54125, -1.8542, 1.21285
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_ldb_uc_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_ldb_uc_atch  &
   location = 12.54125, 1.8542, 1.21285
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_ldb_uc_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_ldb_udb_atch_1  &
   location = 11.532351205, -1.2389654784, 1.5180528618
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_ldb_udb_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_ldb_udb_atch_1  &
   location = 11.532351205, 1.2389654784, 1.5180528618
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_ldb_udb_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_lta_uta_atch  &
   location = 13.02385, -1.8796, 0.62865
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_lta_uta_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_lta_uta_atch  &
   location = 13.02385, 1.8796, 0.62865
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_lta_uta_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_lta_connect_atch_1  &
   location = 12.048547912, -1.5622090168, 0.5321183668
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_lta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_lta_connect_atch_1  &
   location = 12.048547912, 1.5622090168, 0.5321183668
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_lta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_uta_connect_atch_1  &
   location = 12.0522523496, -1.4912788564, 0.5290216242
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_uta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_uta_connect_atch_1  &
   location = 12.0522523496, 1.4912788564, 0.5290216242
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_uta_connect_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_uta_connect_atch_2  &
   location = 12.087047708, -1.4934025504, 0.5220012166
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_uta_connect_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_uta_connect_atch_2  &
   location = 12.087047708, 1.4934025504, 0.5220012166
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_uta_connect_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_lta_lc_atch_1  &
   location = 12.150137371, -1.5536660062, 0.2740663556
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_lta_lc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_lta_lc_atch_1  &
   location = 12.150137371, 1.5536660062, 0.2740663556
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_lta_lc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_lta_lc_atch_2  &
   location = 12.1525627408, -1.5072279736, 0.2720389276
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_lta_lc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_lta_lc_atch_2  &
   location = 12.1525627408, 1.5072279736, 0.2720389276
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_lta_lc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_uta_collar_atch_1  &
   location = 12.1066524694, -1.4965360468, 0.800236779
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_uta_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_uta_collar_atch_1  &
   location = 12.1066524694, 1.4965360468, 0.800236779
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_uta_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_uta_collar_atch_2  &
   location = 12.1102139304, -1.428342457, 0.797259518
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_uta_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_uta_collar_atch_2  &
   location = 12.1102139304, 1.428342457, 0.797259518
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_uta_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_collar_top  &
   location = 12.216682831, -1.4943808822, 0.9812211008
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_collar_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_collar_top  &
   location = 12.216682831, 1.4943808822, 0.9812211008
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_collar_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_collar_bot  &
   location = 12.2313550394, -1.5046108084, 0.7644576024
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_collar_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_collar_bot  &
   location = 12.2313550394, 1.5046108084, 0.7644576024
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_collar_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_upr_strt_bot  &
   location = 12.2327072846, -1.5055538596, 0.7444805024
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_upr_strt_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_upr_strt_bot  &
   location = 12.2327072846, 1.5055538596, 0.7444805024
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_upr_strt_bot  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_upr_strt_top  &
   location = 12.1478181986, -1.4463662462, 1.9986101506
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_upr_strt_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_upr_strt_top  &
   location = 12.1478181986, 1.4463662462, 1.9986101506
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_upr_strt_top  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_lwract_uc_atch_1  &
   location = 12.3053060472, -1.3728605004, 1.3061589828
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_lwract_uc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_lwract_uc_atch_1  &
   location = 12.3053060472, 1.3728605004, 1.3061589828
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_lwract_uc_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_lwract_uc_atch_2  &
   location = 12.306350165, -1.3555888052, 1.3038056982
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_lwract_uc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_lwract_uc_atch_2  &
   location = 12.306350165, 1.3555888052, 1.3038056982
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_lwract_uc_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_upract_sf_atch_1  &
   location = 12.30147781, -1.2843931894, 1.952816897
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_upract_sf_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_upract_sf_atch_1  &
   location = 12.30147781, 1.2843931894, 1.952816897
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_upract_sf_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_upract_sf_atch_2  &
   location = 12.303675418, -1.2504491628, 1.9481928778
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_upract_sf_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_upract_sf_atch_2  &
   location = 12.303675418, 1.2504491628, 1.9481928778
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_upract_sf_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_spndl_sf_atch  &
   location = 10.777681391, -0.9566499282, 2.0951467876
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_spndl_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_spndl_sf_atch  &
   location = 10.777681391, 0.9566499282, 2.0951467876
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_spndl_sf_atch  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_connect_1  &
   location = 12.045992164, -1.6111431582, 0.5342547862
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_connect_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_connect_1  &
   location = 12.045992164, 1.6111431582, 0.5342547862
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_connect_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_ldb_udb_atch_2  &
   location = 11.5117089298, -1.2969830804, 1.51939371
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_ldb_udb_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_ldb_udb_atch_2  &
   location = 11.5117089298, 1.2969830804, 1.51939371
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_ldb_udb_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_ldb_collar_atch_1  &
   location = 12.111152689, -1.4634257498, 0.9176941514
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_ldb_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_ldb_collar_atch_1  &
   location = 12.111152689, 1.4634257498, 0.9176941514
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_ldb_collar_atch_1  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_ldb_collar_atch_2  &
   location = 12.0829855622, -1.5425928508, 0.9195237896
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_ldb_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_ldb_collar_atch_2  &
   location = 12.0829855622, 1.5425928508, 0.9195237896
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_ldb_collar_atch_2  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_uplock_tab  &
   location = 11.9014828772, -1.2751123164, 1.0332048729
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_uplock_tab  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_uplock_tab  &
   location = 11.9014828772, 1.2751123164, 1.0332048729
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_uplock_tab  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hsg_1  &
   location = 6.1976, 0.2, 0.8
!
point create  &
   point_name = .template_5_turn_force.ground.hsg_2  &
   location = 5.7328083759, -0.1123599625, 0.8
!
point create  &
   point_name = .template_5_turn_force.ground.hps_db_sf_atch  &
   location = 7.48411, 0.0, 1.62306
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_db_sf_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_uc_sf_atch_l  &
   location = 6.31444, -0.34036, 1.69164
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_uc_sf_atch_l  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_uc_sf_atch_r  &
   location = 6.31444, 0.34036, 1.69164
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_uc_sf_atch_r  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_lc_bot  &
   location = 6.1976, 0.0, 0.308
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_lc_bot  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_uc_top  &
   location = 6.1976, 0.0, 1.6256
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_uc_top  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_db_uc_atch  &
   location = 6.4516, 0.0, 1.016
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_db_uc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_uta_uc_atch  &
   location = 6.3246, 0.0, 0.8382
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_uta_uc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_lta_lc_atch  &
   location = 6.2992, 0.0, 0.3334
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_lta_lc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_lta_uta_atch  &
   location = 6.6548, 0.0, 0.6112
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_lta_uta_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_uc_geompt  &
   location = 6.1976, 0.0, 1.4732
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_uc_geompt  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_uc_bot  &
   location = 6.1976, 0.0, 0.762
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_uc_bot  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_lc_top  &
   location = 6.1976, 0.0, 1.197
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_lc_top  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_origin_reference  &
   location = 0.0, 0.0, 0.0
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_origin_reference  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_lb_uc_atch  &
   location = 6.021578, 0.0, 0.79502
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_lb_uc_atch  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_wheel_center1  &
   location = 6.229096, -0.20955, 0.308
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_wheel_center1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_wheel_center1  &
   location = 6.229096, 0.20955, 0.308
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_wheel_center1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpl_ob_axle1  &
   location = 6.229096, -0.28575, 0.308
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpl_ob_axle1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hpr_ob_axle1  &
   location = 6.229096, 0.28575, 0.308
!
point attributes  &
   point_name = .template_5_turn_force.ground.hpr_ob_axle1  &
   size_of_icons = 5.0E-02
!
point create  &
   point_name = .template_5_turn_force.ground.hps_nlg_axle_lowpoint  &
   location = 6.229096, 0.0, 0.4826
!
point attributes  &
   point_name = .template_5_turn_force.ground.hps_nlg_axle_lowpoint  &
   size_of_icons = 5.0E-02
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_5_turn_force.ground  &
   size_of_icons = 5.0E-02
!
!------------------------------------- js -------------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.js  &
   adams_id = 46  &
   location = -0.92679, 0.0, 0.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.js
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.js.dadi  &
   adams_id = 494  &
   location = 0.92679, 0.0, -0.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.js.MARKER_492  &
   adams_id = 492  &
   location = 8.4109, 0.0, 1.12306  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_5_turn_force.js.MARKER_433  &
   adams_id = 433  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.js.MARKER_433  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.js.cm  &
   adams_id = 438  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.js.cm  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.js.MARKER_443  &
   adams_id = 443  &
   location = 13.064130597, 1.4390607744, 1.6534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.js.MARKER_443  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.js.MARKER_445  &
   adams_id = 445  &
   location = 13.064130597, -1.4390607744, 1.6534060818  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.js.MARKER_445  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.js.MARKER_475  &
   adams_id = 475  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 90.0d, 90.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.js.MARKER_476  &
   adams_id = 476  &
   location = 11.550194959, 0.0, 2.1282477971  &
   orientation = 90.0d, 90.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.js.MARKER_483  &
   adams_id = 483  &
   location = 7.12439, 0.0, 1.1256  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.js.MARKER_484  &
   adams_id = 484  &
   location = 7.12439, 0.0, 1.1256  &
   orientation = 0.0d, 0.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.js  &
   mass = 3.4246223935E+04  &
   center_of_mass_marker = .template_5_turn_force.js.cm  &
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
   ellipsoid_name = .template_5_turn_force.js.ELLIPSOID_156  &
   adams_id = 150  &
   center_marker = .template_5_turn_force.js.MARKER_433  &
   x_scale_factor = 0.2  &
   y_scale_factor = 0.2  &
   z_scale_factor = 0.2
!
part attributes  &
   part_name = .template_5_turn_force.js  &
   color = GREEN  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
!------------------------------------ hsg -------------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.hsg  &
   adams_id = 47  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.hsg
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.hsg.gralin_463  &
   adams_id = 463  &
   location = 6.1976, 0.2, 0.8  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_5_turn_force.hsg.cm  &
   adams_id = 473  &
   location = 5.9652041879, 4.3820018775E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 92.4616131589d
!
marker create  &
   marker_name = .template_5_turn_force.hsg.MARKER_466  &
   adams_id = 466  &
   location = 6.1976, 0.2, 0.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.hsg.MARKER_469  &
   adams_id = 469  &
   location = 5.8490062819, -3.4269971838E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_5_turn_force.hsg.MARKER_471  &
   adams_id = 471  &
   location = 5.9652041879, 4.3820018775E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.hsg.MARKER_472  &
   adams_id = 472  &
   location = 5.9652041879, 4.3820018775E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 0.0d
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.hsg  &
   mass = 6.6425302253  &
   center_of_mass_marker = .template_5_turn_force.hsg.cm  &
   ixx = 0.1743952027  &
   iyy = 0.1743952027  &
   izz = 1.6074923145E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.hsg.CYLINDER_213  &
   adams_id = 213  &
   center_marker = .template_5_turn_force.hsg.gralin_463  &
   angle_extent = 360.0  &
   length = 0.56  &
   radius = 2.2E-02  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_5_turn_force.hsg  &
   color = RED  &
   name_visibility = off
!
!----------------------------- gel_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_upper_cylinder  &
   adams_id = 4  &
   location = 12.1860123345, -1.4729962566, 1.4343428627  &
   orientation = 55.1145661544d, 175.2828647294d, 235.2057167569d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_gearaero_i_1  &
   adams_id = 69  &
   location = 0.0, 0.0, 0.2927550811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_gearaero_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.cm  &
   adams_id = 71  &
   location = -2.0756301703E-04, 6.4023904007E-03, -1.4668262126E-02  &
   orientation = 1.8568667884d, 1.160957641d, 3.8718469355E-06d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.inertia_frame  &
   adams_id = 72  &
   location = -2.0756301702E-04, 6.4023904007E-03, -1.4668262126E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.gralin_12  &
   adams_id = 73  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.gralin_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.gralin_16  &
   adams_id = 74  &
   location = -1.267958076E-02, 0.3910980589, -0.6781339507  &
   orientation = 1.8570008801d, 40.351475152d, 357.5638844642d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.gralin_16  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.gralin_20  &
   adams_id = 75  &
   location = -1.267958076E-02, 0.3910980589, -0.6781339507  &
   orientation = 1.8569053823d, 96.3249984393d, 196.3982135299d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.gralin_20  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_12  &
   adams_id = 76  &
   location = 0.0, 0.0, 0.5071310811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_spring_j_1  &
   adams_id = 78  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_spring_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_damper_j_1  &
   adams_id = 79  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_damper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_stopper_j_1  &
   adams_id = 80  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_stopper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_4  &
   adams_id = 81  &
   location = 0.0, 0.0, 0.5562289935  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_i_7  &
   adams_id = 82  &
   location = -0.1103647044, 0.1064191121, 0.1310872657  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_i_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_actuator_j_3  &
   adams_id = 83  &
   location = -6.3397903797E-03, 0.1955490295, -0.6998205159  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_actuator_j_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_267  &
   adams_id = 267  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_267  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_272  &
   adams_id = 272  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_272  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_411  &
   adams_id = 411  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_411  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_413  &
   adams_id = 413  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_413  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_415  &
   adams_id = 415  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_415  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_446  &
   adams_id = 446  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_446  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_upper_cylinder  &
   mass = 112.770857716  &
   center_of_mass_marker = .template_5_turn_force.gel_upper_cylinder.cm  &
   inertia_marker = .template_5_turn_force.gel_upper_cylinder.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_upper_cylinder.gralin_upper_cylinder  &
   adams_id = 1  &
   center_marker = .template_5_turn_force.gel_upper_cylinder.gralin_12  &
   angle_extent = 360.0  &
   length = 1.4430141621  &
   radius = 9.398E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_upper_cylinder.gralin_upper_cylinder  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_upper_cylinder.gralin_geom  &
   adams_id = 2  &
   center_marker = .template_5_turn_force.gel_upper_cylinder.gralin_16  &
   angle_extent = 360.0  &
   length = 0.4529277436  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_upper_cylinder.gralin_geom  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_upper_cylinder.gralin_geom3  &
   adams_id = 3  &
   center_marker = .template_5_turn_force.gel_upper_cylinder.gralin_20  &
   angle_extent = 360.0  &
   length = 0.3937000024  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_upper_cylinder.gralin_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_turn_force.gel_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ger_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_upper_cylinder  &
   adams_id = 5  &
   location = 12.1860123345, 1.4729962566, 1.4343428627  &
   orientation = 124.8854338456d, 175.2828647294d, 304.7942832431d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_gearaero_i_1  &
   adams_id = 84  &
   location = 0.0, 0.0, 0.2927550811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_gearaero_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.cm  &
   adams_id = 85  &
   location = -2.0756301703E-04, -6.4023904007E-03, -1.4668262126E-02  &
   orientation = 178.1431332116d, 1.160957641d, 179.9999961282d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.inertia_frame  &
   adams_id = 86  &
   location = -2.0756301702E-04, -6.4023904007E-03, -1.4668262126E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.gralin_13  &
   adams_id = 87  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.gralin_13  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.gralin_17  &
   adams_id = 88  &
   location = -1.267958076E-02, -0.3910980589, -0.6781339507  &
   orientation = 178.1429991199d, 40.351475152d, 182.4361155358d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.gralin_17  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.gralin_21  &
   adams_id = 89  &
   location = -1.267958076E-02, -0.3910980589, -0.6781339507  &
   orientation = 178.1430946177d, 96.3249984393d, 343.6017864701d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.gralin_21  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_12  &
   adams_id = 90  &
   location = 0.0, 0.0, 0.5071310811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_spring_j_1  &
   adams_id = 92  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_spring_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_damper_j_1  &
   adams_id = 93  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_damper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_stopper_j_1  &
   adams_id = 94  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_stopper_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_4  &
   adams_id = 95  &
   location = 0.0, 0.0, 0.5562289935  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_i_7  &
   adams_id = 96  &
   location = -0.1103647044, -0.1064191121, 0.1310872657  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_i_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_actuator_j_3  &
   adams_id = 97  &
   location = -6.3397903797E-03, -0.1955490295, -0.6998205159  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_actuator_j_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_269  &
   adams_id = 269  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_269  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_278  &
   adams_id = 278  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_278  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_417  &
   adams_id = 417  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_417  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_419  &
   adams_id = 419  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_419  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_421  &
   adams_id = 421  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_421  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_444  &
   adams_id = 444  &
   location = 0.0, 0.0, -0.7215070811  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_444  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_upper_cylinder  &
   mass = 112.770857716  &
   center_of_mass_marker = .template_5_turn_force.ger_upper_cylinder.cm  &
   inertia_marker = .template_5_turn_force.ger_upper_cylinder.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_upper_cylinder.gralin_upper_cylinder  &
   adams_id = 4  &
   center_marker = .template_5_turn_force.ger_upper_cylinder.gralin_13  &
   angle_extent = 360.0  &
   length = 1.4430141621  &
   radius = 9.398E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_upper_cylinder.gralin_upper_cylinder  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_upper_cylinder.gralin_geom  &
   adams_id = 5  &
   center_marker = .template_5_turn_force.ger_upper_cylinder.gralin_17  &
   angle_extent = 360.0  &
   length = 0.4529277436  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_upper_cylinder.gralin_geom  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_upper_cylinder.gralin_geom3  &
   adams_id = 6  &
   center_marker = .template_5_turn_force.ger_upper_cylinder.gralin_21  &
   angle_extent = 360.0  &
   length = 0.3937000024  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_upper_cylinder.gralin_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_turn_force.ger_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- gel_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_lower_cylinder  &
   adams_id = 6  &
   location = 12.2383679771, -1.5095002745, 0.6608546166  &
   orientation = 55.1145661544d, 175.2828647294d, 235.2057167569d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_495  &
   adams_id = 495  &
   location = 3.2976999835E-04, -0.2788194422, 0.5013550985  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.cm  &
   adams_id = 99  &
   location = 1.6535536877E-05, -1.3980732745E-02, 3.2717040657E-02  &
   orientation = 6.7765835809E-02d, 4.4745452767d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.inertia_frame  &
   adams_id = 100  &
   location = 1.653553688E-05, -1.3980732745E-02, 3.2717040657E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.gralin_14  &
   adams_id = 101  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.gralin_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.gralin_22  &
   adams_id = 102  &
   location = 0.0, -5.0742924723E-09, 0.4833620002  &
   orientation = 6.7765837027E-02d, 86.3072194251d, 358.9479605068d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.gralin_22  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.jxl_joint_j_11  &
   adams_id = 103  &
   location = 0.114150217, -2.6246375424E-02, 0.3816035459  &
   orientation = 182.811221391d, 89.9999933852d, 90.0001347091d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.jxl_joint_j_11  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.jxl_joint_i_12  &
   adams_id = 104  &
   location = 0.0, 0.0, -0.268986  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.jxl_joint_i_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.coomarker_1  &
   adams_id = 105  &
   location = 3.2976999835E-04, -0.2788194422, 0.5013550985  &
   orientation = 180.0677659208d, 93.6935934189d, 183.8814472486d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.coomarker_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.uel_spring_i_1  &
   adams_id = 106  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.uel_spring_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.uel_damper_i_1  &
   adams_id = 107  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.uel_damper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.uel_stopper_i_1  &
   adams_id = 108  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.uel_stopper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_497  &
   adams_id = 497  &
   location = 3.2976995844E-04, -0.2788194421, 0.5013550985  &
   orientation = 180.0d, 92.6958536659d, 3.872313078d
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_266  &
   adams_id = 266  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_266  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_273  &
   adams_id = 273  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_273  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_412  &
   adams_id = 412  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_412  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_414  &
   adams_id = 414  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_414  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_416  &
   adams_id = 416  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 304.7942832431d, 175.2828647294d, 124.8854338456d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_416  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_lower_cylinder  &
   mass = 217.3555691677  &
   center_of_mass_marker = .template_5_turn_force.gel_lower_cylinder.cm  &
   inertia_marker = .template_5_turn_force.gel_lower_cylinder.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_lower_cylinder.gralin_lower_cylinder  &
   adams_id = 7  &
   center_marker = .template_5_turn_force.gel_lower_cylinder.gralin_14  &
   angle_extent = 360.0  &
   length = 0.966724  &
   radius = 6.35E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_lower_cylinder.gralin_lower_cylinder  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_lower_cylinder.gralin_geom  &
   adams_id = 8  &
   center_marker = .template_5_turn_force.gel_lower_cylinder.gralin_22  &
   angle_extent = 360.0  &
   length = 0.425703605  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_lower_cylinder.gralin_geom  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_5_turn_force.gel_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ger_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_lower_cylinder  &
   adams_id = 7  &
   location = 12.2383679771, 1.5095002745, 0.6608546166  &
   orientation = 124.8854338456d, 175.2828647294d, 304.7942832431d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.cm  &
   adams_id = 109  &
   location = 1.6535536877E-05, 1.3980732745E-02, 3.2717040657E-02  &
   orientation = 179.9322341642d, 4.4745452767d, 180.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.inertia_frame  &
   adams_id = 110  &
   location = 1.653553688E-05, 1.3980732745E-02, 3.2717040657E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.gralin_15  &
   adams_id = 111  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.gralin_15  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.gralin_23  &
   adams_id = 112  &
   location = 0.0, 5.0742924688E-09, 0.4833620002  &
   orientation = 179.932234163d, 86.3072194251d, 181.0520394932d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.gralin_23  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.jxr_joint_j_11  &
   adams_id = 113  &
   location = 0.114150217, 2.6246375424E-02, 0.3816035459  &
   orientation = 357.188778609d, 89.9999933852d, 89.9998652909d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.jxr_joint_j_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.jxr_joint_i_12  &
   adams_id = 114  &
   location = 0.0, 0.0, -0.268986  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.jxr_joint_i_12  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.coomarker_2  &
   adams_id = 115  &
   location = 3.2976999835E-04, 0.2788194422, 0.5013550985  &
   orientation = 359.9322340792d, 93.6935934189d, 356.1185527514d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.coomarker_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.uer_spring_i_1  &
   adams_id = 116  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.uer_spring_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.uer_damper_i_1  &
   adams_id = 117  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.uer_damper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.uer_stopper_i_1  &
   adams_id = 118  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.uer_stopper_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_498  &
   adams_id = 498  &
   location = 3.2976999835E-04, 0.2788194422, 0.5013550985  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_500  &
   adams_id = 500  &
   location = 3.2976995844E-04, 0.2788194421, 0.5013550985  &
   orientation = 180.0d, 87.3041463341d, 3.872313078d
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_268  &
   adams_id = 268  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_268  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_279  &
   adams_id = 279  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_279  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_418  &
   adams_id = 418  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_418  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_420  &
   adams_id = 420  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_420  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_422  &
   adams_id = 422  &
   location = 0.0, 0.0, -0.483362  &
   orientation = 235.2057167569d, 175.2828647294d, 55.1145661544d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_422  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_lower_cylinder  &
   mass = 217.3555691677  &
   center_of_mass_marker = .template_5_turn_force.ger_lower_cylinder.cm  &
   inertia_marker = .template_5_turn_force.ger_lower_cylinder.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_lower_cylinder.gralin_lower_cylinder  &
   adams_id = 9  &
   center_marker = .template_5_turn_force.ger_lower_cylinder.gralin_15  &
   angle_extent = 360.0  &
   length = 0.966724  &
   radius = 6.35E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_lower_cylinder.gralin_lower_cylinder  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_lower_cylinder.gralin_geom  &
   adams_id = 10  &
   center_marker = .template_5_turn_force.ger_lower_cylinder.gralin_23  &
   angle_extent = 360.0  &
   length = 0.425703605  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_lower_cylinder.gralin_geom  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_5_turn_force.ger_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_upper_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_upper_dragbrace  &
   adams_id = 8  &
   location = 11.247700263, -1.1306922298, 1.8105711871  &
   orientation = 69.1745865818d, 133.845797857d, 255.2385761183d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_upper_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.cm  &
   adams_id = 119  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.inertia_frame  &
   adams_id = 120  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.gralin_24  &
   adams_id = 121  &
   location = 0.0, 0.0, -0.4222750594  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.gralin_24  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.jxl_joint_j_14  &
   adams_id = 122  &
   location = 0.0, 0.0, 0.4222750594  &
   orientation = 193.0027634258d, 90.0301580129d, 133.8272261428d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.jxl_joint_j_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.jxl_joint_i_5  &
   adams_id = 123  &
   location = 0.0, 0.0, -0.4222750594  &
   orientation = 12.9738149065d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.jxl_joint_i_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.uel_actuator_i_3  &
   adams_id = 124  &
   location = 0.0, 0.0, 0.4222750594  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.uel_actuator_i_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_upper_dragbrace  &
   mass = 6.7539180723  &
   center_of_mass_marker = .template_5_turn_force.gel_upper_dragbrace.cm  &
   inertia_marker = .template_5_turn_force.gel_upper_dragbrace.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_upper_dragbrace.gralin_upper_dragbrace  &
   adams_id = 11  &
   center_marker = .template_5_turn_force.gel_upper_dragbrace.gralin_24  &
   angle_extent = 360.0  &
   length = 0.8445501187  &
   radius = 3.048E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_upper_dragbrace.gralin_upper_dragbrace  &
   color = RED
!
part attributes  &
   part_name = .template_5_turn_force.gel_upper_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_upper_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_upper_dragbrace  &
   adams_id = 9  &
   location = 11.247700263, 1.1306922298, 1.8105711871  &
   orientation = 110.8254134182d, 133.845797857d, 284.7614238817d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_upper_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.cm  &
   adams_id = 125  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.inertia_frame  &
   adams_id = 126  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.gralin_25  &
   adams_id = 127  &
   location = 0.0, 0.0, -0.4222750594  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.gralin_25  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.jxr_joint_j_14  &
   adams_id = 128  &
   location = 0.0, 0.0, 0.4222750594  &
   orientation = 346.9972365742d, 90.0301580129d, 46.1727738572d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.jxr_joint_j_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.jxr_joint_i_5  &
   adams_id = 129  &
   location = 0.0, 0.0, -0.4222750594  &
   orientation = 347.0261850935d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.jxr_joint_i_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.uer_actuator_i_3  &
   adams_id = 130  &
   location = 0.0, 0.0, 0.4222750594  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.uer_actuator_i_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_upper_dragbrace  &
   mass = 6.7539180723  &
   center_of_mass_marker = .template_5_turn_force.ger_upper_dragbrace.cm  &
   inertia_marker = .template_5_turn_force.ger_upper_dragbrace.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_upper_dragbrace.gralin_upper_dragbrace  &
   adams_id = 12  &
   center_marker = .template_5_turn_force.ger_upper_dragbrace.gralin_25  &
   angle_extent = 360.0  &
   length = 0.8445501187  &
   radius = 3.048E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_upper_dragbrace.gralin_upper_dragbrace  &
   color = RED
!
part attributes  &
   part_name = .template_5_turn_force.ger_upper_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_lower_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_lower_dragbrace  &
   adams_id = 10  &
   location = 11.821751947, -1.3511956141, 1.2178735066  &
   orientation = 68.8036164538d, 134.040966185d, 254.9123665662d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_lower_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.cm  &
   adams_id = 131  &
   location = 3.9348735476E-03, 6.8056064573E-03, 2.4978613416E-02  &
   orientation = 149.9643072355d, 1.0992652329d, 180.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.inertia_frame  &
   adams_id = 132  &
   location = 3.9348735476E-03, 6.8056064573E-03, 2.4978613416E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.gralin_26  &
   adams_id = 133  &
   location = 0.0, 0.0, -0.4318055559  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.gralin_26  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.jxl_joint_i_14  &
   adams_id = 134  &
   location = 0.0, 0.0, -0.4318055559  &
   orientation = 193.0709676552d, 90.2906925253d, 133.6233654172d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.jxl_joint_i_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.jxl_joint_i_10  &
   adams_id = 135  &
   location = 0.0, 0.0, 0.4318055559  &
   orientation = 193.0709676552d, 90.2906925253d, 133.6233654172d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.jxl_joint_i_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_1  &
   adams_id = 136  &
   location = 7.0772384942E-02, 0.1224052041, 0.1620383572  &
   orientation = 239.9643072355d, 90.0d, 337.5559025594d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_2  &
   adams_id = 137  &
   location = 0.0, 0.0, 0.1036333334  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_3  &
   adams_id = 138  &
   location = 0.0, 0.0, 0.2072666668  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_lower_dragbrace  &
   mass = 5.6992574801  &
   center_of_mass_marker = .template_5_turn_force.gel_lower_dragbrace.cm  &
   inertia_marker = .template_5_turn_force.gel_lower_dragbrace.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_lower_dragbrace.gralin_lower_dragbrace  &
   adams_id = 13  &
   center_marker = .template_5_turn_force.gel_lower_dragbrace.gralin_26  &
   angle_extent = 360.0  &
   length = 0.8636111118  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_lower_dragbrace.gralin_lower_dragbrace  &
   color = PEACH
!
geometry create shape plate  &
   plate_name = .template_5_turn_force.gel_lower_dragbrace.graarm_uplock_tab  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_1,  &
                 .template_5_turn_force.gel_lower_dragbrace.graarm_2,  &
                 .template_5_turn_force.gel_lower_dragbrace.graarm_3  &
   width = 2.54E-02  &
   radius = 1.27E-02
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_lower_dragbrace.graarm_uplock_tab  &
   color = PEACH
!
part attributes  &
   part_name = .template_5_turn_force.gel_lower_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_lower_dragbrace -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_lower_dragbrace  &
   adams_id = 11  &
   location = 11.821751947, 1.3511956141, 1.2178735066  &
   orientation = 111.1963835462d, 134.040966185d, 285.0876334338d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_lower_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.cm  &
   adams_id = 139  &
   location = 3.9348735476E-03, -6.8056064573E-03, 2.4978613416E-02  &
   orientation = 30.0356927645d, 1.0992652329d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.inertia_frame  &
   adams_id = 140  &
   location = 3.9348735476E-03, -6.8056064573E-03, 2.4978613416E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.gralin_27  &
   adams_id = 141  &
   location = 0.0, 0.0, -0.4318055559  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.gralin_27  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.jxr_joint_i_14  &
   adams_id = 142  &
   location = 0.0, 0.0, -0.4318055559  &
   orientation = 346.9290323448d, 90.2906925253d, 46.3766345828d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.jxr_joint_i_14  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.jxr_joint_i_10  &
   adams_id = 143  &
   location = 0.0, 0.0, 0.4318055559  &
   orientation = 346.9290323448d, 90.2906925253d, 46.3766345828d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.jxr_joint_i_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_4  &
   adams_id = 144  &
   location = 7.0772384942E-02, -0.1224052041, 0.1620383572  &
   orientation = 120.0356927645d, 90.0d, 337.5559025594d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_5  &
   adams_id = 145  &
   location = 0.0, 0.0, 0.1036333334  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_6  &
   adams_id = 146  &
   location = 0.0, 0.0, 0.2072666668  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_6  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_lower_dragbrace  &
   mass = 5.6992574801  &
   center_of_mass_marker = .template_5_turn_force.ger_lower_dragbrace.cm  &
   inertia_marker = .template_5_turn_force.ger_lower_dragbrace.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_lower_dragbrace.gralin_lower_dragbrace  &
   adams_id = 14  &
   center_marker = .template_5_turn_force.ger_lower_dragbrace.gralin_27  &
   angle_extent = 360.0  &
   length = 0.8636111118  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_lower_dragbrace.gralin_lower_dragbrace  &
   color = PEACH
!
geometry create shape plate  &
   plate_name = .template_5_turn_force.ger_lower_dragbrace.graarm_uplock_tab  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_4,  &
                 .template_5_turn_force.ger_lower_dragbrace.graarm_5,  &
                 .template_5_turn_force.ger_lower_dragbrace.graarm_6  &
   width = 2.54E-02  &
   radius = 1.27E-02
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_lower_dragbrace.graarm_uplock_tab  &
   color = PEACH
!
part attributes  &
   part_name = .template_5_turn_force.ger_lower_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_upper_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_upper_torquearm  &
   adams_id = 12  &
   location = 12.0794524095, -1.4939074516, 0.6646292016  &
   orientation = 264.4801161257d, 168.6067018386d, 84.5882371559d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_upper_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.cm  &
   adams_id = 147  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.inertia_frame  &
   adams_id = 148  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.gralin_11  &
   adams_id = 149  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.gralin_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.jxl_joint_i_2  &
   adams_id = 150  &
   location = 0.0, 0.0, 0.1383335383  &
   orientation = 273.4244432527d, 89.9999731825d, 177.0527623566d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.jxl_joint_i_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.jxl_joint_i_3  &
   adams_id = 151  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 183.4245252295d, 87.0529836943d, 74.5991863345d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.jxl_joint_i_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_upper_torquearm  &
   mass = 1.5364744752  &
   center_of_mass_marker = .template_5_turn_force.gel_upper_torquearm.cm  &
   inertia_marker = .template_5_turn_force.gel_upper_torquearm.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_upper_torquearm.gralin_upper_torquearm  &
   adams_id = 15  &
   center_marker = .template_5_turn_force.gel_upper_torquearm.gralin_11  &
   angle_extent = 360.0  &
   length = 0.2766670766  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_upper_torquearm.gralin_upper_torquearm  &
   color = GREEN
!
part attributes  &
   part_name = .template_5_turn_force.gel_upper_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_upper_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_upper_torquearm  &
   adams_id = 13  &
   location = 12.0794524095, 1.4939074516, 0.6646292016  &
   orientation = 275.5198838743d, 168.6067018386d, 95.4117628441d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_upper_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.cm  &
   adams_id = 152  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.inertia_frame  &
   adams_id = 153  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.gralin_28  &
   adams_id = 154  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.gralin_28  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.jxr_joint_i_2  &
   adams_id = 155  &
   location = 0.0, 0.0, 0.1383335383  &
   orientation = 266.5755567473d, 89.9999731825d, 2.9472376434d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.jxr_joint_i_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.jxr_joint_i_3  &
   adams_id = 156  &
   location = 0.0, 0.0, -0.1383335383  &
   orientation = 356.5754747705d, 87.0529836943d, 105.4008136655d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.jxr_joint_i_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_upper_torquearm  &
   mass = 1.5364744752  &
   center_of_mass_marker = .template_5_turn_force.ger_upper_torquearm.cm  &
   inertia_marker = .template_5_turn_force.ger_upper_torquearm.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_upper_torquearm.gralin_upper_torquearm  &
   adams_id = 16  &
   center_marker = .template_5_turn_force.ger_upper_torquearm.gralin_28  &
   angle_extent = 360.0  &
   length = 0.2766670766  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_upper_torquearm.gralin_upper_torquearm  &
   color = GREEN
!
part attributes  &
   part_name = .template_5_turn_force.ger_upper_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- gel_lower_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_lower_torquearm  &
   adams_id = 14  &
   location = 12.0993426415, -1.5579375115, 0.4030923612  &
   orientation = 274.806891489d, 21.5573785759d, 85.5279353352d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_lower_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.cm  &
   adams_id = 157  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.inertia_frame  &
   adams_id = 158  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.gralin_29  &
   adams_id = 159  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.gralin_29  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.jxl_joint_i_11  &
   adams_id = 160  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 178.1282947989d, 95.1813481522d, 287.4366988554d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.jxl_joint_i_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.jxl_joint_i_1  &
   adams_id = 161  &
   location = 0.0, 0.0, 0.1387301713  &
   orientation = 178.1282565411d, 95.1813639555d, 331.2687567728d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.jxl_joint_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_lower_torquearm  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.gel_lower_torquearm.cm  &
   inertia_marker = .template_5_turn_force.gel_lower_torquearm.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_lower_torquearm.gralin_lower_torquearm  &
   adams_id = 17  &
   center_marker = .template_5_turn_force.gel_lower_torquearm.gralin_29  &
   angle_extent = 360.0  &
   length = 0.2774603426  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_lower_torquearm.gralin_lower_torquearm  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_5_turn_force.gel_lower_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ger_lower_torquearm -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_lower_torquearm  &
   adams_id = 15  &
   location = 12.0993426415, 1.5579375115, 0.4030923612  &
   orientation = 265.193108511d, 21.5573785759d, 94.4720646648d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_lower_torquearm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.cm  &
   adams_id = 162  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.inertia_frame  &
   adams_id = 163  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.gralin_30  &
   adams_id = 164  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.gralin_30  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.jxr_joint_i_11  &
   adams_id = 165  &
   location = 0.0, 0.0, -0.1387301713  &
   orientation = 1.8717052011d, 95.1813481522d, 252.5633011446d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.jxr_joint_i_11  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.jxr_joint_i_1  &
   adams_id = 166  &
   location = 0.0, 0.0, 0.1387301713  &
   orientation = 1.8717434589d, 95.1813639555d, 208.7312432272d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.jxr_joint_i_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_lower_torquearm  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.ger_lower_torquearm.cm  &
   inertia_marker = .template_5_turn_force.ger_lower_torquearm.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_lower_torquearm.gralin_lower_torquearm  &
   adams_id = 18  &
   center_marker = .template_5_turn_force.ger_lower_torquearm.gralin_30  &
   angle_extent = 360.0  &
   length = 0.2774603426  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_lower_torquearm.gralin_lower_torquearm  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_5_turn_force.ger_lower_torquearm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- gel_connector --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_connector  &
   adams_id = 17  &
   location = 12.0491222568, -1.5512110073, 0.5316382052  &
   orientation = 177.0103140237d, 92.4964937717d, 309.8285622575d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_connector
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_connector.cm  &
   adams_id = 169  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_connector.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_connector.inertia_frame  &
   adams_id = 170  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_connector.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_connector.gralin_3  &
   adams_id = 171  &
   location = 0.0, 0.0, -6.0070847244E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_connector.gralin_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_connector.jxl_joint_j_1  &
   adams_id = 172  &
   location = -3.2030730841E-08, -3.9921405011E-08, -1.1023458626E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_connector.jxl_joint_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_connector.jxl_joint_j_2  &
   adams_id = 173  &
   location = 0.0, 0.0, 6.0070847244E-02  &
   orientation = 331.5687748605d, 89.9998761701d, 89.9997712794d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_connector.jxl_joint_j_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_connector  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.gel_connector.cm  &
   inertia_marker = .template_5_turn_force.gel_connector.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_connector.gralin_connector  &
   adams_id = 19  &
   center_marker = .template_5_turn_force.gel_connector.gralin_3  &
   angle_extent = 360.0  &
   length = 0.1201416945  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_connector.gralin_connector  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_turn_force.gel_connector  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- ger_connector --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_connector  &
   adams_id = 18  &
   location = 12.0491222568, 1.5512110073, 0.5316382052  &
   orientation = 2.9896859763d, 92.4964937717d, 230.1714377425d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_connector
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_connector.cm  &
   adams_id = 174  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_connector.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_connector.inertia_frame  &
   adams_id = 175  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_connector.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_connector.gralin_4  &
   adams_id = 176  &
   location = 0.0, 0.0, -6.0070847244E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_connector.gralin_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_connector.jxr_joint_j_1  &
   adams_id = 177  &
   location = -3.2030730842E-08, 3.9921405013E-08, -1.1023458626E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_connector.jxr_joint_j_1  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_connector.jxr_joint_j_2  &
   adams_id = 178  &
   location = 0.0, 0.0, 6.0070847244E-02  &
   orientation = 208.4312251395d, 89.9998761701d, 90.0002287206d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_connector.jxr_joint_j_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_connector  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.ger_connector.cm  &
   inertia_marker = .template_5_turn_force.ger_connector.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_connector.gralin_connector  &
   adams_id = 20  &
   center_marker = .template_5_turn_force.ger_connector.gralin_4  &
   angle_extent = 360.0  &
   length = 0.1201416945  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_connector.gralin_connector  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_turn_force.ger_connector  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- gel_uc_collar --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_uc_collar  &
   adams_id = 19  &
   location = 12.2235346711, -1.4991580222, 0.8799979074  &
   orientation = 55.1145661544d, 175.2828647294d, 235.2057167569d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_uc_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_uc_collar.cm  &
   adams_id = 179  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_uc_collar.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_uc_collar.inertia_frame  &
   adams_id = 180  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_uc_collar.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_uc_collar.gralin_5  &
   adams_id = 181  &
   location = 0.0, 0.0, -0.1089542389  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_uc_collar.gralin_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_j_3  &
   adams_id = 182  &
   location = 0.1220018852, 5.9907462808E-03, 7.1482951795E-02  &
   orientation = 182.811221391d, 89.9999933852d, 90.0001347091d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_j_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_i_4  &
   adams_id = 183  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_i_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_j_10  &
   adams_id = 184  &
   location = 0.1095796704, 3.3566796849E-02, -4.6830310723E-02  &
   orientation = 199.444502672d, 90.0d, 92.2365720495d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_j_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_uc_collar  &
   mass = 30.2539444008  &
   center_of_mass_marker = .template_5_turn_force.gel_uc_collar.cm  &
   inertia_marker = .template_5_turn_force.gel_uc_collar.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_uc_collar.gralin_uc_collar  &
   adams_id = 21  &
   center_marker = .template_5_turn_force.gel_uc_collar.gralin_5  &
   angle_extent = 360.0  &
   length = 0.2179084778  &
   radius = 0.127  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_uc_collar.gralin_uc_collar  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_turn_force.gel_uc_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------- ger_uc_collar --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_uc_collar  &
   adams_id = 20  &
   location = 12.2235346711, 1.4991580222, 0.8799979074  &
   orientation = 124.8854338456d, 175.2828647294d, 304.7942832431d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_uc_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_uc_collar.cm  &
   adams_id = 185  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_uc_collar.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_uc_collar.inertia_frame  &
   adams_id = 186  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_uc_collar.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_uc_collar.gralin_6  &
   adams_id = 187  &
   location = 0.0, 0.0, -0.1089542389  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_uc_collar.gralin_6  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_j_3  &
   adams_id = 188  &
   location = 0.1220018852, -5.9907462808E-03, 7.1482951795E-02  &
   orientation = 357.188778609d, 89.9999933852d, 89.9998652909d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_j_3  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_i_4  &
   adams_id = 189  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_i_4  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_j_10  &
   adams_id = 190  &
   location = 0.1095796704, -3.3566796849E-02, -4.6830310723E-02  &
   orientation = 340.555497328d, 90.0d, 87.7634279505d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_j_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_uc_collar  &
   mass = 30.2539444008  &
   center_of_mass_marker = .template_5_turn_force.ger_uc_collar.cm  &
   inertia_marker = .template_5_turn_force.ger_uc_collar.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_uc_collar.gralin_uc_collar  &
   adams_id = 22  &
   center_marker = .template_5_turn_force.ger_uc_collar.gralin_6  &
   angle_extent = 360.0  &
   length = 0.2179084778  &
   radius = 0.127  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_uc_collar.gralin_uc_collar  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_turn_force.ger_uc_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!-------------------------------- gel_spindle ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_spindle  &
   adams_id = 21  &
   location = 10.870365356, -0.9895344548, 2.09911815  &
   orientation = 70.4651745203d, 87.687537877d, 270.820189184d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_spindle
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_spindle.cm  &
   adams_id = 191  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_spindle.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_spindle.inertia_frame  &
   adams_id = 192  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_spindle.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_spindle.gralin_7  &
   adams_id = 193  &
   location = 0.0, 0.0, -9.8425002791E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_spindle.gralin_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_spindle.jxl_joint_j_5  &
   adams_id = 194  &
   location = 0.0, 0.0, 9.8425002791E-02  &
   orientation = 357.8896246905d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_spindle.jxl_joint_j_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_spindle  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.gel_spindle.cm  &
   inertia_marker = .template_5_turn_force.gel_spindle.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_spindle.gralin_spindle  &
   adams_id = 23  &
   center_marker = .template_5_turn_force.gel_spindle.gralin_7  &
   angle_extent = 360.0  &
   length = 0.1968500056  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_spindle.gralin_spindle  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_turn_force.gel_spindle  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!-------------------------------- ger_spindle ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_spindle  &
   adams_id = 22  &
   location = 10.870365356, 0.9895344548, 2.09911815  &
   orientation = 109.5348254797d, 87.687537877d, 269.179810816d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_spindle
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_spindle.cm  &
   adams_id = 196  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_spindle.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_spindle.inertia_frame  &
   adams_id = 197  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_spindle.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_spindle.gralin_8  &
   adams_id = 198  &
   location = 0.0, 0.0, -9.8425002791E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_spindle.gralin_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_spindle.jxr_joint_j_5  &
   adams_id = 199  &
   location = 0.0, 0.0, 9.8425002791E-02  &
   orientation = 2.1103753095d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_spindle.jxr_joint_j_5  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_spindle  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.ger_spindle.cm  &
   inertia_marker = .template_5_turn_force.ger_spindle.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_spindle.gralin_spindle  &
   adams_id = 24  &
   center_marker = .template_5_turn_force.ger_spindle.gralin_8  &
   angle_extent = 360.0  &
   length = 0.1968500056  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_spindle.gralin_spindle  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_turn_force.ger_spindle  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- gel_lwract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_lwract  &
   adams_id = 23  &
   location = 12.3035450581, -1.3321655373, 1.6036216233  &
   orientation = 182.4778087702d, 7.7973026753d, 177.4990974089d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_lwract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_lwract.cm  &
   adams_id = 201  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lwract.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lwract.inertia_frame  &
   adams_id = 202  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lwract.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lwract.gralin_9  &
   adams_id = 203  &
   location = 0.0, 0.0, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lwract.gralin_9  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lwract.jxl_joint_j_7  &
   adams_id = 204  &
   location = 0.0, 0.0, -0.3002385778  &
   orientation = 2.5009025911d, 7.7973026753d, 357.5221912298d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lwract.jxl_joint_j_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lwract.jxl_joint_i_8  &
   adams_id = 205  &
   location = 0.0, 0.0, 0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lwract.jxl_joint_i_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lwract.uel_stopper_i_2  &
   adams_id = 206  &
   location = 0.0, 0.0, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lwract.uel_stopper_i_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lwract.uel_actuator_j_1  &
   adams_id = 207  &
   location = 0.0, 0.0, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lwract.uel_actuator_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_lwract.uel_actuator_i_2  &
   adams_id = 208  &
   location = 0.0, 0.0, 0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_lwract.uel_actuator_i_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_lwract  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.gel_lwract.cm  &
   inertia_marker = .template_5_turn_force.gel_lwract.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_lwract.gralin_lwract  &
   adams_id = 25  &
   center_marker = .template_5_turn_force.gel_lwract.gralin_9  &
   angle_extent = 360.0  &
   length = 0.6004771556  &
   radius = 7.62E-03  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_lwract.gralin_lwract  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_turn_force.gel_lwract  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- ger_lwract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_lwract  &
   adams_id = 24  &
   location = 12.3035450581, 1.3321655373, 1.6036216233  &
   orientation = 357.5221912298d, 7.7973026753d, 2.5009025911d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_lwract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_lwract.cm  &
   adams_id = 209  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lwract.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lwract.inertia_frame  &
   adams_id = 210  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lwract.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lwract.gralin_10  &
   adams_id = 211  &
   location = 0.0, 0.0, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lwract.gralin_10  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lwract.jxr_joint_j_7  &
   adams_id = 212  &
   location = 0.0, 0.0, -0.3002385778  &
   orientation = 177.4990974089d, 7.7973026753d, 182.4778087702d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lwract.jxr_joint_j_7  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lwract.jxr_joint_i_8  &
   adams_id = 213  &
   location = 0.0, 0.0, 0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lwract.jxr_joint_i_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lwract.uer_stopper_i_2  &
   adams_id = 214  &
   location = 0.0, 0.0, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lwract.uer_stopper_i_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lwract.uer_actuator_i_2  &
   adams_id = 215  &
   location = 0.0, 0.0, 0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lwract.uer_actuator_i_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_lwract.uer_actuator_j_1  &
   adams_id = 216  &
   location = 0.0, 0.0, -0.3002385778  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_lwract.uer_actuator_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_lwract  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.ger_lwract.cm  &
   inertia_marker = .template_5_turn_force.ger_lwract.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_lwract.gralin_lwract  &
   adams_id = 26  &
   center_marker = .template_5_turn_force.ger_lwract.gralin_10  &
   angle_extent = 360.0  &
   length = 0.6004771556  &
   radius = 7.62E-03  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_lwract.gralin_lwract  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_turn_force.ger_lwract  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- gel_upract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.gel_upract  &
   adams_id = 25  &
   location = 12.3026262812, -1.3109333827, 1.7588195227  &
   orientation = 182.4778087702d, 7.7973026753d, 177.4990974089d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.gel_upract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.gel_upract.uel_actuator_i_1  &
   adams_id = 217  &
   location = 0.0, 0.0, 0.1958077681  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upract.uel_actuator_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upract.cm  &
   adams_id = 218  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upract.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upract.inertia_frame  &
   adams_id = 219  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upract.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upract.gralin_18  &
   adams_id = 220  &
   location = 0.0, 0.0, -0.1958077681  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upract.gralin_18  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upract.jxl_joint_j_8  &
   adams_id = 221  &
   location = 0.0, 0.0, 0.1435923633  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upract.jxl_joint_j_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upract.uel_stopper_j_2  &
   adams_id = 223  &
   location = 0.0, 0.0, 0.1958077681  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upract.uel_stopper_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.gel_upract.uel_actuator_j_2  &
   adams_id = 224  &
   location = 0.0, 0.0, 0.1435923633  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.gel_upract.uel_actuator_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.gel_upract  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.gel_upract.cm  &
   inertia_marker = .template_5_turn_force.gel_upract.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.gel_upract.gralin_upract  &
   adams_id = 27  &
   center_marker = .template_5_turn_force.gel_upract.gralin_18  &
   angle_extent = 360.0  &
   length = 0.3916155363  &
   radius = 1.778E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.gel_upract.gralin_upract  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_turn_force.gel_upract  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- ger_upract ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ger_upract  &
   adams_id = 26  &
   location = 12.3026262812, 1.3109333827, 1.7588195227  &
   orientation = 357.5221912298d, 7.7973026753d, 2.5009025911d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ger_upract
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ger_upract.uer_actuator_i_1  &
   adams_id = 225  &
   location = 0.0, 0.0, 0.1958077681  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upract.uer_actuator_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upract.cm  &
   adams_id = 226  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upract.cm  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upract.inertia_frame  &
   adams_id = 227  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upract.inertia_frame  &
   visibility = on  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upract.gralin_19  &
   adams_id = 228  &
   location = 0.0, 0.0, -0.1958077681  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upract.gralin_19  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upract.jxr_joint_j_8  &
   adams_id = 229  &
   location = 0.0, 0.0, 0.1435923633  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upract.jxr_joint_j_8  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upract.uer_stopper_j_2  &
   adams_id = 231  &
   location = 0.0, 0.0, 0.1958077681  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upract.uer_stopper_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ger_upract.uer_actuator_j_2  &
   adams_id = 232  &
   location = 0.0, 0.0, 0.1435923633  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ger_upract.uer_actuator_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ger_upract  &
   mass = 0.45359237  &
   center_of_mass_marker = .template_5_turn_force.ger_upract.cm  &
   inertia_marker = .template_5_turn_force.ger_upract.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ger_upract.gralin_upract  &
   adams_id = 28  &
   center_marker = .template_5_turn_force.ger_upract.gralin_19  &
   angle_extent = 360.0  &
   length = 0.3916155363  &
   radius = 1.778E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ger_upract.gralin_upract  &
   color = YELLOW
!
part attributes  &
   part_name = .template_5_turn_force.ger_upract  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!------------------------------------ zdt -------------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.zdt  &
   adams_id = 48  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.zdt
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.zdt.gralin_464  &
   adams_id = 464  &
   location = 5.9187250255, 1.258402253E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_5_turn_force.zdt.cm  &
   adams_id = 474  &
   location = 5.8490062819, -3.4269971838E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
marker create  &
   marker_name = .template_5_turn_force.zdt.MARKER_468  &
   adams_id = 468  &
   location = 5.9187250255, 1.258402253E-02, 0.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.zdt.MARKER_470  &
   adams_id = 470  &
   location = 5.8490062819, -3.4269971838E-02, 0.8  &
   orientation = 303.9027984031d, 90.0d, 90.0d
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.zdt  &
   mass = 7.2628656927  &
   center_of_mass_marker = .template_5_turn_force.zdt.cm  &
   ixx = 2.028518388E-02  &
   iyy = 2.028518388E-02  &
   izz = 6.4058475409E-03  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.zdt.CYLINDER_214  &
   adams_id = 214  &
   center_marker = .template_5_turn_force.zdt.gralin_464  &
   angle_extent = 360.0  &
   length = 0.168  &
   radius = 4.2E-02  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_5_turn_force.zdt  &
   color = GREEN  &
   name_visibility = off
!
!---------------------------------- _cv_part ----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force._cv_part  &
   adams_id = 2  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force._cv_part
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force._cv_part.marker  &
   adams_id = 300  &
   comments = "Dummy for communicators"  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force._cv_part.marker  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force._cv_part  &
   mass = 0.0  &
   center_of_mass_marker = .template_5_turn_force._cv_part.marker  &
   ixx = 0.0  &
   iyy = 0.0  &
   izz = 0.0  &
   ixy = 0.0  &
   izx = 0.0  &
   iyz = 0.0
!
part attributes  &
   part_name = .template_5_turn_force._cv_part  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
!------------------------------- ges_dragbrace --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ges_dragbrace  &
   adams_id = 33  &
   location = 6.967855, 0.0, 1.31953  &
   orientation = 270.0d, 120.4532239091d, 90.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ges_dragbrace
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ges_dragbrace.MARKER_491  &
   adams_id = 491  &
   location = 0.0, 0.0, -0.5988736811  &
   orientation = 90.0d, 120.4532239091d, 270.0d
!
marker create  &
   marker_name = .template_5_turn_force.ges_dragbrace.MARKER_493  &
   adams_id = 493  &
   location = 0.0, 0.0, -0.5988736811  &
   orientation = 180.0d, 90.0d, 300.4532239091d
!
marker create  &
   marker_name = .template_5_turn_force.ges_dragbrace.cm  &
   adams_id = 301  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_dragbrace.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_dragbrace.inertia_frame  &
   adams_id = 302  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_dragbrace.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_dragbrace.gralin_1  &
   adams_id = 303  &
   location = 0.0, 0.0, -0.5988736811  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_dragbrace.gralin_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_dragbrace.jxs_joint_i_12  &
   adams_id = 304  &
   location = 0.0, 0.0, 0.5988736811  &
   orientation = 90.0d, 120.4532239091d, 270.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_dragbrace.jxs_joint_i_12  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ges_dragbrace  &
   mass = 27.3726690382  &
   center_of_mass_marker = .template_5_turn_force.ges_dragbrace.cm  &
   inertia_marker = .template_5_turn_force.ges_dragbrace.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ges_dragbrace.gralin_dragbrace_geom  &
   adams_id = 85  &
   center_marker = .template_5_turn_force.ges_dragbrace.gralin_1  &
   angle_extent = 360.0  &
   length = 1.1977473622  &
   radius = 5.08E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ges_dragbrace.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .template_5_turn_force.ges_dragbrace  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ges_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ges_upper_cylinder  &
   adams_id = 34  &
   location = 6.1976, 0.0, 1.1938  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ges_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_405  &
   adams_id = 405  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_405  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_407  &
   adams_id = 407  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_407  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_409  &
   adams_id = 409  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_409  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_467  &
   adams_id = 467  &
   location = 0.2788749745, 1.258402253E-02, 0.3938  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_478  &
   adams_id = 478  &
   location = -3.3167643E-03, 0.0, -1.33824231E-02  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_481  &
   adams_id = 481  &
   location = 0.0, 0.0, 0.384302  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_485  &
   adams_id = 485  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.cm  &
   adams_id = 306  &
   location = -3.3167643494E-03, 0.0, -1.3382423116E-02  &
   orientation = 90.0d, 2.0673379194d, 270.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.cm  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.inertia_frame  &
   adams_id = 307  &
   location = -3.3167643494E-03, 0.0, -1.3382423116E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.gralin_2  &
   adams_id = 308  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.gralin_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.gralin_3  &
   adams_id = 309  &
   location = -0.11684, -0.34036, -0.49784  &
   orientation = 161.0534953105d, 58.7414044414d, 213.4869581747d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.gralin_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.gralin_4  &
   adams_id = 310  &
   location = -0.11684, 0.34036, -0.49784  &
   orientation = 18.9465046895d, 58.7414044414d, 326.5130418253d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.gralin_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_11  &
   adams_id = 311  &
   location = 0.0, 0.0, 0.1143  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_11  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_12  &
   adams_id = 312  &
   location = -0.254, 0.0, 0.1778  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_12  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_spring_j_1  &
   adams_id = 314  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_spring_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_damper_j_1  &
   adams_id = 315  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_damper_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_stopper_j_1  &
   adams_id = 316  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_stopper_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1  &
   adams_id = 317  &
   location = 0.0, 0.0, 0.336804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_actuator_j_1  &
   adams_id = 318  &
   location = 0.0, 0.0, 0.336804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_actuator_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_actuator_j_4  &
   adams_id = 319  &
   location = 0.0, 0.0, 0.336804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_actuator_j_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_2  &
   adams_id = 2  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_2  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_116  &
   adams_id = 324  &
   location = 0.0, 0.0, -0.4318  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_116  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ges_upper_cylinder  &
   mass = 82.2524279101  &
   center_of_mass_marker = .template_5_turn_force.ges_upper_cylinder.cm  &
   inertia_marker = .template_5_turn_force.ges_upper_cylinder.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 86  &
   center_marker = .template_5_turn_force.ges_upper_cylinder.gralin_2  &
   angle_extent = 360.0  &
   length = 0.8636  &
   radius = 0.127  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 87  &
   center_marker = .template_5_turn_force.ges_upper_cylinder.gralin_3  &
   angle_extent = 360.0  &
   length = 0.4209662086  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 88  &
   center_marker = .template_5_turn_force.ges_upper_cylinder.gralin_4  &
   angle_extent = 360.0  &
   length = 0.4209662086  &
   radius = 2.54E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_5_turn_force.ges_upper_cylinder  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!----------------------------- ges_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ges_lower_cylinder  &
   adams_id = 35  &
   location = 6.1976, 0.0, 0.9525  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ges_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_378  &
   adams_id = 378  &
   location = -0.1016, 0.0, 0.6191  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_378  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_406  &
   adams_id = 406  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_406  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_408  &
   adams_id = 408  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_408  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_410  &
   adams_id = 410  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_410  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_1  &
   adams_id = 325  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_1  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.cm  &
   adams_id = 326  &
   location = -2.4871874502E-03, 0.0, 3.4740392449E-02  &
   orientation = 270.0d, 0.8125241803d, 90.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.inertia_frame  &
   adams_id = 327  &
   location = -2.4871874502E-03, 0.0, 3.4740392449E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.gralin_5  &
   adams_id = 328  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.gralin_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.jxs_joint_i_11  &
   adams_id = 330  &
   location = 0.0, 0.0, -0.127  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.jxs_joint_i_11  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.gralin_7  &
   adams_id = 331  &
   location = -3.1496E-02, 0.20955, 0.6445  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.gralin_7  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.ues_spring_i_1  &
   adams_id = 332  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.ues_spring_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.ues_damper_i_1  &
   adams_id = 51  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.ues_damper_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.ues_stopper_i_1  &
   adams_id = 333  &
   location = 0.0, 0.0, -0.2445  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.ues_stopper_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.coomarker_2  &
   adams_id = 334  &
   location = -3.1496E-02, 0.0, 0.4445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.coomarker_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.coomarker_3  &
   adams_id = 335  &
   location = -3.1496E-02, 0.0, 0.4699  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.coomarker_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_3  &
   adams_id = 336  &
   location = -3.1496E-02, -0.20955, 0.6445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_3  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_4  &
   adams_id = 337  &
   location = -3.1496E-02, 0.20955, 0.6445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_4  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_6  &
   adams_id = 338  &
   location = -3.1496E-02, 0.20955, 0.6445  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_6  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_8  &
   adams_id = 339  &
   location = -3.1496E-02, -0.20955, 0.6445  &
   orientation = 0.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_8  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_115  &
   adams_id = 344  &
   location = 0.0, 0.0, -0.4445  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_115  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ges_lower_cylinder  &
   mass = 84.8838172052  &
   center_of_mass_marker = .template_5_turn_force.ges_lower_cylinder.cm  &
   inertia_marker = .template_5_turn_force.ges_lower_cylinder.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ges_lower_cylinder.gralin_geom1  &
   adams_id = 89  &
   center_marker = .template_5_turn_force.ges_lower_cylinder.gralin_5  &
   angle_extent = 360.0  &
   length = 0.889  &
   radius = 0.1016  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ges_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_lower_cylinder.gralin_geom2  &
   adams_id = 90  &
   center_marker = .template_5_turn_force.ges_lower_cylinder.gralin_7  &
   angle_extent = 360.0  &
   length = 0.4191  &
   radius = 3.048E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ges_lower_cylinder.gralin_geom2  &
   color = BLUE_GRAY
!
part attributes  &
   part_name = .template_5_turn_force.ges_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ges_upper_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ges_upper_torque_arm  &
   adams_id = 36  &
   location = 6.4897, 0.0, 0.7747  &
   orientation = 90.0d, 111.0375110254d, 270.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ges_upper_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.cm  &
   adams_id = 345  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.inertia_frame  &
   adams_id = 346  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.gralin_9  &
   adams_id = 347  &
   location = 0.0, 0.0, -0.1768905311  &
   orientation = 90.0d, 13.4695391009d, 270.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.gralin_9  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.jxs_joint_j_8  &
   adams_id = 348  &
   location = 9.333456062E-02, 0.0, 0.2127884391  &
   orientation = 0.0d, 90.0d, 111.0375110254d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.jxs_joint_j_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.jxs_joint_i_10  &
   adams_id = 349  &
   location = 0.0, 0.0, -0.1768905311  &
   orientation = 0.0d, 90.0d, 111.0375110254d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.jxs_joint_i_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ges_upper_torque_arm  &
   mass = 0.3898630024  &
   center_of_mass_marker = .template_5_turn_force.ges_upper_torque_arm.cm  &
   inertia_marker =   &
                    .template_5_turn_force.ges_upper_torque_arm.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   adams_id = 91  &
   center_marker = .template_5_turn_force.ges_upper_torque_arm.gralin_9  &
   angle_extent = 360.0  &
   length = 0.4007006863  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   color = GREEN
!
part attributes  &
   part_name = .template_5_turn_force.ges_upper_torque_arm  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!---------------------------- ges_lower_torque_arm ----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ges_lower_torque_arm  &
   adams_id = 37  &
   location = 6.477, 0.0, 0.6223  &
   orientation = 90.0d, 63.4349488229d, 270.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ges_lower_torque_arm
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.MARKER_379  &
   adams_id = 379  &
   location = 0.1788854382, 0.0, -0.2882291623  &
   orientation = 0.0d, 90.0d, 63.4349488229d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.MARKER_379  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.cm  &
   adams_id = 350  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.inertia_frame  &
   adams_id = 351  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.jxs_joint_i_8  &
   adams_id = 352  &
   location = 8.94427191E-02, 0.0, 0.1540650836  &
   orientation = 0.0d, 90.0d, 63.4349488229d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.jxs_joint_i_8  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.gralin_10  &
   adams_id = 353  &
   location = 0.1788854382, 0.0, -0.2882291623  &
   orientation = 270.0d, 11.4324305526d, 90.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.gralin_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ges_lower_torque_arm  &
   mass = 0.3898630024  &
   center_of_mass_marker = .template_5_turn_force.ges_lower_torque_arm.cm  &
   inertia_marker =   &
                    .template_5_turn_force.ges_lower_torque_arm.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   adams_id = 92  &
   center_marker = .template_5_turn_force.ges_lower_torque_arm.gralin_10  &
   angle_extent = 360.0  &
   length = 0.4512473823  &
   radius = 1.27E-02  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   color = MAGENTA
!
part attributes  &
   part_name = .template_5_turn_force.ges_lower_torque_arm  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- ges_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_5_turn_force.ges_collar  &
   adams_id = 40  &
   location = 6.1976, 0.0, 0.809498  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ges_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.MARKER_465  &
   adams_id = 465  &
   location = 0.0, 0.2, -9.498E-03  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.MARKER_477  &
   adams_id = 477  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.MARKER_482  &
   adams_id = 482  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.jxs_joint_j_10  &
   adams_id = 368  &
   location = 0.127, 0.0, 2.8702E-02  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_collar.jxs_joint_j_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.cm  &
   adams_id = 369  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_collar.cm  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.inertia_frame  &
   adams_id = 370  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_collar.inertia_frame  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.gralin_24  &
   adams_id = 371  &
   location = 0.0, 0.0, -4.7498E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_collar.gralin_24  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.jxs_joint_i_1  &
   adams_id = 372  &
   location = 0.0, 0.0, 4.7498E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_collar.jxs_joint_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.ues_actuator_i_1  &
   adams_id = 373  &
   location = 0.0, 0.0, 4.7498E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_collar.ues_actuator_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
marker create  &
   marker_name = .template_5_turn_force.ges_collar.ues_actuator_i_4  &
   adams_id = 374  &
   location = 0.0, 0.0, 4.7498E-02  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.ges_collar.ues_actuator_i_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
part create rigid_body mass_properties  &
   part_name = .template_5_turn_force.ges_collar  &
   mass = 6.4242828175  &
   center_of_mass_marker = .template_5_turn_force.ges_collar.cm  &
   inertia_marker = .template_5_turn_force.ges_collar.inertia_frame  &
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
   cylinder_name = .template_5_turn_force.ges_collar.gralin_collar  &
   adams_id = 93  &
   center_marker = .template_5_turn_force.ges_collar.gralin_24  &
   angle_extent = 360.0  &
   length = 9.4996E-02  &
   radius = 0.1397  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_5_turn_force.ges_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .template_5_turn_force.ges_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 5.0E-02
!
!--------------------------------- Equations ----------------------------------!
!
!
part create equation differential_equation  &
   differential_equation_name = .template_5_turn_force._cv_diff  &
   adams_id = 1  &
   comments = "Dummy for communicators"  &
   initial_condition = 0.0  &
   function = ""  &
   implicit = off  &
   static_hold = off
!
part attributes  &
   equation_name = .template_5_turn_force._cv_diff  &
   visibility = off
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.JOINT_51  &
   adams_id = 51  &
   i_marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_378  &
   j_marker_name = .template_5_turn_force.ges_lower_torque_arm.MARKER_379
!
constraint attributes  &
   constraint_name = .template_5_turn_force.JOINT_51  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.jolrev_lta_lc_joint  &
   adams_id = 2  &
   i_marker_name = .template_5_turn_force.gel_lower_torquearm.jxl_joint_i_11  &
   j_marker_name = .template_5_turn_force.gel_lower_cylinder.jxl_joint_j_11
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolrev_lta_lc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.jorrev_lta_lc_joint  &
   adams_id = 3  &
   i_marker_name = .template_5_turn_force.ger_lower_torquearm.jxr_joint_i_11  &
   j_marker_name = .template_5_turn_force.ger_lower_cylinder.jxr_joint_j_11
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorrev_lta_lc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_turn_force.jolcyl_lc_uc_joint  &
   adams_id = 4  &
   i_marker_name = .template_5_turn_force.gel_lower_cylinder.jxl_joint_i_12  &
   j_marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_12
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolcyl_lc_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_turn_force.jorcyl_lc_uc_joint  &
   adams_id = 5  &
   i_marker_name = .template_5_turn_force.ger_lower_cylinder.jxr_joint_i_12  &
   j_marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_12
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorcyl_lc_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_turn_force.jolrev_ldb_udb_joint  &
   adams_id = 6  &
   i_marker_name = .template_5_turn_force.gel_lower_dragbrace.jxl_joint_i_14  &
   j_marker_name = .template_5_turn_force.gel_upper_dragbrace.jxl_joint_j_14
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolrev_ldb_udb_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_turn_force.jorrev_ldb_udb_joint  &
   adams_id = 7  &
   i_marker_name = .template_5_turn_force.ger_lower_dragbrace.jxr_joint_i_14  &
   j_marker_name = .template_5_turn_force.ger_upper_dragbrace.jxr_joint_j_14
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorrev_ldb_udb_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_turn_force.jolcyl_lta_connect  &
   adams_id = 12  &
   i_marker_name = .template_5_turn_force.gel_lower_torquearm.jxl_joint_i_1  &
   j_marker_name = .template_5_turn_force.gel_connector.jxl_joint_j_1
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolcyl_lta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_turn_force.jorcyl_lta_connect  &
   adams_id = 13  &
   i_marker_name = .template_5_turn_force.ger_lower_torquearm.jxr_joint_i_1  &
   j_marker_name = .template_5_turn_force.ger_connector.jxr_joint_j_1
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorcyl_lta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.jolrev_uta_connect  &
   adams_id = 14  &
   i_marker_name = .template_5_turn_force.gel_upper_torquearm.jxl_joint_i_2  &
   j_marker_name = .template_5_turn_force.gel_connector.jxl_joint_j_2
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolrev_uta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.jorrev_uta_connect  &
   adams_id = 15  &
   i_marker_name = .template_5_turn_force.ger_upper_torquearm.jxr_joint_i_2  &
   j_marker_name = .template_5_turn_force.ger_connector.jxr_joint_j_2
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorrev_uta_connect  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.jolrev_uta_collar  &
   adams_id = 16  &
   i_marker_name = .template_5_turn_force.gel_upper_torquearm.jxl_joint_i_3  &
   j_marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_j_3
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolrev_uta_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.jorrev_uta_collar  &
   adams_id = 17  &
   i_marker_name = .template_5_turn_force.ger_upper_torquearm.jxr_joint_i_3  &
   j_marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_j_3
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorrev_uta_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_turn_force.jolrev_collar_uc  &
   adams_id = 18  &
   i_marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_i_4  &
   j_marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_4
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolrev_collar_uc  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_turn_force.jorrev_collar_uc  &
   adams_id = 19  &
   i_marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_i_4  &
   j_marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_4
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorrev_collar_uc  &
   size_of_icons = 5.0E-02
!
constraint create joint hooke  &
   joint_name = .template_5_turn_force.jolhoo_udb_spndl  &
   adams_id = 20  &
   i_marker_name = .template_5_turn_force.gel_upper_dragbrace.jxl_joint_i_5  &
   j_marker_name = .template_5_turn_force.gel_spindle.jxl_joint_j_5
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolhoo_udb_spndl  &
   size_of_icons = 5.0E-02
!
constraint create joint hooke  &
   joint_name = .template_5_turn_force.jorhoo_udb_spndl  &
   adams_id = 21  &
   i_marker_name = .template_5_turn_force.ger_upper_dragbrace.jxr_joint_i_5  &
   j_marker_name = .template_5_turn_force.ger_spindle.jxr_joint_j_5
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorhoo_udb_spndl  &
   size_of_icons = 5.0E-02
!
constraint create joint spherical  &
   joint_name = .template_5_turn_force.jolsph_uc_lwract  &
   adams_id = 24  &
   i_marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_i_7  &
   j_marker_name = .template_5_turn_force.gel_lwract.jxl_joint_j_7
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolsph_uc_lwract  &
   size_of_icons = 5.0E-02
!
constraint create joint spherical  &
   joint_name = .template_5_turn_force.jorsph_uc_lwract  &
   adams_id = 25  &
   i_marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_i_7  &
   j_marker_name = .template_5_turn_force.ger_lwract.jxr_joint_j_7
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorsph_uc_lwract  &
   size_of_icons = 5.0E-02
!
constraint create joint translational  &
   joint_name = .template_5_turn_force.joltra_lwract_upract  &
   adams_id = 26  &
   i_marker_name = .template_5_turn_force.gel_lwract.jxl_joint_i_8  &
   j_marker_name = .template_5_turn_force.gel_upract.jxl_joint_j_8
!
constraint attributes  &
   constraint_name = .template_5_turn_force.joltra_lwract_upract  &
   size_of_icons = 5.0E-02
!
constraint create joint translational  &
   joint_name = .template_5_turn_force.jortra_lwract_upract  &
   adams_id = 27  &
   i_marker_name = .template_5_turn_force.ger_lwract.jxr_joint_i_8  &
   j_marker_name = .template_5_turn_force.ger_upract.jxr_joint_j_8
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jortra_lwract_upract  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.jolrev_ldb_collar  &
   adams_id = 30  &
   i_marker_name = .template_5_turn_force.gel_lower_dragbrace.jxl_joint_i_10  &
   j_marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_j_10
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jolrev_ldb_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.jorrev_ldb_collar  &
   adams_id = 31  &
   i_marker_name = .template_5_turn_force.ger_lower_dragbrace.jxr_joint_i_10  &
   j_marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_j_10
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jorrev_ldb_collar  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_turn_force.JOINT_69  &
   adams_id = 69  &
   i_marker_name = .template_5_turn_force.js.MARKER_492  &
   j_marker_name = .template_5_turn_force.ges_dragbrace.MARKER_493
!
constraint attributes  &
   constraint_name = .template_5_turn_force.JOINT_69  &
   name_visibility = off
!
constraint create joint fixed  &
   joint_name = .template_5_turn_force.JOINT_59  &
   adams_id = 59  &
   i_marker_name = .template_5_turn_force.js.MARKER_443  &
   j_marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_444
!
constraint attributes  &
   constraint_name = .template_5_turn_force.JOINT_59  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_turn_force.JOINT_60  &
   adams_id = 60  &
   i_marker_name = .template_5_turn_force.js.MARKER_445  &
   j_marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_446
!
constraint attributes  &
   constraint_name = .template_5_turn_force.JOINT_60  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.collar_hsg  &
   adams_id = 64  &
   i_marker_name = .template_5_turn_force.ges_collar.MARKER_465  &
   j_marker_name = .template_5_turn_force.hsg.MARKER_466
!
constraint attributes  &
   constraint_name = .template_5_turn_force.collar_hsg  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.upcylinder_zdt  &
   adams_id = 65  &
   i_marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_467  &
   j_marker_name = .template_5_turn_force.zdt.MARKER_468
!
constraint attributes  &
   constraint_name = .template_5_turn_force.upcylinder_zdt  &
   name_visibility = off
!
constraint create joint translational  &
   joint_name = .template_5_turn_force.hsg_zdt  &
   adams_id = 66  &
   i_marker_name = .template_5_turn_force.hsg.MARKER_469  &
   j_marker_name = .template_5_turn_force.zdt.MARKER_470
!
constraint attributes  &
   constraint_name = .template_5_turn_force.hsg_zdt  &
   name_visibility = off
!
constraint create joint spherical  &
   joint_name = .template_5_turn_force.josrev_lta_uta_joint  &
   adams_id = 39  &
   i_marker_name = .template_5_turn_force.ges_lower_torque_arm.jxs_joint_i_8  &
   j_marker_name = .template_5_turn_force.ges_upper_torque_arm.jxs_joint_j_8
!
constraint attributes  &
   constraint_name = .template_5_turn_force.josrev_lta_uta_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.josrev_uta_uc_joint  &
   adams_id = 41  &
   i_marker_name =   &
                   .template_5_turn_force.ges_upper_torque_arm.jxs_joint_i_10  &
   j_marker_name = .template_5_turn_force.ges_collar.jxs_joint_j_10
!
constraint attributes  &
   constraint_name = .template_5_turn_force.josrev_uta_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint cylindrical  &
   joint_name = .template_5_turn_force.joscyl_lc_uc_joint  &
   adams_id = 42  &
   i_marker_name = .template_5_turn_force.ges_lower_cylinder.jxs_joint_i_11  &
   j_marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_11
!
constraint attributes  &
   constraint_name = .template_5_turn_force.joscyl_lc_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint spherical  &
   joint_name = .template_5_turn_force.jossph_db_uc_joint  &
   adams_id = 43  &
   i_marker_name = .template_5_turn_force.ges_dragbrace.jxs_joint_i_12  &
   j_marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_12
!
constraint attributes  &
   constraint_name = .template_5_turn_force.jossph_db_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.josrev_collar_uc_joint  &
   adams_id = 48  &
   i_marker_name = .template_5_turn_force.ges_collar.jxs_joint_i_1  &
   j_marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1
!
constraint attributes  &
   constraint_name = .template_5_turn_force.josrev_collar_uc_joint  &
   size_of_icons = 5.0E-02
!
constraint create joint fixed  &
   joint_name = .template_5_turn_force.JOINT_68  &
   adams_id = 68  &
   i_marker_name = .template_5_turn_force.js.MARKER_484  &
   j_marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_485
!
constraint attributes  &
   constraint_name = .template_5_turn_force.JOINT_68  &
   name_visibility = off
!
!----------------------------------- Forces -----------------------------------!
!
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.NLG_AIR  &
   adams_id = 11  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_405  &
   j_marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_406  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_turn_force.NLG_AIR  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.NLG_OIL  &
   adams_id = 12  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_407  &
   j_marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_408  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_turn_force.NLG_OIL  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.NLG_STOP  &
   adams_id = 13  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_409  &
   j_marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_410  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_turn_force.NLG_STOP  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.LMLG_AIR  &
   adams_id = 14  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_411  &
   j_marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_412  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_turn_force.LMLG_AIR  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.LMLG_OIL  &
   adams_id = 15  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_413  &
   j_marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_414  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_turn_force.LMLG_OIL  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.LMLG_STOP  &
   adams_id = 16  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_415  &
   j_marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_416  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_turn_force.LMLG_STOP  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.RMLG_AIR  &
   adams_id = 17  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_417  &
   j_marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_418  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_turn_force.RMLG_AIR  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.RMLG_OIL  &
   adams_id = 18  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_419  &
   j_marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_420  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_turn_force.RMLG_OIL  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.RMLG_STOP  &
   adams_id = 19  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_421  &
   j_marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_422  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_5_turn_force.RMLG_STOP  &
   size_of_icons = 5.0E-02
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.turning_force  &
   adams_id = 22  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.hsg.MARKER_471  &
   j_marker_name = .template_5_turn_force.hsg.MARKER_472  &
   action_only = on  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.thrust  &
   adams_id = 23  &
   type_of_freedom = translational  &
   i_marker_name = .template_5_turn_force.js.MARKER_475  &
   j_marker_name = .template_5_turn_force.js.MARKER_476  &
   action_only = on  &
   function = ""
!
force create direct single_component_force  &
   single_component_force_name = .template_5_turn_force.damping_force  &
   adams_id = 24  &
   type_of_freedom = rotational  &
   i_marker_name = .template_5_turn_force.ges_collar.MARKER_477  &
   j_marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_478  &
   action_only = off  &
   function = ""
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_5_turn_force.NLG_m  &
   range = -10.0, 10.0  &
   delta_type = percent_relative  &
   real_value = 13.6077711
!
variable create  &
   variable_name = .template_5_turn_force.NLG_Ixx_Iyy  &
   range = -10.0, 10.0  &
   delta_type = percent_relative  &
   real_value = 0.3511675841
!
variable create  &
   variable_name = .template_5_turn_force.NLG_Izz  &
   range = -10.0, 10.0  &
   delta_type = percent_relative  &
   real_value = 0.5560153415
!
variable create  &
   variable_name = .template_5_turn_force.MLG_m  &
   range = -10.0, 10.0  &
   delta_type = percent_relative  &
   real_value = 45.359237
!
variable create  &
   variable_name = .template_5_turn_force.MLG_Ixx_Iyy  &
   range = -10.0, 10.0  &
   delta_type = percent_relative  &
   real_value = 2.7215487769
!
variable create  &
   variable_name = .template_5_turn_force.MLG_Izz  &
   range = -10.0, 10.0  &
   delta_type = percent_relative  &
   real_value = 4.6822344549
!
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .template_5_turn_force.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=35.0 step_size=1.0E-02 model_name=.GCMB"
!
simulation script create  &
   sim_script_name = .template_5_turn_force.Last_Sim_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=2.0 number_of_steps=300 model_name=._AA_nlg_post_2hubs"
!
!-------------------------- Adams View UDE Instances --------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
undo begin_block suppress = yes
!
ude create instance  &
   instance_name = .template_5_turn_force.lumian  &
   definition_name = .MDI.Forces.vpg_road  &
   location = 12.2383679771, 1.5095002745, -0.5608546166  &
   orientation = 0.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_5_turn_force.lumian  &
   color = DimGray  &
   visibility = on
!
ude create instance  &
   instance_name = .template_5_turn_force.luntai1  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 0.0, 90.0, 0.0
!
ude create instance  &
   instance_name = .template_5_turn_force.luntai2  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 0.0, 90.0, 0.0
!
ude create instance  &
   instance_name = .template_5_turn_force.luntai1_2  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 6.229096, -0.20955, 0.308  &
   orientation = 0.0, 90.0, 0.0
!
ude create instance  &
   instance_name = .template_5_turn_force.luntai2_2  &
   definition_name = .MDI.Forces.vpg_tire  &
   location = 6.229096, 0.20955, 0.308  &
   orientation = 0.0, 90.0, 0.0
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_turn_force.lumian.ref_marker  &
   object_value = .template_5_turn_force.ground.lumian_ref_1
!
variable modify  &
   variable_name = .template_5_turn_force.lumian.road_property_file  &
   string_value = "2d_flat.rdf"
!
variable modify  &
   variable_name = .template_5_turn_force.lumian.road_graphics  &
   string_value = "on"
!
ude modify instance  &
   instance_name = .template_5_turn_force.lumian
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.vmmrk  &
   object_value = (.template_5_turn_force.luntai1.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.wmmrk  &
   object_value = (.template_5_turn_force.luntai1.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.road_property_file  &
   string_value = (.template_5_turn_force.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.j_fmarker  &
   object_value = .template_5_turn_force.ground.luntai1_tire_jf_1
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.ref_marker  &
   object_value = (.template_5_turn_force.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.wheel_tire_mass  &
   real_value = (.template_5_turn_force.MLG_m)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.Ixx_Iyy  &
   real_value = (.template_5_turn_force.MLG_Ixx_Iyy)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.Izz  &
   real_value = (.template_5_turn_force.MLG_Izz)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.property_file  &
   string_value = "MLG.tir"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1.road_name  &
   string_value = (.template_5_turn_force.lumian)
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai1
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker create  &
   marker_name = .template_5_turn_force.luntai1.wheel_part.MARKER_499  &
   adams_id = 499  &
   location = 12.2709739569, 1.8115919597, 0.1742595194  &
   orientation = 180.0d, 90.0d, 180.0d
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.vmmrk  &
   object_value = (.template_5_turn_force.luntai2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.wmmrk  &
   object_value = (.template_5_turn_force.luntai2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.road_property_file  &
   string_value = (.template_5_turn_force.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.j_fmarker  &
   object_value = .template_5_turn_force.ground.luntai2_tire_jf_1
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.ref_marker  &
   object_value = (.template_5_turn_force.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.wheel_tire_mass  &
   real_value = (.template_5_turn_force.MLG_m)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.Ixx_Iyy  &
   real_value = (.template_5_turn_force.MLG_Ixx_Iyy)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.Izz  &
   real_value = (.template_5_turn_force.MLG_Izz)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.property_file  &
   string_value = "MLG.tir"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2.road_name  &
   string_value = (.template_5_turn_force.lumian)
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai2
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker create  &
   marker_name = .template_5_turn_force.luntai2.wheel_part.MARKER_496  &
   adams_id = 496  &
   location = 12.2709739569, -1.8115919597, 0.1742595194  &
   orientation = 180.0d, 90.0d, 180.0d
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.vmmrk  &
   object_value = (.template_5_turn_force.luntai1_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.wmmrk  &
   object_value = (.template_5_turn_force.luntai1_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.road_property_file  &
   string_value = (.template_5_turn_force.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.j_fmarker  &
   object_value = .template_5_turn_force.ground.luntai1_tire_jf_11
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.ref_marker  &
   object_value = (.template_5_turn_force.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.wheel_tire_mass  &
   real_value = (.template_5_turn_force.NLG_Izz)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.Ixx_Iyy  &
   real_value = (.template_5_turn_force.NLG_Ixx_Iyy)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.Izz  &
   real_value = (.template_5_turn_force.NLG_Izz)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.property_file  &
   string_value = "NLG.tir"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai1_2.road_name  &
   string_value = (.template_5_turn_force.lumian)
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai1_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker create  &
   marker_name = .template_5_turn_force.luntai1_2.wheel_part.MARKER_7  &
   adams_id = 376  &
   location = 6.229096, -0.20955, 0.308  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.luntai1_2.wheel_part.MARKER_7  &
   size_of_icons = 5.0E-02
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.cm_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.center_offset  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ic_vmode  &
   string_value = "advanced"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.vm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.wm  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.long_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.spin_vel  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.vx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.vy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.vz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.wx  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.wy  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.wz  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ic_vx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ic_vy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ic_vz  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ic_wx  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ic_wy  &
   string_value = "off"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ic_wz  &
   string_value = "wz"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ic_vm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ic_wm  &
   string_value = "marker"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.vmmrk  &
   object_value = (.template_5_turn_force.luntai2_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.wmmrk  &
   object_value = (.template_5_turn_force.luntai2_2.wheel_part.wheel_cm)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.side  &
   string_value = "left"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.road_property_file  &
   string_value = (.template_5_turn_force.lumian.road_property_file)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.j_fmarker  &
   object_value = .template_5_turn_force.ground.luntai2_tire_jf_11
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.ref_marker  &
   object_value = (.template_5_turn_force.lumian.ref_marker.object_value)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.wheel_tire_mass  &
   real_value = (.template_5_turn_force.NLG_m)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.Ixx_Iyy  &
   real_value = (.template_5_turn_force.NLG_Ixx_Iyy)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.Izz  &
   real_value = (.template_5_turn_force.NLG_Izz)
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.property_file  &
   string_value = "NLG.tir"
!
variable modify  &
   variable_name = .template_5_turn_force.luntai2_2.road_name  &
   string_value = (.template_5_turn_force.lumian)
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai2_2
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker create  &
   marker_name = .template_5_turn_force.luntai2_2.wheel_part.MARKER_5  &
   adams_id = 377  &
   location = 6.229096, 0.20955, 0.308  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_5_turn_force.luntai2_2.wheel_part.MARKER_5  &
   size_of_icons = 5.0E-02
!
undo end_block
!
!--------------------------- UDE Dependent Objects ----------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.JOINT_70  &
   adams_id = 70  &
   i_marker_name = .template_5_turn_force.luntai2.wheel_part.MARKER_496  &
   j_marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_497
!
constraint attributes  &
   constraint_name = .template_5_turn_force.JOINT_70  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.JOINT_71  &
   adams_id = 71  &
   i_marker_name = .template_5_turn_force.luntai1.wheel_part.MARKER_499  &
   j_marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_500
!
constraint attributes  &
   constraint_name = .template_5_turn_force.JOINT_71  &
   name_visibility = off
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.JOINT_1  &
   adams_id = 1  &
   i_marker_name = .template_5_turn_force.luntai2_2.wheel_part.MARKER_5  &
   j_marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_6
!
constraint attributes  &
   constraint_name = .template_5_turn_force.JOINT_1  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
constraint create joint revolute  &
   joint_name = .template_5_turn_force.JOINT_2  &
   adams_id = 49  &
   i_marker_name = .template_5_turn_force.luntai1_2.wheel_part.MARKER_7  &
   j_marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_8
!
constraint attributes  &
   constraint_name = .template_5_turn_force.JOINT_2  &
   name_visibility = off  &
   size_of_icons = 5.0E-02
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry create shape force  &
   force_name = .template_5_turn_force.SFORCE_22_force_graphic_1  &
   adams_id = 215  &
   force_element_name = .template_5_turn_force.turning_force  &
   applied_at_marker_name = .template_5_turn_force.hsg.MARKER_471
!
geometry create shape force  &
   force_name = .template_5_turn_force.NLG_OIL_force_graphic_2  &
   adams_id = 210  &
   force_element_name = .template_5_turn_force.NLG_OIL  &
   applied_at_marker_name =   &
                            .template_5_turn_force.ges_lower_cylinder.MARKER_408
!
geometry create shape force  &
   force_name = .template_5_turn_force.SFORCE_23_force_graphic_1  &
   adams_id = 264  &
   force_element_name = .template_5_turn_force.thrust  &
   applied_at_marker_name = .template_5_turn_force.js.MARKER_475
!
geometry create shape force  &
   force_name = .template_5_turn_force.SFORCE_24_force_graphic_1  &
   adams_id = 265  &
   force_element_name = .template_5_turn_force.damping_force  &
   applied_at_marker_name = .template_5_turn_force.ges_collar.MARKER_477
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   z_component_gravity = -9.81
!
force attributes  &
   force_name = .template_5_turn_force.gravity  &
   size_of_icons = 5.0E-02
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------------- Measures ----------------------------------!
!
!
measure create object  &
   measure_name = .template_5_turn_force.Disp_X  &
   from_first = no  &
   object = .template_5_turn_force.js  &
   characteristic = cm_position  &
   component = x_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_5_turn_force.Disp_X  &
   color = WHITE
!
measure create object  &
   measure_name = .template_5_turn_force.Disp_Y  &
   from_first = no  &
   object = .template_5_turn_force.js  &
   characteristic = cm_position  &
   component = y_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_5_turn_force.Disp_Y  &
   color = WHITE
!
measure create point  &
   measure_name = .template_5_turn_force.jscm_sd  &
   point = .template_5_turn_force.js.cm  &
   characteristic = translational_velocity  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_5_turn_force.jscm_sd  &
   color = WHITE
!
measure create function  &
   measure_name = .template_5_turn_force.jiaodu  &
   function = ""  &
   units = "no_units"  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_5_turn_force.jiaodu  &
   color = WHITE
!
measure create function  &
   measure_name = .template_5_turn_force.jsd  &
   function = ""  &
   units = "no_units"  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_5_turn_force.jsd  &
   color = WHITE
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_5_turn_force.NLG_Aa  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.480717E-02
!
variable create  &
   variable_name = .template_5_turn_force.NLG_V0  &
   units = "volume"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.028E-02
!
variable create  &
   variable_name = .template_5_turn_force.NLG_P0  &
   units = "pressure"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.3E+06
!
variable create  &
   variable_name = .template_5_turn_force.n_Poly  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.1
!
variable create  &
   variable_name = .template_5_turn_force.Patm  &
   units = "pressure"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.01325E+05
!
variable create  &
   variable_name = .template_5_turn_force.rho_Oil  &
   units = "density"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 860.0
!
variable create  &
   variable_name = .template_5_turn_force.NLG_A_MAIN_OIL  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.953E-02
!
variable create  &
   variable_name = .template_5_turn_force.NLG_A_RET_OIL  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 6.139E-03
!
variable create  &
   variable_name = .template_5_turn_force.NLG_A_MAIN_POS  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.14E-04
!
variable create  &
   variable_name = .template_5_turn_force.NLG_A_MAIN_NEG  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.14E-04
!
variable create  &
   variable_name = .template_5_turn_force.NLG_A_RET_POS  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.313E-03
!
variable create  &
   variable_name = .template_5_turn_force.NLG_A_RET_NEG  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.0E-04
!
variable create  &
   variable_name = .template_5_turn_force.NLG_MAIN_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_5_turn_force.NLG_RET_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_5_turn_force.MLG_Aa  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 8.921E-03
!
variable create  &
   variable_name = .template_5_turn_force.MLG_V0  &
   units = "volume"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.931E-03
!
variable create  &
   variable_name = .template_5_turn_force.MLG_P0  &
   units = "pressure"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.45E+06
!
variable create  &
   variable_name = .template_5_turn_force.MLG_A_MAIN_OIL  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 5.5571E-02
!
variable create  &
   variable_name = .template_5_turn_force.MLG_A_RET_OIL  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.4961E-02
!
variable create  &
   variable_name = .template_5_turn_force.MLG_A_MAIN_POS  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.96E-03
!
variable create  &
   variable_name = .template_5_turn_force.MLG_A_MAIN_NEG  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.96E-03
!
variable create  &
   variable_name = .template_5_turn_force.MLG_A_RET_POS  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 3.798E-03
!
variable create  &
   variable_name = .template_5_turn_force.MLG_A_RET_NEG  &
   units = "area"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 1.57E-04
!
variable create  &
   variable_name = .template_5_turn_force.MLG_MAIN_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_5_turn_force.MLG_RET_Cd  &
   units = "no_units"  &
   range = -6.4516E-04, 6.4516E-04  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 0.8
!
variable create  &
   variable_name = .template_5_turn_force.V_sheding  &
   units = "velocity"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 2.0
!
variable create  &
   variable_name = .template_5_turn_force.T_1  &
   units = "time"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 10.0
!
variable create  &
   variable_name = .template_5_turn_force.T_2  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 14.0
!
variable create  &
   variable_name = .template_5_turn_force.angle  &
   units = "no_units"  &
   range = -1.0, 1.0  &
   use_allowed_values = no  &
   delta_type = relative  &
   real_value = 30.0
!
!---------------------------- Function definitions ----------------------------!
!
!
data_element modify variable  &
   variable_name = .template_5_turn_force.NLG_V  &
   function = "-1*VR(.template_5_turn_force.ges_upper_cylinder.MARKER_2,.template_5_turn_force.ges_lower_cylinder.MARKER_1)"
!
data_element modify variable  &
   variable_name = .template_5_turn_force.LMLG_S  &
   function = "1.014262-DM(.template_5_turn_force.gel_upper_cylinder.MARKER_272,.template_5_turn_force.gel_lower_cylinder.MARKER_273)"
!
data_element modify variable  &
   variable_name = .template_5_turn_force.RMLG_S  &
   function = "1.014262-DM(.template_5_turn_force.ger_upper_cylinder.MARKER_278,.template_5_turn_force.ger_lower_cylinder.MARKER_279)"
!
data_element modify variable  &
   variable_name = .template_5_turn_force.LMLG_V  &
   function = "-1*VR(.template_5_turn_force.gel_upper_cylinder.MARKER_272,.template_5_turn_force.gel_lower_cylinder.MARKER_273)"
!
data_element modify variable  &
   variable_name = .template_5_turn_force.RMLG_V  &
   function = "-1*VR(.template_5_turn_force.ger_upper_cylinder.MARKER_278,.template_5_turn_force.ger_lower_cylinder.MARKER_279)"
!
data_element modify variable  &
   variable_name = .template_5_turn_force.NLG_S  &
   function = "0.4286-DM(.template_5_turn_force.ges_upper_cylinder.MARKER_2,.template_5_turn_force.ges_lower_cylinder.MARKER_1)"
!
data_element modify variable  &
   variable_name = .template_5_turn_force.x1  &
   function = "-1*(VARVAL(.template_5_turn_force.NLG_V)*0.5*(VARVAL(.template_5_turn_force.NLG_V)-ABS(VARVAL(.template_5_turn_force.NLG_V)))*((.template_5_turn_force.rho_Oil*.template_5_turn_force.NLG_A_MAIN_OIL**3/(2*.template_5_turn_force.NLG_MAIN_Cd**2*.template_5_turn_force.NLG_A_MAIN_NEG**2))+(.template_5_turn_force.rho_Oil*.template_5_turn_force.NLG_A_RET_OIL**3/(2*.template_5_turn_force.NLG_RET_Cd**2*.template_5_turn_force.NLG_A_RET_NEG**2))))"
!
data_element modify variable  &
   variable_name = .template_5_turn_force.x2  &
   function = "0.00001*VARVAL(.template_5_turn_force.NLG_V)*0.5*(VARVAL(.template_5_turn_force.NLG_V)+ABS(VARVAL(.template_5_turn_force.NLG_V)))*((.template_5_turn_force.rho_Oil*.template_5_turn_force.NLG_A_MAIN_OIL**3/(2*.template_5_turn_force.NLG_MAIN_Cd**2*.template_5_turn_force.NLG_A_MAIN_POS**2))+(.template_5_turn_force.rho_Oil*.template_5_turn_force.NLG_A_RET_OIL**3/(2*.template_5_turn_force.NLG_RET_Cd**2*.template_5_turn_force.NLG_A_RET_POS**2)))"
!
data_element modify variable  &
   variable_name = .template_5_turn_force.VARIABLE_123  &
   function = "IF(TIME:0,1,2)"
!
data_element modify variable  &
   variable_name = .template_5_turn_force.VARIABLE_124  &
   function = "VARVAL(.template_5_turn_force.NLG_V)-ABS(VARVAL(.template_5_turn_force.NLG_V))"
!
data_element modify variable  &
   variable_name = .template_5_turn_force._cv_solver_variable  &
   function = "0"
!
measure modify function  &
   measure_name = .template_5_turn_force.jiaodu  &
   function = "AZ(.template_5_turn_force.ges_collar.inertia_frame,.template_5_turn_force.ges_upper_cylinder.inertia_frame)*180/pi-180"
!
measure modify function  &
   measure_name = .template_5_turn_force.jsd  &
   function = "wz(.template_5_turn_force.ges_collar.inertia_frame,.template_5_turn_force.ges_upper_cylinder.inertia_frame)*30/pi"
!
part modify equation differential_equation  &
   differential_equation_name = .template_5_turn_force._cv_diff  &
   function = "0"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.NLG_AIR  &
   function = "1*.template_5_turn_force.NLG_Aa*(.template_5_turn_force.NLG_P0*(.template_5_turn_force.NLG_V0/(.template_5_turn_force.NLG_V0-.template_5_turn_force.NLG_Aa*(0.4286-DM(.template_5_turn_force.ges_upper_cylinder.MARKER_2,.template_5_turn_force.ges_lower_cylinder.MARKER_1))))**1.1-.template_5_turn_force.Patm)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.NLG_OIL  &
   function = "IF(VARVAL(.template_5_turn_force.NLG_V):1*-1*(VARVAL(.template_5_turn_force.NLG_V)*0.5*(VARVAL(.template_5_turn_force.NLG_V)-ABS(VARVAL(.template_5_turn_force.NLG_V)))*((.template_5_turn_force.rho_Oil*.template_5_turn_force.NLG_A_MAIN_OIL**3/(2*.template_5_turn_force.NLG_MAIN_Cd**2*.template_5_turn_force.NLG_A_MAIN_NEG**2))+(.template_5_turn_force.rho_Oil*.template_5_turn_force.NLG_A_RET_OIL**3/(2*.template_5_turn_force.NLG_RET_Cd**2*.template_5_turn_force.NLG_A_RET_NEG**2)))),0,1*VARVAL(.template_5_turn_force.NLG_V)*0.5*(VARVAL(.template_5_turn_force.NLG_V)+ABS(VARVAL(.template_5_turn_force.NLG_V)))*((.template_5_turn_force.rho_Oil*.template_5_turn_force.NLG_A_MAIN_OIL**3/(2*.template_5_turn_force.NLG_MAIN_Cd**2*.template_5_turn_force.NLG_A_MAIN_POS**2))+(.template_5_turn_force.rho_Oil*.template_5_turn_force.NLG_A_RET_OIL**3/(2*.template_5_turn_force.NLG_RET_Cd**2*.template_5_turn_force.NLG_A_RET_POS**2))))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.NLG_STOP  &
   function = "IF(0.4286-DM(.template_5_turn_force.ges_upper_cylinder.MARKER_2,.template_5_turn_force.ges_lower_cylinder.MARKER_1) :1.0E+09*(0.4286-DM(.template_5_turn_force.ges_upper_cylinder.MARKER_2,.template_5_turn_force.ges_lower_cylinder.MARKER_1)), 0 , 0 )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.LMLG_AIR  &
   function = ".template_5_turn_force.MLG_Aa*(.template_5_turn_force.MLG_P0*(.template_5_turn_force.MLG_V0/(.template_5_turn_force.MLG_V0-.template_5_turn_force.MLG_Aa*VARVAL(.template_5_turn_force.LMLG_S)))**1.1-.template_5_turn_force.Patm)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.LMLG_OIL  &
   function = "IF(VARVAL(.template_5_turn_force.LMLG_V):2*-1*(VARVAL(.template_5_turn_force.LMLG_V)*0.5*(VARVAL(.template_5_turn_force.LMLG_V)-ABS(VARVAL(.template_5_turn_force.LMLG_V)))*((.template_5_turn_force.rho_Oil*.template_5_turn_force.MLG_A_MAIN_OIL**3/(2*.template_5_turn_force.MLG_MAIN_Cd**2*.template_5_turn_force.MLG_A_MAIN_NEG**2))+(.template_5_turn_force.rho_Oil*.template_5_turn_force.MLG_A_RET_OIL**3/(2*.template_5_turn_force.MLG_RET_Cd**2*.template_5_turn_force.MLG_A_RET_NEG**2)))),0,2*VARVAL(.template_5_turn_force.LMLG_V)*0.5*(VARVAL(.template_5_turn_force.LMLG_V)+ABS(VARVAL(.template_5_turn_force.LMLG_V)))*((.template_5_turn_force.rho_Oil*.template_5_turn_force.MLG_A_MAIN_OIL**3/(2*.template_5_turn_force.MLG_MAIN_Cd**2*.template_5_turn_force.MLG_A_MAIN_POS**2))+(.template_5_turn_force.rho_Oil*.template_5_turn_force.MLG_A_RET_OIL**3/(2*.template_5_turn_force.MLG_RET_Cd**2*.template_5_turn_force.MLG_A_RET_POS**2))))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.LMLG_STOP  &
   function = "IF(1.014262-DM(.template_5_turn_force.gel_upper_cylinder.MARKER_272,.template_5_turn_force.gel_lower_cylinder.MARKER_273) :1.0E+09*(1.014262-DM(.template_5_turn_force.gel_upper_cylinder.MARKER_272,.template_5_turn_force.gel_lower_cylinder.MARKER_273)) , 0 , 0 )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.RMLG_AIR  &
   function = ".template_5_turn_force.MLG_Aa*(.template_5_turn_force.MLG_P0*(.template_5_turn_force.MLG_V0/(.template_5_turn_force.MLG_V0-.template_5_turn_force.MLG_Aa*VARVAL(.template_5_turn_force.RMLG_S)))**1.1-.template_5_turn_force.Patm)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.RMLG_OIL  &
   function = "IF(VARVAL(.template_5_turn_force.RMLG_V):2*-1*(VARVAL(.template_5_turn_force.RMLG_V)*0.5*(VARVAL(.template_5_turn_force.RMLG_V)-ABS(VARVAL(.template_5_turn_force.RMLG_V)))*((.template_5_turn_force.rho_Oil*.template_5_turn_force.MLG_A_MAIN_OIL**3/(2*.template_5_turn_force.MLG_MAIN_Cd**2*.template_5_turn_force.MLG_A_MAIN_NEG**2))+(.template_5_turn_force.rho_Oil*.template_5_turn_force.MLG_A_RET_OIL**3/(2*.template_5_turn_force.MLG_RET_Cd**2*.template_5_turn_force.MLG_A_RET_NEG**2)))),0,2*VARVAL(.template_5_turn_force.RMLG_V)*0.5*(VARVAL(.template_5_turn_force.RMLG_V)+ABS(VARVAL(.template_5_turn_force.RMLG_V)))*((.template_5_turn_force.rho_Oil*.template_5_turn_force.MLG_A_MAIN_OIL**3/(2*.template_5_turn_force.MLG_MAIN_Cd**2*.template_5_turn_force.MLG_A_MAIN_POS**2))+(.template_5_turn_force.rho_Oil*.template_5_turn_force.MLG_A_RET_OIL**3/(2*.template_5_turn_force.MLG_RET_Cd**2*.template_5_turn_force.MLG_A_RET_POS**2))))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.RMLG_STOP  &
   function = "IF(1.014262-DM(.template_5_turn_force.ger_upper_cylinder.MARKER_278,.template_5_turn_force.ger_lower_cylinder.MARKER_279) :1.0E+09*(1.014262-DM(.template_5_turn_force.ger_upper_cylinder.MARKER_278,.template_5_turn_force.ger_lower_cylinder.MARKER_279)) , 0 ,0 )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.turning_force  &
   function = "step(time,.template_5_turn_force.T_1,0,.template_5_turn_force.T_2,1)*(500000/.template_5_turn_force.angle)*(.template_5_turn_force.angle+.template_5_turn_force.jiaodu)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.thrust  &
   function = "-300000*2/3.14*atan(.template_5_turn_force.V_sheding-.template_5_turn_force.jscm_sd)*step(time,3,0,3.5,1)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_5_turn_force.damping_force  &
   function = "-.template_5_turn_force.jsd*50"
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_turn_force.lumian
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai1
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai1_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai2_2
!
!------------------------- Part IC Reference Markers --------------------------!
!
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_turn_force.luntai1.wheel_part  &
   vm = .template_5_turn_force.luntai1.wheel_part.wheel_cm  &
   wm = .template_5_turn_force.luntai1.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_turn_force.luntai1.belt_part  &
   vm = .template_5_turn_force.luntai1.wheel_part.wheel_cm  &
   wm = .template_5_turn_force.luntai1.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_turn_force.luntai2.wheel_part  &
   vm = .template_5_turn_force.luntai2.wheel_part.wheel_cm  &
   wm = .template_5_turn_force.luntai2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_turn_force.luntai2.belt_part  &
   vm = .template_5_turn_force.luntai2.wheel_part.wheel_cm  &
   wm = .template_5_turn_force.luntai2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_turn_force.luntai1_2.wheel_part  &
   vm = .template_5_turn_force.luntai1_2.wheel_part.wheel_cm  &
   wm = .template_5_turn_force.luntai1_2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_turn_force.luntai1_2.belt_part  &
   vm = .template_5_turn_force.luntai1_2.wheel_part.wheel_cm  &
   wm = .template_5_turn_force.luntai1_2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_turn_force.luntai2_2.wheel_part  &
   vm = .template_5_turn_force.luntai2_2.wheel_part.wheel_cm  &
   wm = .template_5_turn_force.luntai2_2.wheel_part.wheel_cm
!
part modify rigid_body initial_velocity  &
   part_name = .template_5_turn_force.luntai2_2.belt_part  &
   vm = .template_5_turn_force.luntai2_2.wheel_part.wheel_cm  &
   wm = .template_5_turn_force.luntai2_2.wheel_part.wheel_cm
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.cfl_spin_axis_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({180.0, 180.0, 180.0}degrees, .template_5_turn_force.ground.cfl_spin_axis_1))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_spin_axis  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.cfr_spin_axis_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({-180.0, -180.0, -180.0}degrees, .template_5_turn_force.ground.cfr_spin_axis_1))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_axial_reference  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_lc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_lc_bot, .template_5_turn_force.ground.hpl_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_axial_reference  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_lc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_lc_bot, .template_5_turn_force.ground.hpr_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_uc_bot  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 21.18}inch, .template_5_turn_force.ground.cfl_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_uc_bot  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 21.18}inch, .template_5_turn_force.ground.cfr_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_uc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_uc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_lc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 38.06}inch, .template_5_turn_force.ground.cfl_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_lc_top  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 38.06}inch, .template_5_turn_force.ground.cfr_axial_reference))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_uta_uc_atch  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.cfl_uc_bot))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_uta_uc_atch  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.cfr_uc_bot))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_lta_lc_atch  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_lc_bot))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_lta_lc_atch  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_lc_bot))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpl_uc_top, .template_5_turn_force.ground.hpl_lc_bot, 0.59 * DM(.template_5_turn_force.ground.hpl_uc_top, .template_5_turn_force.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_uc_top, .template_5_turn_force.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpr_uc_top, .template_5_turn_force.ground.hpr_lc_bot, 0.59 * DM(.template_5_turn_force.ground.hpr_uc_top, .template_5_turn_force.ground.hpr_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_uc_top, .template_5_turn_force.ground.hpr_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_collar_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpl_uc_top, .template_5_turn_force.ground.hpl_lc_bot, 0.7 * DM(.template_5_turn_force.ground.hpl_uc_top, .template_5_turn_force.ground.hpl_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_uc_top, .template_5_turn_force.ground.hpl_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_collar_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpr_uc_top, .template_5_turn_force.ground.hpr_lc_bot, 0.7 * DM(.template_5_turn_force.ground.hpr_uc_top, .template_5_turn_force.ground.hpr_lc_bot)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_uc_top, .template_5_turn_force.ground.hpr_lc_bot, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_plane_ref_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.cfl_plane_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, -90.0, 0.0}degrees, .template_5_turn_force.ground.cfl_plane_ref))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_plane_ref_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.cfr_plane_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_5_turn_force.ground.cfr_plane_ref))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_lwract_top  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpl_lwract_uc_atch_1, .template_5_turn_force.ground.hpl_upract_sf_atch_1, 0.92 * DM(.template_5_turn_force.ground.hpl_lwract_uc_atch_1, .template_5_turn_force.ground.hpl_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_lwract_uc_atch_1, .template_5_turn_force.ground.hpl_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_lwract_top  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpr_lwract_uc_atch_1, .template_5_turn_force.ground.hpr_upract_sf_atch_1, 0.92 * DM(.template_5_turn_force.ground.hpr_lwract_uc_atch_1, .template_5_turn_force.ground.hpr_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_lwract_uc_atch_1, .template_5_turn_force.ground.hpr_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_upract_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpl_lwract_uc_atch_1, .template_5_turn_force.ground.hpl_upract_sf_atch_1, 0.4 * DM(.template_5_turn_force.ground.hpl_lwract_uc_atch_1, .template_5_turn_force.ground.hpl_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_lwract_uc_atch_1, .template_5_turn_force.ground.hpl_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_upract_bot  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpr_lwract_uc_atch_1, .template_5_turn_force.ground.hpr_upract_sf_atch_1, 0.4 * DM(.template_5_turn_force.ground.hpr_lwract_uc_atch_1, .template_5_turn_force.ground.hpr_upract_sf_atch_1)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_lwract_uc_atch_1, .template_5_turn_force.ground.hpr_upract_sf_atch_1, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_spin_axis_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_wheel_center, .template_5_turn_force.ground.hpl_ob_axle, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_spin_axis_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_wheel_center, .template_5_turn_force.ground.hpr_ob_axle, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_ldb_geompt_1  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpl_ldb_udb_atch_1, .template_5_turn_force.ground.hpl_ldb_collar_atch_1, 0.62 * DM(.template_5_turn_force.ground.hpl_ldb_udb_atch_1, .template_5_turn_force.ground.hpl_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_ldb_geompt_1  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpr_ldb_udb_atch_1, .template_5_turn_force.ground.hpr_ldb_collar_atch_1, 0.62 * DM(.template_5_turn_force.ground.hpr_ldb_udb_atch_1, .template_5_turn_force.ground.hpr_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_ldb_geompt_2  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpl_ldb_udb_atch_1, .template_5_turn_force.ground.hpl_ldb_collar_atch_1, 0.74 * DM(.template_5_turn_force.ground.hpl_ldb_udb_atch_1, .template_5_turn_force.ground.hpl_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_ldb_geompt_2  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hpr_ldb_udb_atch_1, .template_5_turn_force.ground.hpr_ldb_collar_atch_1, 0.74 * DM(.template_5_turn_force.ground.hpr_ldb_udb_atch_1, .template_5_turn_force.ground.hpr_ldb_collar_atch_1)))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_aero_ref  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_aero_ref  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_uc_top))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.uel_gearaero_origin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.origo))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.uel_gearaero_rm_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_aero_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_aero_ref))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.uer_gearaero_origin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.origo))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.origo))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.uer_gearaero_rm_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_aero_ref))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_aero_ref))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.lumian_ref_1  &
   location =   &
      (.template_5_turn_force.lumian.location)  &
   orientation =   &
      (.template_5_turn_force.lumian.orientation)
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfl_spin_axis1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_wheel_center1, .template_5_turn_force.ground.hpl_ob_axle1, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfr_spin_axis1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_wheel_center1, .template_5_turn_force.ground.hpr_ob_axle1, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfs_nlg_axle_lowpoint  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hps_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo1))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hps_uc_bot, .template_5_turn_force.ground.hps_uc_top, 0.11 * DM(.template_5_turn_force.ground.hps_uc_bot, .template_5_turn_force.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_uc_bot, .template_5_turn_force.ground.hps_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.zdt1  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.hsg_2, 0.6 * DM(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.hsg_2)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.hsg_2, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.ground.zdt2  &
   location =   &
      (LOC_ALONG_LINE(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.hsg_2, 0.9 * DM(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.hsg_2)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.hsg_2, "Z"))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_gearaero_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_lc_top))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_cylinder))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.gralin_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.cfl_uc_top, .template_5_turn_force.ground.cfl_uc_bot, "Z"))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.gralin_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_ib_uc_sf_atch, .template_5_turn_force.ground.hpl_uc_geompt, "Z"))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.gralin_20  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_ib_uc_sf_atch, .template_5_turn_force.ground.hpl_uc_top, "Z"))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_uc_top))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_uc_top))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_uc_top))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.jxl_joint_i_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lwract.jxl_joint_j_7))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lwract.jxl_joint_j_7))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.uel_actuator_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_uc_sf_atch))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_upper_cylinder.gralin_upper_cylinder  &
   length = (DM(.template_5_turn_force.ground.cfl_uc_top, .template_5_turn_force.ground.cfl_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_upper_cylinder.gralin_geom  &
   length = (DM(.template_5_turn_force.ground.hpl_ib_uc_sf_atch, .template_5_turn_force.ground.hpl_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_upper_cylinder.gralin_geom3  &
   length = (DM(.template_5_turn_force.ground.hpl_ib_uc_sf_atch, .template_5_turn_force.ground.hpl_uc_top))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_267  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_uc_top))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_cylinder.MARKER_446  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_uc_top))  &
   relative_to = .template_5_turn_force.gel_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_gearaero_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_lc_top))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_cylinder))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.gralin_13  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.cfr_uc_top, .template_5_turn_force.ground.cfr_uc_bot, "Z"))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.gralin_17  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_ib_uc_sf_atch, .template_5_turn_force.ground.hpr_uc_geompt, "Z"))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.gralin_21  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_ib_uc_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_ib_uc_sf_atch, .template_5_turn_force.ground.hpr_uc_top, "Z"))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_uc_top))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_uc_top))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_uc_top))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.jxr_joint_i_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lwract.jxr_joint_j_7))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lwract.jxr_joint_j_7))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.uer_actuator_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_uc_sf_atch))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_upper_cylinder.gralin_upper_cylinder  &
   length = (DM(.template_5_turn_force.ground.cfr_uc_top, .template_5_turn_force.ground.cfr_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_upper_cylinder.gralin_geom  &
   length = (DM(.template_5_turn_force.ground.hpr_ib_uc_sf_atch, .template_5_turn_force.ground.hpr_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_upper_cylinder.gralin_geom3  &
   length = (DM(.template_5_turn_force.ground.hpr_ib_uc_sf_atch, .template_5_turn_force.ground.hpr_uc_top))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_269  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_uc_top))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_cylinder.MARKER_444  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_uc_top))  &
   relative_to = .template_5_turn_force.ger_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lower_cylinder))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.gralin_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.cfl_lc_top, .template_5_turn_force.ground.hpl_lc_bot, "Z"))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.gralin_22  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_ib_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_ib_axle, .template_5_turn_force.ground.hpl_ob_axle, "Z"))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.jxl_joint_j_11  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_lta_connect_atch_1, .template_5_turn_force.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.jxl_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_12))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.coomarker_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_spin_axis))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_spin_axis))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.uel_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_lc_top))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.uel_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_lc_top))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.uel_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_lc_top))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_lower_cylinder.gralin_lower_cylinder  &
   length = (DM(.template_5_turn_force.ground.cfl_lc_top, .template_5_turn_force.ground.hpl_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_lower_cylinder.gralin_geom  &
   length = (DM(.template_5_turn_force.ground.hpl_ib_axle, .template_5_turn_force.ground.hpl_ob_axle))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_cylinder.MARKER_495  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_wheel_center))  &
   relative_to = .template_5_turn_force.gel_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lower_cylinder))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.gralin_15  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.cfr_lc_top, .template_5_turn_force.ground.hpr_lc_bot, "Z"))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.gralin_23  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_ib_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_ib_axle, .template_5_turn_force.ground.hpr_ob_axle, "Z"))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.jxr_joint_j_11  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_lta_connect_atch_1, .template_5_turn_force.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.jxr_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_12))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.coomarker_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_spin_axis))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_spin_axis))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.uer_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_lc_top))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.uer_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_lc_top))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.uer_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_lc_top))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_lower_cylinder.gralin_lower_cylinder  &
   length = (DM(.template_5_turn_force.ground.cfr_lc_top, .template_5_turn_force.ground.hpr_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_lower_cylinder.gralin_geom  &
   length = (DM(.template_5_turn_force.ground.hpr_ib_axle, .template_5_turn_force.ground.hpr_ob_axle))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_cylinder.MARKER_498  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_wheel_center))  &
   relative_to = .template_5_turn_force.ger_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_dragbrace))  &
   relative_to = .template_5_turn_force.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_udb_spndl_atch_1, .template_5_turn_force.ground.hpl_ldb_udb_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.jxl_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_5_turn_force.ground.cfl_plane_ref_2, "Z+Z"), .template_5_turn_force.gel_upper_dragbrace))  &
   relative_to = .template_5_turn_force.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.jxl_joint_i_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_spindle.jxl_joint_j_5))  &
   orientation =   &
      (ORI_IN_PLANE(.template_5_turn_force.gel_upper_dragbrace.jxl_joint_i_5, .template_5_turn_force.ground.hpl_ldb_udb_atch_1, .template_5_turn_force.ground.hpl_spndl_sf_atch, "Z_ZX"))  &
   relative_to = .template_5_turn_force.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_dragbrace.uel_actuator_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_ldb_udb_atch_1))  &
   relative_to = .template_5_turn_force.gel_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_upper_dragbrace.gralin_upper_dragbrace  &
   length = (DM(.template_5_turn_force.ground.hpl_udb_spndl_atch_1, .template_5_turn_force.ground.hpl_ldb_udb_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_dragbrace))  &
   relative_to = .template_5_turn_force.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.gralin_25  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_udb_spndl_atch_1, .template_5_turn_force.ground.hpr_ldb_udb_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.jxr_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_5_turn_force.ground.cfr_plane_ref_2, "Z+Z"), .template_5_turn_force.ger_upper_dragbrace))  &
   relative_to = .template_5_turn_force.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.jxr_joint_i_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_spindle.jxr_joint_j_5))  &
   orientation =   &
      (ORI_IN_PLANE(.template_5_turn_force.ger_upper_dragbrace.jxr_joint_i_5, .template_5_turn_force.ground.hpr_ldb_udb_atch_1, .template_5_turn_force.ground.hpr_spndl_sf_atch, "Z_ZX"))  &
   relative_to = .template_5_turn_force.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_dragbrace.uer_actuator_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_ldb_udb_atch_1))  &
   relative_to = .template_5_turn_force.ger_upper_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_upper_dragbrace.gralin_upper_dragbrace  &
   length = (DM(.template_5_turn_force.ground.hpr_udb_spndl_atch_1, .template_5_turn_force.ground.hpr_ldb_udb_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lower_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lower_dragbrace))  &
   relative_to = .template_5_turn_force.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.gralin_26  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_ldb_udb_atch_1, .template_5_turn_force.ground.hpl_ldb_collar_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.jxl_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_dragbrace.jxl_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_dragbrace.jxl_joint_j_14))  &
   relative_to = .template_5_turn_force.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.jxl_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_uc_collar.jxl_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_uc_collar.jxl_joint_j_10))  &
   relative_to = .template_5_turn_force.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_uplock_tab))  &
   orientation =   &
      (ORI_IN_PLANE(.template_5_turn_force.ground.hpl_uplock_tab, .template_5_turn_force.ground.cfl_ldb_geompt_1, .template_5_turn_force.ground.cfl_ldb_geompt_2, "X_XY"))  &
   relative_to = .template_5_turn_force.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_ldb_geompt_1))  &
   relative_to = .template_5_turn_force.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_dragbrace.graarm_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_ldb_geompt_2))  &
   relative_to = .template_5_turn_force.gel_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_lower_dragbrace.gralin_lower_dragbrace  &
   length = (DM(.template_5_turn_force.ground.hpl_ldb_udb_atch_1, .template_5_turn_force.ground.hpl_ldb_collar_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lower_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lower_dragbrace))  &
   relative_to = .template_5_turn_force.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.gralin_27  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_ldb_udb_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_ldb_udb_atch_1, .template_5_turn_force.ground.hpr_ldb_collar_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.jxr_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_dragbrace.jxr_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_dragbrace.jxr_joint_j_14))  &
   relative_to = .template_5_turn_force.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.jxr_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_uc_collar.jxr_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_uc_collar.jxr_joint_j_10))  &
   relative_to = .template_5_turn_force.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_uplock_tab))  &
   orientation =   &
      (ORI_IN_PLANE(.template_5_turn_force.ground.hpr_uplock_tab, .template_5_turn_force.ground.cfr_ldb_geompt_1, .template_5_turn_force.ground.cfr_ldb_geompt_2, "X_XY"))  &
   relative_to = .template_5_turn_force.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_ldb_geompt_1))  &
   relative_to = .template_5_turn_force.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_dragbrace.graarm_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_ldb_geompt_2))  &
   relative_to = .template_5_turn_force.ger_lower_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_lower_dragbrace.gralin_lower_dragbrace  &
   length = (DM(.template_5_turn_force.ground.hpr_ldb_udb_atch_1, .template_5_turn_force.ground.hpr_ldb_collar_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_torquearm))  &
   relative_to = .template_5_turn_force.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.gralin_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_uta_collar_atch_1, .template_5_turn_force.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.jxl_joint_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_connector.jxl_joint_j_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_connector.jxl_joint_j_2))  &
   relative_to = .template_5_turn_force.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upper_torquearm.jxl_joint_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_uc_collar.jxl_joint_j_3))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_uc_collar.jxl_joint_j_3))  &
   relative_to = .template_5_turn_force.gel_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_upper_torquearm.gralin_upper_torquearm  &
   length = (DM(.template_5_turn_force.ground.hpl_uta_collar_atch_1, .template_5_turn_force.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_torquearm))  &
   relative_to = .template_5_turn_force.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.gralin_28  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_uta_collar_atch_1, .template_5_turn_force.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.jxr_joint_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_connector.jxr_joint_j_2))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_connector.jxr_joint_j_2))  &
   relative_to = .template_5_turn_force.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upper_torquearm.jxr_joint_i_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_uc_collar.jxr_joint_j_3))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_uc_collar.jxr_joint_j_3))  &
   relative_to = .template_5_turn_force.ger_upper_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_upper_torquearm.gralin_upper_torquearm  &
   length = (DM(.template_5_turn_force.ground.hpr_uta_collar_atch_1, .template_5_turn_force.ground.hpr_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lower_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lower_torquearm))  &
   relative_to = .template_5_turn_force.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.gralin_29  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_lta_lc_atch_1, .template_5_turn_force.ground.hpl_lta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.jxl_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lower_cylinder.jxl_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lower_cylinder.jxl_joint_j_11))  &
   relative_to = .template_5_turn_force.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lower_torquearm.jxl_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_connector.jxl_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_connector.jxl_joint_j_1))  &
   relative_to = .template_5_turn_force.gel_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_lower_torquearm.gralin_lower_torquearm  &
   length = (DM(.template_5_turn_force.ground.hpl_lta_lc_atch_1, .template_5_turn_force.ground.hpl_lta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lower_torquearm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lower_torquearm))  &
   relative_to = .template_5_turn_force.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.gralin_30  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_lta_lc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_lta_lc_atch_1, .template_5_turn_force.ground.hpr_lta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.jxr_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lower_cylinder.jxr_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lower_cylinder.jxr_joint_j_11))  &
   relative_to = .template_5_turn_force.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lower_torquearm.jxr_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_connector.jxr_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_connector.jxr_joint_j_1))  &
   relative_to = .template_5_turn_force.ger_lower_torquearm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_lower_torquearm.gralin_lower_torquearm  &
   length = (DM(.template_5_turn_force.ground.hpr_lta_lc_atch_1, .template_5_turn_force.ground.hpr_lta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_connector.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_connector.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_connector))  &
   relative_to = .template_5_turn_force.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_connector.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_connect_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_connect_1, .template_5_turn_force.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_connector.jxl_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_lta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_lta_connect_atch_1, .template_5_turn_force.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_connector.jxl_joint_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_uta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_uta_connect_atch_1, .template_5_turn_force.ground.hpl_uta_connect_atch_2, "Z"))  &
   relative_to = .template_5_turn_force.gel_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_connector.gralin_connector  &
   length = (DM(.template_5_turn_force.ground.hpl_connect_1, .template_5_turn_force.ground.hpl_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_connector.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_connector.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_connector))  &
   relative_to = .template_5_turn_force.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_connector.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_connect_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_connect_1, .template_5_turn_force.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_connector.jxr_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_lta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_lta_connect_atch_1, .template_5_turn_force.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_connector.jxr_joint_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_uta_connect_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_uta_connect_atch_1, .template_5_turn_force.ground.hpr_uta_connect_atch_2, "Z"))  &
   relative_to = .template_5_turn_force.ger_connector
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_connector.gralin_connector  &
   length = (DM(.template_5_turn_force.ground.hpr_connect_1, .template_5_turn_force.ground.hpr_uta_connect_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_uc_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_uc_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_uc_collar))  &
   relative_to = .template_5_turn_force.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_uc_collar.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.cfl_collar_top, .template_5_turn_force.ground.cfl_collar_bot, "Z"))  &
   relative_to = .template_5_turn_force.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_lta_connect_atch_1, .template_5_turn_force.ground.hpl_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_4))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upper_cylinder.jxl_joint_j_4))  &
   relative_to = .template_5_turn_force.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_uc_collar.jxl_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_ldb_collar_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_5_turn_force.ground.cfl_plane_ref_2, "Z+Z"), .template_5_turn_force.gel_uc_collar))  &
   relative_to = .template_5_turn_force.gel_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_uc_collar.gralin_uc_collar  &
   length = (DM(.template_5_turn_force.ground.cfl_collar_top, .template_5_turn_force.ground.cfl_collar_bot))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_uc_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_uc_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_uc_collar))  &
   relative_to = .template_5_turn_force.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_uc_collar.gralin_6  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.cfr_collar_top, .template_5_turn_force.ground.cfr_collar_bot, "Z"))  &
   relative_to = .template_5_turn_force.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_j_3  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_uta_collar_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_lta_connect_atch_1, .template_5_turn_force.ground.hpr_uta_connect_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_4))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upper_cylinder.jxr_joint_j_4))  &
   relative_to = .template_5_turn_force.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_uc_collar.jxr_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_ldb_collar_atch_1))  &
   orientation =   &
      (ORI_LOCAL(ORI_ALIGN_AXIS(.template_5_turn_force.ground.cfr_plane_ref_2, "Z+Z"), .template_5_turn_force.ger_uc_collar))  &
   relative_to = .template_5_turn_force.ger_uc_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_uc_collar.gralin_uc_collar  &
   length = (DM(.template_5_turn_force.ground.cfr_collar_top, .template_5_turn_force.ground.cfr_collar_bot))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_spindle.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_spindle.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_spindle))  &
   relative_to = .template_5_turn_force.gel_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_spindle.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_spndl_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_spndl_sf_atch, .template_5_turn_force.ground.hpl_udb_spndl_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_spindle.jxl_joint_j_5  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_IN_PLANE(.template_5_turn_force.ground.hpl_spndl_sf_atch, .template_5_turn_force.gel_spindle.jxl_joint_j_5, .template_5_turn_force.ground.hpl_ldb_udb_atch_1, "Z_ZX"))  &
   relative_to = .template_5_turn_force.gel_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_spindle.gralin_spindle  &
   length = (DM(.template_5_turn_force.ground.hpl_spndl_sf_atch, .template_5_turn_force.ground.hpl_udb_spndl_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_spindle.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_spindle.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_spindle))  &
   relative_to = .template_5_turn_force.ger_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_spindle.gralin_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_spndl_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_spndl_sf_atch, .template_5_turn_force.ground.hpr_udb_spndl_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_spindle.jxr_joint_j_5  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_udb_spndl_atch_1))  &
   orientation =   &
      (ORI_IN_PLANE(.template_5_turn_force.ground.hpr_spndl_sf_atch, .template_5_turn_force.ger_spindle.jxr_joint_j_5, .template_5_turn_force.ground.hpr_ldb_udb_atch_1, "Z_ZX"))  &
   relative_to = .template_5_turn_force.ger_spindle
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_spindle.gralin_spindle  &
   length = (DM(.template_5_turn_force.ground.hpr_spndl_sf_atch, .template_5_turn_force.ground.hpr_udb_spndl_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lwract.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lwract.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lwract))  &
   relative_to = .template_5_turn_force.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lwract.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_lwract_uc_atch_1, .template_5_turn_force.ground.cfl_lwract_top, "Z"))  &
   relative_to = .template_5_turn_force.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lwract.jxl_joint_j_7  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))  &
   relative_to = .template_5_turn_force.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lwract.jxl_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upract.jxl_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upract.jxl_joint_j_8))  &
   relative_to = .template_5_turn_force.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lwract.uel_stopper_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_lwract_uc_atch_1))  &
   relative_to = .template_5_turn_force.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lwract.uel_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_lwract_uc_atch_1))  &
   relative_to = .template_5_turn_force.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_lwract.uel_actuator_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lwract.jxl_joint_i_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_lwract.jxl_joint_i_8))  &
   relative_to = .template_5_turn_force.gel_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_lwract.gralin_lwract  &
   length = (DM(.template_5_turn_force.ground.hpl_lwract_uc_atch_1, .template_5_turn_force.ground.cfl_lwract_top))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lwract.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lwract.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lwract))  &
   relative_to = .template_5_turn_force.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lwract.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_lwract_uc_atch_1, .template_5_turn_force.ground.cfr_lwract_top, "Z"))  &
   relative_to = .template_5_turn_force.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lwract.jxr_joint_j_7  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_lwract_uc_atch_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo))  &
   relative_to = .template_5_turn_force.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lwract.jxr_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upract.jxr_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upract.jxr_joint_j_8))  &
   relative_to = .template_5_turn_force.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lwract.uer_stopper_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_lwract_uc_atch_1))  &
   relative_to = .template_5_turn_force.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lwract.uer_actuator_i_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lwract.jxr_joint_i_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_lwract.jxr_joint_i_8))  &
   relative_to = .template_5_turn_force.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_lwract.uer_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_lwract_uc_atch_1))  &
   relative_to = .template_5_turn_force.ger_lwract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_lwract.gralin_lwract  &
   length = (DM(.template_5_turn_force.ground.hpr_lwract_uc_atch_1, .template_5_turn_force.ground.cfr_lwract_top))
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upract.uel_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_upract_sf_atch_1))  &
   relative_to = .template_5_turn_force.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upract.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upract.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upract))  &
   relative_to = .template_5_turn_force.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upract.gralin_18  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfl_upract_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.cfl_upract_bot, .template_5_turn_force.ground.hpl_upract_sf_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upract.jxl_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.cfl_lwract_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpl_lwract_uc_atch_1, .template_5_turn_force.ground.hpl_upract_sf_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upract.uel_stopper_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_upract_sf_atch_1))  &
   relative_to = .template_5_turn_force.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.gel_upract.uel_actuator_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upract.jxl_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.gel_upract.jxl_joint_j_8))  &
   relative_to = .template_5_turn_force.gel_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.gel_upract.gralin_upract  &
   length = (DM(.template_5_turn_force.ground.cfl_upract_bot, .template_5_turn_force.ground.hpl_upract_sf_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upract.uer_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_upract_sf_atch_1))  &
   relative_to = .template_5_turn_force.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upract.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upract.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upract))  &
   relative_to = .template_5_turn_force.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upract.gralin_19  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfr_upract_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.cfr_upract_bot, .template_5_turn_force.ground.hpr_upract_sf_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upract.jxr_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.cfr_lwract_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_lwract_uc_atch_1, .template_5_turn_force.ground.hpr_upract_sf_atch_1, "Z"))  &
   relative_to = .template_5_turn_force.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upract.uer_stopper_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_upract_sf_atch_1))  &
   relative_to = .template_5_turn_force.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ger_upract.uer_actuator_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upract.jxr_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ger_upract.jxr_joint_j_8))  &
   relative_to = .template_5_turn_force.ger_upract
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ger_upract.gralin_upract  &
   length = (DM(.template_5_turn_force.ground.cfr_upract_bot, .template_5_turn_force.ground.hpr_upract_sf_atch_1))
!
marker modify  &
   marker_name = .template_5_turn_force.luntai1.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_5_turn_force.luntai1.wheel_part.wheel_cm))  &
   relative_to = .template_5_turn_force.luntai1.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpr_wheel_center))
!
marker modify  &
   marker_name = .template_5_turn_force.luntai2.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_5_turn_force.luntai2.wheel_part.wheel_cm))  &
   relative_to = .template_5_turn_force.luntai2.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai2  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hpl_wheel_center))
!
material modify  &
   material_name = .template_5_turn_force.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_5_turn_force.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_5_turn_force.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .template_5_turn_force.ges_dragbrace.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_dragbrace.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_dragbrace))  &
   relative_to = .template_5_turn_force.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_dragbrace.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_db_sf_atch, .template_5_turn_force.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .template_5_turn_force.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_dragbrace.jxs_joint_i_12  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_12))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_12))  &
   relative_to = .template_5_turn_force.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_dragbrace.gralin_dragbrace_geom  &
   length = (DM(.template_5_turn_force.ground.hps_db_sf_atch, .template_5_turn_force.ground.hps_db_uc_atch))
!
marker modify  &
   marker_name = .template_5_turn_force.ges_dragbrace.MARKER_491  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_db_sf_atch))  &
   relative_to = .template_5_turn_force.ges_dragbrace
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_uc_top, .template_5_turn_force.ground.hps_uc_bot, "Z"))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_uc_sf_atch_l, .template_5_turn_force.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_uc_sf_atch_r, .template_5_turn_force.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_12  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hps_db_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_5_turn_force.ground.origo1))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_spring_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_uc_top))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_damper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_uc_top))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_stopper_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_uc_top))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_uc_bot, .template_5_turn_force.ground.hps_uc_top, "Z"))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_actuator_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.ues_actuator_j_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.template_5_turn_force.ground.hps_uc_top, .template_5_turn_force.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.template_5_turn_force.ground.hps_uc_sf_atch_l, .template_5_turn_force.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.template_5_turn_force.ground.hps_uc_sf_atch_r, .template_5_turn_force.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_cylinder.MARKER_467  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.zdt1))  &
   relative_to = .template_5_turn_force.ges_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_lower_cylinder.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_lower_cylinder))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_lc_top, .template_5_turn_force.ground.hps_lc_bot, "Z"))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_wheel_center1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hpr_wheel_center1, .template_5_turn_force.ground.hpl_wheel_center1, "Z"))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.ues_spring_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_lc_top))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.ues_damper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_lc_top))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.ues_stopper_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_lc_top))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.coomarker_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfs_wheel_centers_midpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfs_wheel_centers_midpoint))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.coomarker_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfs_nlg_axle_lowpoint))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.cfs_nlg_axle_lowpoint))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_wheel_center1))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_wheel_center1))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_lower_cylinder.gralin_geom1  &
   length = (DM(.template_5_turn_force.ground.hps_lc_top, .template_5_turn_force.ground.hps_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_lower_cylinder.gralin_geom2  &
   length = (DM(.template_5_turn_force.ground.hpr_wheel_center1, .template_5_turn_force.ground.hpl_wheel_center1))
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_cylinder.MARKER_378  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_lta_lc_atch))  &
   relative_to = .template_5_turn_force.ges_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_torque_arm))  &
   relative_to = .template_5_turn_force.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_uta_uc_atch, .template_5_turn_force.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_5_turn_force.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.jxs_joint_j_8  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hps_lta_uta_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_5_turn_force.ground.origo1))  &
   relative_to = .template_5_turn_force.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_upper_torque_arm.jxs_joint_i_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_collar.jxs_joint_j_10))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_collar.jxs_joint_j_10))  &
   relative_to = .template_5_turn_force.ges_upper_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_upper_torque_arm.gralin_upper_torque_arm_geom  &
   length = (DM(.template_5_turn_force.ground.hps_uta_uc_atch, .template_5_turn_force.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_lower_torque_arm.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_lower_torque_arm))  &
   relative_to = .template_5_turn_force.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.jxs_joint_i_8  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_torque_arm.jxs_joint_j_8))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_torque_arm.jxs_joint_j_8))  &
   relative_to = .template_5_turn_force.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_lta_lc_atch, .template_5_turn_force.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_5_turn_force.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_lower_torque_arm.gralin_lower_torque_arm_geom  &
   length = (DM(.template_5_turn_force.ground.hps_lta_lc_atch, .template_5_turn_force.ground.hps_lta_uta_atch))
!
marker modify  &
   marker_name = .template_5_turn_force.ges_lower_torque_arm.MARKER_379  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_lta_lc_atch))  &
   relative_to = .template_5_turn_force.ges_lower_torque_arm
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_collar.jxs_joint_j_10  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_5_turn_force.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_5_turn_force.ground.origo1))  &
   relative_to = .template_5_turn_force.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_collar.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_collar.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_collar))  &
   relative_to = .template_5_turn_force.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_collar.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hps_uc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hps_uc_bot, .template_5_turn_force.ground.cfs_collar_top, "Z"))  &
   relative_to = .template_5_turn_force.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_5_turn_force.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_collar.ues_actuator_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_5_turn_force.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.ges_collar.ues_actuator_i_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_collar.jxs_joint_i_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ges_collar.jxs_joint_i_1))  &
   relative_to = .template_5_turn_force.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.ges_collar.gralin_collar  &
   length = (DM(.template_5_turn_force.ground.hps_uc_bot, .template_5_turn_force.ground.cfs_collar_top))
!
marker modify  &
   marker_name = .template_5_turn_force.ges_collar.MARKER_465  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hsg_1))  &
   relative_to = .template_5_turn_force.ges_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.luntai1_2.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_5_turn_force.luntai1_2.wheel_part.wheel_cm))  &
   relative_to = .template_5_turn_force.luntai1_2.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai1_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_wheel_center1))
!
marker modify  &
   marker_name = .template_5_turn_force.luntai2_2.wheel_part.gfo_i  &
   orientation =   &
      (ORI_RELATIVE_TO({0d, 270d, 0d}, .template_5_turn_force.luntai2_2.wheel_part.wheel_cm))  &
   relative_to = .template_5_turn_force.luntai2_2.wheel_part
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
ude modify instance  &
   instance_name = .template_5_turn_force.luntai2_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_wheel_center1))
!
geometry modify shape ellipsoid  &
   ellipsoid_name = .template_5_turn_force.js.ELLIPSOID_156  &
   x_scale_factor = (2 * 10.0cm)  &
   y_scale_factor = (2 * 10.0cm)  &
   z_scale_factor = (2 * 10.0cm)
!
marker modify  &
   marker_name = .template_5_turn_force.js.MARKER_443  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpr_uc_top))  &
   relative_to = .template_5_turn_force.js
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.js.MARKER_445  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hpl_uc_top))  &
   relative_to = .template_5_turn_force.js
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape force  &
   force_name = .template_5_turn_force.NLG_OIL_force_graphic_2  &
   applied_at_marker_name = (.template_5_turn_force.NLG_OIL.j)
!
marker modify  &
   marker_name = .template_5_turn_force.hsg.gralin_463  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hsg_1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.hsg_2, "Z"))  &
   relative_to = .template_5_turn_force.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.hsg.CYLINDER_213  &
   length = (DM(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.hsg_2))  &
   radius = (2.2E-02meter)
!
marker modify  &
   marker_name = .template_5_turn_force.hsg.MARKER_466  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.hsg_1))  &
   relative_to = .template_5_turn_force.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.hsg.MARKER_469  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.zdt.cm))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.zdt1, "Z"))  &
   relative_to = .template_5_turn_force.hsg
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.zdt.gralin_464  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.zdt1))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.zdt1, .template_5_turn_force.ground.zdt2, "Z"))  &
   relative_to = .template_5_turn_force.zdt
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_5_turn_force.zdt.CYLINDER_214  &
   length = (DM(.template_5_turn_force.ground.zdt1, .template_5_turn_force.ground.zdt2))  &
   radius = (4.2E-02meter)
!
marker modify  &
   marker_name = .template_5_turn_force.zdt.MARKER_468  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.ground.zdt1))  &
   relative_to = .template_5_turn_force.zdt
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
marker modify  &
   marker_name = .template_5_turn_force.zdt.MARKER_470  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_5_turn_force.zdt.cm))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_5_turn_force.ground.hsg_1, .template_5_turn_force.ground.zdt1, "Z"))  &
   relative_to = .template_5_turn_force.zdt
!
defaults coordinate_system  &
   default_coordinate_system = .template_5_turn_force.ground
!
material modify  &
   material_name = .template_5_turn_force.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
geometry modify shape force  &
   force_name = .template_5_turn_force.SFORCE_22_force_graphic_1  &
   applied_at_marker_name = (.template_5_turn_force.turning_force.i)
!
geometry modify shape force  &
   force_name = .template_5_turn_force.SFORCE_23_force_graphic_1  &
   applied_at_marker_name = (.template_5_turn_force.thrust.i)
!
geometry modify shape force  &
   force_name = .template_5_turn_force.SFORCE_24_force_graphic_1  &
   applied_at_marker_name = (.template_5_turn_force.damping_force.i)
!
model display  &
   model_name = template_5_turn_force

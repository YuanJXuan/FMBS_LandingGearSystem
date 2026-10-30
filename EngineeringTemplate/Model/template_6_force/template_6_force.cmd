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
!-------------------------------- Data storage --------------------------------!
!
!
data_element create spline  &
   spline_name = .template_6_force.SPLINE_angle_aeroforce  &
   adams_id = 1  &
   x = -20.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0,  &
       90.0, 100.0, 110.0, 120.0  &
   y = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,  &
       0.0  &
   linear_extrapolate = no
!
!--------------------------------- Materials ----------------------------------!
!
!
material create  &
   material_name = .template_6_force.steel  &
   adams_id = 39  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum  &
   adams_id = 3  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_2  &
   adams_id = 1  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_2  &
   adams_id = 4  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_3  &
   adams_id = 6  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_3  &
   adams_id = 7  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_2_2  &
   adams_id = 8  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_2_2  &
   adams_id = 9  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_3_2  &
   adams_id = 10  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_3_2  &
   adams_id = 11  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_2_2_2  &
   adams_id = 12  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_2_2_2  &
   adams_id = 13  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_4  &
   adams_id = 27  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_4  &
   adams_id = 28  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_2_3  &
   adams_id = 29  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_2_3  &
   adams_id = 30  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_3_3  &
   adams_id = 31  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_3_3  &
   adams_id = 32  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_2_2_3  &
   adams_id = 33  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_2_2_3  &
   adams_id = 34  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_3_2_2  &
   adams_id = 35  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_3_2_2  &
   adams_id = 36  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_2_2_2_2  &
   adams_id = 37  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_2_2_2_2  &
   adams_id = 38  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_4_2  &
   adams_id = 15  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_4_2  &
   adams_id = 16  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_2_3_2  &
   adams_id = 17  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_2_3_2  &
   adams_id = 18  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_3_3_2  &
   adams_id = 19  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_3_3_2  &
   adams_id = 20  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_2_2_3_2  &
   adams_id = 21  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_2_2_3_2  &
   adams_id = 22  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_3_2_2_2  &
   adams_id = 23  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_3_2_2_2  &
   adams_id = 24  &
   density = 2.74E-06  &
   youngs_modulus = 7.1705E+04  &
   poissons_ratio = 0.33
!
material create  &
   material_name = .template_6_force.steel_2_2_2_2_2  &
   adams_id = 25  &
   density = 7.801E-06  &
   youngs_modulus = 2.07E+05  &
   poissons_ratio = 0.29
!
material create  &
   material_name = .template_6_force.aluminum_2_2_2_2_2  &
   adams_id = 26  &
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
   default_coordinate_system = .template_6_force.ground
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.ground.origo  &
   adams_id = 10  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.origo  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.cfs_subframe_to_body_point  &
   adams_id = 13  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
marker attributes  &
   marker_name = .template_6_force.ground.cfs_subframe_to_body_point  &
   color = MAIZE  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.mts_mount_j_2  &
   adams_id = 14  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.mts_mount_j_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.cfs_collar_top  &
   adams_id = 19  &
   location = 6197.6, 0.0, 856.996  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.cfs_collar_top  &
   color = MAIZE  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_996  &
   adams_id = 996  &
   location = 5167.8134765644, -2.0856155039E-10, 1931.4468383829  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_996  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1104  &
   adams_id = 1104  &
   location = 5184.8134765625, 0.0, 1945.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1104  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1031  &
   adams_id = 1031  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1031  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1049  &
   adams_id = 1049  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1049  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1070  &
   adams_id = 1070  &
   location = 5167.8134765644, -2.0856155039E-10, 1931.4468383829  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1070  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1116  &
   adams_id = 1116  &
   location = 5202.8134765625, 0.0, 1981.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1116  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1310  &
   adams_id = 1310  &
   location = 1.0337216477E+04, -617.9999999999, 1755.4468383787  &
   orientation = 270.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1310  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1313  &
   adams_id = 1313  &
   location = 1.0337340597E+04, -1639.0607744, 1652.406081799  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1313  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1335  &
   adams_id = 1335  &
   location = 1.0337216477E+04, -596.0000000019, 1741.4468383829  &
   orientation = 89.9999999082d, 90.0000001904d, 58.2679219728d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1335  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1330  &
   adams_id = 1330  &
   location = 1.0337216477E+04, -531.0, 1791.4468383789  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1330  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1470  &
   adams_id = 1470  &
   location = 9537.340597, 1639.0607744, 1652.406081799  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1470  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_1485  &
   adams_id = 1485  &
   location = 9537.340597, -1639.0607744, 1652.406081799  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_1485  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_9962  &
   adams_id = 1487  &
   location = 1.0337216477E+04, -596.0, 1741.4468383789  &
   orientation = 90.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_9962  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_10312  &
   adams_id = 1488  &
   location = 1.0337216477E+04, -555.127351812, 1772.3668617453  &
   orientation = 90.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_10312  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_10492  &
   adams_id = 1489  &
   location = 1.0337216477E+04, -555.127351812, 1772.3668617453  &
   orientation = 90.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_10492  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_13101  &
   adams_id = 1341  &
   location = 1.0337464717E+04, 617.9999999999, 1755.4468383787  &
   orientation = 90.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_13101  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_13131  &
   adams_id = 1343  &
   location = 1.0337340597E+04, 1639.0607744, 1652.406081799  &
   orientation = 90.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_13131  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_13351  &
   adams_id = 1344  &
   location = 1.0337464717E+04, 596.0, 1741.4468383789  &
   orientation = 269.9999999082d, 90.0000001904d, 58.2679219728d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_13351  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_13301  &
   adams_id = 1345  &
   location = 1.0337464717E+04, 531.0, 1791.4468383789  &
   orientation = 90.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_13301  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_9961  &
   adams_id = 1346  &
   location = 1.0337464717E+04, 596.0, 1741.4468383789  &
   orientation = 270.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_9961  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_10311  &
   adams_id = 1347  &
   location = 1.0337464717E+04, 555.127351812, 1772.3668617453  &
   orientation = 270.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_10311  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_10491  &
   adams_id = 1348  &
   location = 1.0337464717E+04, 555.127351812, 1772.3668617453  &
   orientation = 270.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_10491  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_5791  &
   adams_id = 1354  &
   location = 1.0487340597E+04, 739.0607744005, 1752.406081798  &
   orientation = 90.0d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_5791  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_5671  &
   adams_id = 1355  &
   location = 1.0337340597E+04, 1639.0607744, 1652.406081799  &
   orientation = 90.0d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_5671  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_579  &
   adams_id = 579  &
   location = 1.0487340597E+04, -739.0607744005, 1752.406081798  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_579  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.ground.MARKER_567  &
   adams_id = 567  &
   location = 1.0337340597E+04, -1639.0607744, 1652.406081799  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.ground.MARKER_567  &
   size_of_icons = 25.0
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uel_gearaero_jfloat_11  &
   adams_id = 699
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uel_gearaero_jfloat_1  &
   adams_id = 175
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uer_gearaero_jfloat_1  &
   adams_id = 176
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uer_gearaero_jfloat_11  &
   adams_id = 700
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uel_gearaero_jfloat_112  &
   adams_id = 1493
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uel_gearaero_jfloat_13  &
   adams_id = 1494
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uer_gearaero_jfloat_13  &
   adams_id = 1495
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uer_gearaero_jfloat_112  &
   adams_id = 1496
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uel_gearaero_jfloat_111  &
   adams_id = 1360
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uel_gearaero_jfloat_12  &
   adams_id = 1361
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uer_gearaero_jfloat_12  &
   adams_id = 1362
!
floating_marker create  &
   floating_marker_name = .template_6_force.ground.uer_gearaero_jfloat_111  &
   adams_id = 1363
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
!------------------------------ nlg_suo_liangan -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_suo_liangan  &
   adams_id = 178  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_suo_liangan
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1373  &
   adams_id = 1373  &
   location = 5127.6041601028, 0.0, 1924.5997322579  &
   orientation = 0.2912774787d, 90.7341157487d, 1.4589947341d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1373  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1374  &
   adams_id = 1374  &
   location = 5098.8134765625, 0.0, 1911.4468383789  &
   orientation = 0.2912774787d, 90.7341157487d, 1.4589947341d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1374  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1375  &
   adams_id = 1375  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 0.2912774787d, 90.7341157487d, 1.4589947341d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1375  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_liangan.cm  &
   adams_id = 1025  &
   location = 5109.6519184774, -0.1336109756, 1927.9044592846  &
   orientation = 99.2819384265d, 175.3125934819d, 9.0203369998d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_liangan.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1029  &
   adams_id = 1029  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1029  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1006  &
   adams_id = 1006  &
   location = 5127.6041601028, 0.0, 1924.5997322579  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1006  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1382  &
   adams_id = 1382  &
   location = 5098.8134765625, -8.0, 1911.4468383789  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1382  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1384  &
   adams_id = 1384  &
   location = 5098.8134765625, 8.0, 1911.4468383789  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1384  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_suo_liangan  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape plate  &
   plate_name = .template_6_force.nlg_suo_liangan.PLATE_647  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1373,  &
                 .template_6_force.nlg_suo_liangan.MARKER_1374,  &
                 .template_6_force.nlg_suo_liangan.MARKER_1375  &
   width = 15.0  &
   radius = 2.0
!
part attributes  &
   part_name = .template_6_force.nlg_suo_liangan  &
   color = MAIZE  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------ nlg_sf_actuator -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_sf_actuator  &
   adams_id = 7  &
   location = 6967.855, 0.0, 1319.53  &
   orientation = 270.0d, 120.4532239091d, 90.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_sf_actuator
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_sf_actuator.cm  &
   adams_id = 21  &
   location = -4.58524116E-10, 0.0, 0.0  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_actuator.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_actuator.gralin_1  &
   adams_id = 23  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_actuator.gralin_1  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_actuator.jxs_joint_i_14  &
   adams_id = 24  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 0.0d, 90.0d, 239.5467760909d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_actuator.jxs_joint_i_14  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_actuator.MARKER_85  &
   adams_id = 85  &
   location = 1.3451462166E-09, 0.0, 158.8736811071  &
   orientation = 90.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_actuator.MARKER_85  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_actuator.MARKER_97  &
   adams_id = 97  &
   location = -4.5918824298E-10, 0.0, -598.873681109  &
   orientation = 90.0d, 120.4532239091d, 270.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_actuator.MARKER_97  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_actuator.MARKER_512  &
   adams_id = 512  &
   location = -4.4586556669E-10, 0.0, 3.108624469E-11  &
   orientation = 90.0d, 120.4532239091d, 270.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_actuator.MARKER_512  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_actuator.MARKER_532  &
   adams_id = 532  &
   location = -4.5852210917E-10, 0.0, -598.873681109  &
   orientation = 180.0d, 89.9999999993d, 300.4532239097d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_actuator.MARKER_532  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_sf_actuator  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_sf_actuator.gralin_dragbrace_geom  &
   adams_id = 32  &
   center_marker = .template_6_force.nlg_sf_actuator.gralin_1  &
   angle_extent = 360.0  &
   length = 1197.7473622179  &
   radius = 50.8  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_sf_actuator.gralin_dragbrace_geom  &
   color = PEACH
!
part attributes  &
   part_name = .template_6_force.nlg_sf_actuator  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!----------------------------- nlg_upper_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_upper_cylinder  &
   adams_id = 8  &
   location = 6197.6, 0.0, 1193.8  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_upper_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.MARKER_4  &
   adams_id = 4  &
   location = -236.7591354821, 0.0, 187.9366952496  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.MARKER_4  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.cm  &
   adams_id = 25  &
   location = -2.1926640514, 0.0, -14.5859826029  &
   orientation = 90.0d, 0.8375931978d, 270.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.gralin_2  &
   adams_id = 27  &
   location = 0.0, 0.0, -431.8  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.gralin_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.gralin_3  &
   adams_id = 28  &
   location = -116.84, -340.36, -497.84  &
   orientation = 161.0534953105d, 58.7414044414d, 213.4869581747d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.gralin_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.gralin_4  &
   adams_id = 29  &
   location = -116.84, 340.36, -497.84  &
   orientation = 18.9465046895d, 58.7414044414d, 326.5130418253d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.gralin_4  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.jxs_joint_j_11  &
   adams_id = 30  &
   location = 0.0, 0.0, 114.3  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.jxs_joint_j_11  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.MARKER_516  &
   adams_id = 516  &
   location = -116.84, 0.0, -497.84  &
   orientation = 179.9999999994d, 89.9999999997d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.MARKER_516  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.jxs_joint_j_1  &
   adams_id = 35  &
   location = 0.0, 0.0, 336.804  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.jxs_joint_j_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.MARKER_526  &
   adams_id = 526  &
   location = -116.84, 0.0, -497.84  &
   orientation = 179.9999999994d, 89.9999999997d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.MARKER_526  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_upper_cylinder.MARKER_781  &
   adams_id = 781  &
   location = -3.3167643494, 3.3852562994E-11, -13.3824231157  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_upper_cylinder.MARKER_781  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_upper_cylinder  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom1  &
   adams_id = 33  &
   center_marker = .template_6_force.nlg_upper_cylinder.gralin_2  &
   angle_extent = 360.0  &
   length = 863.6  &
   radius = 127.0  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom1  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom2  &
   adams_id = 34  &
   center_marker = .template_6_force.nlg_upper_cylinder.gralin_3  &
   angle_extent = 360.0  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom2  &
   color = DARK_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom3  &
   adams_id = 35  &
   center_marker = .template_6_force.nlg_upper_cylinder.gralin_4  &
   angle_extent = 360.0000000012  &
   length = 420.9662086201  &
   radius = 25.4  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom3  &
   color = DARK_GRAY
!
part attributes  &
   part_name = .template_6_force.nlg_upper_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!----------------------------- nlg_lower_cylinder -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_lower_cylinder  &
   adams_id = 9  &
   location = 6197.6, 0.0, 952.5  &
   orientation = 180.0d, 180.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_lower_cylinder
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.cm  &
   adams_id = 38  &
   location = -10.4138885641, 0.0, 112.8955994241  &
   orientation = 270.0d, 2.0209046446d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_5  &
   adams_id = 40  &
   location = 0.0, 0.0, -444.5  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_5  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.jxs_joint_i_11  &
   adams_id = 42  &
   location = 0.0, 0.0, -127.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.jxs_joint_i_11  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_7  &
   adams_id = 43  &
   location = -31.496, 209.55, 444.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_7  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_9  &
   adams_id = 51  &
   location = -127.0, 0.0, 114.3  &
   orientation = 270.0d, 68.9624889746d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_9  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_10  &
   adams_id = 57  &
   location = -101.6, 0.0, 419.1  &
   orientation = 270.0d, 116.5650511771d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_10  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_359  &
   adams_id = 359  &
   location = 81.549, 50.0, 367.076  &
   orientation = 90.0d, 90.0d, 270.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_359  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_360  &
   adams_id = 360  &
   location = 81.549, -50.0, 367.076  &
   orientation = 90.0d, 90.0d, 270.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_360  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_361  &
   adams_id = 361  &
   location = 146.549, -50.0, 367.076  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_361  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_782  &
   adams_id = 782  &
   location = -3.3167643494, 3.3882113721E-11, -254.6824231157  &
   orientation = 180.0d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_782  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_436  &
   adams_id = 436  &
   location = 146.549, 0.0, 367.076  &
   orientation = 56.6067815944d, 108.7094912792d, 176.556099572d
!
marker attributes  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_436  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_1562  &
   adams_id = 1562  &
   location = -31.496, -285.75, 444.5  &
   orientation = 180.0d, 90.0d, 180.0d
!
marker create  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_1563  &
   adams_id = 1563  &
   location = -31.496, 285.75, 444.5  &
   orientation = 0.0d, 90.0d, 0.0d
!
! ****** Floating Markers for current part ******
!
floating_marker create  &
   floating_marker_name = .template_6_force.nlg_lower_cylinder.FMARKER_783  &
   adams_id = 783
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_lower_cylinder  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.gralin_geom1  &
   adams_id = 36  &
   center_marker = .template_6_force.nlg_lower_cylinder.gralin_5  &
   angle_extent = 360.0  &
   length = 889.0  &
   radius = 101.6  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_lower_cylinder.gralin_geom1  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.gralin_geom2  &
   adams_id = 37  &
   center_marker = .template_6_force.nlg_lower_cylinder.gralin_7  &
   angle_extent = 360.0  &
   length = 419.1  &
   radius = 30.48  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_lower_cylinder.gralin_geom2  &
   color = BLUE_GRAY
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.CYLINDER_128  &
   adams_id = 128  &
   center_marker = .template_6_force.nlg_lower_cylinder.MARKER_359  &
   angle_extent = 360.0000000012  &
   length = 73.0  &
   radius = 8.125  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.CYLINDER_132  &
   adams_id = 132  &
   center_marker = .template_6_force.nlg_lower_cylinder.MARKER_360  &
   angle_extent = 360.0000000012  &
   length = 73.0  &
   radius = 8.125  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.CYLINDER_136  &
   adams_id = 136  &
   center_marker = .template_6_force.nlg_lower_cylinder.MARKER_361  &
   angle_extent = 360.0000000012  &
   length = 100.0  &
   radius = 7.5  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_6_force.nlg_lower_cylinder.suo_qiu  &
   adams_id = 164  &
   center_marker = .template_6_force.nlg_lower_cylinder.MARKER_436  &
   x_scale_factor = 12.8  &
   y_scale_factor = 12.8  &
   z_scale_factor = 12.8
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.gralin_lower_torque_arm_geom  &
   adams_id = 39  &
   center_marker = .template_6_force.nlg_lower_cylinder.gralin_10  &
   angle_extent = 360.0  &
   length = 397.5728863995  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_lower_cylinder.gralin_lower_torque_arm_geom  &
   color = MAGENTA
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.gralin_upper_torque_arm_geom  &
   adams_id = 38  &
   center_marker = .template_6_force.nlg_lower_cylinder.gralin_9  &
   angle_extent = 360.0  &
   length = 353.7810622405  &
   radius = 12.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_lower_cylinder.gralin_upper_torque_arm_geom  &
   color = GREEN
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.CYLINDER_861  &
   adams_id = 861  &
   center_marker = .template_6_force.nlg_lower_cylinder.MARKER_1562  &
   angle_extent = 360.0  &
   length = 90.0  &
   radius = 120.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.CYLINDER_882  &
   adams_id = 882  &
   center_marker = .template_6_force.nlg_lower_cylinder.MARKER_1563  &
   angle_extent = 360.0  &
   length = 90.0  &
   radius = 120.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.nlg_lower_cylinder  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!------------------------------- nlg_suo_yaobi --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_suo_yaobi  &
   adams_id = 179  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_suo_yaobi
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1026  &
   adams_id = 1026  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 148.2679219719d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1026  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1027  &
   adams_id = 1027  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 148.2679219719d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1027  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_yaobi.cm  &
   adams_id = 1047  &
   location = 5115.1636285173, -1.0559664715E-09, 1954.4435861482  &
   orientation = 90.0000000159d, 58.2679219732d, 359.9999998764d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_yaobi.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1028  &
   adams_id = 1028  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1028  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1030  &
   adams_id = 1030  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1030  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1048  &
   adams_id = 1048  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1048  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1372  &
   adams_id = 1372  &
   location = 5126.6611975793, -5.0, 1958.6666746361  &
   orientation = 179.9999999032d, 90.0000001951d, 58.2679219716d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1372  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1566  &
   adams_id = 1566  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1566  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_suo_yaobi  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape block  &
   block_name = .template_6_force.nlg_suo_yaobi.BOX_632  &
   adams_id = 632  &
   corner_marker = .template_6_force.nlg_suo_yaobi.MARKER_1372  &
   diag_corner_coords = -3.0, -24.0, 10.0
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_suo_yaobi.BOX_632  &
   color = YELLOW
!
geometry create shape link  &
   link_name = .template_6_force.nlg_suo_yaobi.LINK_483  &
   i_marker = .template_6_force.nlg_suo_yaobi.MARKER_1026  &
   j_marker = .template_6_force.nlg_suo_yaobi.MARKER_1027  &
   width = 12.5  &
   depth = 11.0
!
part attributes  &
   part_name = .template_6_force.nlg_suo_yaobi  &
   color = MAGENTA  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!-------------------------------- nlg_suo_rod ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_suo_rod  &
   adams_id = 180  &
   location = -15.0, 0.0, -2.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_suo_rod
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1097  &
   adams_id = 1097  &
   location = 5147.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1097  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1101  &
   adams_id = 1101  &
   location = 5149.8134765625, 7.4791382279E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1101  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1099  &
   adams_id = 1099  &
   location = 5147.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1099  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1050  &
   adams_id = 1050  &
   location = 5134.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1050  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod.cm  &
   adams_id = 1068  &
   location = 5149.8134765625, 7.6505528345E-11, 1947.4468383788  &
   orientation = 90.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1075  &
   adams_id = 1075  &
   location = 5134.8134765625, 0.0, 1947.4468383789  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1075  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1076  &
   adams_id = 1076  &
   location = 5164.8134765625, 1.2758529918E-10, 1947.4468383788  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod.MARKER_1076  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_suo_rod  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_6_force.nlg_suo_rod.nlg_suo_rod_n  &
   adams_id = 492  &
   center_marker = .template_6_force.nlg_suo_rod.MARKER_1050  &
   x_scale_factor = 3.6  &
   y_scale_factor = 3.6  &
   z_scale_factor = 3.6
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_suo_rod.CYLINDER_499  &
   adams_id = 499  &
   center_marker = .template_6_force.nlg_suo_rod.MARKER_1075  &
   angle_extent = 360.0000000012  &
   length = 30.0  &
   radius = 1.8  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_6_force.nlg_suo_rod.ELLIPSOID_500  &
   adams_id = 506  &
   center_marker = .template_6_force.nlg_suo_rod.MARKER_1076  &
   x_scale_factor = 3.6  &
   y_scale_factor = 3.6  &
   z_scale_factor = 3.6
!
part attributes  &
   part_name = .template_6_force.nlg_suo_rod  &
   color = RED  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!-------------------------------- nlg_subframe --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_subframe  &
   adams_id = 12  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 90.0d, 356.6444799092d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_subframe
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.MARKER_517  &
   adams_id = 517  &
   location = -390.5595878992, 5.906386491E-11, 0.0  &
   orientation = 3.3555200902d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.MARKER_517  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.cm  &
   adams_id = 59  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.inertia_frame  &
   adams_id = 60  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.inertia_frame  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.graout_1  &
   adams_id = 61  &
   location = -390.5595878992, 5.9337951219E-11, -340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.graout_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.graout_2  &
   adams_id = 62  &
   location = -390.5595878992, 5.9337951219E-11, 340.36  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.graout_2  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.graout_3  &
   adams_id = 63  &
   location = 781.1191757984, -1.1845385783E-10, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.graout_3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.jxs_joint_i_16  &
   adams_id = 65  &
   location = 0.0, 0.0, 0.0  &
   orientation = 183.3555200908d, 90.0d, 180.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.jxs_joint_i_16  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.jxs_joint_j_14  &
   adams_id = 66  &
   location = 781.1191757984, -1.1845385783E-10, 0.0  &
   orientation = 3.3555200908d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.jxs_joint_j_14  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.MARKER_527  &
   adams_id = 527  &
   location = -390.5595878992, 5.906386491E-11, 0.0  &
   orientation = 3.3555200902d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.MARKER_527  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_subframe.MARKER_533  &
   adams_id = 533  &
   location = 781.1191757984, -1.1845385783E-10, 0.0  &
   orientation = 3.3555200902d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_subframe.MARKER_533  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_subframe  &
   mass = 4.5359237E-03  &
   center_of_mass_marker = .template_6_force.nlg_subframe.cm  &
   inertia_marker = .template_6_force.nlg_subframe.inertia_frame  &
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
   outline_name = .template_6_force.nlg_subframe.graout_subframe_geom  &
   adams_id = 41  &
   marker_name =  &
      .template_6_force.nlg_subframe.graout_1,  &
      .template_6_force.nlg_subframe.graout_2,  &
      .template_6_force.nlg_subframe.graout_3  &
   visibility_between_markers = on, on, on  &
   close = yes
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_subframe.graout_subframe_geom  &
   color = WHITE
!
part attributes  &
   part_name = .template_6_force.nlg_subframe  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!------------------------------- mts_body_mount -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mts_body_mount  &
   adams_id = 13  &
   location = 6704.33, 0.0, 1668.78  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mts_body_mount
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mts_body_mount.mount_i  &
   adams_id = 67  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mts_body_mount.mount_i  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mts_body_mount.jxs_joint_j_16  &
   adams_id = 68  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mts_body_mount.jxs_joint_j_16  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
part attributes  &
   part_name = .template_6_force.mts_body_mount  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!--------------------------------- nlg_collar ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_collar  &
   adams_id = 14  &
   location = 6197.6, 0.0, 809.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_collar
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_collar.cm  &
   adams_id = 70  &
   location = 0.0, 0.0, 0.0  &
   orientation = 180.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_collar.cm  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_collar.gralin_24  &
   adams_id = 72  &
   location = 0.0, 0.0, -47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_collar.gralin_24  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_collar.jxs_joint_i_1  &
   adams_id = 73  &
   location = 0.0, 0.0, 47.498  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_collar.jxs_joint_i_1  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_collar  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_collar.gralin_collar  &
   adams_id = 40  &
   center_marker = .template_6_force.nlg_collar.gralin_24  &
   angle_extent = 360.0  &
   length = 94.996  &
   radius = 139.7  &
   side_count_for_body = 15  &
   segment_count_for_ends = 15
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_collar.gralin_collar  &
   color = WHITE
!
part attributes  &
   part_name = .template_6_force.nlg_collar  &
   visibility = on  &
   name_visibility = on  &
   size_of_icons = 25.0
!
!------------------------------ nlg_suo_rod_base ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_suo_rod_base  &
   adams_id = 182  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_suo_rod_base
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1105  &
   adams_id = 1105  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1105  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1106  &
   adams_id = 1106  &
   location = 5110.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1106  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1107  &
   adams_id = 1107  &
   location = 5106.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1107  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1108  &
   adams_id = 1108  &
   location = 5102.8134765625, 0.0, 1981.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1108  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1109  &
   adams_id = 1109  &
   location = 5202.8134765625, 0.0, 1981.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1109  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1110  &
   adams_id = 1110  &
   location = 5196.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1110  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1111  &
   adams_id = 1111  &
   location = 5186.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1111  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1112  &
   adams_id = 1112  &
   location = 5186.8134765625, 0.0, 1961.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1112  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1113  &
   adams_id = 1113  &
   location = 5167.8134765644, -2.0856155039E-10, 1931.4468383829  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1113  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1114  &
   adams_id = 1114  &
   location = 5156.8134765625, 0.0, 1961.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1114  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.cm  &
   adams_id = 1134  &
   location = 5157.0479081759, 3.4169043054E-10, 1967.4173714033  &
   orientation = 90.0000000005d, 101.9034193153d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1115  &
   adams_id = 1115  &
   location = 5202.8134765625, 0.0, 1981.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1115  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_suo_rod_base  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape plate  &
   plate_name = .template_6_force.nlg_suo_rod_base.PLATE_509  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1105,  &
                 .template_6_force.nlg_suo_rod_base.MARKER_1106,  &
                 .template_6_force.nlg_suo_rod_base.MARKER_1107,  &
                 .template_6_force.nlg_suo_rod_base.MARKER_1108,  &
                 .template_6_force.nlg_suo_rod_base.MARKER_1109,  &
                 .template_6_force.nlg_suo_rod_base.MARKER_1110,  &
                 .template_6_force.nlg_suo_rod_base.MARKER_1111,  &
                 .template_6_force.nlg_suo_rod_base.MARKER_1112,  &
                 .template_6_force.nlg_suo_rod_base.MARKER_1113,  &
                 .template_6_force.nlg_suo_rod_base.MARKER_1114  &
   width = 15.0  &
   radius = 2.0
!
part attributes  &
   part_name = .template_6_force.nlg_suo_rod_base  &
   color = Gray  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!--------------------------------- nlg_sf_rod ---------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_sf_rod  &
   adams_id = 5  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_sf_rod
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_5  &
   adams_id = 5  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_5  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.gralin_25  &
   adams_id = 3  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 270.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.gralin_25  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.cm  &
   adams_id = 76  &
   location = 6830.8990194197, 0.0, 1239.0072955518  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_79  &
   adams_id = 79  &
   location = 6830.8990194192, 0.0, 1239.0072955517  &
   orientation = 270.0d, 120.453223909d, 180.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_79  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_80  &
   adams_id = 80  &
   location = 6830.8990194192, 0.0, 1239.0072955517  &
   orientation = 270.0d, 120.453223909d, 180.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_80  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_84  &
   adams_id = 84  &
   location = 6830.8990194192, 0.0, 1239.0072955517  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_84  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_90  &
   adams_id = 90  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_90  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_91  &
   adams_id = 91  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 90.0d, 59.546776091d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_91  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_96  &
   adams_id = 96  &
   location = 6434.3591354821, 0.0, 1005.8633047504  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_96  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_511  &
   adams_id = 511  &
   location = 6830.8990194197, 0.0, 1239.0072955518  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_511  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_sf_rod  &
   material_type = .template_6_force.steel
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_6_force.nlg_sf_rod.PT3  &
   location = 6434.3591354821, 0.0, 1005.8633047504
!
point attributes  &
   point_name = .template_6_force.nlg_sf_rod.PT3  &
   visibility = off  &
   name_visibility = off  &
   size_of_icons = 25.0
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_sf_rod.CYLINDER_30  &
   adams_id = 30  &
   center_marker = .template_6_force.nlg_sf_rod.gralin_25  &
   angle_extent = 360.0  &
   length = 920.0  &
   radius = 27.5  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.nlg_sf_rod  &
   color = RED  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------ nlg_suo_actuator ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_suo_actuator  &
   adams_id = 181  &
   location = 0.0, 0.0, -2.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_suo_actuator
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1078  &
   adams_id = 1078  &
   location = 5171.8134765625, -6.0, 1952.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1078  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1103  &
   adams_id = 1103  &
   location = 5184.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1103  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1098  &
   adams_id = 1098  &
   location = 5150.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1098  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1102  &
   adams_id = 1102  &
   location = 5132.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1102  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1100  &
   adams_id = 1100  &
   location = 5150.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1100  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1077  &
   adams_id = 1077  &
   location = 5143.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1077  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_actuator.cm  &
   adams_id = 1094  &
   location = 5174.2151476425, 1.0471684534E-10, 1947.4468383787  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_actuator.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1294  &
   adams_id = 1294  &
   location = 5143.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_actuator.MARKER_1294  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_suo_actuator  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_suo_actuator.CYLINDER_501  &
   adams_id = 501  &
   center_marker = .template_6_force.nlg_suo_actuator.MARKER_1077  &
   angle_extent = 360.0000000012  &
   length = 42.0  &
   radius = 3.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape block  &
   block_name = .template_6_force.nlg_suo_actuator.BOX_502  &
   adams_id = 502  &
   corner_marker = .template_6_force.nlg_suo_actuator.MARKER_1078  &
   diag_corner_coords = 18.0, 10.0, 12.0
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.nlg_suo_actuator.CYLINDER_572  &
   adams_id = 572  &
   center_marker = .template_6_force.nlg_suo_actuator.MARKER_1294  &
   angle_extent = 360.0000000012  &
   length = 3.0  &
   radius = 3.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.nlg_suo_actuator  &
   color = MAIZE  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!----------------------------- mlg_suo_liangan_L ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_liangan_L  &
   adams_id = 184  &
   location = 1.0337216477E+04, 4571.8134765625, -190.0  &
   orientation = 270.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_liangan_L
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1336  &
   adams_id = 1336  &
   location = 5098.8134765625, -8.0, 1911.4468383789  &
   orientation = 90.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1336  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1338  &
   adams_id = 1338  &
   location = 5098.8134765625, 8.0, 1911.4468383789  &
   orientation = 90.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1338  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_997  &
   adams_id = 997  &
   location = 5127.6041601028, 0.0, 1924.5997322579  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_997  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_998  &
   adams_id = 998  &
   location = 5098.8134765625, -4.3751220019E-07, 1911.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_998  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_999  &
   adams_id = 999  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_999  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_L.cm  &
   adams_id = 1497  &
   location = 5109.6512166816, -1.7068144649E-10, 1927.9062437195  &
   orientation = 89.9999999969d, 175.3624587705d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_L.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1029  &
   adams_id = 1498  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1029  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1006  &
   adams_id = 1499  &
   location = 5127.6041601028, 0.0, 1924.5997322579  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1006  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_liangan_L  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape plate  &
   plate_name = .template_6_force.mlg_suo_liangan_L.PLATE_464  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_997,  &
                 .template_6_force.mlg_suo_liangan_L.MARKER_998,  &
                 .template_6_force.mlg_suo_liangan_L.MARKER_999  &
   width = 5.0  &
   radius = 2.0
!
part attributes  &
   part_name = .template_6_force.mlg_suo_liangan_L  &
   color = MAIZE  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------ mlg_dragbrace_R -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_dragbrace_R  &
   adams_id = 195  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_dragbrace_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1468  &
   adams_id = 1468  &
   location = 9537.340597, 1639.0607744, 1652.406081799  &
   orientation = 90.2501196905d, 126.9516172164d, 90.1503576632d
!
marker attributes  &
   marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1468  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_dragbrace_R.cm  &
   adams_id = 1483  &
   location = 9872.9776358092, 1640.5259777056, 1399.9271096871  &
   orientation = 270.2501196905d, 53.0483827836d, 89.6339752922d
!
marker attributes  &
   marker_name = .template_6_force.mlg_dragbrace_R.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1469  &
   adams_id = 1469  &
   location = 9537.340597, 1639.0607744, 1652.406081799  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1469  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1471  &
   adams_id = 1471  &
   location = 1.0208614675E+04, 1641.9911810113, 1147.4481375752  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1471  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_dragbrace_R  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_dragbrace_R.CYLINDER_778  &
   adams_id = 778  &
   center_marker = .template_6_force.mlg_dragbrace_R.MARKER_1468  &
   angle_extent = 360.0  &
   length = 840.0  &
   radius = 25.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.mlg_dragbrace_R  &
   color = GREEN  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------ mlg_suo_yaobi_L -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_yaobi_L  &
   adams_id = 196  &
   location = 1.0337216477E+04, 4571.8134765625, -190.0  &
   orientation = 270.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_yaobi_L
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1333  &
   adams_id = 1333  &
   location = 5126.6611975794, -2.9999995625, 1958.6666746359  &
   orientation = 179.9999999082d, 90.0000001904d, 58.2679219728d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1333  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1026  &
   adams_id = 1500  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 148.2679219719d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1026  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1027  &
   adams_id = 1501  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 148.2679219719d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1027  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.cm  &
   adams_id = 1502  &
   location = 5115.0837647465, 3.7459686717E-08, 1954.5727348265  &
   orientation = 90.0000000191d, 58.2679219733d, 2.0546340454E-06d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1028  &
   adams_id = 1503  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1028  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1030  &
   adams_id = 1504  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1030  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1048  &
   adams_id = 1505  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1048  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_yaobi_L  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape block  &
   block_name = .template_6_force.mlg_suo_yaobi_L.BOX_611  &
   adams_id = 611  &
   corner_marker = .template_6_force.mlg_suo_yaobi_L.MARKER_1333  &
   diag_corner_coords = -3.0, -24.0, 6.0
!
geometry create shape link  &
   link_name = .template_6_force.mlg_suo_yaobi_L.LINK_483  &
   i_marker = .template_6_force.mlg_suo_yaobi_L.MARKER_1026  &
   j_marker = .template_6_force.mlg_suo_yaobi_L.MARKER_1027  &
   width = 12.0  &
   depth = 10.0
!
part attributes  &
   part_name = .template_6_force.mlg_suo_yaobi_L  &
   color = MAGENTA  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------- mlg_suo_rod_L --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_rod_L  &
   adams_id = 197  &
   location = 1.0337216477E+04, 4586.8134765625, -192.0  &
   orientation = 270.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_rod_L
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1097  &
   adams_id = 1506  &
   location = 5147.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1097  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1101  &
   adams_id = 1507  &
   location = 5149.8134765625, 7.4791382279E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1101  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1099  &
   adams_id = 1508  &
   location = 5147.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1099  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1050  &
   adams_id = 1509  &
   location = 5134.9134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1050  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_L.cm  &
   adams_id = 1510  &
   location = 5149.8203731142, 7.6505528345E-11, 1947.4468383788  &
   orientation = 90.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_L.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1075  &
   adams_id = 1511  &
   location = 5134.8134765625, 0.0, 1947.4468383789  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1075  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1076  &
   adams_id = 1512  &
   location = 5164.8134765625, 1.2758529918E-10, 1947.4468383788  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1076  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_rod_L  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_6_force.mlg_suo_rod_L.nlg_suo_rod_n  &
   adams_id = 780  &
   center_marker = .template_6_force.mlg_suo_rod_L.MARKER_1050  &
   x_scale_factor = 3.6  &
   y_scale_factor = 3.6  &
   z_scale_factor = 3.6
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_suo_rod_L.CYLINDER_499  &
   adams_id = 779  &
   center_marker = .template_6_force.mlg_suo_rod_L.MARKER_1075  &
   angle_extent = 360.0000000012  &
   length = 30.0  &
   radius = 1.8  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_6_force.mlg_suo_rod_L.ELLIPSOID_500  &
   adams_id = 781  &
   center_marker = .template_6_force.mlg_suo_rod_L.MARKER_1076  &
   x_scale_factor = 3.6  &
   y_scale_factor = 3.6  &
   z_scale_factor = 3.6
!
part attributes  &
   part_name = .template_6_force.mlg_suo_rod_L  &
   color = RED  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------- mlg_suo_base_L -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_base_L  &
   adams_id = 198  &
   location = 1.0337216477E+04, 4571.8134765625, -190.0  &
   orientation = 270.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_base_L
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1329  &
   adams_id = 1329  &
   location = 5102.8134765625, 4.3750958412E-07, 1981.4468383789  &
   orientation = 0.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1329  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1105  &
   adams_id = 1513  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1105  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1106  &
   adams_id = 1514  &
   location = 5110.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1106  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1107  &
   adams_id = 1515  &
   location = 5106.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1107  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1108  &
   adams_id = 1516  &
   location = 5102.8134765625, 0.0, 1981.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1108  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1109  &
   adams_id = 1517  &
   location = 5202.8134765625, 0.0, 1981.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1109  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1110  &
   adams_id = 1518  &
   location = 5196.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1110  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1111  &
   adams_id = 1519  &
   location = 5186.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1111  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1112  &
   adams_id = 1520  &
   location = 5186.8134765625, 0.0, 1961.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1112  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1113  &
   adams_id = 1521  &
   location = 5167.8134765644, 1.0721262838E-08, 1931.4468383829  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1113  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1114  &
   adams_id = 1522  &
   location = 5156.8134765625, 0.0, 1961.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1114  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_L.cm  &
   adams_id = 1523  &
   location = 5157.0479081759, 3.42635905E-10, 1967.4173714033  &
   orientation = 90.0000000005d, 101.9034193149d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_L.cm  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_base_L  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape plate  &
   plate_name = .template_6_force.mlg_suo_base_L.PLATE_509  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1105,  &
                 .template_6_force.mlg_suo_base_L.MARKER_1106,  &
                 .template_6_force.mlg_suo_base_L.MARKER_1107,  &
                 .template_6_force.mlg_suo_base_L.MARKER_1108,  &
                 .template_6_force.mlg_suo_base_L.MARKER_1109,  &
                 .template_6_force.mlg_suo_base_L.MARKER_1110,  &
                 .template_6_force.mlg_suo_base_L.MARKER_1111,  &
                 .template_6_force.mlg_suo_base_L.MARKER_1112,  &
                 .template_6_force.mlg_suo_base_L.MARKER_1113,  &
                 .template_6_force.mlg_suo_base_L.MARKER_1114  &
   width = 15.0  &
   radius = 2.0
!
part attributes  &
   part_name = .template_6_force.mlg_suo_base_L  &
   color = Gray  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------ mlg_dragbrace_L -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_dragbrace_L  &
   adams_id = 199  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_dragbrace_L
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1484  &
   adams_id = 1484  &
   location = 9537.340597, -1639.0607744, 1652.406081799  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1484  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1145  &
   adams_id = 1145  &
   location = 9537.340597, -1639.0607744, 1652.406081799  &
   orientation = 89.7502130907d, 126.9522076919d, 269.8498403277d
!
marker attributes  &
   marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1145  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_dragbrace_L.cm  &
   adams_id = 1160  &
   location = 9872.9750423374, -1640.5240169392, 1399.9236506789  &
   orientation = 89.7502130907d, 126.9522076919d, 36.4129954643d
!
marker attributes  &
   marker_name = .template_6_force.mlg_dragbrace_L.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1148  &
   adams_id = 1148  &
   location = 1.0208609488E+04, -1641.9872594779, 1147.4412195584  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1148  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_dragbrace_L  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_dragbrace_L.CYLINDER_526  &
   adams_id = 526  &
   center_marker = .template_6_force.mlg_dragbrace_L.MARKER_1145  &
   angle_extent = 360.0000000012  &
   length = 840.0  &
   radius = 25.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.mlg_dragbrace_L  &
   color = GREEN  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!----------------------------- mlg_suo_actuator_L -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_actuator_L  &
   adams_id = 200  &
   location = 1.0337216477E+04, 4571.8134765625, -192.0  &
   orientation = 270.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_actuator_L
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1309  &
   adams_id = 1309  &
   location = 5189.8134765624, 4.3750958412E-07, 1947.4468383787  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1309  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1078  &
   adams_id = 1524  &
   location = 5172.8134765625, -6.0, 1952.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1078  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1098  &
   adams_id = 1525  &
   location = 5150.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1098  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1102  &
   adams_id = 1526  &
   location = 5132.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1102  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1100  &
   adams_id = 1527  &
   location = 5150.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1100  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1077  &
   adams_id = 1528  &
   location = 5140.3134765625, 6.3789433965E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1077  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_L.cm  &
   adams_id = 1529  &
   location = 5174.0478519674, 1.0922168846E-10, 1947.4468383787  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_L.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1294  &
   adams_id = 1530  &
   location = 5143.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1294  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_actuator_L  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_suo_actuator_L.CYLINDER_501  &
   adams_id = 783  &
   center_marker = .template_6_force.mlg_suo_actuator_L.MARKER_1077  &
   angle_extent = 360.0  &
   length = 45.0  &
   radius = 3.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape block  &
   block_name = .template_6_force.mlg_suo_actuator_L.BOX_502  &
   adams_id = 782  &
   corner_marker = .template_6_force.mlg_suo_actuator_L.MARKER_1078  &
   diag_corner_coords = 18.0, 10.0, 12.0
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_suo_actuator_L.CYLINDER_572  &
   adams_id = 784  &
   center_marker = .template_6_force.mlg_suo_actuator_L.MARKER_1294  &
   angle_extent = 360.0000000012  &
   length = 3.0  &
   radius = 3.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.mlg_suo_actuator_L  &
   color = MAIZE  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!----------------------------- mlg_suo_liangan_R ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_liangan_R  &
   adams_id = 185  &
   location = 1.0337464717E+04, -4571.8134765625, -190.0  &
   orientation = 90.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_liangan_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1336  &
   adams_id = 1364  &
   location = 5098.8134765625, -8.0, 1911.4468383789  &
   orientation = 90.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1336  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1338  &
   adams_id = 1365  &
   location = 5098.8134765625, 8.0, 1911.4468383789  &
   orientation = 90.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1338  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_997  &
   adams_id = 1366  &
   location = 5127.6041601028, 0.0, 1924.5997322579  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_997  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_998  &
   adams_id = 1367  &
   location = 5098.8134765625, 4.3751313683E-07, 1911.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_998  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_999  &
   adams_id = 1368  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_999  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_R.cm  &
   adams_id = 1369  &
   location = 5109.6512166816, -1.7066917322E-10, 1927.9062437195  &
   orientation = 89.9999999969d, 175.3624587761d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_R.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1029  &
   adams_id = 1370  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1029  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1006  &
   adams_id = 1371  &
   location = 5127.6041601028, 0.0, 1924.5997322579  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1006  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_liangan_R  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape plate  &
   plate_name = .template_6_force.mlg_suo_liangan_R.PLATE_464  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_997,  &
                 .template_6_force.mlg_suo_liangan_R.MARKER_998,  &
                 .template_6_force.mlg_suo_liangan_R.MARKER_999  &
   width = 5.0  &
   radius = 2.0
!
part attributes  &
   part_name = .template_6_force.mlg_suo_liangan_R  &
   color = MAIZE  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------ mlg_suo_yaobi_R -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_yaobi_R  &
   adams_id = 186  &
   location = 1.0337464717E+04, -4571.8134765625, -190.0  &
   orientation = 90.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_yaobi_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1333  &
   adams_id = 1531  &
   location = 5126.6611975794, -2.9999995625, 1958.6666746359  &
   orientation = 179.9999999082d, 90.0000001904d, 58.2679219728d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1333  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1026  &
   adams_id = 1532  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 148.2679219719d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1026  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1027  &
   adams_id = 1533  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 148.2679219719d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1027  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.cm  &
   adams_id = 1534  &
   location = 5115.0837647465, 3.7459686717E-08, 1954.5727348265  &
   orientation = 90.0000000191d, 58.2679219733d, 2.0546340454E-06d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1028  &
   adams_id = 1376  &
   location = 5102.8134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1028  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1030  &
   adams_id = 1377  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1030  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1048  &
   adams_id = 1378  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1048  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_yaobi_R  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape block  &
   block_name = .template_6_force.mlg_suo_yaobi_R.BOX_611  &
   adams_id = 713  &
   corner_marker = .template_6_force.mlg_suo_yaobi_R.MARKER_1333  &
   diag_corner_coords = -3.0, -24.0, 6.0
!
geometry create shape link  &
   link_name = .template_6_force.mlg_suo_yaobi_R.LINK_483  &
   i_marker = .template_6_force.mlg_suo_yaobi_R.MARKER_1026  &
   j_marker = .template_6_force.mlg_suo_yaobi_R.MARKER_1027  &
   width = 12.0  &
   depth = 10.0
!
part attributes  &
   part_name = .template_6_force.mlg_suo_yaobi_R  &
   color = MAGENTA  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------- mlg_suo_rod_R --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_rod_R  &
   adams_id = 187  &
   location = 1.0337464717E+04, -4586.8134765625, -192.0  &
   orientation = 90.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_rod_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1097  &
   adams_id = 1379  &
   location = 5147.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1097  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1101  &
   adams_id = 1380  &
   location = 5149.8134765625, 7.4791382279E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1101  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1099  &
   adams_id = 1381  &
   location = 5147.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1099  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1050  &
   adams_id = 1535  &
   location = 5134.9134765625, 0.0, 1947.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1050  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_R.cm  &
   adams_id = 1536  &
   location = 5149.8203731142, 7.6505528345E-11, 1947.4468383788  &
   orientation = 90.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_R.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1075  &
   adams_id = 1537  &
   location = 5134.8134765625, 0.0, 1947.4468383789  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1075  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1076  &
   adams_id = 1538  &
   location = 5164.8134765625, 1.2758529918E-10, 1947.4468383788  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1076  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_rod_R  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_6_force.mlg_suo_rod_R.nlg_suo_rod_n  &
   adams_id = 715  &
   center_marker = .template_6_force.mlg_suo_rod_R.MARKER_1050  &
   x_scale_factor = 3.6  &
   y_scale_factor = 3.6  &
   z_scale_factor = 3.6
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_suo_rod_R.CYLINDER_499  &
   adams_id = 714  &
   center_marker = .template_6_force.mlg_suo_rod_R.MARKER_1075  &
   angle_extent = 360.0000000012  &
   length = 30.0  &
   radius = 1.8  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_6_force.mlg_suo_rod_R.ELLIPSOID_500  &
   adams_id = 716  &
   center_marker = .template_6_force.mlg_suo_rod_R.MARKER_1076  &
   x_scale_factor = 3.6  &
   y_scale_factor = 3.6  &
   z_scale_factor = 3.6
!
part attributes  &
   part_name = .template_6_force.mlg_suo_rod_R  &
   color = RED  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------- mlg_suo_base_R -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_base_R  &
   adams_id = 188  &
   location = 1.0337464717E+04, -4571.8134765625, -190.0  &
   orientation = 90.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_base_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1329  &
   adams_id = 1386  &
   location = 5102.8134765625, 4.3750958412E-07, 1981.4468383789  &
   orientation = 0.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1329  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1105  &
   adams_id = 1387  &
   location = 5126.9408283745, 0.0, 1962.3668617453  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1105  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1106  &
   adams_id = 1388  &
   location = 5110.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1106  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1107  &
   adams_id = 1389  &
   location = 5106.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1107  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1108  &
   adams_id = 1390  &
   location = 5102.8134765625, 0.0, 1981.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1108  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1109  &
   adams_id = 1391  &
   location = 5202.8134765625, 0.0, 1981.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1109  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1110  &
   adams_id = 1392  &
   location = 5196.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1110  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1111  &
   adams_id = 1393  &
   location = 5186.8134765625, 0.0, 1979.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1111  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1112  &
   adams_id = 1394  &
   location = 5186.8134765625, 0.0, 1961.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1112  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1113  &
   adams_id = 1395  &
   location = 5167.8134765644, 1.0718537169E-08, 1931.4468383829  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1113  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1114  &
   adams_id = 1396  &
   location = 5156.8134765625, 0.0, 1961.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1114  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_base_R.cm  &
   adams_id = 1397  &
   location = 5157.0479081759, 3.4169376491E-10, 1967.4173714033  &
   orientation = 90.0000000005d, 101.9034193153d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_base_R.cm  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_base_R  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape plate  &
   plate_name = .template_6_force.mlg_suo_base_R.PLATE_509  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1105,  &
                 .template_6_force.mlg_suo_base_R.MARKER_1106,  &
                 .template_6_force.mlg_suo_base_R.MARKER_1107,  &
                 .template_6_force.mlg_suo_base_R.MARKER_1108,  &
                 .template_6_force.mlg_suo_base_R.MARKER_1109,  &
                 .template_6_force.mlg_suo_base_R.MARKER_1110,  &
                 .template_6_force.mlg_suo_base_R.MARKER_1111,  &
                 .template_6_force.mlg_suo_base_R.MARKER_1112,  &
                 .template_6_force.mlg_suo_base_R.MARKER_1113,  &
                 .template_6_force.mlg_suo_base_R.MARKER_1114  &
   width = 15.0  &
   radius = 2.0
!
part attributes  &
   part_name = .template_6_force.mlg_suo_base_R  &
   color = Gray  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!----------------------------- mlg_suo_actuator_R -----------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_actuator_R  &
   adams_id = 190  &
   location = 1.0337464717E+04, -4571.8134765625, -192.0  &
   orientation = 90.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_actuator_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1309  &
   adams_id = 1403  &
   location = 5189.8134765624, 4.3750958412E-07, 1947.4468383787  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1309  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1078  &
   adams_id = 1404  &
   location = 5172.8134765625, -6.0, 1952.4468383789  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1078  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1098  &
   adams_id = 1405  &
   location = 5150.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1098  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1102  &
   adams_id = 1406  &
   location = 5132.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1102  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1100  &
   adams_id = 1407  &
   location = 5150.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1100  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1077  &
   adams_id = 1408  &
   location = 5140.3134765625, 6.3789433965E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1077  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_R.cm  &
   adams_id = 1409  &
   location = 5174.0478519674, 1.0922168846E-10, 1947.4468383787  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_R.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1294  &
   adams_id = 1410  &
   location = 5143.3134765625, 6.3792649591E-11, 1947.4468383788  &
   orientation = 90.0000000003d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1294  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_actuator_R  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_suo_actuator_R.CYLINDER_501  &
   adams_id = 719  &
   center_marker = .template_6_force.mlg_suo_actuator_R.MARKER_1077  &
   angle_extent = 360.0  &
   length = 45.0  &
   radius = 3.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape block  &
   block_name = .template_6_force.mlg_suo_actuator_R.BOX_502  &
   adams_id = 718  &
   corner_marker = .template_6_force.mlg_suo_actuator_R.MARKER_1078  &
   diag_corner_coords = 18.0, 10.0, 12.0
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_suo_actuator_R.CYLINDER_572  &
   adams_id = 720  &
   center_marker = .template_6_force.mlg_suo_actuator_R.MARKER_1294  &
   angle_extent = 360.0000000012  &
   length = 3.0  &
   radius = 3.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.mlg_suo_actuator_R  &
   color = MAIZE  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!-------------------------------- mlg_struct_R --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_struct_R  &
   adams_id = 191  &
   location = 2.2574681194E+04, 200.0, -501.000000001  &
   orientation = 180.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_struct_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_1472  &
   adams_id = 1472  &
   location = 1.2366066519E+04, -1441.9911810113, 1648.4481375762  &
   orientation = 90.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_1472  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_1314  &
   adams_id = 1411  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_1314  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_553  &
   adams_id = 1415  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 90.0000000003d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_553  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.cm  &
   adams_id = 1416  &
   location = 1.2237340597E+04, -1546.2385697912, 1343.8046907198  &
   orientation = 180.0d, 15.8564980715d, 180.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_554  &
   adams_id = 1417  &
   location = 1.2237340597E+04, -1439.0607743967, 1703.4060818  &
   orientation = 90.0000000003d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_554  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_555  &
   adams_id = 1418  &
   location = 1.2237340597E+04, -1439.0607743967, 953.4060818  &
   orientation = 0.0d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_555  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_556  &
   adams_id = 1419  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_556  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_557  &
   adams_id = 1420  &
   location = 1.2237340597E+04, -1289.0607744, 2253.4060818  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_557  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_558  &
   adams_id = 1421  &
   location = 1.2237340597E+04, -1589.0607744, 2253.4060818  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_558  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_566  &
   adams_id = 1422  &
   location = 1.2087340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_566  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_568  &
   adams_id = 1423  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_568  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_588  &
   adams_id = 1424  &
   location = 1.2297340597E+04, -1359.0607743967, 1153.4060818006  &
   orientation = 180.0000000006d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_588  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_589  &
   adams_id = 1425  &
   location = 1.2177340597E+04, -1359.0607743967, 1153.4060817994  &
   orientation = 180.0000000006d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_589  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_590  &
   adams_id = 1426  &
   location = 1.2297340597E+04, -1299.0607743967, 1153.4060818006  &
   orientation = 270.0000000009d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_590  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_591  &
   adams_id = 1427  &
   location = 1.2237340597E+04, -1299.0607743985, 1153.4060818  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_591  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_1565  &
   adams_id = 1565  &
   location = 1.2237340597E+04, -1829.0607743967, 953.406081798  &
   orientation = 180.0d, 89.9999999997d, 68.2585681126d
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_struct_R  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_304  &
   adams_id = 721  &
   center_marker = .template_6_force.mlg_struct_R.MARKER_553  &
   angle_extent = 360.0000000012  &
   length = 1080.0  &
   radius = 92.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_308  &
   adams_id = 722  &
   center_marker = .template_6_force.mlg_struct_R.MARKER_554  &
   angle_extent = 360.0000000012  &
   length = 750.0  &
   radius = 62.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_R.CYLINDER_308  &
   color = PEACH
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_309  &
   adams_id = 723  &
   center_marker = .template_6_force.mlg_struct_R.MARKER_555  &
   angle_extent = 360.0  &
   length = 390.0  &
   radius = 50.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_R.CYLINDER_309  &
   color = PEACH
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_322  &
   adams_id = 724  &
   center_marker = .template_6_force.mlg_struct_R.MARKER_588  &
   angle_extent = 360.0000000012  &
   length = 70.0  &
   radius = 10.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_R.CYLINDER_322  &
   color = WHITE
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_323  &
   adams_id = 725  &
   center_marker = .template_6_force.mlg_struct_R.MARKER_589  &
   angle_extent = 360.0000000012  &
   length = 70.0  &
   radius = 10.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_R.CYLINDER_323  &
   color = WHITE
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_324  &
   adams_id = 726  &
   center_marker = .template_6_force.mlg_struct_R.MARKER_590  &
   angle_extent = 360.0000000012  &
   length = 120.0  &
   radius = 10.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_R.CYLINDER_324  &
   color = WHITE
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_6_force.mlg_struct_R.ELLIPSOID_325  &
   adams_id = 727  &
   center_marker = .template_6_force.mlg_struct_R.MARKER_591  &
   x_scale_factor = 15.0  &
   y_scale_factor = 15.0  &
   z_scale_factor = 15.0
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_R.ELLIPSOID_325  &
   color = Orange
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_910  &
   adams_id = 910  &
   center_marker = .template_6_force.mlg_struct_R.MARKER_1565  &
   angle_extent = 360.0  &
   length = 150.0  &
   radius = 200.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_R.CYLINDER_910  &
   color = Orange
!
geometry create shape plate  &
   plate_name = .template_6_force.mlg_struct_R.PLATE_310  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_556,  &
                 .template_6_force.mlg_struct_R.MARKER_557,  &
                 .template_6_force.mlg_struct_R.MARKER_558  &
   width = 60.0  &
   radius = 5.0
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_R.PLATE_310  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_force.mlg_struct_R  &
   color = RED  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!--------------------------------- mlg_rod_R ----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_rod_R  &
   adams_id = 192  &
   location = 2.2874681194E+04, 200.0, -501.000000001  &
   orientation = 180.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_rod_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_559  &
   adams_id = 1430  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 180.0000000006d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_559  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_R.cm  &
   adams_id = 1431  &
   location = 1.2387340597E+04, -989.0607744005, 2253.4060817991  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_R.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_564  &
   adams_id = 1432  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 0.0d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_564  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_565  &
   adams_id = 1433  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_565  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_593  &
   adams_id = 1434  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_593  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_603  &
   adams_id = 1435  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_603  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_1556  &
   adams_id = 1556  &
   location = 1.2387340597E+04, -989.0607744005, 2253.4060817991  &
   orientation = 180.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_1556  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_rod_R  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_rod_R.CYLINDER_315  &
   adams_id = 728  &
   center_marker = .template_6_force.mlg_rod_R.MARKER_559  &
   angle_extent = 360.0000000012  &
   length = 600.0  &
   radius = 26.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.mlg_rod_R  &
   color = GREEN  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------- mlg_actuator_R -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_actuator_R  &
   adams_id = 193  &
   location = 2.2874681194E+04, 200.0, -501.000000001  &
   orientation = 180.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_actuator_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_560  &
   adams_id = 1439  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 180.0000000006d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_560  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuator_R.cm  &
   adams_id = 1440  &
   location = 1.2387340597E+04, -864.0607744005, 2253.4060817996  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuator_R.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_578  &
   adams_id = 1441  &
   location = 1.2387340597E+04, -539.0607744005, 2253.406081799  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_578  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_563  &
   adams_id = 1442  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 0.0d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_563  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_592  &
   adams_id = 1443  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_592  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_602  &
   adams_id = 1444  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_602  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_1557  &
   adams_id = 1557  &
   location = 1.2387340597E+04, -689.0607744005, 2253.4060817976  &
   orientation = 180.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_1557  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_actuator_R  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_actuator_R.CYLINDER_320  &
   adams_id = 729  &
   center_marker = .template_6_force.mlg_actuator_R.MARKER_560  &
   angle_extent = 360.0000000012  &
   length = 650.0  &
   radius = 40.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.mlg_actuator_R  &
   color = MAIZE  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------ mlg_suo_suogou_R ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_suogou_R  &
   adams_id = 194  &
   location = 1.0337464717E+04, -4982.4955993011, 4342.9415786566  &
   orientation = 180.0d, 28.6478897565d, 270.0000000001d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_suogou_R
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_995  &
   adams_id = 1446  &
   location = 6142.8134765625, 0.0, 391.4468383789  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_995  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1334  &
   adams_id = 1448  &
   location = 6142.8134765625, 0.0, 391.4468383789  &
   orientation = 179.9999998281d, 90.0000001231d, 29.6200322163d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1334  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1337  &
   adams_id = 1449  &
   location = 6145.9420208936, -8.0000000107, 366.9476096035  &
   orientation = 269.9999999999d, 28.6478897565d, 180.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1337  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1339  &
   adams_id = 1450  &
   location = 6145.9420208936, 7.9999999893, 366.9476096035  &
   orientation = 269.9999999999d, 28.6478897565d, 180.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1339  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_514  &
   adams_id = 1451  &
   location = 6152.0, -6.0, 387.0  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_514  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_520  &
   adams_id = 1452  &
   location = 6146.9, -6.0, 364.6  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_520  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1135  &
   adams_id = 1453  &
   location = 6142.8134765625, 0.0, 391.4468383789  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1135  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1136  &
   adams_id = 1454  &
   location = 6110.8091591519, 1.4961334447E-10, 366.1605642471  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1136  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1137  &
   adams_id = 1455  &
   location = 6136.8493067665, 7.3181002209E-11, 358.561755459  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1137  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1138  &
   adams_id = 1456  &
   location = 6146.8999999999, 5.9999999999, 359.5999999999  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1138  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1139  &
   adams_id = 1457  &
   location = 6181.8999999999, -5.9999999997, 359.5999999997  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1139  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.cm  &
   adams_id = 1458  &
   location = 6153.0350282156, -7.0714316168E-11, 374.4685142105  &
   orientation = 90.0000000004d, 79.6996199096d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1140  &
   adams_id = 1459  &
   location = 6181.9, -5.9999999997, 364.5999999996  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1140  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1141  &
   adams_id = 1460  &
   location = 6146.9, -6.0, 364.6  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1141  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1007  &
   adams_id = 1461  &
   location = 6110.8091591519, 1.4961334447E-10, 366.1605642471  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1007  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1142  &
   adams_id = 1464  &
   location = 6151.9999999999, -6.0, 382.0  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1142  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1143  &
   adams_id = 1465  &
   location = 6194.0, -5.9999999996, 381.9999999995  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1143  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1144  &
   adams_id = 1466  &
   location = 6193.9999999999, 6.0000000005, 386.9999999995  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1144  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_suogou_R  &
   material_type = .template_6_force.steel
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_6_force.mlg_suo_suogou_R.PT200  &
   location = 6142.8134765625, 0.0, 391.4468383789
!
point attributes  &
   point_name = .template_6_force.mlg_suo_suogou_R.PT200  &
   name_visibility = off  &
   size_of_icons = 25.0
!
! ****** Graphics for current part ******
!
geometry create shape block  &
   block_name = .template_6_force.mlg_suo_suogou_R.BOX_268  &
   adams_id = 730  &
   corner_marker = .template_6_force.mlg_suo_suogou_R.MARKER_514  &
   diag_corner_coords = 42.0, 5.0, 12.0
!
geometry create shape block  &
   block_name = .template_6_force.mlg_suo_suogou_R.BOX_272  &
   adams_id = 731  &
   corner_marker = .template_6_force.mlg_suo_suogou_R.MARKER_520  &
   diag_corner_coords = 35.0, 5.0, 12.0
!
geometry create shape plate  &
   plate_name = .template_6_force.mlg_suo_suogou_R.PLATE_515  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1135,  &
                 .template_6_force.mlg_suo_suogou_R.MARKER_1136,  &
                 .template_6_force.mlg_suo_suogou_R.MARKER_1137,  &
                 .template_6_force.mlg_suo_suogou_R.MARKER_1138,  &
                 .template_6_force.mlg_suo_suogou_R.MARKER_1139,  &
                 .template_6_force.mlg_suo_suogou_R.MARKER_1140,  &
                 .template_6_force.mlg_suo_suogou_R.MARKER_1141,  &
                 .template_6_force.mlg_suo_suogou_R.MARKER_1142,  &
                 .template_6_force.mlg_suo_suogou_R.MARKER_1143,  &
                 .template_6_force.mlg_suo_suogou_R.MARKER_1144  &
   width = 15.0  &
   radius = 1.0
!
part attributes  &
   part_name = .template_6_force.mlg_suo_suogou_R  &
   color = GREEN  &
   size_of_icons = 25.0
!
!-------------------------------- mlg_struct_L --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_struct_L  &
   adams_id = 158  &
   location = -1900.000000002, -200.0, -501.000000001  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_struct_L
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_1314  &
   adams_id = 1314  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 270.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_1314  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_1149  &
   adams_id = 1149  &
   location = 1.2108609488E+04, -1441.9872594779, 1648.4412195594  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_1149  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_553  &
   adams_id = 553  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 90.0000000003d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_553  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.cm  &
   adams_id = 575  &
   location = 1.2237340597E+04, -1546.2385697912, 1343.8046907198  &
   orientation = 180.0d, 15.8564980715d, 179.9999999998d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_554  &
   adams_id = 554  &
   location = 1.2237340597E+04, -1439.0607743967, 1703.4060818  &
   orientation = 90.0000000003d, 180.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_554  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_555  &
   adams_id = 555  &
   location = 1.2237340597E+04, -1439.0607743967, 953.4060818  &
   orientation = 0.0d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_555  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_556  &
   adams_id = 556  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_556  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_557  &
   adams_id = 557  &
   location = 1.2237340597E+04, -1289.0607744, 2253.4060818  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_557  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_558  &
   adams_id = 558  &
   location = 1.2237340597E+04, -1589.0607744, 2253.4060818  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_558  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_566  &
   adams_id = 566  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_566  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_568  &
   adams_id = 568  &
   location = 1.2237340597E+04, -1439.0607744, 2153.4060818  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_568  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_588  &
   adams_id = 588  &
   location = 1.2297340597E+04, -1359.0607743967, 1153.4060818006  &
   orientation = 180.0000000006d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_588  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_589  &
   adams_id = 589  &
   location = 1.2177340597E+04, -1359.0607743967, 1153.4060817994  &
   orientation = 180.0000000006d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_589  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_590  &
   adams_id = 590  &
   location = 1.2297340597E+04, -1299.0607743967, 1153.4060818006  &
   orientation = 270.0000000009d, 90.0000000003d, 270.0000000009d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_590  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_591  &
   adams_id = 591  &
   location = 1.2237340597E+04, -1299.0607743985, 1153.4060818  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_591  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_1564  &
   adams_id = 1564  &
   location = 1.2237340597E+04, -1829.0607743967, 953.406081798  &
   orientation = 180.0d, 89.9999999997d, 275.6904154614d
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_struct_L  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_304  &
   adams_id = 304  &
   center_marker = .template_6_force.mlg_struct_L.MARKER_553  &
   angle_extent = 360.0000000012  &
   length = 1080.0  &
   radius = 92.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_308  &
   adams_id = 308  &
   center_marker = .template_6_force.mlg_struct_L.MARKER_554  &
   angle_extent = 360.0000000012  &
   length = 750.0  &
   radius = 62.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_L.CYLINDER_308  &
   color = PEACH
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_309  &
   adams_id = 309  &
   center_marker = .template_6_force.mlg_struct_L.MARKER_555  &
   angle_extent = 360.0  &
   length = 390.0  &
   radius = 50.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_L.CYLINDER_309  &
   color = PEACH
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_322  &
   adams_id = 322  &
   center_marker = .template_6_force.mlg_struct_L.MARKER_588  &
   angle_extent = 360.0000000012  &
   length = 70.0  &
   radius = 10.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_L.CYLINDER_322  &
   color = WHITE
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_323  &
   adams_id = 323  &
   center_marker = .template_6_force.mlg_struct_L.MARKER_589  &
   angle_extent = 360.0000000012  &
   length = 70.0  &
   radius = 10.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_L.CYLINDER_323  &
   color = WHITE
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_324  &
   adams_id = 324  &
   center_marker = .template_6_force.mlg_struct_L.MARKER_590  &
   angle_extent = 360.0000000012  &
   length = 120.0  &
   radius = 10.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_L.CYLINDER_324  &
   color = WHITE
!
geometry create shape ellipsoid  &
   ellipsoid_name = .template_6_force.mlg_struct_L.ELLIPSOID_325  &
   adams_id = 325  &
   center_marker = .template_6_force.mlg_struct_L.MARKER_591  &
   x_scale_factor = 15.0  &
   y_scale_factor = 15.0  &
   z_scale_factor = 15.0
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_L.ELLIPSOID_325  &
   color = Orange
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_903  &
   adams_id = 903  &
   center_marker = .template_6_force.mlg_struct_L.MARKER_1564  &
   angle_extent = 360.0  &
   length = 150.0  &
   radius = 200.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_L.CYLINDER_903  &
   color = Orange
!
geometry create shape plate  &
   plate_name = .template_6_force.mlg_struct_L.PLATE_310  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_556,  &
                 .template_6_force.mlg_struct_L.MARKER_557,  &
                 .template_6_force.mlg_struct_L.MARKER_558  &
   width = 60.0  &
   radius = 5.0
!
geometry attributes  &
   geometry_name = .template_6_force.mlg_struct_L.PLATE_310  &
   color = YELLOW
!
part attributes  &
   part_name = .template_6_force.mlg_struct_L  &
   color = RED  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!--------------------------------- mlg_rod_L ----------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_rod_L  &
   adams_id = 159  &
   location = -1900.000000002, -200.0, -501.000000001  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_rod_L
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_559  &
   adams_id = 559  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 180.0000000006d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_559  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_L.cm  &
   adams_id = 576  &
   location = 1.2387340597E+04, -989.0607744005, 2253.4060817991  &
   orientation = 0.0d, 90.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_L.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_564  &
   adams_id = 564  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 0.0d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_564  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_565  &
   adams_id = 565  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_565  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_593  &
   adams_id = 593  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_593  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_603  &
   adams_id = 603  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_603  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_682  &
   adams_id = 682  &
   location = 1.2387340597E+04, -1289.0607744005, 2253.4060818007  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_682  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_rod_L  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_rod_L.CYLINDER_315  &
   adams_id = 315  &
   center_marker = .template_6_force.mlg_rod_L.MARKER_559  &
   angle_extent = 360.0000000012  &
   length = 600.0  &
   radius = 26.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.mlg_rod_L  &
   color = GREEN  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------- mlg_actuatorL --------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_actuatorL  &
   adams_id = 160  &
   location = -1900.000000002, -200.0, -501.000000001  &
   orientation = 0.0d, 0.0d, 0.0d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_actuatorL
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_560  &
   adams_id = 560  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 180.0000000006d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_560  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuatorL.cm  &
   adams_id = 577  &
   location = 1.2387340597E+04, -864.0607744005, 2253.4060817996  &
   orientation = 180.0d, 90.0d, 90.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuatorL.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_578  &
   adams_id = 578  &
   location = 1.2387340597E+04, -539.0607744005, 2253.406081799  &
   orientation = 270.0000000009d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_578  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_563  &
   adams_id = 563  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 0.0d, 90.0000000003d, 90.0000000003d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_563  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_592  &
   adams_id = 592  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_592  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_602  &
   adams_id = 602  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_602  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_683  &
   adams_id = 683  &
   location = 1.2387340597E+04, -1189.0607744005, 2253.4060818013  &
   orientation = 0.0d, 0.0d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_683  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_actuatorL  &
   material_type = .template_6_force.steel
!
! ****** Graphics for current part ******
!
geometry create shape cylinder  &
   cylinder_name = .template_6_force.mlg_actuatorL.CYLINDER_320  &
   adams_id = 320  &
   center_marker = .template_6_force.mlg_actuatorL.MARKER_560  &
   angle_extent = 360.0000000012  &
   length = 650.0  &
   radius = 40.0  &
   side_count_for_body = 20  &
   segment_count_for_ends = 20
!
part attributes  &
   part_name = .template_6_force.mlg_actuatorL  &
   color = MAIZE  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!------------------------------ mlg_suo_suogou_L ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.mlg_suo_suogou_L  &
   adams_id = 201  &
   location = 1.0337216477E+04, 4982.4955993011, 4342.9415786566  &
   orientation = 0.0d, 28.6478897565d, 270.0000000001d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.mlg_suo_suogou_L
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_995  &
   adams_id = 1539  &
   location = 6142.8134765625, 0.0, 391.4468383789  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_995  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1334  &
   adams_id = 1334  &
   location = 6142.8134765625, 0.0, 391.4468383789  &
   orientation = 179.9999998281d, 90.0000001231d, 29.6200322163d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1334  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1337  &
   adams_id = 1337  &
   location = 6145.9420208936, -8.0000000107, 366.9476096035  &
   orientation = 269.9999999999d, 28.6478897565d, 180.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1337  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1339  &
   adams_id = 1339  &
   location = 6145.9420208936, 7.9999999893, 366.9476096035  &
   orientation = 269.9999999999d, 28.6478897565d, 180.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1339  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_514  &
   adams_id = 1540  &
   location = 6152.0, -6.0, 387.0  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_514  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_520  &
   adams_id = 1541  &
   location = 6146.9, -6.0, 364.6  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_520  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1135  &
   adams_id = 1542  &
   location = 6142.8134765625, 0.0, 391.4468383789  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1135  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1136  &
   adams_id = 1543  &
   location = 6110.8091591519, 1.4961334447E-10, 366.1605642471  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1136  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1137  &
   adams_id = 1544  &
   location = 6136.8493067665, 7.3181002209E-11, 358.561755459  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1137  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1138  &
   adams_id = 1545  &
   location = 6146.8999999999, 5.9999999999, 359.5999999999  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1138  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1139  &
   adams_id = 1546  &
   location = 6181.8999999999, -5.9999999997, 359.5999999997  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1139  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.cm  &
   adams_id = 1547  &
   location = 6153.0350282156, -6.9808220123E-11, 374.4685142105  &
   orientation = 90.0000000004d, 79.6996199096d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1140  &
   adams_id = 1548  &
   location = 6181.9, -5.9999999997, 364.5999999996  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1140  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1141  &
   adams_id = 1549  &
   location = 6146.9, -6.0, 364.6  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1141  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1007  &
   adams_id = 1550  &
   location = 6110.8091591519, 1.4961334447E-10, 366.1605642471  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1007  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1142  &
   adams_id = 1553  &
   location = 6151.9999999999, -6.0, 382.0  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1142  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1143  &
   adams_id = 1554  &
   location = 6194.0, -5.9999999996, 381.9999999995  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1143  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1144  &
   adams_id = 1555  &
   location = 6193.9999999999, 6.0000000005, 386.9999999995  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1144  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.mlg_suo_suogou_L  &
   material_type = .template_6_force.steel
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_6_force.mlg_suo_suogou_L.PT200  &
   location = 6142.8134765625, 0.0, 391.4468383789
!
point attributes  &
   point_name = .template_6_force.mlg_suo_suogou_L.PT200  &
   name_visibility = off  &
   size_of_icons = 25.0
!
! ****** Graphics for current part ******
!
geometry create shape block  &
   block_name = .template_6_force.mlg_suo_suogou_L.BOX_268  &
   adams_id = 785  &
   corner_marker = .template_6_force.mlg_suo_suogou_L.MARKER_514  &
   diag_corner_coords = 42.0, 5.0, 12.0
!
geometry create shape block  &
   block_name = .template_6_force.mlg_suo_suogou_L.BOX_272  &
   adams_id = 786  &
   corner_marker = .template_6_force.mlg_suo_suogou_L.MARKER_520  &
   diag_corner_coords = 35.0, 5.0, 12.0
!
geometry create shape plate  &
   plate_name = .template_6_force.mlg_suo_suogou_L.PLATE_515  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1135,  &
                 .template_6_force.mlg_suo_suogou_L.MARKER_1136,  &
                 .template_6_force.mlg_suo_suogou_L.MARKER_1137,  &
                 .template_6_force.mlg_suo_suogou_L.MARKER_1138,  &
                 .template_6_force.mlg_suo_suogou_L.MARKER_1139,  &
                 .template_6_force.mlg_suo_suogou_L.MARKER_1140,  &
                 .template_6_force.mlg_suo_suogou_L.MARKER_1141,  &
                 .template_6_force.mlg_suo_suogou_L.MARKER_1142,  &
                 .template_6_force.mlg_suo_suogou_L.MARKER_1143,  &
                 .template_6_force.mlg_suo_suogou_L.MARKER_1144  &
   width = 15.0  &
   radius = 1.0
!
part attributes  &
   part_name = .template_6_force.mlg_suo_suogou_L  &
   color = GREEN  &
   size_of_icons = 25.0
!
!------------------------------- nlg_suo_suogou -------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part create rigid_body name_and_position  &
   part_name = .template_6_force.nlg_suo_suogou  &
   adams_id = 142  &
   location = -410.6821227386, -2.0665186286E-08, 4532.9415786566  &
   orientation = 90.0000000001d, 28.6478897565d, 270.0000000001d
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.nlg_suo_suogou
!
! ****** Markers for current part ******
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_995  &
   adams_id = 995  &
   location = 6142.8134765625, 0.0, 391.4468383789  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_995  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_514  &
   adams_id = 514  &
   location = 6152.0, -6.0, 387.0  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_514  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_520  &
   adams_id = 520  &
   location = 6146.9, -6.0, 364.6  &
   orientation = 180.0000000006d, 90.0000000003d, 180.0000000006d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_520  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1135  &
   adams_id = 1135  &
   location = 6142.8134765625, 0.0, 391.4468383789  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1135  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1136  &
   adams_id = 1136  &
   location = 6110.8091591519, 1.4961334447E-10, 366.1605642471  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1136  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1137  &
   adams_id = 1137  &
   location = 6136.8493067665, 7.3181002209E-11, 358.561755459  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1137  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1138  &
   adams_id = 1138  &
   location = 6146.8999999999, 5.9999999999, 359.5999999999  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1138  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1139  &
   adams_id = 1139  &
   location = 6181.8999999999, -5.9999999997, 359.5999999997  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1139  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.cm  &
   adams_id = 461  &
   location = 6153.0350282156, -7.0269117814E-11, 374.4685142105  &
   orientation = 90.0000000004d, 79.6996199099d, 0.0d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.cm  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1140  &
   adams_id = 1140  &
   location = 6181.9, -5.9999999997, 364.5999999996  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1140  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1141  &
   adams_id = 1141  &
   location = 6146.9, -6.0, 364.6  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1141  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1007  &
   adams_id = 1007  &
   location = 6110.8091591519, 1.4961334447E-10, 366.1605642471  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1007  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1069  &
   adams_id = 1069  &
   location = 6142.8134765625, 0.0, 391.4468383789  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1069  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1383  &
   adams_id = 1383  &
   location = 6135.8975052716, -7.9999999998, 372.1303493358  &
   orientation = 269.9999999999d, 28.6478897565d, 89.9999999999d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1383  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1142  &
   adams_id = 1142  &
   location = 6151.9999999999, -6.0, 382.0  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1142  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1143  &
   adams_id = 1143  &
   location = 6194.0, -5.9999999996, 381.9999999995  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1143  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1144  &
   adams_id = 1144  &
   location = 6193.9999999999, 6.0000000005, 386.9999999995  &
   orientation = 180.0000000002d, 90.0000000005d, 151.352110244d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1144  &
   size_of_icons = 25.0
!
marker create  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1385  &
   adams_id = 1385  &
   location = 6135.8975052717, 8.0000000002, 372.1303493358  &
   orientation = 269.9999999999d, 28.6478897565d, 89.9999999999d
!
marker attributes  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1385  &
   size_of_icons = 25.0
!
part create rigid_body mass_properties  &
   part_name = .template_6_force.nlg_suo_suogou  &
   material_type = .template_6_force.steel
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_6_force.nlg_suo_suogou.PT200  &
   location = 6142.8134765625, 0.0, 391.4468383789
!
point attributes  &
   point_name = .template_6_force.nlg_suo_suogou.PT200  &
   name_visibility = off  &
   size_of_icons = 25.0
!
point create  &
   point_name = .template_6_force.nlg_suo_suogou.PT201  &
   location = 6142.8134765625, 0.0, 391.4468383789
!
point attributes  &
   point_name = .template_6_force.nlg_suo_suogou.PT201  &
   name_visibility = off  &
   size_of_icons = 25.0
!
! ****** Graphics for current part ******
!
geometry create shape block  &
   block_name = .template_6_force.nlg_suo_suogou.BOX_268  &
   adams_id = 268  &
   corner_marker = .template_6_force.nlg_suo_suogou.MARKER_514  &
   diag_corner_coords = 42.0, 5.0, 12.0
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_suo_suogou.BOX_268  &
   color = YELLOW
!
geometry create shape block  &
   block_name = .template_6_force.nlg_suo_suogou.BOX_272  &
   adams_id = 272  &
   corner_marker = .template_6_force.nlg_suo_suogou.MARKER_520  &
   diag_corner_coords = 35.0, 5.0, 12.0
!
geometry attributes  &
   geometry_name = .template_6_force.nlg_suo_suogou.BOX_272  &
   color = YELLOW
!
geometry create shape plate  &
   plate_name = .template_6_force.nlg_suo_suogou.PLATE_515  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1135,  &
                 .template_6_force.nlg_suo_suogou.MARKER_1136,  &
                 .template_6_force.nlg_suo_suogou.MARKER_1137,  &
                 .template_6_force.nlg_suo_suogou.MARKER_1138,  &
                 .template_6_force.nlg_suo_suogou.MARKER_1139,  &
                 .template_6_force.nlg_suo_suogou.MARKER_1140,  &
                 .template_6_force.nlg_suo_suogou.MARKER_1141,  &
                 .template_6_force.nlg_suo_suogou.MARKER_1142,  &
                 .template_6_force.nlg_suo_suogou.MARKER_1143,  &
                 .template_6_force.nlg_suo_suogou.MARKER_1144  &
   width = 15.0  &
   radius = 1.0
!
part attributes  &
   part_name = .template_6_force.nlg_suo_suogou  &
   color = GREEN  &
   size_of_icons = 25.0
!
!---------------------------------- Contacts ----------------------------------!
!
!
contact create  &
   contact_name = .template_6_force.CONTACT_40  &
   adams_id = 40  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.nlg_suo_actuator.CYLINDER_572  &
   j_geometry_name = .template_6_force.nlg_suo_rod.ELLIPSOID_500  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_40  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.NLG_CONTACT_down  &
   adams_id = 11  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.nlg_suo_suogou.BOX_272  &
   j_geometry_name = .template_6_force.nlg_lower_cylinder.suo_qiu  &
   stiffness = 1.0E+06  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 1.0
!
force attributes  &
   force_name = .template_6_force.NLG_CONTACT_down  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_23  &
   adams_id = 23  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.nlg_suo_rod.ELLIPSOID_500  &
   j_geometry_name = .template_6_force.nlg_suo_actuator.BOX_502  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_23  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.NLG_CONTACT_up  &
   adams_id = 6  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.nlg_lower_cylinder.suo_qiu  &
   j_geometry_name = .template_6_force.nlg_suo_suogou.BOX_268  &
   stiffness = 1.0E+06  &
   damping = 100.0  &
   exponent = 2.2  &
   dmax = 1.0
!
force attributes  &
   force_name = .template_6_force.NLG_CONTACT_up  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_28  &
   adams_id = 28  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.nlg_suo_actuator.CYLINDER_572  &
   j_geometry_name = .template_6_force.nlg_suo_rod.ELLIPSOID_500  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_28  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_30  &
   adams_id = 30  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.nlg_suo_yaobi.BOX_632  &
   j_geometry_name = .template_6_force.nlg_suo_rod.nlg_suo_rod_n  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_30  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_31_L  &
   adams_id = 31  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_suo_yaobi_L.BOX_611  &
   j_geometry_name = .template_6_force.mlg_suo_rod_L.nlg_suo_rod_n  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_31_L  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_29_L  &
   adams_id = 29  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_struct_L.ELLIPSOID_325  &
   j_geometry_name = .template_6_force.mlg_suo_suogou_L.BOX_268  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_29_L  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_23_L  &
   adams_id = 32  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_suo_rod_L.ELLIPSOID_500  &
   j_geometry_name = .template_6_force.mlg_suo_actuator_L.BOX_502  &
   stiffness = 1.0E+08  &
   damping = 1.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_23_L  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_30_L  &
   adams_id = 33  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_suo_suogou_L.BOX_272  &
   j_geometry_name = .template_6_force.mlg_struct_L.ELLIPSOID_325  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_30_L  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_28_L  &
   adams_id = 34  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_suo_actuator_L.CYLINDER_572  &
   j_geometry_name = .template_6_force.mlg_suo_rod_L.ELLIPSOID_500  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_28_L  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_31_R  &
   adams_id = 35  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_suo_yaobi_R.BOX_611  &
   j_geometry_name = .template_6_force.mlg_suo_rod_R.nlg_suo_rod_n  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_31_R  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_29_R  &
   adams_id = 36  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_struct_R.ELLIPSOID_325  &
   j_geometry_name = .template_6_force.mlg_suo_suogou_R.BOX_268  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_29_R  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_23_R  &
   adams_id = 37  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_suo_rod_R.ELLIPSOID_500  &
   j_geometry_name = .template_6_force.mlg_suo_actuator_R.BOX_502  &
   stiffness = 1.0E+08  &
   damping = 1.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_23_R  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_30_R  &
   adams_id = 38  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_suo_suogou_R.BOX_272  &
   j_geometry_name = .template_6_force.mlg_struct_R.ELLIPSOID_325  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_30_R  &
   size_of_icons = 25.0
!
contact create  &
   contact_name = .template_6_force.CONTACT_28_R  &
   adams_id = 39  &
   type = solid_to_solid  &
   i_geometry_name = .template_6_force.mlg_suo_actuator_R.CYLINDER_572  &
   j_geometry_name = .template_6_force.mlg_suo_rod_R.ELLIPSOID_500  &
   stiffness = 1.0E+07  &
   damping = 10.0  &
   exponent = 2.2  &
   dmax = 0.1
!
force attributes  &
   force_name = .template_6_force.CONTACT_28_R  &
   size_of_icons = 25.0
!
!----------------------------------- Joints -----------------------------------!
!
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_93  &
   adams_id = 93  &
   i_marker_name = .template_6_force.nlg_suo_suogou.MARKER_995  &
   j_marker_name = .template_6_force.ground.MARKER_996
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_93  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.josrev_uc_sf_joint  &
   adams_id = 51  &
   i_marker_name = .template_6_force.nlg_upper_cylinder.MARKER_516  &
   j_marker_name = .template_6_force.nlg_subframe.MARKER_517
!
constraint attributes  &
   constraint_name = .template_6_force.josrev_uc_sf_joint  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_97  &
   adams_id = 97  &
   i_marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1028  &
   j_marker_name = .template_6_force.nlg_suo_liangan.MARKER_1029
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_97  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_6_force.joscyl_lc_uc_joint  &
   adams_id = 7  &
   i_marker_name = .template_6_force.nlg_lower_cylinder.jxs_joint_i_11  &
   j_marker_name = .template_6_force.nlg_upper_cylinder.jxs_joint_j_11
!
constraint attributes  &
   constraint_name = .template_6_force.joscyl_lc_uc_joint  &
   visibility = on  &
   size_of_icons = 25.0
!
constraint create joint spherical  &
   joint_name = .template_6_force.jossph_rd_uc  &
   adams_id = 1  &
   i_marker_name = .template_6_force.nlg_upper_cylinder.MARKER_4  &
   j_marker_name = .template_6_force.nlg_sf_rod.MARKER_5
!
constraint attributes  &
   constraint_name = .template_6_force.jossph_rd_uc  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_98  &
   adams_id = 98  &
   i_marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1030  &
   j_marker_name = .template_6_force.ground.MARKER_1031
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_98  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_6_force.mts_fixed_2  &
   adams_id = 9  &
   i_marker_name = .template_6_force.mts_body_mount.mount_i  &
   j_marker_name = .template_6_force.ground.mts_mount_j_2
!
constraint attributes  &
   constraint_name = .template_6_force.mts_fixed_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_6_force.josfix_subframe_to_body  &
   adams_id = 10  &
   i_marker_name = .template_6_force.nlg_subframe.jxs_joint_i_16  &
   j_marker_name = .template_6_force.mts_body_mount.jxs_joint_j_16
!
constraint attributes  &
   constraint_name = .template_6_force.josfix_subframe_to_body  &
   visibility = on  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.joscyl_db_sf  &
   adams_id = 11  &
   i_marker_name = .template_6_force.nlg_sf_actuator.jxs_joint_i_14  &
   j_marker_name = .template_6_force.nlg_subframe.jxs_joint_j_14
!
constraint attributes  &
   constraint_name = .template_6_force.joscyl_db_sf  &
   visibility = on  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.josrev_collar_uc_joint  &
   adams_id = 12  &
   i_marker_name = .template_6_force.nlg_collar.jxs_joint_i_1  &
   j_marker_name = .template_6_force.nlg_upper_cylinder.jxs_joint_j_1
!
constraint attributes  &
   constraint_name = .template_6_force.josrev_collar_uc_joint  &
   visibility = on  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_96  &
   adams_id = 96  &
   i_marker_name = .template_6_force.nlg_suo_liangan.MARKER_1006  &
   j_marker_name = .template_6_force.nlg_suo_suogou.MARKER_1007
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_96  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint cylindrical  &
   joint_name = .template_6_force.joscly_ac_rd  &
   adams_id = 13  &
   i_marker_name = .template_6_force.nlg_sf_rod.MARKER_84  &
   j_marker_name = .template_6_force.nlg_sf_actuator.MARKER_85
!
constraint attributes  &
   constraint_name = .template_6_force.joscly_ac_rd  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_6_force.JOINT_101  &
   adams_id = 101  &
   i_marker_name = .template_6_force.nlg_suo_actuator.MARKER_1103  &
   j_marker_name = .template_6_force.ground.MARKER_1104
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_101  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint cylindrical  &
   joint_name = .template_6_force.JOINT_100  &
   adams_id = 100  &
   i_marker_name = .template_6_force.nlg_suo_rod.MARKER_1097  &
   j_marker_name = .template_6_force.nlg_suo_actuator.MARKER_1098
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_100  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_6_force.JOINT_102  &
   adams_id = 102  &
   i_marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1115  &
   j_marker_name = .template_6_force.ground.MARKER_1116
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_102  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_93_2  &
   adams_id = 103  &
   i_marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_995  &
   j_marker_name = .template_6_force.ground.MARKER_9962
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_93_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_6_force.JOINT_106  &
   adams_id = 106  &
   i_marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1309  &
   j_marker_name = .template_6_force.ground.MARKER_1310
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_106  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_6_force.JOINT_107  &
   adams_id = 107  &
   i_marker_name = .template_6_force.mlg_suo_base_L.MARKER_1329  &
   j_marker_name = .template_6_force.ground.MARKER_1330
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_107  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_97_2  &
   adams_id = 108  &
   i_marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1028  &
   j_marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1029
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_97_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_121  &
   adams_id = 121  &
   i_marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1469  &
   j_marker_name = .template_6_force.ground.MARKER_1470
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_121  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint spherical  &
   joint_name = .template_6_force.JOINT_122  &
   adams_id = 122  &
   i_marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1471  &
   j_marker_name = .template_6_force.mlg_struct_R.MARKER_1472
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_122  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint spherical  &
   joint_name = .template_6_force.JOINT_98_2  &
   adams_id = 123  &
   i_marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1030  &
   j_marker_name = .template_6_force.ground.MARKER_10312
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_98_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_123  &
   adams_id = 124  &
   i_marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1484  &
   j_marker_name = .template_6_force.ground.MARKER_1485
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_123  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_96_2  &
   adams_id = 125  &
   i_marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1006  &
   j_marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1007
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_96_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint translational  &
   joint_name = .template_6_force.JOINT_100_2  &
   adams_id = 126  &
   i_marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1097  &
   j_marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1098
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_100_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint spherical  &
   joint_name = .template_6_force.JOINT_104  &
   adams_id = 104  &
   i_marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1148  &
   j_marker_name = .template_6_force.mlg_struct_L.MARKER_1149
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_104  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_93_2_2  &
   adams_id = 127  &
   i_marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_995  &
   j_marker_name = .template_6_force.ground.MARKER_9961
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_93_2_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_6_force.JOINT_106_2  &
   adams_id = 109  &
   i_marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1309  &
   j_marker_name = .template_6_force.ground.MARKER_13101
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_106_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint fixed  &
   joint_name = .template_6_force.JOINT_107_2  &
   adams_id = 110  &
   i_marker_name = .template_6_force.mlg_suo_base_R.MARKER_1329  &
   j_marker_name = .template_6_force.ground.MARKER_13301
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_107_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_97_2_2  &
   adams_id = 111  &
   i_marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1028  &
   j_marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1029
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_97_2_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint spherical  &
   joint_name = .template_6_force.JOINT_98_2_2  &
   adams_id = 112  &
   i_marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1030  &
   j_marker_name = .template_6_force.ground.MARKER_10311
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_98_2_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_96_2_2  &
   adams_id = 113  &
   i_marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1006  &
   j_marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1007
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_96_2_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint translational  &
   joint_name = .template_6_force.JOINT_100_2_2  &
   adams_id = 114  &
   i_marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1097  &
   j_marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1098
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_100_2_2  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_59_2  &
   adams_id = 117  &
   i_marker_name = .template_6_force.mlg_actuator_R.MARKER_578  &
   j_marker_name = .template_6_force.ground.MARKER_5791
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_59_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint cylindrical  &
   joint_name = .template_6_force.JOINT_56_2  &
   adams_id = 118  &
   i_marker_name = .template_6_force.mlg_actuator_R.MARKER_563  &
   j_marker_name = .template_6_force.mlg_rod_R.MARKER_564
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_56_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint spherical  &
   joint_name = .template_6_force.JOINT_57_2  &
   adams_id = 119  &
   i_marker_name = .template_6_force.mlg_rod_R.MARKER_565  &
   j_marker_name = .template_6_force.mlg_struct_R.MARKER_566
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_57_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_58_2  &
   adams_id = 120  &
   i_marker_name = .template_6_force.ground.MARKER_5671  &
   j_marker_name = .template_6_force.mlg_struct_R.MARKER_568
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_58_2  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_59  &
   adams_id = 59  &
   i_marker_name = .template_6_force.mlg_actuatorL.MARKER_578  &
   j_marker_name = .template_6_force.ground.MARKER_579
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_59  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint cylindrical  &
   joint_name = .template_6_force.JOINT_56  &
   adams_id = 56  &
   i_marker_name = .template_6_force.mlg_actuatorL.MARKER_563  &
   j_marker_name = .template_6_force.mlg_rod_L.MARKER_564
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_56  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint spherical  &
   joint_name = .template_6_force.JOINT_57  &
   adams_id = 57  &
   i_marker_name = .template_6_force.mlg_rod_L.MARKER_565  &
   j_marker_name = .template_6_force.mlg_struct_L.MARKER_566
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_57  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
constraint create joint revolute  &
   joint_name = .template_6_force.JOINT_58  &
   adams_id = 58  &
   i_marker_name = .template_6_force.ground.MARKER_567  &
   j_marker_name = .template_6_force.mlg_struct_L.MARKER_568
!
constraint attributes  &
   constraint_name = .template_6_force.JOINT_58  &
   visibility = on  &
   name_visibility = off  &
   size_of_icons = 25.0
!
!----------------------------------- Forces -----------------------------------!
!
!
force create direct general_force  &
   general_force_name = .template_6_force.NLG_aeroforce  &
   adams_id = 1  &
   i_marker_name = .template_6_force.nlg_upper_cylinder.MARKER_781  &
   j_floating_marker_name = .template_6_force.nlg_lower_cylinder.FMARKER_783  &
   ref_marker_name = .template_6_force.nlg_lower_cylinder.MARKER_782  &
   x_force_function = ""  &
   y_force_function = ""  &
   z_force_function = ""  &
   x_torque_function = ""  &
   y_torque_function = ""  &
   z_torque_function = ""
!
force attributes  &
   force_name = .template_6_force.NLG_aeroforce  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_ZDT_FORCE  &
   adams_id = 3  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.nlg_sf_rod.MARKER_79  &
   j_marker_name = .template_6_force.nlg_sf_rod.MARKER_80  &
   action_only = on  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.nlg_ZDT_FORCE  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_suo_unlock  &
   adams_id = 48  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.nlg_suo_rod.MARKER_1101  &
   j_marker_name = .template_6_force.nlg_suo_actuator.MARKER_1102  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.nlg_suo_unlock  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.NLG_stopper_low  &
   adams_id = 5  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.nlg_sf_rod.MARKER_90  &
   j_marker_name = .template_6_force.nlg_sf_rod.MARKER_91  &
   action_only = on  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.NLG_stopper_low  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_suo_rod_springdamper  &
   adams_id = 47  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.nlg_suo_rod.MARKER_1099  &
   j_marker_name = .template_6_force.nlg_suo_actuator.MARKER_1100  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.nlg_suo_rod_springdamper  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_suo_springF_1  &
   adams_id = 54  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.nlg_suo_liangan.MARKER_1382  &
   j_marker_name = .template_6_force.nlg_suo_suogou.MARKER_1383  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.nlg_suo_springF_1  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_suo_springF_2  &
   adams_id = 55  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.nlg_suo_liangan.MARKER_1384  &
   j_marker_name = .template_6_force.nlg_suo_suogou.MARKER_1385  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.nlg_suo_springF_2  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_unlock_L  &
   adams_id = 56  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1101  &
   j_marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1102  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_suo_unlock_L  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_rod_springdamper_L  &
   adams_id = 57  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1099  &
   j_marker_name = .template_6_force.mlg_suo_actuator_L.MARKER_1100  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_suo_rod_springdamper_L  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_springF_1_L  &
   adams_id = 60  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1336  &
   j_marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1337  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_suo_springF_1_L  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_springF_2_L  &
   adams_id = 61  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1338  &
   j_marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1339  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_suo_springF_2_L  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_stopper_low_R  &
   adams_id = 77  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_rod_R.MARKER_1556  &
   j_marker_name = .template_6_force.mlg_actuator_R.MARKER_1557  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_stopper_low_R  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_unlock_R  &
   adams_id = 62  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1101  &
   j_marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1102  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_suo_unlock_R  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_rod_springdamper_R  &
   adams_id = 63  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1099  &
   j_marker_name = .template_6_force.mlg_suo_actuator_R.MARKER_1100  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_suo_rod_springdamper_R  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_springF_1_R  &
   adams_id = 64  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1336  &
   j_marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1337  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_suo_springF_1_R  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_springF_2_R  &
   adams_id = 65  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1338  &
   j_marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1339  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_suo_springF_2_R  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_stopper_low_L  &
   adams_id = 29  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_rod_L.MARKER_682  &
   j_marker_name = .template_6_force.mlg_actuatorL.MARKER_683  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_stopper_low_L  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_zdtF_L  &
   adams_id = 20  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_actuatorL.MARKER_592  &
   j_marker_name = .template_6_force.mlg_rod_L.MARKER_593  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_zdtF_L  &
   size_of_icons = 25.0
!
force create direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_zdtF_R  &
   adams_id = 68  &
   type_of_freedom = translational  &
   i_marker_name = .template_6_force.mlg_actuator_R.MARKER_592  &
   j_marker_name = .template_6_force.mlg_rod_R.MARKER_593  &
   action_only = off  &
   function = ""
!
force attributes  &
   force_name = .template_6_force.mlg_zdtF_R  &
   size_of_icons = 25.0
!
!----------------------------- Simulation Scripts -----------------------------!
!
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=10.0 step_size=1.0E-02 model_name=.gcmb6_force"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_3  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=.retract_mlg_force"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_2_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_3_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_nlg_post_2hubs"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_2_2_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_4  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=13.0 step_size=1.0E-02 model_name=.retract_suo_force_nlg_mlg"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_2_3  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_3_3  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=.retract_mlg_force"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_2_2_3  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_3_2_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_nlg_post_2hubs"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_2_2_2_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_4_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=13.0 step_size=1.0E-02 model_name=.retract_suo_force_nlg_mlg"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_2_3_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_3_3_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=.retract_mlg_force"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_2_2_3_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_3_2_2_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_nlg_post_2hubs"
!
simulation script create  &
   sim_script_name = .template_6_force.Last_Sim_2_2_2_2_2  &
   commands =   &
              "simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract"
!
!-------------------------- Adams View UDE Instances --------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
undo begin_block suppress = yes
!
ude create instance  &
   instance_name = .template_6_force.NLG_SPRING_nlg  &
   definition_name = .MDI.Forces.spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_6_force.NLG_SPRING_nlg  &
   color = RED
!
ude create instance  &
   instance_name = .template_6_force.nlg_suo_zuni_1  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.NLG_TORSION_SPRING_2  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.nlg_suo_zuni_2  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.NLG_TORSION_SPRING_4  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.mlg_struct_torque_zuni_L  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni2_L  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 1.0337216477E+04, 4571.8134765625, -190.0  &
   orientation = 270.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni1_L  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 0.0, 0.0, 0.0  &
   orientation = 0.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.mlg_struct_torque_zuni_R  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 2.0674681194E+04, 0.0, 0.0  &
   orientation = 180.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni2_R  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 1.0337464717E+04, -4571.8134765625, -190.0  &
   orientation = 90.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni1_R  &
   definition_name = .MDI.Forces.torsion_spring  &
   location = 2.0674681194E+04, 0.0, 0.0  &
   orientation = 180.0, 0.0, 0.0
!
ude create instance  &
   instance_name = .template_6_force.mlg_zdt_springF_R  &
   definition_name = .MDI.Forces.spring  &
   location = 2.2874681194E+04, 0.0, -501.0  &
   orientation = 180.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_6_force.mlg_zdt_springF_R  &
   color = RED
!
ude create instance  &
   instance_name = .template_6_force.mlg_zdt_springF_L  &
   definition_name = .MDI.Forces.spring  &
   location = -1900.0, 0.0, -501.0  &
   orientation = 0.0, 0.0, 0.0
!
ude attributes  &
   instance_name = .template_6_force.mlg_zdt_springF_L  &
   color = RED
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.i_marker  &
   object_value = (.template_6_force.nlg_sf_rod.MARKER_511)
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.j_marker  &
   object_value = (.template_6_force.nlg_sf_actuator.MARKER_512)
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.stiffness_coefficient  &
   real_value = (0.36(newton/mm))
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.damping_coefficient  &
   real_value = 80.0
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.free_length_mode  &
   string_value = "Design_Length"
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.free_length  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.i_dynamic_visibility  &
   string_value = "On"
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.j_dynamic_visibility  &
   string_value = "Off"
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.spring_visibility  &
   string_value = "depends"
!
variable modify  &
   variable_name = .template_6_force.NLG_SPRING_nlg.damper_visibility  &
   string_value = "depends"
!
ude modify instance  &
   instance_name = .template_6_force.NLG_SPRING_nlg
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.i_marker  &
   object_value = (.template_6_force.nlg_suo_yaobi.MARKER_1048)
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.j_marker  &
   object_value = (.template_6_force.ground.MARKER_1049)
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.stiffness_coefficient  &
   real_value = (6.6E-03(newton-mm/rad))
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.damping_coefficient  &
   real_value = 5.0
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_1.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.nlg_suo_zuni_1
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.i_marker  &
   object_value = (.template_6_force.nlg_upper_cylinder.MARKER_526)
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.j_marker  &
   object_value = (.template_6_force.nlg_subframe.MARKER_527)
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.stiffness_coefficient  &
   real_value = (9.7E+04(newton-mm/rad))
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.damping_coefficient  &
   real_value = 10.0
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_2.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.NLG_TORSION_SPRING_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.i_marker  &
   object_value = (.template_6_force.nlg_suo_suogou.MARKER_1069)
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.j_marker  &
   object_value = (.template_6_force.ground.MARKER_1070)
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.stiffness_coefficient  &
   real_value = (0.36(newton-mm/rad))
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.damping_coefficient  &
   real_value = 5.0
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.nlg_suo_zuni_2.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.nlg_suo_zuni_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.i_marker  &
   object_value = (.template_6_force.nlg_sf_actuator.MARKER_532)
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.j_marker  &
   object_value = (.template_6_force.nlg_subframe.MARKER_533)
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.stiffness_coefficient  &
   real_value = (3.5E-05(newton-mm/rad))
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.damping_coefficient  &
   real_value = 10.0
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.NLG_TORSION_SPRING_4.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.NLG_TORSION_SPRING_4
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.i_marker  &
   object_value = (.template_6_force.ground.MARKER_1313)
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.j_marker  &
   object_value = (.template_6_force.mlg_struct_L.MARKER_1314)
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.stiffness_coefficient  &
   real_value = (2617.9938779915(newton-mm/deg))
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.damping_coefficient  &
   real_value = 100.0
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_L.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.mlg_struct_torque_zuni_L
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.i_marker  &
   object_value = (.template_6_force.mlg_suo_yaobi_L.MARKER_1048)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.j_marker  &
   object_value = (.template_6_force.ground.MARKER_10492)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.stiffness_coefficient  &
   real_value = (6.6E-03(newton-mm/rad))
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.damping_coefficient  &
   real_value = 20.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_L.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni2_L
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.i_marker  &
   object_value = (.template_6_force.mlg_suo_suogou_L.MARKER_1334)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.j_marker  &
   object_value = (.template_6_force.ground.MARKER_1335)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.stiffness_coefficient  &
   real_value = (7.5049157836E-03(newton-mm/deg))
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.damping_coefficient  &
   real_value = 20.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_L.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni1_L
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.i_marker  &
   object_value = (.template_6_force.ground.MARKER_13131)
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.j_marker  &
   object_value = (.template_6_force.mlg_struct_R.MARKER_1314)
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.stiffness_coefficient  &
   real_value = (2617.9938779915(newton-mm/deg))
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.damping_coefficient  &
   real_value = 100.0
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.mlg_struct_torque_zuni_R.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.mlg_struct_torque_zuni_R
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.i_marker  &
   object_value = (.template_6_force.mlg_suo_yaobi_R.MARKER_1048)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.j_marker  &
   object_value = (.template_6_force.ground.MARKER_10491)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.stiffness_coefficient  &
   real_value = (6.6E-03(newton-mm/rad))
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.damping_coefficient  &
   real_value = 20.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni2_R.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni2_R
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.i_marker  &
   object_value = (.template_6_force.mlg_suo_suogou_R.MARKER_1334)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.j_marker  &
   object_value = (.template_6_force.ground.MARKER_13351)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.stiffness_coefficient  &
   real_value = (7.5049157836E-03(newton-mm/deg))
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.damping_coefficient  &
   real_value = 20.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.free_angle_mode  &
   string_value = "Design_Angle"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.free_angle  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.i_dynamic_visibility  &
   string_value = "on"
!
variable modify  &
   variable_name = .template_6_force.mlg_suo_torque_zuni1_R.j_dynamic_visibility  &
   string_value = "off"
!
ude modify instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni1_R
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.i_marker  &
   object_value = (.template_6_force.mlg_actuator_R.MARKER_602)
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.j_marker  &
   object_value = (.template_6_force.mlg_rod_R.MARKER_603)
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.stiffness_coefficient  &
   real_value = (0.13(newton/mm))
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.damping_coefficient  &
   real_value = 200.0
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.free_length_mode  &
   string_value = "Design_Length"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.free_length  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.i_dynamic_visibility  &
   string_value = "On"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.j_dynamic_visibility  &
   string_value = "Off"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.spring_visibility  &
   string_value = "depends"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_R.damper_visibility  &
   string_value = "depends"
!
ude modify instance  &
   instance_name = .template_6_force.mlg_zdt_springF_R
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.i_marker  &
   object_value = (.template_6_force.mlg_actuatorL.MARKER_602)
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.j_marker  &
   object_value = (.template_6_force.mlg_rod_L.MARKER_603)
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.stiffness_mode  &
   string_value = "none"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.stiffness_coefficient  &
   real_value = (0.13(newton/mm))
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.stiffness_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.damping_mode  &
   string_value = "linear"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.damping_coefficient  &
   real_value = 200.0
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.damping_spline  &
   object_value = (NONE)
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.free_length_mode  &
   string_value = "Design_Length"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.free_length  &
   real_value = 1.0
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.preload  &
   real_value = 0.0
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.i_dynamic_visibility  &
   string_value = "On"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.j_dynamic_visibility  &
   string_value = "Off"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.spring_visibility  &
   string_value = "depends"
!
variable modify  &
   variable_name = .template_6_force.mlg_zdt_springF_L.damper_visibility  &
   string_value = "depends"
!
ude modify instance  &
   instance_name = .template_6_force.mlg_zdt_springF_L
!
undo end_block
!
!------------------------------ Dynamic Graphics ------------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_3_force_graphic_1  &
   adams_id = 44  &
   force_element_name = .template_6_force.nlg_ZDT_FORCE  &
   applied_at_marker_name = .template_6_force.nlg_sf_rod.MARKER_79
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_48_force_graphic_1  &
   adams_id = 508  &
   force_element_name = .template_6_force.nlg_suo_unlock  &
   applied_at_marker_name = .template_6_force.nlg_suo_rod.MARKER_1101
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_47_force_graphic_1  &
   adams_id = 507  &
   force_element_name = .template_6_force.nlg_suo_rod_springdamper  &
   applied_at_marker_name = .template_6_force.nlg_suo_rod.MARKER_1099
!
geometry create shape force  &
   force_name = .template_6_force.GFORCE_1_force_graphic_1  &
   adams_id = 463  &
   force_element_name = .template_6_force.NLG_aeroforce  &
   applied_at_marker_name = .template_6_force.nlg_upper_cylinder.MARKER_781
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_5_force_graphic_1  &
   adams_id = 46  &
   force_element_name = .template_6_force.NLG_stopper_low  &
   applied_at_marker_name = .template_6_force.nlg_sf_rod.MARKER_90
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_54_force_graphic_1  &
   adams_id = 681  &
   force_element_name = .template_6_force.nlg_suo_springF_1  &
   applied_at_marker_name = .template_6_force.nlg_suo_liangan.MARKER_1382
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_55_force_graphic_1  &
   adams_id = 682  &
   force_element_name = .template_6_force.nlg_suo_springF_2  &
   applied_at_marker_name = .template_6_force.nlg_suo_liangan.MARKER_1384
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_48_force_graphic_1_2  &
   adams_id = 787  &
   force_element_name = .template_6_force.mlg_suo_unlock_L  &
   applied_at_marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1101
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_47_force_graphic_1_2  &
   adams_id = 788  &
   force_element_name = .template_6_force.mlg_suo_rod_springdamper_L  &
   applied_at_marker_name = .template_6_force.mlg_suo_rod_L.MARKER_1099
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_60_force_graphic_1  &
   adams_id = 711  &
   force_element_name = .template_6_force.mlg_suo_springF_1_L  &
   applied_at_marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1336
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_61_force_graphic_1  &
   adams_id = 712  &
   force_element_name = .template_6_force.mlg_suo_springF_2_L  &
   applied_at_marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1338
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_48_force_graphic_1_2_2  &
   adams_id = 732  &
   force_element_name = .template_6_force.mlg_suo_unlock_R  &
   applied_at_marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1101
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_47_force_graphic_1_2_2  &
   adams_id = 733  &
   force_element_name = .template_6_force.mlg_suo_rod_springdamper_R  &
   applied_at_marker_name = .template_6_force.mlg_suo_rod_R.MARKER_1099
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_60_force_graphic_1_2  &
   adams_id = 734  &
   force_element_name = .template_6_force.mlg_suo_springF_1_R  &
   applied_at_marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1336
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_61_force_graphic_1_2  &
   adams_id = 735  &
   force_element_name = .template_6_force.mlg_suo_springF_2_R  &
   applied_at_marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1338
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_20_force_graphic_1_2  &
   adams_id = 736  &
   force_element_name = .template_6_force.mlg_zdtF_R  &
   applied_at_marker_name = .template_6_force.mlg_actuator_R.MARKER_592
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_20_force_graphic_1  &
   adams_id = 326  &
   force_element_name = .template_6_force.mlg_zdtF_L  &
   applied_at_marker_name = .template_6_force.mlg_actuatorL.MARKER_592
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_29_force_graphic_1  &
   adams_id = 395  &
   force_element_name = .template_6_force.mlg_stopper_low_L  &
   applied_at_marker_name = .template_6_force.mlg_rod_L.MARKER_682
!
geometry create shape force  &
   force_name = .template_6_force.SFORCE_77_force_graphic_1  &
   adams_id = 825  &
   force_element_name = .template_6_force.mlg_stopper_low_R  &
   applied_at_marker_name = .template_6_force.mlg_rod_R.MARKER_1556
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_828  &
   adams_id = 828  &
   contact_element_name = .template_6_force.CONTACT_40  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_303  &
   adams_id = 303  &
   contact_element_name = .template_6_force.NLG_CONTACT_down  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_505  &
   adams_id = 505  &
   contact_element_name = .template_6_force.CONTACT_23  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_271  &
   adams_id = 271  &
   contact_element_name = .template_6_force.NLG_CONTACT_up  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_579  &
   adams_id = 579  &
   contact_element_name = .template_6_force.CONTACT_28  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_638  &
   adams_id = 638  &
   contact_element_name = .template_6_force.CONTACT_30  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_633  &
   adams_id = 633  &
   contact_element_name = .template_6_force.CONTACT_31_L  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_582  &
   adams_id = 582  &
   contact_element_name = .template_6_force.CONTACT_29_L  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_505_2  &
   adams_id = 789  &
   contact_element_name = .template_6_force.CONTACT_23_L  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_585  &
   adams_id = 585  &
   contact_element_name = .template_6_force.CONTACT_30_L  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_579_2  &
   adams_id = 790  &
   contact_element_name = .template_6_force.CONTACT_28_L  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_633_2  &
   adams_id = 738  &
   contact_element_name = .template_6_force.CONTACT_31_R  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_582_2  &
   adams_id = 739  &
   contact_element_name = .template_6_force.CONTACT_29_R  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_505_2_2  &
   adams_id = 740  &
   contact_element_name = .template_6_force.CONTACT_23_R  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_585_2  &
   adams_id = 741  &
   contact_element_name = .template_6_force.CONTACT_30_R  &
   force_display = none
!
geometry create shape gcontact  &
   contact_force_name = .template_6_force.GCONTACT_579_2_2  &
   adams_id = 742  &
   contact_element_name = .template_6_force.CONTACT_28_R  &
   force_display = none
!
!---------------------------------- Accgrav -----------------------------------!
!
!
force create body gravitational  &
   gravity_field_name = gravity  &
   x_component_gravity = 0.0  &
   y_component_gravity = 0.0  &
   z_component_gravity = -9806.65
!
force attributes  &
   force_name = .template_6_force.gravity  &
   size_of_icons = 25.0
!
!----------------------------- Analysis settings ------------------------------!
!
!
!---------------------------------- Measures ----------------------------------!
!
!
measure create object  &
   measure_name = .template_6_force.NLG_sf_angle  &
   from_first = yes  &
   object = .template_6_force.josrev_uc_sf_joint  &
   characteristic = ax_ay_az_projection_angles  &
   component = z_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_force.NLG_sf_angle  &
   color = WHITE
!
measure create object  &
   measure_name = .template_6_force.mlg_sf_angle  &
   from_first = yes  &
   object = .template_6_force.JOINT_58  &
   characteristic = ax_ay_az_projection_angles  &
   component = z_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_force.mlg_sf_angle  &
   color = WHITE
!
measure create pt2pt  &
   measure_name = .template_6_force.NLG_disp_sf  &
   from_point = .template_6_force.nlg_sf_rod.MARKER_96  &
   to_point = .template_6_force.nlg_sf_actuator.MARKER_97  &
   characteristic = translational_displacement  &
   component = mag_component  &
   create_measure_display = no
!
data_element attributes  &
   data_element_name = .template_6_force.NLG_disp_sf  &
   color = WHITE
!
!---------------------------- Adams View Variables ----------------------------!
!
!
variable create  &
   variable_name = .template_6_force.mts_body_mount.minor_role  &
   string_value = "inherit"
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
!---------------------------- Function definitions ----------------------------!
!
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_ZDT_FORCE  &
   function = "STEP( time , 0 , 0 , .template_6_force.nlg_zdtup_t1 , .template_6_force.NLG_RETRACT_FORCE )+STEP( time , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME , 0 , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3 , -.template_6_force.NLG_RETRACT_FORCE )+STEP( time , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3+.template_6_force.nlg_zdt_t0 , 0 , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3+.template_6_force.nlg_zdt_t0+.template_6_force.nlg_zdtdown_t1 , -.template_6_force.NLG_EXTEND_FORCE )+STEP( time , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3+.template_6_force.nlg_zdt_t0+.template_6_force.nlg_zdtdown_t1+.template_6_force.NLG_EXTEND_HOLD_TIME , 0 , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3+.template_6_force.nlg_zdt_t0+.template_6_force.nlg_zdtdown_t1+.template_6_force.NLG_EXTEND_HOLD_TIME+.template_6_force.nlg_zdtdown_t3 , .template_6_force.NLG_EXTEND_FORCE )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_suo_unlock  &
   function = "STEP( time , .template_6_force.NLG_LOCK_UNLOCK_TIME , 0 , .template_6_force.NLG_LOCK_UNLOCK_TIME+0.1 , -.template_6_force.NLG_UNLOCK_FORCE )+STEP( time , .template_6_force.NLG_LOCK_UNLOCK_TIME+1.0 , 0 , .template_6_force.NLG_LOCK_UNLOCK_TIME+1.1 , .template_6_force.NLG_UNLOCK_FORCE )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.NLG_stopper_low  &
   function = "-abs(IF( .template_6_force.NLG_disp_sf-1217.6474 :50000000000*abs(.template_6_force.NLG_disp_sf-1217.6474), 0 ,0 ))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_suo_rod_springdamper  &
   function = "-10.0*VR(.template_6_force.nlg_suo_rod.MARKER_1099,.template_6_force.nlg_suo_actuator.MARKER_1100)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_suo_springF_1  &
   function = "-.template_6_force.NLG_LOCK_SPRING_K*(DM(.template_6_force.nlg_suo_liangan.MARKER_1382,.template_6_force.nlg_suo_suogou.MARKER_1383)-54.0458262355)-.template_6_force.NLG_LOCK_SPRING_C*VR(.template_6_force.nlg_suo_liangan.MARKER_1382,.template_6_force.nlg_suo_suogou.MARKER_1383)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.nlg_suo_springF_2  &
   function = "-.template_6_force.NLG_LOCK_SPRING_K*(DM(.template_6_force.nlg_suo_liangan.MARKER_1384,.template_6_force.nlg_suo_suogou.MARKER_1385)-54.0458262355)-.template_6_force.NLG_LOCK_SPRING_C*VR(.template_6_force.nlg_suo_liangan.MARKER_1384,.template_6_force.nlg_suo_suogou.MARKER_1385)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_unlock_L  &
   function = "STEP( time , .template_6_force.MLG_LOCK_UNLOCK_TIME , 0 , .template_6_force.MLG_LOCK_UNLOCK_TIME+0.1 , -.template_6_force.MLG_UNLOCK_FORCE )+STEP( time , .template_6_force.MLG_LOCK_UNLOCK_TIME+1.0 , 0 , .template_6_force.MLG_LOCK_UNLOCK_TIME+1.1 , .template_6_force.MLG_UNLOCK_FORCE )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_rod_springdamper_L  &
   function = "-10.0*VR(.template_6_force.mlg_suo_rod_L.MARKER_1099,.template_6_force.mlg_suo_actuator_L.MARKER_1100)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_springF_1_L  &
   function = "-.template_6_force.MLG_LOCK_SPRING_K*(DM(.template_6_force.mlg_suo_liangan_L.MARKER_1336,.template_6_force.mlg_suo_suogou_L.MARKER_1337)-60.0749531835)-.template_6_force.MLG_LOCK_SPRING_C*VR(.template_6_force.mlg_suo_liangan_L.MARKER_1336,.template_6_force.mlg_suo_suogou_L.MARKER_1337)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_springF_2_L  &
   function = "-.template_6_force.MLG_LOCK_SPRING_K*(DM(.template_6_force.mlg_suo_liangan_L.MARKER_1338,.template_6_force.mlg_suo_suogou_L.MARKER_1339)-60.0749531835)-.template_6_force.MLG_LOCK_SPRING_C*VR(.template_6_force.mlg_suo_liangan_L.MARKER_1338,.template_6_force.mlg_suo_suogou_L.MARKER_1339)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_stopper_low_R  &
   function = "abs(IF(.template_6_force.mlg_sf_angle+0.1 :0, 0 ,10000000*abs(.template_6_force.mlg_sf_angle+0.1) ))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_unlock_R  &
   function = "STEP( time , .template_6_force.MLG_LOCK_UNLOCK_TIME , 0 , .template_6_force.MLG_LOCK_UNLOCK_TIME+0.1 , -.template_6_force.MLG_UNLOCK_FORCE )+STEP( time , .template_6_force.MLG_LOCK_UNLOCK_TIME+1.0 , 0 , .template_6_force.MLG_LOCK_UNLOCK_TIME+1.1 , .template_6_force.MLG_UNLOCK_FORCE )"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_rod_springdamper_R  &
   function = "-10.0*VR(.template_6_force.mlg_suo_rod_R.MARKER_1099,.template_6_force.mlg_suo_actuator_R.MARKER_1100)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_springF_1_R  &
   function = "-.template_6_force.MLG_LOCK_SPRING_K*(DM(.template_6_force.mlg_suo_liangan_R.MARKER_1336,.template_6_force.mlg_suo_suogou_R.MARKER_1337)-60.0749531835)-.template_6_force.MLG_LOCK_SPRING_C*VR(.template_6_force.mlg_suo_liangan_R.MARKER_1336,.template_6_force.mlg_suo_suogou_R.MARKER_1337)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_suo_springF_2_R  &
   function = "-.template_6_force.MLG_LOCK_SPRING_K*(DM(.template_6_force.mlg_suo_liangan_R.MARKER_1338,.template_6_force.mlg_suo_suogou_R.MARKER_1339)-60.0749531835)-.template_6_force.MLG_LOCK_SPRING_C*VR(.template_6_force.mlg_suo_liangan_R.MARKER_1338,.template_6_force.mlg_suo_suogou_R.MARKER_1339)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_stopper_low_L  &
   function = "abs(IF(.template_6_force.mlg_sf_angle+0.1 :0, 0 ,10000000*abs(.template_6_force.mlg_sf_angle+0.1) ))"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_zdtF_L  &
   function = "STEP( time , 0 , 0 , .template_6_force.mlg_zdtup_t1 , .template_6_force.MLG_RETRACT_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3 , -.template_6_force.MLG_RETRACT_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0 , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1 , -.template_6_force.MLG_EXTEND_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1+.template_6_force.MLG_EXTEND_HOLD_TIME , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1+.template_6_force.MLG_EXTEND_HOLD_TIME+.template_6_force.mlg_zdtdown_t3 ,.template_6_force.MLG_EXTEND_FORCE)"
!
force modify direct single_component_force  &
   single_component_force_name = .template_6_force.mlg_zdtF_R  &
   function = "STEP( time , 0 , 0 , .template_6_force.mlg_zdtup_t1 , .template_6_force.MLG_RETRACT_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3 , -.template_6_force.MLG_RETRACT_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0 , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1 , -.template_6_force.MLG_EXTEND_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1+.template_6_force.MLG_EXTEND_HOLD_TIME , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1+.template_6_force.MLG_EXTEND_HOLD_TIME+.template_6_force.mlg_zdtdown_t3 ,.template_6_force.MLG_EXTEND_FORCE)"
!
force modify direct general_force  &
   general_force_name = .template_6_force.NLG_aeroforce  &
   x_force_function = ".template_6_force.NLG_DRAG_COEFF*abs(IF( -.template_6_force.NLG_sf_angle-60 : COS( 1.225*-.template_6_force.NLG_sf_angle*pi/180 ) , COS( 1.225*-.template_6_force.NLG_sf_angle*pi/180 ) , COS( -.template_6_force.NLG_sf_angle*pi/180 ) ))*.template_6_force.NLG_PROJ_AREA*cos(-.template_6_force.NLG_sf_angle*pi/180)*0.5*.template_6_force.AIR_DENSITY*.template_6_force.AIR_VELOCITY*abs(.template_6_force.AIR_VELOCITY)*cos(-.template_6_force.NLG_sf_angle*pi/180) "  &
   y_force_function = "0"  &
   z_force_function = ".template_6_force.NLG_DRAG_COEFF*abs(IF( -.template_6_force.NLG_sf_angle-60 : COS( 1.225*-.template_6_force.NLG_sf_angle*pi/180 ) , COS( 1.225*-.template_6_force.NLG_sf_angle*pi/180 ) , COS( -.template_6_force.NLG_sf_angle*pi/180 ) ))*.template_6_force.NLG_PROJ_AREA*cos(-.template_6_force.NLG_sf_angle*pi/180)*0.5*.template_6_force.AIR_DENSITY*.template_6_force.AIR_VELOCITY*abs(.template_6_force.AIR_VELOCITY)*sin(-.template_6_force.NLG_sf_angle*pi/180) "  &
   x_torque_function = "0"  &
   y_torque_function = "-1*CUBSPL( -1*.template_6_force.NLG_sf_angle, 0 , .template_6_force.SPLINE_angle_aeroforce, 0 )"  &
   z_torque_function = "0"
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.NLG_SPRING_nlg
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.nlg_suo_zuni_1
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.NLG_TORSION_SPRING_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.nlg_suo_zuni_2
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.NLG_TORSION_SPRING_4
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.mlg_struct_torque_zuni_L
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni2_L
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni1_L
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.mlg_struct_torque_zuni_R
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni2_R
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.mlg_suo_torque_zuni1_R
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.mlg_zdt_springF_R
!
!-------------------------- Adams View UDE Instance ---------------------------!
!
!
ude modify instance  &
   instance_name = .template_6_force.mlg_zdt_springF_L
!
!--------------------------- Expression definitions ---------------------------!
!
!
defaults coordinate_system  &
   default_coordinate_system = ground
!
marker modify  &
   marker_name = .template_6_force.ground.mts_mount_j_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mts_body_mount))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_force.mts_body_mount))
!
marker modify  &
   marker_name = .template_6_force.ground.cfs_collar_top  &
   location =   &
      (LOC_ALONG_LINE(.template_6_force.ground.hps_uc_bot, .template_6_force.ground.hps_uc_top, 0.11 * DM(.template_6_force.ground.hps_uc_bot, .template_6_force.ground.hps_uc_top)))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_uc_bot, .template_6_force.ground.hps_uc_top, "Z"))
!
marker modify  &
   marker_name = .template_6_force.ground.MARKER_996  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_suo_suogou.PT200))
!
marker modify  &
   marker_name = .template_6_force.ground.MARKER_1031  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_483))
!
marker modify  &
   marker_name = .template_6_force.ground.MARKER_1049  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_483))
!
marker modify  &
   marker_name = .template_6_force.ground.MARKER_1070  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_suo_suogou.PT200))
!
marker modify  &
   marker_name = .template_6_force.ground.MARKER_1313  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_uc_top))
!
marker modify  &
   marker_name = .template_6_force.ground.MARKER_1335  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mlg_suo_suogou_L.PT200))
!
marker modify  &
   marker_name = .template_6_force.ground.MARKER_1470  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_db_top1_2))
!
marker modify  &
   marker_name = .template_6_force.ground.MARKER_1485  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_db_top))
!
material modify  &
   material_name = .template_6_force.steel  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_3  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_3  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_2_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_2_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_3_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_3_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_2_2_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_2_2_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_4  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_4  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_2_3  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_2_3  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_3_3  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_3_3  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_2_2_3  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_2_2_3  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_3_2_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_3_2_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_2_2_2_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_2_2_2_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_4_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_4_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_2_3_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_2_3_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_3_3_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_3_3_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_2_2_3_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_2_2_3_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_3_2_2_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_3_2_2_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.steel_2_2_2_2_2  &
   density = (7801.0(kg/meter**3))  &
   youngs_modulus = (2.07E+11(Newton/meter**2))
!
material modify  &
   material_name = .template_6_force.aluminum_2_2_2_2_2  &
   density = (2740.0(kg/meter**3))  &
   youngs_modulus = (7.1705E+10(Newton/meter**2))
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1374  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_3))  &
   relative_to = .template_6_force.nlg_suo_liangan
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1382  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_spring_slg1))  &
   relative_to = .template_6_force.nlg_suo_liangan
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_liangan.MARKER_1384  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_spring_slg2))  &
   relative_to = .template_6_force.nlg_suo_liangan
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_sf_actuator.gralin_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_db_sf_atch, .template_6_force.ground.hps_db_uc_atch, "Z"))  &
   relative_to = .template_6_force.nlg_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_sf_actuator.jxs_joint_i_14  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_subframe.jxs_joint_j_14))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_subframe.jxs_joint_j_14))  &
   relative_to = .template_6_force.nlg_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_sf_actuator.MARKER_532  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_db_sf_atch))  &
   relative_to = .template_6_force.nlg_sf_actuator
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_sf_actuator.gralin_dragbrace_geom  &
   length = (DM(.template_6_force.ground.hps_db_sf_atch, .template_6_force.ground.hps_db_uc_atch))
!
marker modify  &
   marker_name = .template_6_force.nlg_upper_cylinder.MARKER_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_sf_rod.PT3))  &
   relative_to = .template_6_force.nlg_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_upper_cylinder.gralin_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_uc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_uc_top, .template_6_force.ground.hps_uc_bot, "Z"))  &
   relative_to = .template_6_force.nlg_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_upper_cylinder.gralin_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_uc_sf_atch_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_uc_sf_atch_l, .template_6_force.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_6_force.nlg_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_upper_cylinder.gralin_4  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_uc_sf_atch_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_uc_sf_atch_r, .template_6_force.ground.hps_uc_geompt, "Z"))  &
   relative_to = .template_6_force.nlg_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_upper_cylinder.jxs_joint_j_1  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_force.ground.cfs_collar_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_uc_bot, .template_6_force.ground.hps_uc_top, "Z"))  &
   relative_to = .template_6_force.nlg_upper_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom1  &
   length = (DM(.template_6_force.ground.hps_uc_top, .template_6_force.ground.hps_uc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom2  &
   length = (DM(.template_6_force.ground.hps_uc_sf_atch_l, .template_6_force.ground.hps_uc_geompt))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom3  &
   length = (DM(.template_6_force.ground.hps_uc_sf_atch_r, .template_6_force.ground.hps_uc_geompt))
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_lc_top))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_lc_top, .template_6_force.ground.hps_lc_bot, "Z"))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.jxs_joint_i_11  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_upper_cylinder.jxs_joint_j_11))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_upper_cylinder.jxs_joint_j_11))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_7  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_wheel_center))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hpr_wheel_center, .template_6_force.ground.hpl_wheel_center, "Z"))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_9  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_uta_uc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_uta_uc_atch, .template_6_force.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.gralin_10  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_lta_lc_atch))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_lta_lc_atch, .template_6_force.ground.hps_lta_uta_atch, "Z"))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_359  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_lockroller_l))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_lockroller_l, .template_6_force.ground.hps_lockroller_l_2, "Z"))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_360  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_lockroller_r))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_lockroller_r, .template_6_force.ground.hps_lockroller_r_2, "Z"))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_361  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_lockroller_r_2))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_lockroller_r_2, .template_6_force.ground.hps_lockroller_l_2, "Z"))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_436  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.suo_qiu_point))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_1562  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_ob_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hpl_ob_axle, .template_6_force.ground.hpl_wheel_center, "Z"))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_lower_cylinder.MARKER_1563  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_ob_axle))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hpr_ob_axle, .template_6_force.ground.hpr_wheel_center, "Z"))  &
   relative_to = .template_6_force.nlg_lower_cylinder
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.gralin_geom1  &
   length = (DM(.template_6_force.ground.hps_lc_top, .template_6_force.ground.hps_lc_bot))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.gralin_geom2  &
   length = (DM(.template_6_force.ground.hpr_wheel_center, .template_6_force.ground.hpl_wheel_center))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.CYLINDER_128  &
   length = (73.0mm)  &
   radius = (8.125mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.CYLINDER_132  &
   length = (73.0mm)  &
   radius = (8.125mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.CYLINDER_136  &
   length = (100.0mm)  &
   radius = (7.5mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.gralin_lower_torque_arm_geom  &
   length = (DM(.template_6_force.ground.hps_lta_lc_atch, .template_6_force.ground.hps_lta_uta_atch))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.gralin_upper_torque_arm_geom  &
   length = (DM(.template_6_force.ground.hps_uta_uc_atch, .template_6_force.ground.hps_lta_uta_atch))
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_lower_cylinder.CYLINDER_882  &
   radius = (120mm)
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1027  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_483))  &
   relative_to = .template_6_force.nlg_suo_yaobi
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1030  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_483))  &
   relative_to = .template_6_force.nlg_suo_yaobi
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_yaobi.MARKER_1048  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_483))  &
   relative_to = .template_6_force.nlg_suo_yaobi
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape block  &
   block_name = .template_6_force.nlg_suo_yaobi.BOX_632  &
   diag_corner_coords =   &
      (-3.0mm),  &
      (-24.0mm),  &
      (10.0mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_suo_rod.CYLINDER_499  &
   radius = (1.8mm)
!
geometry modify shape ellipsoid  &
   ellipsoid_name = .template_6_force.nlg_suo_rod.ELLIPSOID_500  &
   x_scale_factor = (2 * 1.8mm)  &
   y_scale_factor = (2 * 1.8mm)  &
   z_scale_factor = (2 * 1.8mm)
!
marker modify  &
   marker_name = .template_6_force.nlg_subframe.inertia_frame  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_subframe.cm))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_subframe))  &
   relative_to = .template_6_force.nlg_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_subframe.graout_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_uc_sf_atch_r))  &
   relative_to = .template_6_force.nlg_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_subframe.graout_2  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_uc_sf_atch_l))  &
   relative_to = .template_6_force.nlg_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_subframe.graout_3  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_db_sf_atch))  &
   relative_to = .template_6_force.nlg_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_subframe.jxs_joint_i_16  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mts_body_mount.jxs_joint_j_16))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_force.mts_body_mount.jxs_joint_j_16))  &
   relative_to = .template_6_force.nlg_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_subframe.jxs_joint_j_14  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_force.ground.hps_db_sf_atch))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 90.0, 0.0}degrees, .template_6_force.ground.origo))  &
   relative_to = .template_6_force.nlg_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_subframe.MARKER_533  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_db_sf_atch))  &
   relative_to = .template_6_force.nlg_subframe
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mts_body_mount.jxs_joint_j_16  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}inch, .template_6_force.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0.0, 0.0, 0.0}degrees, .template_6_force.ground.origo))  &
   relative_to = .template_6_force.mts_body_mount
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
part modify rigid_body name_and_position  &
   part_name = .template_6_force.mts_body_mount  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.cfs_subframe_to_body_point))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.origo))
!
marker modify  &
   marker_name = .template_6_force.nlg_collar.gralin_24  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_uc_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.ground.hps_uc_bot, .template_6_force.ground.cfs_collar_top, "Z"))  &
   relative_to = .template_6_force.nlg_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_collar.jxs_joint_i_1  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_upper_cylinder.jxs_joint_j_1))  &
   orientation =   &
      (ORI_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_upper_cylinder.jxs_joint_j_1))  &
   relative_to = .template_6_force.nlg_collar
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_collar.gralin_collar  &
   length = (DM(.template_6_force.ground.hps_uc_bot, .template_6_force.ground.cfs_collar_top))
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1105  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_483))  &
   relative_to = .template_6_force.nlg_suo_rod_base
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_rod_base.MARKER_1113  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_suo_suogou.PT200))  &
   relative_to = .template_6_force.nlg_suo_rod_base
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape plate  &
   plate_name = .template_6_force.nlg_suo_rod_base.PLATE_509  &
   radius = (2.0mm)
!
marker modify  &
   marker_name = .template_6_force.nlg_sf_rod.MARKER_5  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_sf_rod.PT3))  &
   relative_to = .template_6_force.nlg_sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_sf_rod.gralin_25  &
   location =   &
      (LOC_RELATIVE_TO({0.0, 0.0, 0.0}, .template_6_force.ground.hps_rod_bot))  &
   orientation =   &
      (ORI_ALONG_AXIS(.template_6_force.nlg_sf_rod.PT3, .template_6_force.ground.hps_db_sf_atch, "Z"))  &
   relative_to = .template_6_force.nlg_sf_rod
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.nlg_sf_rod.CYLINDER_30  &
   length = (DM(.template_6_force.ground.hps_rod_bot, .template_6_force.ground.hps_rod_top))  &
   radius = (27.5mm)
!
geometry modify shape block  &
   block_name = .template_6_force.nlg_suo_actuator.BOX_502  &
   diag_corner_coords =   &
      (18.0mm),  &
      (10.0mm),  &
      (12.0mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1336  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.mlg_suo_spring_lg1))  &
   relative_to = .template_6_force.mlg_suo_liangan_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_1338  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.mlg_suo_spring_lg2))  &
   relative_to = .template_6_force.mlg_suo_liangan_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_liangan_L.MARKER_998  &
   location =   &
      (LOC_RELATIVE_TO({-4.3751313683E-07, -1.0769163339E-11, 0.0}, .template_6_force.ground.POINT_636))  &
   relative_to = .template_6_force.mlg_suo_liangan_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape plate  &
   plate_name = .template_6_force.mlg_suo_liangan_L.PLATE_464  &
   width = (5.0mm)  &
   radius = (2.0mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1468  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_db_top1_2))  &
   relative_to = .template_6_force.mlg_dragbrace_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_dragbrace_R.MARKER_1469  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_db_top1_2))  &
   relative_to = .template_6_force.mlg_dragbrace_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1027  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_4832))  &
   relative_to = .template_6_force.mlg_suo_yaobi_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1030  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_4832))  &
   relative_to = .template_6_force.mlg_suo_yaobi_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_yaobi_L.MARKER_1048  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_4832))  &
   relative_to = .template_6_force.mlg_suo_yaobi_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape block  &
   block_name = .template_6_force.mlg_suo_yaobi_L.BOX_611  &
   diag_corner_coords =   &
      (-3.0mm),  &
      (-24.0mm),  &
      (6.0mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_suo_rod_L.CYLINDER_499  &
   radius = (1.8mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1105  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_4832))  &
   relative_to = .template_6_force.mlg_suo_base_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_base_L.MARKER_1113  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mlg_suo_suogou_L.PT200))  &
   relative_to = .template_6_force.mlg_suo_base_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape plate  &
   plate_name = .template_6_force.mlg_suo_base_L.PLATE_509  &
   radius = (2.0mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1484  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_db_top))  &
   relative_to = .template_6_force.mlg_dragbrace_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_dragbrace_L.MARKER_1145  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_db_top))  &
   relative_to = .template_6_force.mlg_dragbrace_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape block  &
   block_name = .template_6_force.mlg_suo_actuator_L.BOX_502  &
   diag_corner_coords =   &
      (18.0mm),  &
      (10.0mm),  &
      (12.0mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1336  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.mlg_suo_spring_lg11))  &
   relative_to = .template_6_force.mlg_suo_liangan_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_1338  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.mlg_suo_spring_lg21))  &
   relative_to = .template_6_force.mlg_suo_liangan_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_liangan_R.MARKER_998  &
   location =   &
      (LOC_RELATIVE_TO({-4.3751313683E-07, -1.0769163339E-11, 0.0}, .template_6_force.ground.POINT_6361))  &
   relative_to = .template_6_force.mlg_suo_liangan_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape plate  &
   plate_name = .template_6_force.mlg_suo_liangan_R.PLATE_464  &
   width = (5.0mm)  &
   radius = (2.0mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1027  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_4831))  &
   relative_to = .template_6_force.mlg_suo_yaobi_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1030  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_4831))  &
   relative_to = .template_6_force.mlg_suo_yaobi_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_yaobi_R.MARKER_1048  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_4831))  &
   relative_to = .template_6_force.mlg_suo_yaobi_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape block  &
   block_name = .template_6_force.mlg_suo_yaobi_R.BOX_611  &
   diag_corner_coords =   &
      (-3.0mm),  &
      (-24.0mm),  &
      (6.0mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_suo_rod_R.CYLINDER_499  &
   radius = (1.8mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1105  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.POINT_4831))  &
   relative_to = .template_6_force.mlg_suo_base_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_base_R.MARKER_1113  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mlg_suo_suogou_R.PT200))  &
   relative_to = .template_6_force.mlg_suo_base_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape plate  &
   plate_name = .template_6_force.mlg_suo_base_R.PLATE_509  &
   radius = (2.0mm)
!
geometry modify shape block  &
   block_name = .template_6_force.mlg_suo_actuator_R.BOX_502  &
   diag_corner_coords =   &
      (18.0mm),  &
      (10.0mm),  &
      (12.0mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_1314  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_uc_top1))  &
   relative_to = .template_6_force.mlg_struct_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_554  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_lc_top1))  &
   relative_to = .template_6_force.mlg_struct_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_555  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_tire_axle1))  &
   relative_to = .template_6_force.mlg_struct_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_556  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_uc_top1))  &
   relative_to = .template_6_force.mlg_struct_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_R.MARKER_568  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_uc_top1))  &
   relative_to = .template_6_force.mlg_struct_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_308  &
   length = (750.0mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_309  &
   length = (390.0mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_R.CYLINDER_324  &
   length = (120.0mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_559  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_rod_bot))  &
   relative_to = .template_6_force.mlg_rod_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_564  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_actuator_bot))  &
   relative_to = .template_6_force.mlg_rod_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_565  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_rod_bot))  &
   relative_to = .template_6_force.mlg_rod_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_rod_R.MARKER_593  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_rod_bot))  &
   relative_to = .template_6_force.mlg_rod_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_560  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_actuator_bot))  &
   relative_to = .template_6_force.mlg_actuator_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_563  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_actuator_bot))  &
   relative_to = .template_6_force.mlg_actuator_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_592  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_actuator_bot))  &
   relative_to = .template_6_force.mlg_actuator_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_actuator_R.MARKER_1557  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpr_rod_topr))  &
   relative_to = .template_6_force.mlg_actuator_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_actuator_R.CYLINDER_320  &
   length = (DM(.template_6_force.ground.hpr_actuator_bot, .template_6_force.ground.hpr_actuator_top))
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_995  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mlg_suo_suogou_R.PT200))  &
   relative_to = .template_6_force.mlg_suo_suogou_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1334  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mlg_suo_suogou_R.PT200))  &
   relative_to = .template_6_force.mlg_suo_suogou_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1337  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.mlg_suo_spring_sg11))  &
   relative_to = .template_6_force.mlg_suo_suogou_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1339  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.mlg_suo_spring_sg21))  &
   relative_to = .template_6_force.mlg_suo_suogou_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_R.MARKER_1135  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mlg_suo_suogou_R.PT200))  &
   relative_to = .template_6_force.mlg_suo_suogou_R
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape block  &
   block_name = .template_6_force.mlg_suo_suogou_R.BOX_268  &
   diag_corner_coords =   &
      (42.0mm),  &
      (5.0mm),  &
      (12.0mm)
!
geometry modify shape block  &
   block_name = .template_6_force.mlg_suo_suogou_R.BOX_272  &
   diag_corner_coords =   &
      (35.0mm),  &
      (5.0mm),  &
      (12.0mm)
!
geometry modify shape plate  &
   plate_name = .template_6_force.mlg_suo_suogou_R.PLATE_515  &
   radius = (1mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_1314  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_uc_top))  &
   relative_to = .template_6_force.mlg_struct_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_554  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_lc_top))  &
   relative_to = .template_6_force.mlg_struct_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_555  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_tire_axle))  &
   relative_to = .template_6_force.mlg_struct_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_556  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_uc_top))  &
   relative_to = .template_6_force.mlg_struct_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_566  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_rod_bot))  &
   relative_to = .template_6_force.mlg_struct_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_struct_L.MARKER_568  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_uc_top))  &
   relative_to = .template_6_force.mlg_struct_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_308  &
   length = (750.0mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_309  &
   length = (390.0mm)
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_struct_L.CYLINDER_324  &
   length = (120.0mm)
!
marker modify  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_559  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_rod_bot))  &
   relative_to = .template_6_force.mlg_rod_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_564  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_actuator_bot))  &
   relative_to = .template_6_force.mlg_rod_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_565  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_rod_bot))  &
   relative_to = .template_6_force.mlg_rod_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_593  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_rod_bot))  &
   relative_to = .template_6_force.mlg_rod_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_rod_L.MARKER_682  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_rod_bot))  &
   relative_to = .template_6_force.mlg_rod_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_560  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_actuator_bot))  &
   relative_to = .template_6_force.mlg_actuatorL
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_578  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_actuator_top))  &
   relative_to = .template_6_force.mlg_actuatorL
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_563  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_actuator_bot))  &
   relative_to = .template_6_force.mlg_actuatorL
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_592  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_actuator_bot))  &
   relative_to = .template_6_force.mlg_actuatorL
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_actuatorL.MARKER_683  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hpl_actuator_bot))  &
   relative_to = .template_6_force.mlg_actuatorL
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape cylinder  &
   cylinder_name = .template_6_force.mlg_actuatorL.CYLINDER_320  &
   length = (DM(.template_6_force.ground.hpl_actuator_bot, .template_6_force.ground.hpl_actuator_top))
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_995  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mlg_suo_suogou_L.PT200))  &
   relative_to = .template_6_force.mlg_suo_suogou_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1334  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mlg_suo_suogou_L.PT200))  &
   relative_to = .template_6_force.mlg_suo_suogou_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1337  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.mlg_suo_spring_sg1))  &
   relative_to = .template_6_force.mlg_suo_suogou_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1339  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.mlg_suo_spring_sg2))  &
   relative_to = .template_6_force.mlg_suo_suogou_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.mlg_suo_suogou_L.MARKER_1135  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.mlg_suo_suogou_L.PT200))  &
   relative_to = .template_6_force.mlg_suo_suogou_L
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape block  &
   block_name = .template_6_force.mlg_suo_suogou_L.BOX_268  &
   diag_corner_coords =   &
      (42.0mm),  &
      (5.0mm),  &
      (12.0mm)
!
geometry modify shape block  &
   block_name = .template_6_force.mlg_suo_suogou_L.BOX_272  &
   diag_corner_coords =   &
      (35.0mm),  &
      (5.0mm),  &
      (12.0mm)
!
geometry modify shape plate  &
   plate_name = .template_6_force.mlg_suo_suogou_L.PLATE_515  &
   radius = (1mm)
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_995  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_suo_suogou.PT200))  &
   relative_to = .template_6_force.nlg_suo_suogou
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1135  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_suo_suogou.PT200))  &
   relative_to = .template_6_force.nlg_suo_suogou
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1069  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.nlg_suo_suogou.PT200))  &
   relative_to = .template_6_force.nlg_suo_suogou
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1383  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_spring_sg1))  &
   relative_to = .template_6_force.nlg_suo_suogou
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
marker modify  &
   marker_name = .template_6_force.nlg_suo_suogou.MARKER_1385  &
   location =   &
      (LOC_RELATIVE_TO({0, 0, 0}, .template_6_force.ground.hps_spring_sg2))  &
   relative_to = .template_6_force.nlg_suo_suogou
!
defaults coordinate_system  &
   default_coordinate_system = .template_6_force.ground
!
geometry modify shape block  &
   block_name = .template_6_force.nlg_suo_suogou.BOX_268  &
   diag_corner_coords =   &
      (42.0mm),  &
      (5.0mm),  &
      (12.0mm)
!
geometry modify shape block  &
   block_name = .template_6_force.nlg_suo_suogou.BOX_272  &
   diag_corner_coords =   &
      (35.0mm),  &
      (5.0mm),  &
      (12.0mm)
!
geometry modify shape plate  &
   plate_name = .template_6_force.nlg_suo_suogou.PLATE_515  &
   radius = (1mm)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_3_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.nlg_ZDT_FORCE.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_48_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.nlg_suo_unlock.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_47_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.nlg_suo_rod_springdamper.i)
!
geometry modify shape force  &
   force_name = .template_6_force.GFORCE_1_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.NLG_aeroforce.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_5_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.NLG_stopper_low.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_54_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.nlg_suo_springF_1.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_55_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.nlg_suo_springF_2.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_48_force_graphic_1_2  &
   applied_at_marker_name = (.template_6_force.mlg_suo_unlock_L.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_47_force_graphic_1_2  &
   applied_at_marker_name = (.template_6_force.mlg_suo_rod_springdamper_L.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_60_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.mlg_suo_springF_1_L.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_61_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.mlg_suo_springF_2_L.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_48_force_graphic_1_2_2  &
   applied_at_marker_name = (.template_6_force.mlg_suo_unlock_R.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_47_force_graphic_1_2_2  &
   applied_at_marker_name = (.template_6_force.mlg_suo_rod_springdamper_R.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_60_force_graphic_1_2  &
   applied_at_marker_name = (.template_6_force.mlg_suo_springF_1_R.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_61_force_graphic_1_2  &
   applied_at_marker_name = (.template_6_force.mlg_suo_springF_2_R.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_20_force_graphic_1_2  &
   applied_at_marker_name = (.template_6_force.mlg_zdtF_R.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_20_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.mlg_zdtF_L.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_29_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.mlg_stopper_low_L.i)
!
geometry modify shape force  &
   force_name = .template_6_force.SFORCE_77_force_graphic_1  &
   applied_at_marker_name = (.template_6_force.mlg_stopper_low_R.i)
!
model display  &
   model_name = template_6_force

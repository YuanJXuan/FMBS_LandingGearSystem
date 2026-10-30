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
   size_of_icons = 25.4  &
   spacing_for_grid = 25.4
!
!------------------------------ Adams View Model ------------------------------!
!
!
model create  &
   model_name = template_2_retract_semirocker  &
   title = "ADAMS/Aircraft template"
!
model attributes  &
   model_name = .template_2_retract_semirocker  &
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
   default_coordinate_system = .template_2_retract_semirocker.ground
!
! ****** Points for current part ******
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_db_sf_atch  &
   location = 7484.11, 0.0, 1623.06
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_db_sf_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_sf_atch_l  &
   location = 6314.44, -340.36, 1691.64
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_sf_atch_l  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_sf_atch_r  &
   location = 6314.44, 340.36, 1691.64
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_sf_atch_r  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_lc_bot  &
   location = 6197.6, 0.0, 508.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_lc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_top  &
   location = 6197.6, 0.0, 1625.6
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_db_uc_atch  &
   location = 6451.6, 0.0, 1016.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_db_uc_atch  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_geompt  &
   location = 6197.6, 0.0, 1473.2
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_geompt  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_bot  &
   location = 6197.6, 0.0, 762.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_uc_bot  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_lc_top  &
   location = 6197.6, 0.0, 1397.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_lc_top  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_origin_reference  &
   location = 0.0, 0.0, 0.0
!
point attributes  &
   point_name = .template_2_retract_semirocker.ground.hps_origin_reference  &
   size_of_icons = 50.8
!
point create  &
   point_name = .template_2_retract_semirocker.ground.hps_lb_uc_atch  &
   location = 6021.578, 0.0, 795.02
!
point create  &
   point_name = .template_2_retract_semirocker.ground.POINT_12  &
   location = 5947.600000001, 0.0, 657.9999999994
!
point create  &
   point_name = .template_2_retract_semirocker.ground.POINT  &
   location = 5947.600000001, -120.0, 657.9999999994
!
point create  &
   point_name = .template_2_retract_semirocker.ground.POINT_2  &
   location = 5947.600000001, 120.0, 657.9999999994
!
point create  &
   point_name = .template_2_retract_semirocker.ground.POINT_27  &
   location = 6197.6, 0.0, 478.0
!
! ****** Graphics for current part ******
!
part attributes  &
   part_name = .template_2_retract_semirocker.ground  &
   size_of_icons = 50.8
!
!----------------------------- Analysis settings ------------------------------!
!
!
model display  &
   model_name = template_2_retract_semirocker

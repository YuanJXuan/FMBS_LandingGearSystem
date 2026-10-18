import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class DropHpsLcTopAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass
     
    def Adjust(self):
         ascene = Jusme.ActiveUSScene
         print("start adjusting HpsLcTop")

         #--------------------------------------------._AA_nlg_post_2hubs.ground.hps_lc_top
         hps_lc_top = ascene.getObject(self.hps_full_name)
         if not hps_lc_top :
            return
         
         #---------------获取全局坐标系原点的mark点
         origo = ascene.getObject("._AA_nlg_post_2hubs.ground.origo")
         if not origo :
            return

         #------------------------------._AA_nlg_post_2hubs.ground.hps_lc_bot
         hps_lc_bot = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_lc_bot")
         if not hps_lc_bot :
             return
         hps_lc_top_loc = hps_lc_top.location
         hps_lc_bot_loc = hps_lc_bot.location
         axis = VecUtils.ORI_ALONG_AXIS(hps_lc_top_loc, hps_lc_bot_loc, 'z')
         center_loc = 0.5 * (hps_lc_top_loc + hps_lc_bot_loc)

         #---------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder
         ges_lower_cylinder = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder")
         if not ges_lower_cylinder :
             return
         #ges_lower_cylinder.location = center_loc
         #ges_lower_cylinder.orientation = axis

         #-------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_5
         gralin_5 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_5")
         if not gralin_5 :
             return
         gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lc_top))
         gralin_5.orientation = axis
         loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, gralin_5.location, gralin_5.orientation)
         gralin_5.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
         gralin_5.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         len = VecUtils.DM(hps_lc_top_loc, hps_lc_bot_loc)
         #---------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_geom1
         gralin_geom1 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_geom1")
         if not gralin_geom1 :
            return
         gralin_geom1.length = len

         #---------------------------._AA_nlg_post_2hubs.ground.hpl_wheel_center
         hpr_wheel_center = ascene.getObject("._AA_nlg_post_2hubs.ground.hpr_wheel_center")
         if not hpr_wheel_center :
            return
         hpr_wheel_center_loc = hpr_wheel_center.location

        #---------------------------._AA_nlg_post_2hubs.ground.hpl_wheel_center
         hpl_wheel_center = ascene.getObject("._AA_nlg_post_2hubs.ground.hpl_wheel_center")
         if not hpl_wheel_center :
            return
         hpl_wheel_center_loc = hpl_wheel_center.location
         
         #---------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_7
         gralin_7 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_7")
         if not gralin_7 :
             return
         gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_wheel_center))
         gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(hpr_wheel_center_loc, hpl_wheel_center_loc, 'z'))
         loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, gralin_7.location, gralin_7.orientation)
         gralin_7.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
         gralin_7.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        # #---------------------------._AA_nlg_post_2hubs.ground.hpr_wheel_center
        #  hpr_wheel_center = ascene.getObject("._AA_nlg_post_2hubs.ground.hpr_wheel_center")
        #  if not hpr_wheel_center :
        #      return
        #  #---------------------------._AA_nlg_post_2hubs.ground.hpl_wheel_center
        #  hpl_wheel_center = ascene.getObject("._AA_nlg_post_2hubs.ground.hpl_wheel_center")
        #  if not hpl_wheel_center :
        #      return
        #  hpr_wheel_center_loc = hpr_wheel_center.location
        #  hpl_wheel_center_loc = hpl_wheel_center.location
        #  center2 = 0.5 * (hpr_wheel_center_loc + hpl_wheel_center_loc)

        #  len1 = VecUtils.DM(hps_lc_top_loc, hps_lc_bot_loc)
        #  #---------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_geom1
        #  gralin_geom1 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_geom1")
        #  if not gralin_geom1 :
        #      return
        #  gralin_geom1.length = len1
        #  radius1 = gralin_geom1.radius

        #  #--------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_geom2
        #  gralin_geom2 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.gralin_geom2")
        #  if not gralin_geom2 :
        #      return
        #  len2 = gralin_geom2.length
        #  radius2 = gralin_geom2.radius
        #  print("{},{},{},{}".format(len1, radius1, len2, radius2))
        #  w1 = radius1 * radius1 * len1
        #  w2 = radius2 * radius2 * len2
        #  w = w1 + w2
        #  coff1 = w1 / w
        #  coff2 = w2 / w
        #  center = coff1 * center1 + coff2 * center2
        #  print(center)
         
         

         #-------------------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.ues_stopper_i_1
         ues_stopper_i_1 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.ues_stopper_i_1")
         if not ues_stopper_i_1 :
             return
         ues_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lc_top))
         ues_stopper_i_1.orientation = axis
         loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, ues_stopper_i_1.location, ues_stopper_i_1.orientation)
         ues_stopper_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
         ues_stopper_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #-------------------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.ues_damper_i_1
         ues_damper_i_1 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.ues_damper_i_1")
         if not ues_damper_i_1 :
             return
         ues_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lc_top))
         ues_damper_i_1.orientation = axis
         loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, ues_damper_i_1.location, ues_damper_i_1.orientation)
         ues_damper_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
         ues_damper_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #-------------------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.ues_spring_i_1
         ues_spring_i_1 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.ues_spring_i_1")
         if not ues_spring_i_1 :
             return
         ues_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lc_top))
         ues_spring_i_1.orientation = axis
         loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, ues_spring_i_1.location, ues_spring_i_1.orientation)
         ues_spring_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
         ues_spring_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         

         #-----------------------------._AA_nlg_post_2hubs.ground.cfs_wheel_centers_midpoint
         cfs_wheel_centers_midpoint = ascene.getObject("._AA_nlg_post_2hubs.ground.cfs_wheel_centers_midpoint")
         if not cfs_wheel_centers_midpoint :
             return
         
         #-----------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.coomarker_2
         coomarker_2 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.coomarker_2")
         if not coomarker_2 :
             return
         coomarker_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfs_wheel_centers_midpoint))
         coomarker_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], cfs_wheel_centers_midpoint))
         loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, coomarker_2.location, coomarker_2.orientation)
         coomarker_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
         coomarker_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #--------------------._AA_nlg_post_2hubs.ground.hps_nlg_axle_lowpoint
         hps_nlg_axle_lowpoint = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_nlg_axle_lowpoint")
         if not hps_nlg_axle_lowpoint :
             return
         
         #---------------------._AA_nlg_post_2hubs.ground.cfs_nlg_axle_lowpoint
         cfs_nlg_axle_lowpoint = ascene.getObject("._AA_nlg_post_2hubs.ground.cfs_nlg_axle_lowpoint")
         if not cfs_nlg_axle_lowpoint :
             return
         cfs_nlg_axle_lowpoint.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_nlg_axle_lowpoint))
         cfs_nlg_axle_lowpoint.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))

         #----------------------._AA_nlg_post_2hubs.ges_lower_cylinder.coomarker_3
         coomarker_3 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.coomarker_3")
         if not coomarker_3 :
             return
         coomarker_3.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfs_nlg_axle_lowpoint))
         coomarker_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], cfs_nlg_axle_lowpoint))
         loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, coomarker_3.location, coomarker_3.orientation)
         coomarker_3.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
         coomarker_3.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #------------------------._AA_nlg_post_2hubs.ges_upper_cylinder.jxs_joint_j_11
         jxs_joint_j_11 = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_cylinder.jxs_joint_j_11")
         if not jxs_joint_j_11 :
             return
         #----------------------._AA_nlg_post_2hubs.ges_lower_cylinder.jxs_joint_i_11
         jxs_joint_i_11 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.jxs_joint_i_11")
         jxs_joint_i_11.location =  (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_11))
         jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_11))
         loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
         jxs_joint_i_11.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
         jxs_joint_i_11.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #------------------------._AA_nlg_post_2hubs.ground.hps_lta_lc_atch
         hps_lta_lc_atch = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_lta_lc_atch")
         if not hps_lta_lc_atch :
             return
         
         #---------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.jxs_joint_j_9
         jxs_joint_j_9 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.jxs_joint_j_9")
         if not jxs_joint_j_9 :
             return
         jxs_joint_j_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_lc_atch))
         jxs_joint_j_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
         loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, jxs_joint_j_9.location, jxs_joint_j_9.orientation)
         jxs_joint_j_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
         jxs_joint_j_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


         #-----------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_115
         marker_115 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_115")
         if marker_115 :
            marker_115.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lc_top))
            marker_115.orientation = (0.0, 0.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_115.location, marker_115.orientation)
            marker_115.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_115.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #-------------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_114
         marker_114 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_114")
         if marker_114 :
            marker_114.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lc_top))
            marker_114.orientation = (0.0, 0.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_114.location, marker_114.orientation)
            marker_114.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_114.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #---------------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_107
         #-------------------------._AA_nlg_post_2hubs.ground.hps_uc_top
         hps_uc_top = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_uc_top")
         if not hps_uc_top :
             return
         marker_107 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_107")
         if marker_107 :
            marker_107.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_top))
            marker_107.orientation = (0.0, 0.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_107.location, marker_107.orientation)
            marker_107.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_107.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #---------------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_106
         marker_106 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_106")
         if marker_106 :
            marker_106.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lc_top))
            marker_106.orientation = (0.0, 0.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_106.location, marker_106.orientation)
            marker_106.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_106.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #--------------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_104
         marker_104 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_104")
         if marker_104 :
            marker_104.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lc_top))
            marker_104.orientation = (0.0, 0.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_104.location, marker_104.orientation)
            marker_104.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_104.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_8
         marker_8 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_8")
         if marker_8 :
            marker_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_wheel_center))
            marker_8.orientation = (0.0, 90.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_8.location, marker_8.orientation)
            marker_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_6
         marker_6 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_6")
         if marker_6 :
            marker_6.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_wheel_center))
            marker_6.orientation = (0.0, 90.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_6.location, marker_6.orientation)
            marker_6.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_6.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        
         #------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_4
         marker_4 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_4")
         if marker_4 :
            marker_4.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_wheel_center))
            marker_4.orientation = (0.0, 0.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_4.location, marker_4.orientation)
            marker_4.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_4.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #------------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_3
         marker_3 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_3")
         if marker_3 :
            marker_3.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_wheel_center))
            marker_3.orientation = (0.0, 0.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_3.location, marker_3.orientation)
            marker_3.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_3.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #-----------------------------._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_1
         marker_1 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.MARKER_1")
         if marker_1 :
            marker_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lc_top))
            marker_1.orientation = (0.0, 0.0, 0.0)
            loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, marker_1.location, marker_1.orientation)
            marker_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
            marker_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

         #------------------------------._AA_nlg_post_2hubs.joscyl_lc_uc_joint
         joscyl_lc_uc_joint = ascene.getObject("._AA_nlg_post_2hubs.joscyl_lc_uc_joint")
         if not joscyl_lc_uc_joint :
             return
         joscyl_lc_uc_joint.recompute()

         #---------------------------------._AA_nlg_post_2hubs.jossph_lta_lc_joint
         jossph_lta_lc_joint = ascene.getObject("._AA_nlg_post_2hubs.jossph_lta_lc_joint")
         if not jossph_lta_lc_joint :
             return
         jossph_lta_lc_joint.recompute()


         pass
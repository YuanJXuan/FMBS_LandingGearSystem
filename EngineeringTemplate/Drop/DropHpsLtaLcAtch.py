import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class DropHpsLtaLcAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        ascene = Jusme.ActiveUSScene
        #----------------获取已调整位置的硬点节点
        hps_lta_lc_atch = ascene.getObject(self.hps_full_name)
        if not hps_lta_lc_atch :
            print("Can not obtain hps_lta_lc_atch")
            return
        
        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject("._AA_nlg_post_2hubs.ground.origo")
        if not origo :
            print("Can not obtain origo")
            return
        
        #----------------------------得到hps_lta_uta_atch硬点节点
        hps_lta_uta_atch = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_lta_uta_atch")
        if not hps_lta_uta_atch:
            print("Can not obtain hps_lta_uta_atch")
            return
        
        #-----------------------得到下扭力臂前后硬点的坐标位置
        hps_lta_lc_atch_loc = hps_lta_lc_atch.location
        hps_lta_uta_atch_loc = hps_lta_uta_atch.location

        #-----------------------计算ges_lower_torque_arm的欧拉角
        axis = VecUtils.ORI_ALONG_AXIS(hps_lta_lc_atch_loc, hps_lta_uta_atch_loc, 'z')
        #-----------------------ges_lower_torque_arm中心点位置
        center_loc = 0.5 * (hps_lta_lc_atch_loc + hps_lta_uta_atch_loc)

        #--------------------------得到ges_lower_torque_arm节点
        ges_lower_torque_arm = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm")
        if not ges_lower_torque_arm :
            return
        ges_lower_torque_arm.location = center_loc
        ges_lower_torque_arm.orientation = axis

        #----------------------得到下扭力臂的中心点
        gralin_10 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.gralin_10")
        if not gralin_10 :
            return
        
        #------------------------设置中心点gralin_10位置和欧拉角
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_lc_atch))
        gralin_10.orientation = axis
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------------计算ges_lower_torque_arm的长度 
        len = VecUtils.DM(hps_lta_lc_atch_loc, hps_lta_uta_atch_loc)
        gralin_lower_torque_arm_geom = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.gralin_lower_torque_arm_geom")
        if not gralin_lower_torque_arm_geom :
            return
        gralin_lower_torque_arm_geom.length = len

        #--------------------设置ges_lower_torque_arm质心位置
        cm = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.cm")
        if not cm :
            return
        cm.location = ges_lower_torque_arm.location
        cm.orientation = axis
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------设置ges_lower_torque_arm转动惯量Mark点位置
        inertia_frame = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.inertia_frame") 
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ges_lower_torque_arm))
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------------._AA_nlg_post_2hubs.ges_lower_cylinder
        ges_lower_cylinder = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder") 
        if not ges_lower_cylinder :
            return
        #------------._AA_nlg_post_2hubs.ges_lower_cylinder.jxs_joint_j_9
        jxs_joint_j_9 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.jxs_joint_j_9") 
        if not jxs_joint_j_9 :
            return
        jxs_joint_j_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_lc_atch))
        jxs_joint_j_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, jxs_joint_j_9.location, jxs_joint_j_9.orientation)
        jxs_joint_j_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------------------------------._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_9
        jxs_joint_i_9 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_9") 
        if not jxs_joint_i_9 :
            return
        jxs_joint_i_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_9))
        jxs_joint_i_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_9))
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, jxs_joint_i_9.location, jxs_joint_i_9.orientation)
        jxs_joint_i_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------._AA_nlg_post_2hubs.jossph_lta_lc_joint
        jossph_lta_lc_joint = ascene.getObject("._AA_nlg_post_2hubs.jossph_lta_lc_joint") 
        if not jossph_lta_lc_joint :
            return
        jossph_lta_lc_joint.recompute()

        #---------------------._AA_nlg_post_2hubs.ges_upper_torque_arm.jxs_joint_j_8
        jxs_joint_j_8 = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.jxs_joint_j_8") 
        if not jxs_joint_j_8 :
            return
        #------------------------._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_8
        jxs_joint_i_8 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_8") 
        if not jxs_joint_i_8:
            return
        jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_8))
        jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_8))
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
        jxs_joint_i_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------._AA_nlg_post_2hubs.josrev_lta_uta_joint
        josrev_lta_uta_joint = ascene.getObject("._AA_nlg_post_2hubs.josrev_lta_uta_joint") 
        if not josrev_lta_uta_joint :
            return
        josrev_lta_uta_joint.recompute()

        pass


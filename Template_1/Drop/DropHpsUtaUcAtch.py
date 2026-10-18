import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class DropHpsUtaUcAtchAdjust(AbstractHps.AbstractHpsAdjust)  :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        ascene = Jusme.ActiveUSScene
        #----------------获取已调整位置的硬点节点
        hps_uta_uc_atch = ascene.getObject(self.hps_full_name)
        if not hps_uta_uc_atch :
            print("Can not obtain hps_lta_lc_atch")
            return
        
        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject("._AA_nlg_post_2hubs.ground.origo")
        if not origo :
            print("Can not obtain origo")
            return
        
        #-------------------------._AA_nlg_post_2hubs.ground.hps_lta_uta_atch
        hps_lta_uta_atch = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_lta_uta_atch")
        if not hps_lta_uta_atch :
            return
        
        hps_uta_uc_atch_loc = hps_uta_uc_atch.location
        hps_lta_uta_atch_loc = hps_lta_uta_atch.location

        #-------------------------._AA_nlg_post_2hubs.ges_upper_torque_arm
        ges_upper_torque_arm = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm")
        if not ges_upper_torque_arm :
            return
        
        #-----------------------计算ges_upper_torque_arm的欧拉角
        axis = VecUtils.ORI_ALONG_AXIS(hps_uta_uc_atch_loc, hps_lta_uta_atch_loc, 'z')
        #-----------------------ges_upper_torque_arm中心点位置
        center_loc = 0.5 * (hps_uta_uc_atch_loc + hps_lta_uta_atch_loc)
        ges_upper_torque_arm.location = center_loc
        ges_upper_torque_arm.orientation = axis

        #---------------------------._AA_nlg_post_2hubs.ges_upper_torque_arm.gralin_9
        gralin_9 =  ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.gralin_9")
        if not gralin_9 :
            return
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uta_uc_atch))
        gralin_9.orientation = axis
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------------计算ges_upper_torque_arm的长度 
        len = VecUtils.DM(hps_uta_uc_atch_loc, hps_lta_uta_atch_loc)
        #----------------------------._AA_nlg_post_2hubs.ges_upper_torque_arm.gralin_upper_torque_arm_geom
        gralin_upper_torque_arm_geom = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.gralin_upper_torque_arm_geom")
        if not gralin_upper_torque_arm_geom :
            return
        gralin_upper_torque_arm_geom.length = len

        #--------------------设置ges_lower_torque_arm质心位置
        cm = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.cm")
        if not cm :
            return
        cm.location = ges_upper_torque_arm.location
        cm.orientation = axis
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------设置ges_lower_torque_arm转动惯量Mark点位置
        inertia_frame = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.inertia_frame")
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ges_upper_torque_arm))
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------._AA_nlg_post_2hubs.ges_collar.jxs_joint_j_10
        jxs_joint_j_10 = ascene.getObject("._AA_nlg_post_2hubs.ges_collar.jxs_joint_j_10")
        if not jxs_joint_j_10 :
            return
        jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uta_uc_atch))
        jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        #------------------------------------._AA_nlg_post_2hubs.ges_collar
        ges_collar = ascene.getObject("._AA_nlg_post_2hubs.ges_collar")
        if not ges_collar :
            return
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
        jxs_joint_j_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------------._AA_nlg_post_2hubs.ges_upper_torque_arm.jxs_joint_i_10
        jxs_joint_i_10 = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.jxs_joint_i_10")
        if not jxs_joint_i_10 :
            return
        jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_10))
        jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_10))
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
        jxs_joint_i_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------._AA_nlg_post_2hubs.josrev_uta_uc_joint
        josrev_uta_uc_joint = ascene.getObject("._AA_nlg_post_2hubs.josrev_uta_uc_joint")
        if not josrev_uta_uc_joint :
            return
        josrev_uta_uc_joint.recompute()

        #------------------------------._AA_nlg_post_2hubs.ges_upper_torque_arm.jxs_joint_j_8
        jxs_joint_j_8 = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.jxs_joint_j_8")
        if not jxs_joint_j_8 :
            return
        jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_uta_atch))
        jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
        jxs_joint_j_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #_______________________._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_8
        jxs_joint_i_8 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_8")
        if not jxs_joint_i_8 :
            return
        jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_8))
        jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_8))
        #---------------------------------._AA_nlg_post_2hubs.ges_lower_torque_arm
        ges_lower_torque_arm = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm")
        if not ges_lower_torque_arm :
            return
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
        jxs_joint_i_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------------------------------------._AA_nlg_post_2hubs.josrev_lta_uta_joint
        josrev_lta_uta_joint = ascene.getObject("._AA_nlg_post_2hubs.josrev_lta_uta_joint")
        if not josrev_lta_uta_joint :
            return
        josrev_lta_uta_joint.recompute()
        
        pass
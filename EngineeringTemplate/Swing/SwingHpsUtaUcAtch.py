import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class SwingHpsUtaUcAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始转弯仿真hps_uta_uc_atch硬点调整")

        ascene = Jusme.ActiveUSScene

        #--------------得到模型名称
        model_name = Common.getModelName()

        origo = ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            return

        #-----.gcmb_2_turn.ground.hps_uta_uc_atch
        hps_uta_uc_atch = ascene.getObject(self.hps_full_name)
        if not hps_uta_uc_atch :
            return
        hps_uta_uc_atch_loc = hps_uta_uc_atch.location

        #-----.gcmb_2_turn.ground.hps_lta_lc_atch
        hps_lta_lc_atch = ascene.getObject(".{}.ground.hps_lta_lc_atch".format(model_name))
        if not hps_lta_lc_atch :
            return
        hps_lta_lc_atch_loc = hps_lta_lc_atch.location

        #------.gcmb_2_turn.ground.hps_lta_uta_atch
        hps_lta_uta_atch = ascene.getObject(".{}.ground.hps_lta_uta_atch".format(model_name))
        if not hps_lta_uta_atch :
            return
        hps_lta_uta_atch_loc = hps_lta_uta_atch.location

        #-----------------------------------------------开始上扭力臂结构参数化调整
        center_loc = 0.5 * (hps_uta_uc_atch_loc + hps_lta_uta_atch_loc)
        axis = VecUtils.ORI_ALONG_AXIS(hps_uta_uc_atch_loc, hps_lta_uta_atch_loc, "Z")
        geo_len = VecUtils.DM(hps_uta_uc_atch_loc, hps_lta_uta_atch_loc)

        #------.gcmb_2_turn.ges_upper_torque_arm
        ges_upper_torque_arm = ascene.getObject(".{}.ges_upper_torque_arm".format(model_name))
        if not ges_upper_torque_arm :
            return
        ges_upper_torque_arm.location = center_loc
        ges_upper_torque_arm.orientation = axis

        #------.gcmb_2_turn.ges_upper_torque_arm.gralin_9
        gralin_9 = ascene.getObject(".{}.ges_upper_torque_arm.gralin_9".format(model_name))
        if not gralin_9 :
            return
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uta_uc_atch))
        gralin_9.orientation = VecUtils.ORI_ALONG_AXIS(hps_uta_uc_atch_loc, hps_lta_uta_atch_loc, 'z')
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------.gcmb_2_turn.ges_upper_torque_arm.gralin_upper_torque_arm_geom
        gralin_upper_torque_arm_geom = ascene.getObject(".{}.ges_upper_torque_arm.gralin_upper_torque_arm_geom".format(model_name))
        if not gralin_upper_torque_arm_geom :
            return
        gralin_upper_torque_arm_geom.length = geo_len

        #------.gcmb_2_turn.ges_upper_torque_arm.cm
        cm = ascene.getObject(".{}.ges_upper_torque_arm.cm".format(model_name))
        if not cm :
            return
        cm.recompute()

        #------.gcmb_2_turn.ges_upper_torque_arm.inertia_frame
        inertia_frame = ascene.getObject(".{}.ges_upper_torque_arm.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ges_upper_torque_arm))
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------.gcmb_2_turn.ges_upper_torque_arm.jxs_joint_j_8
        jxs_joint_j_8 = ascene.getObject(".{}.ges_upper_torque_arm.jxs_joint_j_8".format(model_name))
        if not jxs_joint_j_8 :
            return
        jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_uta_atch))
        jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
        jxs_joint_j_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------.gcmb_2_turn.ges_lower_torque_arm
        ges_lower_torque_arm = ascene.getObject(".{}.ges_lower_torque_arm".format(model_name))
        if not ges_lower_torque_arm :
            return

        #-------.gcmb_2_turn.ges_lower_torque_arm.jxs_joint_i_8
        jxs_joint_i_8 = ascene.getObject(".{}.ges_lower_torque_arm.jxs_joint_i_8".format(model_name))
        if not jxs_joint_i_8 :
            return
        jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_8))
        jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_8))
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
        jxs_joint_i_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------.gcmb_2_turn.ges_collar
        ges_collar = ascene.getObject(".{}.ges_collar".format(model_name))
        if not ges_collar :
            return
        
        #-------.gcmb_2_turn.ges_collar.jxs_joint_j_10
        jxs_joint_j_10 = ascene.getObject(".{}.ges_collar.jxs_joint_j_10".format(model_name))
        if not jxs_joint_j_10 :
            return
        jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uta_uc_atch))
        jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
        jxs_joint_j_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------.gcmb_2_turn.ges_upper_torque_arm.jxs_joint_i_10
        jxs_joint_i_10 = ascene.getObject(".{}.ges_upper_torque_arm.jxs_joint_i_10".format(model_name))
        if not jxs_joint_i_10 :
            return
        jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_10))
        jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_10))
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
        jxs_joint_i_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------------------进行下扭力臂参数化调整
        #-------.gcmb_2_turn.ges_lower_torque_arm
        ges_lower_torque_arm = ascene.getObject(".{}.ges_lower_torque_arm".format(model_name))
        if not ges_lower_torque_arm :
            return
        
        center_loc = 0.5 * (hps_lta_lc_atch_loc + hps_lta_uta_atch_loc)
        axis = VecUtils.ORI_ALONG_AXIS(hps_lta_lc_atch_loc, hps_lta_uta_atch_loc, "Z")
        geo_len = VecUtils.DM(hps_lta_lc_atch_loc, hps_lta_uta_atch_loc)

        ges_lower_torque_arm.location = center_loc
        ges_lower_torque_arm.orientation = axis

        #-------.gcmb_2_turn.ges_lower_torque_arm.gralin_10
        gralin_10 = ascene.getObject(".{}.ges_lower_torque_arm.gralin_10".format(model_name))
        if not gralin_10 :
            return
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_lc_atch))
        gralin_10.orientation = VecUtils.ORI_ALONG_AXIS(hps_lta_lc_atch_loc, hps_lta_uta_atch_loc, "Z")
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.gcmb_2_turn.ges_lower_torque_arm.gralin_lower_torque_arm_geom
        gralin_lower_torque_arm_geom = ascene.getObject(".{}.ges_lower_torque_arm.gralin_lower_torque_arm_geom".format(model_name))
        if not gralin_lower_torque_arm_geom :
            return
        gralin_lower_torque_arm_geom.length = geo_len

        #---------.gcmb_2_turn.ges_lower_torque_arm.cm
        cm = ascene.getObject(".{}.ges_lower_torque_arm.cm".format(model_name))
        if not cm :
            return
        cm.recompute()

        #-------.gcmb_2_turn.ges_lower_torque_arm.inertia_frame
        inertia_frame = ascene.getObject(".{}.ges_lower_torque_arm.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ges_lower_torque_arm))
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------.gcmb_2_turn.ges_upper_torque_arm
        ges_upper_torque_arm = ascene.getObject(".{}.ges_upper_torque_arm".format(model_name))
        if not ges_upper_torque_arm :
            return

        #--------.gcmb_2_turn.ges_upper_torque_arm.jxs_joint_j_8
        jxs_joint_j_8 = ascene.getObject(".{}.ges_upper_torque_arm.jxs_joint_j_8".format(model_name))
        if not jxs_joint_j_8 :
            return
        jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_uta_atch))
        jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_upper_torque_arm.location, ges_upper_torque_arm.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
        jxs_joint_j_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------.gcmb_2_turn.ges_lower_torque_arm.jxs_joint_i_8
        jxs_joint_i_8 = ascene.getObject(".{}.ges_lower_torque_arm.jxs_joint_i_8".format(model_name))
        if not jxs_joint_i_8 :
            return
        jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_8))
        jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_8))
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
        jxs_joint_i_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------.gcmb_2_turn.ges_lower_cylinder
        ges_lower_cylinder = ascene.getObject(".{}.ges_lower_cylinder".format(model_name))
        if not ges_lower_cylinder :
            return
        
        #-------.gcmb_2_turn.ges_lower_cylinder.jxs_joint_j_9
        jxs_joint_j_9 = ascene.getObject(".{}.ges_lower_cylinder.jxs_joint_j_9".format(model_name))
        if not jxs_joint_j_9 :
            return
        jxs_joint_j_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_lc_atch))
        jxs_joint_j_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, jxs_joint_j_9.location, jxs_joint_j_9.orientation)
        jxs_joint_j_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------.gcmb_2_turn.ges_lower_torque_arm.jxs_joint_i_9
        jxs_joint_i_9 = ascene.getObject(".{}.ges_lower_torque_arm.jxs_joint_i_9".format(model_name))
        if not jxs_joint_i_9 :
            return
        jxs_joint_i_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_9))
        jxs_joint_i_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_9))
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, jxs_joint_i_9.location, jxs_joint_i_9.orientation)
        jxs_joint_i_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------更新运动副，测量以及驱动等xinxi
        #------.gcmb_2_turn.josrev_lta_uta_joint
        josrev_lta_uta_joint = ascene.getObject(".{}.josrev_lta_uta_joint".format(model_name))
        if not josrev_lta_uta_joint :
            return
        josrev_lta_uta_joint.recompute()

        #------.gcmb_2_turn.jossph_lta_lc_joint
        jossph_lta_lc_joint = ascene.getObject(".{}.jossph_lta_lc_joint".format(model_name))
        if not jossph_lta_lc_joint :
            return
        jossph_lta_lc_joint.recompute()

        #-----.gcmb_2_turn.josrev_uta_uc_joint
        josrev_uta_uc_joint = ascene.getObject(".{}.josrev_uta_uc_joint".format(model_name))
        if not josrev_uta_uc_joint :
            return
        josrev_uta_uc_joint.recompute()


        pass
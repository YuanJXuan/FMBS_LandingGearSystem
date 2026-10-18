import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class CosimHpsRodBotAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始收放仿真hps_rod_bot硬点调整")

        ascene = Jusme.ActiveUSScene
        #--------------得到模型名称
        model_name = Common.getModelName()

        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            return

        #--------._AA_nlg_post_2hubs.ground.hps_rod_bot
        hps_rod_bot = ascene.getObject(self.hps_full_name)
        if not hps_rod_bot :
            return
        hps_rod_bot_loc = hps_rod_bot.location

        #----------._AA_nlg_post_2hubs.ground.hps_rod_top
        hps_rod_top = ascene.getObject(".{}.ground.hps_rod_top".format(model_name))
        if not hps_rod_top :
            return
        hps_rod_top_loc = hps_rod_top.location

        #-------._AA_nlg_post_2hubs.ground.hps_db_sf_atch
        hps_db_sf_atch = ascene.getObject(".{}.ground.hps_db_sf_atch".format(model_name))
        if not hps_db_sf_atch :
            return
        hps_db_sf_atch_loc = hps_db_sf_atch.location

        #-----------._AA_nlg_post_2hubs.ground.hps_uc_sf_atch_r
        hps_uc_sf_atch_r = ascene.getObject(".{}.ground.hps_uc_sf_atch_r".format(model_name))
        if not hps_uc_sf_atch_r :
            return
        hps_uc_sf_atch_r_loc = hps_uc_sf_atch_r.location

        #---------._AA_nlg_post_2hubs.ground.hps_uc_sf_atch_l
        hps_uc_sf_atch_l = ascene.getObject(".{}.ground.hps_uc_sf_atch_l".format(model_name))
        if not hps_uc_sf_atch_l :
            return
        hps_uc_sf_atch_l_loc = hps_uc_sf_atch_l.location

        #--------._AA_nlg_post_2hubs.ground.hps_db_uc_atch
        hps_db_uc_atch = ascene.getObject(".{}.ground.hps_db_uc_atch".format(model_name))
        if not hps_db_uc_atch :
            return
        hps_db_uc_atch_loc = hps_db_uc_atch.location

        #--------计算ges_sf_actuator的轴线方向
        axis = VecUtils.ORI_ALONG_AXIS(hps_db_sf_atch_loc, hps_rod_bot_loc, "Z")
        geo_len = VecUtils.DM(hps_db_sf_atch_loc, hps_rod_bot_loc)
        hps_db_uc_atch.location = VecUtils.LOC_ALONG_LINE(hps_db_sf_atch_loc, hps_rod_bot_loc, geo_len - 20)
        hps_db_uc_atch_loc = hps_db_uc_atch.location
        geo_len = VecUtils.DM(hps_db_sf_atch_loc, hps_db_uc_atch_loc)
        center_loc = 0.5 * (hps_db_sf_atch_loc + hps_db_uc_atch_loc)

        #------._AA_nlg_post_2hubs.ges_sf_actuator
        ges_sf_actuator = ascene.getObject(".{}.ges_sf_actuator".format(model_name))
        if not ges_sf_actuator :
            return
        ges_sf_actuator.location = center_loc
        ges_sf_actuator.orientation = axis

        #-------._AA_nlg_post_2hubs.ges_sf_actuator.gralin_1
        gralin_1 = ascene.getObject(".{}.ges_sf_actuator.gralin_1".format(model_name))
        if not gralin_1 :
            return
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        gralin_1.orientation = axis
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------._AA_nlg_post_2hubs.ges_sf_actuator.gralin_dragbrace_geom
        gralin_dragbrace_geom = ascene.getObject(".{}.ges_sf_actuator.gralin_dragbrace_geom".format(model_name))
        if not gralin_dragbrace_geom :
            return
        gralin_dragbrace_geom.length = geo_len

        #-----------------._AA_nlg_post_2hubs.ges_sf_actuator.cm
        cm = ascene.getObject(".{}.ges_sf_actuator.cm".format(model_name))
        if not cm :
            return
        cm.recompute()

        #--------------------._AA_nlg_post_2hubs.ges_sf_actuator.inertia_frame
        inertia_frame = ascene.getObject(".{}.ges_sf_actuator.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = axis
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------------._AA_nlg_post_2hubs.ges_subframe
        ges_subframe = ascene.getObject(".{}.ges_subframe".format(model_name))
        if not ges_subframe :
            return

        #--------._AA_nlg_post_2hubs.ges_subframe.jxs_joint_j_14
        jxs_joint_j_14 = ascene.getObject(".{}.ges_subframe.jxs_joint_j_14".format(model_name))
        if not jxs_joint_j_14 :
            return
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_nlg_post_2hubs.ges_sf_actuator.jxs_joint_i_14
        jxs_joint_i_14 = ascene.getObject(".{}.ges_sf_actuator.jxs_joint_i_14".format(model_name))
        if not jxs_joint_i_14 :
            return
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_14))
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_14))
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------._AA_nlg_post_2hubs.ges_sf_actuator.MARKER_97
        MARKER_97 = ascene.getObject(".{}.ges_sf_actuator.MARKER_97".format(model_name))
        if not MARKER_97 :
            return
        MARKER_97.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        MARKER_97.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_97.location, MARKER_97.orientation)
        MARKER_97.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_97.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_nlg_post_2hubs.ges_sf_rod
        ges_sf_rod = ascene.getObject(".{}.ges_sf_rod".format(model_name))
        if not ges_sf_rod :
            return

        #--------._AA_nlg_post_2hubs.ges_sf_rod.MARKER_84
        MARKER_84 = ascene.getObject(".{}.ges_sf_rod.MARKER_84".format(model_name))
        if not MARKER_84 :
            return
        MARKER_84.location = 0.5 * (hps_rod_bot_loc + hps_rod_bot_loc)
        MARKER_84.orientation = VecUtils.ORI_ALONG_AXIS(hps_db_uc_atch_loc, hps_db_sf_atch_loc, "Z")
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_84.location, MARKER_84.orientation)
        MARKER_84.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_84.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_nlg_post_2hubs.ges_sf_actuator.MARKER_85
        # ------MARKER_85目前未发现与任何硬点有关联
        #-------在参数化结构调整中认定其为ges_sf_rod质心位置
        MARKER_85 = ascene.getObject(".{}.ges_sf_actuator.MARKER_85".format(model_name))
        if not MARKER_85 :
            return
        MARKER_85.location = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        MARKER_85.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_85.location, MARKER_85.orientation)
        MARKER_85.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_85.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------------------------------对内筒进行结构参数化调整
        geo_len = VecUtils.DM(hps_rod_bot_loc, hps_rod_top_loc)
        hps_rod_top.location = VecUtils.LOC_ALONG_LINE(hps_rod_bot_loc, hps_db_sf_atch_loc, geo_len)
        hps_rod_top_loc = hps_rod_top.location
        axis = VecUtils.ORI_ALONG_AXIS(hps_rod_bot_loc, hps_rod_top_loc, "Z")
        center_loc = 0.5 * (hps_rod_bot_loc + hps_rod_top_loc)

        #-----------._AA_nlg_post_2hubs.ges_sf_rod.gralin_25
        gralin_25 = ascene.getObject(".{}.ges_sf_rod.gralin_25".format(model_name))
        if not gralin_25 :
            return
        gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        gralin_25.orientation = axis
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, gralin_25.location, gralin_25.orientation)
        gralin_25.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_25.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------计算ges_sf_rod物体的长度且保持不变
        CYLINDER_30 = ascene.getObject(".{}.ges_sf_rod.CYLINDER_30".format(model_name))
        if not CYLINDER_30 :
            return
        CYLINDER_30.length = geo_len

        #---------._AA_nlg_post_2hubs.ges_sf_rod.cm
        cm = ascene.getObject(".{}.ges_sf_rod.cm".format(model_name))
        if not cm :
            return
        #cm.recompute()
        cm.location = 0.5*(hps_rod_top.location+hps_rod_bot.location)
        cm.orientation = VecUtils.ORI_ALONG_AXIS(hps_rod_bot.location, hps_rod_top.location, 'z')
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------._AA_nlg_post_2hubs.ges_sf_rod.MARKER_84
        MARKER_84 = ascene.getObject(".{}.ges_sf_rod.MARKER_84".format(model_name))
        if not MARKER_84 :
            return
        MARKER_84.location = center_loc
        MARKER_84.orientation = VecUtils.ORI_ALONG_AXIS(hps_db_uc_atch_loc, hps_db_sf_atch_loc, "Z")
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_84.location, MARKER_84.orientation)
        MARKER_84.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_84.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_nlg_post_2hubs.ges_sf_actuator.MARKER_85
        MARKER_85 = ascene.getObject(".{}.ges_sf_actuator.MARKER_85".format(model_name))
        if not MARKER_85 :
            return
        MARKER_85.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        MARKER_85.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_85.location, MARKER_85.orientation)
        MARKER_85.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_85.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------._AA_nlg_post_2hubs.ges_sf_rod.MARKER_96
        MARKER_96 = ascene.getObject(".{}.ges_sf_rod.MARKER_96".format(model_name))
        if not MARKER_96 :
            return
        MARKER_96.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_96.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_96.location, MARKER_96.orientation)
        MARKER_96.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_96.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------._AA_nlg_post_2hubs.ges_sf_rod.MARKER_5
        MARKER_5 = ascene.getObject(".{}.ges_sf_rod.MARKER_5".format(model_name))
        if not MARKER_5 :
            return
        MARKER_5.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_5.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_5.location, MARKER_5.orientation)
        MARKER_5.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_5.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------._AA_nlg_post_2hubs.ges_upper_cylinder
        ges_upper_cylinder = ascene.getObject(".{}.ges_upper_cylinder".format(model_name))
        if not ges_upper_cylinder :
            return
        #--------._AA_nlg_post_2hubs.ges_upper_cylinder.MARKER_4
        MARKER_4 = ascene.getObject(".{}.ges_upper_cylinder.MARKER_4".format(model_name))
        if not MARKER_4 :
            return
        MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_5))
        MARKER_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_5))
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_4.location, MARKER_4.orientation)
        MARKER_4.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_4.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------添加并修改ges_sf_rod上的marker点--------------------
        #---------.ges_sf_rod.MARKER_511
        MARKER_511 = ascene.getObject(".{}.ges_sf_rod.MARKER_511".format(model_name))
        if not MARKER_511 :
            print("31")
            return
        MARKER_511.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_84))
        MARKER_511.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_511.location, MARKER_511.orientation)
        MARKER_511.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_511.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_rod.MARKER_101
        MARKER_101 = ascene.getObject(".{}.ges_sf_rod.MARKER_101".format(model_name))
        if not MARKER_101 :
            print("31")
            return
        MARKER_101.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_101.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_101.location, MARKER_101.orientation)
        MARKER_101.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_101.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_rod.MARKER_91
        MARKER_91 = ascene.getObject(".{}.ges_sf_rod.MARKER_91".format(model_name))
        if not MARKER_91 :
            print("31")
            return
        MARKER_91.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_91.orientation = (VecUtils.ORI_RELATIVE_TO([0,0,0],MARKER_84))
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_91.location, MARKER_91.orientation)
        MARKER_91.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_91.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_rod.MARKER_90
        MARKER_90 = ascene.getObject(".{}.ges_sf_rod.MARKER_90".format(model_name))
        if not MARKER_90 :
            print("31")
            return
        MARKER_90.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_90.orientation = (VecUtils.ORI_RELATIVE_TO([0,0,0],MARKER_84))
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_90.location, MARKER_90.orientation)
        MARKER_90.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_90.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_rod.MARKER_88
        MARKER_88 = ascene.getObject(".{}.ges_sf_rod.MARKER_88".format(model_name))
        if not MARKER_88 :
            print("31")
            return
        MARKER_88.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_88.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_88.location, MARKER_88.orientation)
        MARKER_88.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_88.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_rod.MARKER_80
        MARKER_80 = ascene.getObject(".{}.ges_sf_rod.MARKER_80".format(model_name))
        if not MARKER_80 :
            print("31")
            return
        MARKER_80.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_84))
        MARKER_80.orientation = Jusme.Vector(270.0, 120, 180.0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_80.location, MARKER_80.orientation)
        MARKER_80.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_80.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_rod.MARKER_79
        MARKER_79 = ascene.getObject(".{}.ges_sf_rod.MARKER_79".format(model_name))
        if not MARKER_79 :
            print("31")
            return
        MARKER_79.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_84))
        MARKER_79.orientation = Jusme.Vector(270.0, 120, 180.0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_79.location, MARKER_79.orientation)
        MARKER_79.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_79.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_rod.MARKER_stopper_rod
        MARKER_stopper_rod = ascene.getObject(".{}.ges_sf_rod.MARKER_stopper_rod".format(model_name))
        if not MARKER_stopper_rod :
            print("31")
            return
        MARKER_stopper_rod.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_stopper_rod.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_stopper_rod.location, MARKER_stopper_rod.orientation)
        MARKER_stopper_rod.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_stopper_rod.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_rod.MARKER_785
        MARKER_785 = ascene.getObject(".{}.ges_sf_rod.MARKER_785".format(model_name))
        if not MARKER_785 :
            print("31")
            return
        MARKER_785.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_785.orientation = (VecUtils.ORI_RELATIVE_TO([0,0,0],MARKER_84))
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_785.location, MARKER_785.orientation)
        MARKER_785.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_785.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_rod.MARKER_784
        MARKER_784 = ascene.getObject(".{}.ges_sf_rod.MARKER_784".format(model_name))
        if not MARKER_784 :
            print("31")
            return
        MARKER_784.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_784.orientation = (VecUtils.ORI_RELATIVE_TO([0,0,0],MARKER_84))
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_784.location, MARKER_784.orientation)
        MARKER_784.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_784.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------添加并修改ges_sf_actuator上的marker点--------------------
        #---------.ges_sf_actuator.MARKER_532
        MARKER_532 = ascene.getObject(".{}.ges_sf_actuator.MARKER_532".format(model_name))
        if not MARKER_532 :
            print("31")
            return
        MARKER_532.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        MARKER_532.orientation = Jusme.Vector(180,90,180)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_532.location, MARKER_532.orientation)
        MARKER_532.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_532.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_actuator.MARKER_512
        MARKER_512 = ascene.getObject(".{}.ges_sf_actuator.MARKER_512".format(model_name))
        if not MARKER_512 :
            print("31")
            return
        MARKER_512.location = 0.5*(hps_db_sf_atch.location+hps_db_uc_atch.location)
        MARKER_512.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_512.location, MARKER_512.orientation)
        MARKER_512.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_512.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_actuator.MARKER_100
        MARKER_100 = ascene.getObject(".{}.ges_sf_actuator.MARKER_100".format(model_name))
        if not MARKER_100 :
            print("31")
            return
        MARKER_100.location = (VecUtils.LOC_RELATIVE_TO([0,0,0],hps_rod_bot))
        MARKER_100.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_100.location, MARKER_100.orientation)
        MARKER_100.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_100.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_actuator.MARKER_89
        MARKER_89 = ascene.getObject(".{}.ges_sf_actuator.MARKER_89".format(model_name))
        if not MARKER_89 :
            print("31")
            return
        MARKER_89.location = (VecUtils.LOC_RELATIVE_TO([0,0,0],hps_rod_bot))
        MARKER_89.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_89.location, MARKER_89.orientation)
        MARKER_89.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_89.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_sf_actuator.stopper_actuator
        stopper_actuator = ascene.getObject(".{}.ges_sf_actuator.stopper_actuator".format(model_name))
        if not stopper_actuator :
            print("31")
            return
        stopper_actuator.location = (VecUtils.LOC_RELATIVE_TO([0,0,0],hps_rod_bot))
        stopper_actuator.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, stopper_actuator.location, stopper_actuator.orientation)
        stopper_actuator.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        stopper_actuator.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------添加并修改ges_subframe上的marker点--------------------
        #---------.ges_subframe.MARKER_533
        MARKER_533 = ascene.getObject(".{}.ges_subframe.MARKER_533".format(model_name))
        if not MARKER_533 :
            print("31")
            return
        MARKER_533.location = (VecUtils.LOC_RELATIVE_TO([0,0,0],hps_db_sf_atch))
        MARKER_533.orientation = Jusme.Vector(180,90,180)
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, MARKER_533.location, MARKER_533.orientation)
        MARKER_533.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_533.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_subframe.MARKER_527
        MARKER_527 = ascene.getObject(".{}.ges_subframe.MARKER_527".format(model_name))
        if not MARKER_527 :
            print("31")
            return
        MARKER_527.location = 0.5*(hps_uc_sf_atch_l.location+hps_uc_sf_atch_r.location)
        MARKER_527.orientation = Jusme.Vector(180,90,180)
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, MARKER_527.location, MARKER_527.orientation)
        MARKER_527.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_527.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------.ges_subframe.MARKER_517
        MARKER_517 = ascene.getObject(".{}.ges_subframe.MARKER_517".format(model_name))
        if not MARKER_517 :
            print("31")
            return
        MARKER_517.location = 0.5*(hps_uc_sf_atch_l.location+hps_uc_sf_atch_r.location)
        MARKER_517.orientation = Jusme.Vector(180,90,180)
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, MARKER_517.location, MARKER_517.orientation)
        MARKER_517.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_517.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #---------------------更新相关的运动副、测量和驱动
        #------------._AA_nlg_post_2hubs.joscyl_db_sf
        joscyl_db_sf = ascene.getObject(".{}.joscyl_db_sf".format(model_name))
        if not joscyl_db_sf :
            print("32")
            return
        joscyl_db_sf.recompute()

        #------------._AA_nlg_post_2hubs.joscly_ac_rd
        joscly_ac_rd = ascene.getObject(".{}.joscly_ac_rd".format(model_name))
        if not joscly_ac_rd :
            print("32")
            return
        joscly_ac_rd.recompute()

        #----------._AA_nlg_post_2hubs.josfix_subframe_to_body
        josfix_subframe_to_body = ascene.getObject(".{}.josfix_subframe_to_body".format(model_name))
        if not josfix_subframe_to_body :
            print("35")
            return
        josfix_subframe_to_body.recompute()

        #---------._AA_nlg_post_2hubs.mts_fixed_2
        mts_fixed_2 = ascene.getObject(".{}.mts_fixed_2".format(model_name))
        if not mts_fixed_2 :
            print("36")
            return
        mts_fixed_2.recompute()

        

        #------._AA_nlg_post_2hubs.NLG_disp_sf
        NLG_disp_sf = ascene.getObject(".{}.NLG_disp_sf".format(model_name))
        if not NLG_disp_sf :
            print("38")
            return
        NLG_disp_sf.recompute()

        # #------.NLG_SPRING_nlg
        # NLG_SPRING_nlg = ascene.getObject(".{}.NLG_SPRING_nlg".format(model_name))
        # if not NLG_SPRING_nlg :
        #     print("38")
        #     return
        # NLG_SPRING_nlg.recompute()

        #------.NLG_stopper_low
        NLG_stopper_low = ascene.getObject(".{}.NLG_stopper_low".format(model_name))
        if not NLG_stopper_low :
            print("38")
            return
        NLG_stopper_low.recompute()

        #------.NLG_stopper_up
        NLG_stopper_up = ascene.getObject(".{}.NLG_stopper_up".format(model_name))
        if not NLG_stopper_up :
            print("38")
            return
        NLG_stopper_up.recompute()

        #------.nlg_ZDT_FORCE
        nlg_ZDT_FORCE = ascene.getObject(".{}.nlg_ZDT_FORCE".format(model_name))
        if not nlg_ZDT_FORCE :
            print("38")
            return
        nlg_ZDT_FORCE.recompute()

        #------.NLG_aeroforce
        NLG_aeroforce = ascene.getObject(".{}.NLG_aeroforce".format(model_name))
        if not NLG_aeroforce :
            print("38")
            return
        NLG_aeroforce.recompute()

        #------.jossph_rd_uc
        jossph_rd_uc = ascene.getObject(".{}.jossph_rd_uc".format(model_name))
        if not jossph_rd_uc :
            print("38")
            return
        jossph_rd_uc.recompute()

        print('完成调整hps_rod_bot')

        pass
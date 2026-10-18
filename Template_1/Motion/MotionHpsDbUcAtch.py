import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common


class MotionHpsDbUcAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始收放仿真hps_db_uc_atch硬点调整")

        ascene = Jusme.ActiveUSScene
        #--------------得到模型名称
        model_name = Common.getModelName()

        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            return

        #--------._AA_ges_post_2hubs.ground.hps_db_uc_atch
        hps_db_uc_atch = ascene.getObject(self.hps_full_name)
        if not hps_db_uc_atch :
            return
        hps_db_uc_atch_loc = hps_db_uc_atch.location

        #-------._AA_ges_post_2hubs.ground.hps_db_sf_atch
        hps_db_sf_atch = ascene.getObject(".{}.ground.hps_db_sf_atch".format(model_name))
        if not hps_db_sf_atch :
            return
        hps_db_sf_atch_loc = hps_db_sf_atch.location

        #-------._AA_ges_post_2hubs.ground.hps_rod_top
        hps_rod_top = ascene.getObject(".{}.ground.hps_rod_top".format(model_name))
        if not hps_rod_top :
            return
        hps_rod_top_loc = hps_rod_top.location

        #-------._AA_ges_post_2hubs.ground.hps_rod_bot
        hps_rod_bot = ascene.getObject(".{}.ground.hps_rod_bot".format(model_name))
        if not hps_rod_bot :
            return
        hps_rod_bot_loc = hps_rod_bot.location

        #-------._AA_ges_post_2hubs.ges_sf_actuator
        ges_sf_actuator = ascene.getObject(".{}.ges_sf_actuator".format(model_name))
        if not ges_sf_actuator :
            return
        center_loc = 0.5 * (hps_db_uc_atch_loc + hps_db_sf_atch_loc)
        axis = VecUtils.ORI_ALONG_AXIS(hps_db_sf_atch_loc, hps_db_uc_atch_loc, 'z')
        geo_len = VecUtils.DM(hps_db_sf_atch_loc, hps_db_uc_atch_loc)
        #------设定ges_sf_actuator物体的位置和方向
        ges_sf_actuator.location = center_loc
        ges_sf_actuator.orientation = axis

        #-----------------._AA_ges_post_2hubs.ges_sf_actuator.gralin_1
        gralin_1 = ascene.getObject(".{}.ges_sf_actuator.gralin_1".format(model_name))
        if not gralin_1 :
            return
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        gralin_1.orientation = axis
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------._AA_ges_post_2hubs.ges_sf_actuator.gralin_dragbrace_geom
        gralin_dragbrace_geom = ascene.getObject(".{}.ges_sf_actuator.gralin_dragbrace_geom".format(model_name))
        if not gralin_dragbrace_geom :
            return
        gralin_dragbrace_geom.length = geo_len

        #-----------------._AA_ges_post_2hubs.ges_sf_actuator.cm
        cm = ascene.getObject(".{}.ges_sf_actuator.cm".format(model_name))
        if not cm :
            return
        cm.recompute()
        # cm.location = center_loc
        # cm.orientation = axis
        # loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------._AA_ges_post_2hubs.ges_sf_actuator.inertia_frame
        inertia_frame = ascene.getObject(".{}.ges_sf_actuator.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = axis
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------------._AA_ges_post_2hubs.ges_subframe
        ges_subframe = ascene.getObject(".{}.ges_subframe".format(model_name))
        if not ges_subframe :
            return

        #--------._AA_ges_post_2hubs.ges_subframe.jxs_joint_j_14
        jxs_joint_j_14 = ascene.getObject(".{}.ges_subframe.jxs_joint_j_14".format(model_name))
        if not jxs_joint_j_14 :
            return
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_ges_post_2hubs.ges_sf_actuator.jxs_joint_i_14
        jxs_joint_i_14 = ascene.getObject(".{}.ges_sf_actuator.jxs_joint_i_14".format(model_name))
        if not jxs_joint_i_14 :
            return
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_14))
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_14))
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------._AA_ges_post_2hubs.ges_sf_actuator.MARKER_97
        MARKER_97 = ascene.getObject(".{}.ges_sf_actuator.MARKER_97".format(model_name))
        if not MARKER_97 :
            return
        MARKER_97.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        MARKER_97.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_97.location, MARKER_97.orientation)
        MARKER_97.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_97.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])






       

        

        #----------------------------------------------对内筒进行结构参数化调整
        #--------------------._AA_ges_post_2hubs.ges_sf_rod
        ges_sf_rod = ascene.getObject(".{}.ges_sf_rod".format(model_name))
        if not ges_sf_rod :
            return

        #-------计算ges_sf_rod物体的长度且保持不变
        CYLINDER_30 = ascene.getObject(".{}.ges_sf_rod.CYLINDER_30".format(model_name))
        if not CYLINDER_30 :
            return
        CYLINDER_30_len = CYLINDER_30.length

        #rod_bot_len = VecUtils.DM(hps_db_sf_atch_loc, hps_rod_bot_loc)
        #rod_top_len = VecUtils.DM(hps_db_sf_atch_loc, hps_rod_top_loc)

        geo_len = VecUtils.DM(hps_db_sf_atch_loc, hps_db_uc_atch_loc)

        #-------更新ges_sf_rod物体的顶部和底部硬点
        hps_rod_bot.location = VecUtils.LOC_ALONG_LINE(hps_db_sf_atch_loc, hps_db_uc_atch_loc, geo_len + 20)
        hps_rod_top.location = VecUtils.LOC_ALONG_LINE(hps_db_sf_atch_loc, hps_db_uc_atch_loc, geo_len + 20 - CYLINDER_30_len)
        hps_rod_bot_loc = hps_rod_bot.location
        hps_rod_top_loc = hps_rod_top.location

        #------计算ges_sf_rod物体的轴线和中心点
        axis = VecUtils.ORI_ALONG_AXIS(hps_rod_bot_loc, hps_db_sf_atch_loc, "z")
        center_loc = 0.5 * (hps_rod_top_loc + hps_rod_bot_loc)
        geo_len = VecUtils.DM(hps_rod_bot_loc, hps_rod_top_loc)
        ges_sf_rod.location = center_loc
        ges_sf_rod.orientation = axis

        #-----------._AA_ges_post_2hubs.ges_sf_rod.gralin_25
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

        #---------._AA_ges_post_2hubs.ges_sf_rod.cm
        cm = ascene.getObject(".{}.ges_sf_rod.cm".format(model_name))
        if not cm :
            return
        # cm.recompute()
        cm.location=center_loc
        cm.orientation=axis
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------._AA_ges_post_2hubs.ges_sf_rod.MARKER_84
        MARKER_84 = ascene.getObject(".{}.ges_sf_rod.MARKER_84".format(model_name))
        if not MARKER_84 :
            return
        MARKER_84.location = center_loc
        MARKER_84.orientation = VecUtils.ORI_ALONG_AXIS(hps_db_uc_atch_loc, hps_db_sf_atch_loc, "Z")
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_84.location, MARKER_84.orientation)
        MARKER_84.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_84.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_ges_post_2hubs.ges_sf_actuator.MARKER_85
        MARKER_85 = ascene.getObject(".{}.ges_sf_actuator.MARKER_85".format(model_name))
        if not MARKER_85 :
            return
        MARKER_85.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        MARKER_85.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_85.location, MARKER_85.orientation)
        MARKER_85.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_85.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------._AA_ges_post_2hubs.ges_sf_rod.MARKER_96
        MARKER_96 = ascene.getObject(".{}.ges_sf_rod.MARKER_96".format(model_name))
        if not MARKER_96 :
            return
        MARKER_96.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_96.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_96.location, MARKER_96.orientation)
        MARKER_96.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_96.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------._AA_ges_post_2hubs.ges_sf_rod.MARKER_5
        MARKER_5 = ascene.getObject(".{}.ges_sf_rod.MARKER_5".format(model_name))
        if not MARKER_5 :
            return
        MARKER_5.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_5.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_5.location, MARKER_5.orientation)
        MARKER_5.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_5.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------._AA_ges_post_2hubs.ges_upper_cylinder
        ges_upper_cylinder = ascene.getObject(".{}.ges_upper_cylinder".format(model_name))
        if not ges_upper_cylinder :
            print("24")
            return
        #--------._AA_ges_post_2hubs.ges_upper_cylinder.MARKER_4
        MARKER_4 = ascene.getObject(".{}.ges_upper_cylinder.MARKER_4".format(model_name))
        if not MARKER_4 :
            print("25")
            return
        MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_5))
        MARKER_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_5))
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_4.location, MARKER_4.orientation)
        MARKER_4.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_4.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        

        #--------. .ges_sf_actuator.stopper_actuator
        stopper_actuator = ascene.getObject(".{}.ges_sf_actuator.stopper_actuator".format(model_name))
        if not stopper_actuator :
            print("26")
            return
        stopper_actuator.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_rod_bot)
        stopper_actuator.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, stopper_actuator.location, stopper_actuator.orientation)
        stopper_actuator.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        stopper_actuator.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

     

        #--------. .ges_sf_rod.MARKER_stopper_rod
        MARKER_stopper_rod = ascene.getObject(".{}.ges_sf_rod.MARKER_stopper_rod".format(model_name))
        if not MARKER_stopper_rod :
            print("26")
            return
        MARKER_stopper_rod.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_rod_bot)
        MARKER_stopper_rod.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_stopper_rod.location, MARKER_stopper_rod.orientation)
        MARKER_stopper_rod.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_stopper_rod.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .ges_sf_rod.MARKER_88
        MARKER_88 = ascene.getObject(".{}.ges_sf_rod.MARKER_88".format(model_name))
        if not MARKER_88 :
            print("26")
            return
        MARKER_88.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_rod_bot)
        MARKER_88.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_88.location, MARKER_88.orientation)
        MARKER_88.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_88.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        cm = ascene.getObject(".{}.ges_sf_rod.cm".format(model_name))
        if not cm :
            print("26")
            return

        

        #--------. .ges_sf_rod.MARKER_101
        MARKER_101 = ascene.getObject(".{}.ges_sf_rod.MARKER_101".format(model_name))
        if not MARKER_101 :
            print("26")
            return
        MARKER_101.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_rod_bot)
        MARKER_101.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, MARKER_101.location, MARKER_101.orientation)
        MARKER_101.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_101.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_ges_post_2hubs.ges_sf_actuator.MARKER_89
        MARKER_89 = ascene.getObject(".{}.ges_sf_actuator.MARKER_89".format(model_name))
        if not MARKER_89 :
            return
        MARKER_89.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], hps_rod_bot))
        MARKER_89.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_89.location, MARKER_89.orientation)
        MARKER_89.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_89.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_ges_post_2hubs.ges_sf_actuator.MARKER_100
        MARKER_100 = ascene.getObject(".{}.ges_sf_actuator.MARKER_100".format(model_name))
        if not MARKER_100 :
            return
        MARKER_100.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], hps_rod_bot))
        MARKER_100.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, MARKER_100.location, MARKER_100.orientation)
        MARKER_100.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_100.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------------更新相关的运动副、测量和驱动
        
        
        

        #----------. .josfix_subframe_to_body
        josfix_subframe_to_body = ascene.getObject(".{}.josfix_subframe_to_body".format(model_name))
        if not josfix_subframe_to_body :
            print("52")
            return
        josfix_subframe_to_body.recompute()

        #---------. .mts_fixed_2
        mts_fixed_2 = ascene.getObject(".{}.mts_fixed_2".format(model_name))
        if not mts_fixed_2 :
            print("53")
            return
        mts_fixed_2.recompute()

        #----------._AA_nlg_post_2hubs.joscyl_db_sf
        joscyl_db_sf = ascene.getObject(".{}.joscyl_db_sf".format(model_name))
        if not joscyl_db_sf :
            print("57")
            return
        joscyl_db_sf.recompute()

        #------. .MOTION_LEFT
        MOTION_LEFT = ascene.getObject(".{}.MOTION_LEFT".format(model_name))
        if not MOTION_LEFT :
            print("54")
            return
        MOTION_LEFT.recompute()

        #------. .MOTION_RIGHT
        MOTION_RIGHT = ascene.getObject(".{}.MOTION_RIGHT".format(model_name))
        if not MOTION_RIGHT :
            print("54")
            return
        MOTION_RIGHT.recompute()

        #---------._AA_nlg_post_2hubs.disp_sf
        disp_sf = ascene.getObject(".{}.disp_sf".format(model_name))
        if not disp_sf :
            print("54")
            return
        disp_sf.recompute()

        #---------._AA_nlg_post_2hubs.disp_sf_right
        disp_sf_right = ascene.getObject(".{}.disp_sf_right".format(model_name))
        if not disp_sf_right :
            print("54")
            return
        disp_sf_right.recompute()

        #---------._AA_nlg_post_2hubs.disp_sf_left
        disp_sf_left = ascene.getObject(".{}.disp_sf_left".format(model_name))
        if not disp_sf_left :
            print("54")
            return
        disp_sf_left.recompute()

        


        joscly_ac_rd= ascene.getObject(".{}.joscly_ac_rd".format(model_name))
        if not joscly_ac_rd :
            print("55")
            return
        joscly_ac_rd.recompute()

        

        jossph_rd_uc= ascene.getObject(".{}.jossph_rd_uc".format(model_name))
        if not jossph_rd_uc :
            print("55")
            return
        jossph_rd_uc.recompute()

        #--------._AA_nlg_post_2hubs.MOTION_disp
        MOTION_disp = ascene.getObject(".{}.MOTION_disp".format(model_name))
        if not MOTION_disp :
            return
        MOTION_disp.recompute()

        print('完成调整hps_db_uc_atch')

        pass
import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common


class RetractionHpsDbSfAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始收放仿真hps_db_sf_atch硬点调整")
        ascene = Jusme.ActiveUSScene
        #--------------得到模型名称
        model_name = Common.getModelName()

        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            return

        #-------------------hps_db_sf_atch
        hps_db_sf_atch = ascene.getObject(self.hps_full_name)
        if not hps_db_sf_atch :
            return
        hps_db_sf_atch_loc = hps_db_sf_atch.location

        #--------------._AA_nlg_post_2hubs.ground.hps_db_uc_atch    
        hps_db_uc_atch = ascene.getObject(".{}.ground.hps_db_uc_atch".format(model_name))
        if not hps_db_uc_atch :
            return
        hps_db_uc_atch_loc = hps_db_uc_atch.location

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

        #----------._AA_nlg_post_2hubs.ground.hps_rod_top
        hps_rod_top = ascene.getObject(".{}.ground.hps_rod_top".format(model_name))
        if not hps_rod_top :
            return
        hps_rod_top_loc = hps_rod_top.location

        #------------._AA_nlg_post_2hubs.ground.hps_rod_bot
        hps_rod_bot = ascene.getObject(".{}.ground.hps_rod_bot".format(model_name))
        if not hps_rod_bot :
            return
        hps_rod_bot_loc = hps_rod_bot.location

        #---------------------计算ges_sf_actuator的方向，中心点和长度
        axis = VecUtils.ORI_ALONG_AXIS(hps_db_sf_atch_loc, hps_db_uc_atch_loc, 'z')
        center_loc = 0.5 * (hps_db_sf_atch_loc + hps_db_uc_atch_loc)
        geo_len = VecUtils.DM(hps_db_sf_atch_loc, hps_db_uc_atch_loc)

        #-----------------------------------------------对外筒ges_sf_actuator进行结构参数化调整
        #-----------------._AA_nlg_post_2hubs.ges_sf_actuator
        ges_sf_actuator = ascene.getObject(".{}.ges_sf_actuator".format(model_name))
        if not ges_sf_actuator :
            return
        ges_sf_actuator.location = center_loc
        ges_sf_actuator.orientation = axis

        #-----------------._AA_nlg_post_2hubs.ges_sf_actuator.gralin_1
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
        
        # cm.location = center_loc
        # cm.orientation = axis
        # loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

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
        #--------------------._AA_nlg_post_2hubs.ges_sf_rod
        ges_sf_rod = ascene.getObject(".{}.ges_sf_rod".format(model_name))
        if not ges_sf_rod :
            return

        #------------._AA_nlg_post_2hubs.ground.hps_rod_top
        #-------计算hps_rod_top的新位置
        #-------确保hps_rod_top处于hps_db_uc_atch和hps_db_sf_atch之间的直线上
        #-------保证ges_sf_rod物体的长途不变
        geo_len = VecUtils.DM(hps_db_uc_atch_loc, hps_rod_top_loc)
        hps_rod_top.location = VecUtils.LOC_ALONG_LINE(hps_db_uc_atch_loc, hps_db_sf_atch_loc, geo_len)
        hps_rod_top_loc = hps_rod_top.location

        #-------计算ges_sf_rod物体的长度且保持不变
        CYLINDER_30 = ascene.getObject(".{}.ges_sf_rod.CYLINDER_30".format(model_name))
        if not CYLINDER_30 :
            return
        geo_len = CYLINDER_30.length
        hps_rod_bot.location = VecUtils.LOC_ALONG_LINE(hps_rod_top_loc, hps_db_uc_atch_loc, geo_len)
        hps_rod_bot_loc = hps_rod_bot.location

        #------计算ges_sf_rod物体的轴线和中心点
        axis = VecUtils.ORI_ALONG_AXIS(hps_rod_bot_loc, hps_db_sf_atch_loc, "z")
        center_loc = 0.5 * (hps_rod_top_loc + hps_rod_bot_loc)
        geo_len = VecUtils.DM(hps_rod_bot_loc, hps_rod_top_loc)
        ges_sf_rod.location = center_loc
        ges_sf_rod.orientation = axis

        #-----------._AA_nlg_post_2hubs.ges_sf_rod.gralin_25
        gralin_25 = ascene.getObject(".{}.ges_sf_rod.gralin_25".format(model_name))
        if not gralin_25 :
            return
        gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        gralin_25.orientation = axis
        loc_ori = VecUtils.global2local(ges_sf_rod.location, ges_sf_rod.orientation, gralin_25.location, gralin_25.orientation)
        gralin_25.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_25.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------计算前起收放作动筒原始长度
        #---------------------._AA_nlg_post_2hubs.ges_sf_rod.CYLINDER_30
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





        #--------------------------._AA_nlg_post_2hubs.ges_subframe
        ges_subframe = ascene.getObject(".{}.ges_subframe".format(model_name))
        if not ges_subframe :
            return

        #---------._AA_nlg_post_2hubs.ges_subframe.graout_1
        graout_1 = ascene.getObject(".{}.ges_subframe.graout_1".format(model_name))
        if not graout_1 :
            return
        graout_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_sf_atch_r))
        graout_1_loc = graout_1.location

        #---------._AA_nlg_post_2hubs.ges_subframe.graout_2
        graout_2 = ascene.getObject(".{}.ges_subframe.graout_2".format(model_name))
        if not graout_2 :
            return
        graout_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_sf_atch_l))
        graout_2_loc = graout_2.location
        
        #---------._AA_nlg_post_2hubs.ges_subframe.graout_3
        graout_3 = ascene.getObject(".{}.ges_subframe.graout_3".format(model_name))
        if not graout_3 :
            return
        graout_3.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        graout_3_loc = graout_3.location

        nor_vec = VecUtils.ORI_IN_PLANE(graout_1_loc, graout_2_loc, graout_3_loc, "z_zx")
        graout_1.orientation = nor_vec
        graout_2.orientation = nor_vec
        graout_3.orientation = nor_vec

        ges_subframe_center_loc = (graout_1_loc + graout_2_loc + graout_3_loc) / 3.0
        ges_subframe.location = ges_subframe_center_loc
        ges_subframe.orientation = nor_vec

        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, graout_1.location, graout_1.orientation)
        graout_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        graout_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, graout_2.location, graout_2.orientation)
        graout_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        graout_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, graout_3.location, graout_3.orientation)
        graout_3.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        graout_3.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------._AA_nlg_post_2hubs.ges_subframe.cm
        cm = ascene.getObject(".{}.ges_subframe.cm".format(model_name))
        if not cm :
            return
        cm.location = ges_subframe_center_loc
        cm.orientation = nor_vec
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #--------._AA_nlg_post_2hubs.ges_subframe.inertia_frame
        inertia_frame = ascene.getObject(".{}.ges_subframe.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ges_subframe))
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------._AA_nlg_post_2hubs.ges_subframe.jxs_joint_j_14
        jxs_joint_j_14 = ascene.getObject(".{}.ges_subframe.jxs_joint_j_14".format(model_name))
        if not jxs_joint_j_14 :
            return
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        
        #------._AA_nlg_post_2hubs.ges_sf_actuator.jxs_joint_i_14
        jxs_joint_i_14 = ascene.getObject(".{}.ges_sf_actuator.jxs_joint_i_14".format(model_name))
        if not jxs_joint_i_14 :
            return
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_14))
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_14))
        loc_ori = VecUtils.global2local(ges_sf_actuator.location, ges_sf_actuator.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------._AA_nlg_post_2hubs.ground.cfs_uc_sf_atch_mid
        #---------目前从Adams模型中没有定义拓扑关联
        #--------位置默认按hps_uc_sf_atch_r和hps_uc_sf_atch_l的中点处理
        #--------方向按ges_subframe物体的方向处理
        cfs_uc_sf_atch_mid = ascene.getObject(".{}.ground.cfs_uc_sf_atch_mid".format(model_name))
        if not cfs_uc_sf_atch_mid :
            return
        cfs_uc_sf_atch_mid.location = 0.5 * (hps_uc_sf_atch_r_loc + hps_uc_sf_atch_l_loc)
        cfs_uc_sf_atch_mid.orientation = nor_vec

        #------._AA_nlg_post_2hubs.ges_subframe.jxs_joint_j_15
        jxs_joint_j_15 = ascene.getObject(".{}.ges_subframe.jxs_joint_j_15".format(model_name))
        if not jxs_joint_j_15 :
            return
        jxs_joint_j_15.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfs_uc_sf_atch_mid))
        #-------茉莉平台中没有(ORI_LOCAL(ORI_ALIGN_AXIS(cfs_uc_sf_atch_mid, "Z+Z"), ges_subframe))
        #-------相关处理函数，默认按cfs_uc_sf_atch_mid的同向处理
        jxs_joint_j_15.orientation = nor_vec
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_j_15.location, jxs_joint_j_15.orientation)
        jxs_joint_j_15.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_15.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------._AA_nlg_post_2hubs.ges_upper_cylinder
        ges_upper_cylinder = ascene.getObject(".{}.ges_upper_cylinder".format(model_name))
        if not ges_upper_cylinder :
            return
        
        #------._AA_nlg_post_2hubs.ges_upper_cylinder.jxs_joint_i_15
        jxs_joint_i_15 = ascene.getObject(".{}.ges_upper_cylinder.jxs_joint_i_15".format(model_name))
        if not jxs_joint_i_15 :
            return
        jxs_joint_i_15.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_15))
        jxs_joint_i_15.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_15))
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_i_15.location, jxs_joint_i_15.orientation)
        jxs_joint_i_15.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_15.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------._AA_nlg_post_2hubs.ground.cfs_subframe_to_body_point
        cfs_subframe_to_body_point = ascene.getObject(".{}.ground.cfs_subframe_to_body_point".format(model_name))
        if not cfs_subframe_to_body_point :
            return
        cfs_subframe_to_body_point.location = ges_subframe_center_loc
        cfs_subframe_to_body_point.orientation = nor_vec

        # #-------------._AA_nlg_post_2hubs.mts_body_mount
        # mts_body_mount = ascene.getObject(".{}.mts_body_mount".format(model_name))
        # if not mts_body_mount :
        #     return
        # mts_body_mount.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfs_subframe_to_body_point))
        # mts_body_mount.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))

        # #----------._AA_nlg_post_2hubs.ground.mts_mount_j_2
        # mts_mount_j_2 = ascene.getObject(".{}.ground.mts_mount_j_2".format(model_name))
        # if not mts_mount_j_2 :
        #     return
        # mts_mount_j_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], mts_body_mount))
        # mts_mount_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], mts_body_mount))

        # #---------._AA_nlg_post_2hubs.mts_body_mount.mount_i
        # mount_i = ascene.getObject(".{}.mts_body_mount.mount_i".format(model_name))
        # if not mount_i :
        #     return
        # mount_i.location = ges_subframe_center_loc
        # mount_i.orientation = Jusme.Vector(0, 0, 0)
        # loc_ori = VecUtils.global2local(mts_body_mount.location, mts_body_mount.orientation, mount_i.location, mount_i.orientation)
        # mount_i.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # mount_i.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        # #-------------._AA_nlg_post_2hubs.mts_body_mount.jxs_joint_j_16
        # jxs_joint_j_16 = ascene.getObject(".{}.mts_body_mount.jxs_joint_j_16".format(model_name))
        # if not jxs_joint_j_16 :
        #     return
        # jxs_joint_j_16.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfs_subframe_to_body_point))
        # jxs_joint_j_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        # loc_ori = VecUtils.global2local(mts_body_mount.location, mts_body_mount.orientation, jxs_joint_j_16.location, jxs_joint_j_16.orientation)
        # jxs_joint_j_16.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # jxs_joint_j_16.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        # #---------._AA_nlg_post_2hubs.ges_subframe.jxs_joint_i_16
        # jxs_joint_i_16 = ascene.getObject(".{}.ges_subframe.jxs_joint_i_16".format(model_name))
        # if not jxs_joint_i_16 :
        #     return
        # jxs_joint_i_16.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_16))
        # jxs_joint_i_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_16))
        # loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_i_16.location, jxs_joint_i_16.orientation)
        # jxs_joint_i_16.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # jxs_joint_i_16.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------添加并修改ges_sf_rod上的marker点--------------------
        

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


        #--------------------添加并修改ges_sf_actuator上的marker点--------------------

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
        MARKER_160 = ascene.getObject(".{}.ges_subframe.MARKER_160".format(model_name))
        if not MARKER_160 :
            print("31")
            return
        MARKER_160.location = (1/3)*(hps_db_sf_atch.location+hps_uc_sf_atch_l.location+hps_uc_sf_atch_r.location)
        MARKER_160.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, MARKER_160.location, MARKER_160.orientation)
        MARKER_160.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_160.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------添加并修改ground上的marker点--------------------
        MARKER_161 = ascene.getObject(".{}.ground.MARKER_161".format(model_name))
        if not MARKER_161 :
            print("31")
            return
        MARKER_161.location = (1/3)*(hps_db_sf_atch.location+hps_uc_sf_atch_l.location+hps_uc_sf_atch_r.location)
        MARKER_161.orientation = Jusme.Vector(0,0,0)
        










        #------------._AA_nlg_post_2hubs.joscyl_db_sf
        joscyl_db_sf = ascene.getObject(".{}.joscyl_db_sf".format(model_name))
        if not joscyl_db_sf :
            return
        joscyl_db_sf.recompute()

        #------------._AA_nlg_post_2hubs.joscly_ac_rd
        joscly_ac_rd = ascene.getObject(".{}.joscly_ac_rd".format(model_name))
        if not joscly_ac_rd :
            return
        joscly_ac_rd.recompute()

        #------------._AA_nlg_post_2hubs.jossph_rd_uc
        jossph_rd_uc = ascene.getObject(".{}.jossph_rd_uc".format(model_name))
        if not jossph_rd_uc :
            return
        jossph_rd_uc.recompute()

        #---------._AA_nlg_post_2hubs.JOINT_14
        JOINT_14 = ascene.getObject(".{}.JOINT_14".format(model_name))
        if not JOINT_14 :
            return
        JOINT_14.recompute()

        



        #------._AA_nlg_post_2hubs.MOTION_disp
        MOTION_disp = ascene.getObject(".{}.MOTION_disp".format(model_name))
        if not MOTION_disp :
            return
        MOTION_disp.recompute()

        #------._AA_nlg_post_2hubs.disp_sf
        disp_sf = ascene.getObject(".{}.disp_sf".format(model_name))
        if not disp_sf :
            return
        disp_sf.recompute()

        #------._AA_nlg_post_2hubs.NLG_aeroforce
        NLG_aeroforce = ascene.getObject(".{}.NLG_aeroforce".format(model_name))
        if not NLG_aeroforce :
            return
        NLG_aeroforce.recompute()

        print("完成调整hps_db_sf_atch")

        pass
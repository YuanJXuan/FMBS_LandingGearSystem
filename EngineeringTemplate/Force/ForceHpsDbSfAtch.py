import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common


class ForceHpsDbSfAtchAdjust(AbstractHps.AbstractHpsAdjust) :
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
            print("1")
            return
        hps_db_sf_atch_loc = hps_db_sf_atch.location

        #--------------. .ground.hps_db_uc_atch    
        hps_db_uc_atch = ascene.getObject(".{}.ground.hps_db_uc_atch".format(model_name))
        if not hps_db_uc_atch :
            print("2")
            return
        hps_db_uc_atch_loc = hps_db_uc_atch.location

        #-----------. .ground.hps_uc_sf_atch_r
        hps_uc_sf_atch_r = ascene.getObject(".{}.ground.hps_uc_sf_atch_r".format(model_name))
        if not hps_uc_sf_atch_r :
            print("3")
            return
        hps_uc_sf_atch_r_loc = hps_uc_sf_atch_r.location

        #---------. .ground.hps_uc_sf_atch_l
        hps_uc_sf_atch_l = ascene.getObject(".{}.ground.hps_uc_sf_atch_l".format(model_name))
        if not hps_uc_sf_atch_l :
            print("4")
            return
        hps_uc_sf_atch_l_loc = hps_uc_sf_atch_l.location

        #----------. .ground.hps_rod_top
        hps_rod_top = ascene.getObject(".{}.ground.hps_rod_top".format(model_name))
        if not hps_rod_top :
            print("5")
            return
        hps_rod_top_loc = hps_rod_top.location

        #------------. .ground.hps_rod_bot
        hps_rod_bot = ascene.getObject(".{}.ground.hps_rod_bot".format(model_name))
        if not hps_rod_bot :
            print("6")
            return
        hps_rod_bot_loc = hps_rod_bot.location

        #---------------------计算nlg_sf_actuator的方向，中心点和长度
        axis = VecUtils.ORI_ALONG_AXIS(hps_db_sf_atch_loc, hps_db_uc_atch_loc, 'z')
        center_loc = 0.5 * (hps_db_sf_atch_loc + hps_db_uc_atch_loc)
        geo_len = VecUtils.DM(hps_db_sf_atch_loc, hps_db_uc_atch_loc)

        #-----------------------------------------------对外筒nlg_sf_actuator进行结构参数化调整
        #-----------------. .nlg_sf_actuator
        nlg_sf_actuator = ascene.getObject(".{}.nlg_sf_actuator".format(model_name))
        if not nlg_sf_actuator :
            print("7")
            return
        nlg_sf_actuator.location = center_loc
        nlg_sf_actuator.orientation = axis

        #-----------------. .nlg_sf_actuator.gralin_1
        gralin_1 = ascene.getObject(".{}.nlg_sf_actuator.gralin_1".format(model_name))
        if not gralin_1 :
            print("8")
            return
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        gralin_1.orientation = axis
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------. .nlg_sf_actuator.gralin_dragbrace_geom
        gralin_dragbrace_geom = ascene.getObject(".{}.nlg_sf_actuator.gralin_dragbrace_geom".format(model_name))
        if not gralin_dragbrace_geom :
            print("9")
            return
        gralin_dragbrace_geom.length = geo_len

        #-----------------. .nlg_sf_actuator.cm
        cm = ascene.getObject(".{}.nlg_sf_actuator.cm".format(model_name))
        if not cm :
            print("10")
            return
        cm.recompute()
        
        # cm.location = center_loc
        # print(center_loc)
        # cm.orientation = axis
        # loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------. .nlg_sf_actuator.inertia_frame
        inertia_frame = ascene.getObject(".{}.nlg_sf_actuator.inertia_frame".format(model_name))
        if not inertia_frame :
            print("11")
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = axis
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------------. .nlg_subframe
        nlg_subframe = ascene.getObject(".{}.nlg_subframe".format(model_name))
        if not  nlg_subframe :
            print("12")
            return

        #--------. .nlg_subframe.jxs_joint_j_14
        jxs_joint_j_14 = ascene.getObject(".{}.nlg_subframe.jxs_joint_j_14".format(model_name))
        if not jxs_joint_j_14 :
            print("13")
            return
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local( nlg_subframe.location,  nlg_subframe.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .nlg_sf_actuator.jxs_joint_i_14
        jxs_joint_i_14 = ascene.getObject(".{}.nlg_sf_actuator.jxs_joint_i_14".format(model_name))
        if not jxs_joint_i_14 :
            print("15")
            return
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_14))
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_14))
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------. .nlg_sf_actuator.MARKER_97
        MARKER_97 = ascene.getObject(".{}.nlg_sf_actuator.MARKER_97".format(model_name))
        if not MARKER_97 :
            print("16")
            return
        MARKER_97.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        MARKER_97.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, MARKER_97.location, MARKER_97.orientation)
        MARKER_97.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_97.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .nlg_sf_rod
        nlg_sf_rod = ascene.getObject(".{}.nlg_sf_rod".format(model_name))
        if not nlg_sf_rod :
            print("17")
            return

        #--------. .nlg_sf_rod.MARKER_84
        MARKER_84 = ascene.getObject(".{}.nlg_sf_rod.MARKER_84".format(model_name))
        if not MARKER_84 :
            print("18")
            return
        MARKER_84.location = 0.5 * (hps_rod_bot_loc + hps_rod_bot_loc)
        MARKER_84.orientation = VecUtils.ORI_ALONG_AXIS(hps_db_uc_atch_loc, hps_db_sf_atch_loc, "Z")
        loc_ori = VecUtils.global2local(nlg_sf_rod.location, nlg_sf_rod.orientation, MARKER_84.location, MARKER_84.orientation)
        MARKER_84.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_84.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        

        #--------. .nlg_sf_actuator.MARKER_85
        # ------MARKER_85目前未发现与任何硬点有关联
        #-------在参数化结构调整中认定其为nlg_sf_rod质心位置
        MARKER_85 = ascene.getObject(".{}.nlg_sf_actuator.MARKER_85".format(model_name))
        if not MARKER_85 :
            print("19")
            return
        MARKER_85.location = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        MARKER_85.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, MARKER_85.location, MARKER_85.orientation)
        MARKER_85.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_85.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #----------------------------------------------对内筒进行结构参数化调整
        #--------------------. .nlg_sf_rod
        nlg_sf_rod = ascene.getObject(".{}.nlg_sf_rod".format(model_name))
        if not nlg_sf_rod :
            print("20")
            return

        #------------. .ground.hps_rod_top
        #-------计算hps_rod_top的新位置
        #-------确保hps_rod_top处于hps_db_uc_atch和hps_db_sf_atch之间的直线上
        #-------保证nlg_sf_rod物体的长途不变
        geo_len = VecUtils.DM(hps_db_uc_atch_loc, hps_rod_top_loc)
        hps_rod_top.location = VecUtils.LOC_ALONG_LINE(hps_db_uc_atch_loc, hps_db_sf_atch_loc, geo_len)
        hps_rod_top_loc = hps_rod_top.location

        #-------计算nlg_sf_rod物体的长度且保持不变
        CYLINDER_30 = ascene.getObject(".{}.nlg_sf_rod.CYLINDER_30".format(model_name))
        if not CYLINDER_30 :
            print("21")
            return
        geo_len = CYLINDER_30.length
        hps_rod_bot.location = VecUtils.LOC_ALONG_LINE(hps_rod_top_loc, hps_db_uc_atch_loc, geo_len)
        hps_rod_bot_loc = hps_rod_bot.location

        #------计算nlg_sf_rod物体的轴线和中心点
        axis = VecUtils.ORI_ALONG_AXIS(hps_rod_bot_loc, hps_db_sf_atch_loc, "z")
        center_loc = 0.5 * (hps_rod_top_loc + hps_rod_bot_loc)
        geo_len = VecUtils.DM(hps_rod_bot_loc, hps_rod_top_loc)
        nlg_sf_rod.location = center_loc
        nlg_sf_rod.orientation = axis

        #-----------. .nlg_sf_rod.gralin_25
        gralin_25 = ascene.getObject(".{}.nlg_sf_rod.gralin_25".format(model_name))
        if not gralin_25 :
            print("22")
            return
        gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        gralin_25.orientation = axis
        loc_ori = VecUtils.global2local(nlg_sf_rod.location, nlg_sf_rod.orientation, gralin_25.location, gralin_25.orientation)
        gralin_25.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_25.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------计算前起收放作动筒原始长度
        #---------------------. .nlg_sf_rod.CYLINDER_30
        CYLINDER_30 = ascene.getObject(".{}.nlg_sf_rod.CYLINDER_30".format(model_name))
        if not CYLINDER_30 :
            print("23")
            return
        CYLINDER_30.length = geo_len

        #---------. .nlg_sf_rod.cm
        cm = ascene.getObject(".{}.nlg_sf_rod.cm".format(model_name))
        if not cm :
            print("24")
            return
        
        cm.recompute()
        # cm.location=center_loc
        # print(center_loc)
        # cm.orientation=axis
        # loc_ori = VecUtils.global2local(nlg_sf_rod.location, nlg_sf_rod.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------. .nlg_sf_rod.MARKER_84
        MARKER_84 = ascene.getObject(".{}.nlg_sf_rod.MARKER_84".format(model_name))
        if not MARKER_84 :
            print("25")
            return
        MARKER_84.location = center_loc
        MARKER_84.orientation = VecUtils.ORI_ALONG_AXIS(hps_db_uc_atch_loc, hps_db_sf_atch_loc, "Z")
        loc_ori = VecUtils.global2local(nlg_sf_rod.location, nlg_sf_rod.orientation, MARKER_84.location, MARKER_84.orientation)
        MARKER_84.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_84.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .nlg_sf_actuator.MARKER_85
        MARKER_85 = ascene.getObject(".{}.nlg_sf_actuator.MARKER_85".format(model_name))
        if not MARKER_85 :
            print("26")
            return
        MARKER_85.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        MARKER_85.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_84))
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, MARKER_85.location, MARKER_85.orientation)
        MARKER_85.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_85.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .nlg_sf_actuator.MARKER_532
        MARKER_532 = ascene.getObject(".{}.nlg_sf_actuator.MARKER_532".format(model_name))
        if not MARKER_532 :
            print("26")
            return
        MARKER_532.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], hps_db_sf_atch))
        MARKER_532.orientation = Jusme.Vector(180,90,180)
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, MARKER_532.location, MARKER_532.orientation)
        MARKER_532.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_532.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .nlg_sf_actuator.MARKER_512
        MARKER_512 = ascene.getObject(".{}.nlg_sf_actuator.MARKER_512".format(model_name))
        if not MARKER_512 :
            print("26")
            return
        MARKER_512.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_db_sf_atch)
        MARKER_512.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, MARKER_512.location, MARKER_512.orientation)
        MARKER_512.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_512.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .nlg_sf_rod.MARKER_511
        MARKER_511 = ascene.getObject(".{}.nlg_sf_rod.MARKER_511".format(model_name))
        if not MARKER_511 :
            print("26")
            return
        MARKER_511.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_rod_bot)
        MARKER_511.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(nlg_sf_rod.location, nlg_sf_rod.orientation, MARKER_511.location, MARKER_511.orientation)
        MARKER_511.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_511.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .nlg_sf_actuator.stopper_actuator
        stopper_actuator = ascene.getObject(".{}.nlg_sf_actuator.stopper_actuator".format(model_name))
        if not stopper_actuator :
            print("26")
            return
        stopper_actuator.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_rod_bot)
        stopper_actuator.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, stopper_actuator.location, stopper_actuator.orientation)
        stopper_actuator.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        stopper_actuator.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #------. .nlg_sf_rod.MARKER_96
        MARKER_96 = ascene.getObject(".{}.nlg_sf_rod.MARKER_96".format(model_name))
        if not MARKER_96 :
            print("27")
            return
        MARKER_96.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_96.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(nlg_sf_rod.location, nlg_sf_rod.orientation, MARKER_96.location, MARKER_96.orientation)
        MARKER_96.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_96.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------. .nlg_sf_rod.MARKER_5
        MARKER_5 = ascene.getObject(".{}.nlg_sf_rod.MARKER_5".format(model_name))
        if not MARKER_5 :
            print("28")
            return
        MARKER_5.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_5.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(nlg_sf_rod.location, nlg_sf_rod.orientation, MARKER_5.location, MARKER_5.orientation)
        MARKER_5.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_5.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------. .nlg_upper_cylinder
        nlg_upper_cylinder = ascene.getObject(".{}.nlg_upper_cylinder".format(model_name))
        if not nlg_upper_cylinder :
            print("29")
            return
        #--------. .nlg_upper_cylinder.MARKER_4
        MARKER_4 = ascene.getObject(".{}.nlg_upper_cylinder.MARKER_4".format(model_name))
        if not MARKER_4 :
            print("30")
            return
        MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_5))
        MARKER_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], MARKER_5))
        loc_ori = VecUtils.global2local(nlg_upper_cylinder.location, nlg_upper_cylinder.orientation, MARKER_4.location, MARKER_4.orientation)
        MARKER_4.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_4.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])





        #--------------------------. .nlg_subframe
        nlg_subframe = ascene.getObject(".{}.nlg_subframe".format(model_name))
        if not  nlg_subframe :
            print("31")
            return

        #---------. .nlg_subframe.graout_1
        graout_1 = ascene.getObject(".{}.nlg_subframe.graout_1".format(model_name))
        if not graout_1 :
            print("32")
            return
        graout_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_sf_atch_r))
        graout_1_loc = graout_1.location

        #---------. .nlg_subframe.graout_2
        graout_2 = ascene.getObject(".{}.nlg_subframe.graout_2".format(model_name))
        if not graout_2 :
            print("33")
            return
        graout_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_sf_atch_l))
        graout_2_loc = graout_2.location
        
        #---------. .nlg_subframe.graout_3
        graout_3 = ascene.getObject(".{}.nlg_subframe.graout_3".format(model_name))
        if not graout_3 :
            print("34")
            return
        graout_3.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        graout_3_loc = graout_3.location

        nor_vec = VecUtils.ORI_IN_PLANE(graout_1_loc, graout_2_loc, graout_3_loc, "z_zx")
        graout_1.orientation = nor_vec
        graout_2.orientation = nor_vec
        graout_3.orientation = nor_vec

        nlg_subframe_center_loc = (graout_1_loc + graout_2_loc + graout_3_loc) / 3.0
        nlg_subframe.location =  nlg_subframe_center_loc
        nlg_subframe.orientation = nor_vec

        loc_ori = VecUtils.global2local( nlg_subframe.location,  nlg_subframe.orientation, graout_1.location, graout_1.orientation)
        graout_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        graout_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        loc_ori = VecUtils.global2local( nlg_subframe.location,  nlg_subframe.orientation, graout_2.location, graout_2.orientation)
        graout_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        graout_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        loc_ori = VecUtils.global2local( nlg_subframe.location,  nlg_subframe.orientation, graout_3.location, graout_3.orientation)
        graout_3.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        graout_3.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------. .nlg_subframe.cm
        cm = ascene.getObject(".{}.nlg_subframe.cm".format(model_name))
        if not cm :
            print("35")
            return
        
        cm.location =  nlg_subframe_center_loc
        cm.orientation = nor_vec
        loc_ori = VecUtils.global2local( nlg_subframe.location,  nlg_subframe.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #--------. .nlg_subframe.inertia_frame
        inertia_frame = ascene.getObject(".{}.nlg_subframe.inertia_frame".format(model_name))
        if not inertia_frame :
            print("36")
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0],  nlg_subframe))
        loc_ori = VecUtils.global2local( nlg_subframe.location,  nlg_subframe.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .nlg_subframe.MARKER_533
        MARKER_533 = ascene.getObject(".{}.nlg_subframe.MARKER_533".format(model_name))
        if not MARKER_533 :
            print("36")
            return
        MARKER_533.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        MARKER_533.orientation = Jusme.Vector(180,90,180)
        loc_ori = VecUtils.global2local( nlg_subframe.location,  nlg_subframe.orientation, MARKER_533.location, MARKER_533.orientation)
        MARKER_533.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_533.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])



        #------. .nlg_subframe.jxs_joint_j_14
        jxs_joint_j_14 = ascene.getObject(".{}.nlg_subframe.jxs_joint_j_14".format(model_name))
        if not jxs_joint_j_14 :
            print("37")
            return
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local( nlg_subframe.location,  nlg_subframe.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        
        #------. .nlg_sf_actuator.jxs_joint_i_14
        jxs_joint_i_14 = ascene.getObject(".{}.nlg_sf_actuator.jxs_joint_i_14".format(model_name))
        if not jxs_joint_i_14 :
            print("38")
            return
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_14))
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_14))
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        cm = ascene.getObject(".{}.nlg_sf_rod.cm".format(model_name))
        if not cm :
            print("26")
            return

        #--------. .nlg_sf_rod.MARKER_79
        MARKER_79 = ascene.getObject(".{}.nlg_sf_rod.MARKER_79".format(model_name))
        if not MARKER_79 :
            print("26")
            return
        MARKER_79.location = VecUtils.LOC_RELATIVE_TO([0,0,0],cm)
        MARKER_79.orientation = Jusme.Vector(270,120,180)
        loc_ori = VecUtils.global2local(nlg_sf_rod.location, nlg_sf_rod.orientation, MARKER_79.location, MARKER_79.orientation)
        MARKER_79.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_79.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------. .nlg_sf_rod.MARKER_80
        MARKER_80 = ascene.getObject(".{}.nlg_sf_rod.MARKER_80".format(model_name))
        if not MARKER_80 :
            print("26")
            return
        MARKER_80.location = VecUtils.LOC_RELATIVE_TO([0,0,0],cm)
        MARKER_80.orientation = Jusme.Vector(270,120,180)
        loc_ori = VecUtils.global2local(nlg_sf_rod.location, nlg_sf_rod.orientation, MARKER_80.location, MARKER_80.orientation)
        MARKER_80.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_80.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])






        #------------------. .ground.cfs_uc_sf_atch_mid
        #---------目前从Adams模型中没有定义拓扑关联
        #--------位置默认按hps_uc_sf_atch_r和hps_uc_sf_atch_l的中点处理
        #--------方向按 nlg_subframe物体的方向处理
        cfs_uc_sf_atch_mid = ascene.getObject(".{}.ground.cfs_uc_sf_atch_mid".format(model_name))
        if not cfs_uc_sf_atch_mid :
            print("39")
            return
        cfs_uc_sf_atch_mid.location = 0.5 * (hps_uc_sf_atch_r_loc + hps_uc_sf_atch_l_loc)
        cfs_uc_sf_atch_mid.orientation = nor_vec


        

        #---------. .ground.cfs_subframe_to_body_point
        cfs_subframe_to_body_point = ascene.getObject(".{}.ground.cfs_subframe_to_body_point".format(model_name))
        if not cfs_subframe_to_body_point :
            print("43")
            return
        cfs_subframe_to_body_point.location =  nlg_subframe_center_loc
        cfs_subframe_to_body_point.orientation = nor_vec

        #-------------. .mts_body_mount
        mts_body_mount = ascene.getObject(".{}.mts_body_mount".format(model_name))
        if not mts_body_mount :
            print("44")
            return
        mts_body_mount.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfs_subframe_to_body_point))
        mts_body_mount.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))

        #----------. .ground.mts_mount_j_2
        mts_mount_j_2 = ascene.getObject(".{}.ground.mts_mount_j_2".format(model_name))
        if not mts_mount_j_2 :
            print("45")
            return
        mts_mount_j_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], mts_body_mount))
        mts_mount_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], mts_body_mount))

        #---------. .mts_body_mount.mount_i
        mount_i = ascene.getObject(".{}.mts_body_mount.mount_i".format(model_name))
        if not mount_i :
            print("46")
            return
        mount_i.location =  nlg_subframe_center_loc
        mount_i.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(mts_body_mount.location, mts_body_mount.orientation, mount_i.location, mount_i.orientation)
        mount_i.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        mount_i.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------. .mts_body_mount.jxs_joint_j_16
        jxs_joint_j_16 = ascene.getObject(".{}.mts_body_mount.jxs_joint_j_16".format(model_name))
        if not jxs_joint_j_16 :
            print("47")
            return
        jxs_joint_j_16.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfs_subframe_to_body_point))
        jxs_joint_j_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        loc_ori = VecUtils.global2local(mts_body_mount.location, mts_body_mount.orientation, jxs_joint_j_16.location, jxs_joint_j_16.orientation)
        jxs_joint_j_16.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_16.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------. .nlg_subframe.jxs_joint_i_16
        jxs_joint_i_16 = ascene.getObject(".{}.nlg_subframe.jxs_joint_i_16".format(model_name))
        if not jxs_joint_i_16 :
            print("48")
            return
        jxs_joint_i_16.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_16))
        jxs_joint_i_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_16))
        loc_ori = VecUtils.global2local( nlg_subframe.location,  nlg_subframe.orientation, jxs_joint_i_16.location, jxs_joint_i_16.orientation)
        jxs_joint_i_16.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_16.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_nlg_post_2hubs.nlg_sf_actuator.MARKER_89
        MARKER_89 = ascene.getObject(".{}.nlg_sf_actuator.MARKER_89".format(model_name))
        if not MARKER_89 :
            return
        MARKER_89.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], hps_rod_bot))
        MARKER_89.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, MARKER_89.location, MARKER_89.orientation)
        MARKER_89.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_89.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------._AA_nlg_post_2hubs.nlg_sf_actuator.MARKER_100
        MARKER_100 = ascene.getObject(".{}.nlg_sf_actuator.MARKER_100".format(model_name))
        if not MARKER_100 :
            return
        MARKER_100.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], hps_rod_bot))
        MARKER_100.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(nlg_sf_actuator.location, nlg_sf_actuator.orientation, MARKER_100.location, MARKER_100.orientation)
        MARKER_100.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_100.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------. .joscyl_db_sf
        joscyl_db_sf = ascene.getObject(".{}.joscyl_db_sf".format(model_name))
        if not joscyl_db_sf :
            print("49")
            return
        joscyl_db_sf.recompute()

        # #---------. .JOINT_13
        # JOINT_13 = ascene.getObject(".{}.JOINT_13".format(model_name))
        # if not JOINT_13 :
        #     print("50")
        #     return
        # JOINT_13.recompute()

        # #---------. .JOINT_1
        # JOINT_1 = ascene.getObject(".{}.JOINT_1".format(model_name))
        # if not JOINT_1 :
        #     print("51")
        #     return
        # JOINT_1.recompute()

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

        # #------. .MOTION_disp
        # MOTION_disp = ascene.getObject(".{}.MOTION_disp".format(model_name))
        # if not MOTION_disp :
        #     print("54")
        #     return
        # MOTION_disp.recompute()

        #------. .NLG_disp_sf
        NLG_disp_sf = ascene.getObject(".{}.NLG_disp_sf".format(model_name))
        if not NLG_disp_sf :
            print("55")
            return
        NLG_disp_sf.recompute()

        # #--------. .NLG_vel
        # NLG_vel = ascene.getObject(".{}.NLG_vel".format(model_name))
        # if not NLG_vel :
        #     print("56")
        #     return
        # NLG_vel.recompute()

        joscly_ac_rd= ascene.getObject(".{}.joscly_ac_rd".format(model_name))
        if not joscly_ac_rd :
            print("55")
            return
        joscly_ac_rd.recompute()

        NLG_stopper_low= ascene.getObject(".{}.NLG_stopper_low".format(model_name))
        if not NLG_stopper_low :
            print("55")
            return
        NLG_stopper_low.recompute()

        nlg_ZDT_FORCE= ascene.getObject(".{}.nlg_ZDT_FORCE".format(model_name))
        if not nlg_ZDT_FORCE :
            print("55")
            return
        nlg_ZDT_FORCE.recompute()

        jossph_rd_uc= ascene.getObject(".{}.jossph_rd_uc".format(model_name))
        if not jossph_rd_uc :
            print("55")
            return
        jossph_rd_uc.recompute()

        cm = ascene.getObject(".{}.nlg_sf_rod.cm".format(model_name))
        if not cm :
            print("26")
            return
        cm.recompute()

        print('完成调整hps_db_sf_atch')

        pass
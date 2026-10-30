import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class MotionHprUpractSfAtch1Adjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始收放仿真hpr_upract_sf_atch_1硬点调整")

        ascene = Jusme.ActiveUSScene
        #--------------得到模型名称
        model_name = Common.getModelName()

        #------------------------._AA_nlg_post_2hubs.ground.origo1
        origo1 = ascene.getObject(".{}.ground.origo1".format(model_name))
        if not origo1 :
            return

        #-------------得到当前硬点特征对象._AA_nlg_post_2hubs.ground.hpr_upract_sf_atch_1
        hpr_upract_sf_atch_1 = ascene.getObject(self.hps_full_name)
        if not hpr_upract_sf_atch_1 :
            return
        hpr_upract_sf_atch_1_loc = hpr_upract_sf_atch_1.location

        #-------._AA_nlg_post_2hubs.ground.hpr_lwract_uc_atch_1
        hpr_lwract_uc_atch_1 = ascene.getObject(".{}.ground.hpr_lwract_uc_atch_1".format(model_name))
        if not hpr_lwract_uc_atch_1 :
            return
        hpr_lwract_uc_atch_1_loc = hpr_lwract_uc_atch_1.location

        #-----------------------------------------------------对右主起进行参数化调整
        #----------------------._AA_nlg_post_2hubs.ground.cfr_lwract_top
        cfr_lwract_top = ascene.getObject(".{}.ground.cfr_lwract_top".format(model_name))
        if not cfr_lwract_top :
            return
        cfr_lwract_top_loc = cfr_lwract_top.location

        geo_len = VecUtils.DM(hpr_lwract_uc_atch_1_loc, hpr_upract_sf_atch_1_loc)
        cfr_lwract_top.location = VecUtils.LOC_ALONG_LINE(hpr_lwract_uc_atch_1_loc, hpr_upract_sf_atch_1_loc, 0.92 * geo_len)
        cfr_lwract_top_loc = cfr_lwract_top.location
        cfr_lwract_top.orientation = VecUtils.ORI_ALONG_AXIS(hpr_lwract_uc_atch_1_loc, hpr_upract_sf_atch_1_loc, "z")
        
        #---------------------------------------对右主起收放作动筒内活塞杆进行参数化调整
        geo_len = VecUtils.DM(hpr_lwract_uc_atch_1_loc, cfr_lwract_top_loc)
        axis = VecUtils.ORI_ALONG_AXIS(hpr_lwract_uc_atch_1_loc, cfr_lwract_top_loc, "z")
        center_loc = 0.5 * (hpr_lwract_uc_atch_1_loc + cfr_lwract_top_loc)

        #-----------------------._AA_nlg_post_2hubs.ger_lwract
        ger_lwract = ascene.getObject(".{}.ger_lwract".format(model_name))
        if not ger_lwract :
            return
        ger_lwract.location = center_loc
        ger_lwract.orientation = axis

        #-------------------._AA_nlg_post_2hubs.ger_lwract.gralin_10
        gralin_10 = ascene.getObject(".{}.ger_lwract.gralin_10".format(model_name))
        if not gralin_10 :
            return
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_lwract_uc_atch_1))
        gralin_10.orientation = VecUtils.ORI_ALONG_AXIS(hpr_lwract_uc_atch_1_loc, cfr_lwract_top_loc, "z")
        loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_lwract.gralin_lwract
        gralin_lwract = ascene.getObject(".{}.ger_lwract.gralin_lwract".format(model_name))
        if not gralin_lwract :
            return
        gralin_lwract.length = geo_len

        #----------------._AA_nlg_post_2hubs.ger_lwract.cm
        cm = ascene.getObject(".{}.ger_lwract.cm".format(model_name))
        if not cm :
            return
        cm.recompute()
        # cm.location = center_loc
        # cm.orientation = axis
        # loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_lwract.inertia_frame
        inertia_frame = ascene.getObject(".{}.ger_lwract.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ger_lwract))
        loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #----------------._AA_nlg_post_2hubs.ger_lwract.jxr_joint_j_7
        jxr_joint_j_7 = ascene.getObject(".{}.ger_lwract.jxr_joint_j_7".format(model_name))
        if not jxr_joint_j_7 :
            return
        jxr_joint_j_7.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_lwract_uc_atch_1))
        jxr_joint_j_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo1))
        loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, jxr_joint_j_7.location, jxr_joint_j_7.orientation)
        jxr_joint_j_7.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_j_7.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------._AA_nlg_post_2hubs.ger_upper_cylinder
        ger_upper_cylinder = ascene.getObject(".{}.ger_upper_cylinder".format(model_name))
        if not ger_upper_cylinder :
            return
        #---------------._AA_nlg_post_2hubs.ger_upper_cylinder.jxr_joint_i_7
        jxr_joint_i_7 = ascene.getObject(".{}.ger_upper_cylinder.jxr_joint_i_7".format(model_name))
        if not jxr_joint_i_7 :
            return
        jxr_joint_i_7.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxr_joint_j_7))
        jxr_joint_i_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxr_joint_j_7))
        loc_ori = VecUtils.global2local(ger_upper_cylinder.location, ger_upper_cylinder.orientation, jxr_joint_i_7.location, jxr_joint_i_7.orientation)
        jxr_joint_i_7.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_i_7.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_upract
        ger_upract = ascene.getObject(".{}.ger_upract".format(model_name))
        if not ger_upract :
            return
        #----------------._AA_nlg_post_2hubs.ger_upract.jxr_joint_j_8
        jxr_joint_j_8 = ascene.getObject(".{}.ger_upract.jxr_joint_j_8".format(model_name))
        if not jxr_joint_j_8 :
            return
        
        jxr_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfr_lwract_top))
        jxr_joint_j_8.orientation = VecUtils.ORI_ALONG_AXIS(hpr_lwract_uc_atch_1_loc, hpr_upract_sf_atch_1_loc, "Z")
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, jxr_joint_j_8.location, jxr_joint_j_8.orientation)
        jxr_joint_j_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_j_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_lwract.jxr_joint_i_8
        jxr_joint_i_8 = ascene.getObject(".{}.ger_lwract.jxr_joint_i_8".format(model_name))
        if not jxr_joint_i_8 :
            return
        jxr_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxr_joint_j_8))
        jxr_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxr_joint_j_8))
        loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, jxr_joint_i_8.location, jxr_joint_i_8.orientation)
        jxr_joint_i_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_i_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_lwract.MARKER_239
        #----MARKER_239无参照关系
        #----目测与硬点hpr_lwract_uc_atch_1一致
        #----按照默认关系变成
        MARKER_239 = ascene.getObject(".{}.ger_lwract.MARKER_239".format(model_name))
        if not MARKER_239 :
            return
        MARKER_239.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_lwract_uc_atch_1))
        MARKER_239.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, MARKER_239.location, MARKER_239.orientation)
        MARKER_239.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_239.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_upract
        ger_upract = ascene.getObject(".{}.ger_upract".format(model_name))
        if not ger_upract :
            return

        #---------------._AA_nlg_post_2hubs.ground.cfr_upract_bot
        cfr_upract_bot = ascene.getObject(".{}.ground.cfr_upract_bot".format(model_name))
        if not cfr_upract_bot :
            return
        cfr_upract_bot_loc = cfr_upract_bot.location
        geo_len = VecUtils.DM(hpr_lwract_uc_atch_1_loc, hpr_upract_sf_atch_1_loc)
        axis = VecUtils.ORI_ALONG_AXIS(hpr_lwract_uc_atch_1_loc, hpr_upract_sf_atch_1_loc, "z")
        cfr_upract_bot.location = VecUtils.LOC_ALONG_LINE(hpr_lwract_uc_atch_1_loc, hpr_upract_sf_atch_1_loc, 0.4 * geo_len)
        cfr_upract_bot_loc = cfr_upract_bot.location

        #---------------------------对._AA_nlg_post_2hubs.ger_upract进行参数化调整
        geo_len = VecUtils.DM(cfr_upract_bot_loc, hpr_upract_sf_atch_1_loc)
        axis = VecUtils.ORI_ALONG_AXIS(cfr_upract_bot_loc, hpr_upract_sf_atch_1_loc, "Z")
        center_loc = 0.5 * (cfr_upract_bot_loc + hpr_upract_sf_atch_1_loc)
        ger_upract.location = center_loc
        ger_upract.orientation = axis

        #-------------------------._AA_nlg_post_2hubs.ger_upract.gralin_19
        gralin_19 = ascene.getObject(".{}.ger_upract.gralin_19".format(model_name))
        if not gralin_19 :
            return
        gralin_19.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfr_upract_bot))
        gralin_19.orientation = axis
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, gralin_19.location, gralin_19.orientation)
        gralin_19.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_19.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------._AA_nlg_post_2hubs.ger_upract.gralin_upract
        gralin_upract = ascene.getObject(".{}.ger_upract.gralin_upract".format(model_name))
        if not gralin_upract :
            return
        gralin_upract.length = geo_len

        #--------------------._AA_nlg_post_2hubs.ger_upract.cm
        cm = ascene.getObject(".{}.ger_upract.cm".format(model_name))
        if not cm :
            return
        cm.recompute()
        
        # cm.location = center_loc
        # cm.orientation = axis
        # loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------._AA_nlg_post_2hubs.ger_upract.inertia_frame
        inertia_frame = ascene.getObject(".{}.ger_upract.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ger_upract))
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_upract.jxr_joint_j_8
        jxr_joint_j_8 = ascene.getObject(".{}.ger_upract.jxr_joint_j_8".format(model_name))
        if not jxr_joint_j_8 :
            return
        jxr_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfr_lwract_top))
        jxr_joint_j_8.orientation = VecUtils.ORI_ALONG_AXIS(hpr_lwract_uc_atch_1_loc, hpr_upract_sf_atch_1_loc, "Z")
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, jxr_joint_j_8.location, jxr_joint_j_8.orientation)
        jxr_joint_j_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_j_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_lwract
        ger_lwract = ascene.getObject(".{}.ger_lwract".format(model_name))
        if not ger_lwract :
            return
        
        #----------------._AA_nlg_post_2hubs.ger_lwract.jxr_joint_i_8
        jxr_joint_i_8 = ascene.getObject(".{}.ger_lwract.jxr_joint_i_8".format(model_name))
        if not jxr_joint_i_8 :
            return
        jxr_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxr_joint_j_8))
        jxr_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxr_joint_j_8))
        loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, jxr_joint_i_8.location, jxr_joint_i_8.orientation)
        jxr_joint_i_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_i_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #-----------._AA_nlg_post_2hubs.ges_subframe_2
        ges_subframe_2 = ascene.getObject(".{}.ges_subframe_2".format(model_name))
        if not ges_subframe_2 :
            return
        #-----------._AA_nlg_post_2hubs.ges_subframe_2.jxr_joint_j_17
        jxr_joint_j_17 = ascene.getObject(".{}.ges_subframe_2.jxr_joint_j_17".format(model_name))
        if not jxr_joint_j_17 :
            return
        jxr_joint_j_17.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_upract_sf_atch_1))
        jxr_joint_j_17.orientation = (VecUtils.ORI_RELATIVE_TO([0, 0, 0], origo1))
        loc_ori = VecUtils.global2local(ges_subframe_2.location, ges_subframe_2.orientation, jxr_joint_j_17.location, jxr_joint_j_17.orientation)
        jxr_joint_j_17.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_j_17.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------------------._AA_nlg_post_2hubs.ger_upract.jxr_joint_i_17
        jxr_joint_i_17 = ascene.getObject(".{}.ger_upract.jxr_joint_i_17".format(model_name))
        if not jxr_joint_i_17 :
            return
        jxr_joint_i_17.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxr_joint_j_17))
        jxr_joint_i_17.orientation = (VecUtils.ORI_RELATIVE_TO([0, 0, 0], jxr_joint_j_17))
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, jxr_joint_i_17.location, jxr_joint_i_17.orientation)
        jxr_joint_i_17.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_i_17.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------._AA_nlg_post_2hubs.ger_upract.MARKER_240
        MARKER_240 = ascene.getObject(".{}.ger_upract.MARKER_240".format(model_name))
        if not MARKER_240 :
            return
        #---------MARKER_240无参照建模
        #---------目测数据与hpr_upract_sf_atch_1一致
        #--------按此默认编程
        MARKER_240.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_upract_sf_atch_1))
        MARKER_240.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, MARKER_240.location, MARKER_240.orientation)
        MARKER_240.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_240.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------._AA_nlg_post_2hubs.ger_upract.MARKER_238
        MARKER_238 = ascene.getObject(".{}.ger_upract.MARKER_238".format(model_name))
        if not MARKER_238 :
            return
        MARKER_238.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_upract_sf_atch_1))
        MARKER_238.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, MARKER_238.location, MARKER_238.orientation)
        MARKER_238.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_238.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #------------------._AA_nlg_post_2hubs.ger_upract.uer_actuator_j_2
        uer_actuator_j_2 = ascene.getObject(".{}.ger_upract.uer_actuator_j_2".format(model_name))
        if not uer_actuator_j_2 :
            return
        uer_actuator_j_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxr_joint_j_8))
        uer_actuator_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0, 0, 0], jxr_joint_j_8))
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, uer_actuator_j_2.location, uer_actuator_j_2.orientation)
        uer_actuator_j_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uer_actuator_j_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------._AA_nlg_post_2hubs.ger_upract.uer_stopper_j_2
        uer_stopper_j_2 = ascene.getObject(".{}.ger_upract.uer_stopper_j_2".format(model_name))
        if not uer_stopper_j_2 :
            return
        uer_stopper_j_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_upract_sf_atch_1))
        uer_stopper_j_2.orientation = Jusme.Vector(357.5221912295, 7.7973026777, 2.5009025911)
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, uer_stopper_j_2.location, uer_stopper_j_2.orientation)
        uer_stopper_j_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uer_stopper_j_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------._AA_nlg_post_2hubs.ger_upract.uer_actuator_i_1
        uer_actuator_i_1 = ascene.getObject(".{}.ger_upract.uer_actuator_i_1".format(model_name))
        if not uer_actuator_i_1 :
            return
        uer_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_upract_sf_atch_1))
        uer_actuator_i_1.orientation = Jusme.Vector(357.5221912295, 7.7973026777, 2.5009025911)
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, uer_actuator_i_1.location, uer_actuator_i_1.orientation)
        uer_actuator_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uer_actuator_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_lwract.uer_actuator_j_1
        uer_actuator_j_1 = ascene.getObject(".{}.ger_lwract.uer_actuator_j_1".format(model_name))
        if not uer_actuator_j_1 :
            return
        uer_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_lwract_uc_atch_1))
        uer_actuator_j_1.orientation = Jusme.Vector(357.5221912295, 7.7973026777, 2.5009025911)
        loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, uer_actuator_j_1.location, uer_actuator_j_1.orientation)
        uer_actuator_j_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uer_actuator_j_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_lwract.uer_actuator_i_2
        uer_actuator_i_2 = ascene.getObject(".{}.ger_lwract.uer_actuator_i_2".format(model_name))
        if not uer_actuator_i_2 :
            return
        uer_actuator_i_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxr_joint_i_8))
        uer_actuator_i_2.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxr_joint_i_8)
        loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, uer_actuator_i_2.location, uer_actuator_i_2.orientation)
        uer_actuator_i_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uer_actuator_i_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------._AA_nlg_post_2hubs.ger_lwract.uer_stopper_i_2
        uer_stopper_i_2 = ascene.getObject(".{}.ger_lwract.uer_stopper_i_2".format(model_name))
        if not uer_stopper_i_2 :
            return
        uer_stopper_i_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_lwract_uc_atch_1))
        uer_stopper_i_2.orientation = Jusme.Vector(357.5221912295, 7.7973026777, 2.5009025911)
        loc_ori = VecUtils.global2local(ger_lwract.location, ger_lwract.orientation, uer_stopper_i_2.location, uer_stopper_i_2.orientation)
        uer_stopper_i_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uer_stopper_i_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------------------更新右主起中所有运动副
        #----------._AA_nlg_post_2hubs.jorsph_uc_lwract
        jorsph_uc_lwract = ascene.getObject(".{}.jorsph_uc_lwract".format(model_name))
        if not jorsph_uc_lwract :
            return
        jorsph_uc_lwract.recompute()

        #----------._AA_nlg_post_2hubs.jorsph_upract_sf
        jorsph_upract_sf = ascene.getObject(".{}.jorsph_upract_sf".format(model_name))
        if not jorsph_upract_sf :
            return
        jorsph_upract_sf.recompute()

        #---------._AA_nlg_post_2hubs.sf_right
        sf_right = ascene.getObject(".{}.sf_right".format(model_name))
        if not sf_right :
            return
        sf_right.recompute()

        #---------._AA_nlg_post_2hubs.MOTION_RIGHT
        MOTION_RIGHT = ascene.getObject(".{}.MOTION_RIGHT".format(model_name))
        if not MOTION_RIGHT :
            return
        MOTION_RIGHT.recompute()

        # #---------._AA_nlg_post_2hubs.vel_right
        # vel_right = ascene.getObject(".{}.vel_right".format(model_name))
        # if not vel_right :
        #     return
        # vel_right.recompute()

        #---------._AA_nlg_post_2hubs.disp_sf_right
        disp_sf_right = ascene.getObject(".{}.disp_sf_right".format(model_name))
        if not disp_sf_right :
            return
        disp_sf_right.recompute()


        #-----------------------------------------------------对左主起进行参数化调整
        #--------------------得到当前点的对象及坐标
        hpl_upract_sf_atch_1 = ascene.getObject(".{}.ground.hpl_upract_sf_atch_1".format(model_name))
        if not hpl_upract_sf_atch_1 :
            return
        hpl_upract_sf_atch_1_loc = hpl_upract_sf_atch_1.location

        hpl_upract_sf_atch_1.location.x = hpr_upract_sf_atch_1_loc.x
        hpl_upract_sf_atch_1.location.y = -1 * hpr_upract_sf_atch_1_loc.y
        hpl_upract_sf_atch_1.location.z = hpr_upract_sf_atch_1_loc.z
        hpl_upract_sf_atch_1_loc = hpl_upract_sf_atch_1.location

        #-----------------._AA_nlg_post_2hubs.ground.hpl_lwract_uc_atch_1
        hpl_lwract_uc_atch_1 = ascene.getObject(".{}.ground.hpl_lwract_uc_atch_1".format(model_name))
        if not hpl_lwract_uc_atch_1 :
            return
        hpl_lwract_uc_atch_1_loc = hpl_lwract_uc_atch_1.location

        #------------------------._AA_nlg_post_2hubs.ground.cfl_lwract_top
        cfl_lwract_top = ascene.getObject(".{}.ground.cfl_lwract_top".format(model_name))
        if not cfl_lwract_top :
            return
        #------------------计算左主起收放作动筒两个硬点的距离
        geo_len = VecUtils.DM(hpl_lwract_uc_atch_1_loc, hpl_upract_sf_atch_1_loc)
        #------------------计算左主起收放作动筒两个硬点的方向
        cfl_lwract_top.orientation = VecUtils.ORI_ALONG_AXIS(hpl_lwract_uc_atch_1_loc, hpl_upract_sf_atch_1_loc, 'z')
        #------------------计算左主起收放作动筒内撑杆顶部的位置
        cfl_lwract_top.location = VecUtils.LOC_ALONG_LINE(hpl_lwract_uc_atch_1_loc, hpl_upract_sf_atch_1_loc, 0.92 * geo_len)
        cfl_lwract_top_loc = cfl_lwract_top.location



















        #-----------------------------------------------------------------------针对左主起落架的调整
        #------------------------------------
        #------------------------------------
        #------------------------------------
        #------------------------------------
        #-----------------------计算._AA_nlg_post_2hubs.gel_lwract的全局位置和方向
        axis = VecUtils.ORI_ALONG_AXIS(hpl_lwract_uc_atch_1_loc, cfl_lwract_top_loc, 'z')
        geo_len = VecUtils.DM(hpl_lwract_uc_atch_1_loc, cfl_lwract_top_loc)
        center_loc = 0.5 * (hpl_lwract_uc_atch_1_loc + cfl_lwract_top_loc)

        #--------------------._AA_nlg_post_2hubs.gel_lwract
        gel_lwract = ascene.getObject(".{}.gel_lwract".format(model_name))
        if not gel_lwract :
            return
        gel_lwract.location = center_loc
        gel_lwract.orientation = axis

        #--------------------._AA_nlg_post_2hubs.gel_lwract.gralin_9
        gralin_9 = ascene.getObject(".{}.gel_lwract.gralin_9".format(model_name))
        if not gralin_9 :
            return
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_lwract_uc_atch_1)) 
        gralin_9.orientation = axis
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------._AA_nlg_post_2hubs.gel_lwract.gralin_lwract(更新几何体的长度)
        gralin_lwract = ascene.getObject(".{}.gel_lwract.gralin_lwract".format(model_name))
        if not gralin_lwract :
            return
        gralin_lwract.length = geo_len

        #-----------------._AA_nlg_post_2hubs.gel_lwract.cm
        cm = ascene.getObject(".{}.gel_lwract.cm".format(model_name))
        if not cm :
            return
        cm.recompute()
        
        # cm.location = center_loc
        # cm.orientation = axis
        # loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------._AA_nlg_post_2hubs.gel_lwract.inertia_frame
        inertia_frame = ascene.getObject(".{}.gel_lwract.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm)) 
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], gel_lwract))
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #---------------------------._AA_nlg_post_2hubs.gel_lwract.MARKER_235
        MARKER_235 = ascene.getObject(".{}.gel_lwract.MARKER_235".format(model_name))
        if not MARKER_235 :
            return
        #---------------MARKER_235在Adams里没有关联参照
        # 根据数据与硬点hpl_lwract_uc_atch_1坐标一致
        # 默认按硬点hpl_lwract_uc_atch_1编程
        MARKER_235.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_lwract_uc_atch_1)) 
        MARKER_235.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, MARKER_235.location, MARKER_235.orientation)
        MARKER_235.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_235.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------------._AA_nlg_post_2hubs.gel_lwract.MARKER_233
        MARKER_233 = ascene.getObject(".{}.gel_lwract.MARKER_233".format(model_name))
        if not MARKER_233 :
            return
        MARKER_233.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_lwract_uc_atch_1)) 
        MARKER_233.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, MARKER_233.location, MARKER_233.orientation)
        MARKER_233.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_233.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #-------------------------------._AA_nlg_post_2hubs.gel_lwract.jxl_joint_j_7
        jxl_joint_j_7 = ascene.getObject(".{}.gel_lwract.jxl_joint_j_7".format(model_name))
        if not jxl_joint_j_7 :
            return
        jxl_joint_j_7.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_lwract_uc_atch_1)) 
        jxl_joint_j_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo1))
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, jxl_joint_j_7.location, jxl_joint_j_7.orientation)
        jxl_joint_j_7.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_j_7.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------------------------._AA_nlg_post_2hubs.gel_upper_cylinder
        gel_upper_cylinder = ascene.getObject(".{}.gel_upper_cylinder".format(model_name))
        if not gel_upper_cylinder :
            return
        #--------------------------------._AA_nlg_post_2hubs.gel_upper_cylinder.jxl_joint_i_7
        jxl_joint_i_7 = ascene.getObject(".{}.gel_upper_cylinder.jxl_joint_i_7".format(model_name))
        if not jxl_joint_i_7 :
            return
        jxl_joint_i_7.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxl_joint_j_7)) 
        jxl_joint_i_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxl_joint_j_7))
        loc_ori = VecUtils.global2local(gel_upper_cylinder.location, gel_upper_cylinder.orientation, jxl_joint_i_7.location, jxl_joint_i_7.orientation)
        jxl_joint_i_7.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_i_7.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------------------._AA_nlg_post_2hubs.gel_upract
        gel_upract = ascene.getObject(".{}.gel_upract".format(model_name))
        if not gel_upract :
            return
        #----------------------._AA_nlg_post_2hubs.gel_upract.jxl_joint_j_8
        jxl_joint_j_8 = ascene.getObject(".{}.gel_upract.jxl_joint_j_8".format(model_name))
        if not jxl_joint_j_8 :
            return
        jxl_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfl_lwract_top)) 
        jxl_joint_j_8.orientation = VecUtils.ORI_ALONG_AXIS(hpl_lwract_uc_atch_1_loc, hpl_upract_sf_atch_1_loc, "z")
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, jxl_joint_j_8.location, jxl_joint_j_8.orientation)
        jxl_joint_j_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_j_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------------._AA_nlg_post_2hubs.gel_lwract.jxl_joint_i_8
        jxl_joint_i_8 = ascene.getObject(".{}.gel_lwract.jxl_joint_i_8".format(model_name))
        if not jxl_joint_i_8 :
            return
        jxl_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxl_joint_j_8)) 
        jxl_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxl_joint_j_8))
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, jxl_joint_i_8.location, jxl_joint_i_8.orientation)
        jxl_joint_i_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_i_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #**************************************
        #--------------------------更新左起落架收放外筒底部的Mark点cfl_upract_bot
        #----------------------._AA_nlg_post_2hubs.ground.cfl_upract_bot
        #---------------------计算Marker点cfl_upract_bot的位置和方向
        cfl_upract_bot = ascene.getObject(".{}.ground.cfl_upract_bot".format(model_name))
        if not cfl_upract_bot :
            return
        cfl_upract_bot_loc = cfl_upract_bot.location

        geo_len = VecUtils.DM(hpl_lwract_uc_atch_1_loc, hpl_upract_sf_atch_1_loc)
        cfl_upract_bot.location = VecUtils.LOC_ALONG_LINE(hpl_lwract_uc_atch_1_loc, hpl_upract_sf_atch_1_loc, 0.4 * geo_len)
        cfl_upract_bot_loc = cfl_upract_bot.location
        axis = VecUtils.ORI_ALONG_AXIS(hpl_lwract_uc_atch_1_loc, hpl_upract_sf_atch_1_loc, "z")
        cfl_upract_bot.orientation = axis

        center_loc = 0.5 * (cfl_upract_bot_loc + hpl_upract_sf_atch_1_loc)
        axis = VecUtils.ORI_ALONG_AXIS(cfl_upract_bot_loc, hpl_upract_sf_atch_1_loc, "z")
        geo_len = VecUtils.DM(cfl_upract_bot_loc, hpl_upract_sf_atch_1_loc)

        #-----------------------._AA_nlg_post_2hubs.gel_upract
        gel_upract = ascene.getObject(".{}.gel_upract".format(model_name))
        if not gel_upract :
            return
        gel_upract.location = center_loc
        gel_upract.orientation = axis
        
        #----------------------._AA_nlg_post_2hubs.gel_upract.gralin_18
        gralin_18 = ascene.getObject(".{}.gel_upract.gralin_18".format(model_name))
        if not gralin_18 :
            return
        gralin_18.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfl_upract_bot)) 
        gralin_18.orientation = axis
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, gralin_18.location, gralin_18.orientation)
        gralin_18.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_18.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------------------------._AA_nlg_post_2hubs.gel_upract.gralin_upract
        gralin_upract = ascene.getObject(".{}.gel_upract.gralin_upract".format(model_name))
        if not gralin_upract :
            return
        gralin_upract.length = geo_len

        #----------------------._AA_nlg_post_2hubs.gel_upract.cm
        cm = ascene.getObject(".{}.gel_upract.cm".format(model_name))
        if not cm :
            return
        cm.recompute()
        
        # cm.location = center_loc
        # cm.location = axis
        # loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------------------._AA_nlg_post_2hubs.gel_upract.inertia_frame
        inertia_frame = ascene.getObject(".{}.gel_upract.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm)) 
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], gel_upract))
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------._AA_nlg_post_2hubs.gel_upract.jxl_joint_j_8
        jxl_joint_j_8 = ascene.getObject(".{}.gel_upract.jxl_joint_j_8".format(model_name))
        if not jxl_joint_j_8 :
            return
        jxl_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfl_lwract_top)) 
        jxl_joint_j_8.orientation = VecUtils.ORI_ALONG_AXIS(hpl_lwract_uc_atch_1_loc, hpl_upract_sf_atch_1_loc, "z")
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, jxl_joint_j_8.location, jxl_joint_j_8.orientation)
        jxl_joint_j_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_j_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------------._AA_nlg_post_2hubs.gel_lwract.jxl_joint_i_8
        jxl_joint_i_8 = ascene.getObject(".{}.gel_lwract.jxl_joint_i_8".format(model_name))
        if not jxl_joint_i_8 :
            return
        jxl_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxl_joint_j_8)) 
        jxl_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxl_joint_j_8))
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, jxl_joint_i_8.location, jxl_joint_i_8.orientation)
        jxl_joint_i_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_i_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------------------._AA_nlg_post_2hubs.gel_upract.MARKER_236
        MARKER_236 = ascene.getObject(".{}.gel_upract.MARKER_236".format(model_name))
        if not MARKER_236 :
            return
        #---------------MARKER_236在Adams里没有关联参照，根据数据与硬点hpl_upract_sf_atch_1坐标一致，给与编程  与MARKER_235定义了测量._AA_nlg_post_2hubs.disp_sf_left 
        MARKER_236.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_upract_sf_atch_1)) 
        MARKER_236.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, MARKER_236.location, MARKER_236.orientation)
        MARKER_236.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_236.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------------------._AA_nlg_post_2hubs.gel_upract.MARKER_234
        MARKER_234 = ascene.getObject(".{}.gel_upract.MARKER_234".format(model_name))
        if not MARKER_234 :
            return
        MARKER_234.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_upract_sf_atch_1)) 
        MARKER_234.orientation = Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, MARKER_234.location, MARKER_234.orientation)
        MARKER_234.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_234.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------------._AA_nlg_post_2hubs.ges_subframe_2
        ges_subframe_2 = ascene.getObject(".{}.ges_subframe_2".format(model_name))
        if not ges_subframe_2 :
            return

        #----------------------------._AA_nlg_post_2hubs.ges_subframe_2.jxl_joint_j_17
        jxl_joint_j_17 = ascene.getObject(".{}.ges_subframe_2.jxl_joint_j_17".format(model_name))
        if not jxl_joint_j_17 :
            return
        jxl_joint_j_17.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_upract_sf_atch_1))
        jxl_joint_j_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo1))
        loc_ori = VecUtils.global2local(ges_subframe_2.location, ges_subframe_2.orientation, jxl_joint_j_17.location, jxl_joint_j_17.orientation)
        jxl_joint_j_17.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_j_17.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------------._AA_nlg_post_2hubs.gel_upract.jxl_joint_i_17
        jxl_joint_i_17 = ascene.getObject(".{}.gel_upract.jxl_joint_i_17".format(model_name))
        if not jxl_joint_i_17 :
            return
        jxl_joint_i_17.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxl_joint_j_17))
        jxl_joint_i_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxl_joint_j_17))
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, jxl_joint_i_17.location, jxl_joint_i_17.orientation)
        jxl_joint_i_17.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_i_17.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------------..gel_upract.uel_actuator_j_2
        uel_actuator_j_2 = ascene.getObject(".{}.gel_upract.uel_actuator_j_2".format(model_name))
        if not uel_actuator_j_2 :
            return
        uel_actuator_j_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxl_joint_j_8))
        uel_actuator_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxl_joint_j_8))
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, uel_actuator_j_2.location, uel_actuator_j_2.orientation)
        uel_actuator_j_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uel_actuator_j_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------------..gel_upract.uel_actuator_i_1
        uel_actuator_i_1 = ascene.getObject(".{}.gel_upract.uel_actuator_i_1".format(model_name))
        if not uel_actuator_i_1 :
            return
        uel_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_upract_sf_atch_1))
        uel_actuator_i_1.orientation = Jusme.Vector(182.4778087722, 7.7973026777, 177.4990974087)
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, uel_actuator_i_1.location, uel_actuator_i_1.orientation)
        uel_actuator_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uel_actuator_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------------..gel_upract.uel_stopper_j_2
        uel_stopper_j_2 = ascene.getObject(".{}.gel_upract.uel_stopper_j_2".format(model_name))
        if not uel_stopper_j_2 :
            return
        uel_stopper_j_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_upract_sf_atch_1))
        uel_stopper_j_2.orientation = Jusme.Vector(182.4778087722, 7.7973026777, 177.4990974087)
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, uel_stopper_j_2.location, uel_stopper_j_2.orientation)
        uel_stopper_j_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uel_stopper_j_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------------..gel_lwract.uel_actuator_i_2
        uel_actuator_i_2 = ascene.getObject(".{}.gel_lwract.uel_actuator_i_2".format(model_name))
        if not uel_actuator_i_2 :
            return
        uel_actuator_i_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxl_joint_i_8)) 
        uel_actuator_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxl_joint_i_8))
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, uel_actuator_i_2.location, uel_actuator_i_2.orientation)
        uel_actuator_i_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uel_actuator_i_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------------..gel_lwract.uel_actuator_j_1
        uel_actuator_j_1 = ascene.getObject(".{}.gel_lwract.uel_actuator_j_1".format(model_name))
        if not uel_actuator_j_1 :
            return
        uel_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_lwract_uc_atch_1)) 
        uel_actuator_j_1.orientation = Jusme.Vector(182.4778087722, 7.7973026777, 177.4990974087)
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, uel_actuator_j_1.location, uel_actuator_j_1.orientation)
        uel_actuator_j_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uel_actuator_j_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------------..gel_lwract.uel_stopper_i_2
        uel_stopper_i_2 = ascene.getObject(".{}.gel_lwract.uel_stopper_i_2".format(model_name))
        if not uel_stopper_i_2 :
            return
        uel_stopper_i_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_lwract_uc_atch_1)) 
        uel_stopper_i_2.orientation = Jusme.Vector(182.4778087722, 7.7973026777, 177.4990974087)
        loc_ori = VecUtils.global2local(gel_lwract.location, gel_lwract.orientation, uel_stopper_i_2.location, uel_stopper_i_2.orientation)
        uel_stopper_i_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        uel_stopper_i_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        
        #---------------------------------------更新左主起所有的运动副和测量
        #--------------._AA_nlg_post_2hubs.jolsph_uc_lwract
        jolsph_uc_lwract = ascene.getObject(".{}.jolsph_uc_lwract".format(model_name))
        if not jolsph_uc_lwract :
            return
        jolsph_uc_lwract.recompute()

        #--------------._AA_nlg_post_2hubs.sf_left
        sf_left = ascene.getObject(".{}.sf_left".format(model_name))
        if not sf_left :
            return
        sf_left.recompute()

        #-------------._AA_nlg_post_2hubs.jolsph_upract_sf
        jolsph_upract_sf = ascene.getObject(".{}.jolsph_upract_sf".format(model_name))
        if not jolsph_upract_sf :
            return
        jolsph_upract_sf.recompute()

        #------------._AA_nlg_post_2hubs.disp_sf_left
        #------------对mark点的测量
        #------------测试代码
        disp_sf_left = ascene.getObject(".{}.disp_sf_left".format(model_name))
        if not disp_sf_left :
            return
        disp_sf_left.recompute()

        #----------._AA_nlg_post_2hubs.MOTION_LEFT
        MOTION_LEFT = ascene.getObject(".{}.MOTION_LEFT".format(model_name))
        if not MOTION_LEFT :
            return
        MOTION_LEFT.recompute()

        # #----------._AA_nlg_post_2hubs.vel_left
        # vel_left = ascene.getObject(".{}.vel_left".format(model_name))
        # if not vel_left :
        #     return
        # vel_left.recompute()

        pass
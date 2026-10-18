import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class DropHpsDbUcAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("start adjust hps_db_uc_atch")
        ascene = Jusme.ActiveUSScene

        #----------------------------._AA_nlg_post_2hubs.ground.hps_db_uc_atch
        hps_db_uc_atch = ascene.getObject(self.hps_full_name)
        if not hps_db_uc_atch :
            return
        
        #----------------------------._AA_nlg_post_2hubs.ground.hps_db_sf_atch
        hps_db_sf_atch = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_db_sf_atch")
        if not hps_db_sf_atch :
            return
        hps_db_uc_atch_loc = hps_db_uc_atch.location
        hps_db_sf_atch_loc = hps_db_sf_atch.location

        axis = VecUtils.ORI_ALONG_AXIS(hps_db_sf_atch_loc, hps_db_uc_atch_loc, 'z')
        center_loc = 0.5 * (hps_db_sf_atch_loc + hps_db_uc_atch_loc)

        #-------------------------------._AA_nlg_post_2hubs.ges_dragbrace
        ges_dragbrace = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace")
        if not ges_dragbrace :
            return
        ges_dragbrace.location = center_loc
        ges_dragbrace.orientation = axis

        #--------------------------------._AA_nlg_post_2hubs.ges_dragbrace.gralin_1
        gralin_1 = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.gralin_1")
        if not gralin_1 :
            return
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        gralin_1.orientation = axis
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------------._AA_nlg_post_2hubs.ges_dragbrace.cm
        cm = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.cm")
        if not cm :
            return
        cm.location = center_loc
        cm.orientation = axis
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------------------------._AA_nlg_post_2hubs.ges_dragbrace.inertia_frame
        inertia_frame = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.inertia_frame")
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ges_dragbrace))
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------------------._AA_nlg_post_2hubs.ges_dragbrace.gralin_dragbrace_geom
        gralin_dragbrace_geom = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.gralin_dragbrace_geom")
        if not gralin_dragbrace_geom :
            return
        #------------------------------计算调整后的斜撑杆长度
        len = VecUtils.DM(hps_db_sf_atch_loc, hps_db_uc_atch_loc)
        gralin_dragbrace_geom.length = len

        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject("._AA_nlg_post_2hubs.ground.origo")
        if not origo :
            return

        #-------------------------------------._AA_nlg_post_2hubs.ges_upper_cylinder.jxs_joint_j_12
        jxs_joint_j_12 = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_cylinder.jxs_joint_j_12")
        if not jxs_joint_j_12 :
            return
        #------------------------------------._AA_nlg_post_2hubs.ges_upper_cylinder
        ges_upper_cylinder = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_cylinder")
        if not ges_upper_cylinder :
            return
        jxs_joint_j_12.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_uc_atch))
        jxs_joint_j_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_j_12.location, jxs_joint_j_12.orientation)
        jxs_joint_j_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------------._AA_nlg_post_2hubs.ges_dragbrace.jxs_joint_i_12
        jxs_joint_i_12 = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.jxs_joint_i_12")
        if not jxs_joint_i_12 :
            return
        jxs_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_12))
        jxs_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_12))
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, jxs_joint_i_12.location, jxs_joint_i_12.orientation)
        jxs_joint_i_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------------------------._AA_nlg_post_2hubs.ges_subframe
        #ges_subframe = ascene.getObject("._AA_nlg_post_2hubs.ges_subframe.jxs_joint_j_14")

        #---------------------------------._AA_nlg_post_2hubs.ges_subframe.jxs_joint_j_14
        jxs_joint_j_14 = ascene.getObject("._AA_nlg_post_2hubs.ges_subframe.jxs_joint_j_14")
        if not jxs_joint_j_14 :
            return
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        jxs_joint_j_14.orientation =  (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))

        #---------------------------------._AA_nlg_post_2hubs.ges_dragbrace.jxs_joint_i_14
        jxs_joint_i_14 = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.jxs_joint_i_14")
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_14))
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_14))
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------------------._AA_nlg_post_2hubs.jossph_db_uc_joint
        jossph_db_uc_joint = ascene.getObject("._AA_nlg_post_2hubs.jossph_db_uc_joint")
        if not jossph_db_uc_joint :
            return
        jossph_db_uc_joint.recompute()

        #-------------------------------------._AA_nlg_post_2hubs.joscyl_db_sf
        joscyl_db_sf = ascene.getObject("._AA_nlg_post_2hubs.jossph_db_uc_joint")
        if not joscyl_db_sf :
            return
        joscyl_db_sf.recompute()

        pass
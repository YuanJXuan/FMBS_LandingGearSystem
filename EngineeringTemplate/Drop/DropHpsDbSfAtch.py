import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class DropHpsDbSfAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass
    
    def Adjust(self):
        ascene = Jusme.ActiveUSScene
        print("start adjusting hps_db_sf_atch")

        #----------------------------._AA_nlg_post_2hubs.ground.hps_db_sf_atch
        hps_db_sf_atch = ascene.getObject(self.hps_full_name)
        if not hps_db_sf_atch :
            return
        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject("._AA_nlg_post_2hubs.ground.origo")
        if not origo :
            return
        
        #----------------------------._AA_nlg_post_2hubs.ground.hps_db_uc_atch
        hps_db_uc_atch = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_db_uc_atch")
        if not hps_db_uc_atch :
            return
        hps_db_sf_atch_loc = hps_db_sf_atch.location
        hps_db_uc_atch_loc = hps_db_uc_atch.location

        axis = VecUtils.ORI_ALONG_AXIS(hps_db_sf_atch_loc, hps_db_uc_atch_loc, 'z')
        center_loc = 0.5 * (hps_db_sf_atch_loc + hps_db_uc_atch_loc)

        #--------------------------._AA_nlg_post_2hubs.ges_dragbrace
        ges_dragbrace = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace")
        if not ges_dragbrace :
            return
        ges_dragbrace.location = center_loc
        ges_dragbrace.orientation = axis

        #--------------------------._AA_nlg_post_2hubs.ges_dragbrace.gralin_1
        gralin_1 = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.gralin_1")
        if not gralin_1 :
            return
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        gralin_1.orientation = axis
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------------------计算._AA_nlg_post_2hubs.ges_dragbrace.gralin_dragbrace_geom的长度 
        len = VecUtils.DM(hps_db_sf_atch_loc, hps_db_uc_atch_loc)
        gralin_dragbrace_geom = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.gralin_dragbrace_geom")
        if not gralin_dragbrace_geom :
            return
        gralin_dragbrace_geom.length = len

        #--------------------设置ges_dragbrace质心位置
        cm = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.cm")
        if not cm :
            return
        cm.location = ges_dragbrace.location
        cm.orientation = axis
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------------------设置ges_dragbrace转动惯量Mark点位置
        inertia_frame = ascene.getObject("._AA_nlg_post_2hubs.ges_dragbrace.inertia_frame")
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ges_dragbrace))
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------------------------._AA_nlg_post_2hubs.ground.hps_uc_sf_atch_r
        hps_uc_sf_atch_r = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_uc_sf_atch_r")
        if not hps_uc_sf_atch_r :
            return
        hps_uc_sf_atch_r_loc = hps_uc_sf_atch_r.location

        #---------------------------._AA_nlg_post_2hubs.ground.hps_uc_sf_atch_l
        hps_uc_sf_atch_l = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_uc_sf_atch_l")
        if not hps_uc_sf_atch_l :
            return
        
        #-----------------------------计算ges_dragbrace平面的法矢
        hps_uc_sf_atch_l_loc = hps_uc_sf_atch_l.location
        vec1 = hps_uc_sf_atch_l_loc - hps_uc_sf_atch_r_loc
        vec1.normalize()
        vec2 = hps_db_sf_atch_loc - hps_uc_sf_atch_r_loc
        vec2.normalize()
        vec = vec1.cross(vec2)
        print("cross {}".format(vec))

        ges_subframe_center_loc = (hps_uc_sf_atch_l_loc + hps_uc_sf_atch_r_loc + hps_db_sf_atch_loc) / 3.0
        print("{}".format(ges_subframe_center_loc))

        ges_subframe_center_loc2 = ges_subframe_center_loc + 10 * vec
        print("{}".format(ges_subframe_center_loc2))

        axis2 = VecUtils.ORI_ALONG_AXIS(ges_subframe_center_loc, ges_subframe_center_loc2, 'y')
        print(axis2)


        #----------------------------._AA_nlg_post_2hubs.ges_subframe
        ges_subframe = ascene.getObject("._AA_nlg_post_2hubs.ges_subframe")
        if not ges_subframe :
            return
        ges_subframe.location = ges_subframe_center_loc

        

        #-------------------------------._AA_nlg_post_2hubs.ges_subframe.jxs_joint_j_14
        jxs_joint_j_14 = ascene.getObject("._AA_nlg_post_2hubs.ges_subframe.jxs_joint_j_14")
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))


        pass
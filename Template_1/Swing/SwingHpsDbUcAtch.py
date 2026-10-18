import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class SwingHpsDbUcAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始转弯仿真hps_db_uc_atch硬点调整")

        ascene = Jusme.ActiveUSScene

        #---------------获取当前模型名称
        model_name = Common.getModelName()

        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            return

        #--------获取ground.hps_db_uc_atch
        hps_db_uc_atch = ascene.getObject(self.hps_full_name)
        if not hps_db_uc_atch :
            return
        
        #--------获取.ground.hps_db_sf_atch
        hps_db_sf_atch = ascene.getObject(".{}.ground.hps_db_sf_atch".format(model_name))
        if not hps_db_sf_atch :
            return

        hps_db_sf_atch_loc=hps_db_sf_atch.location
        hps_db_uc_atch_loc=hps_db_uc_atch.location

        axis = VecUtils.ORI_ALONG_AXIS(hps_db_sf_atch_loc, hps_db_uc_atch_loc, 'z')
        center_loc = 0.5 * (hps_db_sf_atch_loc + hps_db_uc_atch_loc)

        #-------获取.ges_dragbrace
        ges_dragbrace = ascene.getObject(".{}.ges_dragbrace".format(model_name))
        if not ges_dragbrace :
            return
        ges_dragbrace.location = center_loc
        ges_dragbrace.orientation = axis

        #-------开始修改.ges_dragbrace的内容

        #-------修改.ges_dragbrace.gralin_1
        gralin_1 = ascene.getObject(".{}.ges_dragbrace.gralin_1".format(model_name))
        if not gralin_1 :
            return
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        gralin_1.orientation = axis
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改.ges_dragbrace.gralin_dragbrace_geom
        gralin_dragbrace_geom = ascene.getObject(".{}.ges_dragbrace.gralin_dragbrace_geom".format(model_name))
        if not gralin_dragbrace_geom :
            return
        #------计算调整后的斜撑杆长度
        len = VecUtils.DM(hps_db_sf_atch_loc, hps_db_uc_atch_loc)
        gralin_dragbrace_geom.length = len

        #------修改.ges_dragbrace.cm
        cm = ascene.getObject(".{}.ges_dragbrace.cm".format(model_name))
        if not cm :
            return
        cm.location = center_loc
        cm.orientation = axis
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改.ges_dragbrace.inertia_frame
        inertia_frame = ascene.getObject(".{}.ges_dragbrace.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cm))
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], ges_dragbrace))
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------修改.ges_upper_cylinder.jxs_joint_j_12
        jxs_joint_j_12 = ascene.getObject(".{}.ges_upper_cylinder.jxs_joint_j_12".format(model_name))
        if not jxs_joint_j_12 :
            return
        #-------获取.ges_upper_cylinder
        ges_upper_cylinder = ascene.getObject(".{}.ges_upper_cylinder".format(model_name))
        if not ges_upper_cylinder :
            return
        jxs_joint_j_12.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_uc_atch))
        jxs_joint_j_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_j_12.location, jxs_joint_j_12.orientation)
        jxs_joint_j_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----修改.ges_upper_cylinder.jxs_joint_i_12
        jxs_joint_i_12 = ascene.getObject(".{}.ges_dragbrace.jxs_joint_i_12".format(model_name))
        if not jxs_joint_i_12 :
            return
        jxs_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_12))
        jxs_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_12))
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, jxs_joint_i_12.location, jxs_joint_i_12.orientation)
        jxs_joint_i_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------获取ges_subframe
        ges_subframe = ascene.getObject(".{}.ges_subframe".format(model_name))
        if not ges_subframe :
            return
        
        #------.ges_subframe.jxs_joint_j_14
        jxs_joint_j_14 = ascene.getObject(".{}.ges_subframe.jxs_joint_j_14".format(model_name))
        if not jxs_joint_j_14 :
            return
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        jxs_joint_j_14.orientation =  (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------.ges_dragbrace.jxs_joint_i_14
        jxs_joint_i_14 = ascene.getObject(".{}.ges_dragbrace.jxs_joint_i_14".format(model_name))
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_14))
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_14))
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------------------.js_wt
        js_wt = ascene.getObject(".{}.js_wt".format(model_name))
        if not js_wt :
            return
        js_wt.recompute()

        #---------------------------.zdt_upcylinder
        zdt_upcylinder = ascene.getObject(".{}.zdt_upcylinder".format(model_name))
        if not zdt_upcylinder :
            return
        zdt_upcylinder.recompute()

        #---------------------------.josrev_collar_uc_joint
        josrev_collar_uc_joint = ascene.getObject(".{}.josrev_collar_uc_joint".format(model_name))
        if not josrev_collar_uc_joint :
            return
        josrev_collar_uc_joint.recompute()

        #---------------------------.josrev_collar_uc_joint
        josrev_collar_uc_joint = ascene.getObject(".{}.josrev_collar_uc_joint".format(model_name))
        if not josrev_collar_uc_joint :
            return
        josrev_collar_uc_joint.recompute()

        #---------------------------.josrev_uc_sf_joint
        josrev_uc_sf_joint = ascene.getObject(".{}.josrev_uc_sf_joint".format(model_name))
        if not josrev_uc_sf_joint :
            return
        josrev_uc_sf_joint.recompute()


        #---------------------------.jossph_db_uc_joint
        jossph_db_uc_joint = ascene.getObject(".{}.jossph_db_uc_joint".format(model_name))
        if not jossph_db_uc_joint :
            return
        jossph_db_uc_joint.recompute()

        #---------------------------.joscyl_lc_uc_joint
        joscyl_lc_uc_joint = ascene.getObject(".{}.joscyl_lc_uc_joint".format(model_name))
        if not joscyl_lc_uc_joint :
            return
        joscyl_lc_uc_joint.recompute()

        #------------joint:joscyl_db_sf
        joscyl_db_sf = ascene.getObject(".{}.joscyl_db_sf".format(model_name))
        if not joscyl_db_sf :
            return
        joscyl_db_sf.recompute()

        #------------joint:mts_fixed_2
        mts_fixed_2 = ascene.getObject(".{}.mts_fixed_2".format(model_name))
        if not mts_fixed_2 :
            return
        mts_fixed_2.recompute()
        print("调整结束")
        pass
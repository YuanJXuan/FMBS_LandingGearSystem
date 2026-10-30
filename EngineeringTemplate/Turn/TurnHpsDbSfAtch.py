import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class TurnHpsDbSfAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        ascene = Jusme.ActiveUSScene
        print("开始转弯仿真hps_db_sf_atch硬点调整")
        
        #----------------获取调整后的硬点hps_db_sf_atch
        hps_db_sf_atch = ascene.getObject(self.hps_full_name)
        if not hps_db_sf_atch :
            return
        #---------------获取当前模型名称
        model_name = Common.getModelName()

        #----------------获取全局坐标系原点origo的mark点
        origo=ascene.getObject(".{}.ground.origo".format(model_name))
        #----------------获取硬点hps_db_uc_atch
        hps_db_uc_atch = ascene.getObject(".{}.ground.hps_db_uc_atch".format(model_name))
        if not hps_db_uc_atch :
            return
        
        hps_db_sf_atch_loc=hps_db_sf_atch.location
        hps_db_uc_atch_loc=hps_db_uc_atch.location

        axis=VecUtils.ORI_ALONG_AXIS(hps_db_sf_atch_loc,hps_db_uc_atch_loc,'z')
        center_loc=0.5*(hps_db_sf_atch_loc+hps_db_uc_atch_loc)

        #----------------开始修改ges_dragbrace的相关内容---------------
        ges_dragbrace=ascene.getObject(".{}.ges_dragbrace".format(model_name))
        if not ges_dragbrace :
            return
        ges_dragbrace.location = center_loc
        ges_dragbrace.orientation = axis
        
        #---------------修改ges_dragbrace.gralin_1
        gralin_1=ascene.getObject(".{}.ges_dragbrace.gralin_1".format(model_name))
        if not gralin_1:
            return
        gralin_1.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hps_db_sf_atch))
        gralin_1.orientation=axis
        loc_ori=VecUtils.global2local(ges_dragbrace.location,ges_dragbrace.orientation,gralin_1.location,gralin_1.orientation)
        gralin_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])
        
        #--------------修改ges_dragbrace.gralin_dragbrace_geom
        len=VecUtils.DM(hps_db_sf_atch_loc,hps_db_uc_atch_loc)
        gralin_dragbrace_geom=ascene.getObject(".{}.ges_dragbrace.gralin_dragbrace_geom".format(model_name))
        if not gralin_dragbrace_geom :
            return
        gralin_dragbrace_geom.length = len

        #--------------修改ges_dragbrace.cm
        cm=ascene.getObject(".{}.ges_dragbrace.cm".format(model_name))
        if not cm:
            return
        cm.location=ges_dragbrace.location
        cm.orientation=ges_dragbrace.orientation
        loc_ori=VecUtils.global2local(ges_dragbrace.location,ges_dragbrace.orientation,cm.location,cm.orientation)
        cm.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        cm.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])
        
        #--------------修改ges_dragbrace.inertia_frame
        inertia_frame=ascene.getObject(".{}.ges_dragbrace.inertia_frame".format(model_name))
        if not inertia_frame:
            return
        inertia_frame.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],cm))
        inertia_frame.orientation=(VecUtils.ORI_RELATIVE_TO([0,0,0],ges_dragbrace))
        loc_ori=VecUtils.global2local(ges_dragbrace.location,ges_dragbrace.orientation,inertia_frame.location,inertia_frame.orientation)
        inertia_frame.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #-------------开始修改ges_subframe的相关内容（修改完jxs_joint_j_14后，修改ges_dragbrace.jxs_joint_i_14）------------------------
        ges_subframe = ascene.getObject(".{}.ges_subframe".format(model_name))
        if not ges_subframe :
            return

        #------------ground.hps_uc_sf_atch_r
        hps_uc_sf_atch_r = ascene.getObject(".{}.ground.hps_uc_sf_atch_r".format(model_name))
        if not hps_uc_sf_atch_r :
            return
        hps_uc_sf_atch_r_loc = hps_uc_sf_atch_r.location

        #-------------ground.hps_uc_sf_atch_l
        hps_uc_sf_atch_l = ascene.getObject(".{}.ground.hps_uc_sf_atch_l".format(model_name))
        if not hps_uc_sf_atch_l :
            return
        hps_uc_sf_atch_l_loc = hps_uc_sf_atch_l.location

         #---------ges_subframe.graout_1
        graout_1 = ascene.getObject(".{}.ges_subframe.graout_1".format(model_name))
        if not graout_1 :
            return
        graout_1.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_sf_atch_r))

        #---------ges_subframe.graout_2
        graout_2 = ascene.getObject(".{}.ges_subframe.graout_2".format(model_name))
        if not graout_2 :
            return
        graout_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_sf_atch_l))
        
        #---------ges_subframe.graout_3
        graout_3 = ascene.getObject(".{}.ges_subframe.graout_3".format(model_name))
        if not graout_3 :
            return
        #---------修改graout3的位置以及graout1、2、3的方向
        graout_3.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        
        nor_vec=VecUtils.ORI_IN_PLANE(graout_1.location,graout_2.location,graout_3.location,"z_zx")

        graout_1.orientation=nor_vec
        graout_2.orientation=nor_vec   
        graout_3.orientation=nor_vec
        
        ges_subframe_center_loc=(graout_1.location+graout_2.location+graout_3.location)/3.0
        ges_subframe.location=ges_subframe_center_loc
        ges_subframe.orientation=nor_vec

        loc_ori=VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, graout_1.location, graout_1.orientation)
        graout_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        graout_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        loc_ori=VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, graout_2.location, graout_2.orientation)
        graout_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        graout_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        loc_ori=VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, graout_3.location, graout_3.orientation)
        graout_3.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        graout_3.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------修改ges_subframe.cm
        cm = ascene.getObject(".{}.ges_subframe.cm".format(model_name))
        if not cm :
            return
        cm.location = ges_subframe_center_loc
        cm.orientation = nor_vec
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, cm.location, cm.orientation)
        cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------修改ges_subframe.inertia_frame
        inertia_frame = ascene.getObject(".{}.ges_subframe.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],cm))
        inertia_frame.orientation=(VecUtils.ORI_RELATIVE_TO([0.0,0.0,0.0],ges_subframe))
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        
        #------修改修改ges_subframe.jxs_joint_j_14
        jxs_joint_j_14 = ascene.getObject(".{}.ges_subframe.jxs_joint_j_14".format(model_name))
        if not jxs_joint_j_14 :
            print("没有找到jxs_joint_j_14")
            return
        jxs_joint_j_14.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hps_db_sf_atch))
        jxs_joint_j_14.orientation=(VecUtils.ORI_RELATIVE_TO([0.0,90.0,0.0],origo))
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------修改ges_dragbrace.jxs_joint_i_14
        jxs_joint_i_14 = ascene.getObject(".{}.ges_dragbrace.jxs_joint_i_14".format(model_name))
        if not jxs_joint_i_14 :
            print("没有找到jxs_joint_i_14")
            return
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_14))
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_14))
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----修改ground.cfs_uc_sf_atch_mid
        #---------目前从Adams模型中没有定义拓扑关联
        #--------位置默认按hps_uc_sf_atch_r和hps_uc_sf_atch_l的中点处理
        #--------方向按ges_subframe物体的方向处理
        cfs_uc_sf_atch_mid = ascene.getObject(".{}.ground.cfs_uc_sf_atch_mid".format(model_name))
        if not cfs_uc_sf_atch_mid :
            return
        cfs_uc_sf_atch_mid.location = 0.5 * (hps_uc_sf_atch_r_loc + hps_uc_sf_atch_l_loc)
        cfs_uc_sf_atch_mid.orientation = nor_vec

        #-----修改ges_subframe.jxs_joint_j_15
        jxs_joint_j_15 = ascene.getObject(".{}.ges_subframe.jxs_joint_j_15".format(model_name))
        if not jxs_joint_j_15 :
            return
        jxs_joint_j_15.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfs_uc_sf_atch_mid))
        #-------茉莉平台中没有(ORI_LOCAL(ORI_ALIGN_AXIS(cfs_uc_sf_atch_mid, "Z+Z"), ges_subframe))
        #-------相关处理函数，默认按cfs_uc_sf_atch_mid的同向处理
        jxs_joint_j_15.orientation=nor_vec
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_j_15.location, jxs_joint_j_15.orientation)
        jxs_joint_j_15.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_15.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----修改ges_upper_cylinder.jxs_joint_i_15
        ges_upper_cylinder = ascene.getObject(".{}.ges_upper_cylinder".format(model_name))
        if not ges_upper_cylinder :
            return

        jxs_joint_i_15 = ascene.getObject(".{}.ges_upper_cylinder.jxs_joint_i_15".format(model_name))
        if not jxs_joint_i_15 :
            return
        jxs_joint_i_15.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_15))
        jxs_joint_i_15.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_15))
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_i_15.location, jxs_joint_i_15.orientation)
        jxs_joint_i_15.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_15.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ground.cfs_subframe_to_body_point
        cfs_subframe_to_body_point = ascene.getObject(".{}.ground.cfs_subframe_to_body_point".format(model_name))
        if not cfs_subframe_to_body_point :
            return
        cfs_subframe_to_body_point.location = ges_subframe_center_loc
        cfs_subframe_to_body_point.orientation = nor_vec

        #-----修改mts_body_mount
        mts_body_mount = ascene.getObject(".{}.mts_body_mount".format(model_name))
        if not mts_body_mount :
            return
        mts_body_mount.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], cfs_subframe_to_body_point))
        mts_body_mount.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))

        #-------修改ground.mts_mount_j_2
        mts_mount_j_2 = ascene.getObject(".{}.ground.mts_mount_j_2".format(model_name))
        if not mts_mount_j_2 :
            return
        mts_mount_j_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], mts_body_mount))
        mts_mount_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], mts_body_mount))

        #-------修改mts_body_mount.mount_i
        mount_i = ascene.getObject(".{}.mts_body_mount.mount_i".format(model_name))
        if not  mount_i :
            return
        mount_i.location = ges_subframe_center_loc
        mount_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        loc_ori= VecUtils.global2local(mts_body_mount.location, mts_body_mount.orientation, mount_i.location, mount_i.orientation)
        mount_i.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        mount_i.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.jxs_joint_j_12
        jxs_joint_j_12 = ascene.getObject(".{}.ges_upper_cylinder.jxs_joint_j_12".format(model_name))
        if not  jxs_joint_j_12 :
            return
        jxs_joint_j_12.location = (VecUtils.LOC_RELATIVE_TO([0,0,0],hps_db_uc_atch))
        jxs_joint_j_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        loc_ori= VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_j_12.location, jxs_joint_j_12.orientation)
        jxs_joint_j_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_dragbrace.jxs_joint_i_12
        jxs_joint_i_12 = ascene.getObject(".{}.ges_dragbrace.jxs_joint_i_12".format(model_name))
        if not  jxs_joint_i_12 :
            return
        jxs_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_j_12))
        jxs_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_12))
        loc_ori= VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, jxs_joint_i_12.location, jxs_joint_i_12.orientation)
        jxs_joint_i_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        # #-------修改mts_body_mount.jxs_joint_j_16
        # jxs_joint_j_16 = ascene.getObject(".{}.mts_body_mount.jxs_joint_j_16".format(model_name))
        # if not  jxs_joint_j_16 :
        #     print("没有找到jxs_joint_j_16")
        #     return
        # jxs_joint_j_16.location = (VecUtils.LOC_RELATIVE_TO([0,0,0],cfs_subframe_to_body_point))
        # jxs_joint_j_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        # loc_ori= VecUtils.global2local(mts_body_mount.location, mts_body_mount.orientation, jxs_joint_j_16.location, jxs_joint_j_16.orientation)
        # jxs_joint_j_16.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # jxs_joint_j_16.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        # #-------修改ges_subframe.jxs_joint_i_16
        # jxs_joint_i_16 = ascene.getObject(".{}.ges_subframe.jxs_joint_i_16".format(model_name))
        # if not  jxs_joint_i_16 :
        #     print("没有找到jxs_joint_i_16")
        #     return
        # jxs_joint_i_16.location = (VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_j_16))
        # jxs_joint_i_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_16))
        # loc_ori= VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_i_16.location, jxs_joint_i_16.orientation)
        # jxs_joint_i_16.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # jxs_joint_i_16.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        print("开始")
        #------------joint:js_wt
        js_wt = ascene.getObject(".{}.js_wt".format(model_name))
        if not js_wt :
            return
        js_wt.recompute()

        #------------joint:zdt_upcylinder
        zdt_upcylinder = ascene.getObject(".{}.zdt_upcylinder".format(model_name))
        if not zdt_upcylinder :
            return
        zdt_upcylinder.recompute()

        #------------joint:josrev_collar_uc_joint
        josrev_collar_uc_joint = ascene.getObject(".{}.josrev_collar_uc_joint".format(model_name))
        if not josrev_collar_uc_joint :
            return
        josrev_collar_uc_joint.recompute()

       

        #------------joint:josrev_uc_sf_joint
        josrev_uc_sf_joint = ascene.getObject(".{}.josrev_uc_sf_joint".format(model_name))
        if not josrev_uc_sf_joint :
            return
        josrev_uc_sf_joint.recompute()

        #------------joint:jossph_db_uc_joint
        jossph_db_uc_joint = ascene.getObject(".{}.jossph_db_uc_joint".format(model_name))
        if not jossph_db_uc_joint :
            return
        jossph_db_uc_joint.recompute()

        #------------joint:joscyl_lc_uc_joint
        joscyl_lc_uc_joint = ascene.getObject(".{}.joscyl_lc_uc_joint".format(model_name))
        if not joscyl_lc_uc_joint :
            return
        joscyl_lc_uc_joint.recompute()

        #------------joint:jossph_db_uc_joint
        jossph_db_uc_joint = ascene.getObject(".{}.jossph_db_uc_joint".format(model_name))
        if not jossph_db_uc_joint :
            return
        jossph_db_uc_joint.recompute()

        #------------joint:jossph_db_uc_joint
        jossph_db_uc_joint = ascene.getObject(".{}.jossph_db_uc_joint".format(model_name))
        if not jossph_db_uc_joint :
            return
        jossph_db_uc_joint.recompute()

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
        print("结束")
        pass
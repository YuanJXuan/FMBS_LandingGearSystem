import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class BrakeHplUtaCollarAtch1Adjust(AbstractHps.AbstractHpsAdjust)  :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始修改hpl_uta_collar_atch_1")
        ascene = Jusme.ActiveUSScene
        model_name = Common.getModelName()

        #-----------获取hpl_uta_collar_atch_1
        hpl_uta_collar_atch_1 = ascene.getObject(self.hps_full_name)
        if not hpl_uta_collar_atch_1 :
            print("未找到hpl_uta_collar_atch_1")
            return

        #---------获取hpl_uta_connect_atch_1(hps)
        hpl_uta_connect_atch_1 = ascene.getObject(".{}.ground.hpl_uta_connect_atch_1".format(model_name))
        if not hpl_uta_connect_atch_1 :
            print("未找到3")
            return
        
        #---------获取hpl_uta_connect_atch_2(hps)
        hpl_uta_connect_atch_2 = ascene.getObject(".{}.ground.hpl_uta_connect_atch_2".format(model_name))
        if not hpl_uta_connect_atch_2 :
            print("未找到3")
            return

        #---------获取hpl_lta_connect_atch_1(hps)
        hpl_lta_connect_atch_1 = ascene.getObject(".{}.ground.hpl_lta_connect_atch_1".format(model_name))
        if not hpl_lta_connect_atch_1 :
            print("未找到3")
            return

        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            print("未找到4")
            return

        #---------获取gel_lower_cylinder(part)
        gel_lower_cylinder = ascene.getObject(".{}.gel_lower_cylinder".format(model_name))
        if not gel_lower_cylinder :
            print("未找到5")
            return

        #---------获取gel_lower_torquearm(part)
        gel_lower_torquearm = ascene.getObject(".{}.gel_lower_torquearm".format(model_name))
        if not gel_lower_torquearm :
            print("未找到6")
            return

        #---------获取gel_upper_torquearm
        gel_upper_torquearm = ascene.getObject(".{}.gel_upper_torquearm".format(model_name))
        if not gel_upper_torquearm :
            print("未找到6")
            return

        #---------修改gel_upper_torquearm(part)的相关内容-----------
        gel_upper_torquearm.location=0.5*(hpl_uta_collar_atch_1.location+hpl_uta_connect_atch_1.location)
        gel_upper_torquearm.orientation=(VecUtils.ORI_ALONG_AXIS(hpl_uta_collar_atch_1.location,hpl_uta_connect_atch_1.location,'z'))


        #---------修改gel_upper_torquearm.gralin_11(marker)
        gralin_11 = ascene.getObject(".{}.gel_upper_torquearm.gralin_11".format(model_name))
        if not gralin_11 :
            print("未找到9")
            return
        gralin_11.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uta_collar_atch_1))
        gralin_11.orientation=(VecUtils.ORI_ALONG_AXIS(hpl_uta_collar_atch_1.location,hpl_uta_connect_atch_1.location,'z'))
        loc_ori=VecUtils.global2local(gel_upper_torquearm.location,gel_upper_torquearm.orientation,gralin_11.location,gralin_11.orientation)
        gralin_11.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_11.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #---------修改gel_upper_torquearm.gralin_upper_torquearm(geom)
        gralin_upper_torquearm = ascene.getObject(".{}.gel_upper_torquearm.gralin_upper_torquearm".format(model_name))
        if not gralin_upper_torquearm :
            print("未找到10")
            return
        gralin_upper_torquearm.length=(VecUtils.DM(hpl_uta_collar_atch_1.location,hpl_uta_connect_atch_1.location))

        #---------修改gel_upper_torquearm.cm(marker)
        gel_upper_torquearm_cm = ascene.getObject(".{}.gel_upper_torquearm.cm".format(model_name))
        if not gel_upper_torquearm_cm :
            print("未找到11")
            return
        gel_upper_torquearm_cm.location=gel_upper_torquearm.location
        gel_upper_torquearm_cm.orientation=gel_upper_torquearm.orientation
        loc_ori=VecUtils.global2local(gel_upper_torquearm.location,gel_upper_torquearm.orientation,gel_upper_torquearm_cm.location,gel_upper_torquearm_cm.orientation)
        gel_upper_torquearm_cm.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gel_upper_torquearm_cm.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #---------修改gel_upper_torquearm.inertia_frame(marker)
        inertia_frame = ascene.getObject(".{}.gel_upper_torquearm.inertia_frame".format(model_name))
        if not inertia_frame :
            print("未找到12")
            return
        inertia_frame.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],gel_upper_torquearm_cm))
        inertia_frame.orientation=(VecUtils.ORI_RELATIVE_TO([0,0,0],gel_upper_torquearm))
        loc_ori=VecUtils.global2local(gel_upper_torquearm.location,gel_upper_torquearm.orientation,inertia_frame.location,inertia_frame.orientation)
        inertia_frame.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #---------获取gel_uc_collar(part)
        gel_lower_cylinder = ascene.getObject(".{}.gel_lower_cylinder".format(model_name))
        if not gel_lower_cylinder :
            print("未找到5")
            return

        #--------修改gel_uc_collar.jxl_joint_j_3
        jxl_joint_j_3 = ascene.getObject(".{}.gel_uc_collar.jxl_joint_j_3".format(model_name))
        if not jxl_joint_j_3 :
            print("未找到12")
            return
        jxl_joint_j_3.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uta_collar_atch_1))
        jxl_joint_j_3.orientation=(VecUtils.ORI_ALONG_AXIS(hpl_lta_connect_atch_1.location,hpl_uta_connect_atch_1.location,'z'))
        loc_ori=VecUtils.global2local(gel_upper_torquearm.location,gel_upper_torquearm.orientation,jxl_joint_j_3.location,jxl_joint_j_3.orientation)
        jxl_joint_j_3.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_3.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #--------修改gel_upper_torquearm.jxl_joint_i_3
        jxl_joint_i_3 = ascene.getObject(".{}.gel_upper_torquearm.jxl_joint_i_3".format(model_name))
        if not jxl_joint_i_3 :
            print("未找到12")
            return
        jxl_joint_i_3.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],jxl_joint_j_3))
        jxl_joint_i_3.orientation=(VecUtils.ORI_RELATIVE_TO([0,0,0],jxl_joint_j_3))
        loc_ori=VecUtils.global2local(gel_upper_torquearm.location,gel_upper_torquearm.orientation,jxl_joint_i_3.location,jxl_joint_i_3.orientation)
        jxl_joint_i_3.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_3.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #---------修改gel_connector的相关内容--------------
        gel_connector = ascene.getObject(".{}.gel_connector".format(model_name))
        if not gel_connector :
            print("未找到8")
            return
        
        #---------修改gel_connector.jxl_joint_j_1
        jxl_joint_j_1 = ascene.getObject(".{}.gel_connector.jxl_joint_j_1".format(model_name))
        if not jxl_joint_j_1 :
            print("未找到8")
            return
        jxl_joint_j_1.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_lta_connect_atch_1))
        jxl_joint_j_1.orientation=(VecUtils.ORI_ALONG_AXIS(hpl_lta_connect_atch_1.location,hpl_uta_connect_atch_1.location,'z'))
        loc_ori=VecUtils.global2local(gel_connector.location,gel_connector.orientation,jxl_joint_j_1.location,jxl_joint_j_1.orientation)
        jxl_joint_j_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #---------修改gel_lower_torquearm.jxl_joint_i_1
        jxl_joint_i_1 = ascene.getObject(".{}.gel_lower_torquearm.jxl_joint_i_1".format(model_name))
        if not jxl_joint_i_1 :
            print("未找到8")
            return
        jxl_joint_i_1.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],jxl_joint_j_1))
        jxl_joint_i_1.orientation=(VecUtils.ORI_RELATIVE_TO([0,0,0],jxl_joint_j_1))
        loc_ori=VecUtils.global2local(gel_lower_torquearm.location,gel_lower_torquearm.orientation,jxl_joint_i_1.location,jxl_joint_i_1.orientation)
        jxl_joint_i_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #---------获取gel_upper_torquearm
        gel_upper_torquearm = ascene.getObject(".{}.gel_upper_torquearm".format(model_name))
        if not gel_upper_torquearm :
            print("未找到6")
            return

        #------修改gel_connector.jxl_joint_j_2
        jxl_joint_j_2 = ascene.getObject(".{}.gel_connector.jxl_joint_j_2".format(model_name))
        if not jxl_joint_j_2 :
            print("未找到7")
            return
        jxl_joint_j_2.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uta_connect_atch_1))
        jxl_joint_j_2.orientation=(VecUtils.ORI_ALONG_AXIS(hpl_uta_connect_atch_1.location,hpl_uta_connect_atch_2.location,'z'))
        loc_ori=VecUtils.global2local(gel_connector.location,gel_connector.orientation,jxl_joint_j_2.location,jxl_joint_j_2.orientation)
        jxl_joint_j_2.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_2.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #------修改gel_upper_torquearm.jxl_joint_i_2
        jxl_joint_i_2 = ascene.getObject(".{}.gel_upper_torquearm.jxl_joint_i_2".format(model_name))
        if not jxl_joint_i_2 :
            print("未找到7")
            return
        jxl_joint_i_2.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],jxl_joint_j_2))
        jxl_joint_i_2.orientation=(VecUtils.ORI_RELATIVE_TO([0,0,0],jxl_joint_j_2))
        loc_ori=VecUtils.global2local(gel_upper_torquearm.location,gel_upper_torquearm.orientation,jxl_joint_i_2.location,jxl_joint_i_2.orientation)
        jxl_joint_i_2.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_2.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        #------------ground.JOINT_33
        JOINT_33 = ascene.getObject(".{}.JOINT_33".format(model_name))
        if not JOINT_33 :
            print("未找到16")
            return
        JOINT_33.recompute()

        #------------ground.jolrev_ldb_collar
        jolrev_ldb_collar = ascene.getObject(".{}.jolrev_ldb_collar".format(model_name))
        if not jolrev_ldb_collar :
            print("未找到16")
            return
        jolrev_ldb_collar.recompute()

        #------------ground.jolrev_collar_uc
        jolrev_collar_uc = ascene.getObject(".{}.jolrev_collar_uc".format(model_name))
        if not jolrev_collar_uc :
            print("未找到16")
            return
        jolrev_collar_uc.recompute()

        #------------ground.jolrev_uta_collar
        jolrev_uta_collar = ascene.getObject(".{}.jolrev_uta_collar".format(model_name))
        if not jolrev_uta_collar :
            print("未找到16")
            return
        jolrev_uta_collar.recompute()

        #------------ground.jolrev_uta_connect
        jolrev_uta_connect = ascene.getObject(".{}.jolrev_uta_connect".format(model_name))
        if not jolrev_uta_connect :
            print("未找到16")
            return
        jolrev_uta_connect.recompute()

        #------------ground.jolcyl_lta_connect
        jolcyl_lta_connect = ascene.getObject(".{}.jolcyl_lta_connect".format(model_name))
        if not jolcyl_lta_connect :
            print("未找到16")
            return
        jolcyl_lta_connect.recompute()

        #------------ground.jolcyl_lc_uc_joint
        jolcyl_lc_uc_joint = ascene.getObject(".{}.jolcyl_lc_uc_joint".format(model_name))
        if not jolcyl_lc_uc_joint :
            print("未找到16")
            return
        jolcyl_lc_uc_joint.recompute()

        #------------ground.jolrev_lta_lc_joint
        jolrev_lta_lc_joint = ascene.getObject(".{}.jolrev_lta_lc_joint".format(model_name))
        if not jolrev_lta_lc_joint :
            print("未找到16")
            return
        jolrev_lta_lc_joint.recompute()


        print("结束修改hpl_uta_collar_atch_1")

        pass
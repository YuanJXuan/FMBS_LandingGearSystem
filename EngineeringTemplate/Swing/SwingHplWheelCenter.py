import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class SwingHplWheelCenterAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始转弯仿真hpl_wheel_center硬点调整")

        ascene = Jusme.ActiveUSScene
        #---------------获取当前模型名称
        model_name = Common.getModelName()

        #----------------获取全局坐标系原点origo的mark点
        origo=ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            return

       #------获取修改后的hpl_wheel_center 并对称修改hpr_wheel_center-----
        hpl_wheel_center = ascene.getObject(self.hps_full_name)
        if not hpl_wheel_center :
            return
     

        hpr_wheel_center = ascene.getObject(".{}.ground.hpr_wheel_center".format(model_name))
        if not hpr_wheel_center :
            return
        hpr_wheel_center.location.y=-1*(hpl_wheel_center.location.y)
        

        hpl_wheel_center_loc=hpl_wheel_center.location
        hpr_wheel_center_loc=hpr_wheel_center.location

        #-------获取hpl_ob_axle
        hpl_ob_axle = ascene.getObject(".{}.ground.hpl_ob_axle".format(model_name))
        if not hpl_ob_axle :
            return
        hpl_ob_axle_loc=hpl_ob_axle.location

        #-------获取hpr_ob_axle
        hpr_ob_axle = ascene.getObject(".{}.ground.hpr_ob_axle".format(model_name))
        if not hpr_ob_axle :
            return
        hpr_ob_axle_loc=hpr_ob_axle.location

        #------修改cfl_spin_axis(marker)
        cfl_spin_axis = ascene.getObject(".{}.ground.cfl_spin_axis".format(model_name))
        if not cfl_spin_axis :
            return
        cfl_spin_axis.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_wheel_center)
        cfl_spin_axis.orientation=VecUtils.ORI_ALONG_AXIS(hpl_wheel_center_loc,hpl_ob_axle_loc,'z')

        #------修改cfr_spin_axis(marker)
        cfr_spin_axis = ascene.getObject(".{}.ground.cfr_spin_axis".format(model_name))
        if not cfr_spin_axis :
            return
        cfr_spin_axis.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_wheel_center)
        cfr_spin_axis.orientation=VecUtils.ORI_ALONG_AXIS(hpr_wheel_center_loc,hpr_ob_axle_loc,'z')

        #------修改ges_lower_cylinder的相关内容(由于part质心计算存在不确定性，没有修改ges_lower_cylinder.cm)
        ges_lower_cylinder = ascene.getObject(".{}.ges_lower_cylinder".format(model_name))
        if not ges_lower_cylinder :
            return

        ges_lower_cylinder_cm=ascene.getObject(".{}.ges_lower_cylinder.cm".format(model_name))
        if not ges_lower_cylinder_cm :
            return
        ges_lower_cylinder_cm.recompute()
        
        ges_lower_cylinder.location=ges_lower_cylinder_cm.location
        # ges_lower_cylinder.orientation=ges_lower_cylinder_cm.orientation

        #------修改ges_lower_cylinder.gralin_7
        gralin_7 = ascene.getObject(".{}.ges_lower_cylinder.gralin_7".format(model_name))
        if not gralin_7 :
            return
        gralin_7.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_wheel_center)
        gralin_7.orientation=VecUtils.ORI_ALONG_AXIS(hpr_wheel_center_loc,hpl_wheel_center_loc,'z')
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----修改ges_lower_cylinder.gralin_geom2
        gralin_geom2 = ascene.getObject(".{}.ges_lower_cylinder.gralin_geom2".format(model_name))
        if not gralin_geom2 :
            return
        gralin_geom2.length=VecUtils.DM(hpr_wheel_center_loc,hpl_wheel_center_loc)

        

        #----修改ges_lower_cylinder.MARKER_158
        MARKER_158 = ascene.getObject(".{}.ges_lower_cylinder.MARKER_158".format(model_name))
        if not MARKER_158 :
            return
        MARKER_158.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_wheel_center)
        MARKER_158.orientation=Jusme.Vector(180, 90, 180)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_158.location, MARKER_158.orientation)
        MARKER_158.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_158.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        

        #----修改ges_lower_cylinder.MARKER_160
        MARKER_160 = ascene.getObject(".{}.ges_lower_cylinder.MARKER_160".format(model_name))
        if not MARKER_160 :
            return
        MARKER_160.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_wheel_center)
        MARKER_160.orientation=Jusme.Vector(0, 90, 0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_160.location, MARKER_160.orientation)
        MARKER_160.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_160.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----修改lt_l的内容------------

        #----修改lt_l.wheel_part.MARKER_157(未找到) 茉莉中未有轮胎模型信息
        # MRAKER_157 = ascene.getObject(".{}.lt_l.wheel_part.MARKER_157".format(model_name))
        # if not MARKER_157 :
        #     print("未找到MARKER_157")
        #     return
        # VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_wheel_center)
        # Jusme.Vector(180, 90, 180)
        # loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_157.location, MARKER_157.orientation)
        # MARKER_157.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # MARKER_157.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        #-----------------------------




        #----修改lt_r的内容------------

        #----修改lt_r.wheel_part.MARKER_159（未找到）
        # MRAKER_159 = ascene.getObject(".{}.lt_r.wheel_part.MARKER_159".format(model_name))
        # if not MARKER_159 :
        #     print("未找到MARKER_159")
        #     return
        # MRAKER_159.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_wheel_center)
        # MARKER_159.orientation=Jusme.Vector(0, 90, 0)
        # loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_159.location, MARKER_159.orientation)
        # MARKER_159.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # MARKER_159.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        #-----------------------------




        #--修改与cfl_spin_axis相关的内容-----
        #-----------------------------------





        #--修改与cfr_spin_axis相关的内容-----
        #-----------------------------------

        joint_lt_y = ascene.getObject(".{}.joint_lt_y".format(model_name))
        if not joint_lt_y :
            return
        joint_lt_y.recompute()

        joint_lt_z = ascene.getObject(".{}.joint_lt_z".format(model_name))
        if not joint_lt_z :
            return
        joint_lt_z.recompute()

        joscyl_lc_uc_joint = ascene.getObject(".{}.joscyl_lc_uc_joint".format(model_name))
        if not joscyl_lc_uc_joint :
            return
        joscyl_lc_uc_joint.recompute()

        jossph_lta_lc_joint = ascene.getObject(".{}.jossph_lta_lc_joint".format(model_name))
        if not jossph_lta_lc_joint :
            return
        jossph_lta_lc_joint.recompute()

        

        print("结束调整hpl_wheel_center")




        pass
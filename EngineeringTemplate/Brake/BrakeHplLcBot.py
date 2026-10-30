import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class BrakeHplLcBotAdjust(AbstractHps.AbstractHpsAdjust)  :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始修改hpl_lc_bot")
        ascene = Jusme.ActiveUSScene
        model_name = Common.getModelName()

        #----------------获取全局坐标系原点origo的mark点
        origo=ascene.getObject(".{}.ground.origo".format(model_name))
        #-----------获取hpl_lc_bot
        hpl_lc_bot = ascene.getObject(self.hps_full_name)
        if not hpl_lc_bot :
            print("hpl_lc_bot")
            return

        #----------获取hpl_lc_top
        hpl_lc_top = ascene.getObject(".{}.ground.hpl_lc_top".format(model_name))
        if not hpl_lc_top :
            print("hpl_lc_top")
            return

        #----------获取hpl_uc_bot
        hpl_uc_bot = ascene.getObject(".{}.ground.hpl_uc_bot".format(model_name))
        if not hpl_uc_bot :
            print("hpl_uc_bot")
            return

        #----------获取hpl_uc_top
        hpl_uc_top = ascene.getObject(".{}.ground.hpl_uc_top".format(model_name))
        if not hpl_uc_top :
            print("hpl_uc_top")
            return

        #----------修改cfl_axial_reference
        cfl_axial_reference = ascene.getObject(".{}.ground.cfl_axial_reference".format(model_name))
        if not cfl_axial_reference :
            print("cfl_axial_reference")
            return
        cfl_axial_reference.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_lc_bot)
        cfl_axial_reference.orientation=VecUtils.ORI_ALONG_AXIS(hpl_lc_bot.location,hpl_uc_top.location,'z')

        #----------修改cfl_lta_lc_atch
        cfl_lta_lc_atch = ascene.getObject(".{}.ground.cfl_lta_lc_atch".format(model_name))
        if not cfl_lta_lc_atch :
            print("cfl_lta_lc_atch")
            return
        cfl_lta_lc_atch.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_lc_bot)
        cfl_lta_lc_atch.orientation=VecUtils.ORI_RELATIVE_TO([0,0,0],origo)

        #-------获取gel_upper_cylinder(part)
        gel_upper_cylinder = ascene.getObject(".{}.gel_upper_cylinder".format(model_name))
        if not gel_upper_cylinder :
            print("gel_upper_cylinder")
            return

        #-------修改gel_upper_cylinder.uel_gearaero_i_1
        uel_gearaero_i_1=ascene.getObject(".{}.gel_upper_cylinder.uel_gearaero_i_1".format(model_name))
        if not uel_gearaero_i_1 :
            return
        uel_gearaero_i_1.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_lc_top))
        uel_gearaero_i_1.orientation=Jusme.Vector(55.1145661544, 175.2828647294, 235.2057167569)
        loc_ori=VecUtils.global2local(gel_upper_cylinder.location,gel_upper_cylinder.orientation,uel_gearaero_i_1.location,uel_gearaero_i_1.orientation)
        uel_gearaero_i_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_gearaero_i_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #-------修改gel_lower_cylinder的相关内容

        #------获取gel_lower_cylinder
        gel_lower_cylinder = ascene.getObject(".{}.gel_lower_cylinder".format(model_name))
        if not gel_lower_cylinder :
            print("gel_lower_cylinder")
            return
        gel_lower_cylinder.location=0.5*(hpl_lc_bot.location+hpl_lc_top.location)
        #gel_lower_cylinder.orientation=VecUtils.ORI_ALONG_AXIS(hpl_lc_top.location,hpl_lc_bot.location,'z')

        #-------修改gel_lower_cylinder.gralin_14
        gralin_14=ascene.getObject(".{}.gel_lower_cylinder.gralin_14".format(model_name))
        if not gralin_14 :
            return
        gralin_14.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_lc_top))
        gralin_14.orientation=(VecUtils.ORI_ALONG_AXIS(hpl_lc_top.location,hpl_lc_bot.location,'z'))
        loc_ori=VecUtils.global2local(gel_lower_cylinder.location,gel_lower_cylinder.orientation,gralin_14.location,gralin_14.orientation)
        gralin_14.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_14.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #-------修改gel_lower_cylinder.gralin_lower_cylinder
        gralin_lower_cylinder=ascene.getObject(".{}.gel_lower_cylinder.gralin_lower_cylinder".format(model_name))
        if not gralin_lower_cylinder :
            return
        gralin_lower_cylinder.length=VecUtils.DM(hpl_lc_top.location,hpl_lc_bot.location)

        #-------修改gel_lower_cylinder.cm
        cm=ascene.getObject(".{}.gel_lower_cylinder.cm".format(model_name))
        if not cm :
            return
        cm.recompute()

        #-------修改gel_lower_cylinder.inertia_frame
        inertia_frame=ascene.getObject(".{}.gel_lower_cylinder.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location=VecUtils.LOC_RELATIVE_TO([0,0,0],cm)
        inertia_frame.orientation=VecUtils.ORI_RELATIVE_TO([0,0,0],gel_lower_cylinder)
        loc_ori=VecUtils.global2local(gel_lower_cylinder.location,gel_lower_cylinder.orientation,inertia_frame.location,inertia_frame.orientation)
        inertia_frame.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #-------修改gel_lower_cylinder.uel_stopper_i_1
        uel_stopper_i_1=ascene.getObject(".{}.gel_lower_cylinder.uel_stopper_i_1".format(model_name))
        if not uel_stopper_i_1 :
            return
        uel_stopper_i_1.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_lc_top)
        uel_stopper_i_1.orientation=Jusme.Vector(55.1145661544, 175.2828647294, 235.2057167569)
        loc_ori=VecUtils.global2local(gel_lower_cylinder.location,gel_lower_cylinder.orientation,uel_stopper_i_1.location,uel_stopper_i_1.orientation)
        uel_stopper_i_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_stopper_i_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #-------修改gel_lower_cylinder.uel_damper_i_1
        uel_damper_i_1=ascene.getObject(".{}.gel_lower_cylinder.uel_damper_i_1".format(model_name))
        if not uel_damper_i_1 :
            return
        uel_damper_i_1.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_lc_top)
        uel_damper_i_1.orientation=Jusme.Vector(55.1145661544, 175.2828647294, 235.2057167569)
        loc_ori=VecUtils.global2local(gel_lower_cylinder.location,gel_lower_cylinder.orientation,uel_damper_i_1.location,uel_damper_i_1.orientation)
        uel_damper_i_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_damper_i_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #-------修改gel_lower_cylinder.uel_spring_i_1
        uel_spring_i_1=ascene.getObject(".{}.gel_lower_cylinder.uel_spring_i_1".format(model_name))
        if not uel_spring_i_1 :
            return
        uel_spring_i_1.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_lc_top)
        uel_spring_i_1.orientation=Jusme.Vector(55.1145661544, 175.2828647294, 235.2057167569)
        loc_ori=VecUtils.global2local(gel_lower_cylinder.location,gel_lower_cylinder.orientation,uel_spring_i_1.location,uel_spring_i_1.orientation)
        uel_spring_i_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_spring_i_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #--------获取hpl_ib_axle
        hpl_ib_axle = ascene.getObject(".{}.ground.hpl_ib_axle".format(model_name))
        if not hpl_ib_axle :
            print("hpl_ib_axle")
            return

        #--------获取hpl_ob_axle
        hpl_ob_axle = ascene.getObject(".{}.ground.hpl_ob_axle".format(model_name))
        if not hpl_ob_axle :
            print("hpl_ob_axle")
            return

        #-----修改gel_lower_cylinder.gralin_22
        gralin_22=ascene.getObject(".{}.gel_lower_cylinder.gralin_22".format(model_name))
        if not gralin_22 :
            return
        gralin_22.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_ib_axle))
        gralin_22.orientation=(VecUtils.ORI_ALONG_AXIS(hpl_ib_axle.location,hpl_ob_axle.location,'z'))
        loc_ori=VecUtils.global2local(gel_lower_cylinder.location,gel_lower_cylinder.orientation,gralin_22.location,gralin_22.orientation)
        gralin_22.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_22.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #-------修改gel_lower_cylinder.gralin_geom
        gralin_geom=ascene.getObject(".{}.gel_lower_cylinder.gralin_geom".format(model_name))
        if not gralin_geom :
            return
        gralin_geom.length=VecUtils.DM(hpl_ib_axle.location,hpl_ob_axle.location)

        #--------获取hpl_wheel_center
        hpl_wheel_center = ascene.getObject(".{}.ground.hpl_wheel_center".format(model_name))
        if not hpl_wheel_center :
            print("hpl_wheel_center")
            return

        #--------获取cfl_spin_axis
        cfl_spin_axis = ascene.getObject(".{}.ground.cfl_spin_axis".format(model_name))
        if not cfl_spin_axis :
            print("cfl_spin_axis")
            return

        #------修改gel_lower_cylinder.MARKER_236
        MARKER_236=ascene.getObject(".{}.gel_lower_cylinder.MARKER_236".format(model_name))
        if not MARKER_236 :
            return
        MARKER_236.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_wheel_center))
        MARKER_236.orientation=Jusme.Vector(180,90,180)
        loc_ori=VecUtils.global2local(gel_lower_cylinder.location,gel_lower_cylinder.orientation,MARKER_236.location,MARKER_236.orientation)
        MARKER_236.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_236.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #------修改gel_lower_cylinder.coomarker_1
        coomarker_1=ascene.getObject(".{}.gel_lower_cylinder.coomarker_1".format(model_name))
        if not coomarker_1 :
            return
        coomarker_1.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],cfl_spin_axis))
        coomarker_1.orientation=(VecUtils.ORI_RELATIVE_TO([0,0,0],cfl_spin_axis))
        loc_ori=VecUtils.global2local(gel_lower_cylinder.location,gel_lower_cylinder.orientation,coomarker_1.location,coomarker_1.orientation)
        coomarker_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #------修改cfl_collar_top
        cfl_collar_top=ascene.getObject(".{}.ground.cfl_collar_top".format(model_name))
        if not cfl_collar_top :
            return
        cfl_collar_top.location=VecUtils.LOC_ALONG_LINE(hpl_uc_top.location,hpl_lc_bot.location,0.59*(VecUtils.DM(hpl_uc_top.location,hpl_lc_bot.location)))
        cfl_collar_top.orientation=VecUtils.ORI_ALONG_AXIS(hpl_uc_top.location,hpl_lc_bot.location,'z')

        #------修改cfl_collar_bot
        cfl_collar_bot=ascene.getObject(".{}.ground.cfl_collar_bot".format(model_name))
        if not cfl_collar_bot :
            return
        cfl_collar_bot.location=VecUtils.LOC_ALONG_LINE(hpl_uc_top.location,hpl_lc_bot.location,0.7*(VecUtils.DM(hpl_uc_top.location,hpl_lc_bot.location)))
        cfl_collar_bot.orientation=VecUtils.ORI_ALONG_AXIS(hpl_uc_top.location,hpl_lc_bot.location,'z')

        #--------修改gel_uc_collar的相关内容
        gel_uc_collar=ascene.getObject(".{}.gel_uc_collar".format(model_name))
        if not gel_uc_collar :
            return
        gel_uc_collar.location=0.5*(hpl_uc_bot.location+cfl_collar_top.location)
        gel_uc_collar.orientation=VecUtils.ORI_ALONG_AXIS(cfl_collar_top.location,cfl_collar_bot.location,'z')

        #--------修改gel_uc_collar.gralin_5
        gralin_5=ascene.getObject(".{}.gel_uc_collar.gralin_5".format(model_name))
        if not gralin_5 :
            return
        gralin_5.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],cfl_collar_top))
        gralin_5.orientation=(VecUtils.ORI_ALONG_AXIS(cfl_collar_top.location,cfl_collar_bot.location,'z'))
        loc_ori=VecUtils.global2local(gel_uc_collar.location,gel_uc_collar.orientation,gralin_5.location,gralin_5.orientation)
        gralin_5.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #------修改gel_uc_collar.gralin_uc_collar
        gralin_uc_collar=ascene.getObject(".{}.gel_uc_collar.gralin_uc_collar".format(model_name))
        if not gralin_uc_collar :
            return
        gralin_uc_collar.length=VecUtils.DM(hpl_uc_bot.location,cfl_collar_top.location)

        #------修改gel_uc_collar.cm
        cm=ascene.getObject(".{}.gel_uc_collar.cm".format(model_name))
        if not cm :
            return
        cm.recompute()

        #------修改gel_uc_collar.inertia_frame
        inertia_frame=ascene.getObject(".{}.gel_uc_collar.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],cm))
        inertia_frame.orientation=(VecUtils.ORI_RELATIVE_TO([0,0,0],gel_uc_collar))
        loc_ori=VecUtils.global2local(gel_uc_collar.location,gel_uc_collar.orientation,inertia_frame.location,inertia_frame.orientation)
        inertia_frame.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #------------joint:jolrev_ldb_collar
        jolrev_ldb_collar = ascene.getObject(".{}.jolrev_ldb_collar".format(model_name))
        if not jolrev_ldb_collar :
            return
        jolrev_ldb_collar.recompute()

        #------------joint:jolrev_collar_uc
        jolrev_collar_uc = ascene.getObject(".{}.jolrev_collar_uc".format(model_name))
        if not jolrev_collar_uc :
            return
        jolrev_collar_uc.recompute()

        #------------joint:jolrev_uta_collar
        jolrev_uta_collar = ascene.getObject(".{}.jolrev_uta_collar".format(model_name))
        if not jolrev_uta_collar :
            return
        jolrev_uta_collar.recompute()

        #------------joint:JOINT_57
        JOINT_57 = ascene.getObject(".{}.JOINT_57".format(model_name))
        if not JOINT_57 :
            return
        JOINT_57.recompute()

        #------------joint:jolcyl_lc_uc_joint
        jolcyl_lc_uc_joint = ascene.getObject(".{}.jolcyl_lc_uc_joint".format(model_name))
        if not jolcyl_lc_uc_joint :
            return
        jolcyl_lc_uc_joint.recompute()

        #------------joint:jolrev_lta_lc_joint
        jolrev_lta_lc_joint = ascene.getObject(".{}.jolrev_lta_lc_joint".format(model_name))
        if not jolrev_lta_lc_joint :
            return
        jolrev_lta_lc_joint.recompute()

        print("结束调整hpl_lc_bot")
        pass
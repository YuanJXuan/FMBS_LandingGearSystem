import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class BrakeHplUcTopAdjust(AbstractHps.AbstractHpsAdjust)  :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始修改hpl_uc_top")
        ascene = Jusme.ActiveUSScene
        model_name = Common.getModelName()

        #----------------获取全局坐标系原点origo的mark点
        origo=ascene.getObject(".{}.ground.origo".format(model_name))
        #-----------获取hpl_uc_top
        hpl_uc_top = ascene.getObject(self.hps_full_name)
        if not hpl_uc_top :
            print("未找到hpl_uc_top")
            return

        #----------获取hpl_lc_bot
        hpl_lc_bot = ascene.getObject(".{}.ground.hpl_lc_bot".format(model_name))
        if not hpl_lc_bot :
            print("hpl_lc_bot")
            return

        #----------获取hpl_uc_bot
        hpl_uc_bot = ascene.getObject(".{}.ground.hpl_uc_bot".format(model_name))
        if not hpl_uc_bot :
            print("hpl_uc_bot")
            return

        #----------修改.ground.cfl_axial_reference(marker)
        cfl_axial_reference=ascene.getObject(".{}.ground.cfl_axial_reference".format(model_name))
        if not cfl_axial_reference :
            return
        cfl_axial_reference.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_lc_bot))
        cfl_axial_reference.orientation=(VecUtils.ORI_ALONG_AXIS(hpl_lc_bot.location,hpl_uc_top.location,'z'))

        #-------修改cfl_uc_bot
        cfl_uc_bot=ascene.getObject(".{}.ground.cfl_uc_bot".format(model_name))
        if not cfl_uc_bot :
            return
        cfl_uc_bot.location=VecUtils.LOC_RELATIVE_TO([0,0,21.18],cfl_axial_reference)
        cfl_uc_bot.orientation=VecUtils.ORI_RELATIVE_TO([0,0,0],origo)

        #-------修改cfl_lc_top
        cfl_lc_top=ascene.getObject(".{}.ground.cfl_lc_top".format(model_name))
        if not cfl_lc_top :
            return
        cfl_lc_top.location=VecUtils.LOC_RELATIVE_TO([0,0,38.06],cfl_axial_reference)
        cfl_lc_top.orientation=VecUtils.ORI_RELATIVE_TO([0,0,0],origo)

        #-------修改cfl_uc_top
        cfl_uc_top=ascene.getObject(".{}.ground.cfl_uc_top".format(model_name))
        if not cfl_uc_top :
            return
        cfl_uc_top.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uc_top)
        cfl_uc_top.orientation=VecUtils.ORI_RELATIVE_TO([0,0,0],origo)

        #-------修改cfl_aero_ref
        cfl_aero_ref=ascene.getObject(".{}.ground.cfl_aero_ref".format(model_name))
        if not cfl_aero_ref :
            return
        cfl_aero_ref.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uc_top)
        cfl_aero_ref.orientation=VecUtils.ORI_RELATIVE_TO([0,0,0],origo)

        #-------修改uel_gearaero_rm_1
        uel_gearaero_rm_1=ascene.getObject(".{}.ground.uel_gearaero_rm_1".format(model_name))
        if not uel_gearaero_rm_1 :
            return
        uel_gearaero_rm_1.location=VecUtils.LOC_RELATIVE_TO([0,0,0],cfl_aero_ref)
        uel_gearaero_rm_1.orientation=VecUtils.ORI_RELATIVE_TO([0,0,0],cfl_aero_ref)

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

        #-------未修改.gel_uc_collar.jxl_joint_j_10


        #------修改gel_upper_cylinder的相关内容
        gel_upper_cylinder=ascene.getObject(".{}.gel_upper_cylinder".format(model_name))
        if not gel_upper_cylinder :
            return
        gel_upper_cylinder.location=0.5*(hpl_uc_top.location+hpl_uc_bot.location)
        gel_upper_cylinder.orientation=VecUtils.ORI_ALONG_AXIS(hpl_uc_top.location,hpl_uc_bot.location,'z')
        
        #--------修改gel_upper_cylinder.gralin_12
        gralin_12=ascene.getObject(".{}.gel_upper_cylinder.gralin_12".format(model_name))
        if not gralin_12 :
            return
        gralin_12.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uc_top))
        gralin_12.orientation=(VecUtils.ORI_ALONG_AXIS(hpl_uc_top.location,hpl_uc_bot.location,'z'))
        loc_ori=VecUtils.global2local(gel_upper_cylinder.location,gel_upper_cylinder.orientation,gralin_12.location,gralin_12.orientation)
        gralin_12.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_12.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #----------修改gel_upper_cylinder.gralin_upper_cylinder
        gralin_upper_cylinder=ascene.getObject(".{}.gel_upper_cylinder.gralin_upper_cylinder".format(model_name))
        if not gralin_upper_cylinder :
            return
        gralin_upper_cylinder.length=VecUtils.DM(hpl_uc_top.location,hpl_uc_bot.location)

        #------gel_upper_cylinder.cm
        cm=ascene.getObject(".{}.gel_upper_cylinder.cm".format(model_name))
        if not cm :
            return
        cm.recompute()

        #------修改gel_upper_cylinder.inertia_frame
        inertia_frame=ascene.getObject(".{}.gel_upper_cylinder.inertia_frame".format(model_name))
        if not inertia_frame :
            return
        inertia_frame.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],cm))
        inertia_frame.orientation=(VecUtils.ORI_RELATIVE_TO([0,0,0],gel_upper_cylinder))
        loc_ori=VecUtils.global2local(gel_upper_cylinder.location,gel_upper_cylinder.orientation,inertia_frame.location,inertia_frame.orientation)
        inertia_frame.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #------修改gel_upper_cylinder.MARKER_267
        MARKER_267=ascene.getObject(".{}.gel_upper_cylinder.MARKER_267".format(model_name))
        if not MARKER_267 :
            return
        MARKER_267.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uc_top))
        MARKER_267.orientation=Jusme.Vector(0, 0, 0)
        loc_ori=VecUtils.global2local(gel_upper_cylinder.location,gel_upper_cylinder.orientation,MARKER_267.location,MARKER_267.orientation)
        MARKER_267.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_267.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #------修改gel_upper_cylinder.uel_stopper_j_1
        uel_stopper_j_1=ascene.getObject(".{}.gel_upper_cylinder.uel_stopper_j_1".format(model_name))
        if not uel_stopper_j_1 :
            return
        uel_stopper_j_1.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uc_top))
        uel_stopper_j_1.orientation=Jusme.Vector(55.1145661544, 175.2828647294, 235.2057167569)
        loc_ori=VecUtils.global2local(gel_upper_cylinder.location,gel_upper_cylinder.orientation,uel_stopper_j_1.location,uel_stopper_j_1.orientation)
        uel_stopper_j_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_stopper_j_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #------修改gel_upper_cylinder.uel_damper_j_1
        uel_damper_j_1=ascene.getObject(".{}.gel_upper_cylinder.uel_damper_j_1".format(model_name))
        if not uel_damper_j_1 :
            return
        uel_damper_j_1.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uc_top))
        uel_damper_j_1.orientation=Jusme.Vector(55.1145661544, 175.2828647294, 235.2057167569)
        loc_ori=VecUtils.global2local(gel_upper_cylinder.location,gel_upper_cylinder.orientation,uel_damper_j_1.location,uel_damper_j_1.orientation)
        uel_damper_j_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_damper_j_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])

        #------修改gel_upper_cylinder.uel_spring_j_1
        uel_spring_j_1=ascene.getObject(".{}.gel_upper_cylinder.uel_spring_j_1".format(model_name))
        if not uel_spring_j_1 :
            return
        uel_spring_j_1.location=(VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_uc_top))
        uel_spring_j_1.orientation=Jusme.Vector(55.1145661544, 175.2828647294, 235.2057167569)
        loc_ori=VecUtils.global2local(gel_upper_cylinder.location,gel_upper_cylinder.orientation,uel_spring_j_1.location,uel_spring_j_1.orientation)
        uel_spring_j_1.location=(loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_spring_j_1.orientation=(loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


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

        #






        print("结束调整hpl_uc_top")
        pass
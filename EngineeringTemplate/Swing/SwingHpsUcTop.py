import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class SwingHpsUcTopAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始转弯仿真hps_uc_top硬点调整")

        ascene = Jusme.ActiveUSScene
        #---------------获取当前模型名称
        model_name = Common.getModelName()

        #----------------获取全局坐标系原点origo的mark点
        origo=ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            return

        #---------获取修改后的(hps)--------
        hps_uc_top = ascene.getObject(self.hps_full_name)
        if not hps_uc_top :
            return
        
        #-------获取hps_uc_bot
        hps_uc_bot=ascene.getObject(".{}.ground.hps_uc_bot".format(model_name))
        if not hps_uc_bot :
            return

        #-------获取hps_lc_top
        hps_lc_top=ascene.getObject(".{}.ground.hps_lc_top".format(model_name))
        if not hps_lc_top :
            return

        #-------获取hps_lc_bot
        hps_lc_bot=ascene.getObject(".{}.ground.hps_lc_bot".format(model_name))
        if not hps_lc_bot :
            return

        #-------获取cfs_collar_top
        cfs_collar_top=ascene.getObject(".{}.ground.cfs_collar_top".format(model_name))
        if not cfs_collar_top :
            return

        #-------获取hsg_1
        hsg_1=ascene.getObject(".{}.ground.hsg_1".format(model_name))
        if not hsg_1 :
            return

        

        #-------获取zdt_1
        zdt_1=ascene.getObject(".{}.ground.zdt_1".format(model_name))
        if not zdt_1 :
            return


        #-------获取hps_lta_lc_atch
        hps_lta_lc_atch=ascene.getObject(".{}.ground.hps_lta_lc_atch".format(model_name))
        if not hps_lta_lc_atch :
            return

        #-------获取hps_uta_uc_atch
        hps_uta_uc_atch=ascene.getObject(".{}.ground.hps_uta_uc_atch".format(model_name))
        if not hps_uta_uc_atch :
            return
        
        #-------获取hps_db_sf_atch
        hps_db_sf_atch=ascene.getObject(".{}.ground.hps_db_sf_atch".format(model_name))
        if not hps_db_sf_atch :
            return

        #-------获取hps_db_uc_atch
        hps_db_uc_atch=ascene.getObject(".{}.ground.hps_db_uc_atch".format(model_name))
        if not hps_db_uc_atch :
            return

        #-------获取hps_uc_sf_atch_l
        hps_uc_sf_atch_l=ascene.getObject(".{}.ground.hps_uc_sf_atch_l".format(model_name))
        if not hps_uc_sf_atch_l :
            return

        #-------获取hps_uc_sf_atch_r
        hps_uc_sf_atch_r=ascene.getObject(".{}.ground.hps_uc_sf_atch_r".format(model_name))
        if not hps_uc_sf_atch_r :
            return

        #-------获取hps_uc_geompt
        hps_uc_geompt=ascene.getObject(".{}.ground.hps_uc_geompt".format(model_name))
        if not hps_uc_geompt :
            return

        #-------获取hpr_wheel_center
        hpr_wheel_center=ascene.getObject(".{}.ground.hpr_wheel_center".format(model_name))
        if not hpr_wheel_center :
            return

        #-------获取hpl_wheel_center
        hpl_wheel_center=ascene.getObject(".{}.ground.hpl_wheel_center".format(model_name))
        if not hpl_wheel_center :
            return

        #-------获取hps_nlg_axle_lowpoint
        hps_nlg_axle_lowpoint=ascene.getObject(".{}.ground.hps_nlg_axle_lowpoint".format(model_name))
        if not hps_nlg_axle_lowpoint :
            return
        
        #-------获取cfs_nlg_axle_lowpoint
        cfs_nlg_axle_lowpoint=ascene.getObject(".{}.ground.cfs_nlg_axle_lowpoint".format(model_name))
        if not cfs_nlg_axle_lowpoint :
            return
        cfs_nlg_axle_lowpoint.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hps_nlg_axle_lowpoint)
        cfs_nlg_axle_lowpoint.orientation=VecUtils.ORI_RELATIVE_TO([0,0,0],origo)

        #-------获取cfs_wheel_centers_midpoint
        cfs_wheel_centers_midpoint=ascene.getObject(".{}.ground.cfs_wheel_centers_midpoint".format(model_name))
        if not cfs_wheel_centers_midpoint :
            return
        cfs_wheel_centers_midpoint.location=0.5*(hpl_wheel_center.location+hpr_wheel_center.location)
        cfs_wheel_centers_midpoint.orientation= Jusme.Vector(0,0,0)

        #------修改cfs_collar_top
        cfs_collar_top=ascene.getObject(".{}.ground.cfs_collar_top".format(model_name))
        if not cfs_collar_top :
            return
        cfs_collar_top.location=(VecUtils.LOC_ALONG_LINE(hps_uc_bot.location,hps_uc_top.location,0.11*(VecUtils.DM(hps_uc_bot.location,hps_uc_top.location))))
        cfs_collar_top.orientation=(VecUtils.ORI_ALONG_AXIS(hps_uc_bot.location,hps_uc_top.location,'z'))

        #-------修改ges_upper_cylinder
        ges_upper_cylinder=ascene.getObject(".{}.ges_upper_cylinder".format(model_name))
        if not ges_upper_cylinder :
            return
        ges_upper_cylinder.location=0.5 * (hps_uc_bot.location + hps_uc_top.location)
        ges_upper_cylinder.orientation=VecUtils.ORI_ALONG_AXIS(hps_uc_top.location, hps_uc_bot.location, 'z')

        #--------修改ges_upper_cylinder.gralin_2
        gralin_2 = ascene.getObject(".{}.ges_upper_cylinder.gralin_2".format(model_name))
        if not gralin_2 :
            return
        gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_top))
        gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(hps_uc_top.location,hps_uc_bot.location,'z'))
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, gralin_2.location, gralin_2.orientation)
        gralin_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改ges_upper_cylinder.gralin_3
        gralin_3 = ascene.getObject(".{}.ges_upper_cylinder.gralin_3".format(model_name))
        if not gralin_3 :
            return
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_sf_atch_l))
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(hps_uc_sf_atch_l.location,hps_uc_geompt.location,'z'))
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改ges_upper_cylinder.gralin_4
        gralin_4 = ascene.getObject(".{}.ges_upper_cylinder.gralin_4".format(model_name))
        if not gralin_4 :
            return
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_sf_atch_r))
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(hps_uc_sf_atch_r.location,hps_uc_geompt.location,'z'))
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------修改.ges_upper_cylinder.gralin_upper_cylinder_geom1
        gralin_upper_cylinder_geom1 = ascene.getObject(".{}.ges_upper_cylinder.gralin_upper_cylinder_geom1".format(model_name))
        if not gralin_upper_cylinder_geom1:
            return
        gralin_upper_cylinder_geom1.length = VecUtils.DM(hps_uc_top.location,hps_uc_bot.location)

        #------------修改.ges_upper_cylinder.gralin_upper_cylinder_geom2
        gralin_upper_cylinder_geom2 = ascene.getObject(".{}.ges_upper_cylinder.gralin_upper_cylinder_geom2".format(model_name))
        if not gralin_upper_cylinder_geom2:
            return
        gralin_upper_cylinder_geom2.length = VecUtils.DM(hps_uc_sf_atch_l.location,hps_uc_geompt.location)

        #------------修改.ges_upper_cylinder.gralin_upper_cylinder_geom3
        gralin_upper_cylinder_geom3 = ascene.getObject(".{}.ges_upper_cylinder.gralin_upper_cylinder_geom3".format(model_name))
        if not gralin_upper_cylinder_geom3:
            return
        gralin_upper_cylinder_geom3.length = VecUtils.DM(hps_uc_sf_atch_r.location,hps_uc_geompt.location)

        #------修改.ges_upper_cylinder.cm
        ges_upper_cylinder_cm=ascene.getObject(".{}.ges_upper_cylinder.cm".format(model_name))
        if not ges_upper_cylinder_cm:
            return
        ges_upper_cylinder_cm.recompute()

        #------修改.ges_upper_cylinder.inertia_frame
        inertia_frame=ascene.getObject(".{}.ges_upper_cylinder.inertia_frame".format(model_name))
        if not inertia_frame:
            return
        inertia_frame.location = VecUtils.LOC_RELATIVE_TO([0,0,0],ges_upper_cylinder_cm)
        inertia_frame.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],ges_upper_cylinder)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.jxs_joint_j_1
        jxs_joint_j_1=ascene.getObject(".{}.ges_upper_cylinder.jxs_joint_j_1".format(model_name))
        if not jxs_joint_j_1:
            return
        jxs_joint_j_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],cfs_collar_top)
        jxs_joint_j_1.orientation = VecUtils.ORI_ALONG_AXIS(hps_uc_bot.location,hps_uc_top.location,'z')
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
        jxs_joint_j_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        

        #-----获取ges_lower_cylinder
        ges_lower_cylinder=ascene.getObject(".{}.ges_lower_cylinder".format(model_name))
        if not ges_lower_cylinder:
            return
        ges_lower_cylinder.location=0.5*(hps_lc_top.location+hps_lc_bot.location)
        ges_lower_cylinder.orientation=VecUtils.ORI_ALONG_AXIS(hps_lc_top.location,hps_lc_bot.location,'z')

        #------ges_lower_cylinder.gralin_5
        gralin_5=ascene.getObject(".{}.ges_lower_cylinder.gralin_5".format(model_name))
        if not gralin_5:
            return
        gralin_5.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_top)
        gralin_5.orientation = VecUtils.ORI_ALONG_AXIS(hps_lc_top.location,hps_lc_bot.location,'z')
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------ges_lower_cylinder.gralin_7
        gralin_7=ascene.getObject(".{}.ges_lower_cylinder.gralin_7".format(model_name))
        if not gralin_7:
            return
        gralin_7.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_wheel_center)
        gralin_7.orientation = VecUtils.ORI_ALONG_AXIS(hpr_wheel_center.location,hpl_wheel_center.location,'z')
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------修改.ges_lower_cylinder.gralin_geom1
        gralin_geom1 = ascene.getObject(".{}.ges_lower_cylinder.gralin_geom1".format(model_name))
        if not gralin_geom1:
            return
        gralin_geom1.length = VecUtils.DM(hps_lc_top.location,hps_lc_bot.location)

        #------------修改.ges_lower_cylinder.gralin_geom2
        gralin_geom2 = ascene.getObject(".{}.ges_lower_cylinder.gralin_geom2".format(model_name))
        if not gralin_geom2:
            return
        gralin_geom2.length = VecUtils.DM(hpr_wheel_center.location,hpl_wheel_center.location)


        #------修改.ges_lower_cylinder.cm
        ges_lower_cylinder_cm=ascene.getObject(".{}.ges_lower_cylinder.cm".format(model_name))
        if not ges_lower_cylinder_cm:
            return
        ges_lower_cylinder_cm.recompute()

        #------修改.ges_upper_cylinder.inertia_frame
        inertia_frame=ascene.getObject(".{}.ges_lower_cylinder.inertia_frame".format(model_name))
        if not inertia_frame:
            return
        inertia_frame.location = VecUtils.LOC_RELATIVE_TO([0,0,0],ges_lower_cylinder_cm)
        inertia_frame.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],ges_lower_cylinder)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])














        #-----获取ges_collar
        ges_collar=ascene.getObject(".{}.ges_collar".format(model_name))
        if not ges_collar:
            return
        ges_collar.location=0.5*(hps_uc_bot.location+cfs_collar_top.location)
        ges_collar.orientation=VecUtils.ORI_ALONG_AXIS(hps_uc_bot.location,cfs_collar_top.location,'z')

        #------修改ges_collar.gralin_collar
        gralin_collar = ascene.getObject(".{}.ges_collar.gralin_collar".format(model_name))
        if not gralin_collar:
            return
        gralin_collar.length = VecUtils.DM(hps_uc_bot.location,cfs_collar_top.location)

        #------修改ges_collar.gralin_24
        gralin_24=ascene.getObject(".{}.ges_collar.gralin_24".format(model_name))
        if not gralin_24:
            return
        gralin_24.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_uc_bot)
        gralin_24.orientation = VecUtils.ORI_ALONG_AXIS(hps_uc_bot.location,cfs_collar_top.location,'z')
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        

        #-------修改ges_collar.cm
        ges_collar_cm=ascene.getObject(".{}.ges_collar.cm".format(model_name))
        if not ges_collar_cm:
            return
        ges_collar_cm.recompute()

        #-------修改ges_collar.inertia_frame
        inertia_frame=ascene.getObject(".{}.ges_collar.inertia_frame".format(model_name))
        if not inertia_frame:
            return
        inertia_frame.location=VecUtils.LOC_RELATIVE_TO([0,0,0],ges_collar_cm)
        inertia_frame.orientation=VecUtils.ORI_RELATIVE_TO([0,0,0],ges_collar)

        #------修改ges_collar.jxs_joint_i_1
        jxs_joint_i_1=ascene.getObject(".{}.ges_collar.jxs_joint_i_1".format(model_name))
        if not jxs_joint_i_1:
            return
        jxs_joint_i_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_j_1)
        jxs_joint_i_1.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxs_joint_j_1)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
        jxs_joint_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.ues_actuator_j_1
        ues_actuator_j_1=ascene.getObject(".{}.ges_upper_cylinder.ues_actuator_j_1".format(model_name))
        if not ues_actuator_j_1:
            return
        ues_actuator_j_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_j_1)
        ues_actuator_j_1.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxs_joint_j_1)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, ues_actuator_j_1.location, ues_actuator_j_1.orientation)
        ues_actuator_j_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_actuator_j_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.ues_actuator_j_4
        ues_actuator_j_4=ascene.getObject(".{}.ges_upper_cylinder.ues_actuator_j_4".format(model_name))
        if not ues_actuator_j_4:
            return
        ues_actuator_j_4.location = VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_j_1)
        ues_actuator_j_4.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxs_joint_j_1)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, ues_actuator_j_4.location, ues_actuator_j_4.orientation)
        ues_actuator_j_4.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_actuator_j_4.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_collar.ues_actuator_i_1
        ues_actuator_i_1=ascene.getObject(".{}.ges_collar.ues_actuator_i_1".format(model_name))
        if not ues_actuator_i_1:
            return
        ues_actuator_i_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_i_1)
        ues_actuator_i_1.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxs_joint_i_1)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, ues_actuator_i_1.location, ues_actuator_i_1.orientation)
        ues_actuator_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_actuator_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_collar.ues_actuator_i_4
        ues_actuator_i_4=ascene.getObject(".{}.ges_collar.ues_actuator_i_4".format(model_name))
        if not ues_actuator_i_4:
            return
        ues_actuator_i_4.location = VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_i_1)
        ues_actuator_i_4.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxs_joint_i_1)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, ues_actuator_i_4.location, ues_actuator_i_4.orientation)
        ues_actuator_i_4.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_actuator_i_4.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------------------修改ges_collar中的其他marker点--------------------------

        

        #------修改ges_collar.MARKER_181
        MARKER_181=ascene.getObject(".{}.ges_collar.MARKER_181".format(model_name))
        if not MARKER_181:
            return
        MARKER_181.location = VecUtils.LOC_RELATIVE_TO([0,0,0],ges_collar_cm)
        MARKER_181.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, MARKER_181.location, MARKER_181.orientation)
        MARKER_181.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_181.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_collar.MARKER_179
        MARKER_179=ascene.getObject(".{}.ges_collar.MARKER_179".format(model_name))
        if not MARKER_179:
            return
        MARKER_179.location = VecUtils.LOC_RELATIVE_TO([0,0,0],cfs_collar_top)
        MARKER_179.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, MARKER_179.location, MARKER_179.orientation)
        MARKER_179.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_179.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_collar.MARKER_177
        MARKER_177=ascene.getObject(".{}.ges_collar.MARKER_177".format(model_name))
        if not MARKER_177:
            return
        MARKER_177.location = VecUtils.LOC_RELATIVE_TO([0,0,0],cfs_collar_top)
        MARKER_177.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, MARKER_177.location, MARKER_177.orientation)
        MARKER_177.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_177.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_collar.MARKER_75
        MARKER_75=ascene.getObject(".{}.ges_collar.MARKER_75".format(model_name))
        if not MARKER_75:
            return
        MARKER_75.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hsg_1)
        MARKER_75.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, MARKER_75.location, MARKER_75.orientation)
        MARKER_75.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_75.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_collar.jxs_joint_j_10
        jxs_joint_j_10=ascene.getObject(".{}.ges_collar.jxs_joint_j_10".format(model_name))
        if not jxs_joint_j_10:
            return
        jxs_joint_j_10.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_uta_uc_atch)
        jxs_joint_j_10.orientation = VecUtils.ORI_RELATIVE_TO([0,90,0],origo)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
        jxs_joint_j_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        

        #---------------------修改ges_upper_cylinder中的其他marker点--------------------------

        #------修改ges_upper_cylinder.MARKER_182
        MARKER_182=ascene.getObject(".{}.ges_upper_cylinder.MARKER_182".format(model_name))
        if not MARKER_182:
            return
        MARKER_182.location = VecUtils.LOC_RELATIVE_TO([0,0,0],ges_collar_cm)
        MARKER_182.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_182.location, MARKER_182.orientation)
        MARKER_182.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_182.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.MARKER_163
        MARKER_163=ascene.getObject(".{}.ges_upper_cylinder.MARKER_163".format(model_name))
        if not MARKER_163:
            return
        MARKER_163.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_uc_top)
        MARKER_163.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_163.location, MARKER_163.orientation)
        MARKER_163.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_163.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.MARKER_126
        MARKER_126=ascene.getObject(".{}.ges_upper_cylinder.MARKER_126".format(model_name))
        if not MARKER_126:
            return
        MARKER_126.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_uc_top)
        MARKER_126.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_126.location, MARKER_126.orientation)
        MARKER_126.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_126.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.MARKER_124
        MARKER_124=ascene.getObject(".{}.ges_upper_cylinder.MARKER_124".format(model_name))
        if not MARKER_124:
            return
        MARKER_124.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_uc_top)
        MARKER_124.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_124.location, MARKER_124.orientation)
        MARKER_124.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_124.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.MARKER_123
        MARKER_123=ascene.getObject(".{}.ges_upper_cylinder.MARKER_123".format(model_name))
        if not MARKER_123:
            return
        MARKER_123.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_uc_top)
        MARKER_123.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_123.location, MARKER_123.orientation)
        MARKER_123.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_123.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.MARKER_180
        MARKER_180=ascene.getObject(".{}.ges_upper_cylinder.MARKER_180".format(model_name))
        if not MARKER_180:
            return
        MARKER_180.location = VecUtils.LOC_RELATIVE_TO([0,0,0],cfs_collar_top)
        MARKER_180.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_180.location, MARKER_180.orientation)
        MARKER_180.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_180.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.MARKER_178
        MARKER_178=ascene.getObject(".{}.ges_upper_cylinder.MARKER_178".format(model_name))
        if not MARKER_178:
            return
        MARKER_178.location = VecUtils.LOC_RELATIVE_TO([0,0,0],cfs_collar_top)
        MARKER_178.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_178.location, MARKER_178.orientation)
        MARKER_178.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_178.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----获取js.cm
        js_cm=ascene.getObject(".{}.js.cm".format(model_name))
        if not js_cm:
            return
        
        #------修改ges_upper_cylinder.MARKER_119
        MARKER_119=ascene.getObject(".{}.ges_upper_cylinder.MARKER_119".format(model_name))
        if not MARKER_119:
            return
        MARKER_119.location = VecUtils.LOC_RELATIVE_TO([0,0,0],js_cm)
        MARKER_119.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_119.location, MARKER_119.orientation)
        MARKER_119.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_119.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
    
        #------修改ges_upper_cylinder.MARKER_77
        MARKER_77=ascene.getObject(".{}.ges_upper_cylinder.MARKER_77".format(model_name))
        if not MARKER_77:
            return
        MARKER_77.location = VecUtils.LOC_RELATIVE_TO([0,0,0],zdt_1)
        MARKER_77.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_77.location, MARKER_77.orientation)
        MARKER_77.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_77.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.ues_stopper_j_1
        ues_stopper_j_1=ascene.getObject(".{}.ges_upper_cylinder.ues_stopper_j_1".format(model_name))
        if not ues_stopper_j_1:
            return
        ues_stopper_j_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_uc_top)
        ues_stopper_j_1.orientation = Jusme.Vector(180,180,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, ues_stopper_j_1.location, ues_stopper_j_1.orientation)
        ues_stopper_j_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_stopper_j_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.ues_damper_j_1
        ues_damper_j_1=ascene.getObject(".{}.ges_upper_cylinder.ues_damper_j_1".format(model_name))
        if not ues_damper_j_1:
            return
        ues_damper_j_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_uc_top)
        ues_damper_j_1.orientation = Jusme.Vector(180,180,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, ues_damper_j_1.location, ues_damper_j_1.orientation)
        ues_damper_j_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_damper_j_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.ues_spring_j_1
        ues_spring_j_1=ascene.getObject(".{}.ges_upper_cylinder.ues_spring_j_1".format(model_name))
        if not ues_spring_j_1:
            return
        ues_spring_j_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_uc_top)
        ues_spring_j_1.orientation = Jusme.Vector(180,180,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, ues_spring_j_1.location, ues_spring_j_1.orientation)
        ues_spring_j_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_spring_j_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.jxs_joint_j_12
        jxs_joint_j_12=ascene.getObject(".{}.ges_upper_cylinder.jxs_joint_j_12".format(model_name))
        if not jxs_joint_j_12:
            return
        jxs_joint_j_12.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_db_uc_atch)
        jxs_joint_j_12.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],origo)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_j_12.location, jxs_joint_j_12.orientation)
        jxs_joint_j_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----获取ges_subframe
        ges_subframe=ascene.getObject(".{}.ges_subframe".format(model_name))
        if not ges_subframe:
            return

        #------修改ges_subframe.jxs_joint_j_15
        jxs_joint_j_15=ascene.getObject(".{}.ges_subframe.jxs_joint_j_15".format(model_name))
        if not jxs_joint_j_15:
            return
        jxs_joint_j_15.location = 0.5*(hps_uc_sf_atch_l.location+hps_uc_sf_atch_r.location)
        jxs_joint_j_15.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_subframe.location, ges_subframe.orientation, jxs_joint_j_15.location, jxs_joint_j_15.orientation)
        jxs_joint_j_15.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_15.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_upper_cylinder.jxs_joint_i_15
        jxs_joint_i_15=ascene.getObject(".{}.ges_upper_cylinder.jxs_joint_i_15".format(model_name))
        if not jxs_joint_i_15:
            return
        jxs_joint_i_15.location = VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_j_15)
        jxs_joint_i_15.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxs_joint_j_15)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_i_15.location, jxs_joint_i_15.orientation)
        jxs_joint_i_15.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_15.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #------修改ges_upper_cylinder.jxs_joint_j_11
        jxs_joint_j_11=ascene.getObject(".{}.ges_upper_cylinder.jxs_joint_j_11".format(model_name))
        if not jxs_joint_j_11:
            return
        jxs_joint_j_11.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_top)
        jxs_joint_j_11.orientation = Jusme.Vector(180,180,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_j_11.location, jxs_joint_j_11.orientation)
        jxs_joint_j_11.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_11.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        



        #---------------------修改ges_lower_cylinder中的其他marker点--------------------------

        #------修改ges_lower_cylinder.MARKER_176
        MARKER_176=ascene.getObject(".{}.ges_lower_cylinder.MARKER_176".format(model_name))
        if not MARKER_176:
            return
        MARKER_176.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_bot)
        MARKER_176.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_176.location, MARKER_176.orientation)
        MARKER_176.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_176.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.MARKER_175
        MARKER_175=ascene.getObject(".{}.ges_lower_cylinder.MARKER_175".format(model_name))
        if not MARKER_175:
            return
        MARKER_175.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_bot)
        MARKER_175.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_175.location, MARKER_175.orientation)
        MARKER_175.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_175.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.MARKER_164
        MARKER_164=ascene.getObject(".{}.ges_lower_cylinder.MARKER_164".format(model_name))
        if not MARKER_164:
            return
        MARKER_164.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_top)
        MARKER_164.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_164.location, MARKER_164.orientation)
        MARKER_164.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_164.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.MARKER_127
        MARKER_127=ascene.getObject(".{}.ges_lower_cylinder.MARKER_127".format(model_name))
        if not MARKER_127:
            return
        MARKER_127.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_top)
        MARKER_127.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_127.location, MARKER_127.orientation)
        MARKER_127.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_127.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.MARKER_125
        MARKER_125=ascene.getObject(".{}.ges_lower_cylinder.MARKER_125".format(model_name))
        if not MARKER_125:
            return
        MARKER_125.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_top)
        MARKER_125.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_125.location, MARKER_125.orientation)
        MARKER_125.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_125.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.MARKER_122
        MARKER_122=ascene.getObject(".{}.ges_lower_cylinder.MARKER_122".format(model_name))
        if not MARKER_122:
            return
        MARKER_122.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_top)
        MARKER_122.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_122.location, MARKER_122.orientation)
        MARKER_122.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_122.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.MARKER_160
        MARKER_160=ascene.getObject(".{}.ges_lower_cylinder.MARKER_160".format(model_name))
        if not MARKER_160:
            return
        MARKER_160.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_wheel_center)
        MARKER_160.orientation = Jusme.Vector(0,90,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_160.location, MARKER_160.orientation)
        MARKER_160.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_160.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.MARKER_158
        MARKER_158=ascene.getObject(".{}.ges_lower_cylinder.MARKER_158".format(model_name))
        if not MARKER_158:
            return
        MARKER_158.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hpl_wheel_center)
        MARKER_158.orientation = Jusme.Vector(0,90,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_158.location, MARKER_158.orientation)
        MARKER_158.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_158.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.coomarker_3
        coomarker_3=ascene.getObject(".{}.ges_lower_cylinder.coomarker_3".format(model_name))
        if not coomarker_3:
            return
        coomarker_3.location = VecUtils.LOC_RELATIVE_TO([0,0,0],cfs_nlg_axle_lowpoint)
        coomarker_3.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],cfs_nlg_axle_lowpoint)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, coomarker_3.location, coomarker_3.orientation)
        coomarker_3.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        coomarker_3.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.coomarker_2
        coomarker_2=ascene.getObject(".{}.ges_lower_cylinder.coomarker_2".format(model_name))
        if not coomarker_2:
            return
        coomarker_2.location = VecUtils.LOC_RELATIVE_TO([0,0,0],cfs_wheel_centers_midpoint)
        coomarker_2.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],cfs_wheel_centers_midpoint)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, coomarker_2.location, coomarker_2.orientation)
        coomarker_2.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        coomarker_2.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.ues_stopper_i_1
        ues_stopper_i_1=ascene.getObject(".{}.ges_lower_cylinder.ues_stopper_i_1".format(model_name))
        if not ues_stopper_i_1:
            return
        ues_stopper_i_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_top)
        ues_stopper_i_1.orientation = Jusme.Vector(180,180,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, ues_stopper_i_1.location, ues_stopper_i_1.orientation)
        ues_stopper_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_stopper_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.ues_damper_i_1
        ues_damper_i_1=ascene.getObject(".{}.ges_lower_cylinder.ues_damper_i_1".format(model_name))
        if not ues_damper_i_1:
            return
        ues_damper_i_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_top)
        ues_damper_i_1.orientation = Jusme.Vector(180,180,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, ues_damper_i_1.location, ues_damper_i_1.orientation)
        ues_damper_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_damper_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.ues_spring_i_1
        ues_spring_i_1=ascene.getObject(".{}.ges_lower_cylinder.ues_spring_i_1".format(model_name))
        if not ues_spring_i_1:
            return
        ues_spring_i_1.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lc_top)
        ues_spring_i_1.orientation = Jusme.Vector(180,180,0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, ues_spring_i_1.location, ues_spring_i_1.orientation)
        ues_spring_i_1.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        ues_spring_i_1.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.jxs_joint_i_11
        jxs_joint_i_11=ascene.getObject(".{}.ges_lower_cylinder.jxs_joint_i_11".format(model_name))
        if not jxs_joint_j_11:
            return
        jxs_joint_i_11.location = VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_j_11)
        jxs_joint_i_11.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxs_joint_j_11)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
        jxs_joint_i_11.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_11.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改ges_lower_cylinder.jxs_joint_j_9
        jxs_joint_j_9=ascene.getObject(".{}.ges_lower_cylinder.jxs_joint_j_9".format(model_name))
        if not jxs_joint_j_9:
            return
        jxs_joint_j_9.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hps_lta_lc_atch)
        jxs_joint_j_9.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],origo)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, jxs_joint_j_9.location, jxs_joint_j_9.orientation)
        jxs_joint_j_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----获取ges_lower_torque_arm
        ges_lower_torque_arm=ascene.getObject(".{}.ges_lower_torque_arm".format(model_name))
        if not ges_lower_torque_arm:
            return

        #------修改ges_lower_torque_arm.jxs_joint_i_9
        jxs_joint_i_9=ascene.getObject(".{}.ges_lower_torque_arm.jxs_joint_i_9".format(model_name))
        if not jxs_joint_i_9:
            return
        jxs_joint_i_9.location = VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_j_9)
        jxs_joint_i_9.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxs_joint_j_9)
        loc_ori = VecUtils.global2local(ges_lower_torque_arm.location, ges_lower_torque_arm.orientation, jxs_joint_i_9.location, jxs_joint_i_9.orientation)
        jxs_joint_i_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----获取ges_dragbrace
        ges_dragbrace=ascene.getObject(".{}.ges_dragbrace".format(model_name))
        if not ges_dragbrace:
            return

        #------修改ges_dragbrace.jxs_joint_i_12
        jxs_joint_i_12=ascene.getObject(".{}.ges_dragbrace.jxs_joint_i_12".format(model_name))
        if not jxs_joint_i_12:
            return
        jxs_joint_i_12.location = VecUtils.LOC_RELATIVE_TO([0,0,0],jxs_joint_j_12)
        jxs_joint_i_12.orientation = VecUtils.ORI_RELATIVE_TO([0,0,0],jxs_joint_j_12)
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, jxs_joint_i_12.location, jxs_joint_i_12.orientation)
        jxs_joint_i_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #------------------------.js_wt
        js_wt = ascene.getObject(".{}.js_wt".format(model_name))
        if not js_wt :
            print("1")
            return
        js_wt.recompute()
        
        #------------------------.zdt_upcylinder
        zdt_upcylinder = ascene.getObject(".{}.zdt_upcylinder".format(model_name))
        if not zdt_upcylinder :
            print("2")
            return
        zdt_upcylinder.recompute()

        #------------------------.hsg_collar
        hsg_collar = ascene.getObject(".{}.hsg_collar".format(model_name))
        if not hsg_collar :
            print("3")
            return
        hsg_collar.recompute()

        #------------------------.josrev_collar_uc_joint
        josrev_collar_uc_joint = ascene.getObject(".{}.josrev_collar_uc_joint".format(model_name))
        if not josrev_collar_uc_joint :
            print("4")
            return
        josrev_collar_uc_joint.recompute()

        #------------------------.josrev_uc_sf_joint
        josrev_uc_sf_joint = ascene.getObject(".{}.josrev_uc_sf_joint".format(model_name))
        if not josrev_uc_sf_joint :
            print("5")
            return
        josrev_uc_sf_joint.recompute()

        #------------------------.jossph_db_uc_joint
        jossph_db_uc_joint = ascene.getObject(".{}.jossph_db_uc_joint".format(model_name))
        if not jossph_db_uc_joint :
            print("6")
            return
        jossph_db_uc_joint.recompute()

        #------------------------.joscyl_lc_uc_joint
        joscyl_lc_uc_joint = ascene.getObject(".{}.joscyl_lc_uc_joint".format(model_name))
        if not joscyl_lc_uc_joint :
            print("7")
            return
        joscyl_lc_uc_joint.recompute()

        #------------------------.josrev_uta_uc_joint
        josrev_uta_uc_joint = ascene.getObject(".{}.josrev_uta_uc_joint".format(model_name))
        if not josrev_uta_uc_joint :
            print("8")
            return
        josrev_uta_uc_joint.recompute()

        #------------------------.MOTION_4
        MOTION_4 = ascene.getObject(".{}.MOTION_4".format(model_name))
        if not MOTION_4 :
            print("8")
            return
        MOTION_4.recompute()

        #------------------------.jiaodu
        jiaodu = ascene.getObject(".{}.jiaodu".format(model_name))
        if not jiaodu :
            print("8")
            return
        jiaodu.recompute()

        #------------------------.hcq_sd
        hcq_sd = ascene.getObject(".{}.hcq_sd".format(model_name))
        if not hcq_sd :
            print("8")
            return
        hcq_sd.recompute()

        #------------------------.jsd
        jsd = ascene.getObject(".{}.jsd".format(model_name))
        if not jsd :
            print("8")
            return
        jsd.recompute()

        



        print("结束调整hps_uc_top")




        pass
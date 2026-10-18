import Jusme
from Jusme import Base
from Fmbs.import_all_node import MakeSceneNodeByType
import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils

import Common
import DesignVariable
import AbstractAssembly

class RetractAssembly(AbstractAssembly.AbstractAssembly) :
    def __init__(self, var : DesignVariable.Variable) -> None:
        super().__init__(var)
        pass

    def InitDesignVariables(self) :
        print("进入收放写设计变量程序")
        model_name = Common.getModelName()
        #----------先创建工况需要的设计变量----------------------
        MLG_ret_disp = MakeSceneNodeByType('DesignVariable', '.{}.MLG_ret_disp'.format(model_name))
        MLG_ret_disp.variable_name = '.{}.MLG_ret_disp'.format(model_name)
        MLG_ret_disp.value_type_opt = 0
        MLG_ret_disp.real_value = 343
        MLG_ret_disp.delta_type = 1
        MLG_ret_disp.use_range = True
        MLG_ret_disp.range = [-1,1]

        NLG_ret_disp = MakeSceneNodeByType('DesignVariable', '.{}.NLG_ret_disp'.format(model_name))
        NLG_ret_disp.variable_name = '.{}.NLG_ret_disp'.format(model_name)
        NLG_ret_disp.value_type_opt = 0
        NLG_ret_disp.real_value = 635
        NLG_ret_disp.delta_type = 1
        NLG_ret_disp.use_range = True
        NLG_ret_disp.range = [-1,1]

        C0_MLG = MakeSceneNodeByType('DesignVariable', '.{}.C0_MLG'.format(model_name))
        C0_MLG.variable_name = '.{}.C0_MLG'.format(model_name)
        C0_MLG.value_type_opt = 0
        C0_MLG.real_value = 0.7
        C0_MLG.delta_type = 1
        C0_MLG.use_range = True
        C0_MLG.range = [-1,1]

        pa_MLG = MakeSceneNodeByType('DesignVariable', '.{}.pa_MLG'.format(model_name))
        pa_MLG.variable_name = '.{}.pa_MLG'.format(model_name)
        pa_MLG.value_type_opt = 0
        pa_MLG.real_value = 0.417
        pa_MLG.delta_type = 1
        pa_MLG.use_range = True
        pa_MLG.range = [-1,1]

        mlg_down_time = MakeSceneNodeByType('DesignVariable', '.{}.mlg_down_time'.format(model_name))
        mlg_down_time.variable_name = '.{}.mlg_down_time'.format(model_name)
        mlg_down_time.value_type_opt = 0
        mlg_down_time.real_value = 5
        mlg_down_time.delta_type = 1
        mlg_down_time.use_range = True
        mlg_down_time.range = [-1,1]

        mlg_hold_time = MakeSceneNodeByType('DesignVariable', '.{}.mlg_hold_time'.format(model_name))
        mlg_hold_time.variable_name = '.{}.mlg_hold_time'.format(model_name)
        mlg_hold_time.value_type_opt = 0
        mlg_hold_time.real_value = 1
        mlg_hold_time.delta_type = 1
        mlg_hold_time.use_range = True
        mlg_hold_time.range = [-1,1]

        mlg_up_time = MakeSceneNodeByType('DesignVariable', '.{}.mlg_up_time'.format(model_name))
        mlg_up_time.variable_name = '.{}.mlg_up_time'.format(model_name)
        mlg_up_time.value_type_opt = 0
        mlg_up_time.real_value = 4.5
        mlg_up_time.delta_type = 1
        mlg_up_time.use_range = True
        mlg_up_time.range = [-1,1]

        nlg_down_time = MakeSceneNodeByType('DesignVariable', '.{}.nlg_down_time'.format(model_name))
        nlg_down_time.variable_name = '.{}.nlg_down_time'.format(model_name)
        nlg_down_time.value_type_opt = 0
        nlg_down_time.real_value = 5
        nlg_down_time.delta_type = 1
        nlg_down_time.use_range = True
        nlg_down_time.range = [-1,1]

        nlg_hold_time = MakeSceneNodeByType('DesignVariable', '.{}.nlg_hold_time'.format(model_name))
        nlg_hold_time.variable_name = '.{}.nlg_hold_time'.format(model_name)
        nlg_hold_time.value_type_opt = 0
        nlg_hold_time.real_value = 1
        nlg_hold_time.delta_type = 1
        nlg_hold_time.use_range = True
        nlg_hold_time.range = [-1,1]

        nlg_up_time = MakeSceneNodeByType('DesignVariable', '.{}.nlg_up_time'.format(model_name))
        nlg_up_time.variable_name = '.{}.nlg_up_time'.format(model_name)
        nlg_up_time.value_type_opt = 0
        nlg_up_time.real_value = 4.5
        nlg_up_time.delta_type = 1
        nlg_up_time.use_range = True
        nlg_up_time.range = [-1,1]

        zdt_down = MakeSceneNodeByType('DesignVariable', '.{}.zdt_down'.format(model_name))
        zdt_down.variable_name = '.{}.zdt_down'.format(model_name)
        zdt_down.value_type_opt = 0
        zdt_down.real_value = 1000
        zdt_down.delta_type = 1
        zdt_down.use_range = True
        zdt_down.range = [-1,1]

        zdt_up = MakeSceneNodeByType('DesignVariable', '.{}.zdt_up'.format(model_name))
        zdt_up.variable_name = '.{}.zdt_up'.format(model_name)
        zdt_up.value_type_opt = 0
        zdt_up.real_value = 3.52E+04
        zdt_up.delta_type = 1
        zdt_up.use_range = True
        zdt_up.range = [-1,1]

        pa = MakeSceneNodeByType('DesignVariable', '.{}.pa'.format(model_name))
        pa.variable_name = '.{}.pa'.format(model_name)
        pa.value_type_opt = 0
        pa.real_value = 0.3077
        pa.delta_type = 1
        pa.use_range = True
        pa.range = [-1,1]

        C0 = MakeSceneNodeByType('DesignVariable', '.{}.C0'.format(model_name))
        C0.variable_name = '.{}.C0'.format(model_name)
        C0.value_type_opt = 0
        C0.real_value = 0.7
        C0.delta_type = 1
        C0.use_range = True
        C0.range = [-1,1]

        mi_du = MakeSceneNodeByType('DesignVariable', '.{}.mi_du'.format(model_name))
        mi_du.variable_name = '.{}.mi_du'.format(model_name)
        mi_du.value_type_opt = 0
        mi_du.real_value = 1
        mi_du.delta_type = 1
        mi_du.use_range = True
        mi_du.range = [-1,1]

        windV = MakeSceneNodeByType('DesignVariable', '.{}.windV'.format(model_name))
        windV.variable_name = '.{}.windV'.format(model_name)
        windV.value_type_opt = 0
        windV.real_value = 35
        windV.delta_type = 1
        windV.use_range = True
        windV.range = [-1,1]
        pass

    def InitElement(self) :
        print("进入收放写单元程序")
        model_name = Common.getModelName()
        #-----------------------------添加单元-------------------------
        SPLINE_angle_aeroforce_NLG = MakeSceneNodeByType('Spline', '.{}.SPLINE_angle_aeroforce_NLG'.format(model_name))
        SPLINE_angle_aeroforce_NLG.linear_extrapolate = False
        SPLINE_angle_aeroforce_NLG.input_method_opt = 1
        SPLINE_angle_aeroforce_NLG.x = [-20.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
        SPLINE_angle_aeroforce_NLG.y =[90000.0, 90000.0, 90000.0, 80000.0, 70000.0, 60000.0, 50000.0, 40000.0, 30000.0, 20000.0, 10000.0, 0.0, 0.0]
        
        SPLINE_angle_aeroforce_MLG = MakeSceneNodeByType('Spline', '.{}.SPLINE_angle_aeroforce_MLG'.format(model_name))
        SPLINE_angle_aeroforce_MLG.linear_extrapolate = False
        SPLINE_angle_aeroforce_MLG.input_method_opt = 1
        SPLINE_angle_aeroforce_MLG.x = [-20.0, -10.0, 0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0]
        SPLINE_angle_aeroforce_MLG.y =[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        pass

    def InitMarker(self) :
        print("进入收放写Marker点程序")
        
        
        pass

    def InitForce(self) :
        print("进入收放写载荷程序")
        model_name = Common.getModelName()
        #--------创建工况需要的载荷-------------
        #--------创建载荷前需添加载荷需要的marker点---
        
        
        MARKER_611 = MakeSceneNodeByType('Marker', '.{}.ges_lower_cylinder.MARKER_611'.format(model_name))
        MARKER_611.is_floating = True
        MARKER_611.floating_marker_name = '.{}.ges_lower_cylinder.MARKER_611'.format(model_name)
        
        MARKER_614 = MakeSceneNodeByType('Marker', '.{}.gel_lower_cylinder.MARKER_614'.format(model_name))
        MARKER_614.is_floating = True
        MARKER_614.floating_marker_name = '.{}.gel_lower_cylinder.MARKER_614'.format(model_name)
        
        MARKER_617 = MakeSceneNodeByType('Marker', '.{}.ger_lower_cylinder.MARKER_617'.format(model_name))
        MARKER_617.is_floating = True
        MARKER_617.floating_marker_name = '.{}.ger_lower_cylinder.MARKER_617'.format(model_name)


        ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder'.format(model_name))

        MARKER_609 = MakeSceneNodeByType('Marker', '.{}.ges_upper_cylinder.MARKER_609'.format(model_name))
        MARKER_609.marker_name = '.{}.ges_upper_cylinder.MARKER_609'.format(model_name)
        MARKER_609.location = Base.Vector (6200.9167643494, 0.0, 1207.1824231157)
        MARKER_609.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_609.location, MARKER_609.orientation)
        MARKER_609.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_609.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        ges_lower_cylinder = Jusme.ActiveUSScene.getObject('.{}.ges_lower_cylinder'.format(model_name))

        MARKER_610 = MakeSceneNodeByType('Marker', '.{}.ges_lower_cylinder.MARKER_610'.format(model_name))
        MARKER_610.marker_name = '.{}.ges_lower_cylinder.MARKER_610'.format(model_name)
        MARKER_610.location = Base.Vector (6200.9167643494, 0.0, 1207.1824231157)
        MARKER_610.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_610.location, MARKER_610.orientation)
        MARKER_610.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_610.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        gel_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.gel_upper_cylinder'.format(model_name))

        MARKER_612 = MakeSceneNodeByType('Marker', '.{}.gel_upper_cylinder.MARKER_612'.format(model_name))
        MARKER_612.marker_name = '.{}.gel_upper_cylinder.MARKER_612'.format(model_name)
        MARKER_612.location = Base.Vector (1.2205761134E+04, -1486.7657470006, 1142.5793907833)
        MARKER_612.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(gel_upper_cylinder.location, gel_upper_cylinder.orientation, MARKER_612.location, MARKER_612.orientation)
        MARKER_612.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_612.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        gel_lower_cylinder = Jusme.ActiveUSScene.getObject('.{}.gel_lower_cylinder'.format(model_name))

        MARKER_613 = MakeSceneNodeByType('Marker', '.{}.gel_lower_cylinder.MARKER_613'.format(model_name))
        MARKER_613.marker_name = '.{}.gel_lower_cylinder.MARKER_613'.format(model_name)
        MARKER_613.location = Base.Vector (1.2205761134E+04, -1486.7657470006, 1142.5793907833)
        MARKER_613.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(gel_lower_cylinder.location, gel_lower_cylinder.orientation, MARKER_613.location, MARKER_613.orientation)
        MARKER_613.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_613.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        ger_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.ger_upper_cylinder'.format(model_name))

        MARKER_615 = MakeSceneNodeByType('Marker', '.{}.ger_upper_cylinder.MARKER_615'.format(model_name))
        MARKER_615.marker_name = '.{}.ger_upper_cylinder.MARKER_615'.format(model_name)
        MARKER_615.location = Base.Vector (1.2205761134E+04, 1486.7657470006, 1142.5793907833)
        MARKER_615.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ger_upper_cylinder.location, ger_upper_cylinder.orientation, MARKER_615.location, MARKER_615.orientation)
        MARKER_615.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_615.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        ger_lower_cylinder = Jusme.ActiveUSScene.getObject('.{}.ger_lower_cylinder'.format(model_name))

        MARKER_616 = MakeSceneNodeByType('Marker', '.{}.ger_lower_cylinder.MARKER_616'.format(model_name))
        MARKER_616.marker_name = '.{}.ger_lower_cylinder.MARKER_616'.format(model_name)
        MARKER_616.location = Base.Vector (1.2205761134E+04, 1486.7657470006, 1142.5793907833)
        MARKER_616.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ger_lower_cylinder.location, ger_lower_cylinder.orientation, MARKER_616.location, MARKER_616.orientation)
        MARKER_616.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_616.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        NLG_aeroforce = MakeSceneNodeByType('ForceGeneral', '.{}.NLG_aeroforce'.format(model_name))
        i_marker = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder.MARKER_609'.format(model_name))
        if not i_marker :
            print("i_marker")
            return
        j_marker = Jusme.ActiveUSScene.getObject('.{}.ges_lower_cylinder.MARKER_611'.format(model_name))
        if not j_marker :
            print("j_marker")
            return
        ref_marker = Jusme.ActiveUSScene.getObject('.{}.ges_lower_cylinder.MARKER_610'.format(model_name))
        if not ref_marker :
            print("ref_marker")
            return
        NLG_aeroforce.i_marker_name = i_marker
        NLG_aeroforce.ref_marker_name = ref_marker
        NLG_aeroforce.define_using_opt = 0
        NLG_aeroforce.j_floating_marker_name = j_marker
        NLG_aeroforce.define_function_opt = 0
        NLG_aeroforce.x_force_function = ".{}.C0*abs(IF( .{}.NLG_sf_angle-60 : COS( 1.225*.{}.NLG_sf_angle*pi/180 ) , COS( 1.225*.{}.NLG_sf_angle*pi/180 ) , COS( .{}.NLG_sf_angle*pi/180 ) ))*.{}.pa*cos(.{}.NLG_sf_angle*pi/180)*0.5*.{}.mi_du*.{}.windV*abs(.{}.windV)*cos(.{}.NLG_sf_angle*pi/180) ".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        NLG_aeroforce.y_force_function = "0"
        NLG_aeroforce.z_force_function = "-.{}.C0*abs(IF( .{}.NLG_sf_angle-60 : COS( 1.225*.{}.NLG_sf_angle*pi/180 ) , COS( 1.225*.{}.NLG_sf_angle*pi/180 ) , COS( .{}.NLG_sf_angle*pi/180 ) ))*.{}.pa*cos(.{}.NLG_sf_angle*pi/180)*0.5*.{}.mi_du*.{}.windV*abs(.{}.windV)*sin(.{}.NLG_sf_angle*pi/180) ".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        NLG_aeroforce.x_torque_function = "0"
        NLG_aeroforce.y_torque_function = "-1*CUBSPL( -.{}.NLG_sf_angle, 0 , .{}.SPLINE_angle_aeroforce_NLG, 0 )".format(model_name,model_name)
        NLG_aeroforce.z_torque_function = "0"

        MLG_aeroforce_L = MakeSceneNodeByType('ForceGeneral', '.{}.MLG_aeroforce_L'.format(model_name))
        i_marker = Jusme.ActiveUSScene.getObject('.{}.gel_upper_cylinder.MARKER_612'.format(model_name))
        if not i_marker :
            print("i_marker")
            return
        j_marker = Jusme.ActiveUSScene.getObject('.{}.gel_lower_cylinder.MARKER_614'.format(model_name))
        if not j_marker :
            print("j_marker")
            return
        ref_marker = Jusme.ActiveUSScene.getObject('.{}.gel_lower_cylinder.MARKER_613'.format(model_name))
        if not ref_marker :
            print("ref_marker")
            return
        MLG_aeroforce_L.i_marker_name = i_marker
        MLG_aeroforce_L.ref_marker_name = ref_marker
        MLG_aeroforce_L.define_using_opt = 0
        MLG_aeroforce_L.j_floating_marker_name = j_marker
        MLG_aeroforce_L.define_function_opt = 0
        MLG_aeroforce_L.x_force_function = ".{}.C0_MLG*abs(IF( .{}.MLG_sf_angle-60 : COS( 1.225*.{}.MLG_sf_angle*pi/180 ) , COS( 1.225*.{}.MLG_sf_angle*pi/180 ) , COS( .{}.MLG_sf_angle*pi/180 ) ))*.{}.pa_MLG*cos(.{}.MLG_sf_angle*pi/180)*0.5*.{}.mi_du*.{}.windV*abs(.{}.windV)*cos(.{}.MLG_sf_angle*pi/180) ".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MLG_aeroforce_L.y_force_function = "0"
        MLG_aeroforce_L.z_force_function = ".{}.C0_MLG*abs(IF( .{}.MLG_sf_angle-60 : COS( 1.225*.{}.MLG_sf_angle*pi/180 ) , COS( 1.225*.{}.MLG_sf_angle*pi/180 ) , COS( .{}.MLG_sf_angle*pi/180 ) ))*.{}.pa_MLG*cos(.{}.MLG_sf_angle*pi/180)*0.5*.{}.mi_du*.{}.windV*abs(.{}.windV)*sin(.{}.MLG_sf_angle*pi/180) ".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MLG_aeroforce_L.x_torque_function = "0"
        MLG_aeroforce_L.y_torque_function = "-1*CUBSPL( .{}.MLG_sf_angle, 0 , .{}.SPLINE_angle_aeroforce_MLG, 0 )".format(model_name,model_name)
        MLG_aeroforce_L.z_torque_function = "0"

        MLG_aeroforce_R = MakeSceneNodeByType('ForceGeneral', '.{}.MLG_aeroforce_R'.format(model_name))
        i_marker = Jusme.ActiveUSScene.getObject('.{}.ger_upper_cylinder.MARKER_615'.format(model_name))
        if not i_marker :
            print("i_marker")
            return
        j_marker = Jusme.ActiveUSScene.getObject('.{}.ger_lower_cylinder.MARKER_617'.format(model_name))
        if not j_marker :
            print("j_marker")
            return
        ref_marker = Jusme.ActiveUSScene.getObject('.{}.ger_lower_cylinder.MARKER_616'.format(model_name))
        if not ref_marker :
            print("ref_marker")
            return
        MLG_aeroforce_R.i_marker_name = i_marker
        MLG_aeroforce_R.ref_marker_name = ref_marker
        MLG_aeroforce_R.define_using_opt = 0
        MLG_aeroforce_R.j_floating_marker_name = j_marker
        MLG_aeroforce_R.define_function_opt = 0
        MLG_aeroforce_R.x_force_function = ".{}.C0_MLG*abs(IF( .{}.MLG_sf_angle-60 : COS( 1.225*.{}.MLG_sf_angle*pi/180 ) , COS( 1.225*.{}.MLG_sf_angle*pi/180 ) , COS( .{}.MLG_sf_angle*pi/180 ) ))*.{}.pa_MLG*cos(.{}.MLG_sf_angle*pi/180)*0.5*.{}.mi_du*.{}.windV*abs(.{}.windV)*cos(.{}.MLG_sf_angle*pi/180) ".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MLG_aeroforce_R.y_force_function = "0"
        MLG_aeroforce_R.z_force_function = ".{}.C0_MLG*abs(IF( .{}.MLG_sf_angle-60 : COS( 1.225*.{}.MLG_sf_angle*pi/180 ) , COS( 1.225*.{}.MLG_sf_angle*pi/180 ) , COS( .{}.MLG_sf_angle*pi/180 ) ))*.{}.pa_MLG*cos(.{}.MLG_sf_angle*pi/180)*0.5*.{}.mi_du*.{}.windV*abs(.{}.windV)*sin(.{}.MLG_sf_angle*pi/180) ".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MLG_aeroforce_R.x_torque_function = "0"
        MLG_aeroforce_R.y_torque_function = "-1*CUBSPL( .{}.MLG_sf_angle, 0 , .{}.SPLINE_angle_aeroforce_MLG, 0 )".format(model_name,model_name)
        MLG_aeroforce_R.z_torque_function = "0"
        pass

    def InitJoint(self) :
        print("进入收放初始化约束程序")

        model_name = Common.getModelName()
        #-----创建部件之间的约束
        #-----先创建约束需要的marker点


        #----创建joscly_db_sf
        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))
        ges_dragbrace = Jusme.ActiveUSScene.getObject('.{}.ges_dragbrace'.format(model_name))
        hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.{}.ground.hps_db_sf_atch'.format(model_name))

        MARKER_593 = MakeSceneNodeByType('Marker', '.{}.PART_46.MARKER_593'.format(model_name))
        MARKER_593.marker_name = '.{}.PART_46.MARKER_593'.format(model_name)
        MARKER_593.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        MARKER_593.orientation = Base.Vector (180.0, 90.0, 180.0)
        loc_ori = VecUtils.global2local(PART_46.location, PART_46.orientation, MARKER_593.location, MARKER_593.orientation)
        MARKER_593.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_593.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_592 = MakeSceneNodeByType('Marker', '.{}.ges_dragbrace.MARKER_592'.format(model_name))
        MARKER_592.marker_name = '.{}.ges_dragbrace.MARKER_592'.format(model_name)
        MARKER_592.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        MARKER_592.orientation = Base.Vector (180.0, 90.0, 180.0)
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, MARKER_592.location, MARKER_592.orientation)
        MARKER_592.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_592.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        joscly_db_sf = MakeSceneNodeByType('JointCylinder', '.{}.joscly_db_sf'.format(model_name))
        MARKER_593 = Jusme.ActiveUSScene.getObject('.{}.PART_46.MARKER_593'.format(model_name))
        if not MARKER_593 :
            print("MARKER_593")
            return
        MARKER_592 = Jusme.ActiveUSScene.getObject('.{}.ges_dragbrace.MARKER_592'.format(model_name))
        if not MARKER_592 :
            print("MARKER_592")
            return
        joscly_db_sf.position_define_opt = 1
        joscly_db_sf.i_marker_name = MARKER_592
        joscly_db_sf.j_marker_name = MARKER_593


        #----创建jossph_db_uc_joint
        sf_rod = Jusme.ActiveUSScene.getObject('.{}.sf_rod'.format(model_name))
        ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder'.format(model_name))
        hps_rod_bot = Jusme.ActiveUSScene.getObject('.{}.ground.hps_rod_bot'.format(model_name))

        MARKER_591 = MakeSceneNodeByType('Marker', '.{}.ges_upper_cylinder.MARKER_591'.format(model_name))
        MARKER_591.marker_name = '.{}.ges_upper_cylinder.MARKER_591'.format(model_name)
        MARKER_591.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_591.orientation = Base.Vector (0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_591.location, MARKER_591.orientation)
        MARKER_591.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_591.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_590 = MakeSceneNodeByType('Marker', '.{}.sf_rod.MARKER_590'.format(model_name))
        MARKER_590.marker_name = '.{}.sf_rod.MARKER_590'.format(model_name)
        MARKER_590.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_rod_bot))
        MARKER_590.orientation = Base.Vector (0,0,0)
        loc_ori = VecUtils.global2local(sf_rod.location, sf_rod.orientation, MARKER_590.location, MARKER_590.orientation)
        MARKER_590.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_590.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jossph_db_uc_joint = MakeSceneNodeByType('JointSpherical', '.{}.jossph_db_uc_joint'.format(model_name))
        MARKER_590 = Jusme.ActiveUSScene.getObject('.{}.sf_rod.MARKER_590'.format(model_name))
        if not MARKER_590 :
            print("MARKER_590")
            return
        MARKER_591 = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder.MARKER_591'.format(model_name))
        if not MARKER_591 :
            print("MARKER_591")
            return
        jossph_db_uc_joint.position_define_opt = 1
        jossph_db_uc_joint.i_marker_name = MARKER_590
        jossph_db_uc_joint.j_marker_name = MARKER_591


        #----创建JOINT_56
        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))
        ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder'.format(model_name))
        hps_uc_top = Jusme.ActiveUSScene.getObject('.{}.ground.hps_uc_top'.format(model_name))

        MARKER_428 = MakeSceneNodeByType('Marker', '.{}.ges_upper_cylinder.MARKER_428'.format(model_name))
        MARKER_428.marker_name = '.{}.ges_upper_cylinder.MARKER_428'.format(model_name)
        MARKER_428.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_top))
        MARKER_428.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_428.location, MARKER_428.orientation)
        MARKER_428.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_428.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_427 = MakeSceneNodeByType('Marker', '.{}.PART_46.MARKER_427'.format(model_name))
        MARKER_427.marker_name = '.{}.PART_46.MARKER_427'.format(model_name)
        MARKER_427.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uc_top))
        MARKER_427.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(PART_46.location, PART_46.orientation, MARKER_427.location, MARKER_427.orientation)
        MARKER_427.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_427.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        JOINT_56 = MakeSceneNodeByType('JointRevolute', '.{}.JOINT_56'.format(model_name))
        MARKER_427 = Jusme.ActiveUSScene.getObject('.{}.PART_46.MARKER_427'.format(model_name))
        if not MARKER_427 :
            print("MARKER_427")
            return
        MARKER_428 = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder.MARKER_428'.format(model_name))
        if not MARKER_428 :
            print("MARKER_428")
            return
        JOINT_56.position_define_opt = 1
        JOINT_56.i_marker_name = MARKER_427
        JOINT_56.j_marker_name = MARKER_428


        #----创建JOINT_59
        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))
        ger_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.ger_upper_cylinder'.format(model_name))
        hpr_uc_top = Jusme.ActiveUSScene.getObject('.{}.ground.hpr_uc_top'.format(model_name))

        MARKER_443 = MakeSceneNodeByType('Marker', '.{}.PART_46.MARKER_443'.format(model_name))
        MARKER_443.marker_name = '.{}.PART_46.MARKER_443'.format(model_name)
        MARKER_443.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_uc_top))
        MARKER_443.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(PART_46.location, PART_46.orientation, MARKER_443.location, MARKER_443.orientation)
        MARKER_443.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_443.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_444 = MakeSceneNodeByType('Marker', '.{}.ger_upper_cylinder.MARKER_444'.format(model_name))
        MARKER_444.marker_name = '.{}.ger_upper_cylinder.MARKER_444'.format(model_name)
        MARKER_444.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_uc_top))
        MARKER_444.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ger_upper_cylinder.location, ger_upper_cylinder.orientation, MARKER_444.location, MARKER_444.orientation)
        MARKER_444.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_444.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        JOINT_59 = MakeSceneNodeByType('JointRevolute', '.{}.JOINT_59'.format(model_name))
        MARKER_443 = Jusme.ActiveUSScene.getObject('.{}.PART_46.MARKER_443'.format(model_name))
        if not MARKER_443 :
            print("MARKER_443")
            return
        MARKER_444 = Jusme.ActiveUSScene.getObject('.{}.ger_upper_cylinder.MARKER_444'.format(model_name))
        if not MARKER_444 :
            print("MARKER_444")
            return
        JOINT_59.position_define_opt = 1
        JOINT_59.i_marker_name = MARKER_443
        JOINT_59.j_marker_name = MARKER_444


        #----创建JOINT_60
        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))
        gel_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.gel_upper_cylinder'.format(model_name))
        hpl_uc_top = Jusme.ActiveUSScene.getObject('.{}.ground.hpl_uc_top'.format(model_name))

        MARKER_445 = MakeSceneNodeByType('Marker', '.{}.PART_46.MARKER_445'.format(model_name))
        MARKER_445.marker_name = '.{}.PART_46.MARKER_445'.format(model_name)
        MARKER_445.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_uc_top))
        MARKER_445.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(PART_46.location, PART_46.orientation, MARKER_445.location, MARKER_445.orientation)
        MARKER_445.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_445.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_446 = MakeSceneNodeByType('Marker', '.{}.gel_upper_cylinder.MARKER_446'.format(model_name))
        MARKER_446.marker_name = '.{}.gel_upper_cylinder.MARKER_446'.format(model_name)
        MARKER_446.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_uc_top))
        MARKER_446.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(gel_upper_cylinder.location, gel_upper_cylinder.orientation, MARKER_446.location, MARKER_446.orientation)
        MARKER_446.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_446.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        JOINT_60 = MakeSceneNodeByType('JointRevolute', '.{}.JOINT_60'.format(model_name))
        MARKER_445 = Jusme.ActiveUSScene.getObject('.{}.PART_46.MARKER_445'.format(model_name))
        if not MARKER_445 :
            print("MARKER_445")
            return
        MARKER_446 = Jusme.ActiveUSScene.getObject('.{}.gel_upper_cylinder.MARKER_446'.format(model_name))
        if not MARKER_446 :
            print("MARKER_446")
            return
        JOINT_60.position_define_opt = 1
        JOINT_60.i_marker_name = MARKER_445
        JOINT_60.j_marker_name = MARKER_446


        #----创建jorrev_spndl_sf
        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))
        ger_spindle = Jusme.ActiveUSScene.getObject('.{}.ger_spindle'.format(model_name))
        hpr_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.{}.ground.hpr_spndl_sf_atch'.format(model_name))
        hpr_uc_top = Jusme.ActiveUSScene.getObject('.{}.ground.hpr_uc_top'.format(model_name))

        jxr_joint_j_6 = MakeSceneNodeByType('Marker', '.{}.PART_46.jxr_joint_j_6'.format(model_name))
        jxr_joint_j_6.marker_name = '.{}.PART_46.jxr_joint_j_6'.format(model_name)
        jxr_joint_j_6.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_spndl_sf_atch))
        jxr_joint_j_6.orientation = VecUtils.ORI_ALONG_AXIS(hpr_spndl_sf_atch.location, hpr_uc_top.location, 'z')
        loc_ori = VecUtils.global2local(PART_46.location, PART_46.orientation, jxr_joint_j_6.location, jxr_joint_j_6.orientation)
        jxr_joint_j_6.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_j_6.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jxr_joint_i_6 = MakeSceneNodeByType('Marker', '.{}.ger_spindle.jxr_joint_i_6'.format(model_name))
        jxr_joint_i_6.marker_name = '.{}.ger_spindle.jxr_joint_i_6'.format(model_name)
        jxr_joint_i_6.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxr_joint_j_6))
        jxr_joint_i_6.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxr_joint_j_6))
        loc_ori = VecUtils.global2local(ger_spindle.location, ger_spindle.orientation, jxr_joint_i_6.location, jxr_joint_i_6.orientation)
        jxr_joint_i_6.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_i_6.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jorrev_spndl_sf = MakeSceneNodeByType('JointRevolute', '.{}.jorrev_spndl_sf'.format(model_name))
        jxr_joint_j_6 = Jusme.ActiveUSScene.getObject('.{}.PART_46.jxr_joint_j_6'.format(model_name))
        if not jxr_joint_j_6 :
            print("jxr_joint_j_6")
            return
        jxr_joint_i_6 = Jusme.ActiveUSScene.getObject('.{}.ger_spindle.jxr_joint_i_6'.format(model_name))
        if not jxr_joint_i_6 :
            print("jxr_joint_i_6")
            return
        jorrev_spndl_sf.position_define_opt = 1
        jorrev_spndl_sf.i_marker_name = jxr_joint_i_6
        jorrev_spndl_sf.j_marker_name = jxr_joint_j_6


        #----创建jolrev_spndl_sf
        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))
        gel_spindle = Jusme.ActiveUSScene.getObject('.{}.gel_spindle'.format(model_name))
        hpl_spndl_sf_atch = Jusme.ActiveUSScene.getObject('.{}.ground.hpl_spndl_sf_atch'.format(model_name))
        hpl_uc_top = Jusme.ActiveUSScene.getObject('.{}.ground.hpl_uc_top'.format(model_name))

        jxl_joint_j_6 = MakeSceneNodeByType('Marker', '.{}.PART_46.jxl_joint_j_6'.format(model_name))
        jxl_joint_j_6.marker_name = '.{}.PART_46.jxl_joint_j_6'.format(model_name)
        jxl_joint_j_6.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_spndl_sf_atch))
        jxl_joint_j_6.orientation = VecUtils.ORI_ALONG_AXIS(hpl_spndl_sf_atch.location, hpl_uc_top.location, 'z')
        loc_ori = VecUtils.global2local(PART_46.location, PART_46.orientation, jxl_joint_j_6.location, jxl_joint_j_6.orientation)
        jxl_joint_j_6.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_j_6.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jxl_joint_i_6 = MakeSceneNodeByType('Marker', '.{}.gel_spindle.jxl_joint_i_6'.format(model_name))
        jxl_joint_i_6.marker_name = '.{}.gel_spindle.jxl_joint_i_6'.format(model_name)
        jxl_joint_i_6.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxl_joint_j_6))
        jxl_joint_i_6.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxl_joint_j_6))
        loc_ori = VecUtils.global2local(gel_spindle.location, gel_spindle.orientation, jxl_joint_i_6.location, jxl_joint_i_6.orientation)
        jxl_joint_i_6.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_i_6.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jolrev_spndl_sf = MakeSceneNodeByType('JointRevolute', '.{}.jolrev_spndl_sf'.format(model_name))
        jxl_joint_j_6 = Jusme.ActiveUSScene.getObject('.{}.PART_46.jxl_joint_j_6'.format(model_name))
        if not jxl_joint_j_6 :
            print("jxl_joint_j_6")
            return
        jxl_joint_i_6 = Jusme.ActiveUSScene.getObject('.{}.gel_spindle.jxl_joint_i_6'.format(model_name))
        if not jxl_joint_i_6 :
            print("jxl_joint_i_6")
            return
        jolrev_spndl_sf.position_define_opt = 1
        jolrev_spndl_sf.i_marker_name = jxl_joint_i_6
        jolrev_spndl_sf.j_marker_name = jxl_joint_j_6



        #----创建jorsph_upract_sf
        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))
        ger_upract = Jusme.ActiveUSScene.getObject('.{}.ger_upract'.format(model_name))
        hpr_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.{}.ground.hpr_upract_sf_atch_1'.format(model_name))
        origo = Jusme.ActiveUSScene.getObject('.{}.ground.origo'.format(model_name))

        jxr_joint_j_17 = MakeSceneNodeByType('Marker', '.{}.PART_46.jxr_joint_j_17'.format(model_name))
        jxr_joint_j_17.marker_name = '.{}.PART_46.jxr_joint_j_17'.format(model_name)
        jxr_joint_j_17.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_upract_sf_atch_1))
        jxr_joint_j_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        loc_ori = VecUtils.global2local(PART_46.location, PART_46.orientation, jxr_joint_j_17.location, jxr_joint_j_17.orientation)
        jxr_joint_j_17.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_j_17.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jxr_joint_i_17 = MakeSceneNodeByType('Marker', '.{}.ger_upract.jxr_joint_i_17'.format(model_name))
        jxr_joint_i_17.marker_name = '.{}.ger_upract.jxr_joint_i_17'.format(model_name)
        jxr_joint_i_17.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxr_joint_j_17))
        jxr_joint_i_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxr_joint_j_17))
        loc_ori = VecUtils.global2local(ger_upract.location, ger_upract.orientation, jxr_joint_i_17.location, jxr_joint_i_17.orientation)
        jxr_joint_i_17.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxr_joint_i_17.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jorsph_upract_sf = MakeSceneNodeByType('JointSpherical', '.{}.jorsph_upract_sf'.format(model_name))
        jxr_joint_j_17 = Jusme.ActiveUSScene.getObject('.{}.PART_46.jxr_joint_j_17'.format(model_name))
        if not jxr_joint_j_17 :
            print("jxr_joint_j_17")
            return
        jxr_joint_i_17 = Jusme.ActiveUSScene.getObject('.{}.ger_upract.jxr_joint_i_17'.format(model_name))
        if not jxr_joint_i_17 :
            print("jxr_joint_i_17")
            return
        jorsph_upract_sf.position_define_opt = 1
        jorsph_upract_sf.i_marker_name = jxr_joint_i_17
        jorsph_upract_sf.j_marker_name = jxr_joint_j_17


        #----创建jolsph_upract_sf
        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))
        gel_upract = Jusme.ActiveUSScene.getObject('.{}.gel_upract'.format(model_name))
        hpl_upract_sf_atch_1 = Jusme.ActiveUSScene.getObject('.{}.ground.hpl_upract_sf_atch_1'.format(model_name))
        origo = Jusme.ActiveUSScene.getObject('.{}.ground.origo'.format(model_name))

        jxl_joint_j_17 = MakeSceneNodeByType('Marker', '.{}.PART_46.jxl_joint_j_17'.format(model_name))
        jxl_joint_j_17.marker_name = '.{}.PART_46.jxl_joint_j_17'.format(model_name)
        jxl_joint_j_17.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_upract_sf_atch_1))
        jxl_joint_j_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
        loc_ori = VecUtils.global2local(PART_46.location, PART_46.orientation, jxl_joint_j_17.location, jxl_joint_j_17.orientation)
        jxl_joint_j_17.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_j_17.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jxl_joint_i_17 = MakeSceneNodeByType('Marker', '.{}.gel_upract.jxl_joint_i_17'.format(model_name))
        jxl_joint_i_17.marker_name = '.{}.gel_upract.jxl_joint_i_17'.format(model_name)
        jxl_joint_i_17.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxl_joint_j_17))
        jxl_joint_i_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxl_joint_j_17))
        loc_ori = VecUtils.global2local(gel_upract.location, gel_upract.orientation, jxl_joint_i_17.location, jxl_joint_i_17.orientation)
        jxl_joint_i_17.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxl_joint_i_17.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jolsph_upract_sf = MakeSceneNodeByType('JointSpherical', '.{}.jolsph_upract_sf'.format(model_name))
        jxl_joint_j_17 = Jusme.ActiveUSScene.getObject('.{}.PART_46.jxl_joint_j_17'.format(model_name))
        if not jxl_joint_j_17 :
            print("jxl_joint_j_17")
            return
        jxl_joint_i_17 = Jusme.ActiveUSScene.getObject('.{}.gel_upract.jxl_joint_i_17'.format(model_name))
        if not jxl_joint_i_17 :
            print("jxl_joint_i_17")
            return
        jolsph_upract_sf.position_define_opt = 1
        jolsph_upract_sf.i_marker_name = jxl_joint_i_17
        jolsph_upract_sf.j_marker_name = jxl_joint_j_17



        #----创建upcylinder_zdt
        ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder'.format(model_name))
        zdt = Jusme.ActiveUSScene.getObject('.{}.zdt'.format(model_name))
        zdt_1 = Jusme.ActiveUSScene.getObject('.{}.ground.zdt_1'.format(model_name))
        origo = Jusme.ActiveUSScene.getObject('.{}.ground.origo'.format(model_name))

        MARKER_467 = MakeSceneNodeByType('Marker', '.{}.ges_upper_cylinder.MARKER_467'.format(model_name))
        MARKER_467.marker_name = '.{}.ges_upper_cylinder.MARKER_467'.format(model_name)
        MARKER_467.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], zdt_1))
        MARKER_467.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_467.location, MARKER_467.orientation)
        MARKER_467.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_467.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_468 = MakeSceneNodeByType('Marker', '.{}.zdt.MARKER_468'.format(model_name))
        MARKER_468.marker_name = '.{}.zdt.MARKER_468'.format(model_name)
        MARKER_468.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], zdt_1))
        MARKER_468.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(zdt.location, zdt.orientation, MARKER_468.location, MARKER_468.orientation)
        MARKER_468.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_468.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        upcylinder_zdt = MakeSceneNodeByType('JointRevolute', '.{}.upcylinder_zdt'.format(model_name))
        MARKER_467 = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder.MARKER_467'.format(model_name))
        if not MARKER_467 :
            print("MARKER_467")
            return
        MARKER_468 = Jusme.ActiveUSScene.getObject('.{}.zdt.MARKER_468'.format(model_name))
        if not MARKER_468 :
            print("MARKER_468")
            return
        upcylinder_zdt.position_define_opt = 1
        upcylinder_zdt.i_marker_name = MARKER_467
        upcylinder_zdt.j_marker_name = MARKER_468



        #----创建collar_hsg
        ges_collar = Jusme.ActiveUSScene.getObject('.{}.ges_collar'.format(model_name))
        hsg = Jusme.ActiveUSScene.getObject('.{}.hsg'.format(model_name))
        
        hsg_1 = Jusme.ActiveUSScene.getObject('.{}.ground.hsg_1'.format(model_name))
        origo = Jusme.ActiveUSScene.getObject('.{}.ground.origo'.format(model_name))

        MARKER_465 = MakeSceneNodeByType('Marker', '.{}.ges_collar.MARKER_465'.format(model_name))
        MARKER_465.marker_name = '.{}.ges_collar.MARKER_465'.format(model_name)
        MARKER_465.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hsg_1))
        MARKER_465.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, MARKER_465.location, MARKER_465.orientation)
        MARKER_465.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_465.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_466 = MakeSceneNodeByType('Marker', '.{}.hsg.MARKER_466'.format(model_name))
        MARKER_466.marker_name = '.{}.hsg.MARKER_466'.format(model_name)
        MARKER_466.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hsg_1))
        MARKER_466.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(hsg.location, hsg.orientation, MARKER_466.location, MARKER_466.orientation)
        MARKER_466.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_466.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        collar_hsg = MakeSceneNodeByType('JointRevolute', '.{}.collar_hsg'.format(model_name))
        MARKER_465 = Jusme.ActiveUSScene.getObject('.{}.ges_collar.MARKER_465'.format(model_name))
        if not MARKER_465 :
            print("MARKER_465")
            return
        MARKER_466 = Jusme.ActiveUSScene.getObject('.{}.hsg.MARKER_466'.format(model_name))
        if not MARKER_466 :
            print("MARKER_466")
            return
        collar_hsg.position_define_opt = 1
        collar_hsg.i_marker_name = MARKER_465
        collar_hsg.j_marker_name = MARKER_466
        pass

    def InitMotion(self) :
        print("进入收放初始化驱动程序")
        model_name = Common.getModelName()
        #----------------------------------------添加驱动
        MOTION_RIGHT = MakeSceneNodeByType('JointMotion', '.{}.MOTION_RIGHT'.format(model_name))
        MOTION_RIGHT.function_type_opt = 0
        MOTION_RIGHT.function = "-STEP( time , 0 , 0.1 , .{}.mlg_up_time , .{}.MLG_ret_disp )-STEP( time , .{}.mlg_up_time+.{}.mlg_hold_time , 0 , .{}.mlg_up_time+.{}.mlg_hold_time+.{}.mlg_down_time , -.{}.MLG_ret_disp )".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MOTION_RIGHT.time_derivative = 0
        MOTION_RIGHT.motion_type_opt = 1
        motion_joint = Jusme.ActiveUSScene.getObject('.{}.jortra_lwract_upract'.format(model_name))
        MOTION_RIGHT.joint_name = motion_joint
        MOTION_RIGHT.type_of_freedom = 0
        MOTION_RIGHT.ic_type_opt = 0

        MOTION_LEFT = MakeSceneNodeByType('JointMotion', '.{}.MOTION_LEFT'.format(model_name))
        MOTION_LEFT.function_type_opt = 0
        MOTION_LEFT.function = "-STEP( time , 0 , 0.1 , .{}.mlg_up_time , .{}.MLG_ret_disp )-STEP( time , .{}.mlg_up_time+.{}.mlg_hold_time , 0 , .{}.mlg_up_time+.{}.mlg_hold_time+.{}.mlg_down_time , -.{}.MLG_ret_disp )".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MOTION_LEFT.time_derivative = 0
        MOTION_LEFT.motion_type_opt = 1
        motion_joint = Jusme.ActiveUSScene.getObject('.{}.joltra_lwract_upract'.format(model_name))
        MOTION_LEFT.joint_name = motion_joint
        MOTION_LEFT.type_of_freedom = 0
        MOTION_LEFT.ic_type_opt = 0

        NLG_DISP = MakeSceneNodeByType('JointMotion', '.{}.NLG_DISP'.format(model_name))
        NLG_DISP.function_type_opt = 0
        NLG_DISP.function = "-STEP( time , 0 , 0 , .{}.nlg_up_time , .{}.NLG_ret_disp )-STEP( time , .{}.nlg_up_time+.{}.nlg_hold_time , 0 , .{}.nlg_up_time+.{}.nlg_hold_time+.{}.nlg_down_time , -.{}.NLG_ret_disp )".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        NLG_DISP.time_derivative = 0
        NLG_DISP.motion_type_opt = 1
        motion_joint = Jusme.ActiveUSScene.getObject('.{}.joscly_ac_rd'.format(model_name))
        NLG_DISP.joint_name = motion_joint
        NLG_DISP.type_of_freedom = 0
        NLG_DISP.ic_type_opt = 0
        pass

    def InitMeasure(self) :
        print("进入收放初始化测量程序")
        model_name = Common.getModelName()

        MLG_sf_angle = MakeSceneNodeByType('Orient', '.{}.MLG_sf_angle'.format(model_name))
        MLG_sf_angle.characteristic_opt = 0
        MLG_sf_angle.component_angle_opt = 0
        MARKER_445 = Jusme.ActiveUSScene.getObject('.{}.PART_46.MARKER_445'.format(model_name))
        if not MARKER_445 :
            print("MARKER_445")
            return
        MARKER_446 = Jusme.ActiveUSScene.getObject('.{}.gel_upper_cylinder.MARKER_446'.format(model_name))
        if not MARKER_446 :
            print("MARKER_446")
            return
        MLG_sf_angle.to_frame = MARKER_446
        MLG_sf_angle.from_frame = MARKER_445



        NLG_sf_angle = MakeSceneNodeByType('Orient', '.{}.NLG_sf_angle'.format(model_name))
        NLG_sf_angle.characteristic_opt = 0
        NLG_sf_angle.component_angle_opt = 0
        MARKER_427 = Jusme.ActiveUSScene.getObject('.{}.PART_46.MARKER_427'.format(model_name))
        if not MARKER_427 :
            print("MARKER_427")
            return
        MARKER_428 = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder.MARKER_428'.format(model_name))
        if not MARKER_428 :
            print("MARKER_428")
            return
        NLG_sf_angle.to_frame = MARKER_428
        NLG_sf_angle.from_frame = MARKER_427

        pass
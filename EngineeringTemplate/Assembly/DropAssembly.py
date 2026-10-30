#----------------落震装配操作

import Jusme
from Jusme import Base
from Fmbs.import_all_node import MakeSceneNodeByType
import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils

import Common
import DesignVariable
import AbstractAssembly

class DropAssembly(AbstractAssembly.AbstractAssembly) :
    def __init__(self, var : DesignVariable.Variable) -> None:
        super().__init__(var)
        pass

    def InitDesignVariables(self) :
        print("进入落震写设计变量程序")

        #---------------删除设计变量
        Common.removeDesignTools()
        model_name = Common.getModelName()

        #----------------添加刹车工况设计变量
        name_val_dic = self.design_var.name_val_dic


        #----------先创建工况需要的设计变量----------------------
        MLG_Cs = MakeSceneNodeByType('DesignVariable', '.{}.MLG_Cs'.format(model_name))
        MLG_Cs.variable_name = '.{}.MLG_Cs'.format(model_name)
        MLG_Cs.value_type_opt = 0
        MLG_Cs.real_value = 0.8
        MLG_Cs.delta_type = 1
        MLG_Cs.use_range = True
        MLG_Cs.range = [-6.4516E-04,6.4516E-04]
        name_val_dic["MLG_Cs"] = 0.8

        MLG_Ch = MakeSceneNodeByType('DesignVariable', '.{}.MLG_Ch'.format(model_name))
        MLG_Ch.variable_name = '.{}.MLG_Ch'.format(model_name)
        MLG_Ch.value_type_opt = 0
        MLG_Ch.real_value = 0.8
        MLG_Ch.delta_type = 1
        MLG_Ch.use_range = True
        MLG_Ch.range = [-6.4516E-04,6.4516E-04]
        name_val_dic["MLG_Ch"] = 0.8

        MLG_Asdl = MakeSceneNodeByType('DesignVariable', '.{}.MLG_Asdl'.format(model_name))
        MLG_Asdl.variable_name = '.{}.MLG_Asdl'.format(model_name)
        MLG_Asdl.value_type_opt = 0
        MLG_Asdl.real_value = 1.57E-04
        MLG_Asdl.delta_type = 1
        MLG_Asdl.use_range = True
        MLG_Asdl.range = [-6.4516E-04,6.4516E-04]
        name_val_dic["MLG_Asdl"] = 1.57E-04

        MLG_Asd = MakeSceneNodeByType('DesignVariable', '.{}.MLG_Asd'.format(model_name))
        MLG_Asd.variable_name = '.{}.MLG_Asd'.format(model_name)
        MLG_Asd.value_type_opt = 0
        MLG_Asd.real_value = 3.798E-03
        MLG_Asd.delta_type = 1
        MLG_Asd.use_range = True
        MLG_Asd.range = [-6.4516E-04,6.4516E-04]

        MLG_Ahdl = MakeSceneNodeByType('DesignVariable', '.{}.MLG_Ahdl'.format(model_name))
        MLG_Ahdl.variable_name = '.{}.MLG_Ahdl'.format(model_name)
        MLG_Ahdl.value_type_opt = 0
        MLG_Ahdl.real_value = 1.96E-03
        MLG_Ahdl.delta_type = 1
        MLG_Ahdl.use_range = True
        MLG_Ahdl.range = [-6.4516E-04,6.4516E-04]

        MLG_Ahd = MakeSceneNodeByType('DesignVariable', '.{}.MLG_Ahd'.format(model_name))
        MLG_Ahd.variable_name = '.{}.MLG_Ahd'.format(model_name)
        MLG_Ahd.value_type_opt = 0
        MLG_Ahd.real_value = 1.96E-03
        MLG_Ahd.delta_type = 1
        MLG_Ahd.use_range = True
        MLG_Ahd.range = [-6.4516E-04,6.4516E-04]

        MLG_As = MakeSceneNodeByType('DesignVariable', '.{}.MLG_As'.format(model_name))
        MLG_As.variable_name = '.{}.MLG_As'.format(model_name)
        MLG_As.value_type_opt = 0
        MLG_As.real_value = 1.4961E-02
        MLG_As.delta_type = 1
        MLG_As.use_range = True
        MLG_As.range = [-6.4516E-04,6.4516E-04]

        MLG_Ah = MakeSceneNodeByType('DesignVariable', '.{}.MLG_Ah'.format(model_name))
        MLG_Ah.variable_name = '.{}.MLG_Ah'.format(model_name)
        MLG_Ah.value_type_opt = 0
        MLG_Ah.real_value = 5.5571E-02
        MLG_Ah.delta_type = 1
        MLG_Ah.use_range = True
        MLG_Ah.range = [-6.4516E-04,6.4516E-04]

        MLG_P0 = MakeSceneNodeByType('DesignVariable', '.{}.MLG_P0'.format(model_name))
        MLG_P0.variable_name = '.{}.MLG_P0'.format(model_name)
        MLG_P0.value_type_opt = 0
        MLG_P0.real_value = 1.45E+06
        MLG_P0.delta_type = 1
        MLG_P0.use_range = True
        MLG_P0.range = [-6.4516E-04,6.4516E-04]

        MLG_V0 = MakeSceneNodeByType('DesignVariable', '.{}.MLG_V0'.format(model_name))
        MLG_V0.variable_name = '.{}.MLG_V0'.format(model_name)
        MLG_V0.value_type_opt = 0
        MLG_V0.real_value = 3.931E-03
        MLG_V0.delta_type = 1
        MLG_V0.use_range = True
        MLG_V0.range = [-6.4516E-04,6.4516E-04]

        MLG_Aa = MakeSceneNodeByType('DesignVariable', '.{}.MLG_Aa'.format(model_name))
        MLG_Aa.variable_name = '.{}.MLG_Aa'.format(model_name)
        MLG_Aa.value_type_opt = 0
        MLG_Aa.real_value = 8.921E-03
        MLG_Aa.delta_type = 1
        MLG_Aa.use_range = True
        MLG_Aa.range = [-6.4516E-04,6.4516E-04]

        NLG_Cs = MakeSceneNodeByType('DesignVariable', '.{}.NLG_Cs'.format(model_name))
        NLG_Cs.variable_name = '.{}.NLG_Cs'.format(model_name)
        NLG_Cs.value_type_opt = 0
        NLG_Cs.real_value = 0.8
        NLG_Cs.delta_type = 1
        NLG_Cs.use_range = True
        NLG_Cs.range = [-6.4516E-04,6.4516E-04]

        NLG_Ch = MakeSceneNodeByType('DesignVariable', '.{}.NLG_Ch'.format(model_name))
        NLG_Ch.variable_name = '.{}.NLG_Ch'.format(model_name)
        NLG_Ch.value_type_opt = 0
        NLG_Ch.real_value = 0.8
        NLG_Ch.delta_type = 1
        NLG_Ch.use_range = True
        NLG_Ch.range = [-6.4516E-04,6.4516E-04]

        NLG_Asdl = MakeSceneNodeByType('DesignVariable', '.{}.NLG_Asdl'.format(model_name))
        NLG_Asdl.variable_name = '.{}.NLG_Asdl'.format(model_name)
        NLG_Asdl.value_type_opt = 0
        NLG_Asdl.real_value = 1.0E-04
        NLG_Asdl.delta_type = 1
        NLG_Asdl.use_range = True
        NLG_Asdl.range = [-6.4516E-04,6.4516E-04]

        NLG_Asd = MakeSceneNodeByType('DesignVariable', '.{}.NLG_Asd'.format(model_name))
        NLG_Asd.variable_name = '.{}.NLG_Asd'.format(model_name)
        NLG_Asd.value_type_opt = 0
        NLG_Asd.real_value = 2.313E-03
        NLG_Asd.delta_type = 1
        NLG_Asd.use_range = True
        NLG_Asd.range = [-6.4516E-04,6.4516E-04]

        NLG_Ahdl = MakeSceneNodeByType('DesignVariable', '.{}.NLG_Ahdl'.format(model_name))
        NLG_Ahdl.variable_name = '.{}.NLG_Ahdl'.format(model_name)
        NLG_Ahdl.value_type_opt = 0
        NLG_Ahdl.real_value = 3.14E-04
        NLG_Ahdl.delta_type = 1
        NLG_Ahdl.use_range = True
        NLG_Ahdl.range = [-6.4516E-04,6.4516E-04]

        NLG_Ahd = MakeSceneNodeByType('DesignVariable', '.{}.NLG_Ahd'.format(model_name))
        NLG_Ahd.variable_name = '.{}.NLG_Ahd'.format(model_name)
        NLG_Ahd.value_type_opt = 0
        NLG_Ahd.real_value = 3.14E-04
        NLG_Ahd.delta_type = 1
        NLG_Ahd.use_range = True
        NLG_Ahd.range = [-6.4516E-04,6.4516E-04]

        NLG_As = MakeSceneNodeByType('DesignVariable', '.{}.NLG_As'.format(model_name))
        NLG_As.variable_name = '.{}.NLG_As'.format(model_name)
        NLG_As.value_type_opt = 0
        NLG_As.real_value = 6.139E-03
        NLG_As.delta_type = 1
        NLG_As.use_range = True
        NLG_As.range = [-6.4516E-04,6.4516E-04]

        NLG_Ah = MakeSceneNodeByType('DesignVariable', '.{}.NLG_Ah'.format(model_name))
        NLG_Ah.variable_name = '.{}.NLG_Ah'.format(model_name)
        NLG_Ah.value_type_opt = 0
        NLG_Ah.real_value = 1.953E-02
        NLG_Ah.delta_type = 1
        NLG_Ah.use_range = True
        NLG_Ah.range = [-6.4516E-04,6.4516E-04]

        rou = MakeSceneNodeByType('DesignVariable', '.{}.rou'.format(model_name))
        rou.variable_name = '.{}.rou'.format(model_name)
        rou.value_type_opt = 0
        rou.real_value = 860
        rou.delta_type = 1
        rou.use_range = True
        rou.range = [-6.4516E-04,6.4516E-04]

        Patm = MakeSceneNodeByType('DesignVariable', '.{}.Patm'.format(model_name))
        Patm.variable_name = '.{}.Patm'.format(model_name)
        Patm.value_type_opt = 0
        Patm.real_value = 1.01325E+05
        Patm.delta_type = 1
        Patm.use_range = True
        Patm.range = [-6.4516E-04,6.4516E-04]

        GAMA = MakeSceneNodeByType('DesignVariable', '.{}.GAMA'.format(model_name))
        GAMA.variable_name = '.{}.GAMA'.format(model_name)
        GAMA.value_type_opt = 0
        GAMA.real_value = 1.1
        GAMA.delta_type = 1
        GAMA.use_range = True
        GAMA.range = [-6.4516E-04,6.4516E-04]

        NLG_P0 = MakeSceneNodeByType('DesignVariable', '.{}.NLG_P0'.format(model_name))
        NLG_P0.variable_name = '.{}.NLG_P0'.format(model_name)
        NLG_P0.value_type_opt = 0
        NLG_P0.real_value = 1.3E+06
        NLG_P0.delta_type = 1
        NLG_P0.use_range = True
        NLG_P0.range = [-6.4516E-04,6.4516E-04]

        NLG_V0 = MakeSceneNodeByType('DesignVariable', '.{}.NLG_V0'.format(model_name))
        NLG_V0.variable_name = '.{}.NLG_V0'.format(model_name)
        NLG_V0.value_type_opt = 0
        NLG_V0.real_value = 1.028E-02
        NLG_V0.delta_type = 1
        NLG_V0.use_range = True
        NLG_V0.range = [-6.4516E-04,6.4516E-04]

        NLG_Aa = MakeSceneNodeByType('DesignVariable', '.{}.NLG_Aa'.format(model_name))
        NLG_Aa.variable_name = '.{}.NLG_Aa'.format(model_name)
        NLG_Aa.value_type_opt = 0
        NLG_Aa.real_value = 2.480717E-02
        NLG_Aa.delta_type = 1
        NLG_Aa.use_range = True
        NLG_Aa.range = [-6.4516E-04,6.4516E-04]


        pass
    def InitElement(self) :

        print("进入落震写单元程序")

        #-----------删除单元
        Common.removeElements()
        model_name = Common.getModelName()

        #-----------------------------添加单元-------------------------
        NLG_S = MakeSceneNodeByType('DataElementVariable', '.{}.NLG_S'.format(model_name))
        NLG_S.initial_condition = 0
        NLG_S.function_opt = 0
        NLG_S.initial_condition_opt = 1
        NLG_S.function = "0.4286-DM(.{}.ges_upper_cylinder.MARKER_2,.{}.ges_lower_cylinder.MARKER_1)".format(model_name, model_name)

        LMLG_S = MakeSceneNodeByType('DataElementVariable', '.{}.LMLG_S'.format(model_name))
        LMLG_S.initial_condition = 0
        LMLG_S.function_opt = 0
        LMLG_S.initial_condition_opt = 1
        LMLG_S.function = "1.014262-DM(.{}.gel_upper_cylinder.MARKER_272,.{}.gel_lower_cylinder.MARKER_273)".format(model_name, model_name)

        RMLG_S = MakeSceneNodeByType('DataElementVariable', '.{}.RMLG_S'.format(model_name))
        RMLG_S.initial_condition = 0
        RMLG_S.function_opt = 0
        RMLG_S.initial_condition_opt = 1
        RMLG_S.function = "1.014262-DM(.{}.ger_upper_cylinder.MARKER_278,.{}.ger_lower_cylinder.MARKER_279)".format(model_name, model_name)

        LMLG_V = MakeSceneNodeByType('DataElementVariable', '.{}.LMLG_V'.format(model_name))
        LMLG_V.initial_condition = 0
        LMLG_V.function_opt = 0
        LMLG_V.initial_condition_opt = 1
        LMLG_V.function = "-1*VR(.{}.gel_upper_cylinder.MARKER_272,.{}.gel_lower_cylinder.MARKER_273)".format(model_name, model_name)

        RMLG_V = MakeSceneNodeByType('DataElementVariable', '.{}.RMLG_V'.format(model_name))
        RMLG_V.initial_condition = 0
        RMLG_V.function_opt = 0
        RMLG_V.initial_condition_opt = 1
        RMLG_V.function = "-1*VR(.{}.ger_upper_cylinder.MARKER_278,.{}.ger_lower_cylinder.MARKER_279)".format(model_name, model_name)

        NLG_V = MakeSceneNodeByType('DataElementVariable', '.{}.NLG_V'.format(model_name))
        NLG_V.initial_condition = 0
        NLG_V.function_opt = 0
        NLG_V.initial_condition_opt = 1
        NLG_V.function = "-1*VR(.{}.ges_upper_cylinder.MARKER_2,.{}.ges_lower_cylinder.MARKER_1)".format(model_name, model_name)
        pass

    def InitMarker(self) :
        print("进入落震写Marker点程序")
        pass

    def InitForce(self) :
        print("进入落震写载荷程序")

        model_name = Common.getModelName()
        #--------创建工况需要的载荷-------------
        #--------创建载荷前需添加载荷需要的marker点---


        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))


        ges_collar = Jusme.ActiveUSScene.getObject('.{}.ges_collar'.format(model_name))

        ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder'.format(model_name))


        MARKER_405 = MakeSceneNodeByType('Marker', '.{}.ges_upper_cylinder.MARKER_405'.format(model_name))
        MARKER_405.marker_name = '.{}.ges_upper_cylinder.MARKER_405'.format(model_name)
        MARKER_405.location = Base.Vector (6.1976, 0.0, 1.6256)
        MARKER_405.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_405.location, MARKER_405.orientation)
        MARKER_405.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_405.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        ges_lower_cylinder = Jusme.ActiveUSScene.getObject('.{}.ges_lower_cylinder'.format(model_name))

        MARKER_406 = MakeSceneNodeByType('Marker', '.{}.ges_lower_cylinder.MARKER_406'.format(model_name))
        MARKER_406.marker_name = '.{}.ges_lower_cylinder.MARKER_406'.format(model_name)
        MARKER_406.location = Base.Vector (6.1976, 0.0, 1.197)
        MARKER_406.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_406.location, MARKER_406.orientation)
        MARKER_406.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_406.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_407 = MakeSceneNodeByType('Marker', '.{}.ges_upper_cylinder.MARKER_407'.format(model_name))
        MARKER_407.marker_name = '.{}.ges_upper_cylinder.MARKER_407'.format(model_name)
        MARKER_407.location = Base.Vector (6.1976, 0.0, 1.6256)
        MARKER_407.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_407.location, MARKER_407.orientation)
        MARKER_407.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_407.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_408 = MakeSceneNodeByType('Marker', '.{}.ges_lower_cylinder.MARKER_408'.format(model_name))
        MARKER_408.marker_name = '.{}.ges_lower_cylinder.MARKER_408'.format(model_name)
        MARKER_408.location = Base.Vector (6.1976, 0.0, 1.197)
        MARKER_408.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_408.location, MARKER_408.orientation)
        MARKER_408.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_408.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_409 = MakeSceneNodeByType('Marker', '.{}.ges_upper_cylinder.MARKER_409'.format(model_name))
        MARKER_409.marker_name = '.{}.ges_upper_cylinder.MARKER_409'.format(model_name)
        MARKER_409.location = Base.Vector (6.1976, 0.0, 1.6256)
        MARKER_409.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_409.location, MARKER_409.orientation)
        MARKER_409.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_409.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_410 = MakeSceneNodeByType('Marker', '.{}.ges_lower_cylinder.MARKER_410'.format(model_name))
        MARKER_410.marker_name = '.{}.ges_lower_cylinder.MARKER_410'.format(model_name)
        MARKER_410.location = Base.Vector (6.1976, 0.0, 1.197)
        MARKER_410.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, MARKER_410.location, MARKER_410.orientation)
        MARKER_410.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_410.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        gel_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.gel_upper_cylinder'.format(model_name))

        MARKER_411 = MakeSceneNodeByType('Marker', '.{}.gel_upper_cylinder.MARKER_411'.format(model_name))
        MARKER_411.marker_name = '.{}.gel_upper_cylinder.MARKER_411'.format(model_name)
        MARKER_411.location = Base.Vector (12.137340597, -1.4390607744, 2.1534060818)
        MARKER_411.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(gel_upper_cylinder.location, gel_upper_cylinder.orientation, MARKER_411.location, MARKER_411.orientation)
        MARKER_411.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_411.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        gel_lower_cylinder = Jusme.ActiveUSScene.getObject('.{}.gel_lower_cylinder'.format(model_name))

        MARKER_412 = MakeSceneNodeByType('Marker', '.{}.gel_lower_cylinder.MARKER_412'.format(model_name))
        MARKER_412.marker_name = '.{}.gel_lower_cylinder.MARKER_412'.format(model_name)
        MARKER_412.location = Base.Vector (12.2057611337, -1.486765747, 1.1425793908)
        MARKER_412.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(gel_lower_cylinder.location, gel_lower_cylinder.orientation, MARKER_412.location, MARKER_412.orientation)
        MARKER_412.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_412.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_413 = MakeSceneNodeByType('Marker', '.{}.gel_upper_cylinder.MARKER_413'.format(model_name))
        MARKER_413.marker_name = '.{}.gel_upper_cylinder.MARKER_413'.format(model_name)
        MARKER_413.location = Base.Vector (12.137340597, -1.4390607744, 2.1534060818)
        MARKER_413.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(gel_upper_cylinder.location, gel_upper_cylinder.orientation, MARKER_413.location, MARKER_413.orientation)
        MARKER_413.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_413.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_414 = MakeSceneNodeByType('Marker', '.{}.gel_lower_cylinder.MARKER_414'.format(model_name))
        MARKER_414.marker_name = '.{}.gel_lower_cylinder.MARKER_414'.format(model_name)
        MARKER_414.location = Base.Vector (12.2057611337, -1.486765747, 1.1425793908)
        MARKER_414.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(gel_lower_cylinder.location, gel_lower_cylinder.orientation, MARKER_414.location, MARKER_414.orientation)
        MARKER_414.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_414.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_415 = MakeSceneNodeByType('Marker', '.{}.gel_upper_cylinder.MARKER_415'.format(model_name))
        MARKER_415.marker_name = '.{}.gel_upper_cylinder.MARKER_415'.format(model_name)
        MARKER_415.location = Base.Vector (12.137340597, -1.4390607744, 2.1534060818)
        MARKER_415.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(gel_upper_cylinder.location, gel_upper_cylinder.orientation, MARKER_415.location, MARKER_415.orientation)
        MARKER_415.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_415.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_416 = MakeSceneNodeByType('Marker', '.{}.gel_lower_cylinder.MARKER_416'.format(model_name))
        MARKER_416.marker_name = '.{}.gel_lower_cylinder.MARKER_416'.format(model_name)
        MARKER_416.location = Base.Vector (12.2057611337, -1.486765747, 1.1425793908)
        MARKER_416.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(gel_lower_cylinder.location, gel_lower_cylinder.orientation, MARKER_416.location, MARKER_416.orientation)
        MARKER_416.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_416.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        ger_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.ger_upper_cylinder'.format(model_name))

        MARKER_417 = MakeSceneNodeByType('Marker', '.{}.ger_upper_cylinder.MARKER_417'.format(model_name))
        MARKER_417.marker_name = '.{}.ger_upper_cylinder.MARKER_417'.format(model_name)
        MARKER_417.location = Base.Vector (12.137340597, 1.4390607744, 2.1534060818)
        MARKER_417.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ger_upper_cylinder.location, ger_upper_cylinder.orientation, MARKER_417.location, MARKER_417.orientation)
        MARKER_417.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_417.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        ger_lower_cylinder = Jusme.ActiveUSScene.getObject('.{}.ger_lower_cylinder'.format(model_name))

        MARKER_418 = MakeSceneNodeByType('Marker', '.{}.ger_lower_cylinder.MARKER_418'.format(model_name))
        MARKER_418.marker_name = '.{}.ger_lower_cylinder.MARKER_418'.format(model_name)
        MARKER_418.location = Base.Vector (12.2057611337, 1.486765747, 1.1425793908)
        MARKER_418.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ger_lower_cylinder.location, ger_lower_cylinder.orientation, MARKER_418.location, MARKER_418.orientation)
        MARKER_418.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_418.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_419 = MakeSceneNodeByType('Marker', '.{}.ger_upper_cylinder.MARKER_419'.format(model_name))
        MARKER_419.marker_name = '.{}.ger_upper_cylinder.MARKER_419'.format(model_name)
        MARKER_419.location = Base.Vector (12.137340597, 1.4390607744, 2.1534060818)
        MARKER_419.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ger_upper_cylinder.location, ger_upper_cylinder.orientation, MARKER_419.location, MARKER_419.orientation)
        MARKER_419.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_419.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_420 = MakeSceneNodeByType('Marker', '.{}.ger_lower_cylinder.MARKER_420'.format(model_name))
        MARKER_420.marker_name = '.{}.ger_lower_cylinder.MARKER_420'.format(model_name)
        MARKER_420.location = Base.Vector (12.2057611337, 1.486765747, 1.1425793908)
        MARKER_420.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ger_lower_cylinder.location, ger_lower_cylinder.orientation, MARKER_420.location, MARKER_420.orientation)
        MARKER_420.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_420.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_421 = MakeSceneNodeByType('Marker', '.{}.ger_upper_cylinder.MARKER_421'.format(model_name))
        MARKER_421.marker_name = '.{}.ger_upper_cylinder.MARKER_421'.format(model_name)
        MARKER_421.location = Base.Vector (12.137340597, 1.4390607744, 2.1534060818)
        MARKER_421.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ger_upper_cylinder.location, ger_upper_cylinder.orientation, MARKER_421.location, MARKER_421.orientation)
        MARKER_421.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_421.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_422 = MakeSceneNodeByType('Marker', '.{}.ger_lower_cylinder.MARKER_422'.format(model_name))
        MARKER_422.marker_name = '.{}.ger_lower_cylinder.MARKER_422'.format(model_name)
        MARKER_422.location = Base.Vector (12.2057611337, 1.486765747, 1.1425793908)
        MARKER_422.orientation = Base.Vector (0.0, 0.0, 0.0)
        loc_ori = VecUtils.global2local(ger_lower_cylinder.location, ger_lower_cylinder.orientation, MARKER_422.location, MARKER_422.orientation)
        MARKER_422.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_422.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        

        LMLG_AIR = MakeSceneNodeByType('ForceSingleComponent', '.{}.LMLG_AIR'.format(model_name))
        LMLG_AIR.type_of_freedom = "translational"
        LMLG_AIR.freedom_opt = 0
        LMLG_AIR.action_only = False
        LMLG_AIR.function_opt = 0
        LMLG_AIR.function = "1*.{}.NLG_Aa*(.{}.NLG_P0*(.{}.NLG_V0/(.{}.NLG_V0-.{}.NLG_Aa*(0.4286-DM(.{}.ges_upper_cylinder.MARKER_2,.{}.ges_lower_cylinder.MARKER_1))))**GAMA-.{}.Patm)".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MARKER_405 = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder.MARKER_405'.format(model_name))
        if not MARKER_405 :
            print("MARKER_405")
            return
        MARKER_406 = Jusme.ActiveUSScene.getObject('.{}.ges_lower_cylinder.MARKER_406'.format(model_name))
        if not MARKER_406 :
            print("MARKER_406")
            return
        LMLG_AIR.position_define_opt = 1
        LMLG_AIR.i_marker_name = MARKER_405
        LMLG_AIR.j_marker_name = MARKER_406

        NLG_OIL = MakeSceneNodeByType('ForceSingleComponent', '.{}.NLG_OIL'.format(model_name))
        NLG_OIL.type_of_freedom = "translational"
        NLG_OIL.freedom_opt = 0
        NLG_OIL.action_only = False
        NLG_OIL.function_opt = 0
        NLG_OIL.function = "IF(VARVAL(.{}.NLG_V):1*-1*(VARVAL(.{}.NLG_V)*0.5*(VARVAL(.{}.NLG_V)-ABS(VARVAL(.{}.NLG_V)))*((.{}.rou*.{}.NLG_Ah**3/(2*.{}.NLG_Ch**2*.{}.NLG_Ahdl**2))+(.{}.rou*.{}.NLG_As**3/(2*.{}.NLG_Cs**2*.{}.NLG_Asdl**2)))),0,1*VARVAL(.{}.NLG_V)*0.5*(VARVAL(.{}.NLG_V)+ABS(VARVAL(.{}.NLG_V)))*((.{}.rou*.{}.NLG_Ah**3/(2*.{}.NLG_Ch**2*.{}.NLG_Ahd**2))+(.{}.rou*.{}.NLG_As**3/(2*.{}.NLG_Cs**2*.{}.NLG_Asd**2))))".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MARKER_407 = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder.MARKER_407'.format(model_name))
        if not MARKER_407 :
            print("MARKER_407")
            return
        MARKER_408 = Jusme.ActiveUSScene.getObject('.{}.ges_lower_cylinder.MARKER_408'.format(model_name))
        if not MARKER_408 :
            print("MARKER_408")
            return
        NLG_OIL.position_define_opt = 1
        NLG_OIL.i_marker_name = MARKER_407
        NLG_OIL.j_marker_name = MARKER_408

        NLG_STOP = MakeSceneNodeByType('ForceSingleComponent', '.{}.NLG_STOP'.format(model_name))
        NLG_STOP.type_of_freedom = "translational"
        NLG_STOP.freedom_opt = 0
        NLG_STOP.action_only = False
        NLG_STOP.function_opt = 0
        NLG_STOP.function = "IF(0.4286-DM(.{}.ges_upper_cylinder.MARKER_2,.{}.ges_lower_cylinder.MARKER_1) :1.0E+09*(0.4286-DM(.{}.ges_upper_cylinder.MARKER_2,.{}.ges_lower_cylinder.MARKER_1)), 0 , 0 )".format(model_name,model_name,model_name,model_name)
        MARKER_409 = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder.MARKER_409'.format(model_name))
        if not MARKER_409 :
            print("MARKER_409")
            return
        MARKER_410 = Jusme.ActiveUSScene.getObject('.{}.ges_lower_cylinder.MARKER_410'.format(model_name))
        if not MARKER_410 :
            print("MARKER_410")
            return
        NLG_STOP.position_define_opt = 1
        NLG_STOP.i_marker_name = MARKER_409
        NLG_STOP.j_marker_name = MARKER_410

        LMLG_AIR = MakeSceneNodeByType('ForceSingleComponent', '.{}.LMLG_AIR'.format(model_name))
        LMLG_AIR.type_of_freedom = "translational"
        LMLG_AIR.freedom_opt = 0
        LMLG_AIR.action_only = False
        LMLG_AIR.function_opt = 0
        LMLG_AIR.function = ".{}.MLG_Aa*(.{}.MLG_P0*(.{}.MLG_V0/(.{}.MLG_V0-.{}.MLG_Aa*VARVAL(.{}.LMLG_S)))**GAMA-.{}.Patm)".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MARKER_411 = Jusme.ActiveUSScene.getObject('.{}.gel_upper_cylinder.MARKER_411'.format(model_name))
        if not MARKER_411 :
            print("MARKER_411")
            return
        MARKER_412 = Jusme.ActiveUSScene.getObject('.{}.gel_lower_cylinder.MARKER_412'.format(model_name))
        if not MARKER_412 :
            print("MARKER_412")
            return
        LMLG_AIR.position_define_opt = 1
        LMLG_AIR.i_marker_name = MARKER_411
        LMLG_AIR.j_marker_name = MARKER_412

        LMLG_OIL = MakeSceneNodeByType('ForceSingleComponent', '.{}.LMLG_OIL'.format(model_name))
        LMLG_OIL.type_of_freedom = "translational"
        LMLG_OIL.freedom_opt = 0
        LMLG_OIL.action_only = False
        LMLG_OIL.function_opt = 0
        LMLG_OIL.function = "IF(VARVAL(.{}.LMLG_V):2*-1*(VARVAL(.{}.LMLG_V)*0.5*(VARVAL(.{}.LMLG_V)-ABS(VARVAL(.{}.LMLG_V)))*((.{}.rou*.{}.MLG_Ah**3/(2*.{}.MLG_Ch**2*.{}.MLG_Ahdl**2))+(.{}.rou*.{}.MLG_As**3/(2*.{}.MLG_Cs**2*.{}.MLG_Asdl**2)))),0,2*VARVAL(.{}.LMLG_V)*0.5*(VARVAL(.{}.LMLG_V)+ABS(VARVAL(.{}.LMLG_V)))*((.{}.rou*.{}.MLG_Ah**3/(2*.{}.MLG_Ch**2*.{}.MLG_Ahd**2))+(.{}.rou*.{}.MLG_As**3/(2*.{}.MLG_Cs**2*.{}.MLG_Asd**2))))".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MARKER_413 = Jusme.ActiveUSScene.getObject('.{}.gel_upper_cylinder.MARKER_413'.format(model_name))
        if not MARKER_413 :
            print("MARKER_413")
            return
        MARKER_414 = Jusme.ActiveUSScene.getObject('.{}.gel_lower_cylinder.MARKER_414'.format(model_name))
        if not MARKER_414 :
            print("MARKER_414")
            return
        LMLG_OIL.position_define_opt = 1
        LMLG_OIL.i_marker_name = MARKER_413
        LMLG_OIL.j_marker_name = MARKER_414

        LMLG_STOP = MakeSceneNodeByType('ForceSingleComponent', '.{}.LMLG_STOP'.format(model_name))
        LMLG_STOP.type_of_freedom = "translational"
        LMLG_STOP.freedom_opt = 0
        LMLG_STOP.action_only = False
        LMLG_STOP.function_opt = 0
        LMLG_STOP.function = "IF(1.014262-DM(.{}.gel_upper_cylinder.MARKER_272,.{}.gel_lower_cylinder.MARKER_273) :1.0E+09*(1.014262-DM(.{}.gel_upper_cylinder.MARKER_272,.{}.gel_lower_cylinder.MARKER_273)) , 0 , 0 )".format(model_name,model_name,model_name,model_name)
        MARKER_415 = Jusme.ActiveUSScene.getObject('.{}.gel_upper_cylinder.MARKER_415'.format(model_name))
        if not MARKER_415 :
            print("MARKER_415")
            return
        MARKER_416 = Jusme.ActiveUSScene.getObject('.{}.gel_lower_cylinder.MARKER_416'.format(model_name))
        if not MARKER_416 :
            print("MARKER_416")
            return
        LMLG_STOP.position_define_opt = 1
        LMLG_STOP.i_marker_name = MARKER_415
        LMLG_STOP.j_marker_name = MARKER_416

        RMLG_AIR = MakeSceneNodeByType('ForceSingleComponent', '.{}.RMLG_AIR'.format(model_name))
        RMLG_AIR.type_of_freedom = "translational"
        RMLG_AIR.freedom_opt = 0
        RMLG_AIR.action_only = False
        RMLG_AIR.function_opt = 0
        RMLG_AIR.function = ".{}.MLG_Aa*(.{}.MLG_P0*(.{}.MLG_V0/(.{}.MLG_V0-.{}.MLG_Aa*VARVAL(.{}.RMLG_S)))**GAMA-.{}.Patm)".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MARKER_417 = Jusme.ActiveUSScene.getObject('.{}.ger_upper_cylinder.MARKER_417'.format(model_name))
        if not MARKER_417 :
            print("MARKER_417")
            return
        MARKER_418 = Jusme.ActiveUSScene.getObject('.{}.ger_lower_cylinder.MARKER_418'.format(model_name))
        if not MARKER_418 :
            print("MARKER_418")
            return
        RMLG_AIR.position_define_opt = 1
        RMLG_AIR.i_marker_name = MARKER_417
        RMLG_AIR.j_marker_name = MARKER_418

        RMLG_OIL = MakeSceneNodeByType('ForceSingleComponent', '.{}.RMLG_OIL'.format(model_name))
        RMLG_OIL.type_of_freedom = "translational"
        RMLG_OIL.freedom_opt = 0
        RMLG_OIL.action_only = False
        RMLG_OIL.function_opt = 0
        RMLG_OIL.function = "IF(VARVAL(.{}.RMLG_V):2*-1*(VARVAL(.{}.RMLG_V)*0.5*(VARVAL(.{}.RMLG_V)-ABS(VARVAL(.{}.RMLG_V)))*((.{}.rou*.{}.MLG_Ah**3/(2*.{}.MLG_Ch**2*.{}.MLG_Ahdl**2))+(.{}.rou*.{}.MLG_As**3/(2*.{}.MLG_Cs**2*.{}.MLG_Asdl**2)))),0,2*VARVAL(.{}.RMLG_V)*0.5*(VARVAL(.{}.RMLG_V)+ABS(VARVAL(.{}.RMLG_V)))*((.{}.rou*.{}.MLG_Ah**3/(2*.{}.MLG_Ch**2*.{}.MLG_Ahd**2))+(.{}.rou*.{}.MLG_As**3/(2*.{}.MLG_Cs**2*.{}.MLG_Asd**2))))".format(model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name,model_name)
        MARKER_419 = Jusme.ActiveUSScene.getObject('.{}.ger_upper_cylinder.MARKER_419'.format(model_name))
        if not MARKER_419 :
            print("MARKER_419")
            return
        MARKER_420 = Jusme.ActiveUSScene.getObject('.{}.ger_lower_cylinder.MARKER_420'.format(model_name))
        if not MARKER_420 :
            print("MARKER_420")
            return
        RMLG_OIL.position_define_opt = 1
        RMLG_OIL.i_marker_name = MARKER_419
        RMLG_OIL.j_marker_name = MARKER_420

        RMLG_STOP = MakeSceneNodeByType('ForceSingleComponent', '.{}.RMLG_STOP'.format(model_name))
        RMLG_STOP.type_of_freedom = "translational"
        RMLG_STOP.freedom_opt = 0
        RMLG_STOP.action_only = False
        RMLG_STOP.function_opt = 0
        RMLG_STOP.function = "IF(1.014262-DM(.{}.ger_upper_cylinder.MARKER_278,.{}.ger_lower_cylinder.MARKER_279) :1.0E+09*(1.014262-DM(.{}.ger_upper_cylinder.MARKER_278,.{}.ger_lower_cylinder.MARKER_279)) , 0 ,0 )".format(model_name,model_name,model_name,model_name)
        MARKER_421 = Jusme.ActiveUSScene.getObject('.{}.ger_upper_cylinder.MARKER_421'.format(model_name))
        if not MARKER_421 :
            print("MARKER_421")
            return
        MARKER_422 = Jusme.ActiveUSScene.getObject('.{}.ger_lower_cylinder.MARKER_422'.format(model_name))
        if not MARKER_422 :
            print("MARKER_422")
            return
        RMLG_STOP.position_define_opt = 1
        RMLG_STOP.i_marker_name = MARKER_421
        RMLG_STOP.j_marker_name = MARKER_422
        pass

    def InitJoint(self) :
        print("进入落震初始化约束程序")

        model_name = Common.getModelName()
        #-----创建部件之间的约束
        #-----先创建约束需要的marker点


        #----创建joscly_db_sf
        PART_46 = Jusme.ActiveUSScene.getObject('.{}.PART_46'.format(model_name))
        ges_dragbrace = Jusme.ActiveUSScene.getObject('.{}.ges_dragbrace'.format(model_name))
        hps_db_sf_atch = Jusme.ActiveUSScene.getObject('.{}.ground.hps_db_sf_atch'.format(model_name))

        MARKER_581 = MakeSceneNodeByType('Marker', '.{}.PART_46.MARKER_581'.format(model_name))
        MARKER_581.marker_name = '.{}.PART_46.MARKER_581'.format(model_name)
        MARKER_581.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        MARKER_581.orientation = Base.Vector (162.3096284375, 104.8061609624, 180.0)
        loc_ori = VecUtils.global2local(PART_46.location, PART_46.orientation, MARKER_581.location, MARKER_581.orientation)
        MARKER_581.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_581.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        MARKER_580 = MakeSceneNodeByType('Marker', '.{}.ges_dragbrace.MARKER_580'.format(model_name))
        MARKER_580.marker_name = '.{}.ges_dragbrace.MARKER_580'.format(model_name)
        MARKER_580.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_sf_atch))
        MARKER_580.orientation = Base.Vector (162.3096284375, 104.8061609624, 180.0)
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, MARKER_580.location, MARKER_580.orientation)
        MARKER_580.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_580.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        joscly_db_sf = MakeSceneNodeByType('JointCylinder', '.{}.joscly_db_sf'.format(model_name))
        MARKER_581 = Jusme.ActiveUSScene.getObject('.{}.PART_46.MARKER_581'.format(model_name))
        if not MARKER_581 :
            print("MARKER_581")
            return
        MARKER_580 = Jusme.ActiveUSScene.getObject('.{}.ges_dragbrace.MARKER_580'.format(model_name))
        if not MARKER_580 :
            print("MARKER_580")
            return
        joscly_db_sf.position_define_opt = 1
        joscly_db_sf.i_marker_name = MARKER_580
        joscly_db_sf.j_marker_name = MARKER_581


        #----创建jossph_db_uc_joint
        ges_dragbrace = Jusme.ActiveUSScene.getObject('.{}.ges_dragbrace'.format(model_name))
        ges_upper_cylinder = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder'.format(model_name))
        hps_db_uc_atch = Jusme.ActiveUSScene.getObject('.{}.ground.hps_db_uc_atch'.format(model_name))

        jxs_joint_j_12 = MakeSceneNodeByType('Marker', '.{}.ges_upper_cylinder.jxs_joint_j_12'.format(model_name))
        jxs_joint_j_12.marker_name = '.{}.ges_upper_cylinder.jxs_joint_j_12'.format(model_name)
        jxs_joint_j_12.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_uc_atch))
        jxs_joint_j_12.orientation = Base.Vector (0,0,0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, jxs_joint_j_12.location, jxs_joint_j_12.orientation)
        jxs_joint_j_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_j_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jxs_joint_i_12 = MakeSceneNodeByType('Marker', '.{}.ges_dragbrace.jxs_joint_i_12'.format(model_name))
        jxs_joint_i_12.marker_name = '.{}.ges_dragbrace.jxs_joint_i_12'.format(model_name)
        jxs_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_db_uc_atch))
        jxs_joint_i_12.orientation = Base.Vector (0,0,0)
        loc_ori = VecUtils.global2local(ges_dragbrace.location, ges_dragbrace.orientation, jxs_joint_i_12.location, jxs_joint_i_12.orientation)
        jxs_joint_i_12.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        jxs_joint_i_12.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        jossph_db_uc_joint = MakeSceneNodeByType('JointSpherical', '.{}.jossph_db_uc_joint'.format(model_name))
        jxs_joint_j_12 = Jusme.ActiveUSScene.getObject('.{}.ges_upper_cylinder.jxs_joint_j_12'.format(model_name))
        if not jxs_joint_j_12 :
            print("jxs_joint_j_12")
            return
        jxs_joint_i_12 = Jusme.ActiveUSScene.getObject('.{}.ges_dragbrace.jxs_joint_i_12'.format(model_name))
        if not jxs_joint_i_12 :
            print("jxs_joint_i_12")
            return
        jossph_db_uc_joint.position_define_opt = 1
        jossph_db_uc_joint.i_marker_name = jxs_joint_i_12
        jossph_db_uc_joint.j_marker_name = jxs_joint_j_12


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

        JOINT_56 = MakeSceneNodeByType('JointFixed', '.{}.JOINT_56'.format(model_name))
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

        JOINT_59 = MakeSceneNodeByType('JointFixed', '.{}.JOINT_59'.format(model_name))
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

        JOINT_60 = MakeSceneNodeByType('JointFixed', '.{}.JOINT_60'.format(model_name))
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
        print("进入落震初始化驱动程序")
        #无需添加驱动
        pass

    def InitMeasure(self) :
        print("进入落震初始化测量程序")
        #无需添加测量
        pass
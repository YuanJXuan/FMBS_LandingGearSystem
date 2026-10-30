import Common

class Variable :
    #-----------------构造函数
    def __init__(self, name, type):
        self.variable_name = name
        self.variable_type = type

        self.chinese_name_list = []
        self.english_name_list = []
        self.value_list = []
        self.name_val_dic = {}
        pass


class TurnVariable(Variable) :
    # chinese_name_list = []
    # english_name_list = []
    # value_list = []
    # name_val_dic = {}

    #-----------------构造函数
    def __init__(self, name, type):
        super(TurnVariable, self).__init__(name, type)
        self.Init()
        pass

    def Init(self) :
        #---------------初始化中文参数
        self.chinese_name_list.append("主起回油腔油孔缩流系数")
        self.chinese_name_list.append("主起主油腔油孔缩流系数")
        self.chinese_name_list.append("主起回油腔反行程油孔面积")
        self.chinese_name_list.append("主起回油腔正行程油孔面积")
        self.chinese_name_list.append("主起主油腔反行程油孔面积")

        self.chinese_name_list.append("主起主油腔正行程油孔面积")
        self.chinese_name_list.append("主起回油腔压油面积")
        self.chinese_name_list.append("主起主油腔压油面积")
        self.chinese_name_list.append("主起初始气压")
        self.chinese_name_list.append("主起初始气腔容积")

        self.chinese_name_list.append("主起压气面积")
        self.chinese_name_list.append("前起回油腔油孔缩流系数")
        self.chinese_name_list.append("前起主油腔油孔缩流系数")
        self.chinese_name_list.append("前起回油腔反行程油孔面积")
        self.chinese_name_list.append("前起回油腔正行程油孔面积")

        self.chinese_name_list.append("前起主油腔反行程油孔面积")
        self.chinese_name_list.append("前起主油腔正行程油孔面积")
        self.chinese_name_list.append("前起回油腔压油面积")
        self.chinese_name_list.append("前起主油腔压油面积")
        self.chinese_name_list.append("油液密度")

        self.chinese_name_list.append("标准大气压")
        self.chinese_name_list.append("前起初始气压")
        self.chinese_name_list.append("前起初始气腔容积")
        self.chinese_name_list.append("多变指数")
        self.chinese_name_list.append("前起压气面积")

        self.chinese_name_list.append("转弯力设定角度")
        self.chinese_name_list.append("驱动设定角度")
        self.chinese_name_list.append("转弯速度")
        self.chinese_name_list.append("转弯开始时间")
        self.chinese_name_list.append("转弯结束时间")

        #------------初始化英文名称
        self.english_name_list.append("MLG_Cs")
        self.english_name_list.append("MLG_Ch")
        self.english_name_list.append("MLG_Asdl")
        self.english_name_list.append("MLG_Asd")
        self.english_name_list.append("MLG_Ahdl")

        self.english_name_list.append("MLG_Ahd")
        self.english_name_list.append("MLG_As")
        self.english_name_list.append("MLG_Ah")
        self.english_name_list.append("MLG_P0")
        self.english_name_list.append("MLG_V0")

        self.english_name_list.append("MLG_Aa")
        self.english_name_list.append("NLG_Cs")
        self.english_name_list.append("NLG_Ch")
        self.english_name_list.append("NLG_Asdl")
        self.english_name_list.append("NLG_Asd")

        self.english_name_list.append("NLG_Ahdl")
        self.english_name_list.append("NLG_Ahd")
        self.english_name_list.append("NLG_As")
        self.english_name_list.append("NLG_Ah")
        self.english_name_list.append("rou")

        self.english_name_list.append("Patm")
        self.english_name_list.append("NLG_P0")
        self.english_name_list.append("NLG_V0")
        self.english_name_list.append("GAMA")
        self.english_name_list.append("NLG_Aa")

        self.english_name_list.append("JD_sheding_2")
        self.english_name_list.append("JD_sheding_1")
        self.english_name_list.append("V_sheding")
        self.english_name_list.append("T_1")
        self.english_name_list.append("T_2")


        model_name = Common.getModelName()
        for i in range(30) :
            var_name = ".{}.{}".format(model_name, self.english_name_list[i])
            var_list = Common.getDesignVariable(var_name)
            if var_list.__len__() != 0 :
                self.name_val_dic[self.english_name_list[i]] = var_list[0]
            else :
                self.name_val_dic[self.english_name_list[i]] = 0
        pass



class BrakeVariable(Variable) :
    # chinese_name_list = []
    # english_name_list = []
    # value_list = []

    #-----------------构造函数
    def __init__(self, name, type):
        super(BrakeVariable, self).__init__(name, type)
        self.Init()
        pass

    def Init(self) :
        self.chinese_name_list.append("主起回油腔油孔缩流系数")
        self.chinese_name_list.append("主起主油腔油孔缩流系数")
        self.chinese_name_list.append("主起回油腔反行程油孔面积")
        self.chinese_name_list.append("主起回油腔正行程油孔面积")
        self.chinese_name_list.append("主起主油腔反行程油孔面积")

        self.chinese_name_list.append("主起主油腔正行程油孔面积")
        self.chinese_name_list.append("主起回油腔压油面积")
        self.chinese_name_list.append("主起主油腔压油面积")
        self.chinese_name_list.append("主起初始气压")
        self.chinese_name_list.append("主起初始气腔容积")

        self.chinese_name_list.append("主起压气面积")
        self.chinese_name_list.append("前起回油腔油孔缩流系数")
        self.chinese_name_list.append("前起主油腔油孔缩流系数")
        self.chinese_name_list.append("前起回油腔反行程油孔面积")
        self.chinese_name_list.append("前起回油腔正行程油孔面积")

        self.chinese_name_list.append("前起主油腔反行程油孔面积")
        self.chinese_name_list.append("前起主油腔正行程油孔面积")
        self.chinese_name_list.append("前起回油腔压油面积")
        self.chinese_name_list.append("前起主油腔压油面积")
        self.chinese_name_list.append("油液密度")

        self.chinese_name_list.append("标准大气压")
        self.chinese_name_list.append("前起初始气压")
        self.chinese_name_list.append("前起初始气腔容积")
        self.chinese_name_list.append("多变指数")
        self.chinese_name_list.append("前起压气面积")

        self.chinese_name_list.append("设定速度")
        self.chinese_name_list.append("刹车力矩")

        #------------初始化英文名称
        self.english_name_list.append("MLG_Cs")
        self.english_name_list.append("MLG_Ch")
        self.english_name_list.append("MLG_Asdl")
        self.english_name_list.append("MLG_Asd")
        self.english_name_list.append("MLG_Ahdl")

        self.english_name_list.append("MLG_Ahd")
        self.english_name_list.append("MLG_As")
        self.english_name_list.append("MLG_Ah")
        self.english_name_list.append("MLG_P0")
        self.english_name_list.append("MLG_V0")

        self.english_name_list.append("MLG_Aa")
        self.english_name_list.append("NLG_Cs")
        self.english_name_list.append("NLG_Ch")
        self.english_name_list.append("NLG_Asdl")
        self.english_name_list.append("NLG_Asd")

        self.english_name_list.append("NLG_Ahdl")
        self.english_name_list.append("NLG_Ahd")
        self.english_name_list.append("NLG_As")
        self.english_name_list.append("NLG_Ah")
        self.english_name_list.append("rou")

        self.english_name_list.append("Patm")
        self.english_name_list.append("NLG_P0")
        self.english_name_list.append("NLG_V0")
        self.english_name_list.append("GAMA")
        self.english_name_list.append("NLG_Aa")

        self.english_name_list.append("V_sheding")
        self.english_name_list.append("M")


        model_name = Common.getModelName()
        for i in range(27) :
            var_name = ".{0}.{1}".format(model_name, self.english_name_list[i])
            var_list = Common.getDesignVariable(var_name)
            if var_list.__len__() != 0 :
                self.name_val_dic[self.english_name_list[i]] = var_list[0]
            else :
                self.name_val_dic[self.english_name_list[i]] = 0
        pass


        # for i in range(27) :
        #     self.value_list.append(0)
        #     self.name_val_dic[self.english_name_list[i]] = 0


        pass


class DropVariable(Variable) :
    # chinese_name_list = []
    # english_name_list = []
    # value_list = []

    def __init__(self, name, type):
        super(DropVariable, self).__init__(name, type)
        self.Init()
        pass


    def Init(self) :

        #---------------初始化中文参数
        self.chinese_name_list.append("主起回油腔油孔缩流系数")
        self.chinese_name_list.append("主起主油腔油孔缩流系数")
        self.chinese_name_list.append("主起回油腔反行程油孔面积")
        self.chinese_name_list.append("主起回油腔正行程油孔面积")
        self.chinese_name_list.append("主起主油腔反行程油孔面积")

        self.chinese_name_list.append("主起主油腔正行程油孔面积")
        self.chinese_name_list.append("主起回油腔压油面积")
        self.chinese_name_list.append("主起主油腔压油面积")
        self.chinese_name_list.append("主起初始气压")
        self.chinese_name_list.append("主起初始气腔容积")

        self.chinese_name_list.append("主起压气面积")
        self.chinese_name_list.append("前起回油腔油孔缩流系数")
        self.chinese_name_list.append("前起主油腔油孔缩流系数")
        self.chinese_name_list.append("前起回油腔反行程油孔面积")
        self.chinese_name_list.append("前起回油腔正行程油孔面积")

        self.chinese_name_list.append("前起主油腔反行程油孔面积")
        self.chinese_name_list.append("前起主油腔正行程油孔面积")
        self.chinese_name_list.append("前起回油腔压油面积")
        self.chinese_name_list.append("前起主油腔压油面积")
        self.chinese_name_list.append("油液密度")

        self.chinese_name_list.append("标准大气压")
        self.chinese_name_list.append("前起初始气压")
        self.chinese_name_list.append("前起初始气腔容积")
        self.chinese_name_list.append("多变指数")
        self.chinese_name_list.append("前起压气面积")


        #------------初始化英文名称
        self.english_name_list.append("MLG_Cs")
        self.english_name_list.append("MLG_Ch")
        self.english_name_list.append("MLG_Asdl")
        self.english_name_list.append("MLG_Asd")
        self.english_name_list.append("MLG_Ahdl")

        self.english_name_list.append("MLG_Ahd")
        self.english_name_list.append("MLG_As")
        self.english_name_list.append("MLG_Ah")
        self.english_name_list.append("MLG_P0")
        self.english_name_list.append("MLG_V0")

        self.english_name_list.append("MLG_Aa")
        self.english_name_list.append("NLG_Cs")
        self.english_name_list.append("NLG_Ch")
        self.english_name_list.append("NLG_Asdl")
        self.english_name_list.append("NLG_Asd")

        self.english_name_list.append("NLG_Ahdl")
        self.english_name_list.append("NLG_Ahd")
        self.english_name_list.append("NLG_As")
        self.english_name_list.append("NLG_Ah")
        self.english_name_list.append("rou")

        self.english_name_list.append("Patm")
        self.english_name_list.append("NLG_P0")
        self.english_name_list.append("NLG_V0")
        self.english_name_list.append("GAMA")
        self.english_name_list.append("NLG_Aa")

        #-----------------初始化设计变量数值
        model_name = Common.getModelName()
        for i in range(25) :
            var_name = ".{}.{}".format(model_name, self.english_name_list[i])
            var_list = Common.getDesignVariable(var_name)
            if var_list.__len__() != 0 :
                self.name_val_dic[self.english_name_list[i]] = var_list[0]
            else :
                self.name_val_dic[self.english_name_list[i]] = 0
        pass
        # for i in range(25) :
        #     self.value_list.append(0)
        #     self.name_val_dic[self.english_name_list[i]] = 0


        pass

class RetractVariable(Variable) :
    # chinese_name_list = []
    # english_name_list = []
    # value_list = []

    def __init__(self, name, type):
        super(RetractVariable, self).__init__(name, type)
        self.Init()
        pass

    def Init(self) :

        #---------------初始化中文参数
        self.chinese_name_list.append("主起作动筒行程")
        self.chinese_name_list.append("前起作动筒行程")
        self.chinese_name_list.append("主起阻力系数")
        self.chinese_name_list.append("主起投影面积")
        self.chinese_name_list.append("主起放下时间")

        self.chinese_name_list.append("主起上位时间")
        self.chinese_name_list.append("主起收起时间")
        self.chinese_name_list.append("前起放下时间")
        self.chinese_name_list.append("前起上位时间")
        self.chinese_name_list.append("前起收起时间")

        self.chinese_name_list.append("前起放下载荷")
        self.chinese_name_list.append("前起收起载荷")
        self.chinese_name_list.append("前起投影面积")
        self.chinese_name_list.append("前起阻力系数")
        self.chinese_name_list.append("密度")

        self.chinese_name_list.append("风速")

        #------------初始化英文名称
        self.english_name_list.append("MLG_ret_disp")
        self.english_name_list.append("NLG_ret_disp")
        self.english_name_list.append("C0_MLG")
        self.english_name_list.append("pa_MLG")
        self.english_name_list.append("mlg_down_time")

        self.english_name_list.append("mlg_hold_time")
        self.english_name_list.append("mlg_up_time")
        self.english_name_list.append("nlg_down_time")
        self.english_name_list.append("nlg_hold_time")
        self.english_name_list.append("nlg_up_time")

        self.english_name_list.append("zdt_down")
        self.english_name_list.append("zdt_up")
        self.english_name_list.append("pa")
        self.english_name_list.append("C0")
        self.english_name_list.append("mi_du")

        self.english_name_list.append("windV")

        #--------------初始化设计变量数据
        #-----------------初始化设计变量数值
        model_name = Common.getModelName()
        for i in range(16) :
            var_name = ".{}.{}".format(model_name, self.english_name_list[i])
            var_list = Common.getDesignVariable(var_name)
            if var_list.__len__() != 0 :
                self.name_val_dic[self.english_name_list[i]] = var_list[0]
            else :
                self.name_val_dic[self.english_name_list[i]] = 0
        pass
        # for i in range(16) :
        #     self.value_list.append(0)
        #     self.name_val_dic[self.english_name_list[i]] = 0

        pass


def CreateVariableObject(type : int) -> Variable :
    if type == 0 :
        return BrakeVariable("brake design variables", 0)
    elif type == 1 :
        return DropVariable("drop design variables", 1)
    elif type == 2 :
        return TurnVariable("turn design variables", 2)
    elif type == 3 :
        return TurnVariable("rectract design variables", 3)
    else :
        return None


#------------------从茉莉平台数模中读取设计变量
def ReadModelDesignVariables(var : Variable) :
    if not var :
        return
    
    #----------遍历设计变量中的名称
    for name in var.english_name_list :
        val_list = Common.getDesignVariable(name)
        if val_list.__len__() != 0 :
            val = val_list[0]
            var.name_val_dic[name] = val
    pass


import Jusme


from FmbsShortcut.import_all_node import MakeSceneNodeByType as SCMakeSceneNodeByType
from Fmbs.import_all_node import MakeSceneNodeByType
from FmbsShortcut.SCcmd.TireCMD import GenCommand

import sys
import os
import TireParameter


def splitStringLast(inputString) :
    strSplit = inputString.split('.')
    length = len(strSplit)
    return strSplit[length - 1]

def getModelName() :
    ascene = Jusme.ActiveUSScene
    model_name = ascene.Name
    return model_name

def getJointList() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    joints_full_name = ".{}.Connectors".format(model_name)
    joints_c = ascene.getObject(joints_full_name)
    joints = joints_c.getObjects()
    #for joint in joints:
        #print(">>>[INFO] Joint Name{}".format(joint.Name))
    return joints

def getPartsMarkers():
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    bodies_full_name = ".{}.Bodies".format(model_name)
    bodies = ascene.getObject(bodies_full_name)
    parts = bodies.getObjects()
    part_shapes = {}
    part_markers = {}

    for part in parts:
        part_markers[part.Name] = {}
        part_shapes[part.Name] = {}
        shapes_markers = part.part_owned_shapes_markers
        print(">>>[INFO] Part Name: {}".format(part.Name))

        for node in shapes_markers:
            if node.Proxy.Type == "Fmbs::Marker":
                part_markers[part.Name][node.Name] = node
                print(">>>[INFO] Marker({0}) type({1}) ".format(node.Name, node.Proxy.Type))
                print(">>>[INFO] Marker({0}) type({1}) ".format(node.Name, node.location))
            else:
                part_shapes[part.Name][node.Name] = node
                print(">>>[INFO] Shape({0}) type({1}) ".format(node.Name, node.Proxy.Type))
                #print(">>>[INFO] Shape({0}) Volumn({1}) ".format(node.Name, node.Shape.Volumn))   这句不能要对于Fmbs::Point可能出问题

    return parts, part_shapes, part_markers

def getDesignVariables() -> list :
    var_list = []
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    strVariableName = ".{0}.{1}".format(model_name, "Aa")
    print("开始获取工程模板的设计变量    {}".format(strVariableName))
    node = ascene.getObject(strVariableName)
    print(node)
    if node is None:
        print("开始获取工程模板的设计变量Aa失败")
        return var_list
    Aa = node.real_value
    var_list.append(Aa)

    strVariableName = ".{0}.{1}".format(model_name, "Ad")
    print("开始获取工程模板的设计变量{}".format(strVariableName))
    node = ascene.getObject(strVariableName)
    if node is None:
        return var_list
    Ad = node.real_value
    var_list.append(Ad)

    strVariableName = ".{0}.{1}".format(model_name, "md")
    print("开始获取工程模板的设计变量{}".format(strVariableName))
    node = ascene.getObject(strVariableName)
    if node is None:
        return var_list
    Md = node.real_value
    var_list.append(Md)

    return var_list

def getDesignVariablesName() -> list :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    name_list = []
    DesignTools = ascene.getObject(".{}.DesignTools".format(model_name))
    for ele in DesignTools :
        name_list.append(ele.Name)

    return name_list
  
def getDesignVariablesNodes() -> list :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    node_list = []
    DesignTools = ascene.getObject(".{}.DesignTools".format(model_name))
    node_list = DesignTools.getObjects()
    
    return node_list
    

def getDesignVariable(var_name : str) -> list :
    var_list = []
    #--------------判断输入的设计变量名称是否为空
    if var_name is None:
        return var_list
    
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    strVariableName = ".{0}.{1}".format(model_name, var_name)
    #print(strVariableName)
    node = ascene.getObject(strVariableName)

    if node is None :
        return var_list
    design_var = node.real_value
    #print("design_var---{}".format(design_var))
    var_list.append(design_var)

    return var_list


def setDesignVariable(var_name : str, var_val : float) -> bool :
    #--------------判断输入的设计变量名称是否为空
    if var_name is None:
        return False
    
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    strVariableName = ".{0}.{1}".format(model_name, var_name)
    node = ascene.getObject(strVariableName)
    if node is None :
        return False
    
    node.real_value = var_val
    return True

#---------------------------------王志国新增
def removeParts() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    bodies_full_name = ".{}.Bodies".format(model_name)
    bodies = ascene.getObject(bodies_full_name)
    parts = bodies.getObjects()

    #-------------遍历Parts集合
    for part in parts :
        if part.Label != "ground" :
            shapes_markers = part.part_owned_shapes_markers
            for ele in shapes_markers :
                ele_name = ele.Name
                ascene.removeObject(ele_name)

            part_name = part.Name
            ascene.removeObject(part_name)

    ground_node = ascene.getObject(".{}.ground".format(model_name))
    if ground_node :
        shapes_markers = ground_node.part_owned_shapes_markers
        for ele in shapes_markers :
            ele_name = ele.Name
            ascene.removeObject(ele_name)
        ground_node.recompute()
    
    bodies.recompute()
    ascene.recompute()   



#-----------------------------------------王志国新增
def removeElements():
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    element_group = ascene.getObject(".{}.Elements".format(model_name))
    element_list = element_group.getObjects()
    
    for ele in element_list :
        ele_name = ele.Name
        ascene.removeObject(ele_name)

    element_group.recompute()
    ascene.recompute()

#---------------------------------王志国新增
def removeDefaults() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    default_group = ascene.getObject(".{}.Defaults".format(model_name))
    default_list = default_group.getObjects()
    for ele in default_list :
        ele_name = ele.Name
        ascene.removeObject(ele_name)

    #default_group.recompute()  
    ascene.recompute()


#---------------------------王志国新增
def removeSimulations() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    sim_group = ascene.getObject(".{}.Simulations".format(model_name))
    sim_list = sim_group.getObjects()
    for ele in sim_list :
        ele_name = ele.Name
        ascene.removeObject(ele_name)
    sim_group.recompute()
    ascene.recompute()

#---------------------------王志国新增
def removeMaterials() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    mat_group = ascene.getObject(".{}.Materials".format(model_name))
    mat_list = mat_group.getObjects()
    for ele in mat_list :
        ele_name = ele.Name
        ascene.removeObject(ele_name)

    mat_group.recompute()
    ascene.recompute()

#---------------------------王志国新增
def removeMeasures() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    mea_group = ascene.getObject(".{}.Measures".format(model_name))
    mea_list = mea_group.getObjects()
    for ele in mea_list :
        ele_name = ele.Name
        ascene.removeObject(ele_name)
    mea_group.recompute()
    ascene.recompute()


#-------------------王志国新增
def removeDesignTools() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()

    DesignTools = ascene.getObject(".{}.DesignTools".format(model_name))
    DesignTools_list = DesignTools.getObjects()
    for ele in DesignTools_list :
        ele_name = ele.Name
        ascene.removeObject(ele_name)

    DesignTools.recompute()
    ascene.recompute()

#-------------------王志国新增
def removeMotions() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    motion_group = ascene.getObject(".{}.Motions".format(model_name))
    motion_list = motion_group.getObjects()
    for ele in motion_list :
        ele_name = ele.Name
        ascene.removeObject(ele_name)

    motion_group.recompute()
    ascene.recompute()

#-------------删除某个指定名称约束
def removeJoint(joint_name : str) :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    joint_full_name = ".{}.{}".format(model_name, joint_name)
    node = ascene.getObject(joint_full_name)
    if node :
        ascene.removeObject(joint_full_name)
    pass

#-----------------王志国新增
def removeJoints() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    joints_full_name = ".{}.Connectors".format(model_name)
    joints_c = ascene.getObject(joints_full_name)
    joints = joints_c.getObjects()
    for ele in joints :
        ele_name = ele.Name
        ascene.removeObject(ele_name)

    joints_c.recompute()
    ascene.recompute()

#-----------------王志国新增
def removeForces() :
    ascene = Jusme.ActiveUSScene
    model_name = getModelName()
    forces_full_name = ".{}.Forces".format(model_name)
    forces_group = ascene.getObject(forces_full_name)
    forces_list = forces_group.getObjects()

    for ele in forces_list :
        ele_name = ele.Name
        ascene.removeObject(ele_name)
    forces_group.recompute()
    ascene.recompute()


#----------------通过轮胎对象创建轮胎
def createTireByObject(tire_obj : TireParameter.TireParameter) :

    import FmbsShortcut.SCcmd.TireCMD as TireCMD
    scene = Jusme.ActiveUSScene
    model_name = getModelName()
    
    default_uints = MakeSceneNodeByType("DefaultsUnits", "defaultsunits")
    default_uints.length = "Millimeter"

    parameter = SCMakeSceneNodeByType("Tire", tire_obj.strTireName)
    print(tire_obj.strTireName)
    parameter.tire_name = tire_obj.strTireName
    parameter.tire_file_path = tire_obj.strTireFilePath
    parameter.road_file_path = tire_obj.strRoadFilePath
    parameter.mass = tire_obj.Mass
    parameter.lxx_lyy = tire_obj.Ixx_Iyy
    parameter.Izz = tire_obj.Izz
    parameter.tire_center_direction_opt = tire_obj.tire_center_direction_opt
    parameter.tire_euler_angles = Jusme.Vector(tire_obj.tire_euler_angles[0], tire_obj.tire_euler_angles[1], tire_obj.tire_euler_angles[2])
    parameter.tire_center_location = tire_obj.tire_center_location
    parameter.road_opt = tire_obj.road_opt
    if tire_obj.road_opt == 0 : #----------表示生成路面
        parameter.road_name = tire_obj.road_name
        parameter.road_direction_opt = tire_obj.road_direction_opt
        parameter.road_euler_angles = Jusme.Vector(tire_obj.road_euler_angles[0], tire_obj.road_euler_angles[1], tire_obj.road_euler_angles[2])
        node = scene.getObject(".{}.{}".format(model_name, tire_obj.road_belong_to))
        if node :
            parameter.road_belong_part = node
    elif tire_obj.road_opt == 1 :  #---------表示引用已有的路面
        node = scene.getObject(".{}.{}".format(model_name, tire_obj.road_part))
        if node :
            parameter.road_part = node

    parameter.longitudinal_velocites = tire_obj.longitudinal_velocites
    parameter.spin_velocites = tire_obj.spin_velocites

    TireCMD.run_test(tire_obj.strTireName)
    pass

#-----------------创建轮胎函数
def createTire(type : int, file_path : str) :

    scene = Jusme.ActiveUSScene
    
    
    #------------定义轮胎参数对象列表
    tire_list = []
    tire_obj : TireParameter.TireParameter = None

    share_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.dirname(share_dir)
    file_dir = template_dir

    model_name = getModelName()
    ascene = Jusme.ActiveUSScene


    if type == 0 :   #-----------表示刹车工况
        file_dir = os.path.join(template_dir, "AssemblyModel", "Tire", "Brake")
    elif type == 1 :  #----------表示落震工况
        file_dir = os.path.join(template_dir, "AssemblyModel", "Tire", "Drop")
    elif type == 2 :  #----------表示转弯工况
        file_dir = os.path.join(template_dir, "AssemblyModel", "Tire", "Turn")
    elif type == 3 : #---------表示收放工况
        file_dir = os.path.join(template_dir, "AssemblyModel", "Tire", "Retract")

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            #-------------出去字符串结尾的换行符
            strHeader = line.split("\n")
            #-------------------表示轮胎参数定义开始
            if strHeader[0] == "tire definition begin" :
                print("------------------")
                tire_obj = TireParameter.TireParameter()
            else :
                row_list = strHeader[0].split("\t")
                #print(row_list)
                #print(row_list[0])
                #print(row_list[1])
                if row_list[0] == "tire_name" :
                    tire_obj.strTireName = row_list[1]
                elif row_list[0] == "tire_file_name" :
                    tire_obj.strTireFilePath = os.path.join(
                        file_dir, row_list[1].strip()
                    )
                elif row_list[0] == "road_file_name" :
                    tire_obj.strRoadFilePath = os.path.join(
                        file_dir, row_list[1].strip()
                    )
                elif row_list[0] == "mass" :
                    tire_obj.Mass = float(row_list[1])
                elif row_list[0] == "Ixx_Iyy" :
                    tire_obj.Ixx_Iyy = float(row_list[1])
                elif row_list[0] == "Izz" :
                    tire_obj.Izz = float(row_list[1])
                elif row_list[0] == "tire_center_direction_opt" :
                    tire_obj.tire_center_direction_opt = int(row_list[1])
                elif row_list[0] == "tire_euler_angles" :
                    eular_list = row_list[1].split(",")
                    tire_obj.tire_euler_angles[0] = float(eular_list[0])
                    tire_obj.tire_euler_angles[1] = float(eular_list[1])
                    tire_obj.tire_euler_angles[2] = float(eular_list[2])
                    print(tire_obj.tire_euler_angles)
                elif row_list[0] == "tire_center_location" :
                    node_name = ".{}.ground.{}".format(model_name, row_list[1])
                    node = ascene.getObject(node_name)
                    if node :
                        tire_obj.tire_center_location = node.location
                        print(tire_obj.tire_center_location)
                elif row_list[0] == "road_name" :
                    tire_obj.road_name = row_list[1]
                elif row_list[0] == "road_direction_opt" :
                    tire_obj.road_direction_opt = int(row_list[1])
                elif row_list[0] == "longitudinal_velocites" :
                    tire_obj.longitudinal_velocites = float(row_list[1])
                elif row_list[0] == "spin_velocites" :
                    tire_obj.spin_velocites = float(row_list[1])
                elif row_list[0] == "road_euler_angles" :
                    eular_list = row_list[1].split(",")
                    tire_obj.road_euler_angles[0] = float(eular_list[0])
                    tire_obj.road_euler_angles[1] = float(eular_list[1])
                    tire_obj.road_euler_angles[2] = float(eular_list[2])
                    print(tire_obj.road_euler_angles)
                elif row_list[0] == "road_opt" :
                    tire_obj.road_opt = int(row_list[1])
                elif row_list[0] == "road_part" :
                    if tire_obj.road_opt == 0 : #----------表示生成路面
                        tire_obj.road_belong_to = row_list[1]
                    elif tire_obj.road_opt == 1 :
                        tire_obj.road_part = row_list[1]
                    tire_list.append(tire_obj)
                
        pass

    print(tire_list)

    #----------------通过轮胎对象创建茉莉平台的轮胎
    for tire_ele in tire_list :
        createTireByObject(tire_ele)

    pass

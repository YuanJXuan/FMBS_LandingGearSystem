class JusmeElement :
    def __init__(self, strName, strFullName):
        self.strName = strName
        self.strFullName = strFullName
        self.type = -1
        pass

class JusmeUnits(JusmeElement) :
    def __init__(self, strName, strFullName):
        super(JusmeUnits, self).__init__(strName, strFullName)
        self.length = "mm"
        self.length_opt = 0
        self.angle = "deg"
        self.force = "newton"
        self.mass = "kg"
        self.time = "sec"
        self.coordinate_system_type = ""
        self.orientation_type = ""
        self.type = 1 
        pass

class JusmeAdmElement(JusmeElement) :
    def __init__(self, strName, strFullName):
        super(JusmeAdmElement, self).__init__(strName, strFullName)
        self.adams_id = 0
        self.type = 2
        self.visibility = True
        self.comments = "" 

class JusmeDataElementVariable(JusmeAdmElement) :
    def __init__(self, strName, strFullName):
        super(JusmeDataElementVariable, self).__init__(strName, strFullName)
        self.function = ""
        pass

class JusmeDataElementSpline(JusmeAdmElement) :
    def __init__(self, strName, strFullName):
        super(JusmeDataElementSpline, self).__init__(strName, strFullName)
        self.x = []
        self.y = []
        self.z = []
        self.linear_extrapolate = ""
        self.x_units = ""
        self.y_units = ""
        pass



class JusmeMaterialElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName):
        super(JusmeMaterialElement, self).__init__(strName, strFullName)
        self.density = 0
        self.youngs_modulus = 0
        self.poissons_ratio = 0
        pass


#------------定义硬点类
class JusmePointElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName) :
        super(JusmePointElement, self).__init__(strName, strFullName)
        self.location = []

#------------定义Marker点类
class JusmeMarkerElement(JusmePointElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeMarkerElement, self).__init__(strName, strFullName)
        #self.location = []
        self.orientation = []
        self.is_floating = False
        self.floating_marker_name = ""
        self.relative_to = ""

#-------------定义几何体lei
class JusmeShapeElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeShapeElement, self).__init__(strName, strFullName)
        pass

class JusmeShapeCylinderElement(JusmeShapeElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeShapeCylinderElement, self).__init__(strName, strFullName)
        self.center_marker = ""
        self.angle_extent = 360
        self.length = 0
        self.radius = 0
        self.side_count_for_body = 0
        self.segment_count_for_ends = 0
        pass

class JusmeShapeOutlineElement(JusmeShapeElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeShapeOutlineElement, self).__init__(strName, strFullName)
        self.marker_list = []
        self.close = "yes"

class JusmeShapeEllipsoidElement(JusmeShapeElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeShapeEllipsoidElement, self).__init__(strName, strFullName)
        self.center_marker = ""
        self.x_scale_factor = 1
        self.y_scale_factor = 1
        self.z_scale_factor = 1

#--------------定义Part部件类
class JusmePartElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName) :
        super(JusmePartElement, self).__init__(strName, strFullName)
        self.marker_list : list = []   #----------定义Part部件下所有的Marker点列表
        self.shape_list : list = []    #----------定义Part下所有的几何体列表
        self.location = []
        self.orientation = []
        self.mass = 0
        self.center_of_mass_marker = ""
        self.inertia_marker = ""
        self.ixx = 0
        self.iyy = 0
        self.izz = 0
        self.ixy = 0
        self.izx = 0
        self.iyz = 0


#--------------定义偏微分方程类
class JusmeDiffElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeDiffElement, self).__init__(strName, strFullName)
        self.initial_condition = 0.0
        self.function = ""
        self.implicit = "off"
        self.static_hold = "off"


#---------定义约束（铰）类
class JusmeJointElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeJointElement, self).__init__(strName, strFullName)
        self.i_marker_name = ""
        self.j_marker_name = ""


#-------------定义仿真脚本类
class JusmeSimulationElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeSimulationElement, self).__init__(strName, strFullName)
        self.commands = ""

#-----------定义Motion类
class JusmeMotionElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeMotionElement, self).__init__(strName, strFullName)
        self.type_of_freedom = ""
        self.joint_name = ""
        self.function = ""

#-------------定义测量基类
class JusmeMeasureBaseElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeMeasureBaseElement, self).__init__(strName, strFullName)
        self.mesure_type = ""

#-----------定义点到点测量类
class JusmePt2PtMeasureElement(JusmeMeasureBaseElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeMeasureBaseElement, self).__init__(strName, strFullName)
        self.mesure_type = "Pt2pt"
        self.from_point = ""
        self.to_point = ""
        self.characteristic = ""
        self.component = ""
        self.create_measure_display = "no"

#--------------定义设计变量类
class JusmeVariableBaseElement(JusmeAdmElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeVariableBaseElement, self).__init__(strName, strFullName)
        self.value_type_opt = 0

#------------定义字符设计变量
class JusmeStringVariableElement(JusmeVariableBaseElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeStringVariableElement, self).__init__(strName, strFullName)
        self.string_value = ""

class JusmeRealVariableElement(JusmeVariableBaseElement) :
    def __init__(self, strName, strFullName) :
        super(JusmeRealVariableElement, self).__init__(strName, strFullName)
        self.range = ""
        self.use_allowed_values = "no"
        self.delta_type = "relative"
        self.real_value = 0.0
        self.units = ""
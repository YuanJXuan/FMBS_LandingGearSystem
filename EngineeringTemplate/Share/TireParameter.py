class TireParameter :
    #-----------------构造函数
    def __init__(self) :
        self.strTireName = ""
        self.strTireFilePath = ""
        self.strRoadFilePath = ""
        self.Mass = 0
        self.Ixx_Iyy = 0
        self.Izz = 0
        self.tire_center_direction_opt = 0
        self.tire_euler_angles = [0, 0, 0]
        self.tire_center_location = [0, 0, 0]
        self.road_name = ""
        self.road_direction_opt = 0
        self.longitudinal_velocites = 0
        self.spin_velocites = 0
        self.road_euler_angles = [0, 0, 0]
        self.road_opt = 0
        self.road_belong_to = ""
        self.road_part = ""
        pass
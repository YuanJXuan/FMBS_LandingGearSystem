from abc import ABC, abstractmethod

#定义自动装配的抽象类
class AbstractAutoGenerater(ABC) :
    def __init__(self, sim_type, part_create_map) -> None:
        self.sim_type = sim_type
        self.part_create_map = part_create_map
        pass

    #------------定义抽象类接口
    @abstractmethod
    def AutoGenerater(self) :
        pass
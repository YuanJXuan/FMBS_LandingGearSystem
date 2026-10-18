
from abc import ABC, abstractmethod


#定义参数化调整的抽象类
class AbstractHpsAdjust(ABC) :
    def __init__(self, hps_full_name) -> None:
        self.hps_full_name = hps_full_name
        pass

    #------------定义抽象类接口
    @abstractmethod
    def Adjust(self) :
        pass


# class AbstractAssemblyHpsAdjust(AbstractHpsAdjust) :
#     def __init__(self, hps_full_name : str, pos : list) -> None:
#         super().__init__(hps_full_name)
#         self.position = pos
#         pass

#     #------------定义抽象类接口
#     def Adjust(self) :
#         pass


# #-------------------------------------------------------定义自动装配参数调整类  
# #-----------------定义刹车参数调整类
# class AbstractAssemblyBrakeHpsAdjust(AbstractHpsAdjust) :
#     def __init__(self, hps_full_name : str) -> None:
#         super().__init__(hps_full_name)
#         pass

#     #------------定义抽象类接口
#     def Adjust(self) :
#         pass

# #-----------------定义落震参数调整类
# class AbstractAssemblyDropHpsAdjust(AbstractHpsAdjust) :
#     def __init__(self, hps_full_name : str) -> None:
#         super().__init__(hps_full_name)
#         pass

#     #------------定义抽象类接口
#     def Adjust(self) :
#         pass

# #-----------------定义转弯参数调整类
# class AbstractAssemblyTurnHpsAdjust(AbstractHpsAdjust) :
#     def __init__(self, hps_full_name : str) -> None:
#         super().__init__(hps_full_name)
#         pass

#     #------------定义抽象类接口
#     def Adjust(self) :
#         pass


# #-----------------定义收放参数调整类
# class AbstractAssemblyRetractHpsAdjust(AbstractHpsAdjust) :
#     def __init__(self, hps_full_name : str) -> None:
#         super().__init__(hps_full_name)
#         pass

#     #------------定义抽象类接口
#     def Adjust(self) :
#         pass
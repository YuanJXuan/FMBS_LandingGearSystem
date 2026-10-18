from abc import ABC, abstractmethod

import DesignVariable

class AbstractAssembly(ABC) :
    def __init__(self, var : DesignVariable.Variable) -> None:
        self.design_var = var
        pass

    #--------------------------------定义抽象类接口
    #---------写设计变量
    @abstractmethod
    def InitDesignVariables(self) :
        pass

    #---------写系统单元
    @abstractmethod
    def InitElement(self) :
        pass

    #---------写补充的Marker点
    @abstractmethod
    def InitMarker(self) :
        pass

    #---------写载荷
    @abstractmethod
    def InitForce(self) :
        pass

    #---------初始化约束
    @abstractmethod
    def InitJoint(self) :
        pass

    #---------初始化驱动
    @abstractmethod
    def InitMotion(self) :
        pass

    #---------初始化测量
    @abstractmethod
    def InitMeasure(self) :
        pass
    pass

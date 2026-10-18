#--------------------自动装配类厂

import DesignVariable

import BrakeAssembly
import DropAssembly
import TurnAssembly
import RetractAssembly

def CreateAssembly(type : int, var : DesignVariable.Variable) :
    if type == 0 :    #----------表示刹车装配
        return BrakeAssembly.BrakeAssembly(var)
    elif type == 1 :   #---------表示落震装配类
        return DropAssembly.DropAssembly(var)
    elif type == 2 :   #---------表示转弯装配类
        return TurnAssembly.TurnAssembly(var)
    elif type == 3 :   #---------表示收放装配类
        return RetractAssembly.RetractAssembly(var)
    else :
        return None
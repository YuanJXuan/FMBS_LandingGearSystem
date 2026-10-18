
import Jusme

import Common

import BrakeHplLtaLcAtch1
import BrakeHplLtaConnectAtch1
import BrakeHplUtaCollarAtch1
import BrakeHplUtaConnectAtch1
import BrakeHplConnect1
import BrakeHplUcTop
import BrakeHplUcBot
import BrakeHplLcTop
import BrakeHplLcBot

import math

err = 0.001

def BrakeAdjustFactory(hps_full_name : str)  :
    hps_name = Common.splitStringLast(hps_full_name)
    if hps_name == "hpl_lta_lc_atch_1" :
        return BrakeHplLtaLcAtch1.BrakeHplLtaLcAtch1Adjust(hps_full_name)
    elif hps_name == "hpl_uta_collar_atch_1" :
        return BrakeHplUtaCollarAtch1.BrakeHplUtaCollarAtch1Adjust(hps_full_name)
    elif hps_name == "hpl_connect_1" :
        return BrakeHplConnect1.BrakeHplConnect1Adjust(hps_full_name)
    elif hps_name == "hpl_uta_connect_atch_1" :
        return BrakeHplUtaConnectAtch1.BrakeHplUtaConnectAtch1Adjust(hps_full_name)
    elif hps_name == "hpl_lta_connect_atch_1" :
        return BrakeHplLtaConnectAtch1.BrakeHplLtaConnectAtch1Adjust(hps_full_name)
    elif hps_name == "hpl_uc_top" :
        return BrakeHplUcTop.BrakeHplUcTopAdjust(hps_full_name)
    elif hps_name == "hpl_uc_bot" :
        return BrakeHplUcBot.BrakeHplUcBotAdjust(hps_full_name)
    elif hps_name == "hpl_lc_top" :
        return BrakeHplLcTop.BrakeHplLcTopAdjust(hps_full_name)
    elif hps_name == "hpl_lc_bot" :
        return BrakeHplLcBot.BrakeHplLcBotAdjust(hps_full_name)
    else :
        return None
    pass

def checkHpsInput(hps_name : str, old_loc : Jusme.Vector, new_loc : Jusme.Vector) :

    #---------如果新点坐标和老点坐标一样
    if old_loc == new_loc :  
        return False

    if hps_name == "hps_lta_uta_atch" :
        #------------判断hps_lta_uta_atch硬点的Y坐标是否发生了改变
        if math.fabs(old_loc.y - new_loc.y) > err :
            return False
    elif hps_name == "hps_lta_lc_atch" :
        #------------判断hps_lta_lc_atch硬点的坐标是否发生了改变
        if math.fabs(old_loc.y - new_loc.y) > err :
            return False
    elif hps_name == "hps_uta_uc_atch" :
        #------------判断hps_uta_uc_atch硬点的坐标是否发生了改变
        if math.fabs(old_loc.y - new_loc.y) > err :
            return False
    elif hps_name == "hps_uc_top" :
        #----------判断hps_uc_top的X和Y坐标是否发生了改变
        if math.fabs(old_loc.x - new_loc.x) > err or math.fabs(old_loc.y - new_loc.y) > err :
            return False
    elif hps_name == "hps_db_sf_atch" :
        #----------判断hps_uc_top的Y坐标是否发生了改变
        if math.fabs(old_loc.y - new_loc.y) > err :
            return False
    elif hps_name == "hps_db_uc_atch" :
        #----------判断hps_db_uc_atch的Y坐标是否发生了改变
        if math.fabs(old_loc.y - new_loc.y) > err :
            return False
    elif hps_name == "hps_lc_top" :
        #----------判断hps_lc_top的X和Y坐标是否发生了改变
        if math.fabs(old_loc.x - new_loc.x) > err or math.fabs(old_loc.y - new_loc.y) > err :
            return False
    elif hps_name == "hps_lc_bot" :
        #----------判断hps_lc_bot的X和Y坐标是否发生了改变
        if math.fabs(old_loc.x - new_loc.x) > err or math.fabs(old_loc.y - new_loc.y) > err :
            return False
    else :
        return False
    
    return True

    pass 

def BrakeHpsAdjust(hps_name : str, x_coord : float, y_coord : float, z_coord : float) :

    #--------------获取Hps硬点整体路径
    strModelName = Common.getModelName()
    strHpsPath = ".{0}.ground.{1}".format(strModelName, hps_name)

    #--------------由刹车类厂创建对象
    Adjustor = BrakeAdjustFactory(strHpsPath)
    if not Adjustor :
        print("该硬点{}不在调整的范围!".format(hps_name))
        return

    #-----------获取硬点节点对象
    ascene = Jusme.ActiveUSScene
    hps = ascene.getObject(strHpsPath)

    #------------判断是否获取到硬点节点
    if not hps :
        return

    #--------------获取修改之前的硬点坐标
    old_loc = hps.location
    #print(old_loc)
    new_loc = Jusme.Vector(x_coord, y_coord, z_coord)
    #print(new_loc)

    #--------------对硬点的坐标进行核查
    bRet = checkHpsInput(hps_name, old_loc, new_loc)
    if not bRet :
        print("硬点{}无需调整".format(hps_name))
        return

    #--------------------对当前硬点的新坐标赋值
    hps.location = new_loc
    #-------------------进行参数化联动
    print("硬点{}开始参数化调整".format(strHpsPath))
    Adjustor.Adjust()
    

def BrakeHpsAdjustAll(hps_name_list : list, hps_x_list : list, hps_y_list : list, hps_z_list : list) :
    nRowIndex = 0
    #print("--------------BrakeHpsAdjustAll")
    for ele in hps_name_list :
        BrakeHpsAdjust(hps_name_list[nRowIndex], hps_x_list[nRowIndex], hps_y_list[nRowIndex], hps_z_list[nRowIndex])
        nRowIndex += 1
    pass

print("BrakeFactory over")
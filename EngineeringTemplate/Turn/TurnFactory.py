import Jusme
import Common

import TurnHpsDbSfAtch
import TurnHpsDbUcAtch
import TurnHpsLtaLcAtch
import TurnHpsLtaUtaAtch
import TurnHpsUtaUcAtch

import TurnHpsHsg1
import TurnHpsHsg2
import TurnHplWheelCenter
import TurnHprWheelCenter

import TurnHpsUcBot
import TurnHpsUcTop
import TurnHpsLcTop
import TurnHpsLcBot

def TurnAdjustFactory(hps_full_name) :
    hps_name = Common.splitStringLast(hps_full_name)
    print(hps_name)
    if hps_name == "hps_db_sf_atch" :
        return TurnHpsDbSfAtch.TurnHpsDbSfAtchAdjust(hps_full_name)
    elif hps_name == "hps_db_uc_atch" :
        return TurnHpsDbUcAtch.TurnHpsDbUcAtchAdjust(hps_full_name)
    elif hps_name == "hps_uta_uc_atch" :
        return TurnHpsUtaUcAtch.TurnHpsUtaUcAtchAdjust(hps_full_name)
    elif hps_name == "hps_lta_uta_atch" :
        return TurnHpsLtaUtaAtch.TurnHpsLtaUtaAtchAdjust(hps_full_name)
    elif hps_name == "hps_lta_lc_atch" :
        return TurnHpsLtaLcAtch.TurnHpsLtaLcAtchAdjust(hps_full_name)
    elif hps_name == "hsg_1":
        return TurnHpsHsg1.TurnHpsHsg1Adjust(hps_full_name)
    elif hps_name == "hsg_2":
        return TurnHpsHsg2.TurnHpsHsg2Adjust(hps_full_name)
    elif hps_name == "hpl_wheel_center":
        return TurnHplWheelCenter.TurnHplWheelCenterAdjust(hps_full_name)
    elif hps_name== "hpr_wheel_center":
        return TurnHprWheelCenter.TurnHprWheelCenterAdjust(hps_full_name)
    elif hps_name== "hps_uc_bot":
        return TurnHpsUcBot.TurnHpsUcBotAdjust(hps_full_name)
    elif hps_name== "hps_uc_top":
        return TurnHpsUcTop.TurnHpsUcTopAdjust(hps_full_name)
    elif hps_name== "hps_lc_bot":
        return TurnHpsLcBot.TurnHpsLcBotAdjust(hps_full_name)
    elif hps_name== "hps_lc_top":
        return TurnHpsLcTop.TurnHpsLcTopAdjust(hps_full_name)
    pass
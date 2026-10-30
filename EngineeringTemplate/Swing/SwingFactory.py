import Jusme
import Common

import SwingHpsDbSfAtch
import SwingHpsDbUcAtch
import SwingHpsLtaLcAtch
import SwingHpsLtaUtaAtch
import SwingHpsUtaUcAtch

import SwingHplWheelCenter
import SwingHprWheelCenter

import SwingHpsUcBot
import SwingHpsUcTop
import SwingHpsLcBot
import SwingHpsLcTop


def SwingAdjustFactory(hps_full_name) :
    hps_name = Common.splitStringLast(hps_full_name)
    print(hps_name)
    if hps_name == "hps_db_sf_atch" :
        return SwingHpsDbSfAtch.SwingHpsDbSfAtchAdjust(hps_full_name)
    elif hps_name == "hps_db_uc_atch" :
        return SwingHpsDbUcAtch.SwingHpsDbUcAtchAdjust(hps_full_name)
    elif hps_name == "hps_uta_uc_atch" :
        return SwingHpsUtaUcAtch.SwingHpsUtaUcAtchAdjust(hps_full_name)
    elif hps_name == "hps_lta_uta_atch" :
        return SwingHpsLtaUtaAtch.SwingHpsLtaUtaAtchAdjust(hps_full_name)
    elif hps_name == "hps_lta_lc_atch" :
        return SwingHpsLtaLcAtch.SwingHpsLtaLcAtchAdjust(hps_full_name)
    elif hps_name == "hpl_wheel_center":
        return SwingHplWheelCenter.SwingHplWheelCenterAdjust(hps_full_name)
    elif hps_name== "hpr_wheel_center":
        return SwingHprWheelCenter.SwingHprWheelCenterAdjust(hps_full_name)
    elif hps_name== "hps_lc_top":
        return SwingHpsLcTop.SwingHpsLcTopAdjust(hps_full_name)
    elif hps_name== "hps_lc_bot":
        return SwingHpsLcBot.SwingHpsLcBotAdjust(hps_full_name)
    elif hps_name== "hps_uc_bot":
        return SwingHpsUcBot.SwingHpsUcBotAdjust(hps_full_name)
    elif hps_name== "hps_uc_top":
        return SwingHpsUcTop.SwingHpsUcTopAdjust(hps_full_name)
    pass
print("SwingFactory over")
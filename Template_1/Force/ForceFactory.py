import Jusme


import Common

import math


import ForceHpsDbSfAtch
import ForceHpsDbUcAtch
import ForceHpsRodBot
import ForceHpsRodTop

import ForceHplActuatorTop
import ForceHprActuatorTop
import ForceHplRodBot
import ForceHprRodBot


def ForceAdjustFactory(hps_full_name)  :
    hps_name = Common.splitStringLast(hps_full_name)
    print(hps_name)
    if hps_name == "hps_db_sf_atch" :
        return ForceHpsDbSfAtch.ForceHpsDbSfAtchAdjust(hps_full_name)
    elif hps_name == "hps_db_uc_atch" :
        return ForceHpsDbUcAtch.ForceHpsDbUcAtchAdjust(hps_full_name)
    elif hps_name == "hps_rod_top" :
        return ForceHpsRodTop.ForceHpsRodTopAdjust(hps_full_name)
    elif hps_name == "hps_rod_bot" :
        return ForceHpsRodBot.ForceHpsRodBotAdjust(hps_full_name)
    elif hps_name == "hpl_actuator_top" :
        return ForceHplActuatorTop.ForceHplActuatorTopAdjust(hps_full_name)
    elif hps_name == "hpr_actuator_top" :
        return ForceHprActuatorTop.ForceHprActuatorTopAdjust(hps_full_name)
    elif hps_name == "hpl_rod_bot" :
        return ForceHplRodBot.ForceHplRodBotAdjust(hps_full_name)
    elif hps_name == "hpr_rod_bot" :
        return ForceHprRodBot.ForceHprRodBotAdjust(hps_full_name)
    else :
        return None
    pass
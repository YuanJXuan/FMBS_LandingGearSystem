import Jusme


import Common

import math


import CosimHpsDbSfAtch
import CosimHpsDbUcAtch

import CosimHpsRodBot
import CosimHpsRodTop


def CosimAdjustFactory(hps_full_name)  :
    hps_name = Common.splitStringLast(hps_full_name)
    print(hps_name)
    if hps_name == "hps_db_sf_atch" :
        return CosimHpsDbSfAtch.CosimHpsDbSfAtchAdjust(hps_full_name)
    elif hps_name == "hps_db_uc_atch" :
        return CosimHpsDbUcAtch.CosimHpsDbUcAtchAdjust(hps_full_name)
    elif hps_name == "hps_rod_top" :
        return CosimHpsRodTop.CosimHpsRodTopAdjust(hps_full_name)
    elif hps_name == "hps_rod_bot" :
        return CosimHpsRodBot.CosimHpsRodBotAdjust(hps_full_name)
    else :
        return None
    pass
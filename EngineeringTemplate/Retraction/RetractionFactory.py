import Jusme


import Common

import math


import RetractionHpsDbSfAtch
import RetractionHpsDbUcAtch

import RetractionHpsRodBot
import RetractionHpsRodTop


def RetractionAdjustFactory(hps_full_name)  :
    hps_name = Common.splitStringLast(hps_full_name)
    print(hps_name)
    if hps_name == "hps_db_sf_atch" :
        return RetractionHpsDbSfAtch.RetractionHpsDbSfAtchAdjust(hps_full_name)
    elif hps_name == "hps_db_uc_atch" :
        return RetractionHpsDbUcAtch.RetractionHpsDbUcAtchAdjust(hps_full_name)
    elif hps_name == "hps_rod_top" :
        return RetractionHpsRodTop.RetractionHpsRodTopAdjust(hps_full_name)
    elif hps_name == "hps_rod_bot" :
        return RetractionHpsRodBot.RetractionHpsRodBotAdjust(hps_full_name)
    else :
        return None
    pass
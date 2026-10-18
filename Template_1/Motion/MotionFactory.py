import Jusme


import Common

import math


import MotionHpsDbSfAtch
import MotionHpsDbUcAtch

import MotionHplUpractSfAtch1
import MotionHplLwractUcAtch1
import MotionHprUpractSfAtch1
import MotionHprLwractUcAtch1

import MotionHpsRodBot
import MotionHpsRodTop


def MotionAdjustFactory(hps_full_name)  :
    hps_name = Common.splitStringLast(hps_full_name)
    print(hps_name)
    if hps_name == "hps_db_sf_atch" :
        return MotionHpsDbSfAtch.MotionHpsDbSfAtchAdjust(hps_full_name)
    elif hps_name == "hps_db_uc_atch" :
        return MotionHpsDbUcAtch.MotionHpsDbUcAtchAdjust(hps_full_name)
    elif hps_name == "hpl_upract_sf_atch_1" :
        return MotionHplUpractSfAtch1.MotionHplUpractSfAtch1Adjust(hps_full_name)
    elif hps_name == "hpl_lwract_uc_atch_1" :
        return MotionHplLwractUcAtch1.MotionHplLwractUcAtch1Adjust(hps_full_name)
    elif hps_name == "hpr_lwract_uc_atch_1" :
        return MotionHprLwractUcAtch1.MotionHprLwractUcAtch1Adjust(hps_full_name)
    elif hps_name == "hpr_upract_sf_atch_1" :
        return MotionHprUpractSfAtch1.MotionHprUpractSfAtch1Adjust(hps_full_name)
    elif hps_name == "hps_rod_top" :
        return MotionHpsRodTop.MotionHpsRodTopAdjust(hps_full_name)
    elif hps_name == "hps_rod_bot" :
        return MotionHpsRodBot.MotionHpsRodBotAdjust(hps_full_name)
    else :
        return None
    pass
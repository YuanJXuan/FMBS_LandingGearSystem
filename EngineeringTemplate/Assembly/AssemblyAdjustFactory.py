
import AssemblyHpsLtaLcAtchAdjust
import AssemblyHpsLtaUtaAtchAdjust
import AssemblyHpsUcTopAdjust

def CreateAssemblyHpsAdjust(hps_name : str) -> None:
    
    if hps_name == "hps_lta_lc_atch" :
        return AssemblyHpsLtaLcAtchAdjust.AssemblyHpsLtaLcAtchAdjust(hps_name)
    elif hps_name == "hps_lta_uta_atch" :
        return AssemblyHpsLtaUtaAtchAdjust.AssemblyHpsLtaUtaAtchAdjust(hps_name)
    elif hps_name == "hps_uc_top" :
        return AssemblyHpsUcTopAdjust.AssemblyHpsUcTopAdjust(hps_name)
    else :
        return None      
    pass


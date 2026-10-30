
import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common


class AssemblyHpsLtaLcAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name : str) -> None:
        super().__init__(hps_full_name)
        pass

    #------------定义抽象类接口
    def Adjust(self) :
        print("进入落震硬点HpsLtaLcAtch参数化调整程序")
        pass
    pass
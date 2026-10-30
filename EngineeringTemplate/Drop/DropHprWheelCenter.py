import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class DropHprWheelCenterAdjust(AbstractHps.AbstractHpsAdjust)  :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("start adjusting HprWheelCenter")
        ascene = Jusme.ActiveUSScene

        #--------------------------------------------._AA_nlg_post_2hubs.ground.hpr_wheel_center
        hpr_wheel_center = ascene.getObject(self.hps_full_name)
        if not hpr_wheel_center :
            return
        
        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject("._AA_nlg_post_2hubs.ground.origo")
        if not origo :
            return
        
        #------------------------------._AA_nlg_post_2hubs.ground.hpl_wheel_center
        hpl_wheel_center = ascene.getObject("._AA_nlg_post_2hubs.ground.hpl_wheel_center")
        if not hpl_wheel_center :
            return
        
        pass
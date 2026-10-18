import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class TurnHpsHsg2Adjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始转弯仿真hsg_2硬点调整")

        ascene = Jusme.ActiveUSScene
        #---------------获取当前模型名称
        model_name = Common.getModelName()

        #----------------获取全局坐标系原点origo的mark点
        origo=ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            return

        #---------获取修改后的hsg_1 hsg_2(hps)--------
        hsg_2 = ascene.getObject(self.hps_full_name)
        if not hsg_2 :
            return
        
        hsg_1 = ascene.getObject(".{}.ground.hsg_1".format(model_name))
        if not hsg_1 :
            return

        hsg_1_loc=hsg_1.location
        hsg_2_loc=hsg_2.location

        #--------修改zdt1 zdt2(marker)----------
        zdt1=ascene.getObject(".{}.ground.zdt1".format(model_name))
        if not zdt1 :
            return
        zdt2=ascene.getObject(".{}.ground.zdt2".format(model_name))
        if not zdt2 :
            return

        zdt1.location=VecUtils.LOC_ALONG_LINE(hsg_1_loc,hsg_2_loc,0.6*VecUtils.DM(hsg_1_loc,hsg_2_loc))
        zdt1.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1_loc,hsg_2_loc,'z')

        zdt2.location=VecUtils.LOC_ALONG_LINE(hsg_1_loc,hsg_2_loc,0.9*VecUtils.DM(hsg_1_loc,hsg_2_loc))
        zdt2.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1_loc,hsg_2_loc,'z')


        #------获取ges_collar(part)
        ges_collar=ascene.getObject(".{}.ges_collar".format(model_name))
        if not ges_collar :
            return
        
        #-----修改ges_collar.MARKER_75-----
        MARKER_75=ascene.getObject(".{}.ges_collar.MARKER_75".format(model_name))
        if not MARKER_75 :
            return
        MARKER_75.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hsg_1)
        MARKER_75.orientation=Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, MARKER_75.location, MARKER_75.orientation)
        MARKER_75.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_75.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------修改hsg(part)-----
        hsg=ascene.getObject(".{}.hsg".format(model_name))
        if not hsg :
            return
        hsg.location=0.5*(hsg_1_loc+hsg_2_loc)
        hsg.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1_loc,hsg_2_loc,'z')
        
        
        #-------修改hsg.CYLINDER_50(geom)-----
        CYLINDER_50=ascene.getObject(".{}.hsg.CYLINDER_50".format(model_name))
        if not CYLINDER_50 :
            return
        CYLINDER_50.length=VecUtils.DM(hsg_1_loc,hsg_2_loc)

        #-------修改hsg.gralin_73(marker)-----
        gralin_73=ascene.getObject(".{}.hsg.gralin_73".format(model_name))
        if not gralin_73 :
            return
        gralin_73.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hsg_1)
        gralin_73.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1_loc,hsg_2_loc,'z')
        loc_ori = VecUtils.global2local(hsg.location, hsg.orientation, gralin_73.location, gralin_73.orientation)
        gralin_73.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_73.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------修改hsg.cm(marker)-----
        hsg_cm=ascene.getObject(".{}.hsg.cm".format(model_name))
        if not hsg_cm :
            return
        hsg_cm.location=0.5*(hsg_1_loc+hsg_2_loc)
        hsg_cm.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1_loc,hsg_2_loc,'z')
        loc_ori = VecUtils.global2local(hsg.location, hsg.orientation, hsg_cm.location, hsg_cm.orientation)
        hsg_cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        hsg_cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------修改zdt(part)-----
        zdt=ascene.getObject(".{}.zdt".format(model_name))
        if not zdt :
            return
        zdt.location=0.5*(zdt1.location+zdt2.location)
        zdt.orientation=VecUtils.ORI_ALONG_AXIS(zdt1.location,zdt2.location,'z')
        
        
        #-------修改zdt.CYLINDER_51(geom)-----
        CYLINDER_51=ascene.getObject(".{}.zdt.CYLINDER_51".format(model_name))
        if not CYLINDER_51 :
            return
        CYLINDER_51.length=VecUtils.DM(zdt1.location,zdt2.location)

        #-------修改zdt.gralin_74(marker)-----
        gralin_74=ascene.getObject(".{}.zdt.gralin_74".format(model_name))
        if not gralin_74 :
            return
        gralin_74.location=VecUtils.LOC_RELATIVE_TO([0,0,0],zdt1)
        gralin_74.orientation=VecUtils.ORI_ALONG_AXIS(zdt1.location,zdt2.location,'z')
        loc_ori = VecUtils.global2local(zdt.location, zdt.orientation, gralin_74.location, gralin_74.orientation)
        gralin_74.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        gralin_74.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------zdt.cm(marker)-----
        zdt_cm=ascene.getObject(".{}.zdt.cm".format(model_name))
        if not zdt_cm :
            return
        zdt_cm.location=0.5*(zdt1.location+zdt2.location)
        zdt_cm.orientation=VecUtils.ORI_ALONG_AXIS(zdt1.location,zdt2.location,'z')
        loc_ori = VecUtils.global2local(zdt.location, zdt.orientation, zdt_cm.location, zdt_cm.orientation)
        zdt_cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        zdt_cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])     

        #------修改hsg.MARKER_76
        MARKER_76=ascene.getObject(".{}.hsg.MARKER_76".format(model_name))
        if not MARKER_76 :
            return
        MARKER_76.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hsg_1)
        MARKER_76.orientation=Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(hsg.location, hsg.orientation, MARKER_76.location, MARKER_76.orientation)
        MARKER_76.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_76.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改hsg.MARKER_81
        MARKER_81=ascene.getObject(".{}.hsg.MARKER_81".format(model_name))
        if not MARKER_81 :
            return
        MARKER_81.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hsg_cm)
        MARKER_81.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1_loc,zdt1.location,'z')
        loc_ori = VecUtils.global2local(hsg.location, hsg.orientation, MARKER_81.location, MARKER_81.orientation)
        MARKER_81.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_81.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改hsg.MARKER_82
        MARKER_82=ascene.getObject(".{}.hsg.MARKER_82".format(model_name))
        if not MARKER_82 :
            return
        MARKER_82.location=VecUtils.LOC_RELATIVE_TO([0,0,0],hsg_cm)
        MARKER_82.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1_loc,zdt1.location,'z')
        loc_ori = VecUtils.global2local(hsg.location, hsg.orientation, MARKER_82.location, MARKER_82.orientation)
        MARKER_82.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_82.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改hsg.MARKER_85
        MARKER_85=ascene.getObject(".{}.hsg.MARKER_85".format(model_name))
        if not MARKER_85 :
            return
        MARKER_85.location=VecUtils.LOC_RELATIVE_TO([0,0,0],zdt_cm)
        MARKER_85.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1_loc,zdt1.location,'z')
        loc_ori = VecUtils.global2local(hsg.location, hsg.orientation, MARKER_85.location, MARKER_85.orientation)
        MARKER_85.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_85.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改zdt.MARKER_86
        MARKER_86=ascene.getObject(".{}.zdt.MARKER_86".format(model_name))
        if not MARKER_86 :
            return
        MARKER_86.location=VecUtils.LOC_RELATIVE_TO([0,0,0],zdt_cm)
        MARKER_86.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1_loc,zdt1.location,'z')
        loc_ori = VecUtils.global2local(zdt.location, zdt.orientation, MARKER_86.location, MARKER_86.orientation)
        MARKER_86.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_86.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------修改zdt.MARKER_78
        MARKER_78=ascene.getObject(".{}.zdt.MARKER_78".format(model_name))
        if not MARKER_78 :
            return
        MARKER_78.location=VecUtils.LOC_RELATIVE_TO([0,0,0],zdt1)
        MARKER_78.orientation=Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(zdt.location, zdt.orientation, MARKER_78.location, MARKER_78.orientation)
        MARKER_78.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_78.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------获取ges_upper_cylinder
        ges_upper_cylinder=ascene.getObject(".{}.ges_upper_cylinder".format(model_name))
        if not ges_upper_cylinder :
            return
            
        #------修改ges_upper_cylinder.MARKER_77
        MARKER_77=ascene.getObject(".{}.ges_upper_cylinder.MARKER_77".format(model_name))
        if not MARKER_77 :
            return
        MARKER_77.location=VecUtils.LOC_RELATIVE_TO([0,0,0],zdt1)
        MARKER_77.orientation=Jusme.Vector(0, 0, 0)
        loc_ori = VecUtils.global2local(ges_upper_cylinder.location, ges_upper_cylinder.orientation, MARKER_77.location, MARKER_77.orientation)
        MARKER_77.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_77.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-------修改hsg(part)-----
        hsg=ascene.getObject(".{}.hsg".format(model_name))
        if not hsg :
            print("没找到hsg")
            return
        hsg.location=0.5*(hsg_1.location+hsg_2.location)
        hsg.orientation=VecUtils.ORI_ALONG_AXIS(hsg_1.location,hsg_2.location,'z')

        #-------修改zdt(part)-----
        zdt=ascene.getObject(".{}.zdt".format(model_name))
        if not zdt :
            print("没找到zdt")
            return
        zdt.location=0.5*(zdt1.location+zdt2.location)
        zdt.orientation=VecUtils.ORI_ALONG_AXIS(zdt1.location,zdt2.location,'z')

        #---------.hsg_zdt(joint)
        hsg_zdt = ascene.getObject(".{}.hsg_zdt".format(model_name))
        if not hsg_zdt :
            return
        hsg_zdt.recompute()

        #---------.zdt_upcylinder(joint)
        zdt_upcylinder = ascene.getObject(".{}.zdt_upcylinder".format(model_name))
        if not zdt_upcylinder :
            return
        zdt_upcylinder.recompute()

        #---------.hsg_collar(joint)
        hsg_collar = ascene.getObject(".{}.hsg_collar".format(model_name))
        if not hsg_collar :
            return
        hsg_collar.recompute()

        #---------.josrev_collar_uc_joint(joint)
        josrev_collar_uc_joint = ascene.getObject(".{}.josrev_collar_uc_joint".format(model_name))
        if not josrev_collar_uc_joint :
            return
        josrev_collar_uc_joint.recompute()

        #---------.josrev_uta_uc_joint(joint)
        josrev_uta_uc_joint = ascene.getObject(".{}.josrev_uta_uc_joint".format(model_name))
        if not josrev_uta_uc_joint :
            return
        josrev_uta_uc_joint.recompute()

        #---------.ZWL(joint)
        ZWL = ascene.getObject(".{}.ZWL".format(model_name))
        if not ZWL :
            return
        ZWL.recompute()




        print("结束调整hsg_2")




        pass
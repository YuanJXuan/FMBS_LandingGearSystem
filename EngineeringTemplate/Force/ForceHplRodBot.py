import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 
import AbstractHps
import Common

class ForceHplRodBotAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
        print("开始hpl_rod_bot硬点调整")

        ascene = Jusme.ActiveUSScene
        #--------------得到模型名称
        model_name = Common.getModelName()

        #---------------获取全局坐标系原点的mark点
        origo = ascene.getObject(".{}.ground.origo".format(model_name))
        if not origo :
            return

        #--------.ground.hpl_rod_bot
        hpl_rod_bot = ascene.getObject(self.hps_full_name)
        if not hpl_rod_bot :
            return
        
        #--------.ground.hpl_actuator_top
        hpl_actuator_top = ascene.getObject(".{}.ground.hpl_actuator_top".format(model_name))
        if not hpl_actuator_top :
            print("1")
            return
        
        #---------------.ground.hpl_actuator_bot
        hpl_actuator_bot = ascene.getObject(".{}.ground.hpl_actuator_bot".format(model_name))
        if not hpl_actuator_bot :
            print("2")
            return

        #---------------.ground.hpr_actuator_top
        hpr_actuator_top = ascene.getObject(".{}.ground.hpr_actuator_top".format(model_name))
        if not hpr_actuator_top :
            print("3")
            return

        #---------------.ground.hpr_actuator_bot
        hpr_actuator_bot = ascene.getObject(".{}.ground.hpr_actuator_bot".format(model_name))
        if not hpr_actuator_bot :
            print("4")
            return

        #---------------.ground.hpl_rod_bot
        hpl_rod_bot = ascene.getObject(".{}.ground.hpl_rod_bot".format(model_name))
        if not hpl_rod_bot :
            print("5")
            return

        #---------------.ground.hpr_rod_bot
        hpr_rod_bot = ascene.getObject(".{}.ground.hpr_rod_bot".format(model_name))
        if not hpr_rod_bot :
            print("6")
            return
        
        #---------------.ground.hpr_rod_topr
        hpr_rod_topr = ascene.getObject(".{}.ground.hpr_rod_topr".format(model_name))
        if not hpr_rod_topr :
            print("6")
            return

        hpr_rod_bot.location.y=(-1)*hpl_rod_bot.location.y
        hpr_rod_bot.location.x=hpl_rod_bot.location.x
        hpr_rod_bot.location.z=hpl_rod_bot.location.z

        
        
        #===============================修改左侧主起结构=================================

  

        #-------------修改ground.MARKER_top_L
        MARKER_top_L = ascene.getObject(".{}.ground.MARKER_top_L".format(model_name))
        if not MARKER_top_L :
            print("7")
            return
        MARKER_top_L.location=VecUtils.LOC_ALONG_LINE(hpl_actuator_bot.location,hpl_actuator_top.location,(10/13)*VecUtils.DM(hpl_actuator_bot.location,hpl_actuator_top.location))
        



        #---------修改MARKER_top_L相关的内容---------------------------

     

        #-----------修改ground.MARKER_bot_L
        MARKER_bot_L = ascene.getObject(".{}.ground.MARKER_bot_L".format(model_name))
        if not MARKER_bot_L :
            print("8")
            return
        MARKER_bot_L.location=VecUtils.LOC_ALONG_LINE(hpl_rod_bot.location,MARKER_top_L.location,(1/6)*VecUtils.DM(hpl_rod_bot.location,MARKER_top_L.location))
        





        #-----------修改mlg_rod_L----------
        mlg_rod_L = ascene.getObject(".{}.mlg_rod_L".format(model_name))
        if not mlg_rod_L :
            print("9")
            return
        mlg_rod_L.location=0.5*(hpl_rod_bot.location+MARKER_top_L.location)
        mlg_rod_L.orientation=Jusme.Vector(180,90,90)

        #--------修改mlg_rod_L.MARKER_559
        MARKER_559 = ascene.getObject(".{}.mlg_rod_L.MARKER_559".format(model_name))
        if not MARKER_559 :
            print("10")
            return
        MARKER_559.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_rod_bot))
        MARKER_559.orientation = Jusme.Vector(180,90,90)
        loc_ori = VecUtils.global2local(mlg_rod_L.location, mlg_rod_L.orientation, MARKER_559.location, MARKER_559.orientation)
        MARKER_559.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_559.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------修改mlg_rod_L.CYLINDER_315----------
        CYLINDER_315 = ascene.getObject(".{}.mlg_rod_L.CYLINDER_315".format(model_name))
        if not CYLINDER_315 :
            print("11")
            return
        CYLINDER_315.length=VecUtils.DM(hpl_rod_bot.location,MARKER_top_L.location)

        #------修改mlg_rod_L.cm
        cm = ascene.getObject(".{}.mlg_rod_L.cm".format(model_name))
        if not cm :
            print("12")
            return
        # cm.recompute()
        cm.location = 0.5*(hpl_rod_bot.location+MARKER_top_L.location)
        cm.orientation = Jusme.Vector(0.0, 90.0, 0.0)
        # loc_ori = VecUtils.global2local(mlg_rod_L.location, mlg_rod_L.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #---------------修改mlg_actuatorL--------------------
        mlg_actuatorL = ascene.getObject(".{}.mlg_actuatorL".format(model_name))
        if not mlg_actuatorL :
            print("13")
            return
        mlg_actuatorL.location=0.5*(MARKER_bot_L.location+hpl_actuator_top.location)
        mlg_actuatorL.orientation=Jusme.Vector(180,90,90)
        
        #--------修改mlg_actuatorL.MARKER_560
        MARKER_560 = ascene.getObject(".{}.mlg_actuatorL.MARKER_560".format(model_name))
        if not MARKER_560 :
            print("14")
            return
        MARKER_560.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_bot_L))
        MARKER_560.orientation = Jusme.Vector(180,90,90)
        loc_ori = VecUtils.global2local(mlg_actuatorL.location, mlg_actuatorL.orientation, MARKER_560.location, MARKER_560.orientation)
        MARKER_560.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_560.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        
        #---------mlg_actuatorL.CYLINDER_320----------
        CYLINDER_320 = ascene.getObject(".{}.mlg_actuatorL.CYLINDER_320".format(model_name))
        if not CYLINDER_320 :
            print("15")
            return
        CYLINDER_320.length=VecUtils.DM(MARKER_bot_L.location,hpl_actuator_top.location)
        
        #------修改mlg_actuatorL.cm
        cm = ascene.getObject(".{}.mlg_actuatorL.cm".format(model_name))
        if not cm :
            print("16")
            return
        # cm.recompute()
        cm.location = 0.5*(MARKER_bot_L.location+hpl_actuator_top.location)
        cm.orientation = Jusme.Vector(180.0, 90.0, 90.0)
        # loc_ori = VecUtils.global2local(mlg_actuatorL.location, mlg_actuatorL.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        
        
        
        
        
        
        #-----------------mlg_rod_L和mlg_actuatorL中的marker点--------------------------------
        
        #-----------------mlg_rod_L和mlg_actuatorL中的marker点--------------------------------
        
        #--------修改mlg_rod_L.MARKER_682
        MARKER_682 = ascene.getObject(".{}.mlg_rod_L.MARKER_682".format(model_name))
        if not MARKER_682 :
            print("17")
            return
        MARKER_682.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_rod_bot))
        MARKER_682.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(mlg_rod_L.location, mlg_rod_L.orientation, MARKER_682.location, MARKER_682.orientation)
        MARKER_682.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_682.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_actuatorL.MARKER_683
        MARKER_683 = ascene.getObject(".{}.mlg_actuatorL.MARKER_683".format(model_name))
        if not MARKER_683 :
            print("18")
            return
        MARKER_683.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_bot_L))
        MARKER_683.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(mlg_actuatorL.location, mlg_actuatorL.orientation, MARKER_683.location, MARKER_683.orientation)
        MARKER_683.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_683.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_rod_L.MARKER_603
        MARKER_603 = ascene.getObject(".{}.mlg_rod_L.MARKER_603".format(model_name))
        if not MARKER_603 :
            print("17")
            return
        MARKER_603.location = Jusme.Vector(1.0487340597E+04, -1489.0607744005, 1752.4060817997)
        MARKER_603.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(mlg_rod_L.location, mlg_rod_L.orientation, MARKER_603.location, MARKER_603.orientation)
        MARKER_603.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_603.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_actuatorL.MARKER_602
        MARKER_602 = ascene.getObject(".{}.mlg_actuatorL.MARKER_602".format(model_name))
        if not MARKER_602 :
            print("18")
            return
        MARKER_602.location = Jusme.Vector(1.0487340597E+04, -1389.0607744005, 1752.4060818003)
        MARKER_602.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(mlg_actuatorL.location, mlg_actuatorL.orientation, MARKER_602.location, MARKER_602.orientation)
        MARKER_602.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_602.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_rod_L.MARKER_593
        MARKER_593 = ascene.getObject(".{}.mlg_rod_L.MARKER_593".format(model_name))
        if not MARKER_593 :
            print("19")
            return
        MARKER_593.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpl_rod_bot))
        MARKER_593.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(mlg_rod_L.location, mlg_rod_L.orientation, MARKER_593.location, MARKER_593.orientation)
        MARKER_593.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_593.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_actuatorL.MARKER_592
        MARKER_592 = ascene.getObject(".{}.mlg_actuatorL.MARKER_592".format(model_name))
        if not MARKER_592 :
            print("20")
            return
        MARKER_592.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_bot_L))
        MARKER_592.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(mlg_actuatorL.location, mlg_actuatorL.orientation, MARKER_592.location, MARKER_592.orientation)
        MARKER_592.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_592.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_rod_L.MARKER_564
        MARKER_564 = ascene.getObject(".{}.mlg_rod_L.MARKER_564".format(model_name))
        if not MARKER_564 :
            print("21")
            return
        MARKER_564.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_bot_L))
        MARKER_564.orientation = VecUtils.ORI_ALONG_AXIS(hpl_actuator_top.location,hpl_rod_bot.location,'z')
        loc_ori = VecUtils.global2local(mlg_rod_L.location, mlg_rod_L.orientation, MARKER_564.location, MARKER_564.orientation)
        MARKER_564.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_564.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_actuatorL.MARKER_563
        MARKER_563 = ascene.getObject(".{}.mlg_actuatorL.MARKER_563".format(model_name))
        if not MARKER_563 :
            print("22")
            return
        MARKER_563.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_bot_L))
        MARKER_563.orientation = VecUtils.ORI_ALONG_AXIS(hpl_actuator_top.location,hpl_rod_bot.location,'z')
        loc_ori = VecUtils.global2local(mlg_actuatorL.location, mlg_actuatorL.orientation, MARKER_563.location, MARKER_563.orientation)
        MARKER_563.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_563.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_rod_L.MARKER_677
        MARKER_677 = ascene.getObject(".{}.mlg_rod_L.MARKER_677".format(model_name))
        if not MARKER_677 :
            print("21")
            return
        MARKER_677.location =Jusme.Vector(1.0487340597E+04, -1489.0607744005, 1752.4060817997)
        MARKER_677.orientation = Jusme.Vector(293.4993529872, 73.6039865276, 2.2594229001)
        loc_ori = VecUtils.global2local(mlg_rod_L.location, mlg_rod_L.orientation, MARKER_677.location, MARKER_677.orientation)
        MARKER_677.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_677.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_actuatorL.MARKER_676
        MARKER_676 = ascene.getObject(".{}.mlg_actuatorL.MARKER_676".format(model_name))
        if not MARKER_676 :
            print("22")
            return
        MARKER_676.location = Jusme.Vector(1.0487340597E+04, -1389.0607744005, 1752.4060818003)
        MARKER_676.orientation = Jusme.Vector(293.4993529872, 73.6039865276, 2.2594229001)
        loc_ori = VecUtils.global2local(mlg_actuatorL.location, mlg_actuatorL.orientation, MARKER_676.location, MARKER_676.orientation)
        MARKER_676.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_676.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


        #--------修改mlg_actuatorL.MARKER_578
        MARKER_578 = ascene.getObject(".{}.mlg_actuatorL.MARKER_578".format(model_name))
        if not MARKER_578 :
            print("23")
            return
        MARKER_578.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0],hpl_actuator_top))
        MARKER_578.orientation = Jusme.Vector(270,90,90)
        loc_ori = VecUtils.global2local(mlg_actuatorL.location, mlg_actuatorL.orientation, MARKER_578.location, MARKER_578.orientation)
        MARKER_578.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_578.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改ground.MARKER_579
        MARKER_579 = ascene.getObject(".{}.ground.MARKER_579".format(model_name))
        if not MARKER_579 :
            print("24")
            return
        MARKER_579.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0],hpl_actuator_top))
        MARKER_579.orientation = Jusme.Vector(270,90,90)
        loc_ori = VecUtils.global2local(mlg_actuatorL.location, mlg_actuatorL.orientation, MARKER_579.location, MARKER_579.orientation)
        MARKER_579.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_579.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #--------修改mlg_rod_L.MARKER_565
        MARKER_565 = ascene.getObject(".{}.mlg_rod_L.MARKER_565".format(model_name))
        if not MARKER_565 :
            print("21")
            return
        MARKER_565.location = Jusme.Vector(1.0487340597E+04, -1489.0607744005, 1752.4060817997)
        MARKER_565.orientation = Jusme.Vector(270.0000000009, 90.0000000003, 90.0000000003)
        loc_ori = VecUtils.global2local(mlg_rod_L.location, mlg_rod_L.orientation, MARKER_565.location, MARKER_565.orientation)
        MARKER_565.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_565.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        mlg_struct_L = ascene.getObject(".{}.mlg_struct_L".format(model_name))
        if not mlg_struct_L :
            print("21")
            return

        #--------修改mlg_struct_L.MARKER_566
        MARKER_566 = ascene.getObject(".{}.mlg_struct_L.MARKER_566".format(model_name))
        if not MARKER_566 :
            print("21")
            return
        MARKER_566.location = Jusme.Vector(1.0487340597E+04, -1489.0607744005, 1752.4060817997)
        MARKER_566.orientation = Jusme.Vector(270.0000000009, 90.0000000003, 90.0000000003)
        loc_ori = VecUtils.global2local(mlg_struct_L.location, mlg_struct_L.orientation, MARKER_566.location, MARKER_566.orientation)
        MARKER_566.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_566.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----.JOINT_57
        JOINT_57 = ascene.getObject(".{}.JOINT_57".format(model_name))
        if not JOINT_57 :
            return
        JOINT_57.recompute()

        #-----.JOINT_56
        JOINT_56 = ascene.getObject(".{}.JOINT_56".format(model_name))
        if not JOINT_56 :
            return
        JOINT_56.recompute()

        #-----.JOINT_59
        JOINT_59 = ascene.getObject(".{}.JOINT_59".format(model_name))
        if not JOINT_59 :
            return
        JOINT_59.recompute()


        #===============================修改右侧主起结构=================================

        #-------------修改ground.MARKER_top_R和MARKER_bot_R
        MARKER_top_R = ascene.getObject(".{}.ground.MARKER_top_R".format(model_name))
        if not MARKER_top_R :
            print("7")
            return
        MARKER_top_R.location=VecUtils.LOC_ALONG_LINE(hpr_actuator_bot.location,hpr_actuator_top.location,(10/13)*VecUtils.DM(hpr_actuator_bot.location,hpr_actuator_top.location))
        
        MARKER_bot_R = ascene.getObject(".{}.ground.MARKER_bot_R".format(model_name))
        if not MARKER_bot_R :
            print("8")
            return
        MARKER_bot_R.location=VecUtils.LOC_ALONG_LINE(hpr_rod_bot.location,MARKER_top_R.location,(1/6)*VecUtils.DM(hpr_rod_bot.location,MARKER_top_R.location))
        
        #------------修改mlg_rod_R--------------------
        mlg_rod_R = ascene.getObject(".{}.mlg_rod_R".format(model_name))
        if not mlg_rod_R :
            print("9")
            return
        mlg_rod_R.location=0.5*(hpr_rod_bot.location+MARKER_top_R.location)
        mlg_rod_R.orientation=Jusme.Vector(0,90,90)

        #--------修改mlg_rod_R.MARKER_559
        MARKER_559 = ascene.getObject(".{}.mlg_rod_R.MARKER_559".format(model_name))
        if not MARKER_559 :
            print("10")
            return
        MARKER_559.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hpr_rod_bot))
        MARKER_559.orientation = Jusme.Vector(0,90,90)
        loc_ori = VecUtils.global2local(mlg_rod_R.location, mlg_rod_R.orientation, MARKER_559.location, MARKER_559.orientation)
        MARKER_559.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_559.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------修改mlg_rod_L.CYLINDER_315----------
        CYLINDER_315 = ascene.getObject(".{}.mlg_rod_R.CYLINDER_315".format(model_name))
        if not CYLINDER_315 :
            print("11")
            return
        CYLINDER_315.length=VecUtils.DM(hpr_rod_bot.location,MARKER_top_R.location)

        #------修改mlg_rod_L.cm
        cm = ascene.getObject(".{}.mlg_rod_R.cm".format(model_name))
        if not cm :
            print("12")
            return
        # cm.recompute()
        cm.location = 0.5*(hpr_rod_bot.location+MARKER_top_R.location)
        cm.orientation = Jusme.Vector(180.0, 90.0, 0.0)
        # loc_ori = VecUtils.global2local(mlg_rod_L.location, mlg_rod_L.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #------------修改mlg_actuator_R--------------------
        mlg_actuator_R = ascene.getObject(".{}.mlg_actuator_R".format(model_name))
        if not mlg_actuator_R :
            print("13")
            return
        mlg_actuator_R.location=0.5*(MARKER_bot_R.location+hpr_actuator_top.location)
        mlg_actuator_R.orientation=Jusme.Vector(0,90,90)
        
        #--------修改mlg_actuator_R.MARKER_560
        MARKER_560 = ascene.getObject(".{}.mlg_actuator_R.MARKER_560".format(model_name))
        if not MARKER_560 :
            print("14")
            return
        MARKER_560.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], MARKER_bot_R))
        MARKER_560.orientation = Jusme.Vector(0,90,90)
        loc_ori = VecUtils.global2local(mlg_actuator_R.location, mlg_actuator_R.orientation, MARKER_560.location, MARKER_560.orientation)
        MARKER_560.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_560.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
        
        #---------mlg_actuator_R.CYLINDER_320----------
        CYLINDER_320 = ascene.getObject(".{}.mlg_actuator_R.CYLINDER_320".format(model_name))
        if not CYLINDER_320 :
            print("15")
            return
        CYLINDER_320.length=VecUtils.DM(MARKER_bot_R.location,hpr_actuator_top.location)
        
        #------修改mlg_actuator_R.cm
        cm = ascene.getObject(".{}.mlg_actuator_R.cm".format(model_name))
        if not cm :
            print("16")
            return
        # cm.recompute()
        cm.location = 0.5*(MARKER_bot_R.location+hpr_actuator_top.location)
        cm.orientation = Jusme.Vector(180.0, 90.0, 90.0)
        # loc_ori = VecUtils.global2local(mlg_actuator_R.location, mlg_actuator_R.orientation, cm.location, cm.orientation)
        # cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        # cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------修改mlg_actuator_R和mlg_rod_R中的MARKER点--------------------------
        
        #-----------修改mlg_actuator_R.MARKER_1557
        MARKER_1557 = ascene.getObject(".{}.mlg_actuator_R.MARKER_1557".format(model_name))
        if not MARKER_1557 :
            print("21")
            return
        MARKER_1557.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_rod_topr)
        MARKER_1557.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(mlg_actuator_R.location, mlg_actuator_R.orientation, MARKER_1557.location, MARKER_1557.orientation)
        MARKER_1557.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_1557.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------修改mlg_rod_R.MARKER_1556
        MARKER_1556 = ascene.getObject(".{}.mlg_rod_R.MARKER_1556".format(model_name))
        if not MARKER_1556 :
            print("21")
            return
        MARKER_1556.location = Jusme.Vector(1.0487340597E+04, 1189.0607744005, 1752.4060817981)
        MARKER_1556.orientation = Jusme.Vector(0,0,0)
        loc_ori = VecUtils.global2local(mlg_rod_R.location, mlg_rod_R.orientation, MARKER_1556.location, MARKER_1556.orientation)
        MARKER_1556.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_1556.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------修改mlg_actuator_R.MARKER_602
        MARKER_602 = ascene.getObject(".{}.mlg_actuator_R.MARKER_602".format(model_name))
        if not MARKER_602 :
            print("21")
            return
        MARKER_602.location = Jusme.Vector(1.0487340597E+04, 1389.0607744005, 1752.4060818003)
        MARKER_602.orientation = Jusme.Vector(180,0,0)
        loc_ori = VecUtils.global2local(mlg_actuator_R.location, mlg_actuator_R.orientation, MARKER_602.location, MARKER_602.orientation)
        MARKER_602.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_602.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------修改mlg_rod_R.MARKER_603
        MARKER_603 = ascene.getObject(".{}.mlg_rod_R.MARKER_603".format(model_name))
        if not MARKER_603 :
            print("21")
            return
        MARKER_603.location = Jusme.Vector(1.0487340597E+04, 1489.0607744005, 1752.4060817997)
        MARKER_603.orientation = Jusme.Vector(180,0,0)
        loc_ori = VecUtils.global2local(mlg_rod_R.location, mlg_rod_R.orientation, MARKER_603.location, MARKER_603.orientation)
        MARKER_603.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_603.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------修改mlg_actuator_R.MARKER_592
        MARKER_592 = ascene.getObject(".{}.mlg_actuator_R.MARKER_592".format(model_name))
        if not MARKER_592 :
            print("21")
            return
        MARKER_592.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_actuator_bot)
        MARKER_592.orientation = Jusme.Vector(180,0,0)
        loc_ori = VecUtils.global2local(mlg_actuator_R.location, mlg_actuator_R.orientation, MARKER_592.location, MARKER_592.orientation)
        MARKER_592.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_592.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------修改mlg_rod_R.MARKER_593
        MARKER_593 = ascene.getObject(".{}.mlg_rod_R.MARKER_593".format(model_name))
        if not MARKER_593 :
            print("21")
            return
        MARKER_593.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_rod_bot)
        MARKER_593.orientation = Jusme.Vector(180,0,0)
        loc_ori = VecUtils.global2local(mlg_rod_R.location, mlg_rod_R.orientation, MARKER_593.location, MARKER_593.orientation)
        MARKER_593.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_593.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------修改mlg_actuator_R.MARKER_563
        MARKER_563 = ascene.getObject(".{}.mlg_actuator_R.MARKER_563".format(model_name))
        if not MARKER_563 :
            print("21")
            return
        MARKER_563.location = VecUtils.LOC_RELATIVE_TO([0,0,0],MARKER_bot_R)
        MARKER_563.orientation = VecUtils.ORI_ALONG_AXIS(hpr_actuator_top.location,hpr_rod_bot.location,'z')
        loc_ori = VecUtils.global2local(mlg_actuator_R.location, mlg_actuator_R.orientation, MARKER_563.location, MARKER_563.orientation)
        MARKER_563.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_563.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------修改mlg_rod_R.MARKER_564
        MARKER_564 = ascene.getObject(".{}.mlg_rod_R.MARKER_564".format(model_name))
        if not MARKER_564 :
            print("21")
            return
        MARKER_564.location = VecUtils.LOC_RELATIVE_TO([0,0,0],MARKER_bot_R)
        MARKER_564.orientation = VecUtils.ORI_ALONG_AXIS(hpr_actuator_top.location,hpr_rod_bot.location,'z')
        loc_ori = VecUtils.global2local(mlg_rod_R.location, mlg_rod_R.orientation, MARKER_564.location, MARKER_564.orientation)
        MARKER_564.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_564.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------修改mlg_actuator_R.MARKER_676
        MARKER_676 = ascene.getObject(".{}.mlg_actuator_R.MARKER_676".format(model_name))
        if not MARKER_676 :
            print("21")
            return
        MARKER_676.location = Jusme.Vector(1.0487340597E+04, 1389.0607744005, 1752.4060818003)
        MARKER_676.orientation = Jusme.Vector(113.4993529872, 73.6039865276, 2.2594229001)
        loc_ori = VecUtils.global2local(mlg_actuator_R.location, mlg_actuator_R.orientation, MARKER_676.location, MARKER_676.orientation)
        MARKER_676.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_676.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------修改mlg_rod_R.MARKER_677
        MARKER_677 = ascene.getObject(".{}.mlg_rod_R.MARKER_677".format(model_name))
        if not MARKER_677 :
            print("21")
            return
        MARKER_677.location = Jusme.Vector(1.0487340597E+04, 1489.0607744005, 1752.4060817997)
        MARKER_677.orientation = Jusme.Vector(113.4993529872, 73.6039865276, 2.2594229001)
        loc_ori = VecUtils.global2local(mlg_rod_R.location, mlg_rod_R.orientation, MARKER_677.location, MARKER_677.orientation)
        MARKER_677.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_677.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])



        #-----------修改mlg_actuator_R.MARKER_578
        MARKER_578 = ascene.getObject(".{}.mlg_actuator_R.MARKER_578".format(model_name))
        if not MARKER_578 :
            print("21")
            return
        MARKER_578.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_actuator_top)
        MARKER_578.orientation = Jusme.Vector(90,90,90)
        loc_ori = VecUtils.global2local(mlg_actuator_R.location, mlg_actuator_R.orientation, MARKER_578.location, MARKER_578.orientation)
        MARKER_578.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_578.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----------修改ground.MARKER_5791
        MARKER_5791 = ascene.getObject(".{}.ground.MARKER_5791".format(model_name))
        if not MARKER_5791 :
            print("21")
            return
        MARKER_5791.location = VecUtils.LOC_RELATIVE_TO([0,0,0],hpr_actuator_top)
        MARKER_5791.orientation = Jusme.Vector(90,90,90)
        loc_ori = VecUtils.global2local(mlg_actuator_R.location, mlg_actuator_R.orientation, MARKER_5791.location, MARKER_5791.orientation)
        MARKER_5791.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_5791.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])    
        
        #----------修改mlg_rod_R.MARKER_565
        MARKER_565 = ascene.getObject(".{}.mlg_rod_R.MARKER_565".format(model_name))
        if not MARKER_565 :
            print("21")
            return
        MARKER_565.location = Jusme.Vector(1.0487340597E+04, 1489.0607744005, 1752.4060817997)
        MARKER_565.orientation = Jusme.Vector(90,90,90)
        loc_ori = VecUtils.global2local(mlg_rod_R.location, mlg_rod_R.orientation, MARKER_565.location, MARKER_565.orientation)
        MARKER_565.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_565.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #----------修改mlg_struct_R.MARKER_566
        mlg_struct_R = ascene.getObject(".{}.mlg_struct_R".format(model_name))
        if not mlg_struct_R :
            print("21")
            return
        MARKER_566 = ascene.getObject(".{}.mlg_struct_R.MARKER_566".format(model_name))
        if not MARKER_566 :
            print("21")
            return
        MARKER_566.location = Jusme.Vector(1.0487340597E+04, 1489.0607744005, 1752.4060817997)
        MARKER_566.orientation = Jusme.Vector(90,90,90)
        loc_ori = VecUtils.global2local(mlg_struct_R.location, mlg_struct_R.orientation, MARKER_566.location, MARKER_566.orientation)
        MARKER_566.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
        MARKER_566.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

        #-----.JOINT_57_2
        JOINT_57_2 = ascene.getObject(".{}.JOINT_57_2".format(model_name))
        if not JOINT_57_2 :
            return
        JOINT_57_2.recompute()

        #-----.JOINT_56_2
        JOINT_56_2 = ascene.getObject(".{}.JOINT_56_2".format(model_name))
        if not JOINT_56_2 :
            return
        JOINT_56_2.recompute()

        #-----.JOINT_59_2
        JOINT_59_2 = ascene.getObject(".{}.JOINT_59_2".format(model_name))
        if not JOINT_59_2 :
            return
        JOINT_59_2.recompute()

        print("结束hpl_rod_bot硬点调整")

        pass

import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils 

import AbstractHps


import Common


class DropHpsLtaUtaAtchAdjust(AbstractHps.AbstractHpsAdjust) :
    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        pass

    def Adjust(self):
         ascene = Jusme.ActiveUSScene
         #----------------获取已调整位置的硬点节点
         hps_lta_uta_atch = ascene.getObject(self.hps_full_name)

         model_name = Common.getModelName()

         #---------------获取全局坐标系原点的mark点
         origo = ascene.getObject(".{}.ground.origo".format(model_name))

         if  hps_lta_uta_atch :  #-------------表示节点非空
             print("函数AdjustModelParameter中选中的硬点名称{}".format(self.hps_full_name))
             #-------------得到上扭力臂的根部硬点节点
             hps_uta_uc_atch = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_uta_uc_atch")
             #-------------得到下扭力臂的根部硬点节点
             hps_lta_lc_atch = ascene.getObject("._AA_nlg_post_2hubs.ground.hps_lta_lc_atch")

             point1 = hps_uta_uc_atch.location  #----------上圆柱体轴线定义的起点
             point2 = hps_lta_uta_atch.location   #----------圆柱体轴线定义的终点
             point3 = hps_lta_lc_atch.location  #----------下圆柱体轴线定义的起点

             #----------------得到上扭力臂的中心点gralin_9
             center_mark_u = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.gralin_9")
             print("修改前上圆柱体中心点位置{}".format(center_mark_u.location))

             #----------------得到上扭力臂的jxs_joint_j_8
             jxs_joint_j_8 = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.jxs_joint_j_8")

             #----------------得到下扭力臂的中心点
             center_mark_l = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.gralin_10")

             #----------------得到下扭力臂的._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_8
             jxs_joint_i_8 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_8")

             #-------获取ges_collar物体下jxs_joint_j_10的mark点节点对象
             jxs_joint_j_10 = ascene.getObject("._AA_nlg_post_2hubs.ges_collar.jxs_joint_j_10")

             #-----------获取上扭力臂下jxs_joint_i_10的mark点节点对象
             jxs_joint_i_10 = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.jxs_joint_i_10")

             #------------------获取ges_lower_cylinder下j._AA_nlg_post_2hubs.ges_lower_cylinder.jxs_joint_j_9
             jxs_joint_j_9 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder.jxs_joint_j_9")

             #-------------------得到下扭力臂的._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_9
             jxs_joint_i_9 = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_9")

             #----------------得到下扭力臂的._AA_nlg_post_2hubs.ges_lower_torque_arm.jxs_joint_i_9

             #-------计算上圆柱体在调整后的长度
             lenU = VecUtils.DM(point1, point2)
             print("上圆柱体在调整后的长度{}".format(lenU))

             #-----------------计算Point2点移动后的新全局坐标系下的欧拉角
             axis_u = VecUtils.ORI_ALONG_AXIS(point1, point2, 'z')
             print("上圆柱体在调整后的轴线欧拉角{}".format(axis_u))

             #--------获取上圆柱体part节点
             u_part = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm")

             if u_part :
                 #--------------设定上扭力臂Part的位置
                 loc = 0.5 * (point1 + point2)
                 u_part.location = loc
                 #---------------设定上扭力臂part的方向
                 u_part.orientation = axis_u

                 #设定上扭力臂中心点的位置转化为局部坐标系下的位置
                 print("上扭力臂起点转化为局部坐标系下的点")
                 center_mark_u.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uta_uc_atch))
                 center_mark_u.orientation = axis_u
                 loc_ori = VecUtils.global2local(u_part.location, u_part.orientation, center_mark_u.location, center_mark_u.orientation)
                 center_mark_u.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                 center_mark_u.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
                 print("调整后的上扭力臂中心点位置{}".format(center_mark_u.location))
                 print("调整后的上扭力臂中心点方向{}".format(center_mark_u.orientation))

                 #--------设定Mark点jxs_joint_j_8的位置和方向
                 jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_uta_atch))
                 jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
                 loc_ori = VecUtils.global2local(u_part.location, u_part.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
                 jxs_joint_j_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                 jxs_joint_j_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
                 print("调整后的上扭力臂jxs_joint_j_8点位置{}".format(jxs_joint_j_8.location))
                 print("调整后的上扭力臂jxs_joint_j_8点方向{}".format(jxs_joint_j_8.orientation))

                 #-------------调整上扭力臂的质心
                 cm = ascene.getObject(".{}.ges_upper_torque_arm.cm".format(model_name))
                 if not cm :
                     return
                 cm.location = u_part.location
                 cm.orientation = axis_u
                 loc_ori = VecUtils.global2local(u_part.location, u_part.orientation, cm.location, cm.orientation)
                 cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                 cm.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

                 #-------------调整上扭力臂的转动惯量Mark点位置
                 inertia_frame = ascene.getObject(".{}.ges_upper_torque_arm.inertia_frame".format(model_name))
                 inertia_frame.location = loc
                 inertia_frame.orientation = axis_u
                 loc_ori = VecUtils.global2local(u_part.location, u_part.orientation, inertia_frame.location, inertia_frame.orientation)
                 inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                 inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

                 #----------------------------调整ges_collar物体下jxs_joint_j_10的mark点节点对象
                 jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_uta_uc_atch))
                 jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], origo))
                 ges_collar = ascene.getObject("._AA_nlg_post_2hubs.ges_collar")
                 loc_ori = VecUtils.global2local(ges_collar.location, ges_collar.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
                 jxs_joint_j_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                 jxs_joint_j_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

                 #----------------------调整上扭力臂jxs_joint_i_10对象的位置
                 jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_10))
                 jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_10))
                 loc_ori = VecUtils.global2local(u_part.location, u_part.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
                 jxs_joint_i_10.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                 jxs_joint_i_10.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

                 #---------获取上圆柱体的几何体
                 u_part_geo = ascene.getObject("._AA_nlg_post_2hubs.ges_upper_torque_arm.gralin_upper_torque_arm_geom")
                 if u_part_geo :
                    u_part_geo.length = lenU  #-------------设定上扭力臂的长度




                
                 #----------------------------------------------------------------------------调整下扭力臂的结构参数
                 #-------计算下圆柱体在调整后的长度
                 lenL = VecUtils.DM(point3, point2)

                 #-------获取下圆柱体轴线在point2移动后的欧拉角
                 axis_l = VecUtils.ORI_ALONG_AXIS(point3, point2,'z')

                 #---------获取下圆柱体part节点
                 l_part = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm")

                 if l_part :
                    #--------------计算下扭力臂新中点位置
                    loc = 0.5 * (point3 + point2)
                    l_part.location = loc

                    #--------------设定下扭力臂的新方向
                    l_part.orientation = axis_l

                    #---------------设定下扭力臂中心点的局部坐标
                    center_mark_l.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_lc_atch))
                    center_mark_l.orientation = axis_l
                    loc_ori = VecUtils.global2local(l_part.location, l_part.orientation, center_mark_l.location, center_mark_l.orientation)
                    center_mark_l.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                    center_mark_l.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
                    print("调整后的下扭力臂中心点位置{}".format(center_mark_l.location))
                    print("调整后的下扭力臂中心点方向{}".format(center_mark_l.orientation))

                    jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_8))
                    jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_8))
                    loc_ori = VecUtils.global2local(l_part.location, l_part.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
                    jxs_joint_i_8.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                    jxs_joint_i_8.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])
                    print("调整后的下扭力臂jxs_joint_i_8点位置{}".format(jxs_joint_i_8.location))
                    print("调整后的下扭力臂jxs_joint_i_8点方向{}".format(jxs_joint_i_8.orientation))

                    #-------------调整ges_lower_cylinder下jxs_joint_j_9Mark点位置
                    #-----------获取ges_lower_cylinder对象节点
                    ges_lower_cylinder = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_cylinder")
                    jxs_joint_j_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], hps_lta_lc_atch))
                    jxs_joint_j_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], origo))
                    loc_ori = VecUtils.global2local(ges_lower_cylinder.location, ges_lower_cylinder.orientation, jxs_joint_j_9.location, jxs_joint_j_9.orientation)
                    jxs_joint_j_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                    jxs_joint_j_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

                    #-------------调整下扭力臂下jxs_joint_i_9Mark点位置
                    jxs_joint_i_9.location = (VecUtils.LOC_RELATIVE_TO([0, 0, 0], jxs_joint_j_9))
                    jxs_joint_i_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], jxs_joint_j_9))
                    loc_ori = VecUtils.global2local(l_part.location, l_part.orientation, jxs_joint_i_9.location, jxs_joint_i_9.orientation)
                    jxs_joint_i_9.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                    jxs_joint_i_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])


                    #-------------调整下扭力臂的质心
                    cm = ascene.getObject(".{}.ges_lower_torque_arm.cm".format(model_name))
                    cm.location = l_part.location
                    cm.orientation = axis_l
                    loc_ori = VecUtils.global2local(l_part.location, l_part.orientation, cm.location, cm.orientation)
                    cm.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                    jxs_joint_i_9.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

                    #-------------调整下扭力臂的转动惯量Mark点位置
                    inertia_frame = ascene.getObject(".{}.ges_lower_torque_arm.inertia_frame".format(model_name))
                    inertia_frame.location = loc
                    inertia_frame.orientation = axis_l
                    loc_ori = VecUtils.global2local(l_part.location, l_part.orientation, inertia_frame.location, inertia_frame.orientation)
                    inertia_frame.location = (loc_ori[0][0], loc_ori[0][1], loc_ori[0][2])
                    inertia_frame.orientation = (loc_ori[1][0], loc_ori[1][1], loc_ori[1][2])

                    
                 #--------获取下圆柱体集合体
                 l_part_geo = ascene.getObject("._AA_nlg_post_2hubs.ges_lower_torque_arm.gralin_lower_torque_arm_geom")
                 if l_part_geo :
                    l_part_geo.length = lenL

                 #----------更新运动服的位置
                 josrev_lta_uta_joint = ascene.getObject("._AA_nlg_post_2hubs.josrev_lta_uta_joint")
                 if josrev_lta_uta_joint :
                    josrev_lta_uta_joint.recompute()

                 josrev_uta_uc_joint = ascene.getObject("._AA_nlg_post_2hubs.josrev_uta_uc_joint")
                 if josrev_uta_uc_joint :
                     josrev_uta_uc_joint.recompute()

                 jossph_lta_lc_joint = ascene.getObject("._AA_nlg_post_2hubs.jossph_lta_lc_joint")
                 if jossph_lta_lc_joint :
                     jossph_lta_lc_joint.recompute()

         pass
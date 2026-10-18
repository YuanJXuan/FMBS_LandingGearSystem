# -*- coding: utf-8 -*-
"""Generated ADM overlay patch; do not create the physical model here.

Generated from the authoritative Adams CMD.  The ADM importer owns parts,
markers, constraints, forces and tire solver entities.  This module only
restores design expressions and CMD-only data objects.
"""

import os
import re
import traceback
import Jusme
from Fmbs.import_all_node import MakeSceneNodeByType
import FmbsShortcut.SCcmd.utils.VecUtils as VecUtils

SOURCE_MODEL_NAME = 'template_2_retract'
ADM_UDE_KINDS = {}

def apply_patch(model_dir=None, model_name=None):
    scene = Jusme.ActiveUSScene
    if scene is None:
        raise RuntimeError('没有活动模型，无法应用 ADM 补丁')
    model_name = model_name or SOURCE_MODEL_NAME
    source_root = '.' + SOURCE_MODEL_NAME
    target_root = '.' + model_name
    warnings = []
    errors = []
    updated = 0

    def root_path(path):
        if path == source_root or path.startswith(source_root + '.'):
            return target_root + path[len(source_root):]
        return path

    def path_candidates(path):
        resolved = root_path(path)
        candidates = [resolved]
        if not (resolved == target_root or resolved.startswith(target_root + '.')):
            return candidates
        relative = resolved[len(target_root):].lstrip('.')
        for instance_name, kind in sorted(ADM_UDE_KINDS.items(), key=lambda item: len(item[0]), reverse=True):
            if relative == instance_name:
                leaf_name = 'road_part' if kind == 'road' else 'wheel_part'
                candidate = target_root + '.' + instance_name.replace('.', '_') + '_' + leaf_name
            elif relative.startswith(instance_name + '.'):
                tail = relative[len(instance_name) + 1:]
                first, separator, remainder = tail.partition('.')
                if first in ('road_part', 'wheel_part', 'belt_part'):
                    candidate = target_root + '.' + instance_name.replace('.', '_') + '_' + first
                    if separator:
                        candidate += '.' + remainder
                else:
                    candidate = target_root + '.' + (instance_name + '.' + tail).replace('.', '_')
            else:
                continue
            if candidate not in candidates:
                candidates.append(candidate)
        return candidates

    def target_path(path):
        candidates = path_candidates(path)
        for candidate in candidates:
            if scene.getObject(candidate) is not None:
                return candidate
        return candidates[0]

    def rewrite_expression(value):
        text = str(value)
        text = re.sub(re.escape(source_root), target_root, text, flags=re.I)
        return re.sub(r'(?i)\.GCMB(?=\.|$)', target_root, text)

    def rewrite_simulation_command(value):
        text = rewrite_expression(value)
        return re.sub(
            r'(?i)(model_name\s*=\s*)\.[A-Za-z_][A-Za-z0-9_]*',
            lambda match: match.group(1) + target_root,
            text,
        )

    def get_object(path, required=True):
        candidates = path_candidates(path)
        node = None
        for resolved in candidates:
            node = scene.getObject(resolved)
            if node is not None:
                break
        if node is None and required:
            raise RuntimeError('ADM 补丁找不到对象：{}'.format(' 或 '.join(candidates)))
        return node

    def get_or_create(node_type, path):
        node = get_object(path, required=False)
        if node is None:
            node = MakeSceneNodeByType(node_type, target_path(path))
        return node

    def set_resource(path, value):
        node = get_object(path, required=False)
        if node is None:
            warnings.append('未找到资源数据节点：{}'.format(target_path(path)))
            return False
        properties = set(getattr(node, 'PropertiesList', []) or [])
        for prop in ('string_value', 'string', 'value'):
            if prop in properties or hasattr(node, prop):
                setattr(node, prop, value)
                return True
        warnings.append('资源数据节点没有字符串属性：{}'.format(target_path(path)))
        return False

    def record_error(step, exc):
        error_info = {
            'step': step,
            'error_type': type(exc).__name__,
            'error': str(exc),
        }
        errors.append(error_info)
        print('[模型补丁错误] {step}: {error_type}: {error}'.format(**error_info))
        trace_text = traceback.format_exc()
        if trace_text.strip() != 'NoneType: None':
            print(trace_text)

    try:
        node = get_or_create('SimuScript', '.template_2_retract.Last_Sim')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_2_retract.Last_Sim')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 number_of_steps=1200 model_name=.gcmb2_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_2_retract.Last_Sim', exc)

    try:
        node = get_or_create('SimuScript', '.template_2_retract.Last_Sim_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_2_retract.Last_Sim_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_2_retract.Last_Sim_2', exc)

    try:
        node = get_object('.template_2_retract.MOTION_disp')
        node.function = rewrite_expression('-STEP( time , 0 , 0 , .template_2_retract.NLG_RETRACT_TIME , .template_2_retract.NLG_ACTUATOR_STROKE )-STEP( time , .template_2_retract.NLG_RETRACT_TIME+.template_2_retract.NLG_UP_HOLD_TIME , 0 ,  .template_2_retract.NLG_RETRACT_TIME+.template_2_retract.NLG_UP_HOLD_TIME+.template_2_retract.NLG_EXTEND_TIME , -.template_2_retract.NLG_ACTUATOR_STROKE )')
        updated += 1

    except Exception as exc:
        record_error('constraint modify motion_generator .template_2_retract.MOTION_disp', exc)

    try:
        node = get_object('.template_2_retract.NLG_aeroforce')
        node.x_force_function = rewrite_expression('.template_2_retract.NLG_DRAG_CORFF*abs(IF( .template_2_retract.NLG_sf_angle-60 : COS( 1.225*.template_2_retract.NLG_sf_angle*pi/180 ) , COS( 1.225*.template_2_retract.NLG_sf_angle*pi/180 ) , COS( .template_2_retract.NLG_sf_angle*pi/180 ) ))*.template_2_retract.NLG_PROJ_AREA*cos(.template_2_retract.NLG_sf_angle*pi/180)*0.5*.template_2_retract.AIR_DENSITY*.template_2_retract.AIR_VELOCITY*abs(.template_2_retract.AIR_VELOCITY)*cos(.template_2_retract.NLG_sf_angle*pi/180) ')
        node.y_force_function = rewrite_expression('0')
        node.z_force_function = rewrite_expression('.template_2_retract.NLG_DRAG_CORFF*abs(IF( .template_2_retract.NLG_sf_angle-60 : COS( 1.225*.template_2_retract.NLG_sf_angle*pi/180 ) , COS( 1.225*.template_2_retract.NLG_sf_angle*pi/180 ) , COS( .template_2_retract.NLG_sf_angle*pi/180 ) ))*.template_2_retract.NLG_PROJ_AREA*cos(.template_2_retract.NLG_sf_angle*pi/180)*0.5*.template_2_retract.AIR_DENSITY*.template_2_retract.AIR_VELOCITY*abs(.template_2_retract.AIR_VELOCITY)*sin(.template_2_retract.NLG_sf_angle*pi/180) ')
        node.x_torque_function = rewrite_expression('0')
        node.y_torque_function = rewrite_expression('-1*CUBSPL( .template_2_retract.NLG_sf_angle, 0 , .template_2_retract.SPLINE_angle_aeroforce, 0 )')
        node.z_torque_function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('force modify direct general_force .template_2_retract.NLG_aeroforce', exc)

    try:
        cfs_collar_top = get_object('.template_2_retract.ground.cfs_collar_top')
        cfs_collar_top.marker_name = target_path('.template_2_retract.ground.cfs_collar_top')
        _template_2_retract_ground_hps_uc_bot = get_object('.template_2_retract.ground.hps_uc_bot').location
        _template_2_retract_ground_hps_uc_top = get_object('.template_2_retract.ground.hps_uc_top').location
        cfs_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_2_retract_ground_hps_uc_bot, _template_2_retract_ground_hps_uc_top, 0.11 * VecUtils.DM(_template_2_retract_ground_hps_uc_bot, _template_2_retract_ground_hps_uc_top)))
        _template_2_retract_ground_hps_uc_bot = get_object('.template_2_retract.ground.hps_uc_bot').location
        _template_2_retract_ground_hps_uc_top = get_object('.template_2_retract.ground.hps_uc_top').location
        cfs_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_uc_bot, _template_2_retract_ground_hps_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ground.cfs_collar_top', exc)

    try:
        gralin_1 = get_object('.template_2_retract.ges_sf_actuator.gralin_1')
        relative_to = get_object('.template_2_retract.ges_sf_actuator')
        gralin_1.relative_to = relative_to
        gralin_1.marker_name = target_path('.template_2_retract.ges_sf_actuator.gralin_1')
        _template_2_retract_ground_hps_db_sf_atch = get_object('.template_2_retract.ground.hps_db_sf_atch')
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_db_sf_atch))
        _template_2_retract_ground_hps_db_sf_atch = get_object('.template_2_retract.ground.hps_db_sf_atch').location
        _template_2_retract_ground_hps_db_uc_atch = get_object('.template_2_retract.ground.hps_db_uc_atch').location
        gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_db_sf_atch, _template_2_retract_ground_hps_db_uc_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_sf_actuator.gralin_1', exc)

    try:
        jxs_joint_i_14 = get_object('.template_2_retract.ges_sf_actuator.jxs_joint_i_14')
        relative_to = get_object('.template_2_retract.ges_sf_actuator')
        jxs_joint_i_14.relative_to = relative_to
        jxs_joint_i_14.marker_name = target_path('.template_2_retract.ges_sf_actuator.jxs_joint_i_14')
        _template_2_retract_ges_subframe_jxs_joint_j_14 = get_object('.template_2_retract.ges_subframe.jxs_joint_j_14')
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_subframe_jxs_joint_j_14))
        _template_2_retract_ges_subframe_jxs_joint_j_14 = get_object('.template_2_retract.ges_subframe.jxs_joint_j_14')
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_subframe_jxs_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_sf_actuator.jxs_joint_i_14', exc)

    try:
        gralin_dragbrace_geom = get_object('.template_2_retract.ges_sf_actuator.gralin_dragbrace_geom')
        gralin_dragbrace_geom.cylinder_name = target_path('.template_2_retract.ges_sf_actuator.gralin_dragbrace_geom')
        _template_2_retract_ground_hps_db_sf_atch = get_object('.template_2_retract.ground.hps_db_sf_atch').location
        _template_2_retract_ground_hps_db_uc_atch = get_object('.template_2_retract.ground.hps_db_uc_atch').location
        gralin_dragbrace_geom.length = (VecUtils.DM(_template_2_retract_ground_hps_db_sf_atch, _template_2_retract_ground_hps_db_uc_atch) - 50.0)


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_sf_actuator.gralin_dragbrace_geom', exc)

    try:
        MARKER_4 = get_object('.template_2_retract.ges_upper_cylinder.MARKER_4')
        relative_to = get_object('.template_2_retract.ges_upper_cylinder')
        MARKER_4.relative_to = relative_to
        MARKER_4.marker_name = target_path('.template_2_retract.ges_upper_cylinder.MARKER_4')
        _template_2_retract_ges_sf_rod_PT3 = get_object('.template_2_retract.ges_sf_rod.PT3')
        MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_sf_rod_PT3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_4.location, MARKER_4.orientation)
        MARKER_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_cylinder.MARKER_4', exc)

    try:
        gralin_2 = get_object('.template_2_retract.ges_upper_cylinder.gralin_2')
        relative_to = get_object('.template_2_retract.ges_upper_cylinder')
        gralin_2.relative_to = relative_to
        gralin_2.marker_name = target_path('.template_2_retract.ges_upper_cylinder.gralin_2')
        _template_2_retract_ground_hps_uc_top = get_object('.template_2_retract.ground.hps_uc_top')
        gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_uc_top))
        _template_2_retract_ground_hps_uc_top = get_object('.template_2_retract.ground.hps_uc_top').location
        _template_2_retract_ground_hps_uc_bot = get_object('.template_2_retract.ground.hps_uc_bot').location
        gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_uc_top, _template_2_retract_ground_hps_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_2.location, gralin_2.orientation)
        gralin_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_cylinder.gralin_2', exc)

    try:
        gralin_3 = get_object('.template_2_retract.ges_upper_cylinder.gralin_3')
        relative_to = get_object('.template_2_retract.ges_upper_cylinder')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_2_retract.ges_upper_cylinder.gralin_3')
        _template_2_retract_ground_hps_uc_sf_atch_l = get_object('.template_2_retract.ground.hps_uc_sf_atch_l')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_uc_sf_atch_l))
        _template_2_retract_ground_hps_uc_sf_atch_l = get_object('.template_2_retract.ground.hps_uc_sf_atch_l').location
        _template_2_retract_ground_hps_uc_geompt = get_object('.template_2_retract.ground.hps_uc_geompt').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_uc_sf_atch_l, _template_2_retract_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_cylinder.gralin_3', exc)

    try:
        gralin_4 = get_object('.template_2_retract.ges_upper_cylinder.gralin_4')
        relative_to = get_object('.template_2_retract.ges_upper_cylinder')
        gralin_4.relative_to = relative_to
        gralin_4.marker_name = target_path('.template_2_retract.ges_upper_cylinder.gralin_4')
        _template_2_retract_ground_hps_uc_sf_atch_r = get_object('.template_2_retract.ground.hps_uc_sf_atch_r')
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_uc_sf_atch_r))
        _template_2_retract_ground_hps_uc_sf_atch_r = get_object('.template_2_retract.ground.hps_uc_sf_atch_r').location
        _template_2_retract_ground_hps_uc_geompt = get_object('.template_2_retract.ground.hps_uc_geompt').location
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_uc_sf_atch_r, _template_2_retract_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_cylinder.gralin_4', exc)

    try:
        jxs_joint_i_15 = get_object('.template_2_retract.ges_upper_cylinder.jxs_joint_i_15')
        relative_to = get_object('.template_2_retract.ges_upper_cylinder')
        jxs_joint_i_15.relative_to = relative_to
        jxs_joint_i_15.marker_name = target_path('.template_2_retract.ges_upper_cylinder.jxs_joint_i_15')
        _template_2_retract_ges_subframe_jxs_joint_j_15 = get_object('.template_2_retract.ges_subframe.jxs_joint_j_15')
        jxs_joint_i_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_subframe_jxs_joint_j_15))
        _template_2_retract_ges_subframe_jxs_joint_j_15 = get_object('.template_2_retract.ges_subframe.jxs_joint_j_15')
        jxs_joint_i_15.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_subframe_jxs_joint_j_15))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_15.location, jxs_joint_i_15.orientation)
        jxs_joint_i_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_cylinder.jxs_joint_i_15', exc)

    try:
        jxs_joint_j_1 = get_object('.template_2_retract.ges_upper_cylinder.jxs_joint_j_1')
        relative_to = get_object('.template_2_retract.ges_upper_cylinder')
        jxs_joint_j_1.relative_to = relative_to
        jxs_joint_j_1.marker_name = target_path('.template_2_retract.ges_upper_cylinder.jxs_joint_j_1')
        _template_2_retract_ground_cfs_collar_top = get_object('.template_2_retract.ground.cfs_collar_top')
        jxs_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_cfs_collar_top))
        _template_2_retract_ground_hps_uc_bot = get_object('.template_2_retract.ground.hps_uc_bot').location
        _template_2_retract_ground_hps_uc_top = get_object('.template_2_retract.ground.hps_uc_top').location
        jxs_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_uc_bot, _template_2_retract_ground_hps_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
        jxs_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_cylinder.jxs_joint_j_1', exc)

    try:
        MARKER_162 = get_object('.template_2_retract.ges_upper_cylinder.MARKER_162')
        relative_to = get_object('.template_2_retract.ges_upper_cylinder')
        MARKER_162.relative_to = relative_to
        MARKER_162.marker_name = target_path('.template_2_retract.ges_upper_cylinder.MARKER_162')
        _template_2_retract_ground_hps_aeroforceN = get_object('.template_2_retract.ground.hps_aeroforceN')
        MARKER_162.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_aeroforceN))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_162.location, MARKER_162.orientation)
        MARKER_162.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_cylinder.MARKER_162', exc)

    try:
        gralin_upper_cylinder_geom1 = get_object('.template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        gralin_upper_cylinder_geom1.cylinder_name = target_path('.template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        _template_2_retract_ground_hps_uc_top = get_object('.template_2_retract.ground.hps_uc_top').location
        _template_2_retract_ground_hps_uc_bot = get_object('.template_2_retract.ground.hps_uc_bot').location
        gralin_upper_cylinder_geom1.length = (VecUtils.DM(_template_2_retract_ground_hps_uc_top, _template_2_retract_ground_hps_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom1', exc)

    try:
        gralin_upper_cylinder_geom2 = get_object('.template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        gralin_upper_cylinder_geom2.cylinder_name = target_path('.template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        _template_2_retract_ground_hps_uc_sf_atch_l = get_object('.template_2_retract.ground.hps_uc_sf_atch_l').location
        _template_2_retract_ground_hps_uc_geompt = get_object('.template_2_retract.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom2.length = (VecUtils.DM(_template_2_retract_ground_hps_uc_sf_atch_l, _template_2_retract_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom2', exc)

    try:
        gralin_upper_cylinder_geom3 = get_object('.template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        gralin_upper_cylinder_geom3.cylinder_name = target_path('.template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        _template_2_retract_ground_hps_uc_sf_atch_r = get_object('.template_2_retract.ground.hps_uc_sf_atch_r').location
        _template_2_retract_ground_hps_uc_geompt = get_object('.template_2_retract.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom3.length = (VecUtils.DM(_template_2_retract_ground_hps_uc_sf_atch_r, _template_2_retract_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_upper_cylinder.gralin_upper_cylinder_geom3', exc)

    try:
        gralin_5 = get_object('.template_2_retract.ges_lower_cylinder.gralin_5')
        relative_to = get_object('.template_2_retract.ges_lower_cylinder')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_2_retract.ges_lower_cylinder.gralin_5')
        _template_2_retract_ground_hps_lc_top = get_object('.template_2_retract.ground.hps_lc_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_lc_top))
        _template_2_retract_ground_hps_lc_top = get_object('.template_2_retract.ground.hps_lc_top').location
        _template_2_retract_ground_hps_lc_bot = get_object('.template_2_retract.ground.hps_lc_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_lc_top, _template_2_retract_ground_hps_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_cylinder.gralin_5', exc)

    try:
        jxs_joint_j_9 = get_object('.template_2_retract.ges_lower_cylinder.jxs_joint_j_9')
        relative_to = get_object('.template_2_retract.ges_lower_cylinder')
        jxs_joint_j_9.relative_to = relative_to
        jxs_joint_j_9.marker_name = target_path('.template_2_retract.ges_lower_cylinder.jxs_joint_j_9')
        _template_2_retract_ground_hps_lta_lc_atch = get_object('.template_2_retract.ground.hps_lta_lc_atch')
        jxs_joint_j_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_lta_lc_atch))
        _template_2_retract_ground_origo = get_object('.template_2_retract.ground.origo')
        jxs_joint_j_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_9.location, jxs_joint_j_9.orientation)
        jxs_joint_j_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_cylinder.jxs_joint_j_9', exc)

    try:
        jxs_joint_i_11 = get_object('.template_2_retract.ges_lower_cylinder.jxs_joint_i_11')
        relative_to = get_object('.template_2_retract.ges_lower_cylinder')
        jxs_joint_i_11.relative_to = relative_to
        jxs_joint_i_11.marker_name = target_path('.template_2_retract.ges_lower_cylinder.jxs_joint_i_11')
        _template_2_retract_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_2_retract.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_upper_cylinder_jxs_joint_j_11))
        _template_2_retract_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_2_retract.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_upper_cylinder_jxs_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
        jxs_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_cylinder.jxs_joint_i_11', exc)

    try:
        gralin_7 = get_object('.template_2_retract.ges_lower_cylinder.gralin_7')
        relative_to = get_object('.template_2_retract.ges_lower_cylinder')
        gralin_7.relative_to = relative_to
        gralin_7.marker_name = target_path('.template_2_retract.ges_lower_cylinder.gralin_7')
        _template_2_retract_ground_hpr_wheel_center = get_object('.template_2_retract.ground.hpr_wheel_center')
        gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hpr_wheel_center))
        _template_2_retract_ground_hpr_wheel_center = get_object('.template_2_retract.ground.hpr_wheel_center').location
        _template_2_retract_ground_hpl_wheel_center = get_object('.template_2_retract.ground.hpl_wheel_center').location
        gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hpr_wheel_center, _template_2_retract_ground_hpl_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_cylinder.gralin_7', exc)

    try:
        MARKER_163 = get_object('.template_2_retract.ges_lower_cylinder.MARKER_163')
        relative_to = get_object('.template_2_retract.ges_lower_cylinder')
        MARKER_163.relative_to = relative_to
        MARKER_163.marker_name = target_path('.template_2_retract.ges_lower_cylinder.MARKER_163')
        _template_2_retract_ground_hps_aeroforceN = get_object('.template_2_retract.ground.hps_aeroforceN')
        MARKER_163.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_aeroforceN))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_163.location, MARKER_163.orientation)
        MARKER_163.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_cylinder.MARKER_163', exc)

    try:
        MARKER_165 = get_object('.template_2_retract.ges_lower_cylinder.MARKER_165')
        relative_to = get_object('.template_2_retract.ges_lower_cylinder')
        MARKER_165.relative_to = relative_to
        MARKER_165.marker_name = target_path('.template_2_retract.ges_lower_cylinder.MARKER_165')
        _template_2_retract_ground_hpl_ob_axle = get_object('.template_2_retract.ground.hpl_ob_axle')
        MARKER_165.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hpl_ob_axle))
        _template_2_retract_ground_hpl_ob_axle = get_object('.template_2_retract.ground.hpl_ob_axle').location
        _template_2_retract_ground_hpl_wheel_center = get_object('.template_2_retract.ground.hpl_wheel_center').location
        MARKER_165.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hpl_ob_axle, _template_2_retract_ground_hpl_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_165.location, MARKER_165.orientation)
        MARKER_165.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_165.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_cylinder.MARKER_165', exc)

    try:
        MARKER_166 = get_object('.template_2_retract.ges_lower_cylinder.MARKER_166')
        relative_to = get_object('.template_2_retract.ges_lower_cylinder')
        MARKER_166.relative_to = relative_to
        MARKER_166.marker_name = target_path('.template_2_retract.ges_lower_cylinder.MARKER_166')
        _template_2_retract_ground_hpr_ob_axle = get_object('.template_2_retract.ground.hpr_ob_axle')
        MARKER_166.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hpr_ob_axle))
        _template_2_retract_ground_hpr_ob_axle = get_object('.template_2_retract.ground.hpr_ob_axle').location
        _template_2_retract_ground_hpr_wheel_center = get_object('.template_2_retract.ground.hpr_wheel_center').location
        MARKER_166.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hpr_ob_axle, _template_2_retract_ground_hpr_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_166.location, MARKER_166.orientation)
        MARKER_166.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_166.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_cylinder.MARKER_166', exc)

    try:
        gralin_geom1 = get_object('.template_2_retract.ges_lower_cylinder.gralin_geom1')
        gralin_geom1.cylinder_name = target_path('.template_2_retract.ges_lower_cylinder.gralin_geom1')
        _template_2_retract_ground_hps_lc_top = get_object('.template_2_retract.ground.hps_lc_top').location
        _template_2_retract_ground_hps_lc_bot = get_object('.template_2_retract.ground.hps_lc_bot').location
        gralin_geom1.length = (VecUtils.DM(_template_2_retract_ground_hps_lc_top, _template_2_retract_ground_hps_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_lower_cylinder.gralin_geom1', exc)

    try:
        gralin_geom2 = get_object('.template_2_retract.ges_lower_cylinder.gralin_geom2')
        gralin_geom2.cylinder_name = target_path('.template_2_retract.ges_lower_cylinder.gralin_geom2')
        _template_2_retract_ground_hpr_wheel_center = get_object('.template_2_retract.ground.hpr_wheel_center').location
        _template_2_retract_ground_hpl_wheel_center = get_object('.template_2_retract.ground.hpl_wheel_center').location
        gralin_geom2.length = (VecUtils.DM(_template_2_retract_ground_hpr_wheel_center, _template_2_retract_ground_hpl_wheel_center))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_lower_cylinder.gralin_geom2', exc)

    try:
        gralin_9 = get_object('.template_2_retract.ges_upper_torque_arm.gralin_9')
        relative_to = get_object('.template_2_retract.ges_upper_torque_arm')
        gralin_9.relative_to = relative_to
        gralin_9.marker_name = target_path('.template_2_retract.ges_upper_torque_arm.gralin_9')
        _template_2_retract_ground_hps_uta_uc_atch = get_object('.template_2_retract.ground.hps_uta_uc_atch')
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_uta_uc_atch))
        _template_2_retract_ground_hps_uta_uc_atch = get_object('.template_2_retract.ground.hps_uta_uc_atch').location
        _template_2_retract_ground_hps_lta_uta_atch = get_object('.template_2_retract.ground.hps_lta_uta_atch').location
        gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_uta_uc_atch, _template_2_retract_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_torque_arm.gralin_9', exc)

    try:
        jxs_joint_j_8 = get_object('.template_2_retract.ges_upper_torque_arm.jxs_joint_j_8')
        relative_to = get_object('.template_2_retract.ges_upper_torque_arm')
        jxs_joint_j_8.relative_to = relative_to
        jxs_joint_j_8.marker_name = target_path('.template_2_retract.ges_upper_torque_arm.jxs_joint_j_8')
        _template_2_retract_ground_hps_lta_uta_atch = get_object('.template_2_retract.ground.hps_lta_uta_atch')
        jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_lta_uta_atch))
        _template_2_retract_ground_origo = get_object('.template_2_retract.ground.origo')
        jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_2_retract_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
        jxs_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_torque_arm.jxs_joint_j_8', exc)

    try:
        jxs_joint_i_10 = get_object('.template_2_retract.ges_upper_torque_arm.jxs_joint_i_10')
        relative_to = get_object('.template_2_retract.ges_upper_torque_arm')
        jxs_joint_i_10.relative_to = relative_to
        jxs_joint_i_10.marker_name = target_path('.template_2_retract.ges_upper_torque_arm.jxs_joint_i_10')
        _template_2_retract_ges_collar_jxs_joint_j_10 = get_object('.template_2_retract.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_collar_jxs_joint_j_10))
        _template_2_retract_ges_collar_jxs_joint_j_10 = get_object('.template_2_retract.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_collar_jxs_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
        jxs_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_upper_torque_arm.jxs_joint_i_10', exc)

    try:
        gralin_upper_torque_arm_geom = get_object('.template_2_retract.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        gralin_upper_torque_arm_geom.cylinder_name = target_path('.template_2_retract.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        _template_2_retract_ground_hps_uta_uc_atch = get_object('.template_2_retract.ground.hps_uta_uc_atch').location
        _template_2_retract_ground_hps_lta_uta_atch = get_object('.template_2_retract.ground.hps_lta_uta_atch').location
        gralin_upper_torque_arm_geom.length = (VecUtils.DM(_template_2_retract_ground_hps_uta_uc_atch, _template_2_retract_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_upper_torque_arm.gralin_upper_torque_arm_geom', exc)

    try:
        jxs_joint_i_8 = get_object('.template_2_retract.ges_lower_torque_arm.jxs_joint_i_8')
        relative_to = get_object('.template_2_retract.ges_lower_torque_arm')
        jxs_joint_i_8.relative_to = relative_to
        jxs_joint_i_8.marker_name = target_path('.template_2_retract.ges_lower_torque_arm.jxs_joint_i_8')
        _template_2_retract_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_2_retract.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_upper_torque_arm_jxs_joint_j_8))
        _template_2_retract_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_2_retract.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_upper_torque_arm_jxs_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
        jxs_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_torque_arm.jxs_joint_i_8', exc)

    try:
        gralin_10 = get_object('.template_2_retract.ges_lower_torque_arm.gralin_10')
        relative_to = get_object('.template_2_retract.ges_lower_torque_arm')
        gralin_10.relative_to = relative_to
        gralin_10.marker_name = target_path('.template_2_retract.ges_lower_torque_arm.gralin_10')
        _template_2_retract_ground_hps_lta_lc_atch = get_object('.template_2_retract.ground.hps_lta_lc_atch')
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_lta_lc_atch))
        _template_2_retract_ground_hps_lta_lc_atch = get_object('.template_2_retract.ground.hps_lta_lc_atch').location
        _template_2_retract_ground_hps_lta_uta_atch = get_object('.template_2_retract.ground.hps_lta_uta_atch').location
        gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_lta_lc_atch, _template_2_retract_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_torque_arm.gralin_10', exc)

    try:
        jxs_joint_i_9 = get_object('.template_2_retract.ges_lower_torque_arm.jxs_joint_i_9')
        relative_to = get_object('.template_2_retract.ges_lower_torque_arm')
        jxs_joint_i_9.relative_to = relative_to
        jxs_joint_i_9.marker_name = target_path('.template_2_retract.ges_lower_torque_arm.jxs_joint_i_9')
        _template_2_retract_ges_lower_cylinder_jxs_joint_j_9 = get_object('.template_2_retract.ges_lower_cylinder.jxs_joint_j_9')
        jxs_joint_i_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_lower_cylinder_jxs_joint_j_9))
        _template_2_retract_ges_lower_cylinder_jxs_joint_j_9 = get_object('.template_2_retract.ges_lower_cylinder.jxs_joint_j_9')
        jxs_joint_i_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_lower_cylinder_jxs_joint_j_9))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_9.location, jxs_joint_i_9.orientation)
        jxs_joint_i_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_lower_torque_arm.jxs_joint_i_9', exc)

    try:
        gralin_lower_torque_arm_geom = get_object('.template_2_retract.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        gralin_lower_torque_arm_geom.cylinder_name = target_path('.template_2_retract.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        _template_2_retract_ground_hps_lta_lc_atch = get_object('.template_2_retract.ground.hps_lta_lc_atch').location
        _template_2_retract_ground_hps_lta_uta_atch = get_object('.template_2_retract.ground.hps_lta_uta_atch').location
        gralin_lower_torque_arm_geom.length = (VecUtils.DM(_template_2_retract_ground_hps_lta_lc_atch, _template_2_retract_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_lower_torque_arm.gralin_lower_torque_arm_geom', exc)

    try:
        inertia_frame = get_object('.template_2_retract.ges_subframe.inertia_frame')
        relative_to = get_object('.template_2_retract.ges_subframe')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_retract.ges_subframe.inertia_frame')
        _template_2_retract_ges_subframe_cm = get_object('.template_2_retract.ges_subframe.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_subframe_cm))
        _template_2_retract_ges_subframe = get_object('.template_2_retract.ges_subframe')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_subframe))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_subframe.inertia_frame', exc)

    try:
        graout_1 = get_object('.template_2_retract.ges_subframe.graout_1')
        relative_to = get_object('.template_2_retract.ges_subframe')
        graout_1.relative_to = relative_to
        graout_1.marker_name = target_path('.template_2_retract.ges_subframe.graout_1')
        _template_2_retract_ground_hps_uc_sf_atch_r = get_object('.template_2_retract.ground.hps_uc_sf_atch_r')
        graout_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_uc_sf_atch_r))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_1.location, graout_1.orientation)
        graout_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_subframe.graout_1', exc)

    try:
        graout_2 = get_object('.template_2_retract.ges_subframe.graout_2')
        relative_to = get_object('.template_2_retract.ges_subframe')
        graout_2.relative_to = relative_to
        graout_2.marker_name = target_path('.template_2_retract.ges_subframe.graout_2')
        _template_2_retract_ground_hps_uc_sf_atch_l = get_object('.template_2_retract.ground.hps_uc_sf_atch_l')
        graout_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_uc_sf_atch_l))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_2.location, graout_2.orientation)
        graout_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_subframe.graout_2', exc)

    try:
        graout_3 = get_object('.template_2_retract.ges_subframe.graout_3')
        relative_to = get_object('.template_2_retract.ges_subframe')
        graout_3.relative_to = relative_to
        graout_3.marker_name = target_path('.template_2_retract.ges_subframe.graout_3')
        _template_2_retract_ground_hps_db_sf_atch = get_object('.template_2_retract.ground.hps_db_sf_atch')
        graout_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_db_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_3.location, graout_3.orientation)
        graout_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_subframe.graout_3', exc)

    try:
        jxs_joint_j_15 = get_object('.template_2_retract.ges_subframe.jxs_joint_j_15')
        relative_to = get_object('.template_2_retract.ges_subframe')
        jxs_joint_j_15.relative_to = relative_to
        jxs_joint_j_15.marker_name = target_path('.template_2_retract.ges_subframe.jxs_joint_j_15')
        _template_2_retract_ground_cfs_uc_sf_atch_mid = get_object('.template_2_retract.ground.cfs_uc_sf_atch_mid')
        jxs_joint_j_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_cfs_uc_sf_atch_mid))
        _template_2_retract_ground_cfs_uc_sf_atch_mid = get_object('.template_2_retract.ground.cfs_uc_sf_atch_mid')
        jxs_joint_j_15.orientation = _template_2_retract_ground_cfs_uc_sf_atch_mid.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_15.location, jxs_joint_j_15.orientation)
        jxs_joint_j_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_subframe.jxs_joint_j_15', exc)

    try:
        jxs_joint_j_14 = get_object('.template_2_retract.ges_subframe.jxs_joint_j_14')
        relative_to = get_object('.template_2_retract.ges_subframe')
        jxs_joint_j_14.relative_to = relative_to
        jxs_joint_j_14.marker_name = target_path('.template_2_retract.ges_subframe.jxs_joint_j_14')
        _template_2_retract_ground_hps_db_sf_atch = get_object('.template_2_retract.ground.hps_db_sf_atch')
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_db_sf_atch))
        _template_2_retract_ground_origo = get_object('.template_2_retract.ground.origo')
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_2_retract_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_subframe.jxs_joint_j_14', exc)

    try:
        jxs_joint_j_10 = get_object('.template_2_retract.ges_collar.jxs_joint_j_10')
        relative_to = get_object('.template_2_retract.ges_collar')
        jxs_joint_j_10.relative_to = relative_to
        jxs_joint_j_10.marker_name = target_path('.template_2_retract.ges_collar.jxs_joint_j_10')
        _template_2_retract_ground_hps_uta_uc_atch = get_object('.template_2_retract.ground.hps_uta_uc_atch')
        jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_uta_uc_atch))
        _template_2_retract_ground_origo = get_object('.template_2_retract.ground.origo')
        jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_2_retract_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
        jxs_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_collar.jxs_joint_j_10', exc)

    try:
        gralin_24 = get_object('.template_2_retract.ges_collar.gralin_24')
        relative_to = get_object('.template_2_retract.ges_collar')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_2_retract.ges_collar.gralin_24')
        _template_2_retract_ground_hps_uc_bot = get_object('.template_2_retract.ground.hps_uc_bot')
        gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_uc_bot))
        _template_2_retract_ground_hps_uc_bot = get_object('.template_2_retract.ground.hps_uc_bot').location
        _template_2_retract_ground_cfs_collar_top = get_object('.template_2_retract.ground.cfs_collar_top').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ground_hps_uc_bot, _template_2_retract_ground_cfs_collar_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_collar.gralin_24', exc)

    try:
        jxs_joint_i_1 = get_object('.template_2_retract.ges_collar.jxs_joint_i_1')
        relative_to = get_object('.template_2_retract.ges_collar')
        jxs_joint_i_1.relative_to = relative_to
        jxs_joint_i_1.marker_name = target_path('.template_2_retract.ges_collar.jxs_joint_i_1')
        _template_2_retract_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_retract.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_retract_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_retract.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
        jxs_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_collar.jxs_joint_i_1', exc)

    try:
        gralin_collar = get_object('.template_2_retract.ges_collar.gralin_collar')
        gralin_collar.cylinder_name = target_path('.template_2_retract.ges_collar.gralin_collar')
        _template_2_retract_ground_hps_uc_bot = get_object('.template_2_retract.ground.hps_uc_bot').location
        _template_2_retract_ground_cfs_collar_top = get_object('.template_2_retract.ground.cfs_collar_top').location
        gralin_collar.length = (VecUtils.DM(_template_2_retract_ground_hps_uc_bot, _template_2_retract_ground_cfs_collar_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_collar.gralin_collar', exc)

    try:
        MARKER_5 = get_object('.template_2_retract.ges_sf_rod.MARKER_5')
        relative_to = get_object('.template_2_retract.ges_sf_rod')
        MARKER_5.relative_to = relative_to
        MARKER_5.marker_name = target_path('.template_2_retract.ges_sf_rod.MARKER_5')
        _template_2_retract_ges_sf_rod_PT3 = get_object('.template_2_retract.ges_sf_rod.PT3')
        MARKER_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ges_sf_rod_PT3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_5.location, MARKER_5.orientation)
        MARKER_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_sf_rod.MARKER_5', exc)

    try:
        gralin_25 = get_object('.template_2_retract.ges_sf_rod.gralin_25')
        relative_to = get_object('.template_2_retract.ges_sf_rod')
        gralin_25.relative_to = relative_to
        gralin_25.marker_name = target_path('.template_2_retract.ges_sf_rod.gralin_25')
        _template_2_retract_ground_hps_rod_bot = get_object('.template_2_retract.ground.hps_rod_bot')
        gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_ground_hps_rod_bot))
        _template_2_retract_ges_sf_rod_PT3 = get_object('.template_2_retract.ges_sf_rod.PT3').location
        _template_2_retract_ground_hps_db_sf_atch = get_object('.template_2_retract.ground.hps_db_sf_atch').location
        gralin_25.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_ges_sf_rod_PT3, _template_2_retract_ground_hps_db_sf_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_25.location, gralin_25.orientation)
        gralin_25.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_25.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract.ges_sf_rod.gralin_25', exc)

    try:
        CYLINDER_30 = get_object('.template_2_retract.ges_sf_rod.CYLINDER_30')
        CYLINDER_30.cylinder_name = target_path('.template_2_retract.ges_sf_rod.CYLINDER_30')
        _template_2_retract_ground_hps_rod_bot = get_object('.template_2_retract.ground.hps_rod_bot').location
        _template_2_retract_ground_hps_rod_top = get_object('.template_2_retract.ground.hps_rod_top').location
        CYLINDER_30.length = (VecUtils.DM(_template_2_retract_ground_hps_rod_bot, _template_2_retract_ground_hps_rod_top))
        CYLINDER_30.radius = 27.5


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract.ges_sf_rod.CYLINDER_30', exc)

    return {'updated': updated, 'warnings': warnings, 'errors': errors}

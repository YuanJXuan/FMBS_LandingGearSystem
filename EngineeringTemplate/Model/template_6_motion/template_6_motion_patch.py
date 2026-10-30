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

SOURCE_MODEL_NAME = 'template_6_motion'
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
        node = get_or_create('SimuScript', '.template_6_motion.Last_Sim')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_motion.Last_Sim')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=10.0 step_size=1.0E-02 model_name=.gcmb6_motion')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_motion.Last_Sim', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_motion.Last_Sim_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_motion.Last_Sim_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_motion.Last_Sim_2', exc)

    try:
        node = get_object('.template_6_motion.MOTION_disp')
        node.function = rewrite_expression('-STEP( time , 0 , 0 , .template_6_motion.NLG_RETRACT_TIME , .template_6_motion.NLG_ACTUATOR_STROKE )-STEP( time , .template_6_motion.NLG_RETRACT_TIME+.template_6_motion.NLG_UP_HOLD_TIME , 0 ,  .template_6_motion.NLG_RETRACT_TIME+.template_6_motion.NLG_UP_HOLD_TIME+.template_6_motion.NLG_EXTEND_TIME , -.template_6_motion.NLG_ACTUATOR_STROKE )')
        updated += 1

    except Exception as exc:
        record_error('constraint modify motion_generator .template_6_motion.MOTION_disp', exc)

    try:
        node = get_object('.template_6_motion.MOTION_LEFT')
        node.function = rewrite_expression('-STEP( time , 0 , 1 , .template_6_motion.MLG_RETRACT_TIME , .template_6_motion.MLG_ACTUATOR_STROKE )-STEP( time , .template_6_motion.MLG_RETRACT_TIME+.template_6_motion.MLG_UP_HOLD_TIME , 0 , .template_6_motion.MLG_RETRACT_TIME+.template_6_motion.MLG_UP_HOLD_TIME+.template_6_motion.MLG_EXTEND_TIME , -.template_6_motion.MLG_ACTUATOR_STROKE )')
        updated += 1

    except Exception as exc:
        record_error('constraint modify motion_generator .template_6_motion.MOTION_LEFT', exc)

    try:
        node = get_object('.template_6_motion.MOTION_RIGHT')
        node.function = rewrite_expression('-STEP( time , 0 , 1 , .template_6_motion.MLG_RETRACT_TIME , .template_6_motion.MLG_ACTUATOR_STROKE )-STEP( time , .template_6_motion.MLG_RETRACT_TIME+.template_6_motion.MLG_UP_HOLD_TIME , 0 , .template_6_motion.MLG_RETRACT_TIME+.template_6_motion.MLG_UP_HOLD_TIME+.template_6_motion.MLG_EXTEND_TIME , -.template_6_motion.MLG_ACTUATOR_STROKE )')
        updated += 1

    except Exception as exc:
        record_error('constraint modify motion_generator .template_6_motion.MOTION_RIGHT', exc)

    try:
        node = get_object('.template_6_motion.NLG_aeroforce')
        node.x_force_function = rewrite_expression('.template_6_motion.NLG_DRAG_COEFF*abs(IF( .template_6_motion.NLG_sf_angle-60 : COS( 1.225*.template_6_motion.NLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.NLG_sf_angle*pi/180 ) , COS( .template_6_motion.NLG_sf_angle*pi/180 ) ))*.template_6_motion.NLG_PROJ_AREA*cos(.template_6_motion.NLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*cos(.template_6_motion.NLG_sf_angle*pi/180) ')
        node.y_force_function = rewrite_expression('0')
        node.z_force_function = rewrite_expression('.template_6_motion.NLG_DRAG_COEFF*abs(IF( .template_6_motion.NLG_sf_angle-60 : COS( 1.225*.template_6_motion.NLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.NLG_sf_angle*pi/180 ) , COS( .template_6_motion.NLG_sf_angle*pi/180 ) ))*.template_6_motion.NLG_PROJ_AREA*cos(.template_6_motion.NLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*sin(.template_6_motion.NLG_sf_angle*pi/180) ')
        node.x_torque_function = rewrite_expression('0')
        node.y_torque_function = rewrite_expression('-1*CUBSPL( .template_6_motion.NLG_sf_angle, 0 , .template_6_motion.SPLINE_angle_aeroforce_NLG, 0 )')
        node.z_torque_function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('force modify direct general_force .template_6_motion.NLG_aeroforce', exc)

    try:
        node = get_object('.template_6_motion.aeroforce_MLG_L')
        node.x_force_function = rewrite_expression('.template_6_motion.MLG_DRAG_COEFF*abs(IF( .template_6_motion.MLG_sf_angle-60 : COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( .template_6_motion.MLG_sf_angle*pi/180 ) ))*.template_6_motion.MLG_PROJ_AREA*cos(.template_6_motion.MLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*cos(.template_6_motion.MLG_sf_angle*pi/180) ')
        node.y_force_function = rewrite_expression('0')
        node.z_force_function = rewrite_expression('.template_6_motion.MLG_DRAG_COEFF*abs(IF( .template_6_motion.MLG_sf_angle-60 : COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( .template_6_motion.MLG_sf_angle*pi/180 ) ))*.template_6_motion.MLG_PROJ_AREA*cos(.template_6_motion.MLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*sin(.template_6_motion.MLG_sf_angle*pi/180) ')
        node.x_torque_function = rewrite_expression('0')
        node.y_torque_function = rewrite_expression('-1*CUBSPL( .template_6_motion.MLG_sf_angle, 0 , .template_6_motion.SPLINE_angle_aeroforce_MLG, 0 )')
        node.z_torque_function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('force modify direct general_force .template_6_motion.aeroforce_MLG_L', exc)

    try:
        node = get_object('.template_6_motion.aeroforce_MLG_R')
        node.x_force_function = rewrite_expression('.template_6_motion.MLG_DRAG_COEFF*abs(IF( .template_6_motion.MLG_sf_angle-60 : COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( .template_6_motion.MLG_sf_angle*pi/180 ) ))*.template_6_motion.MLG_PROJ_AREA*cos(.template_6_motion.MLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*cos(.template_6_motion.MLG_sf_angle*pi/180) ')
        node.y_force_function = rewrite_expression('0')
        node.z_force_function = rewrite_expression('.template_6_motion.MLG_DRAG_COEFF*abs(IF( .template_6_motion.MLG_sf_angle-60 : COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( 1.225*.template_6_motion.MLG_sf_angle*pi/180 ) , COS( .template_6_motion.MLG_sf_angle*pi/180 ) ))*.template_6_motion.MLG_PROJ_AREA*cos(.template_6_motion.MLG_sf_angle*pi/180)*0.5*.template_6_motion.AIR_DENSITY*.template_6_motion.AIR_VELOCITY*abs(.template_6_motion.AIR_VELOCITY)*sin(.template_6_motion.MLG_sf_angle*pi/180) ')
        node.x_torque_function = rewrite_expression('0')
        node.y_torque_function = rewrite_expression('-1*CUBSPL( .template_6_motion.MLG_sf_angle, 0 , .template_6_motion.SPLINE_angle_aeroforce_MLG, 0 )')
        node.z_torque_function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('force modify direct general_force .template_6_motion.aeroforce_MLG_R', exc)

    try:
        mts_mount_j_2 = get_object('.template_6_motion.ground.mts_mount_j_2')
        mts_mount_j_2.marker_name = target_path('.template_6_motion.ground.mts_mount_j_2')
        _template_6_motion_mts_body_mount = get_object('.template_6_motion.mts_body_mount')
        mts_mount_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_mts_body_mount))
        _template_6_motion_mts_body_mount = get_object('.template_6_motion.mts_body_mount')
        mts_mount_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_mts_body_mount))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.mts_mount_j_2', exc)

    try:
        cfs_nlg_axle_lowpoint = get_object('.template_6_motion.ground.cfs_nlg_axle_lowpoint')
        cfs_nlg_axle_lowpoint.marker_name = target_path('.template_6_motion.ground.cfs_nlg_axle_lowpoint')
        _template_6_motion_ground_hps_nlg_axle_lowpoint = get_object('.template_6_motion.ground.hps_nlg_axle_lowpoint')
        cfs_nlg_axle_lowpoint.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_nlg_axle_lowpoint))
        _template_6_motion_ground_origo = get_object('.template_6_motion.ground.origo')
        cfs_nlg_axle_lowpoint.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfs_nlg_axle_lowpoint', exc)

    try:
        cfs_collar_top = get_object('.template_6_motion.ground.cfs_collar_top')
        cfs_collar_top.marker_name = target_path('.template_6_motion.ground.cfs_collar_top')
        _template_6_motion_ground_hps_uc_bot = get_object('.template_6_motion.ground.hps_uc_bot').location
        _template_6_motion_ground_hps_uc_top = get_object('.template_6_motion.ground.hps_uc_top').location
        cfs_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_6_motion_ground_hps_uc_bot, _template_6_motion_ground_hps_uc_top, 0.11 * VecUtils.DM(_template_6_motion_ground_hps_uc_bot, _template_6_motion_ground_hps_uc_top)))
        _template_6_motion_ground_hps_uc_bot = get_object('.template_6_motion.ground.hps_uc_bot').location
        _template_6_motion_ground_hps_uc_top = get_object('.template_6_motion.ground.hps_uc_top').location
        cfs_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_uc_bot, _template_6_motion_ground_hps_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfs_collar_top', exc)

    try:
        mts_mount_j_4 = get_object('.template_6_motion.ground.mts_mount_j_4')
        mts_mount_j_4.marker_name = target_path('.template_6_motion.ground.mts_mount_j_4')
        _template_6_motion_mts_body_mount_2 = get_object('.template_6_motion.mts_body_mount_2')
        mts_mount_j_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_mts_body_mount_2))
        _template_6_motion_mts_body_mount_2 = get_object('.template_6_motion.mts_body_mount_2')
        mts_mount_j_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_mts_body_mount_2))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.mts_mount_j_4', exc)

    try:
        cfl_axial_reference = get_object('.template_6_motion.ground.cfl_axial_reference')
        cfl_axial_reference.marker_name = target_path('.template_6_motion.ground.cfl_axial_reference')
        _template_6_motion_ground_hpl_lc_bot = get_object('.template_6_motion.ground.hpl_lc_bot')
        cfl_axial_reference.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_lc_bot))
        _template_6_motion_ground_hpl_lc_bot = get_object('.template_6_motion.ground.hpl_lc_bot').location
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top').location
        cfl_axial_reference.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_lc_bot, _template_6_motion_ground_hpl_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_axial_reference', exc)

    try:
        cfr_axial_reference = get_object('.template_6_motion.ground.cfr_axial_reference')
        cfr_axial_reference.marker_name = target_path('.template_6_motion.ground.cfr_axial_reference')
        _template_6_motion_ground_hpr_lc_bot = get_object('.template_6_motion.ground.hpr_lc_bot')
        cfr_axial_reference.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_lc_bot))
        _template_6_motion_ground_hpr_lc_bot = get_object('.template_6_motion.ground.hpr_lc_bot').location
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top').location
        cfr_axial_reference.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_lc_bot, _template_6_motion_ground_hpr_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_axial_reference', exc)

    try:
        cfl_uc_bot = get_object('.template_6_motion.ground.cfl_uc_bot')
        cfl_uc_bot.marker_name = target_path('.template_6_motion.ground.cfl_uc_bot')
        _template_6_motion_ground_cfl_axial_reference = get_object('.template_6_motion.ground.cfl_axial_reference')
        cfl_uc_bot.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 537.972], _template_6_motion_ground_cfl_axial_reference))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        cfl_uc_bot.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_uc_bot', exc)

    try:
        cfr_uc_bot = get_object('.template_6_motion.ground.cfr_uc_bot')
        cfr_uc_bot.marker_name = target_path('.template_6_motion.ground.cfr_uc_bot')
        _template_6_motion_ground_cfr_axial_reference = get_object('.template_6_motion.ground.cfr_axial_reference')
        cfr_uc_bot.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 537.972], _template_6_motion_ground_cfr_axial_reference))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        cfr_uc_bot.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_uc_bot', exc)

    try:
        cfl_uc_top = get_object('.template_6_motion.ground.cfl_uc_top')
        cfl_uc_top.marker_name = target_path('.template_6_motion.ground.cfl_uc_top')
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top')
        cfl_uc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_uc_top))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        cfl_uc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_uc_top', exc)

    try:
        cfr_uc_top = get_object('.template_6_motion.ground.cfr_uc_top')
        cfr_uc_top.marker_name = target_path('.template_6_motion.ground.cfr_uc_top')
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top')
        cfr_uc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_uc_top))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        cfr_uc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_uc_top', exc)

    try:
        cfl_lc_top = get_object('.template_6_motion.ground.cfl_lc_top')
        cfl_lc_top.marker_name = target_path('.template_6_motion.ground.cfl_lc_top')
        _template_6_motion_ground_cfl_axial_reference = get_object('.template_6_motion.ground.cfl_axial_reference')
        cfl_lc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 966.724], _template_6_motion_ground_cfl_axial_reference))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        cfl_lc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_lc_top', exc)

    try:
        cfr_lc_top = get_object('.template_6_motion.ground.cfr_lc_top')
        cfr_lc_top.marker_name = target_path('.template_6_motion.ground.cfr_lc_top')
        _template_6_motion_ground_cfr_axial_reference = get_object('.template_6_motion.ground.cfr_axial_reference')
        cfr_lc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 966.724], _template_6_motion_ground_cfr_axial_reference))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        cfr_lc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_lc_top', exc)

    try:
        cfl_collar_top = get_object('.template_6_motion.ground.cfl_collar_top')
        cfl_collar_top.marker_name = target_path('.template_6_motion.ground.cfl_collar_top')
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top').location
        _template_6_motion_ground_hpl_lc_bot = get_object('.template_6_motion.ground.hpl_lc_bot').location
        cfl_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_6_motion_ground_hpl_uc_top, _template_6_motion_ground_hpl_lc_bot, 0.59 * VecUtils.DM(_template_6_motion_ground_hpl_uc_top, _template_6_motion_ground_hpl_lc_bot)))
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top').location
        _template_6_motion_ground_hpl_lc_bot = get_object('.template_6_motion.ground.hpl_lc_bot').location
        cfl_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_uc_top, _template_6_motion_ground_hpl_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_collar_top', exc)

    try:
        cfr_collar_top = get_object('.template_6_motion.ground.cfr_collar_top')
        cfr_collar_top.marker_name = target_path('.template_6_motion.ground.cfr_collar_top')
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top').location
        _template_6_motion_ground_hpr_lc_bot = get_object('.template_6_motion.ground.hpr_lc_bot').location
        cfr_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_6_motion_ground_hpr_uc_top, _template_6_motion_ground_hpr_lc_bot, 0.59 * VecUtils.DM(_template_6_motion_ground_hpr_uc_top, _template_6_motion_ground_hpr_lc_bot)))
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top').location
        _template_6_motion_ground_hpr_lc_bot = get_object('.template_6_motion.ground.hpr_lc_bot').location
        cfr_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_uc_top, _template_6_motion_ground_hpr_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_collar_top', exc)

    try:
        cfl_collar_bot = get_object('.template_6_motion.ground.cfl_collar_bot')
        cfl_collar_bot.marker_name = target_path('.template_6_motion.ground.cfl_collar_bot')
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top').location
        _template_6_motion_ground_hpl_lc_bot = get_object('.template_6_motion.ground.hpl_lc_bot').location
        cfl_collar_bot.location = (VecUtils.LOC_ALONG_LINE(_template_6_motion_ground_hpl_uc_top, _template_6_motion_ground_hpl_lc_bot, 0.7 * VecUtils.DM(_template_6_motion_ground_hpl_uc_top, _template_6_motion_ground_hpl_lc_bot)))
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top').location
        _template_6_motion_ground_hpl_lc_bot = get_object('.template_6_motion.ground.hpl_lc_bot').location
        cfl_collar_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_uc_top, _template_6_motion_ground_hpl_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_collar_bot', exc)

    try:
        cfr_collar_bot = get_object('.template_6_motion.ground.cfr_collar_bot')
        cfr_collar_bot.marker_name = target_path('.template_6_motion.ground.cfr_collar_bot')
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top').location
        _template_6_motion_ground_hpr_lc_bot = get_object('.template_6_motion.ground.hpr_lc_bot').location
        cfr_collar_bot.location = (VecUtils.LOC_ALONG_LINE(_template_6_motion_ground_hpr_uc_top, _template_6_motion_ground_hpr_lc_bot, 0.7 * VecUtils.DM(_template_6_motion_ground_hpr_uc_top, _template_6_motion_ground_hpr_lc_bot)))
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top').location
        _template_6_motion_ground_hpr_lc_bot = get_object('.template_6_motion.ground.hpr_lc_bot').location
        cfr_collar_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_uc_top, _template_6_motion_ground_hpr_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_collar_bot', exc)

    try:
        cfl_plane_ref_2 = get_object('.template_6_motion.ground.cfl_plane_ref_2')
        cfl_plane_ref_2.marker_name = target_path('.template_6_motion.ground.cfl_plane_ref_2')
        _template_6_motion_ground_cfl_plane_ref = get_object('.template_6_motion.ground.cfl_plane_ref')
        cfl_plane_ref_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfl_plane_ref))
        _template_6_motion_ground_cfl_plane_ref = get_object('.template_6_motion.ground.cfl_plane_ref')
        cfl_plane_ref_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, -90.0, 0.0], _template_6_motion_ground_cfl_plane_ref))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_plane_ref_2', exc)

    try:
        cfr_plane_ref_2 = get_object('.template_6_motion.ground.cfr_plane_ref_2')
        cfr_plane_ref_2.marker_name = target_path('.template_6_motion.ground.cfr_plane_ref_2')
        _template_6_motion_ground_cfr_plane_ref = get_object('.template_6_motion.ground.cfr_plane_ref')
        cfr_plane_ref_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfr_plane_ref))
        _template_6_motion_ground_cfr_plane_ref = get_object('.template_6_motion.ground.cfr_plane_ref')
        cfr_plane_ref_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_6_motion_ground_cfr_plane_ref))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_plane_ref_2', exc)

    try:
        cfl_lwract_top = get_object('.template_6_motion.ground.cfl_lwract_top')
        cfl_lwract_top.marker_name = target_path('.template_6_motion.ground.cfl_lwract_top')
        _template_6_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpl_lwract_uc_atch_1').location
        _template_6_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpl_upract_sf_atch_1').location
        cfl_lwract_top.location = (VecUtils.LOC_ALONG_LINE(_template_6_motion_ground_hpl_lwract_uc_atch_1, _template_6_motion_ground_hpl_upract_sf_atch_1, 0.92 * VecUtils.DM(_template_6_motion_ground_hpl_lwract_uc_atch_1, _template_6_motion_ground_hpl_upract_sf_atch_1)))
        _template_6_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpl_lwract_uc_atch_1').location
        _template_6_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpl_upract_sf_atch_1').location
        cfl_lwract_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_lwract_uc_atch_1, _template_6_motion_ground_hpl_upract_sf_atch_1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_lwract_top', exc)

    try:
        cfr_lwract_top = get_object('.template_6_motion.ground.cfr_lwract_top')
        cfr_lwract_top.marker_name = target_path('.template_6_motion.ground.cfr_lwract_top')
        _template_6_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpr_lwract_uc_atch_1').location
        _template_6_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpr_upract_sf_atch_1').location
        cfr_lwract_top.location = (VecUtils.LOC_ALONG_LINE(_template_6_motion_ground_hpr_lwract_uc_atch_1, _template_6_motion_ground_hpr_upract_sf_atch_1, 0.92 * VecUtils.DM(_template_6_motion_ground_hpr_lwract_uc_atch_1, _template_6_motion_ground_hpr_upract_sf_atch_1)))
        _template_6_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpr_lwract_uc_atch_1').location
        _template_6_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpr_upract_sf_atch_1').location
        cfr_lwract_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_lwract_uc_atch_1, _template_6_motion_ground_hpr_upract_sf_atch_1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_lwract_top', exc)

    try:
        cfl_upract_bot = get_object('.template_6_motion.ground.cfl_upract_bot')
        cfl_upract_bot.marker_name = target_path('.template_6_motion.ground.cfl_upract_bot')
        _template_6_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpl_lwract_uc_atch_1').location
        _template_6_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpl_upract_sf_atch_1').location
        cfl_upract_bot.location = (VecUtils.LOC_ALONG_LINE(_template_6_motion_ground_hpl_lwract_uc_atch_1, _template_6_motion_ground_hpl_upract_sf_atch_1, 0.4 * VecUtils.DM(_template_6_motion_ground_hpl_lwract_uc_atch_1, _template_6_motion_ground_hpl_upract_sf_atch_1)))
        _template_6_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpl_lwract_uc_atch_1').location
        _template_6_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpl_upract_sf_atch_1').location
        cfl_upract_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_lwract_uc_atch_1, _template_6_motion_ground_hpl_upract_sf_atch_1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_upract_bot', exc)

    try:
        cfr_upract_bot = get_object('.template_6_motion.ground.cfr_upract_bot')
        cfr_upract_bot.marker_name = target_path('.template_6_motion.ground.cfr_upract_bot')
        _template_6_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpr_lwract_uc_atch_1').location
        _template_6_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpr_upract_sf_atch_1').location
        cfr_upract_bot.location = (VecUtils.LOC_ALONG_LINE(_template_6_motion_ground_hpr_lwract_uc_atch_1, _template_6_motion_ground_hpr_upract_sf_atch_1, 0.4 * VecUtils.DM(_template_6_motion_ground_hpr_lwract_uc_atch_1, _template_6_motion_ground_hpr_upract_sf_atch_1)))
        _template_6_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpr_lwract_uc_atch_1').location
        _template_6_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpr_upract_sf_atch_1').location
        cfr_upract_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_lwract_uc_atch_1, _template_6_motion_ground_hpr_upract_sf_atch_1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_upract_bot', exc)

    try:
        cfl_spin_axis_1 = get_object('.template_6_motion.ground.cfl_spin_axis_1')
        cfl_spin_axis_1.marker_name = target_path('.template_6_motion.ground.cfl_spin_axis_1')
        _template_6_motion_ground_hpl_wheel_center1 = get_object('.template_6_motion.ground.hpl_wheel_center1')
        cfl_spin_axis_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_wheel_center1))
        _template_6_motion_ground_hpl_wheel_center1 = get_object('.template_6_motion.ground.hpl_wheel_center1').location
        _template_6_motion_ground_hpl_ob_axle1 = get_object('.template_6_motion.ground.hpl_ob_axle1').location
        cfl_spin_axis_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_wheel_center1, _template_6_motion_ground_hpl_ob_axle1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfl_spin_axis_1', exc)

    try:
        cfr_spin_axis_1 = get_object('.template_6_motion.ground.cfr_spin_axis_1')
        cfr_spin_axis_1.marker_name = target_path('.template_6_motion.ground.cfr_spin_axis_1')
        _template_6_motion_ground_hpr_wheel_center1 = get_object('.template_6_motion.ground.hpr_wheel_center1')
        cfr_spin_axis_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_wheel_center1))
        _template_6_motion_ground_hpr_wheel_center1 = get_object('.template_6_motion.ground.hpr_wheel_center1').location
        _template_6_motion_ground_hpr_ob_axle1 = get_object('.template_6_motion.ground.hpr_ob_axle1').location
        cfr_spin_axis_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_wheel_center1, _template_6_motion_ground_hpr_ob_axle1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ground.cfr_spin_axis_1', exc)

    try:
        gralin_1 = get_object('.template_6_motion.ges_sf_actuator.gralin_1')
        relative_to = get_object('.template_6_motion.ges_sf_actuator')
        gralin_1.relative_to = relative_to
        gralin_1.marker_name = target_path('.template_6_motion.ges_sf_actuator.gralin_1')
        _template_6_motion_ground_hps_db_sf_atch = get_object('.template_6_motion.ground.hps_db_sf_atch')
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_db_sf_atch))
        _template_6_motion_ground_hps_db_sf_atch = get_object('.template_6_motion.ground.hps_db_sf_atch').location
        _template_6_motion_ground_hps_db_uc_atch = get_object('.template_6_motion.ground.hps_db_uc_atch').location
        gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_db_sf_atch, _template_6_motion_ground_hps_db_uc_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_sf_actuator.gralin_1', exc)

    try:
        jxs_joint_i_14 = get_object('.template_6_motion.ges_sf_actuator.jxs_joint_i_14')
        relative_to = get_object('.template_6_motion.ges_sf_actuator')
        jxs_joint_i_14.relative_to = relative_to
        jxs_joint_i_14.marker_name = target_path('.template_6_motion.ges_sf_actuator.jxs_joint_i_14')
        _template_6_motion_ges_subframe_jxs_joint_j_14 = get_object('.template_6_motion.ges_subframe.jxs_joint_j_14')
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_jxs_joint_j_14))
        _template_6_motion_ges_subframe_jxs_joint_j_14 = get_object('.template_6_motion.ges_subframe.jxs_joint_j_14')
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_jxs_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_sf_actuator.jxs_joint_i_14', exc)

    try:
        gralin_dragbrace_geom = get_object('.template_6_motion.ges_sf_actuator.gralin_dragbrace_geom')
        gralin_dragbrace_geom.cylinder_name = target_path('.template_6_motion.ges_sf_actuator.gralin_dragbrace_geom')
        _template_6_motion_ground_hps_db_sf_atch = get_object('.template_6_motion.ground.hps_db_sf_atch').location
        _template_6_motion_ground_hps_db_uc_atch = get_object('.template_6_motion.ground.hps_db_uc_atch').location
        gralin_dragbrace_geom.length = (VecUtils.DM(_template_6_motion_ground_hps_db_sf_atch, _template_6_motion_ground_hps_db_uc_atch) - 50.0)


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_sf_actuator.gralin_dragbrace_geom', exc)

    try:
        MARKER_4 = get_object('.template_6_motion.ges_upper_cylinder.MARKER_4')
        relative_to = get_object('.template_6_motion.ges_upper_cylinder')
        MARKER_4.relative_to = relative_to
        MARKER_4.marker_name = target_path('.template_6_motion.ges_upper_cylinder.MARKER_4')
        _template_6_motion_ges_sf_rod_PT3 = get_object('.template_6_motion.ges_sf_rod.PT3')
        MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_sf_rod_PT3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_4.location, MARKER_4.orientation)
        MARKER_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_upper_cylinder.MARKER_4', exc)

    try:
        gralin_2 = get_object('.template_6_motion.ges_upper_cylinder.gralin_2')
        relative_to = get_object('.template_6_motion.ges_upper_cylinder')
        gralin_2.relative_to = relative_to
        gralin_2.marker_name = target_path('.template_6_motion.ges_upper_cylinder.gralin_2')
        _template_6_motion_ground_hps_uc_top = get_object('.template_6_motion.ground.hps_uc_top')
        gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_uc_top))
        _template_6_motion_ground_hps_uc_top = get_object('.template_6_motion.ground.hps_uc_top').location
        _template_6_motion_ground_hps_uc_bot = get_object('.template_6_motion.ground.hps_uc_bot').location
        gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_uc_top, _template_6_motion_ground_hps_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_2.location, gralin_2.orientation)
        gralin_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_upper_cylinder.gralin_2', exc)

    try:
        gralin_3 = get_object('.template_6_motion.ges_upper_cylinder.gralin_3')
        relative_to = get_object('.template_6_motion.ges_upper_cylinder')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_6_motion.ges_upper_cylinder.gralin_3')
        _template_6_motion_ground_hps_uc_sf_atch_l = get_object('.template_6_motion.ground.hps_uc_sf_atch_l')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_uc_sf_atch_l))
        _template_6_motion_ground_hps_uc_sf_atch_l = get_object('.template_6_motion.ground.hps_uc_sf_atch_l').location
        _template_6_motion_ground_hps_uc_geompt = get_object('.template_6_motion.ground.hps_uc_geompt').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_uc_sf_atch_l, _template_6_motion_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_upper_cylinder.gralin_3', exc)

    try:
        gralin_4 = get_object('.template_6_motion.ges_upper_cylinder.gralin_4')
        relative_to = get_object('.template_6_motion.ges_upper_cylinder')
        gralin_4.relative_to = relative_to
        gralin_4.marker_name = target_path('.template_6_motion.ges_upper_cylinder.gralin_4')
        _template_6_motion_ground_hps_uc_sf_atch_r = get_object('.template_6_motion.ground.hps_uc_sf_atch_r')
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_uc_sf_atch_r))
        _template_6_motion_ground_hps_uc_sf_atch_r = get_object('.template_6_motion.ground.hps_uc_sf_atch_r').location
        _template_6_motion_ground_hps_uc_geompt = get_object('.template_6_motion.ground.hps_uc_geompt').location
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_uc_sf_atch_r, _template_6_motion_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_upper_cylinder.gralin_4', exc)

    try:
        jxs_joint_i_15 = get_object('.template_6_motion.ges_upper_cylinder.jxs_joint_i_15')
        relative_to = get_object('.template_6_motion.ges_upper_cylinder')
        jxs_joint_i_15.relative_to = relative_to
        jxs_joint_i_15.marker_name = target_path('.template_6_motion.ges_upper_cylinder.jxs_joint_i_15')
        _template_6_motion_ges_subframe_jxs_joint_j_15 = get_object('.template_6_motion.ges_subframe.jxs_joint_j_15')
        jxs_joint_i_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_jxs_joint_j_15))
        _template_6_motion_ges_subframe_jxs_joint_j_15 = get_object('.template_6_motion.ges_subframe.jxs_joint_j_15')
        jxs_joint_i_15.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_jxs_joint_j_15))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_15.location, jxs_joint_i_15.orientation)
        jxs_joint_i_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_upper_cylinder.jxs_joint_i_15', exc)

    try:
        jxs_joint_j_1 = get_object('.template_6_motion.ges_upper_cylinder.jxs_joint_j_1')
        relative_to = get_object('.template_6_motion.ges_upper_cylinder')
        jxs_joint_j_1.relative_to = relative_to
        jxs_joint_j_1.marker_name = target_path('.template_6_motion.ges_upper_cylinder.jxs_joint_j_1')
        _template_6_motion_ground_cfs_collar_top = get_object('.template_6_motion.ground.cfs_collar_top')
        jxs_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfs_collar_top))
        _template_6_motion_ground_hps_uc_bot = get_object('.template_6_motion.ground.hps_uc_bot').location
        _template_6_motion_ground_hps_uc_top = get_object('.template_6_motion.ground.hps_uc_top').location
        jxs_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_uc_bot, _template_6_motion_ground_hps_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
        jxs_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_upper_cylinder.jxs_joint_j_1', exc)

    try:
        gralin_upper_cylinder_geom1 = get_object('.template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        gralin_upper_cylinder_geom1.cylinder_name = target_path('.template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        _template_6_motion_ground_hps_uc_top = get_object('.template_6_motion.ground.hps_uc_top').location
        _template_6_motion_ground_hps_uc_bot = get_object('.template_6_motion.ground.hps_uc_bot').location
        gralin_upper_cylinder_geom1.length = (VecUtils.DM(_template_6_motion_ground_hps_uc_top, _template_6_motion_ground_hps_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom1', exc)

    try:
        gralin_upper_cylinder_geom2 = get_object('.template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        gralin_upper_cylinder_geom2.cylinder_name = target_path('.template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        _template_6_motion_ground_hps_uc_sf_atch_l = get_object('.template_6_motion.ground.hps_uc_sf_atch_l').location
        _template_6_motion_ground_hps_uc_geompt = get_object('.template_6_motion.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom2.length = (VecUtils.DM(_template_6_motion_ground_hps_uc_sf_atch_l, _template_6_motion_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom2', exc)

    try:
        gralin_upper_cylinder_geom3 = get_object('.template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        gralin_upper_cylinder_geom3.cylinder_name = target_path('.template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        _template_6_motion_ground_hps_uc_sf_atch_r = get_object('.template_6_motion.ground.hps_uc_sf_atch_r').location
        _template_6_motion_ground_hps_uc_geompt = get_object('.template_6_motion.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom3.length = (VecUtils.DM(_template_6_motion_ground_hps_uc_sf_atch_r, _template_6_motion_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_upper_cylinder.gralin_upper_cylinder_geom3', exc)

    try:
        gralin_5 = get_object('.template_6_motion.ges_lower_cylinder.gralin_5')
        relative_to = get_object('.template_6_motion.ges_lower_cylinder')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_6_motion.ges_lower_cylinder.gralin_5')
        _template_6_motion_ground_hps_lc_top = get_object('.template_6_motion.ground.hps_lc_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_lc_top))
        _template_6_motion_ground_hps_lc_top = get_object('.template_6_motion.ground.hps_lc_top').location
        _template_6_motion_ground_hps_lc_bot = get_object('.template_6_motion.ground.hps_lc_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_lc_top, _template_6_motion_ground_hps_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_lower_cylinder.gralin_5', exc)

    try:
        jxs_joint_j_9 = get_object('.template_6_motion.ges_lower_cylinder.jxs_joint_j_9')
        relative_to = get_object('.template_6_motion.ges_lower_cylinder')
        jxs_joint_j_9.relative_to = relative_to
        jxs_joint_j_9.marker_name = target_path('.template_6_motion.ges_lower_cylinder.jxs_joint_j_9')
        _template_6_motion_ground_hps_lta_lc_atch = get_object('.template_6_motion.ground.hps_lta_lc_atch')
        jxs_joint_j_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_lta_lc_atch))
        _template_6_motion_ground_origo = get_object('.template_6_motion.ground.origo')
        jxs_joint_j_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_9.location, jxs_joint_j_9.orientation)
        jxs_joint_j_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_lower_cylinder.jxs_joint_j_9', exc)

    try:
        jxs_joint_i_11 = get_object('.template_6_motion.ges_lower_cylinder.jxs_joint_i_11')
        relative_to = get_object('.template_6_motion.ges_lower_cylinder')
        jxs_joint_i_11.relative_to = relative_to
        jxs_joint_i_11.marker_name = target_path('.template_6_motion.ges_lower_cylinder.jxs_joint_i_11')
        _template_6_motion_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_6_motion.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_upper_cylinder_jxs_joint_j_11))
        _template_6_motion_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_6_motion.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_upper_cylinder_jxs_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
        jxs_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_lower_cylinder.jxs_joint_i_11', exc)

    try:
        gralin_7 = get_object('.template_6_motion.ges_lower_cylinder.gralin_7')
        relative_to = get_object('.template_6_motion.ges_lower_cylinder')
        gralin_7.relative_to = relative_to
        gralin_7.marker_name = target_path('.template_6_motion.ges_lower_cylinder.gralin_7')
        _template_6_motion_ground_hpr_wheel_center = get_object('.template_6_motion.ground.hpr_wheel_center')
        gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_wheel_center))
        _template_6_motion_ground_hpr_wheel_center = get_object('.template_6_motion.ground.hpr_wheel_center').location
        _template_6_motion_ground_hpl_wheel_center = get_object('.template_6_motion.ground.hpl_wheel_center').location
        gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_wheel_center, _template_6_motion_ground_hpl_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_lower_cylinder.gralin_7', exc)

    try:
        MARKER_350 = get_object('.template_6_motion.ges_lower_cylinder.MARKER_350')
        relative_to = get_object('.template_6_motion.ges_lower_cylinder')
        MARKER_350.relative_to = relative_to
        MARKER_350.marker_name = target_path('.template_6_motion.ges_lower_cylinder.MARKER_350')
        _template_6_motion_ground_hpl_ob_axle = get_object('.template_6_motion.ground.hpl_ob_axle')
        MARKER_350.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_ob_axle))
        _template_6_motion_ground_hpl_ob_axle = get_object('.template_6_motion.ground.hpl_ob_axle').location
        _template_6_motion_ground_hpl_wheel_center = get_object('.template_6_motion.ground.hpl_wheel_center').location
        MARKER_350.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_ob_axle, _template_6_motion_ground_hpl_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_350.location, MARKER_350.orientation)
        MARKER_350.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_350.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_lower_cylinder.MARKER_350', exc)

    try:
        MARKER_351 = get_object('.template_6_motion.ges_lower_cylinder.MARKER_351')
        relative_to = get_object('.template_6_motion.ges_lower_cylinder')
        MARKER_351.relative_to = relative_to
        MARKER_351.marker_name = target_path('.template_6_motion.ges_lower_cylinder.MARKER_351')
        _template_6_motion_ground_hpr_ob_axle = get_object('.template_6_motion.ground.hpr_ob_axle')
        MARKER_351.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_ob_axle))
        _template_6_motion_ground_hpr_ob_axle = get_object('.template_6_motion.ground.hpr_ob_axle').location
        _template_6_motion_ground_hpr_wheel_center = get_object('.template_6_motion.ground.hpr_wheel_center').location
        MARKER_351.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_ob_axle, _template_6_motion_ground_hpr_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_351.location, MARKER_351.orientation)
        MARKER_351.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_351.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_lower_cylinder.MARKER_351', exc)

    try:
        gralin_geom1 = get_object('.template_6_motion.ges_lower_cylinder.gralin_geom1')
        gralin_geom1.cylinder_name = target_path('.template_6_motion.ges_lower_cylinder.gralin_geom1')
        _template_6_motion_ground_hps_lc_top = get_object('.template_6_motion.ground.hps_lc_top').location
        _template_6_motion_ground_hps_lc_bot = get_object('.template_6_motion.ground.hps_lc_bot').location
        gralin_geom1.length = (VecUtils.DM(_template_6_motion_ground_hps_lc_top, _template_6_motion_ground_hps_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_lower_cylinder.gralin_geom1', exc)

    try:
        gralin_geom2 = get_object('.template_6_motion.ges_lower_cylinder.gralin_geom2')
        gralin_geom2.cylinder_name = target_path('.template_6_motion.ges_lower_cylinder.gralin_geom2')
        _template_6_motion_ground_hpr_wheel_center = get_object('.template_6_motion.ground.hpr_wheel_center').location
        _template_6_motion_ground_hpl_wheel_center = get_object('.template_6_motion.ground.hpl_wheel_center').location
        gralin_geom2.length = (VecUtils.DM(_template_6_motion_ground_hpr_wheel_center, _template_6_motion_ground_hpl_wheel_center))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_lower_cylinder.gralin_geom2', exc)

    try:
        gralin_9 = get_object('.template_6_motion.ges_upper_torque_arm.gralin_9')
        relative_to = get_object('.template_6_motion.ges_upper_torque_arm')
        gralin_9.relative_to = relative_to
        gralin_9.marker_name = target_path('.template_6_motion.ges_upper_torque_arm.gralin_9')
        _template_6_motion_ground_hps_uta_uc_atch = get_object('.template_6_motion.ground.hps_uta_uc_atch')
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_uta_uc_atch))
        _template_6_motion_ground_hps_uta_uc_atch = get_object('.template_6_motion.ground.hps_uta_uc_atch').location
        _template_6_motion_ground_hps_lta_uta_atch = get_object('.template_6_motion.ground.hps_lta_uta_atch').location
        gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_uta_uc_atch, _template_6_motion_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_upper_torque_arm.gralin_9', exc)

    try:
        jxs_joint_j_8 = get_object('.template_6_motion.ges_upper_torque_arm.jxs_joint_j_8')
        relative_to = get_object('.template_6_motion.ges_upper_torque_arm')
        jxs_joint_j_8.relative_to = relative_to
        jxs_joint_j_8.marker_name = target_path('.template_6_motion.ges_upper_torque_arm.jxs_joint_j_8')
        _template_6_motion_ground_hps_lta_uta_atch = get_object('.template_6_motion.ground.hps_lta_uta_atch')
        jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_lta_uta_atch))
        _template_6_motion_ground_origo = get_object('.template_6_motion.ground.origo')
        jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_6_motion_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
        jxs_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_upper_torque_arm.jxs_joint_j_8', exc)

    try:
        jxs_joint_i_10 = get_object('.template_6_motion.ges_upper_torque_arm.jxs_joint_i_10')
        relative_to = get_object('.template_6_motion.ges_upper_torque_arm')
        jxs_joint_i_10.relative_to = relative_to
        jxs_joint_i_10.marker_name = target_path('.template_6_motion.ges_upper_torque_arm.jxs_joint_i_10')
        _template_6_motion_ges_collar_jxs_joint_j_10 = get_object('.template_6_motion.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_collar_jxs_joint_j_10))
        _template_6_motion_ges_collar_jxs_joint_j_10 = get_object('.template_6_motion.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_collar_jxs_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
        jxs_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_upper_torque_arm.jxs_joint_i_10', exc)

    try:
        gralin_upper_torque_arm_geom = get_object('.template_6_motion.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        gralin_upper_torque_arm_geom.cylinder_name = target_path('.template_6_motion.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        _template_6_motion_ground_hps_uta_uc_atch = get_object('.template_6_motion.ground.hps_uta_uc_atch').location
        _template_6_motion_ground_hps_lta_uta_atch = get_object('.template_6_motion.ground.hps_lta_uta_atch').location
        gralin_upper_torque_arm_geom.length = (VecUtils.DM(_template_6_motion_ground_hps_uta_uc_atch, _template_6_motion_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_upper_torque_arm.gralin_upper_torque_arm_geom', exc)

    try:
        jxs_joint_i_8 = get_object('.template_6_motion.ges_lower_torque_arm.jxs_joint_i_8')
        relative_to = get_object('.template_6_motion.ges_lower_torque_arm')
        jxs_joint_i_8.relative_to = relative_to
        jxs_joint_i_8.marker_name = target_path('.template_6_motion.ges_lower_torque_arm.jxs_joint_i_8')
        _template_6_motion_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_6_motion.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_upper_torque_arm_jxs_joint_j_8))
        _template_6_motion_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_6_motion.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_upper_torque_arm_jxs_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
        jxs_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_lower_torque_arm.jxs_joint_i_8', exc)

    try:
        gralin_10 = get_object('.template_6_motion.ges_lower_torque_arm.gralin_10')
        relative_to = get_object('.template_6_motion.ges_lower_torque_arm')
        gralin_10.relative_to = relative_to
        gralin_10.marker_name = target_path('.template_6_motion.ges_lower_torque_arm.gralin_10')
        _template_6_motion_ground_hps_lta_lc_atch = get_object('.template_6_motion.ground.hps_lta_lc_atch')
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_lta_lc_atch))
        _template_6_motion_ground_hps_lta_lc_atch = get_object('.template_6_motion.ground.hps_lta_lc_atch').location
        _template_6_motion_ground_hps_lta_uta_atch = get_object('.template_6_motion.ground.hps_lta_uta_atch').location
        gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_lta_lc_atch, _template_6_motion_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_lower_torque_arm.gralin_10', exc)

    try:
        jxs_joint_i_9 = get_object('.template_6_motion.ges_lower_torque_arm.jxs_joint_i_9')
        relative_to = get_object('.template_6_motion.ges_lower_torque_arm')
        jxs_joint_i_9.relative_to = relative_to
        jxs_joint_i_9.marker_name = target_path('.template_6_motion.ges_lower_torque_arm.jxs_joint_i_9')
        _template_6_motion_ges_lower_cylinder_jxs_joint_j_9 = get_object('.template_6_motion.ges_lower_cylinder.jxs_joint_j_9')
        jxs_joint_i_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_lower_cylinder_jxs_joint_j_9))
        _template_6_motion_ges_lower_cylinder_jxs_joint_j_9 = get_object('.template_6_motion.ges_lower_cylinder.jxs_joint_j_9')
        jxs_joint_i_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_lower_cylinder_jxs_joint_j_9))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_9.location, jxs_joint_i_9.orientation)
        jxs_joint_i_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_lower_torque_arm.jxs_joint_i_9', exc)

    try:
        gralin_lower_torque_arm_geom = get_object('.template_6_motion.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        gralin_lower_torque_arm_geom.cylinder_name = target_path('.template_6_motion.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        _template_6_motion_ground_hps_lta_lc_atch = get_object('.template_6_motion.ground.hps_lta_lc_atch').location
        _template_6_motion_ground_hps_lta_uta_atch = get_object('.template_6_motion.ground.hps_lta_uta_atch').location
        gralin_lower_torque_arm_geom.length = (VecUtils.DM(_template_6_motion_ground_hps_lta_lc_atch, _template_6_motion_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_lower_torque_arm.gralin_lower_torque_arm_geom', exc)

    try:
        inertia_frame = get_object('.template_6_motion.ges_subframe.inertia_frame')
        relative_to = get_object('.template_6_motion.ges_subframe')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_6_motion.ges_subframe.inertia_frame')
        _template_6_motion_ges_subframe_cm = get_object('.template_6_motion.ges_subframe.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_cm))
        _template_6_motion_ges_subframe = get_object('.template_6_motion.ges_subframe')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe.inertia_frame', exc)

    try:
        graout_1 = get_object('.template_6_motion.ges_subframe.graout_1')
        relative_to = get_object('.template_6_motion.ges_subframe')
        graout_1.relative_to = relative_to
        graout_1.marker_name = target_path('.template_6_motion.ges_subframe.graout_1')
        _template_6_motion_ground_hps_uc_sf_atch_r = get_object('.template_6_motion.ground.hps_uc_sf_atch_r')
        graout_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_uc_sf_atch_r))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_1.location, graout_1.orientation)
        graout_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe.graout_1', exc)

    try:
        graout_2 = get_object('.template_6_motion.ges_subframe.graout_2')
        relative_to = get_object('.template_6_motion.ges_subframe')
        graout_2.relative_to = relative_to
        graout_2.marker_name = target_path('.template_6_motion.ges_subframe.graout_2')
        _template_6_motion_ground_hps_uc_sf_atch_l = get_object('.template_6_motion.ground.hps_uc_sf_atch_l')
        graout_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_uc_sf_atch_l))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_2.location, graout_2.orientation)
        graout_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe.graout_2', exc)

    try:
        graout_3 = get_object('.template_6_motion.ges_subframe.graout_3')
        relative_to = get_object('.template_6_motion.ges_subframe')
        graout_3.relative_to = relative_to
        graout_3.marker_name = target_path('.template_6_motion.ges_subframe.graout_3')
        _template_6_motion_ground_hps_db_sf_atch = get_object('.template_6_motion.ground.hps_db_sf_atch')
        graout_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_db_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_3.location, graout_3.orientation)
        graout_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe.graout_3', exc)

    try:
        jxs_joint_j_15 = get_object('.template_6_motion.ges_subframe.jxs_joint_j_15')
        relative_to = get_object('.template_6_motion.ges_subframe')
        jxs_joint_j_15.relative_to = relative_to
        jxs_joint_j_15.marker_name = target_path('.template_6_motion.ges_subframe.jxs_joint_j_15')
        _template_6_motion_ground_cfs_uc_sf_atch_mid = get_object('.template_6_motion.ground.cfs_uc_sf_atch_mid')
        jxs_joint_j_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfs_uc_sf_atch_mid))
        _template_6_motion_ground_cfs_uc_sf_atch_mid = get_object('.template_6_motion.ground.cfs_uc_sf_atch_mid')
        jxs_joint_j_15.orientation = _template_6_motion_ground_cfs_uc_sf_atch_mid.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_15.location, jxs_joint_j_15.orientation)
        jxs_joint_j_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe.jxs_joint_j_15', exc)

    try:
        jxs_joint_i_16 = get_object('.template_6_motion.ges_subframe.jxs_joint_i_16')
        relative_to = get_object('.template_6_motion.ges_subframe')
        jxs_joint_i_16.relative_to = relative_to
        jxs_joint_i_16.marker_name = target_path('.template_6_motion.ges_subframe.jxs_joint_i_16')
        _template_6_motion_mts_body_mount_jxs_joint_j_16 = get_object('.template_6_motion.mts_body_mount.jxs_joint_j_16')
        jxs_joint_i_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_mts_body_mount_jxs_joint_j_16))
        _template_6_motion_mts_body_mount_jxs_joint_j_16 = get_object('.template_6_motion.mts_body_mount.jxs_joint_j_16')
        jxs_joint_i_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_mts_body_mount_jxs_joint_j_16))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_16.location, jxs_joint_i_16.orientation)
        jxs_joint_i_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe.jxs_joint_i_16', exc)

    try:
        jxs_joint_j_14 = get_object('.template_6_motion.ges_subframe.jxs_joint_j_14')
        relative_to = get_object('.template_6_motion.ges_subframe')
        jxs_joint_j_14.relative_to = relative_to
        jxs_joint_j_14.marker_name = target_path('.template_6_motion.ges_subframe.jxs_joint_j_14')
        _template_6_motion_ground_hps_db_sf_atch = get_object('.template_6_motion.ground.hps_db_sf_atch')
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_db_sf_atch))
        _template_6_motion_ground_origo = get_object('.template_6_motion.ground.origo')
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_6_motion_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe.jxs_joint_j_14', exc)

    try:
        jxs_joint_j_16 = get_object('.template_6_motion.mts_body_mount.jxs_joint_j_16')
        relative_to = get_object('.template_6_motion.mts_body_mount')
        jxs_joint_j_16.relative_to = relative_to
        jxs_joint_j_16.marker_name = target_path('.template_6_motion.mts_body_mount.jxs_joint_j_16')
        _template_6_motion_ground_cfs_subframe_to_body_point = get_object('.template_6_motion.ground.cfs_subframe_to_body_point')
        jxs_joint_j_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfs_subframe_to_body_point))
        _template_6_motion_ground_origo = get_object('.template_6_motion.ground.origo')
        jxs_joint_j_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_16.location, jxs_joint_j_16.orientation)
        jxs_joint_j_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.mts_body_mount.jxs_joint_j_16', exc)

    try:
        mts_body_mount = get_object('.template_6_motion.mts_body_mount')
        mts_body_mount.part_name = target_path('.template_6_motion.mts_body_mount')
        _template_6_motion_ground_cfs_subframe_to_body_point = get_object('.template_6_motion.ground.cfs_subframe_to_body_point')
        mts_body_mount.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfs_subframe_to_body_point))
        _template_6_motion_ground_origo = get_object('.template_6_motion.ground.origo')
        mts_body_mount.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('part modify rigid_body name_and_position .template_6_motion.mts_body_mount', exc)

    try:
        jxs_joint_j_10 = get_object('.template_6_motion.ges_collar.jxs_joint_j_10')
        relative_to = get_object('.template_6_motion.ges_collar')
        jxs_joint_j_10.relative_to = relative_to
        jxs_joint_j_10.marker_name = target_path('.template_6_motion.ges_collar.jxs_joint_j_10')
        _template_6_motion_ground_hps_uta_uc_atch = get_object('.template_6_motion.ground.hps_uta_uc_atch')
        jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_uta_uc_atch))
        _template_6_motion_ground_origo = get_object('.template_6_motion.ground.origo')
        jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_6_motion_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
        jxs_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_collar.jxs_joint_j_10', exc)

    try:
        gralin_24 = get_object('.template_6_motion.ges_collar.gralin_24')
        relative_to = get_object('.template_6_motion.ges_collar')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_6_motion.ges_collar.gralin_24')
        _template_6_motion_ground_hps_uc_bot = get_object('.template_6_motion.ground.hps_uc_bot')
        gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_uc_bot))
        _template_6_motion_ground_hps_uc_bot = get_object('.template_6_motion.ground.hps_uc_bot').location
        _template_6_motion_ground_cfs_collar_top = get_object('.template_6_motion.ground.cfs_collar_top').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hps_uc_bot, _template_6_motion_ground_cfs_collar_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_collar.gralin_24', exc)

    try:
        jxs_joint_i_1 = get_object('.template_6_motion.ges_collar.jxs_joint_i_1')
        relative_to = get_object('.template_6_motion.ges_collar')
        jxs_joint_i_1.relative_to = relative_to
        jxs_joint_i_1.marker_name = target_path('.template_6_motion.ges_collar.jxs_joint_i_1')
        _template_6_motion_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_6_motion.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_upper_cylinder_jxs_joint_j_1))
        _template_6_motion_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_6_motion.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
        jxs_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_collar.jxs_joint_i_1', exc)

    try:
        gralin_collar = get_object('.template_6_motion.ges_collar.gralin_collar')
        gralin_collar.cylinder_name = target_path('.template_6_motion.ges_collar.gralin_collar')
        _template_6_motion_ground_hps_uc_bot = get_object('.template_6_motion.ground.hps_uc_bot').location
        _template_6_motion_ground_cfs_collar_top = get_object('.template_6_motion.ground.cfs_collar_top').location
        gralin_collar.length = (VecUtils.DM(_template_6_motion_ground_hps_uc_bot, _template_6_motion_ground_cfs_collar_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_collar.gralin_collar', exc)

    try:
        MARKER_5 = get_object('.template_6_motion.ges_sf_rod.MARKER_5')
        relative_to = get_object('.template_6_motion.ges_sf_rod')
        MARKER_5.relative_to = relative_to
        MARKER_5.marker_name = target_path('.template_6_motion.ges_sf_rod.MARKER_5')
        _template_6_motion_ges_sf_rod_PT3 = get_object('.template_6_motion.ges_sf_rod.PT3')
        MARKER_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_sf_rod_PT3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_5.location, MARKER_5.orientation)
        MARKER_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_sf_rod.MARKER_5', exc)

    try:
        gralin_25 = get_object('.template_6_motion.ges_sf_rod.gralin_25')
        relative_to = get_object('.template_6_motion.ges_sf_rod')
        gralin_25.relative_to = relative_to
        gralin_25.marker_name = target_path('.template_6_motion.ges_sf_rod.gralin_25')
        _template_6_motion_ground_hps_rod_bot = get_object('.template_6_motion.ground.hps_rod_bot')
        gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hps_rod_bot))
        _template_6_motion_ges_sf_rod_PT3 = get_object('.template_6_motion.ges_sf_rod.PT3').location
        _template_6_motion_ground_hps_db_sf_atch = get_object('.template_6_motion.ground.hps_db_sf_atch').location
        gralin_25.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ges_sf_rod_PT3, _template_6_motion_ground_hps_db_sf_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_25.location, gralin_25.orientation)
        gralin_25.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_25.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_sf_rod.gralin_25', exc)

    try:
        CYLINDER_30 = get_object('.template_6_motion.ges_sf_rod.CYLINDER_30')
        CYLINDER_30.cylinder_name = target_path('.template_6_motion.ges_sf_rod.CYLINDER_30')
        _template_6_motion_ground_hps_rod_bot = get_object('.template_6_motion.ground.hps_rod_bot').location
        _template_6_motion_ground_hps_rod_top = get_object('.template_6_motion.ground.hps_rod_top').location
        CYLINDER_30.length = (VecUtils.DM(_template_6_motion_ground_hps_rod_bot, _template_6_motion_ground_hps_rod_top))
        CYLINDER_30.radius = 27.5


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ges_sf_rod.CYLINDER_30', exc)

    try:
        inertia_frame = get_object('.template_6_motion.ges_subframe_2.inertia_frame')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_6_motion.ges_subframe_2.inertia_frame')
        _template_6_motion_ges_subframe_2_cm = get_object('.template_6_motion.ges_subframe_2.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_cm))
        _template_6_motion_ges_subframe_2 = get_object('.template_6_motion.ges_subframe_2')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.inertia_frame', exc)

    try:
        graout_5 = get_object('.template_6_motion.ges_subframe_2.graout_5')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        graout_5.relative_to = relative_to
        graout_5.marker_name = target_path('.template_6_motion.ges_subframe_2.graout_5')
        _template_6_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpl_udb_spndl_atch_1')
        graout_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_udb_spndl_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_5.location, graout_5.orientation)
        graout_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.graout_5', exc)

    try:
        graout_6 = get_object('.template_6_motion.ges_subframe_2.graout_6')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        graout_6.relative_to = relative_to
        graout_6.marker_name = target_path('.template_6_motion.ges_subframe_2.graout_6')
        _template_6_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpr_udb_spndl_atch_1')
        graout_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_udb_spndl_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_6.location, graout_6.orientation)
        graout_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.graout_6', exc)

    try:
        graout_7 = get_object('.template_6_motion.ges_subframe_2.graout_7')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        graout_7.relative_to = relative_to
        graout_7.marker_name = target_path('.template_6_motion.ges_subframe_2.graout_7')
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top')
        graout_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_7.location, graout_7.orientation)
        graout_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.graout_7', exc)

    try:
        graout_8 = get_object('.template_6_motion.ges_subframe_2.graout_8')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        graout_8.relative_to = relative_to
        graout_8.marker_name = target_path('.template_6_motion.ges_subframe_2.graout_8')
        _template_6_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpr_ib_uc_sf_atch')
        graout_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_ib_uc_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_8.location, graout_8.orientation)
        graout_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.graout_8', exc)

    try:
        graout_9 = get_object('.template_6_motion.ges_subframe_2.graout_9')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        graout_9.relative_to = relative_to
        graout_9.marker_name = target_path('.template_6_motion.ges_subframe_2.graout_9')
        _template_6_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpl_ib_uc_sf_atch')
        graout_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_ib_uc_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_9.location, graout_9.orientation)
        graout_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.graout_9', exc)

    try:
        graout_10 = get_object('.template_6_motion.ges_subframe_2.graout_10')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        graout_10.relative_to = relative_to
        graout_10.marker_name = target_path('.template_6_motion.ges_subframe_2.graout_10')
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top')
        graout_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_10.location, graout_10.orientation)
        graout_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.graout_10', exc)

    try:
        jxl_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_16')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        jxl_joint_j_16.relative_to = relative_to
        jxl_joint_j_16.marker_name = target_path('.template_6_motion.ges_subframe_2.jxl_joint_j_16')
        _template_6_motion_ground_cfl_uc_sf_atch = get_object('.template_6_motion.ground.cfl_uc_sf_atch')
        jxl_joint_j_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfl_uc_sf_atch))
        _template_6_motion_ground_cfl_uc_sf_atch = get_object('.template_6_motion.ground.cfl_uc_sf_atch')
        jxl_joint_j_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfl_uc_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_16.location, jxl_joint_j_16.orientation)
        jxl_joint_j_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.jxl_joint_j_16', exc)

    try:
        jxr_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_16')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        jxr_joint_j_16.relative_to = relative_to
        jxr_joint_j_16.marker_name = target_path('.template_6_motion.ges_subframe_2.jxr_joint_j_16')
        _template_6_motion_ground_cfr_uc_sf_atch = get_object('.template_6_motion.ground.cfr_uc_sf_atch')
        jxr_joint_j_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfr_uc_sf_atch))
        _template_6_motion_ground_cfr_uc_sf_atch = get_object('.template_6_motion.ground.cfr_uc_sf_atch')
        jxr_joint_j_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfr_uc_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_16.location, jxr_joint_j_16.orientation)
        jxr_joint_j_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.jxr_joint_j_16', exc)

    try:
        jxs_joint_i_17 = get_object('.template_6_motion.ges_subframe_2.jxs_joint_i_17')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        jxs_joint_i_17.relative_to = relative_to
        jxs_joint_i_17.marker_name = target_path('.template_6_motion.ges_subframe_2.jxs_joint_i_17')
        _template_6_motion_mts_body_mount_2_jxs_joint_j_17 = get_object('.template_6_motion.mts_body_mount_2.jxs_joint_j_17')
        jxs_joint_i_17.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_mts_body_mount_2_jxs_joint_j_17))
        _template_6_motion_mts_body_mount_2_jxs_joint_j_17 = get_object('.template_6_motion.mts_body_mount_2.jxs_joint_j_17')
        jxs_joint_i_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_mts_body_mount_2_jxs_joint_j_17))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_17.location, jxs_joint_i_17.orientation)
        jxs_joint_i_17.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_17.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.jxs_joint_i_17', exc)

    try:
        jxl_joint_j_6 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_6')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        jxl_joint_j_6.relative_to = relative_to
        jxl_joint_j_6.marker_name = target_path('.template_6_motion.ges_subframe_2.jxl_joint_j_6')
        _template_6_motion_ground_hpl_spndl_sf_atch = get_object('.template_6_motion.ground.hpl_spndl_sf_atch')
        jxl_joint_j_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_spndl_sf_atch))
        _template_6_motion_ground_hpl_spndl_sf_atch = get_object('.template_6_motion.ground.hpl_spndl_sf_atch').location
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top').location
        jxl_joint_j_6.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_spndl_sf_atch, _template_6_motion_ground_hpl_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_6.location, jxl_joint_j_6.orientation)
        jxl_joint_j_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_6.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.jxl_joint_j_6', exc)

    try:
        jxr_joint_j_6 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_6')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        jxr_joint_j_6.relative_to = relative_to
        jxr_joint_j_6.marker_name = target_path('.template_6_motion.ges_subframe_2.jxr_joint_j_6')
        _template_6_motion_ground_hpr_spndl_sf_atch = get_object('.template_6_motion.ground.hpr_spndl_sf_atch')
        jxr_joint_j_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_spndl_sf_atch))
        _template_6_motion_ground_hpr_spndl_sf_atch = get_object('.template_6_motion.ground.hpr_spndl_sf_atch').location
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top').location
        jxr_joint_j_6.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_spndl_sf_atch, _template_6_motion_ground_hpr_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_6.location, jxr_joint_j_6.orientation)
        jxr_joint_j_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_6.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.jxr_joint_j_6', exc)

    try:
        jxl_joint_j_17 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_17')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        jxl_joint_j_17.relative_to = relative_to
        jxl_joint_j_17.marker_name = target_path('.template_6_motion.ges_subframe_2.jxl_joint_j_17')
        _template_6_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpl_upract_sf_atch_1')
        jxl_joint_j_17.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_upract_sf_atch_1))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        jxl_joint_j_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_17.location, jxl_joint_j_17.orientation)
        jxl_joint_j_17.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_17.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.jxl_joint_j_17', exc)

    try:
        jxr_joint_j_17 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_17')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        jxr_joint_j_17.relative_to = relative_to
        jxr_joint_j_17.marker_name = target_path('.template_6_motion.ges_subframe_2.jxr_joint_j_17')
        _template_6_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpr_upract_sf_atch_1')
        jxr_joint_j_17.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_upract_sf_atch_1))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        jxr_joint_j_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_17.location, jxr_joint_j_17.orientation)
        jxr_joint_j_17.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_17.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.jxr_joint_j_17', exc)

    try:
        uel_gearaero_jjoint_1 = get_object('.template_6_motion.ges_subframe_2.uel_gearaero_jjoint_1')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        uel_gearaero_jjoint_1.relative_to = relative_to
        uel_gearaero_jjoint_1.marker_name = target_path('.template_6_motion.ges_subframe_2.uel_gearaero_jjoint_1')
        _template_6_motion_ges_subframe_2_jxl_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_16')
        uel_gearaero_jjoint_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxl_joint_j_16))
        _template_6_motion_ges_subframe_2_jxl_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_16')
        uel_gearaero_jjoint_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxl_joint_j_16))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_gearaero_jjoint_1.location, uel_gearaero_jjoint_1.orientation)
        uel_gearaero_jjoint_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_gearaero_jjoint_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.uel_gearaero_jjoint_1', exc)

    try:
        uer_gearaero_jjoint_1 = get_object('.template_6_motion.ges_subframe_2.uer_gearaero_jjoint_1')
        relative_to = get_object('.template_6_motion.ges_subframe_2')
        uer_gearaero_jjoint_1.relative_to = relative_to
        uer_gearaero_jjoint_1.marker_name = target_path('.template_6_motion.ges_subframe_2.uer_gearaero_jjoint_1')
        _template_6_motion_ges_subframe_2_jxr_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_16')
        uer_gearaero_jjoint_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxr_joint_j_16))
        _template_6_motion_ges_subframe_2_jxr_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_16')
        uer_gearaero_jjoint_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 180.0, 0.0], _template_6_motion_ges_subframe_2_jxr_joint_j_16))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_gearaero_jjoint_1.location, uer_gearaero_jjoint_1.orientation)
        uer_gearaero_jjoint_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uer_gearaero_jjoint_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ges_subframe_2.uer_gearaero_jjoint_1', exc)

    try:
        gralin_12 = get_object('.template_6_motion.gel_upper_cylinder.gralin_12')
        relative_to = get_object('.template_6_motion.gel_upper_cylinder')
        gralin_12.relative_to = relative_to
        gralin_12.marker_name = target_path('.template_6_motion.gel_upper_cylinder.gralin_12')
        _template_6_motion_ground_cfl_uc_top = get_object('.template_6_motion.ground.cfl_uc_top')
        gralin_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfl_uc_top))
        _template_6_motion_ground_cfl_uc_top = get_object('.template_6_motion.ground.cfl_uc_top').location
        _template_6_motion_ground_cfl_uc_bot = get_object('.template_6_motion.ground.cfl_uc_bot').location
        gralin_12.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_cfl_uc_top, _template_6_motion_ground_cfl_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_12.location, gralin_12.orientation)
        gralin_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_cylinder.gralin_12', exc)

    try:
        gralin_16 = get_object('.template_6_motion.gel_upper_cylinder.gralin_16')
        relative_to = get_object('.template_6_motion.gel_upper_cylinder')
        gralin_16.relative_to = relative_to
        gralin_16.marker_name = target_path('.template_6_motion.gel_upper_cylinder.gralin_16')
        _template_6_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpl_ib_uc_sf_atch')
        gralin_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_ib_uc_sf_atch))
        _template_6_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpl_ib_uc_sf_atch').location
        _template_6_motion_ground_hpl_uc_geompt = get_object('.template_6_motion.ground.hpl_uc_geompt').location
        gralin_16.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_ib_uc_sf_atch, _template_6_motion_ground_hpl_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_16.location, gralin_16.orientation)
        gralin_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_cylinder.gralin_16', exc)

    try:
        gralin_20 = get_object('.template_6_motion.gel_upper_cylinder.gralin_20')
        relative_to = get_object('.template_6_motion.gel_upper_cylinder')
        gralin_20.relative_to = relative_to
        gralin_20.marker_name = target_path('.template_6_motion.gel_upper_cylinder.gralin_20')
        _template_6_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpl_ib_uc_sf_atch')
        gralin_20.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_ib_uc_sf_atch))
        _template_6_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpl_ib_uc_sf_atch').location
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top').location
        gralin_20.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_ib_uc_sf_atch, _template_6_motion_ground_hpl_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_20.location, gralin_20.orientation)
        gralin_20.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_20.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_cylinder.gralin_20', exc)

    try:
        jxl_joint_i_16 = get_object('.template_6_motion.gel_upper_cylinder.jxl_joint_i_16')
        relative_to = get_object('.template_6_motion.gel_upper_cylinder')
        jxl_joint_i_16.relative_to = relative_to
        jxl_joint_i_16.marker_name = target_path('.template_6_motion.gel_upper_cylinder.jxl_joint_i_16')
        _template_6_motion_ges_subframe_2_jxl_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_16')
        jxl_joint_i_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxl_joint_j_16))
        _template_6_motion_ges_subframe_2_jxl_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_16')
        jxl_joint_i_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxl_joint_j_16))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_16.location, jxl_joint_i_16.orientation)
        jxl_joint_i_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_cylinder.jxl_joint_i_16', exc)

    try:
        jxl_joint_i_7 = get_object('.template_6_motion.gel_upper_cylinder.jxl_joint_i_7')
        relative_to = get_object('.template_6_motion.gel_upper_cylinder')
        jxl_joint_i_7.relative_to = relative_to
        jxl_joint_i_7.marker_name = target_path('.template_6_motion.gel_upper_cylinder.jxl_joint_i_7')
        _template_6_motion_gel_lwract_jxl_joint_j_7 = get_object('.template_6_motion.gel_lwract.jxl_joint_j_7')
        jxl_joint_i_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_lwract_jxl_joint_j_7))
        _template_6_motion_gel_lwract_jxl_joint_j_7 = get_object('.template_6_motion.gel_lwract.jxl_joint_j_7')
        jxl_joint_i_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_lwract_jxl_joint_j_7))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_7.location, jxl_joint_i_7.orientation)
        jxl_joint_i_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_cylinder.jxl_joint_i_7', exc)

    try:
        gralin_upper_cylinder = get_object('.template_6_motion.gel_upper_cylinder.gralin_upper_cylinder')
        gralin_upper_cylinder.cylinder_name = target_path('.template_6_motion.gel_upper_cylinder.gralin_upper_cylinder')
        _template_6_motion_ground_cfl_uc_top = get_object('.template_6_motion.ground.cfl_uc_top').location
        _template_6_motion_ground_cfl_uc_bot = get_object('.template_6_motion.ground.cfl_uc_bot').location
        gralin_upper_cylinder.length = (VecUtils.DM(_template_6_motion_ground_cfl_uc_top, _template_6_motion_ground_cfl_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_upper_cylinder.gralin_upper_cylinder', exc)

    try:
        gralin_geom = get_object('.template_6_motion.gel_upper_cylinder.gralin_geom')
        gralin_geom.cylinder_name = target_path('.template_6_motion.gel_upper_cylinder.gralin_geom')
        _template_6_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpl_ib_uc_sf_atch').location
        _template_6_motion_ground_hpl_uc_geompt = get_object('.template_6_motion.ground.hpl_uc_geompt').location
        gralin_geom.length = (VecUtils.DM(_template_6_motion_ground_hpl_ib_uc_sf_atch, _template_6_motion_ground_hpl_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_upper_cylinder.gralin_geom', exc)

    try:
        gralin_geom3 = get_object('.template_6_motion.gel_upper_cylinder.gralin_geom3')
        gralin_geom3.cylinder_name = target_path('.template_6_motion.gel_upper_cylinder.gralin_geom3')
        _template_6_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpl_ib_uc_sf_atch').location
        _template_6_motion_ground_hpl_uc_top = get_object('.template_6_motion.ground.hpl_uc_top').location
        gralin_geom3.length = (VecUtils.DM(_template_6_motion_ground_hpl_ib_uc_sf_atch, _template_6_motion_ground_hpl_uc_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_upper_cylinder.gralin_geom3', exc)

    try:
        gralin_13 = get_object('.template_6_motion.ger_upper_cylinder.gralin_13')
        relative_to = get_object('.template_6_motion.ger_upper_cylinder')
        gralin_13.relative_to = relative_to
        gralin_13.marker_name = target_path('.template_6_motion.ger_upper_cylinder.gralin_13')
        _template_6_motion_ground_cfr_uc_top = get_object('.template_6_motion.ground.cfr_uc_top')
        gralin_13.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfr_uc_top))
        _template_6_motion_ground_cfr_uc_top = get_object('.template_6_motion.ground.cfr_uc_top').location
        _template_6_motion_ground_cfr_uc_bot = get_object('.template_6_motion.ground.cfr_uc_bot').location
        gralin_13.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_cfr_uc_top, _template_6_motion_ground_cfr_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_13.location, gralin_13.orientation)
        gralin_13.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_13.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_cylinder.gralin_13', exc)

    try:
        gralin_17 = get_object('.template_6_motion.ger_upper_cylinder.gralin_17')
        relative_to = get_object('.template_6_motion.ger_upper_cylinder')
        gralin_17.relative_to = relative_to
        gralin_17.marker_name = target_path('.template_6_motion.ger_upper_cylinder.gralin_17')
        _template_6_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpr_ib_uc_sf_atch')
        gralin_17.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_ib_uc_sf_atch))
        _template_6_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpr_ib_uc_sf_atch').location
        _template_6_motion_ground_hpr_uc_geompt = get_object('.template_6_motion.ground.hpr_uc_geompt').location
        gralin_17.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_ib_uc_sf_atch, _template_6_motion_ground_hpr_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_17.location, gralin_17.orientation)
        gralin_17.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_17.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_cylinder.gralin_17', exc)

    try:
        gralin_21 = get_object('.template_6_motion.ger_upper_cylinder.gralin_21')
        relative_to = get_object('.template_6_motion.ger_upper_cylinder')
        gralin_21.relative_to = relative_to
        gralin_21.marker_name = target_path('.template_6_motion.ger_upper_cylinder.gralin_21')
        _template_6_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpr_ib_uc_sf_atch')
        gralin_21.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_ib_uc_sf_atch))
        _template_6_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpr_ib_uc_sf_atch').location
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top').location
        gralin_21.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_ib_uc_sf_atch, _template_6_motion_ground_hpr_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_21.location, gralin_21.orientation)
        gralin_21.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_21.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_cylinder.gralin_21', exc)

    try:
        jxr_joint_i_16 = get_object('.template_6_motion.ger_upper_cylinder.jxr_joint_i_16')
        relative_to = get_object('.template_6_motion.ger_upper_cylinder')
        jxr_joint_i_16.relative_to = relative_to
        jxr_joint_i_16.marker_name = target_path('.template_6_motion.ger_upper_cylinder.jxr_joint_i_16')
        _template_6_motion_ges_subframe_2_jxr_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_16')
        jxr_joint_i_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxr_joint_j_16))
        _template_6_motion_ges_subframe_2_jxr_joint_j_16 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_16')
        jxr_joint_i_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxr_joint_j_16))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_16.location, jxr_joint_i_16.orientation)
        jxr_joint_i_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_cylinder.jxr_joint_i_16', exc)

    try:
        jxr_joint_i_7 = get_object('.template_6_motion.ger_upper_cylinder.jxr_joint_i_7')
        relative_to = get_object('.template_6_motion.ger_upper_cylinder')
        jxr_joint_i_7.relative_to = relative_to
        jxr_joint_i_7.marker_name = target_path('.template_6_motion.ger_upper_cylinder.jxr_joint_i_7')
        _template_6_motion_ger_lwract_jxr_joint_j_7 = get_object('.template_6_motion.ger_lwract.jxr_joint_j_7')
        jxr_joint_i_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_lwract_jxr_joint_j_7))
        _template_6_motion_ger_lwract_jxr_joint_j_7 = get_object('.template_6_motion.ger_lwract.jxr_joint_j_7')
        jxr_joint_i_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_lwract_jxr_joint_j_7))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_7.location, jxr_joint_i_7.orientation)
        jxr_joint_i_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_cylinder.jxr_joint_i_7', exc)

    try:
        gralin_upper_cylinder = get_object('.template_6_motion.ger_upper_cylinder.gralin_upper_cylinder')
        gralin_upper_cylinder.cylinder_name = target_path('.template_6_motion.ger_upper_cylinder.gralin_upper_cylinder')
        _template_6_motion_ground_cfr_uc_top = get_object('.template_6_motion.ground.cfr_uc_top').location
        _template_6_motion_ground_cfr_uc_bot = get_object('.template_6_motion.ground.cfr_uc_bot').location
        gralin_upper_cylinder.length = (VecUtils.DM(_template_6_motion_ground_cfr_uc_top, _template_6_motion_ground_cfr_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_upper_cylinder.gralin_upper_cylinder', exc)

    try:
        gralin_geom = get_object('.template_6_motion.ger_upper_cylinder.gralin_geom')
        gralin_geom.cylinder_name = target_path('.template_6_motion.ger_upper_cylinder.gralin_geom')
        _template_6_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpr_ib_uc_sf_atch').location
        _template_6_motion_ground_hpr_uc_geompt = get_object('.template_6_motion.ground.hpr_uc_geompt').location
        gralin_geom.length = (VecUtils.DM(_template_6_motion_ground_hpr_ib_uc_sf_atch, _template_6_motion_ground_hpr_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_upper_cylinder.gralin_geom', exc)

    try:
        gralin_geom3 = get_object('.template_6_motion.ger_upper_cylinder.gralin_geom3')
        gralin_geom3.cylinder_name = target_path('.template_6_motion.ger_upper_cylinder.gralin_geom3')
        _template_6_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_6_motion.ground.hpr_ib_uc_sf_atch').location
        _template_6_motion_ground_hpr_uc_top = get_object('.template_6_motion.ground.hpr_uc_top').location
        gralin_geom3.length = (VecUtils.DM(_template_6_motion_ground_hpr_ib_uc_sf_atch, _template_6_motion_ground_hpr_uc_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_upper_cylinder.gralin_geom3', exc)

    try:
        gralin_14 = get_object('.template_6_motion.gel_lower_cylinder.gralin_14')
        relative_to = get_object('.template_6_motion.gel_lower_cylinder')
        gralin_14.relative_to = relative_to
        gralin_14.marker_name = target_path('.template_6_motion.gel_lower_cylinder.gralin_14')
        _template_6_motion_ground_cfl_lc_top = get_object('.template_6_motion.ground.cfl_lc_top')
        gralin_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfl_lc_top))
        _template_6_motion_ground_cfl_lc_top = get_object('.template_6_motion.ground.cfl_lc_top').location
        _template_6_motion_ground_hpl_lc_bot = get_object('.template_6_motion.ground.hpl_lc_bot').location
        gralin_14.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_cfl_lc_top, _template_6_motion_ground_hpl_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_14.location, gralin_14.orientation)
        gralin_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_cylinder.gralin_14', exc)

    try:
        gralin_22 = get_object('.template_6_motion.gel_lower_cylinder.gralin_22')
        relative_to = get_object('.template_6_motion.gel_lower_cylinder')
        gralin_22.relative_to = relative_to
        gralin_22.marker_name = target_path('.template_6_motion.gel_lower_cylinder.gralin_22')
        _template_6_motion_ground_hpl_ib_axle = get_object('.template_6_motion.ground.hpl_ib_axle')
        gralin_22.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_ib_axle))
        _template_6_motion_ground_hpl_ib_axle = get_object('.template_6_motion.ground.hpl_ib_axle').location
        _template_6_motion_ground_hpl_ob_axle1 = get_object('.template_6_motion.ground.hpl_ob_axle1').location
        gralin_22.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_ib_axle, _template_6_motion_ground_hpl_ob_axle1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_22.location, gralin_22.orientation)
        gralin_22.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_22.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_cylinder.gralin_22', exc)

    try:
        jxl_joint_j_11 = get_object('.template_6_motion.gel_lower_cylinder.jxl_joint_j_11')
        relative_to = get_object('.template_6_motion.gel_lower_cylinder')
        jxl_joint_j_11.relative_to = relative_to
        jxl_joint_j_11.marker_name = target_path('.template_6_motion.gel_lower_cylinder.jxl_joint_j_11')
        _template_6_motion_ground_hpl_lta_lc_atch_1 = get_object('.template_6_motion.ground.hpl_lta_lc_atch_1')
        jxl_joint_j_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_lta_lc_atch_1))
        _template_6_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_lta_connect_atch_1').location
        _template_6_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_1').location
        jxl_joint_j_11.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_lta_connect_atch_1, _template_6_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_11.location, jxl_joint_j_11.orientation)
        jxl_joint_j_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_cylinder.jxl_joint_j_11', exc)

    try:
        jxl_joint_i_12 = get_object('.template_6_motion.gel_lower_cylinder.jxl_joint_i_12')
        relative_to = get_object('.template_6_motion.gel_lower_cylinder')
        jxl_joint_i_12.relative_to = relative_to
        jxl_joint_i_12.marker_name = target_path('.template_6_motion.gel_lower_cylinder.jxl_joint_i_12')
        _template_6_motion_gel_upper_cylinder_jxl_joint_j_12 = get_object('.template_6_motion.gel_upper_cylinder.jxl_joint_j_12')
        jxl_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_upper_cylinder_jxl_joint_j_12))
        _template_6_motion_gel_upper_cylinder_jxl_joint_j_12 = get_object('.template_6_motion.gel_upper_cylinder.jxl_joint_j_12')
        jxl_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_upper_cylinder_jxl_joint_j_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_12.location, jxl_joint_i_12.orientation)
        jxl_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_cylinder.jxl_joint_i_12', exc)

    try:
        MARKER_352 = get_object('.template_6_motion.gel_lower_cylinder.MARKER_352')
        relative_to = get_object('.template_6_motion.gel_lower_cylinder')
        MARKER_352.relative_to = relative_to
        MARKER_352.marker_name = target_path('.template_6_motion.gel_lower_cylinder.MARKER_352')
        _template_6_motion_ground_hpl_ob_axle1 = get_object('.template_6_motion.ground.hpl_ob_axle1')
        MARKER_352.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_ob_axle1))
        _template_6_motion_ground_hpl_ob_axle1 = get_object('.template_6_motion.ground.hpl_ob_axle1').location
        _template_6_motion_ground_hpl_stator_attach = get_object('.template_6_motion.ground.hpl_stator_attach').location
        MARKER_352.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_ob_axle1, _template_6_motion_ground_hpl_stator_attach, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_352.location, MARKER_352.orientation)
        MARKER_352.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_352.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_cylinder.MARKER_352', exc)

    try:
        gralin_lower_cylinder = get_object('.template_6_motion.gel_lower_cylinder.gralin_lower_cylinder')
        gralin_lower_cylinder.cylinder_name = target_path('.template_6_motion.gel_lower_cylinder.gralin_lower_cylinder')
        _template_6_motion_ground_cfl_lc_top = get_object('.template_6_motion.ground.cfl_lc_top').location
        _template_6_motion_ground_hpl_lc_bot = get_object('.template_6_motion.ground.hpl_lc_bot').location
        gralin_lower_cylinder.length = (VecUtils.DM(_template_6_motion_ground_cfl_lc_top, _template_6_motion_ground_hpl_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_lower_cylinder.gralin_lower_cylinder', exc)

    try:
        gralin_geom = get_object('.template_6_motion.gel_lower_cylinder.gralin_geom')
        gralin_geom.cylinder_name = target_path('.template_6_motion.gel_lower_cylinder.gralin_geom')
        _template_6_motion_ground_hpl_ib_axle = get_object('.template_6_motion.ground.hpl_ib_axle').location
        _template_6_motion_ground_hpl_ob_axle1 = get_object('.template_6_motion.ground.hpl_ob_axle1').location
        gralin_geom.length = (VecUtils.DM(_template_6_motion_ground_hpl_ib_axle, _template_6_motion_ground_hpl_ob_axle1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_lower_cylinder.gralin_geom', exc)

    try:
        gralin_15 = get_object('.template_6_motion.ger_lower_cylinder.gralin_15')
        relative_to = get_object('.template_6_motion.ger_lower_cylinder')
        gralin_15.relative_to = relative_to
        gralin_15.marker_name = target_path('.template_6_motion.ger_lower_cylinder.gralin_15')
        _template_6_motion_ground_cfr_lc_top = get_object('.template_6_motion.ground.cfr_lc_top')
        gralin_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfr_lc_top))
        _template_6_motion_ground_cfr_lc_top = get_object('.template_6_motion.ground.cfr_lc_top').location
        _template_6_motion_ground_hpr_lc_bot = get_object('.template_6_motion.ground.hpr_lc_bot').location
        gralin_15.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_cfr_lc_top, _template_6_motion_ground_hpr_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_15.location, gralin_15.orientation)
        gralin_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_cylinder.gralin_15', exc)

    try:
        gralin_23 = get_object('.template_6_motion.ger_lower_cylinder.gralin_23')
        relative_to = get_object('.template_6_motion.ger_lower_cylinder')
        gralin_23.relative_to = relative_to
        gralin_23.marker_name = target_path('.template_6_motion.ger_lower_cylinder.gralin_23')
        _template_6_motion_ground_hpr_ib_axle = get_object('.template_6_motion.ground.hpr_ib_axle')
        gralin_23.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_ib_axle))
        _template_6_motion_ground_hpr_ib_axle = get_object('.template_6_motion.ground.hpr_ib_axle').location
        _template_6_motion_ground_hpr_ob_axle1 = get_object('.template_6_motion.ground.hpr_ob_axle1').location
        gralin_23.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_ib_axle, _template_6_motion_ground_hpr_ob_axle1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_23.location, gralin_23.orientation)
        gralin_23.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_23.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_cylinder.gralin_23', exc)

    try:
        jxr_joint_j_11 = get_object('.template_6_motion.ger_lower_cylinder.jxr_joint_j_11')
        relative_to = get_object('.template_6_motion.ger_lower_cylinder')
        jxr_joint_j_11.relative_to = relative_to
        jxr_joint_j_11.marker_name = target_path('.template_6_motion.ger_lower_cylinder.jxr_joint_j_11')
        _template_6_motion_ground_hpr_lta_lc_atch_1 = get_object('.template_6_motion.ground.hpr_lta_lc_atch_1')
        jxr_joint_j_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_lta_lc_atch_1))
        _template_6_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_lta_connect_atch_1').location
        _template_6_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_1').location
        jxr_joint_j_11.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_lta_connect_atch_1, _template_6_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_11.location, jxr_joint_j_11.orientation)
        jxr_joint_j_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_cylinder.jxr_joint_j_11', exc)

    try:
        jxr_joint_i_12 = get_object('.template_6_motion.ger_lower_cylinder.jxr_joint_i_12')
        relative_to = get_object('.template_6_motion.ger_lower_cylinder')
        jxr_joint_i_12.relative_to = relative_to
        jxr_joint_i_12.marker_name = target_path('.template_6_motion.ger_lower_cylinder.jxr_joint_i_12')
        _template_6_motion_ger_upper_cylinder_jxr_joint_j_12 = get_object('.template_6_motion.ger_upper_cylinder.jxr_joint_j_12')
        jxr_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_upper_cylinder_jxr_joint_j_12))
        _template_6_motion_ger_upper_cylinder_jxr_joint_j_12 = get_object('.template_6_motion.ger_upper_cylinder.jxr_joint_j_12')
        jxr_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_upper_cylinder_jxr_joint_j_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_12.location, jxr_joint_i_12.orientation)
        jxr_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_cylinder.jxr_joint_i_12', exc)

    try:
        MARKER_353 = get_object('.template_6_motion.ger_lower_cylinder.MARKER_353')
        relative_to = get_object('.template_6_motion.ger_lower_cylinder')
        MARKER_353.relative_to = relative_to
        MARKER_353.marker_name = target_path('.template_6_motion.ger_lower_cylinder.MARKER_353')
        _template_6_motion_ground_hpr_ob_axle1 = get_object('.template_6_motion.ground.hpr_ob_axle1')
        MARKER_353.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_ob_axle1))
        _template_6_motion_ground_hpr_ob_axle1 = get_object('.template_6_motion.ground.hpr_ob_axle1').location
        _template_6_motion_ground_hpr_stator_attach = get_object('.template_6_motion.ground.hpr_stator_attach').location
        MARKER_353.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_ob_axle1, _template_6_motion_ground_hpr_stator_attach, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_353.location, MARKER_353.orientation)
        MARKER_353.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_353.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_cylinder.MARKER_353', exc)

    try:
        gralin_lower_cylinder = get_object('.template_6_motion.ger_lower_cylinder.gralin_lower_cylinder')
        gralin_lower_cylinder.cylinder_name = target_path('.template_6_motion.ger_lower_cylinder.gralin_lower_cylinder')
        _template_6_motion_ground_cfr_lc_top = get_object('.template_6_motion.ground.cfr_lc_top').location
        _template_6_motion_ground_hpr_lc_bot = get_object('.template_6_motion.ground.hpr_lc_bot').location
        gralin_lower_cylinder.length = (VecUtils.DM(_template_6_motion_ground_cfr_lc_top, _template_6_motion_ground_hpr_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_lower_cylinder.gralin_lower_cylinder', exc)

    try:
        gralin_geom = get_object('.template_6_motion.ger_lower_cylinder.gralin_geom')
        gralin_geom.cylinder_name = target_path('.template_6_motion.ger_lower_cylinder.gralin_geom')
        _template_6_motion_ground_hpr_ib_axle = get_object('.template_6_motion.ground.hpr_ib_axle').location
        _template_6_motion_ground_hpr_ob_axle1 = get_object('.template_6_motion.ground.hpr_ob_axle1').location
        gralin_geom.length = (VecUtils.DM(_template_6_motion_ground_hpr_ib_axle, _template_6_motion_ground_hpr_ob_axle1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_lower_cylinder.gralin_geom', exc)

    try:
        gralin_24 = get_object('.template_6_motion.gel_upper_dragbrace.gralin_24')
        relative_to = get_object('.template_6_motion.gel_upper_dragbrace')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_6_motion.gel_upper_dragbrace.gralin_24')
        _template_6_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpl_udb_spndl_atch_1')
        gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_udb_spndl_atch_1))
        _template_6_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpl_udb_spndl_atch_1').location
        _template_6_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_udb_atch_1').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_udb_spndl_atch_1, _template_6_motion_ground_hpl_ldb_udb_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_dragbrace.gralin_24', exc)

    try:
        jxl_joint_j_14 = get_object('.template_6_motion.gel_upper_dragbrace.jxl_joint_j_14')
        relative_to = get_object('.template_6_motion.gel_upper_dragbrace')
        jxl_joint_j_14.relative_to = relative_to
        jxl_joint_j_14.marker_name = target_path('.template_6_motion.gel_upper_dragbrace.jxl_joint_j_14')
        _template_6_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_udb_atch_1')
        jxl_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_ldb_udb_atch_1))
        _template_6_motion_ground_cfl_plane_ref_2 = get_object('.template_6_motion.ground.cfl_plane_ref_2')
        jxl_joint_j_14.orientation = _template_6_motion_ground_cfl_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_14.location, jxl_joint_j_14.orientation)
        jxl_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_dragbrace.jxl_joint_j_14', exc)

    try:
        jxl_joint_i_5 = get_object('.template_6_motion.gel_upper_dragbrace.jxl_joint_i_5')
        relative_to = get_object('.template_6_motion.gel_upper_dragbrace')
        jxl_joint_i_5.relative_to = relative_to
        jxl_joint_i_5.marker_name = target_path('.template_6_motion.gel_upper_dragbrace.jxl_joint_i_5')
        _template_6_motion_gel_spindle_jxl_joint_j_5 = get_object('.template_6_motion.gel_spindle.jxl_joint_j_5')
        jxl_joint_i_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_spindle_jxl_joint_j_5))
        _template_6_motion_gel_upper_dragbrace_jxl_joint_i_5 = get_object('.template_6_motion.gel_upper_dragbrace.jxl_joint_i_5').location
        _template_6_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_udb_atch_1').location
        _template_6_motion_ground_hpl_spndl_sf_atch = get_object('.template_6_motion.ground.hpl_spndl_sf_atch').location
        jxl_joint_i_5.orientation = (VecUtils.ORI_IN_PLANE(_template_6_motion_gel_upper_dragbrace_jxl_joint_i_5, _template_6_motion_ground_hpl_ldb_udb_atch_1, _template_6_motion_ground_hpl_spndl_sf_atch, "Z_ZX"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_5.location, jxl_joint_i_5.orientation)
        jxl_joint_i_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_dragbrace.jxl_joint_i_5', exc)

    try:
        gralin_upper_dragbrace = get_object('.template_6_motion.gel_upper_dragbrace.gralin_upper_dragbrace')
        gralin_upper_dragbrace.cylinder_name = target_path('.template_6_motion.gel_upper_dragbrace.gralin_upper_dragbrace')
        _template_6_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpl_udb_spndl_atch_1').location
        _template_6_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_udb_atch_1').location
        gralin_upper_dragbrace.length = (VecUtils.DM(_template_6_motion_ground_hpl_udb_spndl_atch_1, _template_6_motion_ground_hpl_ldb_udb_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_upper_dragbrace.gralin_upper_dragbrace', exc)

    try:
        gralin_25 = get_object('.template_6_motion.ger_upper_dragbrace.gralin_25')
        relative_to = get_object('.template_6_motion.ger_upper_dragbrace')
        gralin_25.relative_to = relative_to
        gralin_25.marker_name = target_path('.template_6_motion.ger_upper_dragbrace.gralin_25')
        _template_6_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpr_udb_spndl_atch_1')
        gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_udb_spndl_atch_1))
        _template_6_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpr_udb_spndl_atch_1').location
        _template_6_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_udb_atch_1').location
        gralin_25.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_udb_spndl_atch_1, _template_6_motion_ground_hpr_ldb_udb_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_25.location, gralin_25.orientation)
        gralin_25.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_25.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_dragbrace.gralin_25', exc)

    try:
        jxr_joint_j_14 = get_object('.template_6_motion.ger_upper_dragbrace.jxr_joint_j_14')
        relative_to = get_object('.template_6_motion.ger_upper_dragbrace')
        jxr_joint_j_14.relative_to = relative_to
        jxr_joint_j_14.marker_name = target_path('.template_6_motion.ger_upper_dragbrace.jxr_joint_j_14')
        _template_6_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_udb_atch_1')
        jxr_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_ldb_udb_atch_1))
        _template_6_motion_ground_cfr_plane_ref_2 = get_object('.template_6_motion.ground.cfr_plane_ref_2')
        jxr_joint_j_14.orientation = _template_6_motion_ground_cfr_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_14.location, jxr_joint_j_14.orientation)
        jxr_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_dragbrace.jxr_joint_j_14', exc)

    try:
        jxr_joint_i_5 = get_object('.template_6_motion.ger_upper_dragbrace.jxr_joint_i_5')
        relative_to = get_object('.template_6_motion.ger_upper_dragbrace')
        jxr_joint_i_5.relative_to = relative_to
        jxr_joint_i_5.marker_name = target_path('.template_6_motion.ger_upper_dragbrace.jxr_joint_i_5')
        _template_6_motion_ger_spindle_jxr_joint_j_5 = get_object('.template_6_motion.ger_spindle.jxr_joint_j_5')
        jxr_joint_i_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_spindle_jxr_joint_j_5))
        _template_6_motion_ger_upper_dragbrace_jxr_joint_i_5 = get_object('.template_6_motion.ger_upper_dragbrace.jxr_joint_i_5').location
        _template_6_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_udb_atch_1').location
        _template_6_motion_ground_hpr_spndl_sf_atch = get_object('.template_6_motion.ground.hpr_spndl_sf_atch').location
        jxr_joint_i_5.orientation = (VecUtils.ORI_IN_PLANE(_template_6_motion_ger_upper_dragbrace_jxr_joint_i_5, _template_6_motion_ground_hpr_ldb_udb_atch_1, _template_6_motion_ground_hpr_spndl_sf_atch, "Z_ZX"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_5.location, jxr_joint_i_5.orientation)
        jxr_joint_i_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_dragbrace.jxr_joint_i_5', exc)

    try:
        gralin_upper_dragbrace = get_object('.template_6_motion.ger_upper_dragbrace.gralin_upper_dragbrace')
        gralin_upper_dragbrace.cylinder_name = target_path('.template_6_motion.ger_upper_dragbrace.gralin_upper_dragbrace')
        _template_6_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpr_udb_spndl_atch_1').location
        _template_6_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_udb_atch_1').location
        gralin_upper_dragbrace.length = (VecUtils.DM(_template_6_motion_ground_hpr_udb_spndl_atch_1, _template_6_motion_ground_hpr_ldb_udb_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_upper_dragbrace.gralin_upper_dragbrace', exc)

    try:
        gralin_26 = get_object('.template_6_motion.gel_lower_dragbrace.gralin_26')
        relative_to = get_object('.template_6_motion.gel_lower_dragbrace')
        gralin_26.relative_to = relative_to
        gralin_26.marker_name = target_path('.template_6_motion.gel_lower_dragbrace.gralin_26')
        _template_6_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_udb_atch_1')
        gralin_26.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_ldb_udb_atch_1))
        _template_6_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_udb_atch_1').location
        _template_6_motion_ground_hpl_ldb_collar_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_collar_atch_1').location
        gralin_26.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_ldb_udb_atch_1, _template_6_motion_ground_hpl_ldb_collar_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_26.location, gralin_26.orientation)
        gralin_26.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_26.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_dragbrace.gralin_26', exc)

    try:
        jxl_joint_i_14 = get_object('.template_6_motion.gel_lower_dragbrace.jxl_joint_i_14')
        relative_to = get_object('.template_6_motion.gel_lower_dragbrace')
        jxl_joint_i_14.relative_to = relative_to
        jxl_joint_i_14.marker_name = target_path('.template_6_motion.gel_lower_dragbrace.jxl_joint_i_14')
        _template_6_motion_gel_upper_dragbrace_jxl_joint_j_14 = get_object('.template_6_motion.gel_upper_dragbrace.jxl_joint_j_14')
        jxl_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_upper_dragbrace_jxl_joint_j_14))
        _template_6_motion_gel_upper_dragbrace_jxl_joint_j_14 = get_object('.template_6_motion.gel_upper_dragbrace.jxl_joint_j_14')
        jxl_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_upper_dragbrace_jxl_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_14.location, jxl_joint_i_14.orientation)
        jxl_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_dragbrace.jxl_joint_i_14', exc)

    try:
        jxl_joint_i_10 = get_object('.template_6_motion.gel_lower_dragbrace.jxl_joint_i_10')
        relative_to = get_object('.template_6_motion.gel_lower_dragbrace')
        jxl_joint_i_10.relative_to = relative_to
        jxl_joint_i_10.marker_name = target_path('.template_6_motion.gel_lower_dragbrace.jxl_joint_i_10')
        _template_6_motion_gel_uc_collar_jxl_joint_j_10 = get_object('.template_6_motion.gel_uc_collar.jxl_joint_j_10')
        jxl_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_uc_collar_jxl_joint_j_10))
        _template_6_motion_gel_uc_collar_jxl_joint_j_10 = get_object('.template_6_motion.gel_uc_collar.jxl_joint_j_10')
        jxl_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_uc_collar_jxl_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_10.location, jxl_joint_i_10.orientation)
        jxl_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_dragbrace.jxl_joint_i_10', exc)

    try:
        gralin_lower_dragbrace = get_object('.template_6_motion.gel_lower_dragbrace.gralin_lower_dragbrace')
        gralin_lower_dragbrace.cylinder_name = target_path('.template_6_motion.gel_lower_dragbrace.gralin_lower_dragbrace')
        _template_6_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_udb_atch_1').location
        _template_6_motion_ground_hpl_ldb_collar_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_collar_atch_1').location
        gralin_lower_dragbrace.length = (VecUtils.DM(_template_6_motion_ground_hpl_ldb_udb_atch_1, _template_6_motion_ground_hpl_ldb_collar_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_lower_dragbrace.gralin_lower_dragbrace', exc)

    try:
        gralin_27 = get_object('.template_6_motion.ger_lower_dragbrace.gralin_27')
        relative_to = get_object('.template_6_motion.ger_lower_dragbrace')
        gralin_27.relative_to = relative_to
        gralin_27.marker_name = target_path('.template_6_motion.ger_lower_dragbrace.gralin_27')
        _template_6_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_udb_atch_1')
        gralin_27.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_ldb_udb_atch_1))
        _template_6_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_udb_atch_1').location
        _template_6_motion_ground_hpr_ldb_collar_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_collar_atch_1').location
        gralin_27.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_ldb_udb_atch_1, _template_6_motion_ground_hpr_ldb_collar_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_27.location, gralin_27.orientation)
        gralin_27.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_27.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_dragbrace.gralin_27', exc)

    try:
        jxr_joint_i_14 = get_object('.template_6_motion.ger_lower_dragbrace.jxr_joint_i_14')
        relative_to = get_object('.template_6_motion.ger_lower_dragbrace')
        jxr_joint_i_14.relative_to = relative_to
        jxr_joint_i_14.marker_name = target_path('.template_6_motion.ger_lower_dragbrace.jxr_joint_i_14')
        _template_6_motion_ger_upper_dragbrace_jxr_joint_j_14 = get_object('.template_6_motion.ger_upper_dragbrace.jxr_joint_j_14')
        jxr_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_upper_dragbrace_jxr_joint_j_14))
        _template_6_motion_ger_upper_dragbrace_jxr_joint_j_14 = get_object('.template_6_motion.ger_upper_dragbrace.jxr_joint_j_14')
        jxr_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_upper_dragbrace_jxr_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_14.location, jxr_joint_i_14.orientation)
        jxr_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_dragbrace.jxr_joint_i_14', exc)

    try:
        jxr_joint_i_10 = get_object('.template_6_motion.ger_lower_dragbrace.jxr_joint_i_10')
        relative_to = get_object('.template_6_motion.ger_lower_dragbrace')
        jxr_joint_i_10.relative_to = relative_to
        jxr_joint_i_10.marker_name = target_path('.template_6_motion.ger_lower_dragbrace.jxr_joint_i_10')
        _template_6_motion_ger_uc_collar_jxr_joint_j_10 = get_object('.template_6_motion.ger_uc_collar.jxr_joint_j_10')
        jxr_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_uc_collar_jxr_joint_j_10))
        _template_6_motion_ger_uc_collar_jxr_joint_j_10 = get_object('.template_6_motion.ger_uc_collar.jxr_joint_j_10')
        jxr_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_uc_collar_jxr_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_10.location, jxr_joint_i_10.orientation)
        jxr_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_dragbrace.jxr_joint_i_10', exc)

    try:
        gralin_lower_dragbrace = get_object('.template_6_motion.ger_lower_dragbrace.gralin_lower_dragbrace')
        gralin_lower_dragbrace.cylinder_name = target_path('.template_6_motion.ger_lower_dragbrace.gralin_lower_dragbrace')
        _template_6_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_udb_atch_1').location
        _template_6_motion_ground_hpr_ldb_collar_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_collar_atch_1').location
        gralin_lower_dragbrace.length = (VecUtils.DM(_template_6_motion_ground_hpr_ldb_udb_atch_1, _template_6_motion_ground_hpr_ldb_collar_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_lower_dragbrace.gralin_lower_dragbrace', exc)

    try:
        gralin_11 = get_object('.template_6_motion.gel_upper_torquearm.gralin_11')
        relative_to = get_object('.template_6_motion.gel_upper_torquearm')
        gralin_11.relative_to = relative_to
        gralin_11.marker_name = target_path('.template_6_motion.gel_upper_torquearm.gralin_11')
        _template_6_motion_ground_hpl_uta_collar_atch_1 = get_object('.template_6_motion.ground.hpl_uta_collar_atch_1')
        gralin_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_uta_collar_atch_1))
        _template_6_motion_ground_hpl_uta_collar_atch_1 = get_object('.template_6_motion.ground.hpl_uta_collar_atch_1').location
        _template_6_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_1').location
        gralin_11.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_uta_collar_atch_1, _template_6_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_11.location, gralin_11.orientation)
        gralin_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_torquearm.gralin_11', exc)

    try:
        jxl_joint_i_2 = get_object('.template_6_motion.gel_upper_torquearm.jxl_joint_i_2')
        relative_to = get_object('.template_6_motion.gel_upper_torquearm')
        jxl_joint_i_2.relative_to = relative_to
        jxl_joint_i_2.marker_name = target_path('.template_6_motion.gel_upper_torquearm.jxl_joint_i_2')
        _template_6_motion_gel_connector_jxl_joint_j_2 = get_object('.template_6_motion.gel_connector.jxl_joint_j_2')
        jxl_joint_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_connector_jxl_joint_j_2))
        _template_6_motion_gel_connector_jxl_joint_j_2 = get_object('.template_6_motion.gel_connector.jxl_joint_j_2')
        jxl_joint_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_connector_jxl_joint_j_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_2.location, jxl_joint_i_2.orientation)
        jxl_joint_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_torquearm.jxl_joint_i_2', exc)

    try:
        jxl_joint_i_3 = get_object('.template_6_motion.gel_upper_torquearm.jxl_joint_i_3')
        relative_to = get_object('.template_6_motion.gel_upper_torquearm')
        jxl_joint_i_3.relative_to = relative_to
        jxl_joint_i_3.marker_name = target_path('.template_6_motion.gel_upper_torquearm.jxl_joint_i_3')
        _template_6_motion_gel_uc_collar_jxl_joint_j_3 = get_object('.template_6_motion.gel_uc_collar.jxl_joint_j_3')
        jxl_joint_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_uc_collar_jxl_joint_j_3))
        _template_6_motion_gel_uc_collar_jxl_joint_j_3 = get_object('.template_6_motion.gel_uc_collar.jxl_joint_j_3')
        jxl_joint_i_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_uc_collar_jxl_joint_j_3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_3.location, jxl_joint_i_3.orientation)
        jxl_joint_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upper_torquearm.jxl_joint_i_3', exc)

    try:
        gralin_upper_torquearm = get_object('.template_6_motion.gel_upper_torquearm.gralin_upper_torquearm')
        gralin_upper_torquearm.cylinder_name = target_path('.template_6_motion.gel_upper_torquearm.gralin_upper_torquearm')
        _template_6_motion_ground_hpl_uta_collar_atch_1 = get_object('.template_6_motion.ground.hpl_uta_collar_atch_1').location
        _template_6_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_1').location
        gralin_upper_torquearm.length = (VecUtils.DM(_template_6_motion_ground_hpl_uta_collar_atch_1, _template_6_motion_ground_hpl_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_upper_torquearm.gralin_upper_torquearm', exc)

    try:
        gralin_28 = get_object('.template_6_motion.ger_upper_torquearm.gralin_28')
        relative_to = get_object('.template_6_motion.ger_upper_torquearm')
        gralin_28.relative_to = relative_to
        gralin_28.marker_name = target_path('.template_6_motion.ger_upper_torquearm.gralin_28')
        _template_6_motion_ground_hpr_uta_collar_atch_1 = get_object('.template_6_motion.ground.hpr_uta_collar_atch_1')
        gralin_28.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_uta_collar_atch_1))
        _template_6_motion_ground_hpr_uta_collar_atch_1 = get_object('.template_6_motion.ground.hpr_uta_collar_atch_1').location
        _template_6_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_1').location
        gralin_28.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_uta_collar_atch_1, _template_6_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_28.location, gralin_28.orientation)
        gralin_28.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_28.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_torquearm.gralin_28', exc)

    try:
        jxr_joint_i_2 = get_object('.template_6_motion.ger_upper_torquearm.jxr_joint_i_2')
        relative_to = get_object('.template_6_motion.ger_upper_torquearm')
        jxr_joint_i_2.relative_to = relative_to
        jxr_joint_i_2.marker_name = target_path('.template_6_motion.ger_upper_torquearm.jxr_joint_i_2')
        _template_6_motion_ger_connector_jxr_joint_j_2 = get_object('.template_6_motion.ger_connector.jxr_joint_j_2')
        jxr_joint_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_connector_jxr_joint_j_2))
        _template_6_motion_ger_connector_jxr_joint_j_2 = get_object('.template_6_motion.ger_connector.jxr_joint_j_2')
        jxr_joint_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_connector_jxr_joint_j_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_2.location, jxr_joint_i_2.orientation)
        jxr_joint_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_torquearm.jxr_joint_i_2', exc)

    try:
        jxr_joint_i_3 = get_object('.template_6_motion.ger_upper_torquearm.jxr_joint_i_3')
        relative_to = get_object('.template_6_motion.ger_upper_torquearm')
        jxr_joint_i_3.relative_to = relative_to
        jxr_joint_i_3.marker_name = target_path('.template_6_motion.ger_upper_torquearm.jxr_joint_i_3')
        _template_6_motion_ger_uc_collar_jxr_joint_j_3 = get_object('.template_6_motion.ger_uc_collar.jxr_joint_j_3')
        jxr_joint_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_uc_collar_jxr_joint_j_3))
        _template_6_motion_ger_uc_collar_jxr_joint_j_3 = get_object('.template_6_motion.ger_uc_collar.jxr_joint_j_3')
        jxr_joint_i_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_uc_collar_jxr_joint_j_3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_3.location, jxr_joint_i_3.orientation)
        jxr_joint_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upper_torquearm.jxr_joint_i_3', exc)

    try:
        gralin_upper_torquearm = get_object('.template_6_motion.ger_upper_torquearm.gralin_upper_torquearm')
        gralin_upper_torquearm.cylinder_name = target_path('.template_6_motion.ger_upper_torquearm.gralin_upper_torquearm')
        _template_6_motion_ground_hpr_uta_collar_atch_1 = get_object('.template_6_motion.ground.hpr_uta_collar_atch_1').location
        _template_6_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_1').location
        gralin_upper_torquearm.length = (VecUtils.DM(_template_6_motion_ground_hpr_uta_collar_atch_1, _template_6_motion_ground_hpr_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_upper_torquearm.gralin_upper_torquearm', exc)

    try:
        gralin_29 = get_object('.template_6_motion.gel_lower_torquearm.gralin_29')
        relative_to = get_object('.template_6_motion.gel_lower_torquearm')
        gralin_29.relative_to = relative_to
        gralin_29.marker_name = target_path('.template_6_motion.gel_lower_torquearm.gralin_29')
        _template_6_motion_ground_hpl_lta_lc_atch_1 = get_object('.template_6_motion.ground.hpl_lta_lc_atch_1')
        gralin_29.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_lta_lc_atch_1))
        _template_6_motion_ground_hpl_lta_lc_atch_1 = get_object('.template_6_motion.ground.hpl_lta_lc_atch_1').location
        _template_6_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_lta_connect_atch_1').location
        gralin_29.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_lta_lc_atch_1, _template_6_motion_ground_hpl_lta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_29.location, gralin_29.orientation)
        gralin_29.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_29.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_torquearm.gralin_29', exc)

    try:
        jxl_joint_i_11 = get_object('.template_6_motion.gel_lower_torquearm.jxl_joint_i_11')
        relative_to = get_object('.template_6_motion.gel_lower_torquearm')
        jxl_joint_i_11.relative_to = relative_to
        jxl_joint_i_11.marker_name = target_path('.template_6_motion.gel_lower_torquearm.jxl_joint_i_11')
        _template_6_motion_gel_lower_cylinder_jxl_joint_j_11 = get_object('.template_6_motion.gel_lower_cylinder.jxl_joint_j_11')
        jxl_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_lower_cylinder_jxl_joint_j_11))
        _template_6_motion_gel_lower_cylinder_jxl_joint_j_11 = get_object('.template_6_motion.gel_lower_cylinder.jxl_joint_j_11')
        jxl_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_lower_cylinder_jxl_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_11.location, jxl_joint_i_11.orientation)
        jxl_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_torquearm.jxl_joint_i_11', exc)

    try:
        jxl_joint_i_1 = get_object('.template_6_motion.gel_lower_torquearm.jxl_joint_i_1')
        relative_to = get_object('.template_6_motion.gel_lower_torquearm')
        jxl_joint_i_1.relative_to = relative_to
        jxl_joint_i_1.marker_name = target_path('.template_6_motion.gel_lower_torquearm.jxl_joint_i_1')
        _template_6_motion_gel_connector_jxl_joint_j_1 = get_object('.template_6_motion.gel_connector.jxl_joint_j_1')
        jxl_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_connector_jxl_joint_j_1))
        _template_6_motion_gel_connector_jxl_joint_j_1 = get_object('.template_6_motion.gel_connector.jxl_joint_j_1')
        jxl_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_connector_jxl_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_1.location, jxl_joint_i_1.orientation)
        jxl_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lower_torquearm.jxl_joint_i_1', exc)

    try:
        gralin_lower_torquearm = get_object('.template_6_motion.gel_lower_torquearm.gralin_lower_torquearm')
        gralin_lower_torquearm.cylinder_name = target_path('.template_6_motion.gel_lower_torquearm.gralin_lower_torquearm')
        _template_6_motion_ground_hpl_lta_lc_atch_1 = get_object('.template_6_motion.ground.hpl_lta_lc_atch_1').location
        _template_6_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_lta_connect_atch_1').location
        gralin_lower_torquearm.length = (VecUtils.DM(_template_6_motion_ground_hpl_lta_lc_atch_1, _template_6_motion_ground_hpl_lta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_lower_torquearm.gralin_lower_torquearm', exc)

    try:
        gralin_30 = get_object('.template_6_motion.ger_lower_torquearm.gralin_30')
        relative_to = get_object('.template_6_motion.ger_lower_torquearm')
        gralin_30.relative_to = relative_to
        gralin_30.marker_name = target_path('.template_6_motion.ger_lower_torquearm.gralin_30')
        _template_6_motion_ground_hpr_lta_lc_atch_1 = get_object('.template_6_motion.ground.hpr_lta_lc_atch_1')
        gralin_30.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_lta_lc_atch_1))
        _template_6_motion_ground_hpr_lta_lc_atch_1 = get_object('.template_6_motion.ground.hpr_lta_lc_atch_1').location
        _template_6_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_lta_connect_atch_1').location
        gralin_30.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_lta_lc_atch_1, _template_6_motion_ground_hpr_lta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_30.location, gralin_30.orientation)
        gralin_30.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_30.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_torquearm.gralin_30', exc)

    try:
        jxr_joint_i_11 = get_object('.template_6_motion.ger_lower_torquearm.jxr_joint_i_11')
        relative_to = get_object('.template_6_motion.ger_lower_torquearm')
        jxr_joint_i_11.relative_to = relative_to
        jxr_joint_i_11.marker_name = target_path('.template_6_motion.ger_lower_torquearm.jxr_joint_i_11')
        _template_6_motion_ger_lower_cylinder_jxr_joint_j_11 = get_object('.template_6_motion.ger_lower_cylinder.jxr_joint_j_11')
        jxr_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_lower_cylinder_jxr_joint_j_11))
        _template_6_motion_ger_lower_cylinder_jxr_joint_j_11 = get_object('.template_6_motion.ger_lower_cylinder.jxr_joint_j_11')
        jxr_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_lower_cylinder_jxr_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_11.location, jxr_joint_i_11.orientation)
        jxr_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_torquearm.jxr_joint_i_11', exc)

    try:
        jxr_joint_i_1 = get_object('.template_6_motion.ger_lower_torquearm.jxr_joint_i_1')
        relative_to = get_object('.template_6_motion.ger_lower_torquearm')
        jxr_joint_i_1.relative_to = relative_to
        jxr_joint_i_1.marker_name = target_path('.template_6_motion.ger_lower_torquearm.jxr_joint_i_1')
        _template_6_motion_ger_connector_jxr_joint_j_1 = get_object('.template_6_motion.ger_connector.jxr_joint_j_1')
        jxr_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_connector_jxr_joint_j_1))
        _template_6_motion_ger_connector_jxr_joint_j_1 = get_object('.template_6_motion.ger_connector.jxr_joint_j_1')
        jxr_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_connector_jxr_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_1.location, jxr_joint_i_1.orientation)
        jxr_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lower_torquearm.jxr_joint_i_1', exc)

    try:
        gralin_lower_torquearm = get_object('.template_6_motion.ger_lower_torquearm.gralin_lower_torquearm')
        gralin_lower_torquearm.cylinder_name = target_path('.template_6_motion.ger_lower_torquearm.gralin_lower_torquearm')
        _template_6_motion_ground_hpr_lta_lc_atch_1 = get_object('.template_6_motion.ground.hpr_lta_lc_atch_1').location
        _template_6_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_lta_connect_atch_1').location
        gralin_lower_torquearm.length = (VecUtils.DM(_template_6_motion_ground_hpr_lta_lc_atch_1, _template_6_motion_ground_hpr_lta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_lower_torquearm.gralin_lower_torquearm', exc)

    try:
        jxs_joint_j_17 = get_object('.template_6_motion.mts_body_mount_2.jxs_joint_j_17')
        relative_to = get_object('.template_6_motion.mts_body_mount_2')
        jxs_joint_j_17.relative_to = relative_to
        jxs_joint_j_17.marker_name = target_path('.template_6_motion.mts_body_mount_2.jxs_joint_j_17')
        _template_6_motion_ground_cfs_subframe_ref = get_object('.template_6_motion.ground.cfs_subframe_ref')
        jxs_joint_j_17.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfs_subframe_ref))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        jxs_joint_j_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_17.location, jxs_joint_j_17.orientation)
        jxs_joint_j_17.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_17.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.mts_body_mount_2.jxs_joint_j_17', exc)

    try:
        mts_body_mount_2 = get_object('.template_6_motion.mts_body_mount_2')
        mts_body_mount_2.part_name = target_path('.template_6_motion.mts_body_mount_2')
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        mts_body_mount_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('part modify rigid_body name_and_position .template_6_motion.mts_body_mount_2', exc)

    try:
        gralin_3 = get_object('.template_6_motion.gel_connector.gralin_3')
        relative_to = get_object('.template_6_motion.gel_connector')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_6_motion.gel_connector.gralin_3')
        _template_6_motion_ground_hpl_connect_1 = get_object('.template_6_motion.ground.hpl_connect_1')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_connect_1))
        _template_6_motion_ground_hpl_connect_1 = get_object('.template_6_motion.ground.hpl_connect_1').location
        _template_6_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_1').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_connect_1, _template_6_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_connector.gralin_3', exc)

    try:
        jxl_joint_j_1 = get_object('.template_6_motion.gel_connector.jxl_joint_j_1')
        relative_to = get_object('.template_6_motion.gel_connector')
        jxl_joint_j_1.relative_to = relative_to
        jxl_joint_j_1.marker_name = target_path('.template_6_motion.gel_connector.jxl_joint_j_1')
        _template_6_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_lta_connect_atch_1')
        jxl_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_lta_connect_atch_1))
        _template_6_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_lta_connect_atch_1').location
        _template_6_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_1').location
        jxl_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_lta_connect_atch_1, _template_6_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_1.location, jxl_joint_j_1.orientation)
        jxl_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_connector.jxl_joint_j_1', exc)

    try:
        jxl_joint_j_2 = get_object('.template_6_motion.gel_connector.jxl_joint_j_2')
        relative_to = get_object('.template_6_motion.gel_connector')
        jxl_joint_j_2.relative_to = relative_to
        jxl_joint_j_2.marker_name = target_path('.template_6_motion.gel_connector.jxl_joint_j_2')
        _template_6_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_1')
        jxl_joint_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_uta_connect_atch_1))
        _template_6_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_1').location
        _template_6_motion_ground_hpl_uta_connect_atch_2 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_2').location
        jxl_joint_j_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_uta_connect_atch_1, _template_6_motion_ground_hpl_uta_connect_atch_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_2.location, jxl_joint_j_2.orientation)
        jxl_joint_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_connector.jxl_joint_j_2', exc)

    try:
        gralin_connector = get_object('.template_6_motion.gel_connector.gralin_connector')
        gralin_connector.cylinder_name = target_path('.template_6_motion.gel_connector.gralin_connector')
        _template_6_motion_ground_hpl_connect_1 = get_object('.template_6_motion.ground.hpl_connect_1').location
        _template_6_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_1').location
        gralin_connector.length = (VecUtils.DM(_template_6_motion_ground_hpl_connect_1, _template_6_motion_ground_hpl_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_connector.gralin_connector', exc)

    try:
        gralin_4 = get_object('.template_6_motion.ger_connector.gralin_4')
        relative_to = get_object('.template_6_motion.ger_connector')
        gralin_4.relative_to = relative_to
        gralin_4.marker_name = target_path('.template_6_motion.ger_connector.gralin_4')
        _template_6_motion_ground_hpr_connect_1 = get_object('.template_6_motion.ground.hpr_connect_1')
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_connect_1))
        _template_6_motion_ground_hpr_connect_1 = get_object('.template_6_motion.ground.hpr_connect_1').location
        _template_6_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_1').location
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_connect_1, _template_6_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_connector.gralin_4', exc)

    try:
        jxr_joint_j_1 = get_object('.template_6_motion.ger_connector.jxr_joint_j_1')
        relative_to = get_object('.template_6_motion.ger_connector')
        jxr_joint_j_1.relative_to = relative_to
        jxr_joint_j_1.marker_name = target_path('.template_6_motion.ger_connector.jxr_joint_j_1')
        _template_6_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_lta_connect_atch_1')
        jxr_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_lta_connect_atch_1))
        _template_6_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_lta_connect_atch_1').location
        _template_6_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_1').location
        jxr_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_lta_connect_atch_1, _template_6_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_1.location, jxr_joint_j_1.orientation)
        jxr_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_connector.jxr_joint_j_1', exc)

    try:
        jxr_joint_j_2 = get_object('.template_6_motion.ger_connector.jxr_joint_j_2')
        relative_to = get_object('.template_6_motion.ger_connector')
        jxr_joint_j_2.relative_to = relative_to
        jxr_joint_j_2.marker_name = target_path('.template_6_motion.ger_connector.jxr_joint_j_2')
        _template_6_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_1')
        jxr_joint_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_uta_connect_atch_1))
        _template_6_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_1').location
        _template_6_motion_ground_hpr_uta_connect_atch_2 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_2').location
        jxr_joint_j_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_uta_connect_atch_1, _template_6_motion_ground_hpr_uta_connect_atch_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_2.location, jxr_joint_j_2.orientation)
        jxr_joint_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_connector.jxr_joint_j_2', exc)

    try:
        gralin_connector = get_object('.template_6_motion.ger_connector.gralin_connector')
        gralin_connector.cylinder_name = target_path('.template_6_motion.ger_connector.gralin_connector')
        _template_6_motion_ground_hpr_connect_1 = get_object('.template_6_motion.ground.hpr_connect_1').location
        _template_6_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_1').location
        gralin_connector.length = (VecUtils.DM(_template_6_motion_ground_hpr_connect_1, _template_6_motion_ground_hpr_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_connector.gralin_connector', exc)

    try:
        gralin_5 = get_object('.template_6_motion.gel_uc_collar.gralin_5')
        relative_to = get_object('.template_6_motion.gel_uc_collar')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_6_motion.gel_uc_collar.gralin_5')
        _template_6_motion_ground_cfl_collar_top = get_object('.template_6_motion.ground.cfl_collar_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfl_collar_top))
        _template_6_motion_ground_cfl_collar_top = get_object('.template_6_motion.ground.cfl_collar_top').location
        _template_6_motion_ground_cfl_collar_bot = get_object('.template_6_motion.ground.cfl_collar_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_cfl_collar_top, _template_6_motion_ground_cfl_collar_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_uc_collar.gralin_5', exc)

    try:
        jxl_joint_j_3 = get_object('.template_6_motion.gel_uc_collar.jxl_joint_j_3')
        relative_to = get_object('.template_6_motion.gel_uc_collar')
        jxl_joint_j_3.relative_to = relative_to
        jxl_joint_j_3.marker_name = target_path('.template_6_motion.gel_uc_collar.jxl_joint_j_3')
        _template_6_motion_ground_hpl_uta_collar_atch_1 = get_object('.template_6_motion.ground.hpl_uta_collar_atch_1')
        jxl_joint_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_uta_collar_atch_1))
        _template_6_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_lta_connect_atch_1').location
        _template_6_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpl_uta_connect_atch_1').location
        jxl_joint_j_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_lta_connect_atch_1, _template_6_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_3.location, jxl_joint_j_3.orientation)
        jxl_joint_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_uc_collar.jxl_joint_j_3', exc)

    try:
        jxl_joint_i_4 = get_object('.template_6_motion.gel_uc_collar.jxl_joint_i_4')
        relative_to = get_object('.template_6_motion.gel_uc_collar')
        jxl_joint_i_4.relative_to = relative_to
        jxl_joint_i_4.marker_name = target_path('.template_6_motion.gel_uc_collar.jxl_joint_i_4')
        _template_6_motion_gel_upper_cylinder_jxl_joint_j_4 = get_object('.template_6_motion.gel_upper_cylinder.jxl_joint_j_4')
        jxl_joint_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_upper_cylinder_jxl_joint_j_4))
        _template_6_motion_gel_upper_cylinder_jxl_joint_j_4 = get_object('.template_6_motion.gel_upper_cylinder.jxl_joint_j_4')
        jxl_joint_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_upper_cylinder_jxl_joint_j_4))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_4.location, jxl_joint_i_4.orientation)
        jxl_joint_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_uc_collar.jxl_joint_i_4', exc)

    try:
        jxl_joint_j_10 = get_object('.template_6_motion.gel_uc_collar.jxl_joint_j_10')
        relative_to = get_object('.template_6_motion.gel_uc_collar')
        jxl_joint_j_10.relative_to = relative_to
        jxl_joint_j_10.marker_name = target_path('.template_6_motion.gel_uc_collar.jxl_joint_j_10')
        _template_6_motion_ground_hpl_ldb_collar_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_collar_atch_1')
        jxl_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_ldb_collar_atch_1))
        _template_6_motion_ground_cfl_plane_ref_2 = get_object('.template_6_motion.ground.cfl_plane_ref_2')
        jxl_joint_j_10.orientation = _template_6_motion_ground_cfl_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_10.location, jxl_joint_j_10.orientation)
        jxl_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_uc_collar.jxl_joint_j_10', exc)

    try:
        gralin_uc_collar = get_object('.template_6_motion.gel_uc_collar.gralin_uc_collar')
        gralin_uc_collar.cylinder_name = target_path('.template_6_motion.gel_uc_collar.gralin_uc_collar')
        _template_6_motion_ground_cfl_collar_top = get_object('.template_6_motion.ground.cfl_collar_top').location
        _template_6_motion_ground_cfl_collar_bot = get_object('.template_6_motion.ground.cfl_collar_bot').location
        gralin_uc_collar.length = (VecUtils.DM(_template_6_motion_ground_cfl_collar_top, _template_6_motion_ground_cfl_collar_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_uc_collar.gralin_uc_collar', exc)

    try:
        gralin_6 = get_object('.template_6_motion.ger_uc_collar.gralin_6')
        relative_to = get_object('.template_6_motion.ger_uc_collar')
        gralin_6.relative_to = relative_to
        gralin_6.marker_name = target_path('.template_6_motion.ger_uc_collar.gralin_6')
        _template_6_motion_ground_cfr_collar_top = get_object('.template_6_motion.ground.cfr_collar_top')
        gralin_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfr_collar_top))
        _template_6_motion_ground_cfr_collar_top = get_object('.template_6_motion.ground.cfr_collar_top').location
        _template_6_motion_ground_cfr_collar_bot = get_object('.template_6_motion.ground.cfr_collar_bot').location
        gralin_6.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_cfr_collar_top, _template_6_motion_ground_cfr_collar_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_6.location, gralin_6.orientation)
        gralin_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_6.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_uc_collar.gralin_6', exc)

    try:
        jxr_joint_j_3 = get_object('.template_6_motion.ger_uc_collar.jxr_joint_j_3')
        relative_to = get_object('.template_6_motion.ger_uc_collar')
        jxr_joint_j_3.relative_to = relative_to
        jxr_joint_j_3.marker_name = target_path('.template_6_motion.ger_uc_collar.jxr_joint_j_3')
        _template_6_motion_ground_hpr_uta_collar_atch_1 = get_object('.template_6_motion.ground.hpr_uta_collar_atch_1')
        jxr_joint_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_uta_collar_atch_1))
        _template_6_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_lta_connect_atch_1').location
        _template_6_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_6_motion.ground.hpr_uta_connect_atch_1').location
        jxr_joint_j_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_lta_connect_atch_1, _template_6_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_3.location, jxr_joint_j_3.orientation)
        jxr_joint_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_uc_collar.jxr_joint_j_3', exc)

    try:
        jxr_joint_i_4 = get_object('.template_6_motion.ger_uc_collar.jxr_joint_i_4')
        relative_to = get_object('.template_6_motion.ger_uc_collar')
        jxr_joint_i_4.relative_to = relative_to
        jxr_joint_i_4.marker_name = target_path('.template_6_motion.ger_uc_collar.jxr_joint_i_4')
        _template_6_motion_ger_upper_cylinder_jxr_joint_j_4 = get_object('.template_6_motion.ger_upper_cylinder.jxr_joint_j_4')
        jxr_joint_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_upper_cylinder_jxr_joint_j_4))
        _template_6_motion_ger_upper_cylinder_jxr_joint_j_4 = get_object('.template_6_motion.ger_upper_cylinder.jxr_joint_j_4')
        jxr_joint_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_upper_cylinder_jxr_joint_j_4))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_4.location, jxr_joint_i_4.orientation)
        jxr_joint_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_uc_collar.jxr_joint_i_4', exc)

    try:
        jxr_joint_j_10 = get_object('.template_6_motion.ger_uc_collar.jxr_joint_j_10')
        relative_to = get_object('.template_6_motion.ger_uc_collar')
        jxr_joint_j_10.relative_to = relative_to
        jxr_joint_j_10.marker_name = target_path('.template_6_motion.ger_uc_collar.jxr_joint_j_10')
        _template_6_motion_ground_hpr_ldb_collar_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_collar_atch_1')
        jxr_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_ldb_collar_atch_1))
        _template_6_motion_ground_cfr_plane_ref_2 = get_object('.template_6_motion.ground.cfr_plane_ref_2')
        jxr_joint_j_10.orientation = _template_6_motion_ground_cfr_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_10.location, jxr_joint_j_10.orientation)
        jxr_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_uc_collar.jxr_joint_j_10', exc)

    try:
        gralin_uc_collar = get_object('.template_6_motion.ger_uc_collar.gralin_uc_collar')
        gralin_uc_collar.cylinder_name = target_path('.template_6_motion.ger_uc_collar.gralin_uc_collar')
        _template_6_motion_ground_cfr_collar_top = get_object('.template_6_motion.ground.cfr_collar_top').location
        _template_6_motion_ground_cfr_collar_bot = get_object('.template_6_motion.ground.cfr_collar_bot').location
        gralin_uc_collar.length = (VecUtils.DM(_template_6_motion_ground_cfr_collar_top, _template_6_motion_ground_cfr_collar_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_uc_collar.gralin_uc_collar', exc)

    try:
        gralin_7 = get_object('.template_6_motion.gel_spindle.gralin_7')
        relative_to = get_object('.template_6_motion.gel_spindle')
        gralin_7.relative_to = relative_to
        gralin_7.marker_name = target_path('.template_6_motion.gel_spindle.gralin_7')
        _template_6_motion_ground_hpl_spndl_sf_atch = get_object('.template_6_motion.ground.hpl_spndl_sf_atch')
        gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_spndl_sf_atch))
        _template_6_motion_ground_hpl_spndl_sf_atch = get_object('.template_6_motion.ground.hpl_spndl_sf_atch').location
        _template_6_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpl_udb_spndl_atch_1').location
        gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_spndl_sf_atch, _template_6_motion_ground_hpl_udb_spndl_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_spindle.gralin_7', exc)

    try:
        jxl_joint_j_5 = get_object('.template_6_motion.gel_spindle.jxl_joint_j_5')
        relative_to = get_object('.template_6_motion.gel_spindle')
        jxl_joint_j_5.relative_to = relative_to
        jxl_joint_j_5.marker_name = target_path('.template_6_motion.gel_spindle.jxl_joint_j_5')
        _template_6_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpl_udb_spndl_atch_1')
        jxl_joint_j_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_udb_spndl_atch_1))
        _template_6_motion_ground_hpl_spndl_sf_atch = get_object('.template_6_motion.ground.hpl_spndl_sf_atch').location
        _template_6_motion_gel_spindle_jxl_joint_j_5 = get_object('.template_6_motion.gel_spindle.jxl_joint_j_5').location
        _template_6_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpl_ldb_udb_atch_1').location
        jxl_joint_j_5.orientation = (VecUtils.ORI_IN_PLANE(_template_6_motion_ground_hpl_spndl_sf_atch, _template_6_motion_gel_spindle_jxl_joint_j_5, _template_6_motion_ground_hpl_ldb_udb_atch_1, "Z_ZX"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_5.location, jxl_joint_j_5.orientation)
        jxl_joint_j_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_spindle.jxl_joint_j_5', exc)

    try:
        jxl_joint_i_6 = get_object('.template_6_motion.gel_spindle.jxl_joint_i_6')
        relative_to = get_object('.template_6_motion.gel_spindle')
        jxl_joint_i_6.relative_to = relative_to
        jxl_joint_i_6.marker_name = target_path('.template_6_motion.gel_spindle.jxl_joint_i_6')
        _template_6_motion_ges_subframe_2_jxl_joint_j_6 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_6')
        jxl_joint_i_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxl_joint_j_6))
        _template_6_motion_ges_subframe_2_jxl_joint_j_6 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_6')
        jxl_joint_i_6.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxl_joint_j_6))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_6.location, jxl_joint_i_6.orientation)
        jxl_joint_i_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_6.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_spindle.jxl_joint_i_6', exc)

    try:
        gralin_spindle = get_object('.template_6_motion.gel_spindle.gralin_spindle')
        gralin_spindle.cylinder_name = target_path('.template_6_motion.gel_spindle.gralin_spindle')
        _template_6_motion_ground_hpl_spndl_sf_atch = get_object('.template_6_motion.ground.hpl_spndl_sf_atch').location
        _template_6_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpl_udb_spndl_atch_1').location
        gralin_spindle.length = (VecUtils.DM(_template_6_motion_ground_hpl_spndl_sf_atch, _template_6_motion_ground_hpl_udb_spndl_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_spindle.gralin_spindle', exc)

    try:
        gralin_8 = get_object('.template_6_motion.ger_spindle.gralin_8')
        relative_to = get_object('.template_6_motion.ger_spindle')
        gralin_8.relative_to = relative_to
        gralin_8.marker_name = target_path('.template_6_motion.ger_spindle.gralin_8')
        _template_6_motion_ground_hpr_spndl_sf_atch = get_object('.template_6_motion.ground.hpr_spndl_sf_atch')
        gralin_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_spndl_sf_atch))
        _template_6_motion_ground_hpr_spndl_sf_atch = get_object('.template_6_motion.ground.hpr_spndl_sf_atch').location
        _template_6_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpr_udb_spndl_atch_1').location
        gralin_8.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_spndl_sf_atch, _template_6_motion_ground_hpr_udb_spndl_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_8.location, gralin_8.orientation)
        gralin_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_spindle.gralin_8', exc)

    try:
        jxr_joint_j_5 = get_object('.template_6_motion.ger_spindle.jxr_joint_j_5')
        relative_to = get_object('.template_6_motion.ger_spindle')
        jxr_joint_j_5.relative_to = relative_to
        jxr_joint_j_5.marker_name = target_path('.template_6_motion.ger_spindle.jxr_joint_j_5')
        _template_6_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpr_udb_spndl_atch_1')
        jxr_joint_j_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_udb_spndl_atch_1))
        _template_6_motion_ground_hpr_spndl_sf_atch = get_object('.template_6_motion.ground.hpr_spndl_sf_atch').location
        _template_6_motion_ger_spindle_jxr_joint_j_5 = get_object('.template_6_motion.ger_spindle.jxr_joint_j_5').location
        _template_6_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_6_motion.ground.hpr_ldb_udb_atch_1').location
        jxr_joint_j_5.orientation = (VecUtils.ORI_IN_PLANE(_template_6_motion_ground_hpr_spndl_sf_atch, _template_6_motion_ger_spindle_jxr_joint_j_5, _template_6_motion_ground_hpr_ldb_udb_atch_1, "Z_ZX"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_5.location, jxr_joint_j_5.orientation)
        jxr_joint_j_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_spindle.jxr_joint_j_5', exc)

    try:
        jxr_joint_i_6 = get_object('.template_6_motion.ger_spindle.jxr_joint_i_6')
        relative_to = get_object('.template_6_motion.ger_spindle')
        jxr_joint_i_6.relative_to = relative_to
        jxr_joint_i_6.marker_name = target_path('.template_6_motion.ger_spindle.jxr_joint_i_6')
        _template_6_motion_ges_subframe_2_jxr_joint_j_6 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_6')
        jxr_joint_i_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxr_joint_j_6))
        _template_6_motion_ges_subframe_2_jxr_joint_j_6 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_6')
        jxr_joint_i_6.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxr_joint_j_6))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_6.location, jxr_joint_i_6.orientation)
        jxr_joint_i_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_6.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_spindle.jxr_joint_i_6', exc)

    try:
        gralin_spindle = get_object('.template_6_motion.ger_spindle.gralin_spindle')
        gralin_spindle.cylinder_name = target_path('.template_6_motion.ger_spindle.gralin_spindle')
        _template_6_motion_ground_hpr_spndl_sf_atch = get_object('.template_6_motion.ground.hpr_spndl_sf_atch').location
        _template_6_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_6_motion.ground.hpr_udb_spndl_atch_1').location
        gralin_spindle.length = (VecUtils.DM(_template_6_motion_ground_hpr_spndl_sf_atch, _template_6_motion_ground_hpr_udb_spndl_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_spindle.gralin_spindle', exc)

    try:
        gralin_9 = get_object('.template_6_motion.gel_lwract.gralin_9')
        relative_to = get_object('.template_6_motion.gel_lwract')
        gralin_9.relative_to = relative_to
        gralin_9.marker_name = target_path('.template_6_motion.gel_lwract.gralin_9')
        _template_6_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpl_lwract_uc_atch_1')
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_lwract_uc_atch_1))
        _template_6_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpl_lwract_uc_atch_1').location
        _template_6_motion_ground_cfl_lwract_top = get_object('.template_6_motion.ground.cfl_lwract_top').location
        gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_lwract_uc_atch_1, _template_6_motion_ground_cfl_lwract_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lwract.gralin_9', exc)

    try:
        jxl_joint_j_7 = get_object('.template_6_motion.gel_lwract.jxl_joint_j_7')
        relative_to = get_object('.template_6_motion.gel_lwract')
        jxl_joint_j_7.relative_to = relative_to
        jxl_joint_j_7.marker_name = target_path('.template_6_motion.gel_lwract.jxl_joint_j_7')
        _template_6_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpl_lwract_uc_atch_1')
        jxl_joint_j_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpl_lwract_uc_atch_1))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        jxl_joint_j_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_7.location, jxl_joint_j_7.orientation)
        jxl_joint_j_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lwract.jxl_joint_j_7', exc)

    try:
        jxl_joint_i_8 = get_object('.template_6_motion.gel_lwract.jxl_joint_i_8')
        relative_to = get_object('.template_6_motion.gel_lwract')
        jxl_joint_i_8.relative_to = relative_to
        jxl_joint_i_8.marker_name = target_path('.template_6_motion.gel_lwract.jxl_joint_i_8')
        _template_6_motion_gel_upract_jxl_joint_j_8 = get_object('.template_6_motion.gel_upract.jxl_joint_j_8')
        jxl_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_upract_jxl_joint_j_8))
        _template_6_motion_gel_upract_jxl_joint_j_8 = get_object('.template_6_motion.gel_upract.jxl_joint_j_8')
        jxl_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_gel_upract_jxl_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_8.location, jxl_joint_i_8.orientation)
        jxl_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_lwract.jxl_joint_i_8', exc)

    try:
        gralin_lwract = get_object('.template_6_motion.gel_lwract.gralin_lwract')
        gralin_lwract.cylinder_name = target_path('.template_6_motion.gel_lwract.gralin_lwract')
        _template_6_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpl_lwract_uc_atch_1').location
        _template_6_motion_ground_cfl_lwract_top = get_object('.template_6_motion.ground.cfl_lwract_top').location
        gralin_lwract.length = (VecUtils.DM(_template_6_motion_ground_hpl_lwract_uc_atch_1, _template_6_motion_ground_cfl_lwract_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_lwract.gralin_lwract', exc)

    try:
        gralin_10 = get_object('.template_6_motion.ger_lwract.gralin_10')
        relative_to = get_object('.template_6_motion.ger_lwract')
        gralin_10.relative_to = relative_to
        gralin_10.marker_name = target_path('.template_6_motion.ger_lwract.gralin_10')
        _template_6_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpr_lwract_uc_atch_1')
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_lwract_uc_atch_1))
        _template_6_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpr_lwract_uc_atch_1').location
        _template_6_motion_ground_cfr_lwract_top = get_object('.template_6_motion.ground.cfr_lwract_top').location
        gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_lwract_uc_atch_1, _template_6_motion_ground_cfr_lwract_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lwract.gralin_10', exc)

    try:
        jxr_joint_j_7 = get_object('.template_6_motion.ger_lwract.jxr_joint_j_7')
        relative_to = get_object('.template_6_motion.ger_lwract')
        jxr_joint_j_7.relative_to = relative_to
        jxr_joint_j_7.marker_name = target_path('.template_6_motion.ger_lwract.jxr_joint_j_7')
        _template_6_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpr_lwract_uc_atch_1')
        jxr_joint_j_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_hpr_lwract_uc_atch_1))
        _template_6_motion_ground_origo1 = get_object('.template_6_motion.ground.origo1')
        jxr_joint_j_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_7.location, jxr_joint_j_7.orientation)
        jxr_joint_j_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lwract.jxr_joint_j_7', exc)

    try:
        jxr_joint_i_8 = get_object('.template_6_motion.ger_lwract.jxr_joint_i_8')
        relative_to = get_object('.template_6_motion.ger_lwract')
        jxr_joint_i_8.relative_to = relative_to
        jxr_joint_i_8.marker_name = target_path('.template_6_motion.ger_lwract.jxr_joint_i_8')
        _template_6_motion_ger_upract_jxr_joint_j_8 = get_object('.template_6_motion.ger_upract.jxr_joint_j_8')
        jxr_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_upract_jxr_joint_j_8))
        _template_6_motion_ger_upract_jxr_joint_j_8 = get_object('.template_6_motion.ger_upract.jxr_joint_j_8')
        jxr_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ger_upract_jxr_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_8.location, jxr_joint_i_8.orientation)
        jxr_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_lwract.jxr_joint_i_8', exc)

    try:
        gralin_lwract = get_object('.template_6_motion.ger_lwract.gralin_lwract')
        gralin_lwract.cylinder_name = target_path('.template_6_motion.ger_lwract.gralin_lwract')
        _template_6_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpr_lwract_uc_atch_1').location
        _template_6_motion_ground_cfr_lwract_top = get_object('.template_6_motion.ground.cfr_lwract_top').location
        gralin_lwract.length = (VecUtils.DM(_template_6_motion_ground_hpr_lwract_uc_atch_1, _template_6_motion_ground_cfr_lwract_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_lwract.gralin_lwract', exc)

    try:
        gralin_18 = get_object('.template_6_motion.gel_upract.gralin_18')
        relative_to = get_object('.template_6_motion.gel_upract')
        gralin_18.relative_to = relative_to
        gralin_18.marker_name = target_path('.template_6_motion.gel_upract.gralin_18')
        _template_6_motion_ground_cfl_upract_bot = get_object('.template_6_motion.ground.cfl_upract_bot')
        gralin_18.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfl_upract_bot))
        _template_6_motion_ground_cfl_upract_bot = get_object('.template_6_motion.ground.cfl_upract_bot').location
        _template_6_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpl_upract_sf_atch_1').location
        gralin_18.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_cfl_upract_bot, _template_6_motion_ground_hpl_upract_sf_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_18.location, gralin_18.orientation)
        gralin_18.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_18.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upract.gralin_18', exc)

    try:
        jxl_joint_j_8 = get_object('.template_6_motion.gel_upract.jxl_joint_j_8')
        relative_to = get_object('.template_6_motion.gel_upract')
        jxl_joint_j_8.relative_to = relative_to
        jxl_joint_j_8.marker_name = target_path('.template_6_motion.gel_upract.jxl_joint_j_8')
        _template_6_motion_ground_cfl_lwract_top = get_object('.template_6_motion.ground.cfl_lwract_top')
        jxl_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfl_lwract_top))
        _template_6_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpl_lwract_uc_atch_1').location
        _template_6_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpl_upract_sf_atch_1').location
        jxl_joint_j_8.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpl_lwract_uc_atch_1, _template_6_motion_ground_hpl_upract_sf_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_8.location, jxl_joint_j_8.orientation)
        jxl_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upract.jxl_joint_j_8', exc)

    try:
        jxl_joint_i_17 = get_object('.template_6_motion.gel_upract.jxl_joint_i_17')
        relative_to = get_object('.template_6_motion.gel_upract')
        jxl_joint_i_17.relative_to = relative_to
        jxl_joint_i_17.marker_name = target_path('.template_6_motion.gel_upract.jxl_joint_i_17')
        _template_6_motion_ges_subframe_2_jxl_joint_j_17 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_17')
        jxl_joint_i_17.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxl_joint_j_17))
        _template_6_motion_ges_subframe_2_jxl_joint_j_17 = get_object('.template_6_motion.ges_subframe_2.jxl_joint_j_17')
        jxl_joint_i_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxl_joint_j_17))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_17.location, jxl_joint_i_17.orientation)
        jxl_joint_i_17.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_17.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.gel_upract.jxl_joint_i_17', exc)

    try:
        gralin_upract = get_object('.template_6_motion.gel_upract.gralin_upract')
        gralin_upract.cylinder_name = target_path('.template_6_motion.gel_upract.gralin_upract')
        _template_6_motion_ground_cfl_upract_bot = get_object('.template_6_motion.ground.cfl_upract_bot').location
        _template_6_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpl_upract_sf_atch_1').location
        gralin_upract.length = (VecUtils.DM(_template_6_motion_ground_cfl_upract_bot, _template_6_motion_ground_hpl_upract_sf_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.gel_upract.gralin_upract', exc)

    try:
        gralin_19 = get_object('.template_6_motion.ger_upract.gralin_19')
        relative_to = get_object('.template_6_motion.ger_upract')
        gralin_19.relative_to = relative_to
        gralin_19.marker_name = target_path('.template_6_motion.ger_upract.gralin_19')
        _template_6_motion_ground_cfr_upract_bot = get_object('.template_6_motion.ground.cfr_upract_bot')
        gralin_19.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfr_upract_bot))
        _template_6_motion_ground_cfr_upract_bot = get_object('.template_6_motion.ground.cfr_upract_bot').location
        _template_6_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpr_upract_sf_atch_1').location
        gralin_19.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_cfr_upract_bot, _template_6_motion_ground_hpr_upract_sf_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_19.location, gralin_19.orientation)
        gralin_19.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_19.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upract.gralin_19', exc)

    try:
        jxr_joint_j_8 = get_object('.template_6_motion.ger_upract.jxr_joint_j_8')
        relative_to = get_object('.template_6_motion.ger_upract')
        jxr_joint_j_8.relative_to = relative_to
        jxr_joint_j_8.marker_name = target_path('.template_6_motion.ger_upract.jxr_joint_j_8')
        _template_6_motion_ground_cfr_lwract_top = get_object('.template_6_motion.ground.cfr_lwract_top')
        jxr_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ground_cfr_lwract_top))
        _template_6_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_6_motion.ground.hpr_lwract_uc_atch_1').location
        _template_6_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpr_upract_sf_atch_1').location
        jxr_joint_j_8.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_motion_ground_hpr_lwract_uc_atch_1, _template_6_motion_ground_hpr_upract_sf_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_8.location, jxr_joint_j_8.orientation)
        jxr_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upract.jxr_joint_j_8', exc)

    try:
        jxr_joint_i_17 = get_object('.template_6_motion.ger_upract.jxr_joint_i_17')
        relative_to = get_object('.template_6_motion.ger_upract')
        jxr_joint_i_17.relative_to = relative_to
        jxr_joint_i_17.marker_name = target_path('.template_6_motion.ger_upract.jxr_joint_i_17')
        _template_6_motion_ges_subframe_2_jxr_joint_j_17 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_17')
        jxr_joint_i_17.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxr_joint_j_17))
        _template_6_motion_ges_subframe_2_jxr_joint_j_17 = get_object('.template_6_motion.ges_subframe_2.jxr_joint_j_17')
        jxr_joint_i_17.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_motion_ges_subframe_2_jxr_joint_j_17))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_17.location, jxr_joint_i_17.orientation)
        jxr_joint_i_17.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_17.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_motion.ger_upract.jxr_joint_i_17', exc)

    try:
        gralin_upract = get_object('.template_6_motion.ger_upract.gralin_upract')
        gralin_upract.cylinder_name = target_path('.template_6_motion.ger_upract.gralin_upract')
        _template_6_motion_ground_cfr_upract_bot = get_object('.template_6_motion.ground.cfr_upract_bot').location
        _template_6_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_6_motion.ground.hpr_upract_sf_atch_1').location
        gralin_upract.length = (VecUtils.DM(_template_6_motion_ground_cfr_upract_bot, _template_6_motion_ground_hpr_upract_sf_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_motion.ger_upract.gralin_upract', exc)

    return {'updated': updated, 'warnings': warnings, 'errors': errors}

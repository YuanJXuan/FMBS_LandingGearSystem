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

SOURCE_MODEL_NAME = 'template_2_drop'
ADM_UDE_KINDS = {'lumian': 'road', 'lumian_2': 'road', 'luntai1_2': 'tire', 'luntai2_2': 'tire'}

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
        node = get_or_create('DataElementVariable', '.template_2_drop.NLG_V')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_drop.NLG_V')
        if hasattr(node, 'adams_id'):
            node.adams_id = 115
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_drop.NLG_V', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_2_drop.NLG_S')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_drop.NLG_S')
        if hasattr(node, 'adams_id'):
            node.adams_id = 120
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_drop.NLG_S', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_2_drop.x1')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_drop.x1')
        if hasattr(node, 'adams_id'):
            node.adams_id = 121
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_drop.x1', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_2_drop.x2')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_drop.x2')
        if hasattr(node, 'adams_id'):
            node.adams_id = 122
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_drop.x2', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_2_drop.VARIABLE_123')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_drop.VARIABLE_123')
        if hasattr(node, 'adams_id'):
            node.adams_id = 123
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_drop.VARIABLE_123', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_2_drop.VARIABLE_124')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_drop.VARIABLE_124')
        if hasattr(node, 'adams_id'):
            node.adams_id = 124
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_drop.VARIABLE_124', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_2_drop._cv_solver_variable')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_drop._cv_solver_variable')
        if hasattr(node, 'adams_id'):
            node.adams_id = 1
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_drop._cv_solver_variable', exc)

    try:
        node = get_or_create('SimuScript', '.template_2_drop.Last_Sim')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_2_drop.Last_Sim')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=2.0 number_of_steps=400 model_name=.GCMB')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_2_drop.Last_Sim', exc)

    try:
        node = get_object('.template_2_drop.NLG_V')
        node.function = rewrite_expression('-1*VR(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_drop.NLG_V', exc)

    try:
        node = get_object('.template_2_drop.NLG_S')
        node.function = rewrite_expression('428.6-DM(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_drop.NLG_S', exc)

    try:
        node = get_object('.template_2_drop.x1')
        node.function = rewrite_expression('-1*(VARVAL(.template_2_drop.NLG_V)*0.5*(VARVAL(.template_2_drop.NLG_V)-ABS(VARVAL(.template_2_drop.NLG_V)))*((.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_MAIN_OIL**3/(2*.template_2_drop.NLG_MAIN_Cd**2*.template_2_drop.NLG_A_MAIN_NEG**2))+(.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_RET_OIL**3/(2*.template_2_drop.NLG_RET_Cd**2*.template_2_drop.NLG_A_RET_NEG**2))))')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_drop.x1', exc)

    try:
        node = get_object('.template_2_drop.x2')
        node.function = rewrite_expression('0.00001*VARVAL(.template_2_drop.NLG_V)*0.5*(VARVAL(.template_2_drop.NLG_V)+ABS(VARVAL(.template_2_drop.NLG_V)))*((.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_MAIN_OIL**3/(2*.template_2_drop.NLG_MAIN_Cd**2*.template_2_drop.NLG_A_MAIN_POS**2))+(.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_RET_OIL**3/(2*.template_2_drop.NLG_RET_Cd**2*.template_2_drop.NLG_A_RET_POS**2)))')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_drop.x2', exc)

    try:
        node = get_object('.template_2_drop.VARIABLE_123')
        node.function = rewrite_expression('IF(TIME:0,1,2)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_drop.VARIABLE_123', exc)

    try:
        node = get_object('.template_2_drop.VARIABLE_124')
        node.function = rewrite_expression('VARVAL(.template_2_drop.NLG_V)-ABS(VARVAL(.template_2_drop.NLG_V))')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_drop.VARIABLE_124', exc)

    try:
        node = get_object('.template_2_drop._cv_solver_variable')
        node.function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_drop._cv_solver_variable', exc)

    try:
        node = get_object('.template_2_drop.hcqwy')
        node.function = rewrite_expression('428.6-DZ(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1)')
        updated += 1

    except Exception as exc:
        record_error('measure modify function .template_2_drop.hcqwy', exc)

    try:
        node = get_object('.template_2_drop.cxzh')
        node.function = rewrite_expression('.template_2_drop.luntai1_2.vertical_force_iso+.template_2_drop.luntai2_2.vertical_force_iso')
        updated += 1

    except Exception as exc:
        record_error('measure modify function .template_2_drop.cxzh', exc)

    try:
        node = get_object('.template_2_drop._cv_diff')
        node.function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('part modify equation differential_equation .template_2_drop._cv_diff', exc)

    try:
        node = get_object('.template_2_drop.NLG_AIR')
        node.function = rewrite_expression('1*.template_2_drop.NLG_A_LOW*(.template_2_drop.NLG_P_LOW*(.template_2_drop.NLG_V_LOW/(.template_2_drop.NLG_V_LOW-.template_2_drop.NLG_A_LOW*(428.6-DM(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1))))**1.1-.template_2_drop.Patm)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_drop.NLG_AIR', exc)

    try:
        node = get_object('.template_2_drop.NLG_OIL')
        node.function = rewrite_expression('IF(VARVAL(.template_2_drop.NLG_V):-0.001*(VARVAL(.template_2_drop.NLG_V)*0.5*(VARVAL(.template_2_drop.NLG_V)-ABS(VARVAL(.template_2_drop.NLG_V)))*((.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_MAIN_OIL**3/(2*.template_2_drop.NLG_MAIN_Cd**2*.template_2_drop.NLG_A_MAIN_NEG**2))+(.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_RET_OIL**3/(2*.template_2_drop.NLG_RET_Cd**2*.template_2_drop.NLG_A_RET_NEG**2)))),0,0.001*VARVAL(.template_2_drop.NLG_V)*0.5*(VARVAL(.template_2_drop.NLG_V)+ABS(VARVAL(.template_2_drop.NLG_V)))*((.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_MAIN_OIL**3/(2*.template_2_drop.NLG_MAIN_Cd**2*.template_2_drop.NLG_A_MAIN_POS**2))+(.template_2_drop.NLG_rho_Oil*.template_2_drop.NLG_A_RET_OIL**3/(2*.template_2_drop.NLG_RET_Cd**2*.template_2_drop.NLG_A_RET_POS**2))))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_drop.NLG_OIL', exc)

    try:
        node = get_object('.template_2_drop.NLG_STOP')
        node.function = rewrite_expression('IF(428.6-DM(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1) :1.0E+09*(428.6-DM(.template_2_drop.ges_upper_cylinder.MARKER_2,.template_2_drop.ges_lower_cylinder.MARKER_1)), 0 , 0 )')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_drop.NLG_STOP', exc)

    try:
        uel_gearaero_origin_1 = get_object('.template_2_drop.ground.uel_gearaero_origin_1')
        uel_gearaero_origin_1.marker_name = target_path('.template_2_drop.ground.uel_gearaero_origin_1')
        _template_2_drop_ground_origo = get_object('.template_2_drop.ground.origo')
        uel_gearaero_origin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_origo))
        _template_2_drop_ground_origo = get_object('.template_2_drop.ground.origo')
        uel_gearaero_origin_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ground.uel_gearaero_origin_1', exc)

    try:
        uer_gearaero_origin_1 = get_object('.template_2_drop.ground.uer_gearaero_origin_1')
        uer_gearaero_origin_1.marker_name = target_path('.template_2_drop.ground.uer_gearaero_origin_1')
        _template_2_drop_ground_origo = get_object('.template_2_drop.ground.origo')
        uer_gearaero_origin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_origo))
        _template_2_drop_ground_origo = get_object('.template_2_drop.ground.origo')
        uer_gearaero_origin_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ground.uer_gearaero_origin_1', exc)

    try:
        cfl_spin_axis1 = get_object('.template_2_drop.ground.cfl_spin_axis1')
        cfl_spin_axis1.marker_name = target_path('.template_2_drop.ground.cfl_spin_axis1')
        _template_2_drop_ground_hpl_wheel_center1 = get_object('.template_2_drop.ground.hpl_wheel_center1')
        cfl_spin_axis1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hpl_wheel_center1))
        _template_2_drop_ground_hpl_wheel_center1 = get_object('.template_2_drop.ground.hpl_wheel_center1').location
        _template_2_drop_ground_hpl_ob_axle1 = get_object('.template_2_drop.ground.hpl_ob_axle1').location
        cfl_spin_axis1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hpl_wheel_center1, _template_2_drop_ground_hpl_ob_axle1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ground.cfl_spin_axis1', exc)

    try:
        cfr_spin_axis1 = get_object('.template_2_drop.ground.cfr_spin_axis1')
        cfr_spin_axis1.marker_name = target_path('.template_2_drop.ground.cfr_spin_axis1')
        _template_2_drop_ground_hpr_wheel_center1 = get_object('.template_2_drop.ground.hpr_wheel_center1')
        cfr_spin_axis1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hpr_wheel_center1))
        _template_2_drop_ground_hpr_wheel_center1 = get_object('.template_2_drop.ground.hpr_wheel_center1').location
        _template_2_drop_ground_hpr_ob_axle1 = get_object('.template_2_drop.ground.hpr_ob_axle1').location
        cfr_spin_axis1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hpr_wheel_center1, _template_2_drop_ground_hpr_ob_axle1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ground.cfr_spin_axis1', exc)

    try:
        cfs_nlg_axle_lowpoint = get_object('.template_2_drop.ground.cfs_nlg_axle_lowpoint')
        cfs_nlg_axle_lowpoint.marker_name = target_path('.template_2_drop.ground.cfs_nlg_axle_lowpoint')
        _template_2_drop_ground_hps_nlg_axle_lowpoint = get_object('.template_2_drop.ground.hps_nlg_axle_lowpoint')
        cfs_nlg_axle_lowpoint.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_nlg_axle_lowpoint))
        _template_2_drop_ground_origo1 = get_object('.template_2_drop.ground.origo1')
        cfs_nlg_axle_lowpoint.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ground.cfs_nlg_axle_lowpoint', exc)

    try:
        cfs_collar_top = get_object('.template_2_drop.ground.cfs_collar_top')
        cfs_collar_top.marker_name = target_path('.template_2_drop.ground.cfs_collar_top')
        _template_2_drop_ground_hps_uc_bot = get_object('.template_2_drop.ground.hps_uc_bot').location
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top').location
        cfs_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_2_drop_ground_hps_uc_bot, _template_2_drop_ground_hps_uc_top, 0.11 * VecUtils.DM(_template_2_drop_ground_hps_uc_bot, _template_2_drop_ground_hps_uc_top)))
        _template_2_drop_ground_hps_uc_bot = get_object('.template_2_drop.ground.hps_uc_bot').location
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top').location
        cfs_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_uc_bot, _template_2_drop_ground_hps_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ground.cfs_collar_top', exc)

    try:
        inertia_frame = get_object('.template_2_drop.ges_dragbrace.inertia_frame')
        relative_to = get_object('.template_2_drop.ges_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_drop.ges_dragbrace.inertia_frame')
        _template_2_drop_ges_dragbrace_cm = get_object('.template_2_drop.ges_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_dragbrace_cm))
        _template_2_drop_ges_dragbrace = get_object('.template_2_drop.ges_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_dragbrace.inertia_frame', exc)

    try:
        gralin_1 = get_object('.template_2_drop.ges_dragbrace.gralin_1')
        relative_to = get_object('.template_2_drop.ges_dragbrace')
        gralin_1.relative_to = relative_to
        gralin_1.marker_name = target_path('.template_2_drop.ges_dragbrace.gralin_1')
        _template_2_drop_ground_hps_db_sf_atch = get_object('.template_2_drop.ground.hps_db_sf_atch')
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_db_sf_atch))
        _template_2_drop_ground_hps_db_sf_atch = get_object('.template_2_drop.ground.hps_db_sf_atch').location
        _template_2_drop_ground_hps_db_uc_atch = get_object('.template_2_drop.ground.hps_db_uc_atch').location
        gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_db_sf_atch, _template_2_drop_ground_hps_db_uc_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_dragbrace.gralin_1', exc)

    try:
        jxs_joint_i_12 = get_object('.template_2_drop.ges_dragbrace.jxs_joint_i_12')
        relative_to = get_object('.template_2_drop.ges_dragbrace')
        jxs_joint_i_12.relative_to = relative_to
        jxs_joint_i_12.marker_name = target_path('.template_2_drop.ges_dragbrace.jxs_joint_i_12')
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_12 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_12')
        jxs_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_12))
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_12 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_12')
        jxs_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_12.location, jxs_joint_i_12.orientation)
        jxs_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_dragbrace.jxs_joint_i_12', exc)

    try:
        gralin_dragbrace_geom = get_object('.template_2_drop.ges_dragbrace.gralin_dragbrace_geom')
        gralin_dragbrace_geom.cylinder_name = target_path('.template_2_drop.ges_dragbrace.gralin_dragbrace_geom')
        _template_2_drop_ground_hps_db_sf_atch = get_object('.template_2_drop.ground.hps_db_sf_atch').location
        _template_2_drop_ground_hps_db_uc_atch = get_object('.template_2_drop.ground.hps_db_uc_atch').location
        gralin_dragbrace_geom.length = (VecUtils.DM(_template_2_drop_ground_hps_db_sf_atch, _template_2_drop_ground_hps_db_uc_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_drop.ges_dragbrace.gralin_dragbrace_geom', exc)

    try:
        MARKER_428 = get_object('.template_2_drop.ges_upper_cylinder.MARKER_428')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        MARKER_428.relative_to = relative_to
        MARKER_428.marker_name = target_path('.template_2_drop.ges_upper_cylinder.MARKER_428')
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top')
        MARKER_428.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_428.location, MARKER_428.orientation)
        MARKER_428.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.MARKER_428', exc)

    try:
        inertia_frame = get_object('.template_2_drop.ges_upper_cylinder.inertia_frame')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_drop.ges_upper_cylinder.inertia_frame')
        _template_2_drop_ges_upper_cylinder_cm = get_object('.template_2_drop.ges_upper_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_cm))
        _template_2_drop_ges_upper_cylinder = get_object('.template_2_drop.ges_upper_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.inertia_frame', exc)

    try:
        gralin_2 = get_object('.template_2_drop.ges_upper_cylinder.gralin_2')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        gralin_2.relative_to = relative_to
        gralin_2.marker_name = target_path('.template_2_drop.ges_upper_cylinder.gralin_2')
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top')
        gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_top))
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top').location
        _template_2_drop_ground_hps_uc_bot = get_object('.template_2_drop.ground.hps_uc_bot').location
        gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_uc_top, _template_2_drop_ground_hps_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_2.location, gralin_2.orientation)
        gralin_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.gralin_2', exc)

    try:
        gralin_3 = get_object('.template_2_drop.ges_upper_cylinder.gralin_3')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_2_drop.ges_upper_cylinder.gralin_3')
        _template_2_drop_ground_hps_uc_sf_atch_l = get_object('.template_2_drop.ground.hps_uc_sf_atch_l')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_sf_atch_l))
        _template_2_drop_ground_hps_uc_sf_atch_l = get_object('.template_2_drop.ground.hps_uc_sf_atch_l').location
        _template_2_drop_ground_hps_uc_geompt = get_object('.template_2_drop.ground.hps_uc_geompt').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_uc_sf_atch_l, _template_2_drop_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.gralin_3', exc)

    try:
        gralin_4 = get_object('.template_2_drop.ges_upper_cylinder.gralin_4')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        gralin_4.relative_to = relative_to
        gralin_4.marker_name = target_path('.template_2_drop.ges_upper_cylinder.gralin_4')
        _template_2_drop_ground_hps_uc_sf_atch_r = get_object('.template_2_drop.ground.hps_uc_sf_atch_r')
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_sf_atch_r))
        _template_2_drop_ground_hps_uc_sf_atch_r = get_object('.template_2_drop.ground.hps_uc_sf_atch_r').location
        _template_2_drop_ground_hps_uc_geompt = get_object('.template_2_drop.ground.hps_uc_geompt').location
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_uc_sf_atch_r, _template_2_drop_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.gralin_4', exc)

    try:
        jxs_joint_j_12 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_12')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        jxs_joint_j_12.relative_to = relative_to
        jxs_joint_j_12.marker_name = target_path('.template_2_drop.ges_upper_cylinder.jxs_joint_j_12')
        _template_2_drop_ground_hps_db_uc_atch = get_object('.template_2_drop.ground.hps_db_uc_atch')
        jxs_joint_j_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_db_uc_atch))
        _template_2_drop_ground_origo1 = get_object('.template_2_drop.ground.origo1')
        jxs_joint_j_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_12.location, jxs_joint_j_12.orientation)
        jxs_joint_j_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.jxs_joint_j_12', exc)

    try:
        ues_spring_j_1 = get_object('.template_2_drop.ges_upper_cylinder.ues_spring_j_1')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        ues_spring_j_1.relative_to = relative_to
        ues_spring_j_1.marker_name = target_path('.template_2_drop.ges_upper_cylinder.ues_spring_j_1')
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top')
        ues_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_j_1.location, ues_spring_j_1.orientation)
        ues_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.ues_spring_j_1', exc)

    try:
        ues_damper_j_1 = get_object('.template_2_drop.ges_upper_cylinder.ues_damper_j_1')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        ues_damper_j_1.relative_to = relative_to
        ues_damper_j_1.marker_name = target_path('.template_2_drop.ges_upper_cylinder.ues_damper_j_1')
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top')
        ues_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_j_1.location, ues_damper_j_1.orientation)
        ues_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.ues_damper_j_1', exc)

    try:
        ues_stopper_j_1 = get_object('.template_2_drop.ges_upper_cylinder.ues_stopper_j_1')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        ues_stopper_j_1.relative_to = relative_to
        ues_stopper_j_1.marker_name = target_path('.template_2_drop.ges_upper_cylinder.ues_stopper_j_1')
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top')
        ues_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_j_1.location, ues_stopper_j_1.orientation)
        ues_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.ues_stopper_j_1', exc)

    try:
        jxs_joint_j_1 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_1')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        jxs_joint_j_1.relative_to = relative_to
        jxs_joint_j_1.marker_name = target_path('.template_2_drop.ges_upper_cylinder.jxs_joint_j_1')
        _template_2_drop_ground_cfs_collar_top = get_object('.template_2_drop.ground.cfs_collar_top')
        jxs_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_cfs_collar_top))
        _template_2_drop_ground_hps_uc_bot = get_object('.template_2_drop.ground.hps_uc_bot').location
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top').location
        jxs_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_uc_bot, _template_2_drop_ground_hps_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
        jxs_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.jxs_joint_j_1', exc)

    try:
        ues_actuator_j_1 = get_object('.template_2_drop.ges_upper_cylinder.ues_actuator_j_1')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        ues_actuator_j_1.relative_to = relative_to
        ues_actuator_j_1.marker_name = target_path('.template_2_drop.ges_upper_cylinder.ues_actuator_j_1')
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_1.location, ues_actuator_j_1.orientation)
        ues_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.ues_actuator_j_1', exc)

    try:
        ues_actuator_j_4 = get_object('.template_2_drop.ges_upper_cylinder.ues_actuator_j_4')
        relative_to = get_object('.template_2_drop.ges_upper_cylinder')
        ues_actuator_j_4.relative_to = relative_to
        ues_actuator_j_4.marker_name = target_path('.template_2_drop.ges_upper_cylinder.ues_actuator_j_4')
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_4.location, ues_actuator_j_4.orientation)
        ues_actuator_j_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_j_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_cylinder.ues_actuator_j_4', exc)

    try:
        gralin_upper_cylinder_geom1 = get_object('.template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        gralin_upper_cylinder_geom1.cylinder_name = target_path('.template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top').location
        _template_2_drop_ground_hps_uc_bot = get_object('.template_2_drop.ground.hps_uc_bot').location
        gralin_upper_cylinder_geom1.length = (VecUtils.DM(_template_2_drop_ground_hps_uc_top, _template_2_drop_ground_hps_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom1', exc)

    try:
        gralin_upper_cylinder_geom2 = get_object('.template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        gralin_upper_cylinder_geom2.cylinder_name = target_path('.template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        _template_2_drop_ground_hps_uc_sf_atch_l = get_object('.template_2_drop.ground.hps_uc_sf_atch_l').location
        _template_2_drop_ground_hps_uc_geompt = get_object('.template_2_drop.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom2.length = (VecUtils.DM(_template_2_drop_ground_hps_uc_sf_atch_l, _template_2_drop_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom2', exc)

    try:
        gralin_upper_cylinder_geom3 = get_object('.template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        gralin_upper_cylinder_geom3.cylinder_name = target_path('.template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        _template_2_drop_ground_hps_uc_sf_atch_r = get_object('.template_2_drop.ground.hps_uc_sf_atch_r').location
        _template_2_drop_ground_hps_uc_geompt = get_object('.template_2_drop.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom3.length = (VecUtils.DM(_template_2_drop_ground_hps_uc_sf_atch_r, _template_2_drop_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_drop.ges_upper_cylinder.gralin_upper_cylinder_geom3', exc)

    try:
        MARKER_378 = get_object('.template_2_drop.ges_lower_cylinder.MARKER_378')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        MARKER_378.relative_to = relative_to
        MARKER_378.marker_name = target_path('.template_2_drop.ges_lower_cylinder.MARKER_378')
        _template_2_drop_ground_hps_lta_lc_atch = get_object('.template_2_drop.ground.hps_lta_lc_atch')
        MARKER_378.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_lta_lc_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_378.location, MARKER_378.orientation)
        MARKER_378.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.MARKER_378', exc)

    try:
        inertia_frame = get_object('.template_2_drop.ges_lower_cylinder.inertia_frame')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_drop.ges_lower_cylinder.inertia_frame')
        _template_2_drop_ges_lower_cylinder_cm = get_object('.template_2_drop.ges_lower_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_lower_cylinder_cm))
        _template_2_drop_ges_lower_cylinder = get_object('.template_2_drop.ges_lower_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_lower_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.inertia_frame', exc)

    try:
        gralin_5 = get_object('.template_2_drop.ges_lower_cylinder.gralin_5')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_2_drop.ges_lower_cylinder.gralin_5')
        _template_2_drop_ground_hps_lc_top = get_object('.template_2_drop.ground.hps_lc_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_lc_top))
        _template_2_drop_ground_hps_lc_top = get_object('.template_2_drop.ground.hps_lc_top').location
        _template_2_drop_ground_hps_lc_bot = get_object('.template_2_drop.ground.hps_lc_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_lc_top, _template_2_drop_ground_hps_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.gralin_5', exc)

    try:
        jxs_joint_i_11 = get_object('.template_2_drop.ges_lower_cylinder.jxs_joint_i_11')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        jxs_joint_i_11.relative_to = relative_to
        jxs_joint_i_11.marker_name = target_path('.template_2_drop.ges_lower_cylinder.jxs_joint_i_11')
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_11))
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
        jxs_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.jxs_joint_i_11', exc)

    try:
        gralin_7 = get_object('.template_2_drop.ges_lower_cylinder.gralin_7')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        gralin_7.relative_to = relative_to
        gralin_7.marker_name = target_path('.template_2_drop.ges_lower_cylinder.gralin_7')
        _template_2_drop_ground_hpr_wheel_center1 = get_object('.template_2_drop.ground.hpr_wheel_center1')
        gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hpr_wheel_center1))
        _template_2_drop_ground_hpr_wheel_center1 = get_object('.template_2_drop.ground.hpr_wheel_center1').location
        _template_2_drop_ground_hpl_wheel_center1 = get_object('.template_2_drop.ground.hpl_wheel_center1').location
        gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hpr_wheel_center1, _template_2_drop_ground_hpl_wheel_center1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.gralin_7', exc)

    try:
        ues_spring_i_1 = get_object('.template_2_drop.ges_lower_cylinder.ues_spring_i_1')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        ues_spring_i_1.relative_to = relative_to
        ues_spring_i_1.marker_name = target_path('.template_2_drop.ges_lower_cylinder.ues_spring_i_1')
        _template_2_drop_ground_hps_lc_top = get_object('.template_2_drop.ground.hps_lc_top')
        ues_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_i_1.location, ues_spring_i_1.orientation)
        ues_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.ues_spring_i_1', exc)

    try:
        ues_damper_i_1 = get_object('.template_2_drop.ges_lower_cylinder.ues_damper_i_1')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        ues_damper_i_1.relative_to = relative_to
        ues_damper_i_1.marker_name = target_path('.template_2_drop.ges_lower_cylinder.ues_damper_i_1')
        _template_2_drop_ground_hps_lc_top = get_object('.template_2_drop.ground.hps_lc_top')
        ues_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_i_1.location, ues_damper_i_1.orientation)
        ues_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.ues_damper_i_1', exc)

    try:
        ues_stopper_i_1 = get_object('.template_2_drop.ges_lower_cylinder.ues_stopper_i_1')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        ues_stopper_i_1.relative_to = relative_to
        ues_stopper_i_1.marker_name = target_path('.template_2_drop.ges_lower_cylinder.ues_stopper_i_1')
        _template_2_drop_ground_hps_lc_top = get_object('.template_2_drop.ground.hps_lc_top')
        ues_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_i_1.location, ues_stopper_i_1.orientation)
        ues_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.ues_stopper_i_1', exc)

    try:
        coomarker_2 = get_object('.template_2_drop.ges_lower_cylinder.coomarker_2')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        coomarker_2.relative_to = relative_to
        coomarker_2.marker_name = target_path('.template_2_drop.ges_lower_cylinder.coomarker_2')
        _template_2_drop_ground_cfs_wheel_centers_midpoint = get_object('.template_2_drop.ground.cfs_wheel_centers_midpoint')
        coomarker_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_cfs_wheel_centers_midpoint))
        _template_2_drop_ground_cfs_wheel_centers_midpoint = get_object('.template_2_drop.ground.cfs_wheel_centers_midpoint')
        coomarker_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_cfs_wheel_centers_midpoint))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_2.location, coomarker_2.orientation)
        coomarker_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.coomarker_2', exc)

    try:
        coomarker_3 = get_object('.template_2_drop.ges_lower_cylinder.coomarker_3')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        coomarker_3.relative_to = relative_to
        coomarker_3.marker_name = target_path('.template_2_drop.ges_lower_cylinder.coomarker_3')
        _template_2_drop_ground_cfs_nlg_axle_lowpoint = get_object('.template_2_drop.ground.cfs_nlg_axle_lowpoint')
        coomarker_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_cfs_nlg_axle_lowpoint))
        _template_2_drop_ground_cfs_nlg_axle_lowpoint = get_object('.template_2_drop.ground.cfs_nlg_axle_lowpoint')
        coomarker_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_cfs_nlg_axle_lowpoint))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_3.location, coomarker_3.orientation)
        coomarker_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.coomarker_3', exc)

    try:
        MARKER_3 = get_object('.template_2_drop.ges_lower_cylinder.MARKER_3')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        MARKER_3.relative_to = relative_to
        MARKER_3.marker_name = target_path('.template_2_drop.ges_lower_cylinder.MARKER_3')
        _template_2_drop_ground_hpl_wheel_center1 = get_object('.template_2_drop.ground.hpl_wheel_center1')
        MARKER_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hpl_wheel_center1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_3.location, MARKER_3.orientation)
        MARKER_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.MARKER_3', exc)

    try:
        MARKER_4 = get_object('.template_2_drop.ges_lower_cylinder.MARKER_4')
        relative_to = get_object('.template_2_drop.ges_lower_cylinder')
        MARKER_4.relative_to = relative_to
        MARKER_4.marker_name = target_path('.template_2_drop.ges_lower_cylinder.MARKER_4')
        _template_2_drop_ground_hpr_wheel_center1 = get_object('.template_2_drop.ground.hpr_wheel_center1')
        MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hpr_wheel_center1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_4.location, MARKER_4.orientation)
        MARKER_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_cylinder.MARKER_4', exc)

    try:
        gralin_geom1 = get_object('.template_2_drop.ges_lower_cylinder.gralin_geom1')
        gralin_geom1.cylinder_name = target_path('.template_2_drop.ges_lower_cylinder.gralin_geom1')
        _template_2_drop_ground_hps_lc_top = get_object('.template_2_drop.ground.hps_lc_top').location
        _template_2_drop_ground_hps_lc_bot = get_object('.template_2_drop.ground.hps_lc_bot').location
        gralin_geom1.length = (VecUtils.DM(_template_2_drop_ground_hps_lc_top, _template_2_drop_ground_hps_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_drop.ges_lower_cylinder.gralin_geom1', exc)

    try:
        gralin_geom2 = get_object('.template_2_drop.ges_lower_cylinder.gralin_geom2')
        gralin_geom2.cylinder_name = target_path('.template_2_drop.ges_lower_cylinder.gralin_geom2')
        _template_2_drop_ground_hpr_wheel_center1 = get_object('.template_2_drop.ground.hpr_wheel_center1').location
        _template_2_drop_ground_hpl_wheel_center1 = get_object('.template_2_drop.ground.hpl_wheel_center1').location
        gralin_geom2.length = (VecUtils.DM(_template_2_drop_ground_hpr_wheel_center1, _template_2_drop_ground_hpl_wheel_center1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_drop.ges_lower_cylinder.gralin_geom2', exc)

    try:
        inertia_frame = get_object('.template_2_drop.ges_upper_torque_arm.inertia_frame')
        relative_to = get_object('.template_2_drop.ges_upper_torque_arm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_drop.ges_upper_torque_arm.inertia_frame')
        _template_2_drop_ges_upper_torque_arm_cm = get_object('.template_2_drop.ges_upper_torque_arm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_torque_arm_cm))
        _template_2_drop_ges_upper_torque_arm = get_object('.template_2_drop.ges_upper_torque_arm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_torque_arm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_torque_arm.inertia_frame', exc)

    try:
        gralin_9 = get_object('.template_2_drop.ges_upper_torque_arm.gralin_9')
        relative_to = get_object('.template_2_drop.ges_upper_torque_arm')
        gralin_9.relative_to = relative_to
        gralin_9.marker_name = target_path('.template_2_drop.ges_upper_torque_arm.gralin_9')
        _template_2_drop_ground_hps_uta_uc_atch = get_object('.template_2_drop.ground.hps_uta_uc_atch')
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uta_uc_atch))
        _template_2_drop_ground_hps_uta_uc_atch = get_object('.template_2_drop.ground.hps_uta_uc_atch').location
        _template_2_drop_ground_hps_lta_uta_atch = get_object('.template_2_drop.ground.hps_lta_uta_atch').location
        gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_uta_uc_atch, _template_2_drop_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_torque_arm.gralin_9', exc)

    try:
        jxs_joint_j_8 = get_object('.template_2_drop.ges_upper_torque_arm.jxs_joint_j_8')
        relative_to = get_object('.template_2_drop.ges_upper_torque_arm')
        jxs_joint_j_8.relative_to = relative_to
        jxs_joint_j_8.marker_name = target_path('.template_2_drop.ges_upper_torque_arm.jxs_joint_j_8')
        _template_2_drop_ground_hps_lta_uta_atch = get_object('.template_2_drop.ground.hps_lta_uta_atch')
        jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_lta_uta_atch))
        _template_2_drop_ground_origo1 = get_object('.template_2_drop.ground.origo1')
        jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_2_drop_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
        jxs_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_torque_arm.jxs_joint_j_8', exc)

    try:
        jxs_joint_i_10 = get_object('.template_2_drop.ges_upper_torque_arm.jxs_joint_i_10')
        relative_to = get_object('.template_2_drop.ges_upper_torque_arm')
        jxs_joint_i_10.relative_to = relative_to
        jxs_joint_i_10.marker_name = target_path('.template_2_drop.ges_upper_torque_arm.jxs_joint_i_10')
        _template_2_drop_ges_collar_jxs_joint_j_10 = get_object('.template_2_drop.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_collar_jxs_joint_j_10))
        _template_2_drop_ges_collar_jxs_joint_j_10 = get_object('.template_2_drop.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_collar_jxs_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
        jxs_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_upper_torque_arm.jxs_joint_i_10', exc)

    try:
        gralin_upper_torque_arm_geom = get_object('.template_2_drop.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        gralin_upper_torque_arm_geom.cylinder_name = target_path('.template_2_drop.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        _template_2_drop_ground_hps_uta_uc_atch = get_object('.template_2_drop.ground.hps_uta_uc_atch').location
        _template_2_drop_ground_hps_lta_uta_atch = get_object('.template_2_drop.ground.hps_lta_uta_atch').location
        gralin_upper_torque_arm_geom.length = (VecUtils.DM(_template_2_drop_ground_hps_uta_uc_atch, _template_2_drop_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_drop.ges_upper_torque_arm.gralin_upper_torque_arm_geom', exc)

    try:
        MARKER_379 = get_object('.template_2_drop.ges_lower_torque_arm.MARKER_379')
        relative_to = get_object('.template_2_drop.ges_lower_torque_arm')
        MARKER_379.relative_to = relative_to
        MARKER_379.marker_name = target_path('.template_2_drop.ges_lower_torque_arm.MARKER_379')
        _template_2_drop_ground_hps_lta_lc_atch = get_object('.template_2_drop.ground.hps_lta_lc_atch')
        MARKER_379.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_lta_lc_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_379.location, MARKER_379.orientation)
        MARKER_379.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_torque_arm.MARKER_379', exc)

    try:
        inertia_frame = get_object('.template_2_drop.ges_lower_torque_arm.inertia_frame')
        relative_to = get_object('.template_2_drop.ges_lower_torque_arm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_drop.ges_lower_torque_arm.inertia_frame')
        _template_2_drop_ges_lower_torque_arm_cm = get_object('.template_2_drop.ges_lower_torque_arm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_lower_torque_arm_cm))
        _template_2_drop_ges_lower_torque_arm = get_object('.template_2_drop.ges_lower_torque_arm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_lower_torque_arm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_torque_arm.inertia_frame', exc)

    try:
        jxs_joint_i_8 = get_object('.template_2_drop.ges_lower_torque_arm.jxs_joint_i_8')
        relative_to = get_object('.template_2_drop.ges_lower_torque_arm')
        jxs_joint_i_8.relative_to = relative_to
        jxs_joint_i_8.marker_name = target_path('.template_2_drop.ges_lower_torque_arm.jxs_joint_i_8')
        _template_2_drop_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_2_drop.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_torque_arm_jxs_joint_j_8))
        _template_2_drop_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_2_drop.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_torque_arm_jxs_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
        jxs_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_torque_arm.jxs_joint_i_8', exc)

    try:
        gralin_10 = get_object('.template_2_drop.ges_lower_torque_arm.gralin_10')
        relative_to = get_object('.template_2_drop.ges_lower_torque_arm')
        gralin_10.relative_to = relative_to
        gralin_10.marker_name = target_path('.template_2_drop.ges_lower_torque_arm.gralin_10')
        _template_2_drop_ground_hps_lta_lc_atch = get_object('.template_2_drop.ground.hps_lta_lc_atch')
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_lta_lc_atch))
        _template_2_drop_ground_hps_lta_lc_atch = get_object('.template_2_drop.ground.hps_lta_lc_atch').location
        _template_2_drop_ground_hps_lta_uta_atch = get_object('.template_2_drop.ground.hps_lta_uta_atch').location
        gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_lta_lc_atch, _template_2_drop_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_lower_torque_arm.gralin_10', exc)

    try:
        gralin_lower_torque_arm_geom = get_object('.template_2_drop.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        gralin_lower_torque_arm_geom.cylinder_name = target_path('.template_2_drop.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        _template_2_drop_ground_hps_lta_lc_atch = get_object('.template_2_drop.ground.hps_lta_lc_atch').location
        _template_2_drop_ground_hps_lta_uta_atch = get_object('.template_2_drop.ground.hps_lta_uta_atch').location
        gralin_lower_torque_arm_geom.length = (VecUtils.DM(_template_2_drop_ground_hps_lta_lc_atch, _template_2_drop_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_drop.ges_lower_torque_arm.gralin_lower_torque_arm_geom', exc)

    try:
        inertia_frame = get_object('.template_2_drop.ges_subframe_2.inertia_frame')
        relative_to = get_object('.template_2_drop.ges_subframe_2')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_drop.ges_subframe_2.inertia_frame')
        _template_2_drop_ges_subframe_2_cm = get_object('.template_2_drop.ges_subframe_2.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_subframe_2_cm))
        _template_2_drop_ges_subframe_2 = get_object('.template_2_drop.ges_subframe_2')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_subframe_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_subframe_2.inertia_frame', exc)

    try:
        graout_1 = get_object('.template_2_drop.ges_subframe_2.graout_1')
        relative_to = get_object('.template_2_drop.ges_subframe_2')
        graout_1.relative_to = relative_to
        graout_1.marker_name = target_path('.template_2_drop.ges_subframe_2.graout_1')
        _template_2_drop_ground_hps_uc_sf_atch_r = get_object('.template_2_drop.ground.hps_uc_sf_atch_r')
        graout_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_sf_atch_r))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_1.location, graout_1.orientation)
        graout_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_subframe_2.graout_1', exc)

    try:
        graout_2 = get_object('.template_2_drop.ges_subframe_2.graout_2')
        relative_to = get_object('.template_2_drop.ges_subframe_2')
        graout_2.relative_to = relative_to
        graout_2.marker_name = target_path('.template_2_drop.ges_subframe_2.graout_2')
        _template_2_drop_ground_hps_uc_sf_atch_l = get_object('.template_2_drop.ground.hps_uc_sf_atch_l')
        graout_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_sf_atch_l))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_2.location, graout_2.orientation)
        graout_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_subframe_2.graout_2', exc)

    try:
        graout_3 = get_object('.template_2_drop.ges_subframe_2.graout_3')
        relative_to = get_object('.template_2_drop.ges_subframe_2')
        graout_3.relative_to = relative_to
        graout_3.marker_name = target_path('.template_2_drop.ges_subframe_2.graout_3')
        _template_2_drop_ground_hps_db_sf_atch = get_object('.template_2_drop.ground.hps_db_sf_atch')
        graout_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_db_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_3.location, graout_3.orientation)
        graout_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_subframe_2.graout_3', exc)

    try:
        MARKER_427 = get_object('.template_2_drop.mts_body_mount_2.MARKER_427')
        relative_to = get_object('.template_2_drop.mts_body_mount_2')
        MARKER_427.relative_to = relative_to
        MARKER_427.marker_name = target_path('.template_2_drop.mts_body_mount_2.MARKER_427')
        _template_2_drop_ground_hps_uc_top = get_object('.template_2_drop.ground.hps_uc_top')
        MARKER_427.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_427.location, MARKER_427.orientation)
        MARKER_427.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.mts_body_mount_2.MARKER_427', exc)

    try:
        mts_body_mount_2 = get_object('.template_2_drop.mts_body_mount_2')
        mts_body_mount_2.part_name = target_path('.template_2_drop.mts_body_mount_2')
        _template_2_drop_ground_cfs_subframe_to_body_point = get_object('.template_2_drop.ground.cfs_subframe_to_body_point')
        mts_body_mount_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_cfs_subframe_to_body_point))
        _template_2_drop_ground_origo1 = get_object('.template_2_drop.ground.origo1')
        mts_body_mount_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('part modify rigid_body name_and_position .template_2_drop.mts_body_mount_2', exc)

    try:
        jxs_joint_j_10 = get_object('.template_2_drop.ges_collar.jxs_joint_j_10')
        relative_to = get_object('.template_2_drop.ges_collar')
        jxs_joint_j_10.relative_to = relative_to
        jxs_joint_j_10.marker_name = target_path('.template_2_drop.ges_collar.jxs_joint_j_10')
        _template_2_drop_ground_hps_uta_uc_atch = get_object('.template_2_drop.ground.hps_uta_uc_atch')
        jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uta_uc_atch))
        _template_2_drop_ground_origo1 = get_object('.template_2_drop.ground.origo1')
        jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_2_drop_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
        jxs_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_collar.jxs_joint_j_10', exc)

    try:
        inertia_frame = get_object('.template_2_drop.ges_collar.inertia_frame')
        relative_to = get_object('.template_2_drop.ges_collar')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_drop.ges_collar.inertia_frame')
        _template_2_drop_ges_collar_cm = get_object('.template_2_drop.ges_collar.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_collar_cm))
        _template_2_drop_ges_collar = get_object('.template_2_drop.ges_collar')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_collar))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_collar.inertia_frame', exc)

    try:
        gralin_24 = get_object('.template_2_drop.ges_collar.gralin_24')
        relative_to = get_object('.template_2_drop.ges_collar')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_2_drop.ges_collar.gralin_24')
        _template_2_drop_ground_hps_uc_bot = get_object('.template_2_drop.ground.hps_uc_bot')
        gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ground_hps_uc_bot))
        _template_2_drop_ground_hps_uc_bot = get_object('.template_2_drop.ground.hps_uc_bot').location
        _template_2_drop_ground_cfs_collar_top = get_object('.template_2_drop.ground.cfs_collar_top').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_drop_ground_hps_uc_bot, _template_2_drop_ground_cfs_collar_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_collar.gralin_24', exc)

    try:
        jxs_joint_i_1 = get_object('.template_2_drop.ges_collar.jxs_joint_i_1')
        relative_to = get_object('.template_2_drop.ges_collar')
        jxs_joint_i_1.relative_to = relative_to
        jxs_joint_i_1.marker_name = target_path('.template_2_drop.ges_collar.jxs_joint_i_1')
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_drop_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_drop.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
        jxs_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_collar.jxs_joint_i_1', exc)

    try:
        ues_actuator_i_1 = get_object('.template_2_drop.ges_collar.ues_actuator_i_1')
        relative_to = get_object('.template_2_drop.ges_collar')
        ues_actuator_i_1.relative_to = relative_to
        ues_actuator_i_1.marker_name = target_path('.template_2_drop.ges_collar.ues_actuator_i_1')
        _template_2_drop_ges_collar_jxs_joint_i_1 = get_object('.template_2_drop.ges_collar.jxs_joint_i_1')
        ues_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_collar_jxs_joint_i_1))
        _template_2_drop_ges_collar_jxs_joint_i_1 = get_object('.template_2_drop.ges_collar.jxs_joint_i_1')
        ues_actuator_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_collar_jxs_joint_i_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_1.location, ues_actuator_i_1.orientation)
        ues_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_collar.ues_actuator_i_1', exc)

    try:
        ues_actuator_i_4 = get_object('.template_2_drop.ges_collar.ues_actuator_i_4')
        relative_to = get_object('.template_2_drop.ges_collar')
        ues_actuator_i_4.relative_to = relative_to
        ues_actuator_i_4.marker_name = target_path('.template_2_drop.ges_collar.ues_actuator_i_4')
        _template_2_drop_ges_collar_jxs_joint_i_1 = get_object('.template_2_drop.ges_collar.jxs_joint_i_1')
        ues_actuator_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_collar_jxs_joint_i_1))
        _template_2_drop_ges_collar_jxs_joint_i_1 = get_object('.template_2_drop.ges_collar.jxs_joint_i_1')
        ues_actuator_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_drop_ges_collar_jxs_joint_i_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_4.location, ues_actuator_i_4.orientation)
        ues_actuator_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.ges_collar.ues_actuator_i_4', exc)

    try:
        gralin_collar = get_object('.template_2_drop.ges_collar.gralin_collar')
        gralin_collar.cylinder_name = target_path('.template_2_drop.ges_collar.gralin_collar')
        _template_2_drop_ground_hps_uc_bot = get_object('.template_2_drop.ground.hps_uc_bot').location
        _template_2_drop_ground_cfs_collar_top = get_object('.template_2_drop.ground.cfs_collar_top').location
        gralin_collar.length = (VecUtils.DM(_template_2_drop_ground_hps_uc_bot, _template_2_drop_ground_cfs_collar_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_drop.ges_collar.gralin_collar', exc)

    try:
        gfo_i = get_object('.template_2_drop.luntai1_2.wheel_part.gfo_i')
        relative_to = get_object('.template_2_drop.luntai1_2.wheel_part')
        gfo_i.relative_to = relative_to
        gfo_i.marker_name = target_path('.template_2_drop.luntai1_2.wheel_part.gfo_i')
        _template_2_drop_luntai1_2_wheel_part_wheel_cm = get_object('.template_2_drop.luntai1_2.wheel_part.wheel_cm')
        gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _template_2_drop_luntai1_2_wheel_part_wheel_cm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
        gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.luntai1_2.wheel_part.gfo_i', exc)

    try:
        gfo_i = get_object('.template_2_drop.luntai2_2.wheel_part.gfo_i')
        relative_to = get_object('.template_2_drop.luntai2_2.wheel_part')
        gfo_i.relative_to = relative_to
        gfo_i.marker_name = target_path('.template_2_drop.luntai2_2.wheel_part.gfo_i')
        _template_2_drop_luntai2_2_wheel_part_wheel_cm = get_object('.template_2_drop.luntai2_2.wheel_part.wheel_cm')
        gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _template_2_drop_luntai2_2_wheel_part_wheel_cm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
        gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_drop.luntai2_2.wheel_part.gfo_i', exc)

    if model_dir is None:
        model_dir = os.path.dirname(os.path.abspath(__file__))
    resource_path_1 = os.path.abspath(os.path.join(model_dir, 'NLG.tir'))
    if not os.path.isfile(resource_path_1):
        record_error('轮胎文件路径（NLG.tir）', FileNotFoundError(resource_path_1))
    else:
        try:
            if set_resource('.template_2_drop.luntai1_2.tpf_file', resource_path_1):
                updated += 1
        except Exception as exc:
            record_error('轮胎文件路径（NLG.tir）', exc)
    resource_path_2 = os.path.abspath(os.path.join(model_dir, '2d_flat.rdf'))
    if not os.path.isfile(resource_path_2):
        record_error('路面文件路径（2d_flat.rdf）', FileNotFoundError(resource_path_2))
    else:
        try:
            if set_resource('.template_2_drop.luntai1_2.rpf_file', resource_path_2):
                updated += 1
        except Exception as exc:
            record_error('路面文件路径（2d_flat.rdf）', exc)
    resource_path_3 = os.path.abspath(os.path.join(model_dir, 'NLG.tir'))
    if not os.path.isfile(resource_path_3):
        record_error('轮胎文件路径（NLG.tir）', FileNotFoundError(resource_path_3))
    else:
        try:
            if set_resource('.template_2_drop.luntai2_2.tpf_file', resource_path_3):
                updated += 1
        except Exception as exc:
            record_error('轮胎文件路径（NLG.tir）', exc)
    resource_path_4 = os.path.abspath(os.path.join(model_dir, '2d_flat.rdf'))
    if not os.path.isfile(resource_path_4):
        record_error('路面文件路径（2d_flat.rdf）', FileNotFoundError(resource_path_4))
    else:
        try:
            if set_resource('.template_2_drop.luntai2_2.rpf_file', resource_path_4):
                updated += 1
        except Exception as exc:
            record_error('路面文件路径（2d_flat.rdf）', exc)
    return {'updated': updated, 'warnings': warnings, 'errors': errors}

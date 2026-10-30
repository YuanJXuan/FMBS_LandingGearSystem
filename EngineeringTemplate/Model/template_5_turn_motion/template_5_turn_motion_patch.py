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

SOURCE_MODEL_NAME = 'template_5_turn_motion'
ADM_UDE_KINDS = {'lumian': 'road', 'luntai1': 'tire', 'luntai1_2': 'tire', 'luntai2': 'tire', 'luntai2_2': 'tire'}

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
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.NLG_V')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.NLG_V')
        if hasattr(node, 'adams_id'):
            node.adams_id = 115
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.NLG_V', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.LMLG_S')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.LMLG_S')
        if hasattr(node, 'adams_id'):
            node.adams_id = 116
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.LMLG_S', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.RMLG_S')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.RMLG_S')
        if hasattr(node, 'adams_id'):
            node.adams_id = 117
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.RMLG_S', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.LMLG_V')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.LMLG_V')
        if hasattr(node, 'adams_id'):
            node.adams_id = 118
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.LMLG_V', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.RMLG_V')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.RMLG_V')
        if hasattr(node, 'adams_id'):
            node.adams_id = 119
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.RMLG_V', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.NLG_S')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.NLG_S')
        if hasattr(node, 'adams_id'):
            node.adams_id = 120
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.NLG_S', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.x1')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.x1')
        if hasattr(node, 'adams_id'):
            node.adams_id = 121
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.x1', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.x2')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.x2')
        if hasattr(node, 'adams_id'):
            node.adams_id = 122
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.x2', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.VARIABLE_123')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.VARIABLE_123')
        if hasattr(node, 'adams_id'):
            node.adams_id = 123
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.VARIABLE_123', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion.VARIABLE_124')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion.VARIABLE_124')
        if hasattr(node, 'adams_id'):
            node.adams_id = 124
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion.VARIABLE_124', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_5_turn_motion._cv_solver_variable')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_5_turn_motion._cv_solver_variable')
        if hasattr(node, 'adams_id'):
            node.adams_id = 1
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_5_turn_motion._cv_solver_variable', exc)

    try:
        node = get_or_create('SimuScript', '.template_5_turn_motion.Last_Sim')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_5_turn_motion.Last_Sim')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=40.0 step_size=1.0E-02 model_name=.GCMB')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_5_turn_motion.Last_Sim', exc)

    try:
        node = get_or_create('SimuScript', '.template_5_turn_motion.Last_Sim_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_5_turn_motion.Last_Sim_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=2.0 number_of_steps=300 model_name=._AA_nlg_post_2hubs')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_5_turn_motion.Last_Sim_2', exc)

    try:
        node = get_object('.template_5_turn_motion.angle_drive')
        node.function = rewrite_expression('step(time,.template_5_turn_motion.T_1,0,.template_5_turn_motion.T_2,.template_5_turn_motion.angle)')
        updated += 1

    except Exception as exc:
        record_error('constraint modify motion_generator .template_5_turn_motion.angle_drive', exc)

    try:
        node = get_object('.template_5_turn_motion.NLG_V')
        node.function = rewrite_expression('-1*VR(.template_5_turn_motion.ges_upper_cylinder.MARKER_2,.template_5_turn_motion.ges_lower_cylinder.MARKER_1)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.NLG_V', exc)

    try:
        node = get_object('.template_5_turn_motion.LMLG_S')
        node.function = rewrite_expression('1.014262-DM(.template_5_turn_motion.gel_upper_cylinder.MARKER_272,.template_5_turn_motion.gel_lower_cylinder.MARKER_273)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.LMLG_S', exc)

    try:
        node = get_object('.template_5_turn_motion.RMLG_S')
        node.function = rewrite_expression('1.014262-DM(.template_5_turn_motion.ger_upper_cylinder.MARKER_278,.template_5_turn_motion.ger_lower_cylinder.MARKER_279)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.RMLG_S', exc)

    try:
        node = get_object('.template_5_turn_motion.LMLG_V')
        node.function = rewrite_expression('-1*VR(.template_5_turn_motion.gel_upper_cylinder.MARKER_272,.template_5_turn_motion.gel_lower_cylinder.MARKER_273)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.LMLG_V', exc)

    try:
        node = get_object('.template_5_turn_motion.RMLG_V')
        node.function = rewrite_expression('-1*VR(.template_5_turn_motion.ger_upper_cylinder.MARKER_278,.template_5_turn_motion.ger_lower_cylinder.MARKER_279)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.RMLG_V', exc)

    try:
        node = get_object('.template_5_turn_motion.NLG_S')
        node.function = rewrite_expression('0.4286-DM(.template_5_turn_motion.ges_upper_cylinder.MARKER_2,.template_5_turn_motion.ges_lower_cylinder.MARKER_1)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.NLG_S', exc)

    try:
        node = get_object('.template_5_turn_motion.x1')
        node.function = rewrite_expression('-1*(VARVAL(.template_5_turn_motion.NLG_V)*0.5*(VARVAL(.template_5_turn_motion.NLG_V)-ABS(VARVAL(.template_5_turn_motion.NLG_V)))*((.template_5_turn_motion.rho_Oil*.template_5_turn_motion.NLG_A_MAIN_OIL**3/(2*.template_5_turn_motion.NLG_MAIN_Cd**2*.template_5_turn_motion.NLG_A_MAIN_NEG**2))+(.template_5_turn_motion.rho_Oil*.template_5_turn_motion.NLG_A_RET_OIL**3/(2*.template_5_turn_motion.NLG_RET_Cd**2*.template_5_turn_motion.NLG_A_RET_NEG**2))))')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.x1', exc)

    try:
        node = get_object('.template_5_turn_motion.x2')
        node.function = rewrite_expression('0.00001*VARVAL(.template_5_turn_motion.NLG_V)*0.5*(VARVAL(.template_5_turn_motion.NLG_V)+ABS(VARVAL(.template_5_turn_motion.NLG_V)))*((.template_5_turn_motion.rho_Oil*.template_5_turn_motion.NLG_A_MAIN_OIL**3/(2*.template_5_turn_motion.NLG_MAIN_Cd**2*.template_5_turn_motion.NLG_A_MAIN_POS**2))+(.template_5_turn_motion.rho_Oil*.template_5_turn_motion.NLG_A_RET_OIL**3/(2*.template_5_turn_motion.NLG_RET_Cd**2*.template_5_turn_motion.NLG_A_RET_POS**2)))')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.x2', exc)

    try:
        node = get_object('.template_5_turn_motion.VARIABLE_123')
        node.function = rewrite_expression('IF(TIME:0,1,2)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.VARIABLE_123', exc)

    try:
        node = get_object('.template_5_turn_motion.VARIABLE_124')
        node.function = rewrite_expression('VARVAL(.template_5_turn_motion.NLG_V)-ABS(VARVAL(.template_5_turn_motion.NLG_V))')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion.VARIABLE_124', exc)

    try:
        node = get_object('.template_5_turn_motion._cv_solver_variable')
        node.function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_5_turn_motion._cv_solver_variable', exc)

    try:
        node = get_object('.template_5_turn_motion.jiaodu')
        node.function = rewrite_expression('AZ(.template_5_turn_motion.ges_collar.inertia_frame,.template_5_turn_motion.ges_upper_cylinder.inertia_frame)*180/pi-180')
        updated += 1

    except Exception as exc:
        record_error('measure modify function .template_5_turn_motion.jiaodu', exc)

    try:
        node = get_object('.template_5_turn_motion.jsd')
        node.function = rewrite_expression('wz(.template_5_turn_motion.ges_collar.inertia_frame,.template_5_turn_motion.ges_upper_cylinder.inertia_frame)*30/pi')
        updated += 1

    except Exception as exc:
        record_error('measure modify function .template_5_turn_motion.jsd', exc)

    try:
        node = get_object('.template_5_turn_motion._cv_diff')
        node.function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('part modify equation differential_equation .template_5_turn_motion._cv_diff', exc)

    try:
        node = get_object('.template_5_turn_motion.NLG_AIR')
        node.function = rewrite_expression('1*.template_5_turn_motion.NLG_Aa*(.template_5_turn_motion.NLG_P0*(.template_5_turn_motion.NLG_V0/(.template_5_turn_motion.NLG_V0-.template_5_turn_motion.NLG_Aa*(0.4286-DM(.template_5_turn_motion.ges_upper_cylinder.MARKER_2,.template_5_turn_motion.ges_lower_cylinder.MARKER_1))))**1.1-.template_5_turn_motion.Patm)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.NLG_AIR', exc)

    try:
        node = get_object('.template_5_turn_motion.NLG_OIL')
        node.function = rewrite_expression('IF(VARVAL(.template_5_turn_motion.NLG_V):1*-1*(VARVAL(.template_5_turn_motion.NLG_V)*0.5*(VARVAL(.template_5_turn_motion.NLG_V)-ABS(VARVAL(.template_5_turn_motion.NLG_V)))*((.template_5_turn_motion.rho_Oil*.template_5_turn_motion.NLG_A_MAIN_OIL**3/(2*.template_5_turn_motion.NLG_MAIN_Cd**2*.template_5_turn_motion.NLG_A_MAIN_NEG**2))+(.template_5_turn_motion.rho_Oil*.template_5_turn_motion.NLG_A_RET_OIL**3/(2*.template_5_turn_motion.NLG_RET_Cd**2*.template_5_turn_motion.NLG_A_RET_NEG**2)))),0,1*VARVAL(.template_5_turn_motion.NLG_V)*0.5*(VARVAL(.template_5_turn_motion.NLG_V)+ABS(VARVAL(.template_5_turn_motion.NLG_V)))*((.template_5_turn_motion.rho_Oil*.template_5_turn_motion.NLG_A_MAIN_OIL**3/(2*.template_5_turn_motion.NLG_MAIN_Cd**2*.template_5_turn_motion.NLG_A_MAIN_POS**2))+(.template_5_turn_motion.rho_Oil*.template_5_turn_motion.NLG_A_RET_OIL**3/(2*.template_5_turn_motion.NLG_RET_Cd**2*.template_5_turn_motion.NLG_A_RET_POS**2))))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.NLG_OIL', exc)

    try:
        node = get_object('.template_5_turn_motion.NLG_STOP')
        node.function = rewrite_expression('IF(0.4286-DM(.template_5_turn_motion.ges_upper_cylinder.MARKER_2,.template_5_turn_motion.ges_lower_cylinder.MARKER_1) :1.0E+09*(0.4286-DM(.template_5_turn_motion.ges_upper_cylinder.MARKER_2,.template_5_turn_motion.ges_lower_cylinder.MARKER_1)), 0 , 0 )')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.NLG_STOP', exc)

    try:
        node = get_object('.template_5_turn_motion.LMLG_AIR')
        node.function = rewrite_expression('.template_5_turn_motion.MLG_Aa*(.template_5_turn_motion.MLG_P0*(.template_5_turn_motion.MLG_V0/(.template_5_turn_motion.MLG_V0-.template_5_turn_motion.MLG_Aa*VARVAL(.template_5_turn_motion.LMLG_S)))**1.1-.template_5_turn_motion.Patm)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.LMLG_AIR', exc)

    try:
        node = get_object('.template_5_turn_motion.LMLG_OIL')
        node.function = rewrite_expression('IF(VARVAL(.template_5_turn_motion.LMLG_V):2*-1*(VARVAL(.template_5_turn_motion.LMLG_V)*0.5*(VARVAL(.template_5_turn_motion.LMLG_V)-ABS(VARVAL(.template_5_turn_motion.LMLG_V)))*((.template_5_turn_motion.rho_Oil*.template_5_turn_motion.MLG_A_MAIN_OIL**3/(2*.template_5_turn_motion.MLG_MAIN_Cd**2*.template_5_turn_motion.MLG_A_MAIN_NEG**2))+(.template_5_turn_motion.rho_Oil*.template_5_turn_motion.MLG_A_RET_OIL**3/(2*.template_5_turn_motion.MLG_RET_Cd**2*.template_5_turn_motion.MLG_A_RET_NEG**2)))),0,2*VARVAL(.template_5_turn_motion.LMLG_V)*0.5*(VARVAL(.template_5_turn_motion.LMLG_V)+ABS(VARVAL(.template_5_turn_motion.LMLG_V)))*((.template_5_turn_motion.rho_Oil*.template_5_turn_motion.MLG_A_MAIN_OIL**3/(2*.template_5_turn_motion.MLG_MAIN_Cd**2*.template_5_turn_motion.MLG_A_MAIN_POS**2))+(.template_5_turn_motion.rho_Oil*.template_5_turn_motion.MLG_A_RET_OIL**3/(2*.template_5_turn_motion.MLG_RET_Cd**2*.template_5_turn_motion.MLG_A_RET_POS**2))))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.LMLG_OIL', exc)

    try:
        node = get_object('.template_5_turn_motion.LMLG_STOP')
        node.function = rewrite_expression('IF(1.014262-DM(.template_5_turn_motion.gel_upper_cylinder.MARKER_272,.template_5_turn_motion.gel_lower_cylinder.MARKER_273) :1.0E+09*(1.014262-DM(.template_5_turn_motion.gel_upper_cylinder.MARKER_272,.template_5_turn_motion.gel_lower_cylinder.MARKER_273)) , 0 , 0 )')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.LMLG_STOP', exc)

    try:
        node = get_object('.template_5_turn_motion.RMLG_AIR')
        node.function = rewrite_expression('.template_5_turn_motion.MLG_Aa*(.template_5_turn_motion.MLG_P0*(.template_5_turn_motion.MLG_V0/(.template_5_turn_motion.MLG_V0-.template_5_turn_motion.MLG_Aa*VARVAL(.template_5_turn_motion.RMLG_S)))**1.1-.template_5_turn_motion.Patm)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.RMLG_AIR', exc)

    try:
        node = get_object('.template_5_turn_motion.RMLG_OIL')
        node.function = rewrite_expression('IF(VARVAL(.template_5_turn_motion.RMLG_V):2*-1*(VARVAL(.template_5_turn_motion.RMLG_V)*0.5*(VARVAL(.template_5_turn_motion.RMLG_V)-ABS(VARVAL(.template_5_turn_motion.RMLG_V)))*((.template_5_turn_motion.rho_Oil*.template_5_turn_motion.MLG_A_MAIN_OIL**3/(2*.template_5_turn_motion.MLG_MAIN_Cd**2*.template_5_turn_motion.MLG_A_MAIN_NEG**2))+(.template_5_turn_motion.rho_Oil*.template_5_turn_motion.MLG_A_RET_OIL**3/(2*.template_5_turn_motion.MLG_RET_Cd**2*.template_5_turn_motion.MLG_A_RET_NEG**2)))),0,2*VARVAL(.template_5_turn_motion.RMLG_V)*0.5*(VARVAL(.template_5_turn_motion.RMLG_V)+ABS(VARVAL(.template_5_turn_motion.RMLG_V)))*((.template_5_turn_motion.rho_Oil*.template_5_turn_motion.MLG_A_MAIN_OIL**3/(2*.template_5_turn_motion.MLG_MAIN_Cd**2*.template_5_turn_motion.MLG_A_MAIN_POS**2))+(.template_5_turn_motion.rho_Oil*.template_5_turn_motion.MLG_A_RET_OIL**3/(2*.template_5_turn_motion.MLG_RET_Cd**2*.template_5_turn_motion.MLG_A_RET_POS**2))))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.RMLG_OIL', exc)

    try:
        node = get_object('.template_5_turn_motion.RMLG_STOP')
        node.function = rewrite_expression('IF(1.014262-DM(.template_5_turn_motion.ger_upper_cylinder.MARKER_278,.template_5_turn_motion.ger_lower_cylinder.MARKER_279) :1.0E+09*(1.014262-DM(.template_5_turn_motion.ger_upper_cylinder.MARKER_278,.template_5_turn_motion.ger_lower_cylinder.MARKER_279)) , 0 ,0 )')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.RMLG_STOP', exc)

    try:
        node = get_object('.template_5_turn_motion.thrust')
        node.function = rewrite_expression('-300000*2/3.14*atan(.template_5_turn_motion.Vel-.template_5_turn_motion.jscm_sd)*step(time,3,0,3.5,1)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.thrust', exc)

    try:
        node = get_object('.template_5_turn_motion.damping_force')
        node.function = rewrite_expression('-.template_5_turn_motion.jsd*50')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_5_turn_motion.damping_force', exc)

    try:
        cfl_spin_axis = get_object('.template_5_turn_motion.ground.cfl_spin_axis')
        cfl_spin_axis.marker_name = target_path('.template_5_turn_motion.ground.cfl_spin_axis')
        _template_5_turn_motion_ground_cfl_spin_axis_1 = get_object('.template_5_turn_motion.ground.cfl_spin_axis_1')
        cfl_spin_axis.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_spin_axis_1))
        _template_5_turn_motion_ground_cfl_spin_axis_1 = get_object('.template_5_turn_motion.ground.cfl_spin_axis_1')
        cfl_spin_axis.orientation = (VecUtils.ORI_RELATIVE_TO([180.0, 180.0, 180.0], _template_5_turn_motion_ground_cfl_spin_axis_1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_spin_axis', exc)

    try:
        cfr_spin_axis = get_object('.template_5_turn_motion.ground.cfr_spin_axis')
        cfr_spin_axis.marker_name = target_path('.template_5_turn_motion.ground.cfr_spin_axis')
        _template_5_turn_motion_ground_cfr_spin_axis_1 = get_object('.template_5_turn_motion.ground.cfr_spin_axis_1')
        cfr_spin_axis.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_spin_axis_1))
        _template_5_turn_motion_ground_cfr_spin_axis_1 = get_object('.template_5_turn_motion.ground.cfr_spin_axis_1')
        cfr_spin_axis.orientation = (VecUtils.ORI_RELATIVE_TO([-180.0, -180.0, -180.0], _template_5_turn_motion_ground_cfr_spin_axis_1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_spin_axis', exc)

    try:
        cfl_axial_reference = get_object('.template_5_turn_motion.ground.cfl_axial_reference')
        cfl_axial_reference.marker_name = target_path('.template_5_turn_motion.ground.cfl_axial_reference')
        _template_5_turn_motion_ground_hpl_lc_bot = get_object('.template_5_turn_motion.ground.hpl_lc_bot')
        cfl_axial_reference.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_lc_bot))
        _template_5_turn_motion_ground_hpl_lc_bot = get_object('.template_5_turn_motion.ground.hpl_lc_bot').location
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top').location
        cfl_axial_reference.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_lc_bot, _template_5_turn_motion_ground_hpl_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_axial_reference', exc)

    try:
        cfr_axial_reference = get_object('.template_5_turn_motion.ground.cfr_axial_reference')
        cfr_axial_reference.marker_name = target_path('.template_5_turn_motion.ground.cfr_axial_reference')
        _template_5_turn_motion_ground_hpr_lc_bot = get_object('.template_5_turn_motion.ground.hpr_lc_bot')
        cfr_axial_reference.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_lc_bot))
        _template_5_turn_motion_ground_hpr_lc_bot = get_object('.template_5_turn_motion.ground.hpr_lc_bot').location
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top').location
        cfr_axial_reference.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_lc_bot, _template_5_turn_motion_ground_hpr_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_axial_reference', exc)

    try:
        cfl_uc_bot = get_object('.template_5_turn_motion.ground.cfl_uc_bot')
        cfl_uc_bot.marker_name = target_path('.template_5_turn_motion.ground.cfl_uc_bot')
        _template_5_turn_motion_ground_cfl_axial_reference = get_object('.template_5_turn_motion.ground.cfl_axial_reference')
        cfl_uc_bot.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 537.972], _template_5_turn_motion_ground_cfl_axial_reference))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfl_uc_bot.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_uc_bot', exc)

    try:
        cfr_uc_bot = get_object('.template_5_turn_motion.ground.cfr_uc_bot')
        cfr_uc_bot.marker_name = target_path('.template_5_turn_motion.ground.cfr_uc_bot')
        _template_5_turn_motion_ground_cfr_axial_reference = get_object('.template_5_turn_motion.ground.cfr_axial_reference')
        cfr_uc_bot.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 537.972], _template_5_turn_motion_ground_cfr_axial_reference))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfr_uc_bot.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_uc_bot', exc)

    try:
        cfl_uc_top = get_object('.template_5_turn_motion.ground.cfl_uc_top')
        cfl_uc_top.marker_name = target_path('.template_5_turn_motion.ground.cfl_uc_top')
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top')
        cfl_uc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_uc_top))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfl_uc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_uc_top', exc)

    try:
        cfr_uc_top = get_object('.template_5_turn_motion.ground.cfr_uc_top')
        cfr_uc_top.marker_name = target_path('.template_5_turn_motion.ground.cfr_uc_top')
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top')
        cfr_uc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_uc_top))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfr_uc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_uc_top', exc)

    try:
        cfl_lc_top = get_object('.template_5_turn_motion.ground.cfl_lc_top')
        cfl_lc_top.marker_name = target_path('.template_5_turn_motion.ground.cfl_lc_top')
        _template_5_turn_motion_ground_cfl_axial_reference = get_object('.template_5_turn_motion.ground.cfl_axial_reference')
        cfl_lc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 966.724], _template_5_turn_motion_ground_cfl_axial_reference))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfl_lc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_lc_top', exc)

    try:
        cfr_lc_top = get_object('.template_5_turn_motion.ground.cfr_lc_top')
        cfr_lc_top.marker_name = target_path('.template_5_turn_motion.ground.cfr_lc_top')
        _template_5_turn_motion_ground_cfr_axial_reference = get_object('.template_5_turn_motion.ground.cfr_axial_reference')
        cfr_lc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 966.724], _template_5_turn_motion_ground_cfr_axial_reference))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfr_lc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_lc_top', exc)

    try:
        cfl_uta_uc_atch = get_object('.template_5_turn_motion.ground.cfl_uta_uc_atch')
        cfl_uta_uc_atch.marker_name = target_path('.template_5_turn_motion.ground.cfl_uta_uc_atch')
        _template_5_turn_motion_ground_cfl_uc_bot = get_object('.template_5_turn_motion.ground.cfl_uc_bot')
        cfl_uta_uc_atch.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_uc_bot))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfl_uta_uc_atch.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_uta_uc_atch', exc)

    try:
        cfr_uta_uc_atch = get_object('.template_5_turn_motion.ground.cfr_uta_uc_atch')
        cfr_uta_uc_atch.marker_name = target_path('.template_5_turn_motion.ground.cfr_uta_uc_atch')
        _template_5_turn_motion_ground_cfr_uc_bot = get_object('.template_5_turn_motion.ground.cfr_uc_bot')
        cfr_uta_uc_atch.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_uc_bot))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfr_uta_uc_atch.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_uta_uc_atch', exc)

    try:
        cfl_lta_lc_atch = get_object('.template_5_turn_motion.ground.cfl_lta_lc_atch')
        cfl_lta_lc_atch.marker_name = target_path('.template_5_turn_motion.ground.cfl_lta_lc_atch')
        _template_5_turn_motion_ground_hpl_lc_bot = get_object('.template_5_turn_motion.ground.hpl_lc_bot')
        cfl_lta_lc_atch.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_lc_bot))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfl_lta_lc_atch.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_lta_lc_atch', exc)

    try:
        cfr_lta_lc_atch = get_object('.template_5_turn_motion.ground.cfr_lta_lc_atch')
        cfr_lta_lc_atch.marker_name = target_path('.template_5_turn_motion.ground.cfr_lta_lc_atch')
        _template_5_turn_motion_ground_hpr_lc_bot = get_object('.template_5_turn_motion.ground.hpr_lc_bot')
        cfr_lta_lc_atch.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_lc_bot))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfr_lta_lc_atch.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_lta_lc_atch', exc)

    try:
        cfl_collar_top = get_object('.template_5_turn_motion.ground.cfl_collar_top')
        cfl_collar_top.marker_name = target_path('.template_5_turn_motion.ground.cfl_collar_top')
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top').location
        _template_5_turn_motion_ground_hpl_lc_bot = get_object('.template_5_turn_motion.ground.hpl_lc_bot').location
        cfl_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpl_uc_top, _template_5_turn_motion_ground_hpl_lc_bot, 0.59 * VecUtils.DM(_template_5_turn_motion_ground_hpl_uc_top, _template_5_turn_motion_ground_hpl_lc_bot)))
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top').location
        _template_5_turn_motion_ground_hpl_lc_bot = get_object('.template_5_turn_motion.ground.hpl_lc_bot').location
        cfl_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_uc_top, _template_5_turn_motion_ground_hpl_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_collar_top', exc)

    try:
        cfr_collar_top = get_object('.template_5_turn_motion.ground.cfr_collar_top')
        cfr_collar_top.marker_name = target_path('.template_5_turn_motion.ground.cfr_collar_top')
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top').location
        _template_5_turn_motion_ground_hpr_lc_bot = get_object('.template_5_turn_motion.ground.hpr_lc_bot').location
        cfr_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpr_uc_top, _template_5_turn_motion_ground_hpr_lc_bot, 0.59 * VecUtils.DM(_template_5_turn_motion_ground_hpr_uc_top, _template_5_turn_motion_ground_hpr_lc_bot)))
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top').location
        _template_5_turn_motion_ground_hpr_lc_bot = get_object('.template_5_turn_motion.ground.hpr_lc_bot').location
        cfr_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_uc_top, _template_5_turn_motion_ground_hpr_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_collar_top', exc)

    try:
        cfl_collar_bot = get_object('.template_5_turn_motion.ground.cfl_collar_bot')
        cfl_collar_bot.marker_name = target_path('.template_5_turn_motion.ground.cfl_collar_bot')
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top').location
        _template_5_turn_motion_ground_hpl_lc_bot = get_object('.template_5_turn_motion.ground.hpl_lc_bot').location
        cfl_collar_bot.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpl_uc_top, _template_5_turn_motion_ground_hpl_lc_bot, 0.7 * VecUtils.DM(_template_5_turn_motion_ground_hpl_uc_top, _template_5_turn_motion_ground_hpl_lc_bot)))
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top').location
        _template_5_turn_motion_ground_hpl_lc_bot = get_object('.template_5_turn_motion.ground.hpl_lc_bot').location
        cfl_collar_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_uc_top, _template_5_turn_motion_ground_hpl_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_collar_bot', exc)

    try:
        cfr_collar_bot = get_object('.template_5_turn_motion.ground.cfr_collar_bot')
        cfr_collar_bot.marker_name = target_path('.template_5_turn_motion.ground.cfr_collar_bot')
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top').location
        _template_5_turn_motion_ground_hpr_lc_bot = get_object('.template_5_turn_motion.ground.hpr_lc_bot').location
        cfr_collar_bot.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpr_uc_top, _template_5_turn_motion_ground_hpr_lc_bot, 0.7 * VecUtils.DM(_template_5_turn_motion_ground_hpr_uc_top, _template_5_turn_motion_ground_hpr_lc_bot)))
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top').location
        _template_5_turn_motion_ground_hpr_lc_bot = get_object('.template_5_turn_motion.ground.hpr_lc_bot').location
        cfr_collar_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_uc_top, _template_5_turn_motion_ground_hpr_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_collar_bot', exc)

    try:
        cfl_plane_ref_2 = get_object('.template_5_turn_motion.ground.cfl_plane_ref_2')
        cfl_plane_ref_2.marker_name = target_path('.template_5_turn_motion.ground.cfl_plane_ref_2')
        _template_5_turn_motion_ground_cfl_plane_ref = get_object('.template_5_turn_motion.ground.cfl_plane_ref')
        cfl_plane_ref_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_plane_ref))
        _template_5_turn_motion_ground_cfl_plane_ref = get_object('.template_5_turn_motion.ground.cfl_plane_ref')
        cfl_plane_ref_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, -90.0, 0.0], _template_5_turn_motion_ground_cfl_plane_ref))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_plane_ref_2', exc)

    try:
        cfr_plane_ref_2 = get_object('.template_5_turn_motion.ground.cfr_plane_ref_2')
        cfr_plane_ref_2.marker_name = target_path('.template_5_turn_motion.ground.cfr_plane_ref_2')
        _template_5_turn_motion_ground_cfr_plane_ref = get_object('.template_5_turn_motion.ground.cfr_plane_ref')
        cfr_plane_ref_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_plane_ref))
        _template_5_turn_motion_ground_cfr_plane_ref = get_object('.template_5_turn_motion.ground.cfr_plane_ref')
        cfr_plane_ref_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_5_turn_motion_ground_cfr_plane_ref))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_plane_ref_2', exc)

    try:
        cfl_lwract_top = get_object('.template_5_turn_motion.ground.cfl_lwract_top')
        cfl_lwract_top.marker_name = target_path('.template_5_turn_motion.ground.cfl_lwract_top')
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpl_upract_sf_atch_1').location
        cfl_lwract_top.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpl_lwract_uc_atch_1, _template_5_turn_motion_ground_hpl_upract_sf_atch_1, 0.92 * VecUtils.DM(_template_5_turn_motion_ground_hpl_lwract_uc_atch_1, _template_5_turn_motion_ground_hpl_upract_sf_atch_1)))
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpl_upract_sf_atch_1').location
        cfl_lwract_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_lwract_uc_atch_1, _template_5_turn_motion_ground_hpl_upract_sf_atch_1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_lwract_top', exc)

    try:
        cfr_lwract_top = get_object('.template_5_turn_motion.ground.cfr_lwract_top')
        cfr_lwract_top.marker_name = target_path('.template_5_turn_motion.ground.cfr_lwract_top')
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpr_upract_sf_atch_1').location
        cfr_lwract_top.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpr_lwract_uc_atch_1, _template_5_turn_motion_ground_hpr_upract_sf_atch_1, 0.92 * VecUtils.DM(_template_5_turn_motion_ground_hpr_lwract_uc_atch_1, _template_5_turn_motion_ground_hpr_upract_sf_atch_1)))
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpr_upract_sf_atch_1').location
        cfr_lwract_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_lwract_uc_atch_1, _template_5_turn_motion_ground_hpr_upract_sf_atch_1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_lwract_top', exc)

    try:
        cfl_upract_bot = get_object('.template_5_turn_motion.ground.cfl_upract_bot')
        cfl_upract_bot.marker_name = target_path('.template_5_turn_motion.ground.cfl_upract_bot')
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpl_upract_sf_atch_1').location
        cfl_upract_bot.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpl_lwract_uc_atch_1, _template_5_turn_motion_ground_hpl_upract_sf_atch_1, 0.4 * VecUtils.DM(_template_5_turn_motion_ground_hpl_lwract_uc_atch_1, _template_5_turn_motion_ground_hpl_upract_sf_atch_1)))
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpl_upract_sf_atch_1').location
        cfl_upract_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_lwract_uc_atch_1, _template_5_turn_motion_ground_hpl_upract_sf_atch_1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_upract_bot', exc)

    try:
        cfr_upract_bot = get_object('.template_5_turn_motion.ground.cfr_upract_bot')
        cfr_upract_bot.marker_name = target_path('.template_5_turn_motion.ground.cfr_upract_bot')
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpr_upract_sf_atch_1').location
        cfr_upract_bot.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpr_lwract_uc_atch_1, _template_5_turn_motion_ground_hpr_upract_sf_atch_1, 0.4 * VecUtils.DM(_template_5_turn_motion_ground_hpr_lwract_uc_atch_1, _template_5_turn_motion_ground_hpr_upract_sf_atch_1)))
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpr_upract_sf_atch_1').location
        cfr_upract_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_lwract_uc_atch_1, _template_5_turn_motion_ground_hpr_upract_sf_atch_1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_upract_bot', exc)

    try:
        cfl_spin_axis_1 = get_object('.template_5_turn_motion.ground.cfl_spin_axis_1')
        cfl_spin_axis_1.marker_name = target_path('.template_5_turn_motion.ground.cfl_spin_axis_1')
        _template_5_turn_motion_ground_hpl_wheel_center = get_object('.template_5_turn_motion.ground.hpl_wheel_center')
        cfl_spin_axis_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_wheel_center))
        _template_5_turn_motion_ground_hpl_wheel_center = get_object('.template_5_turn_motion.ground.hpl_wheel_center').location
        _template_5_turn_motion_ground_hpl_ob_axle = get_object('.template_5_turn_motion.ground.hpl_ob_axle').location
        cfl_spin_axis_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_wheel_center, _template_5_turn_motion_ground_hpl_ob_axle, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_spin_axis_1', exc)

    try:
        cfr_spin_axis_1 = get_object('.template_5_turn_motion.ground.cfr_spin_axis_1')
        cfr_spin_axis_1.marker_name = target_path('.template_5_turn_motion.ground.cfr_spin_axis_1')
        _template_5_turn_motion_ground_hpr_wheel_center = get_object('.template_5_turn_motion.ground.hpr_wheel_center')
        cfr_spin_axis_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_wheel_center))
        _template_5_turn_motion_ground_hpr_wheel_center = get_object('.template_5_turn_motion.ground.hpr_wheel_center').location
        _template_5_turn_motion_ground_hpr_ob_axle = get_object('.template_5_turn_motion.ground.hpr_ob_axle').location
        cfr_spin_axis_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_wheel_center, _template_5_turn_motion_ground_hpr_ob_axle, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_spin_axis_1', exc)

    try:
        cfl_ldb_geompt_1 = get_object('.template_5_turn_motion.ground.cfl_ldb_geompt_1')
        cfl_ldb_geompt_1.marker_name = target_path('.template_5_turn_motion.ground.cfl_ldb_geompt_1')
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpl_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_collar_atch_1').location
        cfl_ldb_geompt_1.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpl_ldb_udb_atch_1, _template_5_turn_motion_ground_hpl_ldb_collar_atch_1, 0.62 * VecUtils.DM(_template_5_turn_motion_ground_hpl_ldb_udb_atch_1, _template_5_turn_motion_ground_hpl_ldb_collar_atch_1)))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfl_ldb_geompt_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_ldb_geompt_1', exc)

    try:
        cfr_ldb_geompt_1 = get_object('.template_5_turn_motion.ground.cfr_ldb_geompt_1')
        cfr_ldb_geompt_1.marker_name = target_path('.template_5_turn_motion.ground.cfr_ldb_geompt_1')
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpr_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_collar_atch_1').location
        cfr_ldb_geompt_1.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpr_ldb_udb_atch_1, _template_5_turn_motion_ground_hpr_ldb_collar_atch_1, 0.62 * VecUtils.DM(_template_5_turn_motion_ground_hpr_ldb_udb_atch_1, _template_5_turn_motion_ground_hpr_ldb_collar_atch_1)))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfr_ldb_geompt_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_ldb_geompt_1', exc)

    try:
        cfl_ldb_geompt_2 = get_object('.template_5_turn_motion.ground.cfl_ldb_geompt_2')
        cfl_ldb_geompt_2.marker_name = target_path('.template_5_turn_motion.ground.cfl_ldb_geompt_2')
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpl_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_collar_atch_1').location
        cfl_ldb_geompt_2.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpl_ldb_udb_atch_1, _template_5_turn_motion_ground_hpl_ldb_collar_atch_1, 0.74 * VecUtils.DM(_template_5_turn_motion_ground_hpl_ldb_udb_atch_1, _template_5_turn_motion_ground_hpl_ldb_collar_atch_1)))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfl_ldb_geompt_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_ldb_geompt_2', exc)

    try:
        cfr_ldb_geompt_2 = get_object('.template_5_turn_motion.ground.cfr_ldb_geompt_2')
        cfr_ldb_geompt_2.marker_name = target_path('.template_5_turn_motion.ground.cfr_ldb_geompt_2')
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpr_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_collar_atch_1').location
        cfr_ldb_geompt_2.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hpr_ldb_udb_atch_1, _template_5_turn_motion_ground_hpr_ldb_collar_atch_1, 0.74 * VecUtils.DM(_template_5_turn_motion_ground_hpr_ldb_udb_atch_1, _template_5_turn_motion_ground_hpr_ldb_collar_atch_1)))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfr_ldb_geompt_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_ldb_geompt_2', exc)

    try:
        cfl_aero_ref = get_object('.template_5_turn_motion.ground.cfl_aero_ref')
        cfl_aero_ref.marker_name = target_path('.template_5_turn_motion.ground.cfl_aero_ref')
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top')
        cfl_aero_ref.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_uc_top))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfl_aero_ref.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_aero_ref', exc)

    try:
        cfr_aero_ref = get_object('.template_5_turn_motion.ground.cfr_aero_ref')
        cfr_aero_ref.marker_name = target_path('.template_5_turn_motion.ground.cfr_aero_ref')
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top')
        cfr_aero_ref.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_uc_top))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        cfr_aero_ref.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_aero_ref', exc)

    try:
        uel_gearaero_origin_1 = get_object('.template_5_turn_motion.ground.uel_gearaero_origin_1')
        uel_gearaero_origin_1.marker_name = target_path('.template_5_turn_motion.ground.uel_gearaero_origin_1')
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        uel_gearaero_origin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        uel_gearaero_origin_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.uel_gearaero_origin_1', exc)

    try:
        uel_gearaero_rm_1 = get_object('.template_5_turn_motion.ground.uel_gearaero_rm_1')
        uel_gearaero_rm_1.marker_name = target_path('.template_5_turn_motion.ground.uel_gearaero_rm_1')
        _template_5_turn_motion_ground_cfl_aero_ref = get_object('.template_5_turn_motion.ground.cfl_aero_ref')
        uel_gearaero_rm_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_aero_ref))
        _template_5_turn_motion_ground_cfl_aero_ref = get_object('.template_5_turn_motion.ground.cfl_aero_ref')
        uel_gearaero_rm_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_aero_ref))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.uel_gearaero_rm_1', exc)

    try:
        uer_gearaero_origin_1 = get_object('.template_5_turn_motion.ground.uer_gearaero_origin_1')
        uer_gearaero_origin_1.marker_name = target_path('.template_5_turn_motion.ground.uer_gearaero_origin_1')
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        uer_gearaero_origin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        uer_gearaero_origin_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.uer_gearaero_origin_1', exc)

    try:
        uer_gearaero_rm_1 = get_object('.template_5_turn_motion.ground.uer_gearaero_rm_1')
        uer_gearaero_rm_1.marker_name = target_path('.template_5_turn_motion.ground.uer_gearaero_rm_1')
        _template_5_turn_motion_ground_cfr_aero_ref = get_object('.template_5_turn_motion.ground.cfr_aero_ref')
        uer_gearaero_rm_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_aero_ref))
        _template_5_turn_motion_ground_cfr_aero_ref = get_object('.template_5_turn_motion.ground.cfr_aero_ref')
        uer_gearaero_rm_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_aero_ref))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.uer_gearaero_rm_1', exc)

    try:
        cfl_spin_axis1 = get_object('.template_5_turn_motion.ground.cfl_spin_axis1')
        cfl_spin_axis1.marker_name = target_path('.template_5_turn_motion.ground.cfl_spin_axis1')
        _template_5_turn_motion_ground_hpl_wheel_center1 = get_object('.template_5_turn_motion.ground.hpl_wheel_center1')
        cfl_spin_axis1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_wheel_center1))
        _template_5_turn_motion_ground_hpl_wheel_center1 = get_object('.template_5_turn_motion.ground.hpl_wheel_center1').location
        _template_5_turn_motion_ground_hpl_ob_axle1 = get_object('.template_5_turn_motion.ground.hpl_ob_axle1').location
        cfl_spin_axis1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_wheel_center1, _template_5_turn_motion_ground_hpl_ob_axle1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfl_spin_axis1', exc)

    try:
        cfr_spin_axis1 = get_object('.template_5_turn_motion.ground.cfr_spin_axis1')
        cfr_spin_axis1.marker_name = target_path('.template_5_turn_motion.ground.cfr_spin_axis1')
        _template_5_turn_motion_ground_hpr_wheel_center1 = get_object('.template_5_turn_motion.ground.hpr_wheel_center1')
        cfr_spin_axis1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_wheel_center1))
        _template_5_turn_motion_ground_hpr_wheel_center1 = get_object('.template_5_turn_motion.ground.hpr_wheel_center1').location
        _template_5_turn_motion_ground_hpr_ob_axle1 = get_object('.template_5_turn_motion.ground.hpr_ob_axle1').location
        cfr_spin_axis1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_wheel_center1, _template_5_turn_motion_ground_hpr_ob_axle1, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfr_spin_axis1', exc)

    try:
        cfs_nlg_axle_lowpoint = get_object('.template_5_turn_motion.ground.cfs_nlg_axle_lowpoint')
        cfs_nlg_axle_lowpoint.marker_name = target_path('.template_5_turn_motion.ground.cfs_nlg_axle_lowpoint')
        _template_5_turn_motion_ground_hps_nlg_axle_lowpoint = get_object('.template_5_turn_motion.ground.hps_nlg_axle_lowpoint')
        cfs_nlg_axle_lowpoint.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_nlg_axle_lowpoint))
        _template_5_turn_motion_ground_origo1 = get_object('.template_5_turn_motion.ground.origo1')
        cfs_nlg_axle_lowpoint.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfs_nlg_axle_lowpoint', exc)

    try:
        cfs_collar_top = get_object('.template_5_turn_motion.ground.cfs_collar_top')
        cfs_collar_top.marker_name = target_path('.template_5_turn_motion.ground.cfs_collar_top')
        _template_5_turn_motion_ground_hps_uc_bot = get_object('.template_5_turn_motion.ground.hps_uc_bot').location
        _template_5_turn_motion_ground_hps_uc_top = get_object('.template_5_turn_motion.ground.hps_uc_top').location
        cfs_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hps_uc_bot, _template_5_turn_motion_ground_hps_uc_top, 0.11 * VecUtils.DM(_template_5_turn_motion_ground_hps_uc_bot, _template_5_turn_motion_ground_hps_uc_top)))
        _template_5_turn_motion_ground_hps_uc_bot = get_object('.template_5_turn_motion.ground.hps_uc_bot').location
        _template_5_turn_motion_ground_hps_uc_top = get_object('.template_5_turn_motion.ground.hps_uc_top').location
        cfs_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_uc_bot, _template_5_turn_motion_ground_hps_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.cfs_collar_top', exc)

    try:
        zdt1 = get_object('.template_5_turn_motion.ground.zdt1')
        zdt1.marker_name = target_path('.template_5_turn_motion.ground.zdt1')
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1').location
        _template_5_turn_motion_ground_hsg_2 = get_object('.template_5_turn_motion.ground.hsg_2').location
        zdt1.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_hsg_2, 0.6 * VecUtils.DM(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_hsg_2)))
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1').location
        _template_5_turn_motion_ground_hsg_2 = get_object('.template_5_turn_motion.ground.hsg_2').location
        zdt1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_hsg_2, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.zdt1', exc)

    try:
        zdt2 = get_object('.template_5_turn_motion.ground.zdt2')
        zdt2.marker_name = target_path('.template_5_turn_motion.ground.zdt2')
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1').location
        _template_5_turn_motion_ground_hsg_2 = get_object('.template_5_turn_motion.ground.hsg_2').location
        zdt2.location = (VecUtils.LOC_ALONG_LINE(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_hsg_2, 0.9 * VecUtils.DM(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_hsg_2)))
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1').location
        _template_5_turn_motion_ground_hsg_2 = get_object('.template_5_turn_motion.ground.hsg_2').location
        zdt2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_hsg_2, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ground.zdt2', exc)

    try:
        uel_gearaero_i_1 = get_object('.template_5_turn_motion.gel_upper_cylinder.uel_gearaero_i_1')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        uel_gearaero_i_1.relative_to = relative_to
        uel_gearaero_i_1.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.uel_gearaero_i_1')
        _template_5_turn_motion_ground_cfl_lc_top = get_object('.template_5_turn_motion.ground.cfl_lc_top')
        uel_gearaero_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_gearaero_i_1.location, uel_gearaero_i_1.orientation)
        uel_gearaero_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.uel_gearaero_i_1', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_upper_cylinder.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.inertia_frame')
        _template_5_turn_motion_gel_upper_cylinder_cm = get_object('.template_5_turn_motion.gel_upper_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_cylinder_cm))
        _template_5_turn_motion_gel_upper_cylinder = get_object('.template_5_turn_motion.gel_upper_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.inertia_frame', exc)

    try:
        gralin_12 = get_object('.template_5_turn_motion.gel_upper_cylinder.gralin_12')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        gralin_12.relative_to = relative_to
        gralin_12.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.gralin_12')
        _template_5_turn_motion_ground_cfl_uc_top = get_object('.template_5_turn_motion.ground.cfl_uc_top')
        gralin_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_uc_top))
        _template_5_turn_motion_ground_cfl_uc_top = get_object('.template_5_turn_motion.ground.cfl_uc_top').location
        _template_5_turn_motion_ground_cfl_uc_bot = get_object('.template_5_turn_motion.ground.cfl_uc_bot').location
        gralin_12.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_cfl_uc_top, _template_5_turn_motion_ground_cfl_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_12.location, gralin_12.orientation)
        gralin_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.gralin_12', exc)

    try:
        gralin_16 = get_object('.template_5_turn_motion.gel_upper_cylinder.gralin_16')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        gralin_16.relative_to = relative_to
        gralin_16.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.gralin_16')
        _template_5_turn_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpl_ib_uc_sf_atch')
        gralin_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_ib_uc_sf_atch))
        _template_5_turn_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpl_ib_uc_sf_atch').location
        _template_5_turn_motion_ground_hpl_uc_geompt = get_object('.template_5_turn_motion.ground.hpl_uc_geompt').location
        gralin_16.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_ib_uc_sf_atch, _template_5_turn_motion_ground_hpl_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_16.location, gralin_16.orientation)
        gralin_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.gralin_16', exc)

    try:
        gralin_20 = get_object('.template_5_turn_motion.gel_upper_cylinder.gralin_20')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        gralin_20.relative_to = relative_to
        gralin_20.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.gralin_20')
        _template_5_turn_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpl_ib_uc_sf_atch')
        gralin_20.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_ib_uc_sf_atch))
        _template_5_turn_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpl_ib_uc_sf_atch').location
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top').location
        gralin_20.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_ib_uc_sf_atch, _template_5_turn_motion_ground_hpl_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_20.location, gralin_20.orientation)
        gralin_20.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_20.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.gralin_20', exc)

    try:
        uel_spring_j_1 = get_object('.template_5_turn_motion.gel_upper_cylinder.uel_spring_j_1')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        uel_spring_j_1.relative_to = relative_to
        uel_spring_j_1.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.uel_spring_j_1')
        _template_5_turn_motion_ground_cfl_uc_top = get_object('.template_5_turn_motion.ground.cfl_uc_top')
        uel_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_spring_j_1.location, uel_spring_j_1.orientation)
        uel_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.uel_spring_j_1', exc)

    try:
        uel_damper_j_1 = get_object('.template_5_turn_motion.gel_upper_cylinder.uel_damper_j_1')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        uel_damper_j_1.relative_to = relative_to
        uel_damper_j_1.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.uel_damper_j_1')
        _template_5_turn_motion_ground_cfl_uc_top = get_object('.template_5_turn_motion.ground.cfl_uc_top')
        uel_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_damper_j_1.location, uel_damper_j_1.orientation)
        uel_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.uel_damper_j_1', exc)

    try:
        uel_stopper_j_1 = get_object('.template_5_turn_motion.gel_upper_cylinder.uel_stopper_j_1')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        uel_stopper_j_1.relative_to = relative_to
        uel_stopper_j_1.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.uel_stopper_j_1')
        _template_5_turn_motion_ground_cfl_uc_top = get_object('.template_5_turn_motion.ground.cfl_uc_top')
        uel_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_j_1.location, uel_stopper_j_1.orientation)
        uel_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.uel_stopper_j_1', exc)

    try:
        jxl_joint_i_7 = get_object('.template_5_turn_motion.gel_upper_cylinder.jxl_joint_i_7')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        jxl_joint_i_7.relative_to = relative_to
        jxl_joint_i_7.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.jxl_joint_i_7')
        _template_5_turn_motion_gel_lwract_jxl_joint_j_7 = get_object('.template_5_turn_motion.gel_lwract.jxl_joint_j_7')
        jxl_joint_i_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lwract_jxl_joint_j_7))
        _template_5_turn_motion_gel_lwract_jxl_joint_j_7 = get_object('.template_5_turn_motion.gel_lwract.jxl_joint_j_7')
        jxl_joint_i_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lwract_jxl_joint_j_7))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_7.location, jxl_joint_i_7.orientation)
        jxl_joint_i_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.jxl_joint_i_7', exc)

    try:
        uel_actuator_j_3 = get_object('.template_5_turn_motion.gel_upper_cylinder.uel_actuator_j_3')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        uel_actuator_j_3.relative_to = relative_to
        uel_actuator_j_3.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.uel_actuator_j_3')
        _template_5_turn_motion_ground_cfl_uc_sf_atch = get_object('.template_5_turn_motion.ground.cfl_uc_sf_atch')
        uel_actuator_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_uc_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_j_3.location, uel_actuator_j_3.orientation)
        uel_actuator_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.uel_actuator_j_3', exc)

    try:
        gralin_upper_cylinder = get_object('.template_5_turn_motion.gel_upper_cylinder.gralin_upper_cylinder')
        gralin_upper_cylinder.cylinder_name = target_path('.template_5_turn_motion.gel_upper_cylinder.gralin_upper_cylinder')
        _template_5_turn_motion_ground_cfl_uc_top = get_object('.template_5_turn_motion.ground.cfl_uc_top').location
        _template_5_turn_motion_ground_cfl_uc_bot = get_object('.template_5_turn_motion.ground.cfl_uc_bot').location
        gralin_upper_cylinder.length = (VecUtils.DM(_template_5_turn_motion_ground_cfl_uc_top, _template_5_turn_motion_ground_cfl_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_upper_cylinder.gralin_upper_cylinder', exc)

    try:
        gralin_geom = get_object('.template_5_turn_motion.gel_upper_cylinder.gralin_geom')
        gralin_geom.cylinder_name = target_path('.template_5_turn_motion.gel_upper_cylinder.gralin_geom')
        _template_5_turn_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpl_ib_uc_sf_atch').location
        _template_5_turn_motion_ground_hpl_uc_geompt = get_object('.template_5_turn_motion.ground.hpl_uc_geompt').location
        gralin_geom.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_ib_uc_sf_atch, _template_5_turn_motion_ground_hpl_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_upper_cylinder.gralin_geom', exc)

    try:
        gralin_geom3 = get_object('.template_5_turn_motion.gel_upper_cylinder.gralin_geom3')
        gralin_geom3.cylinder_name = target_path('.template_5_turn_motion.gel_upper_cylinder.gralin_geom3')
        _template_5_turn_motion_ground_hpl_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpl_ib_uc_sf_atch').location
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top').location
        gralin_geom3.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_ib_uc_sf_atch, _template_5_turn_motion_ground_hpl_uc_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_upper_cylinder.gralin_geom3', exc)

    try:
        MARKER_267 = get_object('.template_5_turn_motion.gel_upper_cylinder.MARKER_267')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        MARKER_267.relative_to = relative_to
        MARKER_267.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.MARKER_267')
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top')
        MARKER_267.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_267.location, MARKER_267.orientation)
        MARKER_267.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.MARKER_267', exc)

    try:
        MARKER_446 = get_object('.template_5_turn_motion.gel_upper_cylinder.MARKER_446')
        relative_to = get_object('.template_5_turn_motion.gel_upper_cylinder')
        MARKER_446.relative_to = relative_to
        MARKER_446.marker_name = target_path('.template_5_turn_motion.gel_upper_cylinder.MARKER_446')
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top')
        MARKER_446.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_446.location, MARKER_446.orientation)
        MARKER_446.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_cylinder.MARKER_446', exc)

    try:
        uer_gearaero_i_1 = get_object('.template_5_turn_motion.ger_upper_cylinder.uer_gearaero_i_1')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        uer_gearaero_i_1.relative_to = relative_to
        uer_gearaero_i_1.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.uer_gearaero_i_1')
        _template_5_turn_motion_ground_cfr_lc_top = get_object('.template_5_turn_motion.ground.cfr_lc_top')
        uer_gearaero_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_gearaero_i_1.location, uer_gearaero_i_1.orientation)
        uer_gearaero_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.uer_gearaero_i_1', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_upper_cylinder.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.inertia_frame')
        _template_5_turn_motion_ger_upper_cylinder_cm = get_object('.template_5_turn_motion.ger_upper_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_cylinder_cm))
        _template_5_turn_motion_ger_upper_cylinder = get_object('.template_5_turn_motion.ger_upper_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.inertia_frame', exc)

    try:
        gralin_13 = get_object('.template_5_turn_motion.ger_upper_cylinder.gralin_13')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        gralin_13.relative_to = relative_to
        gralin_13.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.gralin_13')
        _template_5_turn_motion_ground_cfr_uc_top = get_object('.template_5_turn_motion.ground.cfr_uc_top')
        gralin_13.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_uc_top))
        _template_5_turn_motion_ground_cfr_uc_top = get_object('.template_5_turn_motion.ground.cfr_uc_top').location
        _template_5_turn_motion_ground_cfr_uc_bot = get_object('.template_5_turn_motion.ground.cfr_uc_bot').location
        gralin_13.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_cfr_uc_top, _template_5_turn_motion_ground_cfr_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_13.location, gralin_13.orientation)
        gralin_13.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_13.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.gralin_13', exc)

    try:
        gralin_17 = get_object('.template_5_turn_motion.ger_upper_cylinder.gralin_17')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        gralin_17.relative_to = relative_to
        gralin_17.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.gralin_17')
        _template_5_turn_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpr_ib_uc_sf_atch')
        gralin_17.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_ib_uc_sf_atch))
        _template_5_turn_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpr_ib_uc_sf_atch').location
        _template_5_turn_motion_ground_hpr_uc_geompt = get_object('.template_5_turn_motion.ground.hpr_uc_geompt').location
        gralin_17.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_ib_uc_sf_atch, _template_5_turn_motion_ground_hpr_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_17.location, gralin_17.orientation)
        gralin_17.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_17.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.gralin_17', exc)

    try:
        gralin_21 = get_object('.template_5_turn_motion.ger_upper_cylinder.gralin_21')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        gralin_21.relative_to = relative_to
        gralin_21.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.gralin_21')
        _template_5_turn_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpr_ib_uc_sf_atch')
        gralin_21.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_ib_uc_sf_atch))
        _template_5_turn_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpr_ib_uc_sf_atch').location
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top').location
        gralin_21.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_ib_uc_sf_atch, _template_5_turn_motion_ground_hpr_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_21.location, gralin_21.orientation)
        gralin_21.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_21.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.gralin_21', exc)

    try:
        uer_spring_j_1 = get_object('.template_5_turn_motion.ger_upper_cylinder.uer_spring_j_1')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        uer_spring_j_1.relative_to = relative_to
        uer_spring_j_1.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.uer_spring_j_1')
        _template_5_turn_motion_ground_cfr_uc_top = get_object('.template_5_turn_motion.ground.cfr_uc_top')
        uer_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_spring_j_1.location, uer_spring_j_1.orientation)
        uer_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.uer_spring_j_1', exc)

    try:
        uer_damper_j_1 = get_object('.template_5_turn_motion.ger_upper_cylinder.uer_damper_j_1')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        uer_damper_j_1.relative_to = relative_to
        uer_damper_j_1.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.uer_damper_j_1')
        _template_5_turn_motion_ground_cfr_uc_top = get_object('.template_5_turn_motion.ground.cfr_uc_top')
        uer_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_damper_j_1.location, uer_damper_j_1.orientation)
        uer_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.uer_damper_j_1', exc)

    try:
        uer_stopper_j_1 = get_object('.template_5_turn_motion.ger_upper_cylinder.uer_stopper_j_1')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        uer_stopper_j_1.relative_to = relative_to
        uer_stopper_j_1.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.uer_stopper_j_1')
        _template_5_turn_motion_ground_cfr_uc_top = get_object('.template_5_turn_motion.ground.cfr_uc_top')
        uer_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_stopper_j_1.location, uer_stopper_j_1.orientation)
        uer_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.uer_stopper_j_1', exc)

    try:
        jxr_joint_i_7 = get_object('.template_5_turn_motion.ger_upper_cylinder.jxr_joint_i_7')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        jxr_joint_i_7.relative_to = relative_to
        jxr_joint_i_7.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.jxr_joint_i_7')
        _template_5_turn_motion_ger_lwract_jxr_joint_j_7 = get_object('.template_5_turn_motion.ger_lwract.jxr_joint_j_7')
        jxr_joint_i_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lwract_jxr_joint_j_7))
        _template_5_turn_motion_ger_lwract_jxr_joint_j_7 = get_object('.template_5_turn_motion.ger_lwract.jxr_joint_j_7')
        jxr_joint_i_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lwract_jxr_joint_j_7))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_7.location, jxr_joint_i_7.orientation)
        jxr_joint_i_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.jxr_joint_i_7', exc)

    try:
        uer_actuator_j_3 = get_object('.template_5_turn_motion.ger_upper_cylinder.uer_actuator_j_3')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        uer_actuator_j_3.relative_to = relative_to
        uer_actuator_j_3.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.uer_actuator_j_3')
        _template_5_turn_motion_ground_cfr_uc_sf_atch = get_object('.template_5_turn_motion.ground.cfr_uc_sf_atch')
        uer_actuator_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_uc_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_j_3.location, uer_actuator_j_3.orientation)
        uer_actuator_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.uer_actuator_j_3', exc)

    try:
        gralin_upper_cylinder = get_object('.template_5_turn_motion.ger_upper_cylinder.gralin_upper_cylinder')
        gralin_upper_cylinder.cylinder_name = target_path('.template_5_turn_motion.ger_upper_cylinder.gralin_upper_cylinder')
        _template_5_turn_motion_ground_cfr_uc_top = get_object('.template_5_turn_motion.ground.cfr_uc_top').location
        _template_5_turn_motion_ground_cfr_uc_bot = get_object('.template_5_turn_motion.ground.cfr_uc_bot').location
        gralin_upper_cylinder.length = (VecUtils.DM(_template_5_turn_motion_ground_cfr_uc_top, _template_5_turn_motion_ground_cfr_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_upper_cylinder.gralin_upper_cylinder', exc)

    try:
        gralin_geom = get_object('.template_5_turn_motion.ger_upper_cylinder.gralin_geom')
        gralin_geom.cylinder_name = target_path('.template_5_turn_motion.ger_upper_cylinder.gralin_geom')
        _template_5_turn_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpr_ib_uc_sf_atch').location
        _template_5_turn_motion_ground_hpr_uc_geompt = get_object('.template_5_turn_motion.ground.hpr_uc_geompt').location
        gralin_geom.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_ib_uc_sf_atch, _template_5_turn_motion_ground_hpr_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_upper_cylinder.gralin_geom', exc)

    try:
        gralin_geom3 = get_object('.template_5_turn_motion.ger_upper_cylinder.gralin_geom3')
        gralin_geom3.cylinder_name = target_path('.template_5_turn_motion.ger_upper_cylinder.gralin_geom3')
        _template_5_turn_motion_ground_hpr_ib_uc_sf_atch = get_object('.template_5_turn_motion.ground.hpr_ib_uc_sf_atch').location
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top').location
        gralin_geom3.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_ib_uc_sf_atch, _template_5_turn_motion_ground_hpr_uc_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_upper_cylinder.gralin_geom3', exc)

    try:
        MARKER_269 = get_object('.template_5_turn_motion.ger_upper_cylinder.MARKER_269')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        MARKER_269.relative_to = relative_to
        MARKER_269.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.MARKER_269')
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top')
        MARKER_269.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_269.location, MARKER_269.orientation)
        MARKER_269.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.MARKER_269', exc)

    try:
        MARKER_444 = get_object('.template_5_turn_motion.ger_upper_cylinder.MARKER_444')
        relative_to = get_object('.template_5_turn_motion.ger_upper_cylinder')
        MARKER_444.relative_to = relative_to
        MARKER_444.marker_name = target_path('.template_5_turn_motion.ger_upper_cylinder.MARKER_444')
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top')
        MARKER_444.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_444.location, MARKER_444.orientation)
        MARKER_444.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_cylinder.MARKER_444', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_lower_cylinder.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.inertia_frame')
        _template_5_turn_motion_gel_lower_cylinder_cm = get_object('.template_5_turn_motion.gel_lower_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lower_cylinder_cm))
        _template_5_turn_motion_gel_lower_cylinder = get_object('.template_5_turn_motion.gel_lower_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lower_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.inertia_frame', exc)

    try:
        gralin_14 = get_object('.template_5_turn_motion.gel_lower_cylinder.gralin_14')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        gralin_14.relative_to = relative_to
        gralin_14.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.gralin_14')
        _template_5_turn_motion_ground_cfl_lc_top = get_object('.template_5_turn_motion.ground.cfl_lc_top')
        gralin_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_lc_top))
        _template_5_turn_motion_ground_cfl_lc_top = get_object('.template_5_turn_motion.ground.cfl_lc_top').location
        _template_5_turn_motion_ground_hpl_lc_bot = get_object('.template_5_turn_motion.ground.hpl_lc_bot').location
        gralin_14.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_cfl_lc_top, _template_5_turn_motion_ground_hpl_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_14.location, gralin_14.orientation)
        gralin_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.gralin_14', exc)

    try:
        gralin_22 = get_object('.template_5_turn_motion.gel_lower_cylinder.gralin_22')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        gralin_22.relative_to = relative_to
        gralin_22.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.gralin_22')
        _template_5_turn_motion_ground_hpl_ib_axle = get_object('.template_5_turn_motion.ground.hpl_ib_axle')
        gralin_22.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_ib_axle))
        _template_5_turn_motion_ground_hpl_ib_axle = get_object('.template_5_turn_motion.ground.hpl_ib_axle').location
        _template_5_turn_motion_ground_hpl_ob_axle = get_object('.template_5_turn_motion.ground.hpl_ob_axle').location
        gralin_22.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_ib_axle, _template_5_turn_motion_ground_hpl_ob_axle, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_22.location, gralin_22.orientation)
        gralin_22.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_22.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.gralin_22', exc)

    try:
        jxl_joint_j_11 = get_object('.template_5_turn_motion.gel_lower_cylinder.jxl_joint_j_11')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        jxl_joint_j_11.relative_to = relative_to
        jxl_joint_j_11.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.jxl_joint_j_11')
        _template_5_turn_motion_ground_hpl_lta_lc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_lc_atch_1')
        jxl_joint_j_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_lta_lc_atch_1))
        _template_5_turn_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_connect_atch_1').location
        _template_5_turn_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_1').location
        jxl_joint_j_11.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_lta_connect_atch_1, _template_5_turn_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_11.location, jxl_joint_j_11.orientation)
        jxl_joint_j_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.jxl_joint_j_11', exc)

    try:
        jxl_joint_i_12 = get_object('.template_5_turn_motion.gel_lower_cylinder.jxl_joint_i_12')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        jxl_joint_i_12.relative_to = relative_to
        jxl_joint_i_12.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.jxl_joint_i_12')
        _template_5_turn_motion_gel_upper_cylinder_jxl_joint_j_12 = get_object('.template_5_turn_motion.gel_upper_cylinder.jxl_joint_j_12')
        jxl_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_cylinder_jxl_joint_j_12))
        _template_5_turn_motion_gel_upper_cylinder_jxl_joint_j_12 = get_object('.template_5_turn_motion.gel_upper_cylinder.jxl_joint_j_12')
        jxl_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_cylinder_jxl_joint_j_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_12.location, jxl_joint_i_12.orientation)
        jxl_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.jxl_joint_i_12', exc)

    try:
        coomarker_1 = get_object('.template_5_turn_motion.gel_lower_cylinder.coomarker_1')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        coomarker_1.relative_to = relative_to
        coomarker_1.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.coomarker_1')
        _template_5_turn_motion_ground_cfl_spin_axis = get_object('.template_5_turn_motion.ground.cfl_spin_axis')
        coomarker_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_spin_axis))
        _template_5_turn_motion_ground_cfl_spin_axis = get_object('.template_5_turn_motion.ground.cfl_spin_axis')
        coomarker_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_spin_axis))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_1.location, coomarker_1.orientation)
        coomarker_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.coomarker_1', exc)

    try:
        uel_spring_i_1 = get_object('.template_5_turn_motion.gel_lower_cylinder.uel_spring_i_1')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        uel_spring_i_1.relative_to = relative_to
        uel_spring_i_1.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.uel_spring_i_1')
        _template_5_turn_motion_ground_cfl_lc_top = get_object('.template_5_turn_motion.ground.cfl_lc_top')
        uel_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_spring_i_1.location, uel_spring_i_1.orientation)
        uel_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.uel_spring_i_1', exc)

    try:
        uel_damper_i_1 = get_object('.template_5_turn_motion.gel_lower_cylinder.uel_damper_i_1')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        uel_damper_i_1.relative_to = relative_to
        uel_damper_i_1.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.uel_damper_i_1')
        _template_5_turn_motion_ground_cfl_lc_top = get_object('.template_5_turn_motion.ground.cfl_lc_top')
        uel_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_damper_i_1.location, uel_damper_i_1.orientation)
        uel_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.uel_damper_i_1', exc)

    try:
        uel_stopper_i_1 = get_object('.template_5_turn_motion.gel_lower_cylinder.uel_stopper_i_1')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        uel_stopper_i_1.relative_to = relative_to
        uel_stopper_i_1.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.uel_stopper_i_1')
        _template_5_turn_motion_ground_cfl_lc_top = get_object('.template_5_turn_motion.ground.cfl_lc_top')
        uel_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_i_1.location, uel_stopper_i_1.orientation)
        uel_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.uel_stopper_i_1', exc)

    try:
        gralin_lower_cylinder = get_object('.template_5_turn_motion.gel_lower_cylinder.gralin_lower_cylinder')
        gralin_lower_cylinder.cylinder_name = target_path('.template_5_turn_motion.gel_lower_cylinder.gralin_lower_cylinder')
        _template_5_turn_motion_ground_cfl_lc_top = get_object('.template_5_turn_motion.ground.cfl_lc_top').location
        _template_5_turn_motion_ground_hpl_lc_bot = get_object('.template_5_turn_motion.ground.hpl_lc_bot').location
        gralin_lower_cylinder.length = (VecUtils.DM(_template_5_turn_motion_ground_cfl_lc_top, _template_5_turn_motion_ground_hpl_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_lower_cylinder.gralin_lower_cylinder', exc)

    try:
        gralin_geom = get_object('.template_5_turn_motion.gel_lower_cylinder.gralin_geom')
        gralin_geom.cylinder_name = target_path('.template_5_turn_motion.gel_lower_cylinder.gralin_geom')
        _template_5_turn_motion_ground_hpl_ib_axle = get_object('.template_5_turn_motion.ground.hpl_ib_axle').location
        _template_5_turn_motion_ground_hpl_ob_axle = get_object('.template_5_turn_motion.ground.hpl_ob_axle').location
        gralin_geom.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_ib_axle, _template_5_turn_motion_ground_hpl_ob_axle))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_lower_cylinder.gralin_geom', exc)

    try:
        MARKER_495 = get_object('.template_5_turn_motion.gel_lower_cylinder.MARKER_495')
        relative_to = get_object('.template_5_turn_motion.gel_lower_cylinder')
        MARKER_495.relative_to = relative_to
        MARKER_495.marker_name = target_path('.template_5_turn_motion.gel_lower_cylinder.MARKER_495')
        _template_5_turn_motion_ground_hpl_wheel_center = get_object('.template_5_turn_motion.ground.hpl_wheel_center')
        MARKER_495.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_495.location, MARKER_495.orientation)
        MARKER_495.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_cylinder.MARKER_495', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_lower_cylinder.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.inertia_frame')
        _template_5_turn_motion_ger_lower_cylinder_cm = get_object('.template_5_turn_motion.ger_lower_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lower_cylinder_cm))
        _template_5_turn_motion_ger_lower_cylinder = get_object('.template_5_turn_motion.ger_lower_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lower_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.inertia_frame', exc)

    try:
        gralin_15 = get_object('.template_5_turn_motion.ger_lower_cylinder.gralin_15')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        gralin_15.relative_to = relative_to
        gralin_15.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.gralin_15')
        _template_5_turn_motion_ground_cfr_lc_top = get_object('.template_5_turn_motion.ground.cfr_lc_top')
        gralin_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_lc_top))
        _template_5_turn_motion_ground_cfr_lc_top = get_object('.template_5_turn_motion.ground.cfr_lc_top').location
        _template_5_turn_motion_ground_hpr_lc_bot = get_object('.template_5_turn_motion.ground.hpr_lc_bot').location
        gralin_15.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_cfr_lc_top, _template_5_turn_motion_ground_hpr_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_15.location, gralin_15.orientation)
        gralin_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.gralin_15', exc)

    try:
        gralin_23 = get_object('.template_5_turn_motion.ger_lower_cylinder.gralin_23')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        gralin_23.relative_to = relative_to
        gralin_23.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.gralin_23')
        _template_5_turn_motion_ground_hpr_ib_axle = get_object('.template_5_turn_motion.ground.hpr_ib_axle')
        gralin_23.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_ib_axle))
        _template_5_turn_motion_ground_hpr_ib_axle = get_object('.template_5_turn_motion.ground.hpr_ib_axle').location
        _template_5_turn_motion_ground_hpr_ob_axle = get_object('.template_5_turn_motion.ground.hpr_ob_axle').location
        gralin_23.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_ib_axle, _template_5_turn_motion_ground_hpr_ob_axle, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_23.location, gralin_23.orientation)
        gralin_23.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_23.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.gralin_23', exc)

    try:
        jxr_joint_j_11 = get_object('.template_5_turn_motion.ger_lower_cylinder.jxr_joint_j_11')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        jxr_joint_j_11.relative_to = relative_to
        jxr_joint_j_11.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.jxr_joint_j_11')
        _template_5_turn_motion_ground_hpr_lta_lc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_lc_atch_1')
        jxr_joint_j_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_lta_lc_atch_1))
        _template_5_turn_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_connect_atch_1').location
        _template_5_turn_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_1').location
        jxr_joint_j_11.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_lta_connect_atch_1, _template_5_turn_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_11.location, jxr_joint_j_11.orientation)
        jxr_joint_j_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.jxr_joint_j_11', exc)

    try:
        jxr_joint_i_12 = get_object('.template_5_turn_motion.ger_lower_cylinder.jxr_joint_i_12')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        jxr_joint_i_12.relative_to = relative_to
        jxr_joint_i_12.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.jxr_joint_i_12')
        _template_5_turn_motion_ger_upper_cylinder_jxr_joint_j_12 = get_object('.template_5_turn_motion.ger_upper_cylinder.jxr_joint_j_12')
        jxr_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_cylinder_jxr_joint_j_12))
        _template_5_turn_motion_ger_upper_cylinder_jxr_joint_j_12 = get_object('.template_5_turn_motion.ger_upper_cylinder.jxr_joint_j_12')
        jxr_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_cylinder_jxr_joint_j_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_12.location, jxr_joint_i_12.orientation)
        jxr_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.jxr_joint_i_12', exc)

    try:
        coomarker_2 = get_object('.template_5_turn_motion.ger_lower_cylinder.coomarker_2')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        coomarker_2.relative_to = relative_to
        coomarker_2.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.coomarker_2')
        _template_5_turn_motion_ground_cfr_spin_axis = get_object('.template_5_turn_motion.ground.cfr_spin_axis')
        coomarker_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_spin_axis))
        _template_5_turn_motion_ground_cfr_spin_axis = get_object('.template_5_turn_motion.ground.cfr_spin_axis')
        coomarker_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_spin_axis))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_2.location, coomarker_2.orientation)
        coomarker_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.coomarker_2', exc)

    try:
        uer_spring_i_1 = get_object('.template_5_turn_motion.ger_lower_cylinder.uer_spring_i_1')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        uer_spring_i_1.relative_to = relative_to
        uer_spring_i_1.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.uer_spring_i_1')
        _template_5_turn_motion_ground_cfr_lc_top = get_object('.template_5_turn_motion.ground.cfr_lc_top')
        uer_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_spring_i_1.location, uer_spring_i_1.orientation)
        uer_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.uer_spring_i_1', exc)

    try:
        uer_damper_i_1 = get_object('.template_5_turn_motion.ger_lower_cylinder.uer_damper_i_1')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        uer_damper_i_1.relative_to = relative_to
        uer_damper_i_1.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.uer_damper_i_1')
        _template_5_turn_motion_ground_cfr_lc_top = get_object('.template_5_turn_motion.ground.cfr_lc_top')
        uer_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_damper_i_1.location, uer_damper_i_1.orientation)
        uer_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.uer_damper_i_1', exc)

    try:
        uer_stopper_i_1 = get_object('.template_5_turn_motion.ger_lower_cylinder.uer_stopper_i_1')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        uer_stopper_i_1.relative_to = relative_to
        uer_stopper_i_1.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.uer_stopper_i_1')
        _template_5_turn_motion_ground_cfr_lc_top = get_object('.template_5_turn_motion.ground.cfr_lc_top')
        uer_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_stopper_i_1.location, uer_stopper_i_1.orientation)
        uer_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.uer_stopper_i_1', exc)

    try:
        gralin_lower_cylinder = get_object('.template_5_turn_motion.ger_lower_cylinder.gralin_lower_cylinder')
        gralin_lower_cylinder.cylinder_name = target_path('.template_5_turn_motion.ger_lower_cylinder.gralin_lower_cylinder')
        _template_5_turn_motion_ground_cfr_lc_top = get_object('.template_5_turn_motion.ground.cfr_lc_top').location
        _template_5_turn_motion_ground_hpr_lc_bot = get_object('.template_5_turn_motion.ground.hpr_lc_bot').location
        gralin_lower_cylinder.length = (VecUtils.DM(_template_5_turn_motion_ground_cfr_lc_top, _template_5_turn_motion_ground_hpr_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_lower_cylinder.gralin_lower_cylinder', exc)

    try:
        gralin_geom = get_object('.template_5_turn_motion.ger_lower_cylinder.gralin_geom')
        gralin_geom.cylinder_name = target_path('.template_5_turn_motion.ger_lower_cylinder.gralin_geom')
        _template_5_turn_motion_ground_hpr_ib_axle = get_object('.template_5_turn_motion.ground.hpr_ib_axle').location
        _template_5_turn_motion_ground_hpr_ob_axle = get_object('.template_5_turn_motion.ground.hpr_ob_axle').location
        gralin_geom.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_ib_axle, _template_5_turn_motion_ground_hpr_ob_axle))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_lower_cylinder.gralin_geom', exc)

    try:
        MARKER_498 = get_object('.template_5_turn_motion.ger_lower_cylinder.MARKER_498')
        relative_to = get_object('.template_5_turn_motion.ger_lower_cylinder')
        MARKER_498.relative_to = relative_to
        MARKER_498.marker_name = target_path('.template_5_turn_motion.ger_lower_cylinder.MARKER_498')
        _template_5_turn_motion_ground_hpr_wheel_center = get_object('.template_5_turn_motion.ground.hpr_wheel_center')
        MARKER_498.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_498.location, MARKER_498.orientation)
        MARKER_498.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_cylinder.MARKER_498', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_upper_dragbrace.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_upper_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_upper_dragbrace.inertia_frame')
        _template_5_turn_motion_gel_upper_dragbrace_cm = get_object('.template_5_turn_motion.gel_upper_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_dragbrace_cm))
        _template_5_turn_motion_gel_upper_dragbrace = get_object('.template_5_turn_motion.gel_upper_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_dragbrace.inertia_frame', exc)

    try:
        gralin_24 = get_object('.template_5_turn_motion.gel_upper_dragbrace.gralin_24')
        relative_to = get_object('.template_5_turn_motion.gel_upper_dragbrace')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_5_turn_motion.gel_upper_dragbrace.gralin_24')
        _template_5_turn_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpl_udb_spndl_atch_1')
        gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_udb_spndl_atch_1))
        _template_5_turn_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpl_udb_spndl_atch_1').location
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_udb_spndl_atch_1, _template_5_turn_motion_ground_hpl_ldb_udb_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_dragbrace.gralin_24', exc)

    try:
        jxl_joint_j_14 = get_object('.template_5_turn_motion.gel_upper_dragbrace.jxl_joint_j_14')
        relative_to = get_object('.template_5_turn_motion.gel_upper_dragbrace')
        jxl_joint_j_14.relative_to = relative_to
        jxl_joint_j_14.marker_name = target_path('.template_5_turn_motion.gel_upper_dragbrace.jxl_joint_j_14')
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1')
        jxl_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_ldb_udb_atch_1))
        _template_5_turn_motion_ground_cfl_plane_ref_2 = get_object('.template_5_turn_motion.ground.cfl_plane_ref_2')
        jxl_joint_j_14.orientation = _template_5_turn_motion_ground_cfl_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_14.location, jxl_joint_j_14.orientation)
        jxl_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_dragbrace.jxl_joint_j_14', exc)

    try:
        jxl_joint_i_5 = get_object('.template_5_turn_motion.gel_upper_dragbrace.jxl_joint_i_5')
        relative_to = get_object('.template_5_turn_motion.gel_upper_dragbrace')
        jxl_joint_i_5.relative_to = relative_to
        jxl_joint_i_5.marker_name = target_path('.template_5_turn_motion.gel_upper_dragbrace.jxl_joint_i_5')
        _template_5_turn_motion_gel_spindle_jxl_joint_j_5 = get_object('.template_5_turn_motion.gel_spindle.jxl_joint_j_5')
        jxl_joint_i_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_spindle_jxl_joint_j_5))
        _template_5_turn_motion_gel_upper_dragbrace_jxl_joint_i_5 = get_object('.template_5_turn_motion.gel_upper_dragbrace.jxl_joint_i_5').location
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpl_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpl_spndl_sf_atch').location
        jxl_joint_i_5.orientation = (VecUtils.ORI_IN_PLANE(_template_5_turn_motion_gel_upper_dragbrace_jxl_joint_i_5, _template_5_turn_motion_ground_hpl_ldb_udb_atch_1, _template_5_turn_motion_ground_hpl_spndl_sf_atch, "Z_ZX"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_5.location, jxl_joint_i_5.orientation)
        jxl_joint_i_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_dragbrace.jxl_joint_i_5', exc)

    try:
        uel_actuator_i_3 = get_object('.template_5_turn_motion.gel_upper_dragbrace.uel_actuator_i_3')
        relative_to = get_object('.template_5_turn_motion.gel_upper_dragbrace')
        uel_actuator_i_3.relative_to = relative_to
        uel_actuator_i_3.marker_name = target_path('.template_5_turn_motion.gel_upper_dragbrace.uel_actuator_i_3')
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1')
        uel_actuator_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_ldb_udb_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_i_3.location, uel_actuator_i_3.orientation)
        uel_actuator_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_dragbrace.uel_actuator_i_3', exc)

    try:
        gralin_upper_dragbrace = get_object('.template_5_turn_motion.gel_upper_dragbrace.gralin_upper_dragbrace')
        gralin_upper_dragbrace.cylinder_name = target_path('.template_5_turn_motion.gel_upper_dragbrace.gralin_upper_dragbrace')
        _template_5_turn_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpl_udb_spndl_atch_1').location
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1').location
        gralin_upper_dragbrace.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_udb_spndl_atch_1, _template_5_turn_motion_ground_hpl_ldb_udb_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_upper_dragbrace.gralin_upper_dragbrace', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_upper_dragbrace.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_upper_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_upper_dragbrace.inertia_frame')
        _template_5_turn_motion_ger_upper_dragbrace_cm = get_object('.template_5_turn_motion.ger_upper_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_dragbrace_cm))
        _template_5_turn_motion_ger_upper_dragbrace = get_object('.template_5_turn_motion.ger_upper_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_dragbrace.inertia_frame', exc)

    try:
        gralin_25 = get_object('.template_5_turn_motion.ger_upper_dragbrace.gralin_25')
        relative_to = get_object('.template_5_turn_motion.ger_upper_dragbrace')
        gralin_25.relative_to = relative_to
        gralin_25.marker_name = target_path('.template_5_turn_motion.ger_upper_dragbrace.gralin_25')
        _template_5_turn_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpr_udb_spndl_atch_1')
        gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_udb_spndl_atch_1))
        _template_5_turn_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpr_udb_spndl_atch_1').location
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1').location
        gralin_25.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_udb_spndl_atch_1, _template_5_turn_motion_ground_hpr_ldb_udb_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_25.location, gralin_25.orientation)
        gralin_25.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_25.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_dragbrace.gralin_25', exc)

    try:
        jxr_joint_j_14 = get_object('.template_5_turn_motion.ger_upper_dragbrace.jxr_joint_j_14')
        relative_to = get_object('.template_5_turn_motion.ger_upper_dragbrace')
        jxr_joint_j_14.relative_to = relative_to
        jxr_joint_j_14.marker_name = target_path('.template_5_turn_motion.ger_upper_dragbrace.jxr_joint_j_14')
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1')
        jxr_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_ldb_udb_atch_1))
        _template_5_turn_motion_ground_cfr_plane_ref_2 = get_object('.template_5_turn_motion.ground.cfr_plane_ref_2')
        jxr_joint_j_14.orientation = _template_5_turn_motion_ground_cfr_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_14.location, jxr_joint_j_14.orientation)
        jxr_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_dragbrace.jxr_joint_j_14', exc)

    try:
        jxr_joint_i_5 = get_object('.template_5_turn_motion.ger_upper_dragbrace.jxr_joint_i_5')
        relative_to = get_object('.template_5_turn_motion.ger_upper_dragbrace')
        jxr_joint_i_5.relative_to = relative_to
        jxr_joint_i_5.marker_name = target_path('.template_5_turn_motion.ger_upper_dragbrace.jxr_joint_i_5')
        _template_5_turn_motion_ger_spindle_jxr_joint_j_5 = get_object('.template_5_turn_motion.ger_spindle.jxr_joint_j_5')
        jxr_joint_i_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_spindle_jxr_joint_j_5))
        _template_5_turn_motion_ger_upper_dragbrace_jxr_joint_i_5 = get_object('.template_5_turn_motion.ger_upper_dragbrace.jxr_joint_i_5').location
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpr_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpr_spndl_sf_atch').location
        jxr_joint_i_5.orientation = (VecUtils.ORI_IN_PLANE(_template_5_turn_motion_ger_upper_dragbrace_jxr_joint_i_5, _template_5_turn_motion_ground_hpr_ldb_udb_atch_1, _template_5_turn_motion_ground_hpr_spndl_sf_atch, "Z_ZX"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_5.location, jxr_joint_i_5.orientation)
        jxr_joint_i_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_dragbrace.jxr_joint_i_5', exc)

    try:
        uer_actuator_i_3 = get_object('.template_5_turn_motion.ger_upper_dragbrace.uer_actuator_i_3')
        relative_to = get_object('.template_5_turn_motion.ger_upper_dragbrace')
        uer_actuator_i_3.relative_to = relative_to
        uer_actuator_i_3.marker_name = target_path('.template_5_turn_motion.ger_upper_dragbrace.uer_actuator_i_3')
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1')
        uer_actuator_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_ldb_udb_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_i_3.location, uer_actuator_i_3.orientation)
        uer_actuator_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_dragbrace.uer_actuator_i_3', exc)

    try:
        gralin_upper_dragbrace = get_object('.template_5_turn_motion.ger_upper_dragbrace.gralin_upper_dragbrace')
        gralin_upper_dragbrace.cylinder_name = target_path('.template_5_turn_motion.ger_upper_dragbrace.gralin_upper_dragbrace')
        _template_5_turn_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpr_udb_spndl_atch_1').location
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1').location
        gralin_upper_dragbrace.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_udb_spndl_atch_1, _template_5_turn_motion_ground_hpr_ldb_udb_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_upper_dragbrace.gralin_upper_dragbrace', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_lower_dragbrace.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_lower_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_lower_dragbrace.inertia_frame')
        _template_5_turn_motion_gel_lower_dragbrace_cm = get_object('.template_5_turn_motion.gel_lower_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lower_dragbrace_cm))
        _template_5_turn_motion_gel_lower_dragbrace = get_object('.template_5_turn_motion.gel_lower_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lower_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_dragbrace.inertia_frame', exc)

    try:
        gralin_26 = get_object('.template_5_turn_motion.gel_lower_dragbrace.gralin_26')
        relative_to = get_object('.template_5_turn_motion.gel_lower_dragbrace')
        gralin_26.relative_to = relative_to
        gralin_26.marker_name = target_path('.template_5_turn_motion.gel_lower_dragbrace.gralin_26')
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1')
        gralin_26.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_ldb_udb_atch_1))
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpl_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_collar_atch_1').location
        gralin_26.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_ldb_udb_atch_1, _template_5_turn_motion_ground_hpl_ldb_collar_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_26.location, gralin_26.orientation)
        gralin_26.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_26.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_dragbrace.gralin_26', exc)

    try:
        jxl_joint_i_14 = get_object('.template_5_turn_motion.gel_lower_dragbrace.jxl_joint_i_14')
        relative_to = get_object('.template_5_turn_motion.gel_lower_dragbrace')
        jxl_joint_i_14.relative_to = relative_to
        jxl_joint_i_14.marker_name = target_path('.template_5_turn_motion.gel_lower_dragbrace.jxl_joint_i_14')
        _template_5_turn_motion_gel_upper_dragbrace_jxl_joint_j_14 = get_object('.template_5_turn_motion.gel_upper_dragbrace.jxl_joint_j_14')
        jxl_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_dragbrace_jxl_joint_j_14))
        _template_5_turn_motion_gel_upper_dragbrace_jxl_joint_j_14 = get_object('.template_5_turn_motion.gel_upper_dragbrace.jxl_joint_j_14')
        jxl_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_dragbrace_jxl_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_14.location, jxl_joint_i_14.orientation)
        jxl_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_dragbrace.jxl_joint_i_14', exc)

    try:
        jxl_joint_i_10 = get_object('.template_5_turn_motion.gel_lower_dragbrace.jxl_joint_i_10')
        relative_to = get_object('.template_5_turn_motion.gel_lower_dragbrace')
        jxl_joint_i_10.relative_to = relative_to
        jxl_joint_i_10.marker_name = target_path('.template_5_turn_motion.gel_lower_dragbrace.jxl_joint_i_10')
        _template_5_turn_motion_gel_uc_collar_jxl_joint_j_10 = get_object('.template_5_turn_motion.gel_uc_collar.jxl_joint_j_10')
        jxl_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_uc_collar_jxl_joint_j_10))
        _template_5_turn_motion_gel_uc_collar_jxl_joint_j_10 = get_object('.template_5_turn_motion.gel_uc_collar.jxl_joint_j_10')
        jxl_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_uc_collar_jxl_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_10.location, jxl_joint_i_10.orientation)
        jxl_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_dragbrace.jxl_joint_i_10', exc)

    try:
        graarm_1 = get_object('.template_5_turn_motion.gel_lower_dragbrace.graarm_1')
        relative_to = get_object('.template_5_turn_motion.gel_lower_dragbrace')
        graarm_1.relative_to = relative_to
        graarm_1.marker_name = target_path('.template_5_turn_motion.gel_lower_dragbrace.graarm_1')
        _template_5_turn_motion_ground_hpl_uplock_tab = get_object('.template_5_turn_motion.ground.hpl_uplock_tab')
        graarm_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_uplock_tab))
        _template_5_turn_motion_ground_hpl_uplock_tab = get_object('.template_5_turn_motion.ground.hpl_uplock_tab').location
        _template_5_turn_motion_ground_cfl_ldb_geompt_1 = get_object('.template_5_turn_motion.ground.cfl_ldb_geompt_1').location
        _template_5_turn_motion_ground_cfl_ldb_geompt_2 = get_object('.template_5_turn_motion.ground.cfl_ldb_geompt_2').location
        graarm_1.orientation = (VecUtils.ORI_IN_PLANE(_template_5_turn_motion_ground_hpl_uplock_tab, _template_5_turn_motion_ground_cfl_ldb_geompt_1, _template_5_turn_motion_ground_cfl_ldb_geompt_2, "X_XY"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_1.location, graarm_1.orientation)
        graarm_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        graarm_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_dragbrace.graarm_1', exc)

    try:
        graarm_2 = get_object('.template_5_turn_motion.gel_lower_dragbrace.graarm_2')
        relative_to = get_object('.template_5_turn_motion.gel_lower_dragbrace')
        graarm_2.relative_to = relative_to
        graarm_2.marker_name = target_path('.template_5_turn_motion.gel_lower_dragbrace.graarm_2')
        _template_5_turn_motion_ground_cfl_ldb_geompt_1 = get_object('.template_5_turn_motion.ground.cfl_ldb_geompt_1')
        graarm_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_ldb_geompt_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_2.location, graarm_2.orientation)
        graarm_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_dragbrace.graarm_2', exc)

    try:
        graarm_3 = get_object('.template_5_turn_motion.gel_lower_dragbrace.graarm_3')
        relative_to = get_object('.template_5_turn_motion.gel_lower_dragbrace')
        graarm_3.relative_to = relative_to
        graarm_3.marker_name = target_path('.template_5_turn_motion.gel_lower_dragbrace.graarm_3')
        _template_5_turn_motion_ground_cfl_ldb_geompt_2 = get_object('.template_5_turn_motion.ground.cfl_ldb_geompt_2')
        graarm_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_ldb_geompt_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_3.location, graarm_3.orientation)
        graarm_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_dragbrace.graarm_3', exc)

    try:
        gralin_lower_dragbrace = get_object('.template_5_turn_motion.gel_lower_dragbrace.gralin_lower_dragbrace')
        gralin_lower_dragbrace.cylinder_name = target_path('.template_5_turn_motion.gel_lower_dragbrace.gralin_lower_dragbrace')
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpl_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_collar_atch_1').location
        gralin_lower_dragbrace.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_ldb_udb_atch_1, _template_5_turn_motion_ground_hpl_ldb_collar_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_lower_dragbrace.gralin_lower_dragbrace', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_lower_dragbrace.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_lower_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_lower_dragbrace.inertia_frame')
        _template_5_turn_motion_ger_lower_dragbrace_cm = get_object('.template_5_turn_motion.ger_lower_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lower_dragbrace_cm))
        _template_5_turn_motion_ger_lower_dragbrace = get_object('.template_5_turn_motion.ger_lower_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lower_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_dragbrace.inertia_frame', exc)

    try:
        gralin_27 = get_object('.template_5_turn_motion.ger_lower_dragbrace.gralin_27')
        relative_to = get_object('.template_5_turn_motion.ger_lower_dragbrace')
        gralin_27.relative_to = relative_to
        gralin_27.marker_name = target_path('.template_5_turn_motion.ger_lower_dragbrace.gralin_27')
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1')
        gralin_27.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_ldb_udb_atch_1))
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpr_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_collar_atch_1').location
        gralin_27.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_ldb_udb_atch_1, _template_5_turn_motion_ground_hpr_ldb_collar_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_27.location, gralin_27.orientation)
        gralin_27.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_27.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_dragbrace.gralin_27', exc)

    try:
        jxr_joint_i_14 = get_object('.template_5_turn_motion.ger_lower_dragbrace.jxr_joint_i_14')
        relative_to = get_object('.template_5_turn_motion.ger_lower_dragbrace')
        jxr_joint_i_14.relative_to = relative_to
        jxr_joint_i_14.marker_name = target_path('.template_5_turn_motion.ger_lower_dragbrace.jxr_joint_i_14')
        _template_5_turn_motion_ger_upper_dragbrace_jxr_joint_j_14 = get_object('.template_5_turn_motion.ger_upper_dragbrace.jxr_joint_j_14')
        jxr_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_dragbrace_jxr_joint_j_14))
        _template_5_turn_motion_ger_upper_dragbrace_jxr_joint_j_14 = get_object('.template_5_turn_motion.ger_upper_dragbrace.jxr_joint_j_14')
        jxr_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_dragbrace_jxr_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_14.location, jxr_joint_i_14.orientation)
        jxr_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_dragbrace.jxr_joint_i_14', exc)

    try:
        jxr_joint_i_10 = get_object('.template_5_turn_motion.ger_lower_dragbrace.jxr_joint_i_10')
        relative_to = get_object('.template_5_turn_motion.ger_lower_dragbrace')
        jxr_joint_i_10.relative_to = relative_to
        jxr_joint_i_10.marker_name = target_path('.template_5_turn_motion.ger_lower_dragbrace.jxr_joint_i_10')
        _template_5_turn_motion_ger_uc_collar_jxr_joint_j_10 = get_object('.template_5_turn_motion.ger_uc_collar.jxr_joint_j_10')
        jxr_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_uc_collar_jxr_joint_j_10))
        _template_5_turn_motion_ger_uc_collar_jxr_joint_j_10 = get_object('.template_5_turn_motion.ger_uc_collar.jxr_joint_j_10')
        jxr_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_uc_collar_jxr_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_10.location, jxr_joint_i_10.orientation)
        jxr_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_dragbrace.jxr_joint_i_10', exc)

    try:
        graarm_4 = get_object('.template_5_turn_motion.ger_lower_dragbrace.graarm_4')
        relative_to = get_object('.template_5_turn_motion.ger_lower_dragbrace')
        graarm_4.relative_to = relative_to
        graarm_4.marker_name = target_path('.template_5_turn_motion.ger_lower_dragbrace.graarm_4')
        _template_5_turn_motion_ground_hpr_uplock_tab = get_object('.template_5_turn_motion.ground.hpr_uplock_tab')
        graarm_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_uplock_tab))
        _template_5_turn_motion_ground_hpr_uplock_tab = get_object('.template_5_turn_motion.ground.hpr_uplock_tab').location
        _template_5_turn_motion_ground_cfr_ldb_geompt_1 = get_object('.template_5_turn_motion.ground.cfr_ldb_geompt_1').location
        _template_5_turn_motion_ground_cfr_ldb_geompt_2 = get_object('.template_5_turn_motion.ground.cfr_ldb_geompt_2').location
        graarm_4.orientation = (VecUtils.ORI_IN_PLANE(_template_5_turn_motion_ground_hpr_uplock_tab, _template_5_turn_motion_ground_cfr_ldb_geompt_1, _template_5_turn_motion_ground_cfr_ldb_geompt_2, "X_XY"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_4.location, graarm_4.orientation)
        graarm_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        graarm_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_dragbrace.graarm_4', exc)

    try:
        graarm_5 = get_object('.template_5_turn_motion.ger_lower_dragbrace.graarm_5')
        relative_to = get_object('.template_5_turn_motion.ger_lower_dragbrace')
        graarm_5.relative_to = relative_to
        graarm_5.marker_name = target_path('.template_5_turn_motion.ger_lower_dragbrace.graarm_5')
        _template_5_turn_motion_ground_cfr_ldb_geompt_1 = get_object('.template_5_turn_motion.ground.cfr_ldb_geompt_1')
        graarm_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_ldb_geompt_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_5.location, graarm_5.orientation)
        graarm_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_dragbrace.graarm_5', exc)

    try:
        graarm_6 = get_object('.template_5_turn_motion.ger_lower_dragbrace.graarm_6')
        relative_to = get_object('.template_5_turn_motion.ger_lower_dragbrace')
        graarm_6.relative_to = relative_to
        graarm_6.marker_name = target_path('.template_5_turn_motion.ger_lower_dragbrace.graarm_6')
        _template_5_turn_motion_ground_cfr_ldb_geompt_2 = get_object('.template_5_turn_motion.ground.cfr_ldb_geompt_2')
        graarm_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_ldb_geompt_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_6.location, graarm_6.orientation)
        graarm_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_dragbrace.graarm_6', exc)

    try:
        gralin_lower_dragbrace = get_object('.template_5_turn_motion.ger_lower_dragbrace.gralin_lower_dragbrace')
        gralin_lower_dragbrace.cylinder_name = target_path('.template_5_turn_motion.ger_lower_dragbrace.gralin_lower_dragbrace')
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1').location
        _template_5_turn_motion_ground_hpr_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_collar_atch_1').location
        gralin_lower_dragbrace.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_ldb_udb_atch_1, _template_5_turn_motion_ground_hpr_ldb_collar_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_lower_dragbrace.gralin_lower_dragbrace', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_upper_torquearm.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_upper_torquearm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_upper_torquearm.inertia_frame')
        _template_5_turn_motion_gel_upper_torquearm_cm = get_object('.template_5_turn_motion.gel_upper_torquearm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_torquearm_cm))
        _template_5_turn_motion_gel_upper_torquearm = get_object('.template_5_turn_motion.gel_upper_torquearm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_torquearm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_torquearm.inertia_frame', exc)

    try:
        gralin_11 = get_object('.template_5_turn_motion.gel_upper_torquearm.gralin_11')
        relative_to = get_object('.template_5_turn_motion.gel_upper_torquearm')
        gralin_11.relative_to = relative_to
        gralin_11.marker_name = target_path('.template_5_turn_motion.gel_upper_torquearm.gralin_11')
        _template_5_turn_motion_ground_hpl_uta_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_collar_atch_1')
        gralin_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_uta_collar_atch_1))
        _template_5_turn_motion_ground_hpl_uta_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_collar_atch_1').location
        _template_5_turn_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_1').location
        gralin_11.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_uta_collar_atch_1, _template_5_turn_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_11.location, gralin_11.orientation)
        gralin_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_torquearm.gralin_11', exc)

    try:
        jxl_joint_i_2 = get_object('.template_5_turn_motion.gel_upper_torquearm.jxl_joint_i_2')
        relative_to = get_object('.template_5_turn_motion.gel_upper_torquearm')
        jxl_joint_i_2.relative_to = relative_to
        jxl_joint_i_2.marker_name = target_path('.template_5_turn_motion.gel_upper_torquearm.jxl_joint_i_2')
        _template_5_turn_motion_gel_connector_jxl_joint_j_2 = get_object('.template_5_turn_motion.gel_connector.jxl_joint_j_2')
        jxl_joint_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_connector_jxl_joint_j_2))
        _template_5_turn_motion_gel_connector_jxl_joint_j_2 = get_object('.template_5_turn_motion.gel_connector.jxl_joint_j_2')
        jxl_joint_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_connector_jxl_joint_j_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_2.location, jxl_joint_i_2.orientation)
        jxl_joint_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_torquearm.jxl_joint_i_2', exc)

    try:
        jxl_joint_i_3 = get_object('.template_5_turn_motion.gel_upper_torquearm.jxl_joint_i_3')
        relative_to = get_object('.template_5_turn_motion.gel_upper_torquearm')
        jxl_joint_i_3.relative_to = relative_to
        jxl_joint_i_3.marker_name = target_path('.template_5_turn_motion.gel_upper_torquearm.jxl_joint_i_3')
        _template_5_turn_motion_gel_uc_collar_jxl_joint_j_3 = get_object('.template_5_turn_motion.gel_uc_collar.jxl_joint_j_3')
        jxl_joint_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_uc_collar_jxl_joint_j_3))
        _template_5_turn_motion_gel_uc_collar_jxl_joint_j_3 = get_object('.template_5_turn_motion.gel_uc_collar.jxl_joint_j_3')
        jxl_joint_i_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_uc_collar_jxl_joint_j_3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_3.location, jxl_joint_i_3.orientation)
        jxl_joint_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upper_torquearm.jxl_joint_i_3', exc)

    try:
        gralin_upper_torquearm = get_object('.template_5_turn_motion.gel_upper_torquearm.gralin_upper_torquearm')
        gralin_upper_torquearm.cylinder_name = target_path('.template_5_turn_motion.gel_upper_torquearm.gralin_upper_torquearm')
        _template_5_turn_motion_ground_hpl_uta_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_collar_atch_1').location
        _template_5_turn_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_1').location
        gralin_upper_torquearm.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_uta_collar_atch_1, _template_5_turn_motion_ground_hpl_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_upper_torquearm.gralin_upper_torquearm', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_upper_torquearm.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_upper_torquearm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_upper_torquearm.inertia_frame')
        _template_5_turn_motion_ger_upper_torquearm_cm = get_object('.template_5_turn_motion.ger_upper_torquearm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_torquearm_cm))
        _template_5_turn_motion_ger_upper_torquearm = get_object('.template_5_turn_motion.ger_upper_torquearm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_torquearm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_torquearm.inertia_frame', exc)

    try:
        gralin_28 = get_object('.template_5_turn_motion.ger_upper_torquearm.gralin_28')
        relative_to = get_object('.template_5_turn_motion.ger_upper_torquearm')
        gralin_28.relative_to = relative_to
        gralin_28.marker_name = target_path('.template_5_turn_motion.ger_upper_torquearm.gralin_28')
        _template_5_turn_motion_ground_hpr_uta_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_collar_atch_1')
        gralin_28.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_uta_collar_atch_1))
        _template_5_turn_motion_ground_hpr_uta_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_collar_atch_1').location
        _template_5_turn_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_1').location
        gralin_28.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_uta_collar_atch_1, _template_5_turn_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_28.location, gralin_28.orientation)
        gralin_28.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_28.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_torquearm.gralin_28', exc)

    try:
        jxr_joint_i_2 = get_object('.template_5_turn_motion.ger_upper_torquearm.jxr_joint_i_2')
        relative_to = get_object('.template_5_turn_motion.ger_upper_torquearm')
        jxr_joint_i_2.relative_to = relative_to
        jxr_joint_i_2.marker_name = target_path('.template_5_turn_motion.ger_upper_torquearm.jxr_joint_i_2')
        _template_5_turn_motion_ger_connector_jxr_joint_j_2 = get_object('.template_5_turn_motion.ger_connector.jxr_joint_j_2')
        jxr_joint_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_connector_jxr_joint_j_2))
        _template_5_turn_motion_ger_connector_jxr_joint_j_2 = get_object('.template_5_turn_motion.ger_connector.jxr_joint_j_2')
        jxr_joint_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_connector_jxr_joint_j_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_2.location, jxr_joint_i_2.orientation)
        jxr_joint_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_torquearm.jxr_joint_i_2', exc)

    try:
        jxr_joint_i_3 = get_object('.template_5_turn_motion.ger_upper_torquearm.jxr_joint_i_3')
        relative_to = get_object('.template_5_turn_motion.ger_upper_torquearm')
        jxr_joint_i_3.relative_to = relative_to
        jxr_joint_i_3.marker_name = target_path('.template_5_turn_motion.ger_upper_torquearm.jxr_joint_i_3')
        _template_5_turn_motion_ger_uc_collar_jxr_joint_j_3 = get_object('.template_5_turn_motion.ger_uc_collar.jxr_joint_j_3')
        jxr_joint_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_uc_collar_jxr_joint_j_3))
        _template_5_turn_motion_ger_uc_collar_jxr_joint_j_3 = get_object('.template_5_turn_motion.ger_uc_collar.jxr_joint_j_3')
        jxr_joint_i_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_uc_collar_jxr_joint_j_3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_3.location, jxr_joint_i_3.orientation)
        jxr_joint_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upper_torquearm.jxr_joint_i_3', exc)

    try:
        gralin_upper_torquearm = get_object('.template_5_turn_motion.ger_upper_torquearm.gralin_upper_torquearm')
        gralin_upper_torquearm.cylinder_name = target_path('.template_5_turn_motion.ger_upper_torquearm.gralin_upper_torquearm')
        _template_5_turn_motion_ground_hpr_uta_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_collar_atch_1').location
        _template_5_turn_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_1').location
        gralin_upper_torquearm.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_uta_collar_atch_1, _template_5_turn_motion_ground_hpr_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_upper_torquearm.gralin_upper_torquearm', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_lower_torquearm.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_lower_torquearm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_lower_torquearm.inertia_frame')
        _template_5_turn_motion_gel_lower_torquearm_cm = get_object('.template_5_turn_motion.gel_lower_torquearm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lower_torquearm_cm))
        _template_5_turn_motion_gel_lower_torquearm = get_object('.template_5_turn_motion.gel_lower_torquearm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lower_torquearm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_torquearm.inertia_frame', exc)

    try:
        gralin_29 = get_object('.template_5_turn_motion.gel_lower_torquearm.gralin_29')
        relative_to = get_object('.template_5_turn_motion.gel_lower_torquearm')
        gralin_29.relative_to = relative_to
        gralin_29.marker_name = target_path('.template_5_turn_motion.gel_lower_torquearm.gralin_29')
        _template_5_turn_motion_ground_hpl_lta_lc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_lc_atch_1')
        gralin_29.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_lta_lc_atch_1))
        _template_5_turn_motion_ground_hpl_lta_lc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_lc_atch_1').location
        _template_5_turn_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_connect_atch_1').location
        gralin_29.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_lta_lc_atch_1, _template_5_turn_motion_ground_hpl_lta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_29.location, gralin_29.orientation)
        gralin_29.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_29.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_torquearm.gralin_29', exc)

    try:
        jxl_joint_i_11 = get_object('.template_5_turn_motion.gel_lower_torquearm.jxl_joint_i_11')
        relative_to = get_object('.template_5_turn_motion.gel_lower_torquearm')
        jxl_joint_i_11.relative_to = relative_to
        jxl_joint_i_11.marker_name = target_path('.template_5_turn_motion.gel_lower_torquearm.jxl_joint_i_11')
        _template_5_turn_motion_gel_lower_cylinder_jxl_joint_j_11 = get_object('.template_5_turn_motion.gel_lower_cylinder.jxl_joint_j_11')
        jxl_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lower_cylinder_jxl_joint_j_11))
        _template_5_turn_motion_gel_lower_cylinder_jxl_joint_j_11 = get_object('.template_5_turn_motion.gel_lower_cylinder.jxl_joint_j_11')
        jxl_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lower_cylinder_jxl_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_11.location, jxl_joint_i_11.orientation)
        jxl_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_torquearm.jxl_joint_i_11', exc)

    try:
        jxl_joint_i_1 = get_object('.template_5_turn_motion.gel_lower_torquearm.jxl_joint_i_1')
        relative_to = get_object('.template_5_turn_motion.gel_lower_torquearm')
        jxl_joint_i_1.relative_to = relative_to
        jxl_joint_i_1.marker_name = target_path('.template_5_turn_motion.gel_lower_torquearm.jxl_joint_i_1')
        _template_5_turn_motion_gel_connector_jxl_joint_j_1 = get_object('.template_5_turn_motion.gel_connector.jxl_joint_j_1')
        jxl_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_connector_jxl_joint_j_1))
        _template_5_turn_motion_gel_connector_jxl_joint_j_1 = get_object('.template_5_turn_motion.gel_connector.jxl_joint_j_1')
        jxl_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_connector_jxl_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_1.location, jxl_joint_i_1.orientation)
        jxl_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lower_torquearm.jxl_joint_i_1', exc)

    try:
        gralin_lower_torquearm = get_object('.template_5_turn_motion.gel_lower_torquearm.gralin_lower_torquearm')
        gralin_lower_torquearm.cylinder_name = target_path('.template_5_turn_motion.gel_lower_torquearm.gralin_lower_torquearm')
        _template_5_turn_motion_ground_hpl_lta_lc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_lc_atch_1').location
        _template_5_turn_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_connect_atch_1').location
        gralin_lower_torquearm.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_lta_lc_atch_1, _template_5_turn_motion_ground_hpl_lta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_lower_torquearm.gralin_lower_torquearm', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_lower_torquearm.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_lower_torquearm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_lower_torquearm.inertia_frame')
        _template_5_turn_motion_ger_lower_torquearm_cm = get_object('.template_5_turn_motion.ger_lower_torquearm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lower_torquearm_cm))
        _template_5_turn_motion_ger_lower_torquearm = get_object('.template_5_turn_motion.ger_lower_torquearm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lower_torquearm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_torquearm.inertia_frame', exc)

    try:
        gralin_30 = get_object('.template_5_turn_motion.ger_lower_torquearm.gralin_30')
        relative_to = get_object('.template_5_turn_motion.ger_lower_torquearm')
        gralin_30.relative_to = relative_to
        gralin_30.marker_name = target_path('.template_5_turn_motion.ger_lower_torquearm.gralin_30')
        _template_5_turn_motion_ground_hpr_lta_lc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_lc_atch_1')
        gralin_30.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_lta_lc_atch_1))
        _template_5_turn_motion_ground_hpr_lta_lc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_lc_atch_1').location
        _template_5_turn_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_connect_atch_1').location
        gralin_30.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_lta_lc_atch_1, _template_5_turn_motion_ground_hpr_lta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_30.location, gralin_30.orientation)
        gralin_30.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_30.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_torquearm.gralin_30', exc)

    try:
        jxr_joint_i_11 = get_object('.template_5_turn_motion.ger_lower_torquearm.jxr_joint_i_11')
        relative_to = get_object('.template_5_turn_motion.ger_lower_torquearm')
        jxr_joint_i_11.relative_to = relative_to
        jxr_joint_i_11.marker_name = target_path('.template_5_turn_motion.ger_lower_torquearm.jxr_joint_i_11')
        _template_5_turn_motion_ger_lower_cylinder_jxr_joint_j_11 = get_object('.template_5_turn_motion.ger_lower_cylinder.jxr_joint_j_11')
        jxr_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lower_cylinder_jxr_joint_j_11))
        _template_5_turn_motion_ger_lower_cylinder_jxr_joint_j_11 = get_object('.template_5_turn_motion.ger_lower_cylinder.jxr_joint_j_11')
        jxr_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lower_cylinder_jxr_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_11.location, jxr_joint_i_11.orientation)
        jxr_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_torquearm.jxr_joint_i_11', exc)

    try:
        jxr_joint_i_1 = get_object('.template_5_turn_motion.ger_lower_torquearm.jxr_joint_i_1')
        relative_to = get_object('.template_5_turn_motion.ger_lower_torquearm')
        jxr_joint_i_1.relative_to = relative_to
        jxr_joint_i_1.marker_name = target_path('.template_5_turn_motion.ger_lower_torquearm.jxr_joint_i_1')
        _template_5_turn_motion_ger_connector_jxr_joint_j_1 = get_object('.template_5_turn_motion.ger_connector.jxr_joint_j_1')
        jxr_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_connector_jxr_joint_j_1))
        _template_5_turn_motion_ger_connector_jxr_joint_j_1 = get_object('.template_5_turn_motion.ger_connector.jxr_joint_j_1')
        jxr_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_connector_jxr_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_1.location, jxr_joint_i_1.orientation)
        jxr_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lower_torquearm.jxr_joint_i_1', exc)

    try:
        gralin_lower_torquearm = get_object('.template_5_turn_motion.ger_lower_torquearm.gralin_lower_torquearm')
        gralin_lower_torquearm.cylinder_name = target_path('.template_5_turn_motion.ger_lower_torquearm.gralin_lower_torquearm')
        _template_5_turn_motion_ground_hpr_lta_lc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_lc_atch_1').location
        _template_5_turn_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_connect_atch_1').location
        gralin_lower_torquearm.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_lta_lc_atch_1, _template_5_turn_motion_ground_hpr_lta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_lower_torquearm.gralin_lower_torquearm', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_connector.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_connector')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_connector.inertia_frame')
        _template_5_turn_motion_gel_connector_cm = get_object('.template_5_turn_motion.gel_connector.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_connector_cm))
        _template_5_turn_motion_gel_connector = get_object('.template_5_turn_motion.gel_connector')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_connector))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_connector.inertia_frame', exc)

    try:
        gralin_3 = get_object('.template_5_turn_motion.gel_connector.gralin_3')
        relative_to = get_object('.template_5_turn_motion.gel_connector')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_5_turn_motion.gel_connector.gralin_3')
        _template_5_turn_motion_ground_hpl_connect_1 = get_object('.template_5_turn_motion.ground.hpl_connect_1')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_connect_1))
        _template_5_turn_motion_ground_hpl_connect_1 = get_object('.template_5_turn_motion.ground.hpl_connect_1').location
        _template_5_turn_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_1').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_connect_1, _template_5_turn_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_connector.gralin_3', exc)

    try:
        jxl_joint_j_1 = get_object('.template_5_turn_motion.gel_connector.jxl_joint_j_1')
        relative_to = get_object('.template_5_turn_motion.gel_connector')
        jxl_joint_j_1.relative_to = relative_to
        jxl_joint_j_1.marker_name = target_path('.template_5_turn_motion.gel_connector.jxl_joint_j_1')
        _template_5_turn_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_connect_atch_1')
        jxl_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_lta_connect_atch_1))
        _template_5_turn_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_connect_atch_1').location
        _template_5_turn_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_1').location
        jxl_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_lta_connect_atch_1, _template_5_turn_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_1.location, jxl_joint_j_1.orientation)
        jxl_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_connector.jxl_joint_j_1', exc)

    try:
        jxl_joint_j_2 = get_object('.template_5_turn_motion.gel_connector.jxl_joint_j_2')
        relative_to = get_object('.template_5_turn_motion.gel_connector')
        jxl_joint_j_2.relative_to = relative_to
        jxl_joint_j_2.marker_name = target_path('.template_5_turn_motion.gel_connector.jxl_joint_j_2')
        _template_5_turn_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_1')
        jxl_joint_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_uta_connect_atch_1))
        _template_5_turn_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_1').location
        _template_5_turn_motion_ground_hpl_uta_connect_atch_2 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_2').location
        jxl_joint_j_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_uta_connect_atch_1, _template_5_turn_motion_ground_hpl_uta_connect_atch_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_2.location, jxl_joint_j_2.orientation)
        jxl_joint_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_connector.jxl_joint_j_2', exc)

    try:
        gralin_connector = get_object('.template_5_turn_motion.gel_connector.gralin_connector')
        gralin_connector.cylinder_name = target_path('.template_5_turn_motion.gel_connector.gralin_connector')
        _template_5_turn_motion_ground_hpl_connect_1 = get_object('.template_5_turn_motion.ground.hpl_connect_1').location
        _template_5_turn_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_1').location
        gralin_connector.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_connect_1, _template_5_turn_motion_ground_hpl_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_connector.gralin_connector', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_connector.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_connector')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_connector.inertia_frame')
        _template_5_turn_motion_ger_connector_cm = get_object('.template_5_turn_motion.ger_connector.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_connector_cm))
        _template_5_turn_motion_ger_connector = get_object('.template_5_turn_motion.ger_connector')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_connector))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_connector.inertia_frame', exc)

    try:
        gralin_4 = get_object('.template_5_turn_motion.ger_connector.gralin_4')
        relative_to = get_object('.template_5_turn_motion.ger_connector')
        gralin_4.relative_to = relative_to
        gralin_4.marker_name = target_path('.template_5_turn_motion.ger_connector.gralin_4')
        _template_5_turn_motion_ground_hpr_connect_1 = get_object('.template_5_turn_motion.ground.hpr_connect_1')
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_connect_1))
        _template_5_turn_motion_ground_hpr_connect_1 = get_object('.template_5_turn_motion.ground.hpr_connect_1').location
        _template_5_turn_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_1').location
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_connect_1, _template_5_turn_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_connector.gralin_4', exc)

    try:
        jxr_joint_j_1 = get_object('.template_5_turn_motion.ger_connector.jxr_joint_j_1')
        relative_to = get_object('.template_5_turn_motion.ger_connector')
        jxr_joint_j_1.relative_to = relative_to
        jxr_joint_j_1.marker_name = target_path('.template_5_turn_motion.ger_connector.jxr_joint_j_1')
        _template_5_turn_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_connect_atch_1')
        jxr_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_lta_connect_atch_1))
        _template_5_turn_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_connect_atch_1').location
        _template_5_turn_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_1').location
        jxr_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_lta_connect_atch_1, _template_5_turn_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_1.location, jxr_joint_j_1.orientation)
        jxr_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_connector.jxr_joint_j_1', exc)

    try:
        jxr_joint_j_2 = get_object('.template_5_turn_motion.ger_connector.jxr_joint_j_2')
        relative_to = get_object('.template_5_turn_motion.ger_connector')
        jxr_joint_j_2.relative_to = relative_to
        jxr_joint_j_2.marker_name = target_path('.template_5_turn_motion.ger_connector.jxr_joint_j_2')
        _template_5_turn_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_1')
        jxr_joint_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_uta_connect_atch_1))
        _template_5_turn_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_1').location
        _template_5_turn_motion_ground_hpr_uta_connect_atch_2 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_2').location
        jxr_joint_j_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_uta_connect_atch_1, _template_5_turn_motion_ground_hpr_uta_connect_atch_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_2.location, jxr_joint_j_2.orientation)
        jxr_joint_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_connector.jxr_joint_j_2', exc)

    try:
        gralin_connector = get_object('.template_5_turn_motion.ger_connector.gralin_connector')
        gralin_connector.cylinder_name = target_path('.template_5_turn_motion.ger_connector.gralin_connector')
        _template_5_turn_motion_ground_hpr_connect_1 = get_object('.template_5_turn_motion.ground.hpr_connect_1').location
        _template_5_turn_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_1').location
        gralin_connector.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_connect_1, _template_5_turn_motion_ground_hpr_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_connector.gralin_connector', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_uc_collar.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_uc_collar')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_uc_collar.inertia_frame')
        _template_5_turn_motion_gel_uc_collar_cm = get_object('.template_5_turn_motion.gel_uc_collar.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_uc_collar_cm))
        _template_5_turn_motion_gel_uc_collar = get_object('.template_5_turn_motion.gel_uc_collar')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_uc_collar))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_uc_collar.inertia_frame', exc)

    try:
        gralin_5 = get_object('.template_5_turn_motion.gel_uc_collar.gralin_5')
        relative_to = get_object('.template_5_turn_motion.gel_uc_collar')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_5_turn_motion.gel_uc_collar.gralin_5')
        _template_5_turn_motion_ground_cfl_collar_top = get_object('.template_5_turn_motion.ground.cfl_collar_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_collar_top))
        _template_5_turn_motion_ground_cfl_collar_top = get_object('.template_5_turn_motion.ground.cfl_collar_top').location
        _template_5_turn_motion_ground_cfl_collar_bot = get_object('.template_5_turn_motion.ground.cfl_collar_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_cfl_collar_top, _template_5_turn_motion_ground_cfl_collar_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_uc_collar.gralin_5', exc)

    try:
        jxl_joint_j_3 = get_object('.template_5_turn_motion.gel_uc_collar.jxl_joint_j_3')
        relative_to = get_object('.template_5_turn_motion.gel_uc_collar')
        jxl_joint_j_3.relative_to = relative_to
        jxl_joint_j_3.marker_name = target_path('.template_5_turn_motion.gel_uc_collar.jxl_joint_j_3')
        _template_5_turn_motion_ground_hpl_uta_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_collar_atch_1')
        jxl_joint_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_uta_collar_atch_1))
        _template_5_turn_motion_ground_hpl_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lta_connect_atch_1').location
        _template_5_turn_motion_ground_hpl_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpl_uta_connect_atch_1').location
        jxl_joint_j_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_lta_connect_atch_1, _template_5_turn_motion_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_3.location, jxl_joint_j_3.orientation)
        jxl_joint_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_uc_collar.jxl_joint_j_3', exc)

    try:
        jxl_joint_i_4 = get_object('.template_5_turn_motion.gel_uc_collar.jxl_joint_i_4')
        relative_to = get_object('.template_5_turn_motion.gel_uc_collar')
        jxl_joint_i_4.relative_to = relative_to
        jxl_joint_i_4.marker_name = target_path('.template_5_turn_motion.gel_uc_collar.jxl_joint_i_4')
        _template_5_turn_motion_gel_upper_cylinder_jxl_joint_j_4 = get_object('.template_5_turn_motion.gel_upper_cylinder.jxl_joint_j_4')
        jxl_joint_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_cylinder_jxl_joint_j_4))
        _template_5_turn_motion_gel_upper_cylinder_jxl_joint_j_4 = get_object('.template_5_turn_motion.gel_upper_cylinder.jxl_joint_j_4')
        jxl_joint_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upper_cylinder_jxl_joint_j_4))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_4.location, jxl_joint_i_4.orientation)
        jxl_joint_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_uc_collar.jxl_joint_i_4', exc)

    try:
        jxl_joint_j_10 = get_object('.template_5_turn_motion.gel_uc_collar.jxl_joint_j_10')
        relative_to = get_object('.template_5_turn_motion.gel_uc_collar')
        jxl_joint_j_10.relative_to = relative_to
        jxl_joint_j_10.marker_name = target_path('.template_5_turn_motion.gel_uc_collar.jxl_joint_j_10')
        _template_5_turn_motion_ground_hpl_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_collar_atch_1')
        jxl_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_ldb_collar_atch_1))
        _template_5_turn_motion_ground_cfl_plane_ref_2 = get_object('.template_5_turn_motion.ground.cfl_plane_ref_2')
        jxl_joint_j_10.orientation = _template_5_turn_motion_ground_cfl_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_10.location, jxl_joint_j_10.orientation)
        jxl_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_uc_collar.jxl_joint_j_10', exc)

    try:
        gralin_uc_collar = get_object('.template_5_turn_motion.gel_uc_collar.gralin_uc_collar')
        gralin_uc_collar.cylinder_name = target_path('.template_5_turn_motion.gel_uc_collar.gralin_uc_collar')
        _template_5_turn_motion_ground_cfl_collar_top = get_object('.template_5_turn_motion.ground.cfl_collar_top').location
        _template_5_turn_motion_ground_cfl_collar_bot = get_object('.template_5_turn_motion.ground.cfl_collar_bot').location
        gralin_uc_collar.length = (VecUtils.DM(_template_5_turn_motion_ground_cfl_collar_top, _template_5_turn_motion_ground_cfl_collar_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_uc_collar.gralin_uc_collar', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_uc_collar.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_uc_collar')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_uc_collar.inertia_frame')
        _template_5_turn_motion_ger_uc_collar_cm = get_object('.template_5_turn_motion.ger_uc_collar.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_uc_collar_cm))
        _template_5_turn_motion_ger_uc_collar = get_object('.template_5_turn_motion.ger_uc_collar')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_uc_collar))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_uc_collar.inertia_frame', exc)

    try:
        gralin_6 = get_object('.template_5_turn_motion.ger_uc_collar.gralin_6')
        relative_to = get_object('.template_5_turn_motion.ger_uc_collar')
        gralin_6.relative_to = relative_to
        gralin_6.marker_name = target_path('.template_5_turn_motion.ger_uc_collar.gralin_6')
        _template_5_turn_motion_ground_cfr_collar_top = get_object('.template_5_turn_motion.ground.cfr_collar_top')
        gralin_6.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_collar_top))
        _template_5_turn_motion_ground_cfr_collar_top = get_object('.template_5_turn_motion.ground.cfr_collar_top').location
        _template_5_turn_motion_ground_cfr_collar_bot = get_object('.template_5_turn_motion.ground.cfr_collar_bot').location
        gralin_6.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_cfr_collar_top, _template_5_turn_motion_ground_cfr_collar_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_6.location, gralin_6.orientation)
        gralin_6.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_6.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_uc_collar.gralin_6', exc)

    try:
        jxr_joint_j_3 = get_object('.template_5_turn_motion.ger_uc_collar.jxr_joint_j_3')
        relative_to = get_object('.template_5_turn_motion.ger_uc_collar')
        jxr_joint_j_3.relative_to = relative_to
        jxr_joint_j_3.marker_name = target_path('.template_5_turn_motion.ger_uc_collar.jxr_joint_j_3')
        _template_5_turn_motion_ground_hpr_uta_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_collar_atch_1')
        jxr_joint_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_uta_collar_atch_1))
        _template_5_turn_motion_ground_hpr_lta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lta_connect_atch_1').location
        _template_5_turn_motion_ground_hpr_uta_connect_atch_1 = get_object('.template_5_turn_motion.ground.hpr_uta_connect_atch_1').location
        jxr_joint_j_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_lta_connect_atch_1, _template_5_turn_motion_ground_hpr_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_3.location, jxr_joint_j_3.orientation)
        jxr_joint_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_uc_collar.jxr_joint_j_3', exc)

    try:
        jxr_joint_i_4 = get_object('.template_5_turn_motion.ger_uc_collar.jxr_joint_i_4')
        relative_to = get_object('.template_5_turn_motion.ger_uc_collar')
        jxr_joint_i_4.relative_to = relative_to
        jxr_joint_i_4.marker_name = target_path('.template_5_turn_motion.ger_uc_collar.jxr_joint_i_4')
        _template_5_turn_motion_ger_upper_cylinder_jxr_joint_j_4 = get_object('.template_5_turn_motion.ger_upper_cylinder.jxr_joint_j_4')
        jxr_joint_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_cylinder_jxr_joint_j_4))
        _template_5_turn_motion_ger_upper_cylinder_jxr_joint_j_4 = get_object('.template_5_turn_motion.ger_upper_cylinder.jxr_joint_j_4')
        jxr_joint_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upper_cylinder_jxr_joint_j_4))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_4.location, jxr_joint_i_4.orientation)
        jxr_joint_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_uc_collar.jxr_joint_i_4', exc)

    try:
        jxr_joint_j_10 = get_object('.template_5_turn_motion.ger_uc_collar.jxr_joint_j_10')
        relative_to = get_object('.template_5_turn_motion.ger_uc_collar')
        jxr_joint_j_10.relative_to = relative_to
        jxr_joint_j_10.marker_name = target_path('.template_5_turn_motion.ger_uc_collar.jxr_joint_j_10')
        _template_5_turn_motion_ground_hpr_ldb_collar_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_collar_atch_1')
        jxr_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_ldb_collar_atch_1))
        _template_5_turn_motion_ground_cfr_plane_ref_2 = get_object('.template_5_turn_motion.ground.cfr_plane_ref_2')
        jxr_joint_j_10.orientation = _template_5_turn_motion_ground_cfr_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_10.location, jxr_joint_j_10.orientation)
        jxr_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_uc_collar.jxr_joint_j_10', exc)

    try:
        gralin_uc_collar = get_object('.template_5_turn_motion.ger_uc_collar.gralin_uc_collar')
        gralin_uc_collar.cylinder_name = target_path('.template_5_turn_motion.ger_uc_collar.gralin_uc_collar')
        _template_5_turn_motion_ground_cfr_collar_top = get_object('.template_5_turn_motion.ground.cfr_collar_top').location
        _template_5_turn_motion_ground_cfr_collar_bot = get_object('.template_5_turn_motion.ground.cfr_collar_bot').location
        gralin_uc_collar.length = (VecUtils.DM(_template_5_turn_motion_ground_cfr_collar_top, _template_5_turn_motion_ground_cfr_collar_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_uc_collar.gralin_uc_collar', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_spindle.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_spindle')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_spindle.inertia_frame')
        _template_5_turn_motion_gel_spindle_cm = get_object('.template_5_turn_motion.gel_spindle.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_spindle_cm))
        _template_5_turn_motion_gel_spindle = get_object('.template_5_turn_motion.gel_spindle')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_spindle))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_spindle.inertia_frame', exc)

    try:
        gralin_7 = get_object('.template_5_turn_motion.gel_spindle.gralin_7')
        relative_to = get_object('.template_5_turn_motion.gel_spindle')
        gralin_7.relative_to = relative_to
        gralin_7.marker_name = target_path('.template_5_turn_motion.gel_spindle.gralin_7')
        _template_5_turn_motion_ground_hpl_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpl_spndl_sf_atch')
        gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_spndl_sf_atch))
        _template_5_turn_motion_ground_hpl_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpl_spndl_sf_atch').location
        _template_5_turn_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpl_udb_spndl_atch_1').location
        gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_spndl_sf_atch, _template_5_turn_motion_ground_hpl_udb_spndl_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_spindle.gralin_7', exc)

    try:
        jxl_joint_j_5 = get_object('.template_5_turn_motion.gel_spindle.jxl_joint_j_5')
        relative_to = get_object('.template_5_turn_motion.gel_spindle')
        jxl_joint_j_5.relative_to = relative_to
        jxl_joint_j_5.marker_name = target_path('.template_5_turn_motion.gel_spindle.jxl_joint_j_5')
        _template_5_turn_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpl_udb_spndl_atch_1')
        jxl_joint_j_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_udb_spndl_atch_1))
        _template_5_turn_motion_ground_hpl_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpl_spndl_sf_atch').location
        _template_5_turn_motion_gel_spindle_jxl_joint_j_5 = get_object('.template_5_turn_motion.gel_spindle.jxl_joint_j_5').location
        _template_5_turn_motion_ground_hpl_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpl_ldb_udb_atch_1').location
        jxl_joint_j_5.orientation = (VecUtils.ORI_IN_PLANE(_template_5_turn_motion_ground_hpl_spndl_sf_atch, _template_5_turn_motion_gel_spindle_jxl_joint_j_5, _template_5_turn_motion_ground_hpl_ldb_udb_atch_1, "Z_ZX"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_5.location, jxl_joint_j_5.orientation)
        jxl_joint_j_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_spindle.jxl_joint_j_5', exc)

    try:
        gralin_spindle = get_object('.template_5_turn_motion.gel_spindle.gralin_spindle')
        gralin_spindle.cylinder_name = target_path('.template_5_turn_motion.gel_spindle.gralin_spindle')
        _template_5_turn_motion_ground_hpl_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpl_spndl_sf_atch').location
        _template_5_turn_motion_ground_hpl_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpl_udb_spndl_atch_1').location
        gralin_spindle.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_spndl_sf_atch, _template_5_turn_motion_ground_hpl_udb_spndl_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_spindle.gralin_spindle', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_spindle.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_spindle')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_spindle.inertia_frame')
        _template_5_turn_motion_ger_spindle_cm = get_object('.template_5_turn_motion.ger_spindle.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_spindle_cm))
        _template_5_turn_motion_ger_spindle = get_object('.template_5_turn_motion.ger_spindle')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_spindle))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_spindle.inertia_frame', exc)

    try:
        gralin_8 = get_object('.template_5_turn_motion.ger_spindle.gralin_8')
        relative_to = get_object('.template_5_turn_motion.ger_spindle')
        gralin_8.relative_to = relative_to
        gralin_8.marker_name = target_path('.template_5_turn_motion.ger_spindle.gralin_8')
        _template_5_turn_motion_ground_hpr_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpr_spndl_sf_atch')
        gralin_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_spndl_sf_atch))
        _template_5_turn_motion_ground_hpr_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpr_spndl_sf_atch').location
        _template_5_turn_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpr_udb_spndl_atch_1').location
        gralin_8.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_spndl_sf_atch, _template_5_turn_motion_ground_hpr_udb_spndl_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_8.location, gralin_8.orientation)
        gralin_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_spindle.gralin_8', exc)

    try:
        jxr_joint_j_5 = get_object('.template_5_turn_motion.ger_spindle.jxr_joint_j_5')
        relative_to = get_object('.template_5_turn_motion.ger_spindle')
        jxr_joint_j_5.relative_to = relative_to
        jxr_joint_j_5.marker_name = target_path('.template_5_turn_motion.ger_spindle.jxr_joint_j_5')
        _template_5_turn_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpr_udb_spndl_atch_1')
        jxr_joint_j_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_udb_spndl_atch_1))
        _template_5_turn_motion_ground_hpr_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpr_spndl_sf_atch').location
        _template_5_turn_motion_ger_spindle_jxr_joint_j_5 = get_object('.template_5_turn_motion.ger_spindle.jxr_joint_j_5').location
        _template_5_turn_motion_ground_hpr_ldb_udb_atch_1 = get_object('.template_5_turn_motion.ground.hpr_ldb_udb_atch_1').location
        jxr_joint_j_5.orientation = (VecUtils.ORI_IN_PLANE(_template_5_turn_motion_ground_hpr_spndl_sf_atch, _template_5_turn_motion_ger_spindle_jxr_joint_j_5, _template_5_turn_motion_ground_hpr_ldb_udb_atch_1, "Z_ZX"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_5.location, jxr_joint_j_5.orientation)
        jxr_joint_j_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_spindle.jxr_joint_j_5', exc)

    try:
        gralin_spindle = get_object('.template_5_turn_motion.ger_spindle.gralin_spindle')
        gralin_spindle.cylinder_name = target_path('.template_5_turn_motion.ger_spindle.gralin_spindle')
        _template_5_turn_motion_ground_hpr_spndl_sf_atch = get_object('.template_5_turn_motion.ground.hpr_spndl_sf_atch').location
        _template_5_turn_motion_ground_hpr_udb_spndl_atch_1 = get_object('.template_5_turn_motion.ground.hpr_udb_spndl_atch_1').location
        gralin_spindle.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_spndl_sf_atch, _template_5_turn_motion_ground_hpr_udb_spndl_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_spindle.gralin_spindle', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_lwract.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_lwract')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_lwract.inertia_frame')
        _template_5_turn_motion_gel_lwract_cm = get_object('.template_5_turn_motion.gel_lwract.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lwract_cm))
        _template_5_turn_motion_gel_lwract = get_object('.template_5_turn_motion.gel_lwract')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lwract))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lwract.inertia_frame', exc)

    try:
        gralin_9 = get_object('.template_5_turn_motion.gel_lwract.gralin_9')
        relative_to = get_object('.template_5_turn_motion.gel_lwract')
        gralin_9.relative_to = relative_to
        gralin_9.marker_name = target_path('.template_5_turn_motion.gel_lwract.gralin_9')
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1')
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_lwract_uc_atch_1))
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_cfl_lwract_top = get_object('.template_5_turn_motion.ground.cfl_lwract_top').location
        gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_lwract_uc_atch_1, _template_5_turn_motion_ground_cfl_lwract_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lwract.gralin_9', exc)

    try:
        jxl_joint_j_7 = get_object('.template_5_turn_motion.gel_lwract.jxl_joint_j_7')
        relative_to = get_object('.template_5_turn_motion.gel_lwract')
        jxl_joint_j_7.relative_to = relative_to
        jxl_joint_j_7.marker_name = target_path('.template_5_turn_motion.gel_lwract.jxl_joint_j_7')
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1')
        jxl_joint_j_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_lwract_uc_atch_1))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        jxl_joint_j_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_7.location, jxl_joint_j_7.orientation)
        jxl_joint_j_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lwract.jxl_joint_j_7', exc)

    try:
        jxl_joint_i_8 = get_object('.template_5_turn_motion.gel_lwract.jxl_joint_i_8')
        relative_to = get_object('.template_5_turn_motion.gel_lwract')
        jxl_joint_i_8.relative_to = relative_to
        jxl_joint_i_8.marker_name = target_path('.template_5_turn_motion.gel_lwract.jxl_joint_i_8')
        _template_5_turn_motion_gel_upract_jxl_joint_j_8 = get_object('.template_5_turn_motion.gel_upract.jxl_joint_j_8')
        jxl_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upract_jxl_joint_j_8))
        _template_5_turn_motion_gel_upract_jxl_joint_j_8 = get_object('.template_5_turn_motion.gel_upract.jxl_joint_j_8')
        jxl_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upract_jxl_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_8.location, jxl_joint_i_8.orientation)
        jxl_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lwract.jxl_joint_i_8', exc)

    try:
        uel_stopper_i_2 = get_object('.template_5_turn_motion.gel_lwract.uel_stopper_i_2')
        relative_to = get_object('.template_5_turn_motion.gel_lwract')
        uel_stopper_i_2.relative_to = relative_to
        uel_stopper_i_2.marker_name = target_path('.template_5_turn_motion.gel_lwract.uel_stopper_i_2')
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1')
        uel_stopper_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_lwract_uc_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_i_2.location, uel_stopper_i_2.orientation)
        uel_stopper_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lwract.uel_stopper_i_2', exc)

    try:
        uel_actuator_j_1 = get_object('.template_5_turn_motion.gel_lwract.uel_actuator_j_1')
        relative_to = get_object('.template_5_turn_motion.gel_lwract')
        uel_actuator_j_1.relative_to = relative_to
        uel_actuator_j_1.marker_name = target_path('.template_5_turn_motion.gel_lwract.uel_actuator_j_1')
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1')
        uel_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_lwract_uc_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_j_1.location, uel_actuator_j_1.orientation)
        uel_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lwract.uel_actuator_j_1', exc)

    try:
        uel_actuator_i_2 = get_object('.template_5_turn_motion.gel_lwract.uel_actuator_i_2')
        relative_to = get_object('.template_5_turn_motion.gel_lwract')
        uel_actuator_i_2.relative_to = relative_to
        uel_actuator_i_2.marker_name = target_path('.template_5_turn_motion.gel_lwract.uel_actuator_i_2')
        _template_5_turn_motion_gel_lwract_jxl_joint_i_8 = get_object('.template_5_turn_motion.gel_lwract.jxl_joint_i_8')
        uel_actuator_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lwract_jxl_joint_i_8))
        _template_5_turn_motion_gel_lwract_jxl_joint_i_8 = get_object('.template_5_turn_motion.gel_lwract.jxl_joint_i_8')
        uel_actuator_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_lwract_jxl_joint_i_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_i_2.location, uel_actuator_i_2.orientation)
        uel_actuator_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_actuator_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_lwract.uel_actuator_i_2', exc)

    try:
        gralin_lwract = get_object('.template_5_turn_motion.gel_lwract.gralin_lwract')
        gralin_lwract.cylinder_name = target_path('.template_5_turn_motion.gel_lwract.gralin_lwract')
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_cfl_lwract_top = get_object('.template_5_turn_motion.ground.cfl_lwract_top').location
        gralin_lwract.length = (VecUtils.DM(_template_5_turn_motion_ground_hpl_lwract_uc_atch_1, _template_5_turn_motion_ground_cfl_lwract_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_lwract.gralin_lwract', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_lwract.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_lwract')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_lwract.inertia_frame')
        _template_5_turn_motion_ger_lwract_cm = get_object('.template_5_turn_motion.ger_lwract.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lwract_cm))
        _template_5_turn_motion_ger_lwract = get_object('.template_5_turn_motion.ger_lwract')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lwract))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lwract.inertia_frame', exc)

    try:
        gralin_10 = get_object('.template_5_turn_motion.ger_lwract.gralin_10')
        relative_to = get_object('.template_5_turn_motion.ger_lwract')
        gralin_10.relative_to = relative_to
        gralin_10.marker_name = target_path('.template_5_turn_motion.ger_lwract.gralin_10')
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1')
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_lwract_uc_atch_1))
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_cfr_lwract_top = get_object('.template_5_turn_motion.ground.cfr_lwract_top').location
        gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_lwract_uc_atch_1, _template_5_turn_motion_ground_cfr_lwract_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lwract.gralin_10', exc)

    try:
        jxr_joint_j_7 = get_object('.template_5_turn_motion.ger_lwract.jxr_joint_j_7')
        relative_to = get_object('.template_5_turn_motion.ger_lwract')
        jxr_joint_j_7.relative_to = relative_to
        jxr_joint_j_7.marker_name = target_path('.template_5_turn_motion.ger_lwract.jxr_joint_j_7')
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1')
        jxr_joint_j_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_lwract_uc_atch_1))
        _template_5_turn_motion_ground_origo = get_object('.template_5_turn_motion.ground.origo')
        jxr_joint_j_7.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_7.location, jxr_joint_j_7.orientation)
        jxr_joint_j_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lwract.jxr_joint_j_7', exc)

    try:
        jxr_joint_i_8 = get_object('.template_5_turn_motion.ger_lwract.jxr_joint_i_8')
        relative_to = get_object('.template_5_turn_motion.ger_lwract')
        jxr_joint_i_8.relative_to = relative_to
        jxr_joint_i_8.marker_name = target_path('.template_5_turn_motion.ger_lwract.jxr_joint_i_8')
        _template_5_turn_motion_ger_upract_jxr_joint_j_8 = get_object('.template_5_turn_motion.ger_upract.jxr_joint_j_8')
        jxr_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upract_jxr_joint_j_8))
        _template_5_turn_motion_ger_upract_jxr_joint_j_8 = get_object('.template_5_turn_motion.ger_upract.jxr_joint_j_8')
        jxr_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upract_jxr_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_i_8.location, jxr_joint_i_8.orientation)
        jxr_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lwract.jxr_joint_i_8', exc)

    try:
        uer_stopper_i_2 = get_object('.template_5_turn_motion.ger_lwract.uer_stopper_i_2')
        relative_to = get_object('.template_5_turn_motion.ger_lwract')
        uer_stopper_i_2.relative_to = relative_to
        uer_stopper_i_2.marker_name = target_path('.template_5_turn_motion.ger_lwract.uer_stopper_i_2')
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1')
        uer_stopper_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_lwract_uc_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_stopper_i_2.location, uer_stopper_i_2.orientation)
        uer_stopper_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lwract.uer_stopper_i_2', exc)

    try:
        uer_actuator_i_2 = get_object('.template_5_turn_motion.ger_lwract.uer_actuator_i_2')
        relative_to = get_object('.template_5_turn_motion.ger_lwract')
        uer_actuator_i_2.relative_to = relative_to
        uer_actuator_i_2.marker_name = target_path('.template_5_turn_motion.ger_lwract.uer_actuator_i_2')
        _template_5_turn_motion_ger_lwract_jxr_joint_i_8 = get_object('.template_5_turn_motion.ger_lwract.jxr_joint_i_8')
        uer_actuator_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lwract_jxr_joint_i_8))
        _template_5_turn_motion_ger_lwract_jxr_joint_i_8 = get_object('.template_5_turn_motion.ger_lwract.jxr_joint_i_8')
        uer_actuator_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_lwract_jxr_joint_i_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_i_2.location, uer_actuator_i_2.orientation)
        uer_actuator_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uer_actuator_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lwract.uer_actuator_i_2', exc)

    try:
        uer_actuator_j_1 = get_object('.template_5_turn_motion.ger_lwract.uer_actuator_j_1')
        relative_to = get_object('.template_5_turn_motion.ger_lwract')
        uer_actuator_j_1.relative_to = relative_to
        uer_actuator_j_1.marker_name = target_path('.template_5_turn_motion.ger_lwract.uer_actuator_j_1')
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1')
        uer_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_lwract_uc_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_j_1.location, uer_actuator_j_1.orientation)
        uer_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_lwract.uer_actuator_j_1', exc)

    try:
        gralin_lwract = get_object('.template_5_turn_motion.ger_lwract.gralin_lwract')
        gralin_lwract.cylinder_name = target_path('.template_5_turn_motion.ger_lwract.gralin_lwract')
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_cfr_lwract_top = get_object('.template_5_turn_motion.ground.cfr_lwract_top').location
        gralin_lwract.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_lwract_uc_atch_1, _template_5_turn_motion_ground_cfr_lwract_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_lwract.gralin_lwract', exc)

    try:
        uel_actuator_i_1 = get_object('.template_5_turn_motion.gel_upract.uel_actuator_i_1')
        relative_to = get_object('.template_5_turn_motion.gel_upract')
        uel_actuator_i_1.relative_to = relative_to
        uel_actuator_i_1.marker_name = target_path('.template_5_turn_motion.gel_upract.uel_actuator_i_1')
        _template_5_turn_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpl_upract_sf_atch_1')
        uel_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_upract_sf_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_i_1.location, uel_actuator_i_1.orientation)
        uel_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upract.uel_actuator_i_1', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.gel_upract.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.gel_upract')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.gel_upract.inertia_frame')
        _template_5_turn_motion_gel_upract_cm = get_object('.template_5_turn_motion.gel_upract.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upract_cm))
        _template_5_turn_motion_gel_upract = get_object('.template_5_turn_motion.gel_upract')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upract))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upract.inertia_frame', exc)

    try:
        gralin_18 = get_object('.template_5_turn_motion.gel_upract.gralin_18')
        relative_to = get_object('.template_5_turn_motion.gel_upract')
        gralin_18.relative_to = relative_to
        gralin_18.marker_name = target_path('.template_5_turn_motion.gel_upract.gralin_18')
        _template_5_turn_motion_ground_cfl_upract_bot = get_object('.template_5_turn_motion.ground.cfl_upract_bot')
        gralin_18.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_upract_bot))
        _template_5_turn_motion_ground_cfl_upract_bot = get_object('.template_5_turn_motion.ground.cfl_upract_bot').location
        _template_5_turn_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpl_upract_sf_atch_1').location
        gralin_18.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_cfl_upract_bot, _template_5_turn_motion_ground_hpl_upract_sf_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_18.location, gralin_18.orientation)
        gralin_18.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_18.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upract.gralin_18', exc)

    try:
        jxl_joint_j_8 = get_object('.template_5_turn_motion.gel_upract.jxl_joint_j_8')
        relative_to = get_object('.template_5_turn_motion.gel_upract')
        jxl_joint_j_8.relative_to = relative_to
        jxl_joint_j_8.marker_name = target_path('.template_5_turn_motion.gel_upract.jxl_joint_j_8')
        _template_5_turn_motion_ground_cfl_lwract_top = get_object('.template_5_turn_motion.ground.cfl_lwract_top')
        jxl_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfl_lwract_top))
        _template_5_turn_motion_ground_hpl_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpl_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpl_upract_sf_atch_1').location
        jxl_joint_j_8.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpl_lwract_uc_atch_1, _template_5_turn_motion_ground_hpl_upract_sf_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_8.location, jxl_joint_j_8.orientation)
        jxl_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upract.jxl_joint_j_8', exc)

    try:
        uel_stopper_j_2 = get_object('.template_5_turn_motion.gel_upract.uel_stopper_j_2')
        relative_to = get_object('.template_5_turn_motion.gel_upract')
        uel_stopper_j_2.relative_to = relative_to
        uel_stopper_j_2.marker_name = target_path('.template_5_turn_motion.gel_upract.uel_stopper_j_2')
        _template_5_turn_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpl_upract_sf_atch_1')
        uel_stopper_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_upract_sf_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_j_2.location, uel_stopper_j_2.orientation)
        uel_stopper_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upract.uel_stopper_j_2', exc)

    try:
        uel_actuator_j_2 = get_object('.template_5_turn_motion.gel_upract.uel_actuator_j_2')
        relative_to = get_object('.template_5_turn_motion.gel_upract')
        uel_actuator_j_2.relative_to = relative_to
        uel_actuator_j_2.marker_name = target_path('.template_5_turn_motion.gel_upract.uel_actuator_j_2')
        _template_5_turn_motion_gel_upract_jxl_joint_j_8 = get_object('.template_5_turn_motion.gel_upract.jxl_joint_j_8')
        uel_actuator_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upract_jxl_joint_j_8))
        _template_5_turn_motion_gel_upract_jxl_joint_j_8 = get_object('.template_5_turn_motion.gel_upract.jxl_joint_j_8')
        uel_actuator_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_gel_upract_jxl_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_j_2.location, uel_actuator_j_2.orientation)
        uel_actuator_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uel_actuator_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.gel_upract.uel_actuator_j_2', exc)

    try:
        gralin_upract = get_object('.template_5_turn_motion.gel_upract.gralin_upract')
        gralin_upract.cylinder_name = target_path('.template_5_turn_motion.gel_upract.gralin_upract')
        _template_5_turn_motion_ground_cfl_upract_bot = get_object('.template_5_turn_motion.ground.cfl_upract_bot').location
        _template_5_turn_motion_ground_hpl_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpl_upract_sf_atch_1').location
        gralin_upract.length = (VecUtils.DM(_template_5_turn_motion_ground_cfl_upract_bot, _template_5_turn_motion_ground_hpl_upract_sf_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.gel_upract.gralin_upract', exc)

    try:
        uer_actuator_i_1 = get_object('.template_5_turn_motion.ger_upract.uer_actuator_i_1')
        relative_to = get_object('.template_5_turn_motion.ger_upract')
        uer_actuator_i_1.relative_to = relative_to
        uer_actuator_i_1.marker_name = target_path('.template_5_turn_motion.ger_upract.uer_actuator_i_1')
        _template_5_turn_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpr_upract_sf_atch_1')
        uer_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_upract_sf_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_i_1.location, uer_actuator_i_1.orientation)
        uer_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upract.uer_actuator_i_1', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ger_upract.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ger_upract')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ger_upract.inertia_frame')
        _template_5_turn_motion_ger_upract_cm = get_object('.template_5_turn_motion.ger_upract.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upract_cm))
        _template_5_turn_motion_ger_upract = get_object('.template_5_turn_motion.ger_upract')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upract))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upract.inertia_frame', exc)

    try:
        gralin_19 = get_object('.template_5_turn_motion.ger_upract.gralin_19')
        relative_to = get_object('.template_5_turn_motion.ger_upract')
        gralin_19.relative_to = relative_to
        gralin_19.marker_name = target_path('.template_5_turn_motion.ger_upract.gralin_19')
        _template_5_turn_motion_ground_cfr_upract_bot = get_object('.template_5_turn_motion.ground.cfr_upract_bot')
        gralin_19.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_upract_bot))
        _template_5_turn_motion_ground_cfr_upract_bot = get_object('.template_5_turn_motion.ground.cfr_upract_bot').location
        _template_5_turn_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpr_upract_sf_atch_1').location
        gralin_19.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_cfr_upract_bot, _template_5_turn_motion_ground_hpr_upract_sf_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_19.location, gralin_19.orientation)
        gralin_19.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_19.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upract.gralin_19', exc)

    try:
        jxr_joint_j_8 = get_object('.template_5_turn_motion.ger_upract.jxr_joint_j_8')
        relative_to = get_object('.template_5_turn_motion.ger_upract')
        jxr_joint_j_8.relative_to = relative_to
        jxr_joint_j_8.marker_name = target_path('.template_5_turn_motion.ger_upract.jxr_joint_j_8')
        _template_5_turn_motion_ground_cfr_lwract_top = get_object('.template_5_turn_motion.ground.cfr_lwract_top')
        jxr_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfr_lwract_top))
        _template_5_turn_motion_ground_hpr_lwract_uc_atch_1 = get_object('.template_5_turn_motion.ground.hpr_lwract_uc_atch_1').location
        _template_5_turn_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpr_upract_sf_atch_1').location
        jxr_joint_j_8.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_lwract_uc_atch_1, _template_5_turn_motion_ground_hpr_upract_sf_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxr_joint_j_8.location, jxr_joint_j_8.orientation)
        jxr_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxr_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upract.jxr_joint_j_8', exc)

    try:
        uer_stopper_j_2 = get_object('.template_5_turn_motion.ger_upract.uer_stopper_j_2')
        relative_to = get_object('.template_5_turn_motion.ger_upract')
        uer_stopper_j_2.relative_to = relative_to
        uer_stopper_j_2.marker_name = target_path('.template_5_turn_motion.ger_upract.uer_stopper_j_2')
        _template_5_turn_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpr_upract_sf_atch_1')
        uer_stopper_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_upract_sf_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_stopper_j_2.location, uer_stopper_j_2.orientation)
        uer_stopper_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upract.uer_stopper_j_2', exc)

    try:
        uer_actuator_j_2 = get_object('.template_5_turn_motion.ger_upract.uer_actuator_j_2')
        relative_to = get_object('.template_5_turn_motion.ger_upract')
        uer_actuator_j_2.relative_to = relative_to
        uer_actuator_j_2.marker_name = target_path('.template_5_turn_motion.ger_upract.uer_actuator_j_2')
        _template_5_turn_motion_ger_upract_jxr_joint_j_8 = get_object('.template_5_turn_motion.ger_upract.jxr_joint_j_8')
        uer_actuator_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upract_jxr_joint_j_8))
        _template_5_turn_motion_ger_upract_jxr_joint_j_8 = get_object('.template_5_turn_motion.ger_upract.jxr_joint_j_8')
        uer_actuator_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ger_upract_jxr_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uer_actuator_j_2.location, uer_actuator_j_2.orientation)
        uer_actuator_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        uer_actuator_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ger_upract.uer_actuator_j_2', exc)

    try:
        gralin_upract = get_object('.template_5_turn_motion.ger_upract.gralin_upract')
        gralin_upract.cylinder_name = target_path('.template_5_turn_motion.ger_upract.gralin_upract')
        _template_5_turn_motion_ground_cfr_upract_bot = get_object('.template_5_turn_motion.ground.cfr_upract_bot').location
        _template_5_turn_motion_ground_hpr_upract_sf_atch_1 = get_object('.template_5_turn_motion.ground.hpr_upract_sf_atch_1').location
        gralin_upract.length = (VecUtils.DM(_template_5_turn_motion_ground_cfr_upract_bot, _template_5_turn_motion_ground_hpr_upract_sf_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ger_upract.gralin_upract', exc)

    try:
        gfo_i = get_object('.template_5_turn_motion.luntai1.wheel_part.gfo_i')
        relative_to = get_object('.template_5_turn_motion.luntai1.wheel_part')
        gfo_i.relative_to = relative_to
        gfo_i.marker_name = target_path('.template_5_turn_motion.luntai1.wheel_part.gfo_i')
        _template_5_turn_motion_luntai1_wheel_part_wheel_cm = get_object('.template_5_turn_motion.luntai1.wheel_part.wheel_cm')
        gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _template_5_turn_motion_luntai1_wheel_part_wheel_cm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
        gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.luntai1.wheel_part.gfo_i', exc)

    try:
        gfo_i = get_object('.template_5_turn_motion.luntai2.wheel_part.gfo_i')
        relative_to = get_object('.template_5_turn_motion.luntai2.wheel_part')
        gfo_i.relative_to = relative_to
        gfo_i.marker_name = target_path('.template_5_turn_motion.luntai2.wheel_part.gfo_i')
        _template_5_turn_motion_luntai2_wheel_part_wheel_cm = get_object('.template_5_turn_motion.luntai2.wheel_part.wheel_cm')
        gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _template_5_turn_motion_luntai2_wheel_part_wheel_cm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
        gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.luntai2.wheel_part.gfo_i', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ges_dragbrace.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ges_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ges_dragbrace.inertia_frame')
        _template_5_turn_motion_ges_dragbrace_cm = get_object('.template_5_turn_motion.ges_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_dragbrace_cm))
        _template_5_turn_motion_ges_dragbrace = get_object('.template_5_turn_motion.ges_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_dragbrace.inertia_frame', exc)

    try:
        gralin_1 = get_object('.template_5_turn_motion.ges_dragbrace.gralin_1')
        relative_to = get_object('.template_5_turn_motion.ges_dragbrace')
        gralin_1.relative_to = relative_to
        gralin_1.marker_name = target_path('.template_5_turn_motion.ges_dragbrace.gralin_1')
        _template_5_turn_motion_ground_hps_db_sf_atch = get_object('.template_5_turn_motion.ground.hps_db_sf_atch')
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_db_sf_atch))
        _template_5_turn_motion_ground_hps_db_sf_atch = get_object('.template_5_turn_motion.ground.hps_db_sf_atch').location
        _template_5_turn_motion_ground_hps_db_uc_atch = get_object('.template_5_turn_motion.ground.hps_db_uc_atch').location
        gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_db_sf_atch, _template_5_turn_motion_ground_hps_db_uc_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_dragbrace.gralin_1', exc)

    try:
        jxs_joint_i_12 = get_object('.template_5_turn_motion.ges_dragbrace.jxs_joint_i_12')
        relative_to = get_object('.template_5_turn_motion.ges_dragbrace')
        jxs_joint_i_12.relative_to = relative_to
        jxs_joint_i_12.marker_name = target_path('.template_5_turn_motion.ges_dragbrace.jxs_joint_i_12')
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_12 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_12')
        jxs_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_12))
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_12 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_12')
        jxs_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_12.location, jxs_joint_i_12.orientation)
        jxs_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_dragbrace.jxs_joint_i_12', exc)

    try:
        gralin_dragbrace_geom = get_object('.template_5_turn_motion.ges_dragbrace.gralin_dragbrace_geom')
        gralin_dragbrace_geom.cylinder_name = target_path('.template_5_turn_motion.ges_dragbrace.gralin_dragbrace_geom')
        _template_5_turn_motion_ground_hps_db_sf_atch = get_object('.template_5_turn_motion.ground.hps_db_sf_atch').location
        _template_5_turn_motion_ground_hps_db_uc_atch = get_object('.template_5_turn_motion.ground.hps_db_uc_atch').location
        gralin_dragbrace_geom.length = (VecUtils.DM(_template_5_turn_motion_ground_hps_db_sf_atch, _template_5_turn_motion_ground_hps_db_uc_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ges_dragbrace.gralin_dragbrace_geom', exc)

    try:
        MARKER_491 = get_object('.template_5_turn_motion.ges_dragbrace.MARKER_491')
        relative_to = get_object('.template_5_turn_motion.ges_dragbrace')
        MARKER_491.relative_to = relative_to
        MARKER_491.marker_name = target_path('.template_5_turn_motion.ges_dragbrace.MARKER_491')
        _template_5_turn_motion_ground_hps_db_sf_atch = get_object('.template_5_turn_motion.ground.hps_db_sf_atch')
        MARKER_491.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_db_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_491.location, MARKER_491.orientation)
        MARKER_491.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_dragbrace.MARKER_491', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ges_upper_cylinder.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.inertia_frame')
        _template_5_turn_motion_ges_upper_cylinder_cm = get_object('.template_5_turn_motion.ges_upper_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_cm))
        _template_5_turn_motion_ges_upper_cylinder = get_object('.template_5_turn_motion.ges_upper_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.inertia_frame', exc)

    try:
        gralin_2 = get_object('.template_5_turn_motion.ges_upper_cylinder.gralin_2')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        gralin_2.relative_to = relative_to
        gralin_2.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.gralin_2')
        _template_5_turn_motion_ground_hps_uc_top = get_object('.template_5_turn_motion.ground.hps_uc_top')
        gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_uc_top))
        _template_5_turn_motion_ground_hps_uc_top = get_object('.template_5_turn_motion.ground.hps_uc_top').location
        _template_5_turn_motion_ground_hps_uc_bot = get_object('.template_5_turn_motion.ground.hps_uc_bot').location
        gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_uc_top, _template_5_turn_motion_ground_hps_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_2.location, gralin_2.orientation)
        gralin_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.gralin_2', exc)

    try:
        gralin_3 = get_object('.template_5_turn_motion.ges_upper_cylinder.gralin_3')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.gralin_3')
        _template_5_turn_motion_ground_hps_uc_sf_atch_l = get_object('.template_5_turn_motion.ground.hps_uc_sf_atch_l')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_uc_sf_atch_l))
        _template_5_turn_motion_ground_hps_uc_sf_atch_l = get_object('.template_5_turn_motion.ground.hps_uc_sf_atch_l').location
        _template_5_turn_motion_ground_hps_uc_geompt = get_object('.template_5_turn_motion.ground.hps_uc_geompt').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_uc_sf_atch_l, _template_5_turn_motion_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.gralin_3', exc)

    try:
        gralin_4 = get_object('.template_5_turn_motion.ges_upper_cylinder.gralin_4')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        gralin_4.relative_to = relative_to
        gralin_4.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.gralin_4')
        _template_5_turn_motion_ground_hps_uc_sf_atch_r = get_object('.template_5_turn_motion.ground.hps_uc_sf_atch_r')
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_uc_sf_atch_r))
        _template_5_turn_motion_ground_hps_uc_sf_atch_r = get_object('.template_5_turn_motion.ground.hps_uc_sf_atch_r').location
        _template_5_turn_motion_ground_hps_uc_geompt = get_object('.template_5_turn_motion.ground.hps_uc_geompt').location
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_uc_sf_atch_r, _template_5_turn_motion_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.gralin_4', exc)

    try:
        jxs_joint_j_12 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_12')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        jxs_joint_j_12.relative_to = relative_to
        jxs_joint_j_12.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_12')
        _template_5_turn_motion_ground_hps_db_uc_atch = get_object('.template_5_turn_motion.ground.hps_db_uc_atch')
        jxs_joint_j_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_db_uc_atch))
        _template_5_turn_motion_ground_origo1 = get_object('.template_5_turn_motion.ground.origo1')
        jxs_joint_j_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_12.location, jxs_joint_j_12.orientation)
        jxs_joint_j_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_12', exc)

    try:
        ues_spring_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.ues_spring_j_1')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        ues_spring_j_1.relative_to = relative_to
        ues_spring_j_1.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.ues_spring_j_1')
        _template_5_turn_motion_ground_hps_uc_top = get_object('.template_5_turn_motion.ground.hps_uc_top')
        ues_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_j_1.location, ues_spring_j_1.orientation)
        ues_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.ues_spring_j_1', exc)

    try:
        ues_damper_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.ues_damper_j_1')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        ues_damper_j_1.relative_to = relative_to
        ues_damper_j_1.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.ues_damper_j_1')
        _template_5_turn_motion_ground_hps_uc_top = get_object('.template_5_turn_motion.ground.hps_uc_top')
        ues_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_j_1.location, ues_damper_j_1.orientation)
        ues_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.ues_damper_j_1', exc)

    try:
        ues_stopper_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.ues_stopper_j_1')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        ues_stopper_j_1.relative_to = relative_to
        ues_stopper_j_1.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.ues_stopper_j_1')
        _template_5_turn_motion_ground_hps_uc_top = get_object('.template_5_turn_motion.ground.hps_uc_top')
        ues_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_j_1.location, ues_stopper_j_1.orientation)
        ues_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.ues_stopper_j_1', exc)

    try:
        jxs_joint_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_1')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        jxs_joint_j_1.relative_to = relative_to
        jxs_joint_j_1.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_1')
        _template_5_turn_motion_ground_cfs_collar_top = get_object('.template_5_turn_motion.ground.cfs_collar_top')
        jxs_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfs_collar_top))
        _template_5_turn_motion_ground_hps_uc_bot = get_object('.template_5_turn_motion.ground.hps_uc_bot').location
        _template_5_turn_motion_ground_hps_uc_top = get_object('.template_5_turn_motion.ground.hps_uc_top').location
        jxs_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_uc_bot, _template_5_turn_motion_ground_hps_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
        jxs_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_1', exc)

    try:
        ues_actuator_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.ues_actuator_j_1')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        ues_actuator_j_1.relative_to = relative_to
        ues_actuator_j_1.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.ues_actuator_j_1')
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1))
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_1.location, ues_actuator_j_1.orientation)
        ues_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.ues_actuator_j_1', exc)

    try:
        ues_actuator_j_4 = get_object('.template_5_turn_motion.ges_upper_cylinder.ues_actuator_j_4')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        ues_actuator_j_4.relative_to = relative_to
        ues_actuator_j_4.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.ues_actuator_j_4')
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1))
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_4.location, ues_actuator_j_4.orientation)
        ues_actuator_j_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_j_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.ues_actuator_j_4', exc)

    try:
        gralin_upper_cylinder_geom1 = get_object('.template_5_turn_motion.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        gralin_upper_cylinder_geom1.cylinder_name = target_path('.template_5_turn_motion.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        _template_5_turn_motion_ground_hps_uc_top = get_object('.template_5_turn_motion.ground.hps_uc_top').location
        _template_5_turn_motion_ground_hps_uc_bot = get_object('.template_5_turn_motion.ground.hps_uc_bot').location
        gralin_upper_cylinder_geom1.length = (VecUtils.DM(_template_5_turn_motion_ground_hps_uc_top, _template_5_turn_motion_ground_hps_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ges_upper_cylinder.gralin_upper_cylinder_geom1', exc)

    try:
        gralin_upper_cylinder_geom2 = get_object('.template_5_turn_motion.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        gralin_upper_cylinder_geom2.cylinder_name = target_path('.template_5_turn_motion.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        _template_5_turn_motion_ground_hps_uc_sf_atch_l = get_object('.template_5_turn_motion.ground.hps_uc_sf_atch_l').location
        _template_5_turn_motion_ground_hps_uc_geompt = get_object('.template_5_turn_motion.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom2.length = (VecUtils.DM(_template_5_turn_motion_ground_hps_uc_sf_atch_l, _template_5_turn_motion_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ges_upper_cylinder.gralin_upper_cylinder_geom2', exc)

    try:
        gralin_upper_cylinder_geom3 = get_object('.template_5_turn_motion.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        gralin_upper_cylinder_geom3.cylinder_name = target_path('.template_5_turn_motion.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        _template_5_turn_motion_ground_hps_uc_sf_atch_r = get_object('.template_5_turn_motion.ground.hps_uc_sf_atch_r').location
        _template_5_turn_motion_ground_hps_uc_geompt = get_object('.template_5_turn_motion.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom3.length = (VecUtils.DM(_template_5_turn_motion_ground_hps_uc_sf_atch_r, _template_5_turn_motion_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ges_upper_cylinder.gralin_upper_cylinder_geom3', exc)

    try:
        MARKER_467 = get_object('.template_5_turn_motion.ges_upper_cylinder.MARKER_467')
        relative_to = get_object('.template_5_turn_motion.ges_upper_cylinder')
        MARKER_467.relative_to = relative_to
        MARKER_467.marker_name = target_path('.template_5_turn_motion.ges_upper_cylinder.MARKER_467')
        _template_5_turn_motion_ground_zdt1 = get_object('.template_5_turn_motion.ground.zdt1')
        MARKER_467.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_zdt1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_467.location, MARKER_467.orientation)
        MARKER_467.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_cylinder.MARKER_467', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ges_lower_cylinder.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.inertia_frame')
        _template_5_turn_motion_ges_lower_cylinder_cm = get_object('.template_5_turn_motion.ges_lower_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_lower_cylinder_cm))
        _template_5_turn_motion_ges_lower_cylinder = get_object('.template_5_turn_motion.ges_lower_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_lower_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.inertia_frame', exc)

    try:
        gralin_5 = get_object('.template_5_turn_motion.ges_lower_cylinder.gralin_5')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.gralin_5')
        _template_5_turn_motion_ground_hps_lc_top = get_object('.template_5_turn_motion.ground.hps_lc_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_lc_top))
        _template_5_turn_motion_ground_hps_lc_top = get_object('.template_5_turn_motion.ground.hps_lc_top').location
        _template_5_turn_motion_ground_hps_lc_bot = get_object('.template_5_turn_motion.ground.hps_lc_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_lc_top, _template_5_turn_motion_ground_hps_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.gralin_5', exc)

    try:
        jxs_joint_i_11 = get_object('.template_5_turn_motion.ges_lower_cylinder.jxs_joint_i_11')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        jxs_joint_i_11.relative_to = relative_to
        jxs_joint_i_11.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.jxs_joint_i_11')
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_11))
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
        jxs_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.jxs_joint_i_11', exc)

    try:
        gralin_7 = get_object('.template_5_turn_motion.ges_lower_cylinder.gralin_7')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        gralin_7.relative_to = relative_to
        gralin_7.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.gralin_7')
        _template_5_turn_motion_ground_hpr_wheel_center1 = get_object('.template_5_turn_motion.ground.hpr_wheel_center1')
        gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_wheel_center1))
        _template_5_turn_motion_ground_hpr_wheel_center1 = get_object('.template_5_turn_motion.ground.hpr_wheel_center1').location
        _template_5_turn_motion_ground_hpl_wheel_center1 = get_object('.template_5_turn_motion.ground.hpl_wheel_center1').location
        gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hpr_wheel_center1, _template_5_turn_motion_ground_hpl_wheel_center1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.gralin_7', exc)

    try:
        ues_spring_i_1 = get_object('.template_5_turn_motion.ges_lower_cylinder.ues_spring_i_1')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        ues_spring_i_1.relative_to = relative_to
        ues_spring_i_1.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.ues_spring_i_1')
        _template_5_turn_motion_ground_hps_lc_top = get_object('.template_5_turn_motion.ground.hps_lc_top')
        ues_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_i_1.location, ues_spring_i_1.orientation)
        ues_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.ues_spring_i_1', exc)

    try:
        ues_damper_i_1 = get_object('.template_5_turn_motion.ges_lower_cylinder.ues_damper_i_1')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        ues_damper_i_1.relative_to = relative_to
        ues_damper_i_1.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.ues_damper_i_1')
        _template_5_turn_motion_ground_hps_lc_top = get_object('.template_5_turn_motion.ground.hps_lc_top')
        ues_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_i_1.location, ues_damper_i_1.orientation)
        ues_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.ues_damper_i_1', exc)

    try:
        ues_stopper_i_1 = get_object('.template_5_turn_motion.ges_lower_cylinder.ues_stopper_i_1')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        ues_stopper_i_1.relative_to = relative_to
        ues_stopper_i_1.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.ues_stopper_i_1')
        _template_5_turn_motion_ground_hps_lc_top = get_object('.template_5_turn_motion.ground.hps_lc_top')
        ues_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_i_1.location, ues_stopper_i_1.orientation)
        ues_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.ues_stopper_i_1', exc)

    try:
        coomarker_2 = get_object('.template_5_turn_motion.ges_lower_cylinder.coomarker_2')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        coomarker_2.relative_to = relative_to
        coomarker_2.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.coomarker_2')
        _template_5_turn_motion_ground_cfs_wheel_centers_midpoint = get_object('.template_5_turn_motion.ground.cfs_wheel_centers_midpoint')
        coomarker_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfs_wheel_centers_midpoint))
        _template_5_turn_motion_ground_cfs_wheel_centers_midpoint = get_object('.template_5_turn_motion.ground.cfs_wheel_centers_midpoint')
        coomarker_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfs_wheel_centers_midpoint))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_2.location, coomarker_2.orientation)
        coomarker_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.coomarker_2', exc)

    try:
        coomarker_3 = get_object('.template_5_turn_motion.ges_lower_cylinder.coomarker_3')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        coomarker_3.relative_to = relative_to
        coomarker_3.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.coomarker_3')
        _template_5_turn_motion_ground_cfs_nlg_axle_lowpoint = get_object('.template_5_turn_motion.ground.cfs_nlg_axle_lowpoint')
        coomarker_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfs_nlg_axle_lowpoint))
        _template_5_turn_motion_ground_cfs_nlg_axle_lowpoint = get_object('.template_5_turn_motion.ground.cfs_nlg_axle_lowpoint')
        coomarker_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_cfs_nlg_axle_lowpoint))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_3.location, coomarker_3.orientation)
        coomarker_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.coomarker_3', exc)

    try:
        MARKER_3 = get_object('.template_5_turn_motion.ges_lower_cylinder.MARKER_3')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        MARKER_3.relative_to = relative_to
        MARKER_3.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.MARKER_3')
        _template_5_turn_motion_ground_hpl_wheel_center1 = get_object('.template_5_turn_motion.ground.hpl_wheel_center1')
        MARKER_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_wheel_center1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_3.location, MARKER_3.orientation)
        MARKER_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.MARKER_3', exc)

    try:
        MARKER_4 = get_object('.template_5_turn_motion.ges_lower_cylinder.MARKER_4')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        MARKER_4.relative_to = relative_to
        MARKER_4.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.MARKER_4')
        _template_5_turn_motion_ground_hpr_wheel_center1 = get_object('.template_5_turn_motion.ground.hpr_wheel_center1')
        MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_wheel_center1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_4.location, MARKER_4.orientation)
        MARKER_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.MARKER_4', exc)

    try:
        gralin_geom1 = get_object('.template_5_turn_motion.ges_lower_cylinder.gralin_geom1')
        gralin_geom1.cylinder_name = target_path('.template_5_turn_motion.ges_lower_cylinder.gralin_geom1')
        _template_5_turn_motion_ground_hps_lc_top = get_object('.template_5_turn_motion.ground.hps_lc_top').location
        _template_5_turn_motion_ground_hps_lc_bot = get_object('.template_5_turn_motion.ground.hps_lc_bot').location
        gralin_geom1.length = (VecUtils.DM(_template_5_turn_motion_ground_hps_lc_top, _template_5_turn_motion_ground_hps_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ges_lower_cylinder.gralin_geom1', exc)

    try:
        gralin_geom2 = get_object('.template_5_turn_motion.ges_lower_cylinder.gralin_geom2')
        gralin_geom2.cylinder_name = target_path('.template_5_turn_motion.ges_lower_cylinder.gralin_geom2')
        _template_5_turn_motion_ground_hpr_wheel_center1 = get_object('.template_5_turn_motion.ground.hpr_wheel_center1').location
        _template_5_turn_motion_ground_hpl_wheel_center1 = get_object('.template_5_turn_motion.ground.hpl_wheel_center1').location
        gralin_geom2.length = (VecUtils.DM(_template_5_turn_motion_ground_hpr_wheel_center1, _template_5_turn_motion_ground_hpl_wheel_center1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ges_lower_cylinder.gralin_geom2', exc)

    try:
        MARKER_378 = get_object('.template_5_turn_motion.ges_lower_cylinder.MARKER_378')
        relative_to = get_object('.template_5_turn_motion.ges_lower_cylinder')
        MARKER_378.relative_to = relative_to
        MARKER_378.marker_name = target_path('.template_5_turn_motion.ges_lower_cylinder.MARKER_378')
        _template_5_turn_motion_ground_hps_lta_lc_atch = get_object('.template_5_turn_motion.ground.hps_lta_lc_atch')
        MARKER_378.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_lta_lc_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_378.location, MARKER_378.orientation)
        MARKER_378.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_cylinder.MARKER_378', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ges_upper_torque_arm.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ges_upper_torque_arm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ges_upper_torque_arm.inertia_frame')
        _template_5_turn_motion_ges_upper_torque_arm_cm = get_object('.template_5_turn_motion.ges_upper_torque_arm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_torque_arm_cm))
        _template_5_turn_motion_ges_upper_torque_arm = get_object('.template_5_turn_motion.ges_upper_torque_arm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_torque_arm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_torque_arm.inertia_frame', exc)

    try:
        gralin_9 = get_object('.template_5_turn_motion.ges_upper_torque_arm.gralin_9')
        relative_to = get_object('.template_5_turn_motion.ges_upper_torque_arm')
        gralin_9.relative_to = relative_to
        gralin_9.marker_name = target_path('.template_5_turn_motion.ges_upper_torque_arm.gralin_9')
        _template_5_turn_motion_ground_hps_uta_uc_atch = get_object('.template_5_turn_motion.ground.hps_uta_uc_atch')
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_uta_uc_atch))
        _template_5_turn_motion_ground_hps_uta_uc_atch = get_object('.template_5_turn_motion.ground.hps_uta_uc_atch').location
        _template_5_turn_motion_ground_hps_lta_uta_atch = get_object('.template_5_turn_motion.ground.hps_lta_uta_atch').location
        gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_uta_uc_atch, _template_5_turn_motion_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_torque_arm.gralin_9', exc)

    try:
        jxs_joint_j_8 = get_object('.template_5_turn_motion.ges_upper_torque_arm.jxs_joint_j_8')
        relative_to = get_object('.template_5_turn_motion.ges_upper_torque_arm')
        jxs_joint_j_8.relative_to = relative_to
        jxs_joint_j_8.marker_name = target_path('.template_5_turn_motion.ges_upper_torque_arm.jxs_joint_j_8')
        _template_5_turn_motion_ground_hps_lta_uta_atch = get_object('.template_5_turn_motion.ground.hps_lta_uta_atch')
        jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_lta_uta_atch))
        _template_5_turn_motion_ground_origo1 = get_object('.template_5_turn_motion.ground.origo1')
        jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_5_turn_motion_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
        jxs_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_torque_arm.jxs_joint_j_8', exc)

    try:
        jxs_joint_i_10 = get_object('.template_5_turn_motion.ges_upper_torque_arm.jxs_joint_i_10')
        relative_to = get_object('.template_5_turn_motion.ges_upper_torque_arm')
        jxs_joint_i_10.relative_to = relative_to
        jxs_joint_i_10.marker_name = target_path('.template_5_turn_motion.ges_upper_torque_arm.jxs_joint_i_10')
        _template_5_turn_motion_ges_collar_jxs_joint_j_10 = get_object('.template_5_turn_motion.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_collar_jxs_joint_j_10))
        _template_5_turn_motion_ges_collar_jxs_joint_j_10 = get_object('.template_5_turn_motion.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_collar_jxs_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
        jxs_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_upper_torque_arm.jxs_joint_i_10', exc)

    try:
        gralin_upper_torque_arm_geom = get_object('.template_5_turn_motion.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        gralin_upper_torque_arm_geom.cylinder_name = target_path('.template_5_turn_motion.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        _template_5_turn_motion_ground_hps_uta_uc_atch = get_object('.template_5_turn_motion.ground.hps_uta_uc_atch').location
        _template_5_turn_motion_ground_hps_lta_uta_atch = get_object('.template_5_turn_motion.ground.hps_lta_uta_atch').location
        gralin_upper_torque_arm_geom.length = (VecUtils.DM(_template_5_turn_motion_ground_hps_uta_uc_atch, _template_5_turn_motion_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ges_upper_torque_arm.gralin_upper_torque_arm_geom', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ges_lower_torque_arm.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ges_lower_torque_arm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ges_lower_torque_arm.inertia_frame')
        _template_5_turn_motion_ges_lower_torque_arm_cm = get_object('.template_5_turn_motion.ges_lower_torque_arm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_lower_torque_arm_cm))
        _template_5_turn_motion_ges_lower_torque_arm = get_object('.template_5_turn_motion.ges_lower_torque_arm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_lower_torque_arm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_torque_arm.inertia_frame', exc)

    try:
        jxs_joint_i_8 = get_object('.template_5_turn_motion.ges_lower_torque_arm.jxs_joint_i_8')
        relative_to = get_object('.template_5_turn_motion.ges_lower_torque_arm')
        jxs_joint_i_8.relative_to = relative_to
        jxs_joint_i_8.marker_name = target_path('.template_5_turn_motion.ges_lower_torque_arm.jxs_joint_i_8')
        _template_5_turn_motion_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_5_turn_motion.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_torque_arm_jxs_joint_j_8))
        _template_5_turn_motion_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_5_turn_motion.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_torque_arm_jxs_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
        jxs_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_torque_arm.jxs_joint_i_8', exc)

    try:
        gralin_10 = get_object('.template_5_turn_motion.ges_lower_torque_arm.gralin_10')
        relative_to = get_object('.template_5_turn_motion.ges_lower_torque_arm')
        gralin_10.relative_to = relative_to
        gralin_10.marker_name = target_path('.template_5_turn_motion.ges_lower_torque_arm.gralin_10')
        _template_5_turn_motion_ground_hps_lta_lc_atch = get_object('.template_5_turn_motion.ground.hps_lta_lc_atch')
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_lta_lc_atch))
        _template_5_turn_motion_ground_hps_lta_lc_atch = get_object('.template_5_turn_motion.ground.hps_lta_lc_atch').location
        _template_5_turn_motion_ground_hps_lta_uta_atch = get_object('.template_5_turn_motion.ground.hps_lta_uta_atch').location
        gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_lta_lc_atch, _template_5_turn_motion_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_torque_arm.gralin_10', exc)

    try:
        gralin_lower_torque_arm_geom = get_object('.template_5_turn_motion.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        gralin_lower_torque_arm_geom.cylinder_name = target_path('.template_5_turn_motion.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        _template_5_turn_motion_ground_hps_lta_lc_atch = get_object('.template_5_turn_motion.ground.hps_lta_lc_atch').location
        _template_5_turn_motion_ground_hps_lta_uta_atch = get_object('.template_5_turn_motion.ground.hps_lta_uta_atch').location
        gralin_lower_torque_arm_geom.length = (VecUtils.DM(_template_5_turn_motion_ground_hps_lta_lc_atch, _template_5_turn_motion_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ges_lower_torque_arm.gralin_lower_torque_arm_geom', exc)

    try:
        MARKER_379 = get_object('.template_5_turn_motion.ges_lower_torque_arm.MARKER_379')
        relative_to = get_object('.template_5_turn_motion.ges_lower_torque_arm')
        MARKER_379.relative_to = relative_to
        MARKER_379.marker_name = target_path('.template_5_turn_motion.ges_lower_torque_arm.MARKER_379')
        _template_5_turn_motion_ground_hps_lta_lc_atch = get_object('.template_5_turn_motion.ground.hps_lta_lc_atch')
        MARKER_379.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_lta_lc_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_379.location, MARKER_379.orientation)
        MARKER_379.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_lower_torque_arm.MARKER_379', exc)

    try:
        jxs_joint_j_10 = get_object('.template_5_turn_motion.ges_collar.jxs_joint_j_10')
        relative_to = get_object('.template_5_turn_motion.ges_collar')
        jxs_joint_j_10.relative_to = relative_to
        jxs_joint_j_10.marker_name = target_path('.template_5_turn_motion.ges_collar.jxs_joint_j_10')
        _template_5_turn_motion_ground_hps_uta_uc_atch = get_object('.template_5_turn_motion.ground.hps_uta_uc_atch')
        jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_uta_uc_atch))
        _template_5_turn_motion_ground_origo1 = get_object('.template_5_turn_motion.ground.origo1')
        jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_5_turn_motion_ground_origo1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
        jxs_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_collar.jxs_joint_j_10', exc)

    try:
        inertia_frame = get_object('.template_5_turn_motion.ges_collar.inertia_frame')
        relative_to = get_object('.template_5_turn_motion.ges_collar')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_5_turn_motion.ges_collar.inertia_frame')
        _template_5_turn_motion_ges_collar_cm = get_object('.template_5_turn_motion.ges_collar.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_collar_cm))
        _template_5_turn_motion_ges_collar = get_object('.template_5_turn_motion.ges_collar')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_collar))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_collar.inertia_frame', exc)

    try:
        gralin_24 = get_object('.template_5_turn_motion.ges_collar.gralin_24')
        relative_to = get_object('.template_5_turn_motion.ges_collar')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_5_turn_motion.ges_collar.gralin_24')
        _template_5_turn_motion_ground_hps_uc_bot = get_object('.template_5_turn_motion.ground.hps_uc_bot')
        gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hps_uc_bot))
        _template_5_turn_motion_ground_hps_uc_bot = get_object('.template_5_turn_motion.ground.hps_uc_bot').location
        _template_5_turn_motion_ground_cfs_collar_top = get_object('.template_5_turn_motion.ground.cfs_collar_top').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hps_uc_bot, _template_5_turn_motion_ground_cfs_collar_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_collar.gralin_24', exc)

    try:
        jxs_joint_i_1 = get_object('.template_5_turn_motion.ges_collar.jxs_joint_i_1')
        relative_to = get_object('.template_5_turn_motion.ges_collar')
        jxs_joint_i_1.relative_to = relative_to
        jxs_joint_i_1.marker_name = target_path('.template_5_turn_motion.ges_collar.jxs_joint_i_1')
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1))
        _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_5_turn_motion.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
        jxs_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_collar.jxs_joint_i_1', exc)

    try:
        ues_actuator_i_1 = get_object('.template_5_turn_motion.ges_collar.ues_actuator_i_1')
        relative_to = get_object('.template_5_turn_motion.ges_collar')
        ues_actuator_i_1.relative_to = relative_to
        ues_actuator_i_1.marker_name = target_path('.template_5_turn_motion.ges_collar.ues_actuator_i_1')
        _template_5_turn_motion_ges_collar_jxs_joint_i_1 = get_object('.template_5_turn_motion.ges_collar.jxs_joint_i_1')
        ues_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_collar_jxs_joint_i_1))
        _template_5_turn_motion_ges_collar_jxs_joint_i_1 = get_object('.template_5_turn_motion.ges_collar.jxs_joint_i_1')
        ues_actuator_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_collar_jxs_joint_i_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_1.location, ues_actuator_i_1.orientation)
        ues_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_collar.ues_actuator_i_1', exc)

    try:
        ues_actuator_i_4 = get_object('.template_5_turn_motion.ges_collar.ues_actuator_i_4')
        relative_to = get_object('.template_5_turn_motion.ges_collar')
        ues_actuator_i_4.relative_to = relative_to
        ues_actuator_i_4.marker_name = target_path('.template_5_turn_motion.ges_collar.ues_actuator_i_4')
        _template_5_turn_motion_ges_collar_jxs_joint_i_1 = get_object('.template_5_turn_motion.ges_collar.jxs_joint_i_1')
        ues_actuator_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_collar_jxs_joint_i_1))
        _template_5_turn_motion_ges_collar_jxs_joint_i_1 = get_object('.template_5_turn_motion.ges_collar.jxs_joint_i_1')
        ues_actuator_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ges_collar_jxs_joint_i_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_4.location, ues_actuator_i_4.orientation)
        ues_actuator_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_collar.ues_actuator_i_4', exc)

    try:
        gralin_collar = get_object('.template_5_turn_motion.ges_collar.gralin_collar')
        gralin_collar.cylinder_name = target_path('.template_5_turn_motion.ges_collar.gralin_collar')
        _template_5_turn_motion_ground_hps_uc_bot = get_object('.template_5_turn_motion.ground.hps_uc_bot').location
        _template_5_turn_motion_ground_cfs_collar_top = get_object('.template_5_turn_motion.ground.cfs_collar_top').location
        gralin_collar.length = (VecUtils.DM(_template_5_turn_motion_ground_hps_uc_bot, _template_5_turn_motion_ground_cfs_collar_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.ges_collar.gralin_collar', exc)

    try:
        MARKER_465 = get_object('.template_5_turn_motion.ges_collar.MARKER_465')
        relative_to = get_object('.template_5_turn_motion.ges_collar')
        MARKER_465.relative_to = relative_to
        MARKER_465.marker_name = target_path('.template_5_turn_motion.ges_collar.MARKER_465')
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1')
        MARKER_465.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hsg_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_465.location, MARKER_465.orientation)
        MARKER_465.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.ges_collar.MARKER_465', exc)

    try:
        gfo_i = get_object('.template_5_turn_motion.luntai1_2.wheel_part.gfo_i')
        relative_to = get_object('.template_5_turn_motion.luntai1_2.wheel_part')
        gfo_i.relative_to = relative_to
        gfo_i.marker_name = target_path('.template_5_turn_motion.luntai1_2.wheel_part.gfo_i')
        _template_5_turn_motion_luntai1_2_wheel_part_wheel_cm = get_object('.template_5_turn_motion.luntai1_2.wheel_part.wheel_cm')
        gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _template_5_turn_motion_luntai1_2_wheel_part_wheel_cm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
        gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.luntai1_2.wheel_part.gfo_i', exc)

    try:
        gfo_i = get_object('.template_5_turn_motion.luntai2_2.wheel_part.gfo_i')
        relative_to = get_object('.template_5_turn_motion.luntai2_2.wheel_part')
        gfo_i.relative_to = relative_to
        gfo_i.marker_name = target_path('.template_5_turn_motion.luntai2_2.wheel_part.gfo_i')
        _template_5_turn_motion_luntai2_2_wheel_part_wheel_cm = get_object('.template_5_turn_motion.luntai2_2.wheel_part.wheel_cm')
        gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _template_5_turn_motion_luntai2_2_wheel_part_wheel_cm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
        gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.luntai2_2.wheel_part.gfo_i', exc)

    try:
        MARKER_443 = get_object('.template_5_turn_motion.js.MARKER_443')
        relative_to = get_object('.template_5_turn_motion.js')
        MARKER_443.relative_to = relative_to
        MARKER_443.marker_name = target_path('.template_5_turn_motion.js.MARKER_443')
        _template_5_turn_motion_ground_hpr_uc_top = get_object('.template_5_turn_motion.ground.hpr_uc_top')
        MARKER_443.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpr_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_443.location, MARKER_443.orientation)
        MARKER_443.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.js.MARKER_443', exc)

    try:
        MARKER_445 = get_object('.template_5_turn_motion.js.MARKER_445')
        relative_to = get_object('.template_5_turn_motion.js')
        MARKER_445.relative_to = relative_to
        MARKER_445.marker_name = target_path('.template_5_turn_motion.js.MARKER_445')
        _template_5_turn_motion_ground_hpl_uc_top = get_object('.template_5_turn_motion.ground.hpl_uc_top')
        MARKER_445.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_445.location, MARKER_445.orientation)
        MARKER_445.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.js.MARKER_445', exc)

    try:
        gralin_463 = get_object('.template_5_turn_motion.hsg.gralin_463')
        relative_to = get_object('.template_5_turn_motion.hsg')
        gralin_463.relative_to = relative_to
        gralin_463.marker_name = target_path('.template_5_turn_motion.hsg.gralin_463')
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1')
        gralin_463.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hsg_1))
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1').location
        _template_5_turn_motion_ground_hsg_2 = get_object('.template_5_turn_motion.ground.hsg_2').location
        gralin_463.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_hsg_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_463.location, gralin_463.orientation)
        gralin_463.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_463.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.hsg.gralin_463', exc)

    try:
        CYLINDER_213 = get_object('.template_5_turn_motion.hsg.CYLINDER_213')
        CYLINDER_213.cylinder_name = target_path('.template_5_turn_motion.hsg.CYLINDER_213')
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1').location
        _template_5_turn_motion_ground_hsg_2 = get_object('.template_5_turn_motion.ground.hsg_2').location
        CYLINDER_213.length = (VecUtils.DM(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_hsg_2))
        CYLINDER_213.radius = 0.022


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.hsg.CYLINDER_213', exc)

    try:
        MARKER_466 = get_object('.template_5_turn_motion.hsg.MARKER_466')
        relative_to = get_object('.template_5_turn_motion.hsg')
        MARKER_466.relative_to = relative_to
        MARKER_466.marker_name = target_path('.template_5_turn_motion.hsg.MARKER_466')
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1')
        MARKER_466.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_hsg_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_466.location, MARKER_466.orientation)
        MARKER_466.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.hsg.MARKER_466', exc)

    try:
        MARKER_469 = get_object('.template_5_turn_motion.hsg.MARKER_469')
        relative_to = get_object('.template_5_turn_motion.hsg')
        MARKER_469.relative_to = relative_to
        MARKER_469.marker_name = target_path('.template_5_turn_motion.hsg.MARKER_469')
        _template_5_turn_motion_zdt_cm = get_object('.template_5_turn_motion.zdt.cm')
        MARKER_469.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_zdt_cm))
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1').location
        _template_5_turn_motion_ground_zdt1 = get_object('.template_5_turn_motion.ground.zdt1').location
        MARKER_469.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_zdt1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_469.location, MARKER_469.orientation)
        MARKER_469.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_469.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.hsg.MARKER_469', exc)

    try:
        gralin_464 = get_object('.template_5_turn_motion.zdt.gralin_464')
        relative_to = get_object('.template_5_turn_motion.zdt')
        gralin_464.relative_to = relative_to
        gralin_464.marker_name = target_path('.template_5_turn_motion.zdt.gralin_464')
        _template_5_turn_motion_ground_zdt1 = get_object('.template_5_turn_motion.ground.zdt1')
        gralin_464.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_zdt1))
        _template_5_turn_motion_ground_zdt1 = get_object('.template_5_turn_motion.ground.zdt1').location
        _template_5_turn_motion_ground_zdt2 = get_object('.template_5_turn_motion.ground.zdt2').location
        gralin_464.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_zdt1, _template_5_turn_motion_ground_zdt2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_464.location, gralin_464.orientation)
        gralin_464.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_464.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.zdt.gralin_464', exc)

    try:
        CYLINDER_214 = get_object('.template_5_turn_motion.zdt.CYLINDER_214')
        CYLINDER_214.cylinder_name = target_path('.template_5_turn_motion.zdt.CYLINDER_214')
        _template_5_turn_motion_ground_zdt1 = get_object('.template_5_turn_motion.ground.zdt1').location
        _template_5_turn_motion_ground_zdt2 = get_object('.template_5_turn_motion.ground.zdt2').location
        CYLINDER_214.length = (VecUtils.DM(_template_5_turn_motion_ground_zdt1, _template_5_turn_motion_ground_zdt2))
        CYLINDER_214.radius = 0.042


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_5_turn_motion.zdt.CYLINDER_214', exc)

    try:
        MARKER_468 = get_object('.template_5_turn_motion.zdt.MARKER_468')
        relative_to = get_object('.template_5_turn_motion.zdt')
        MARKER_468.relative_to = relative_to
        MARKER_468.marker_name = target_path('.template_5_turn_motion.zdt.MARKER_468')
        _template_5_turn_motion_ground_zdt1 = get_object('.template_5_turn_motion.ground.zdt1')
        MARKER_468.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_ground_zdt1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_468.location, MARKER_468.orientation)
        MARKER_468.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.zdt.MARKER_468', exc)

    try:
        MARKER_470 = get_object('.template_5_turn_motion.zdt.MARKER_470')
        relative_to = get_object('.template_5_turn_motion.zdt')
        MARKER_470.relative_to = relative_to
        MARKER_470.marker_name = target_path('.template_5_turn_motion.zdt.MARKER_470')
        _template_5_turn_motion_zdt_cm = get_object('.template_5_turn_motion.zdt.cm')
        MARKER_470.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_5_turn_motion_zdt_cm))
        _template_5_turn_motion_ground_hsg_1 = get_object('.template_5_turn_motion.ground.hsg_1').location
        _template_5_turn_motion_ground_zdt1 = get_object('.template_5_turn_motion.ground.zdt1').location
        MARKER_470.orientation = (VecUtils.ORI_ALONG_AXIS(_template_5_turn_motion_ground_hsg_1, _template_5_turn_motion_ground_zdt1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_470.location, MARKER_470.orientation)
        MARKER_470.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_470.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_5_turn_motion.zdt.MARKER_470', exc)

    if model_dir is None:
        model_dir = os.path.dirname(os.path.abspath(__file__))
    resource_path_1 = os.path.abspath(os.path.join(model_dir, 'MLG.tir'))
    if not os.path.isfile(resource_path_1):
        record_error('轮胎文件路径（MLG.tir）', FileNotFoundError(resource_path_1))
    else:
        try:
            if set_resource('.template_5_turn_motion.luntai1.tpf_file', resource_path_1):
                updated += 1
        except Exception as exc:
            record_error('轮胎文件路径（MLG.tir）', exc)
    resource_path_2 = os.path.abspath(os.path.join(model_dir, '2d_flat.rdf'))
    if not os.path.isfile(resource_path_2):
        record_error('路面文件路径（2d_flat.rdf）', FileNotFoundError(resource_path_2))
    else:
        try:
            if set_resource('.template_5_turn_motion.luntai1.rpf_file', resource_path_2):
                updated += 1
        except Exception as exc:
            record_error('路面文件路径（2d_flat.rdf）', exc)
    resource_path_3 = os.path.abspath(os.path.join(model_dir, 'MLG.tir'))
    if not os.path.isfile(resource_path_3):
        record_error('轮胎文件路径（MLG.tir）', FileNotFoundError(resource_path_3))
    else:
        try:
            if set_resource('.template_5_turn_motion.luntai2.tpf_file', resource_path_3):
                updated += 1
        except Exception as exc:
            record_error('轮胎文件路径（MLG.tir）', exc)
    resource_path_4 = os.path.abspath(os.path.join(model_dir, '2d_flat.rdf'))
    if not os.path.isfile(resource_path_4):
        record_error('路面文件路径（2d_flat.rdf）', FileNotFoundError(resource_path_4))
    else:
        try:
            if set_resource('.template_5_turn_motion.luntai2.rpf_file', resource_path_4):
                updated += 1
        except Exception as exc:
            record_error('路面文件路径（2d_flat.rdf）', exc)
    resource_path_5 = os.path.abspath(os.path.join(model_dir, 'NLG.tir'))
    if not os.path.isfile(resource_path_5):
        record_error('轮胎文件路径（NLG.tir）', FileNotFoundError(resource_path_5))
    else:
        try:
            if set_resource('.template_5_turn_motion.luntai1_2.tpf_file', resource_path_5):
                updated += 1
        except Exception as exc:
            record_error('轮胎文件路径（NLG.tir）', exc)
    resource_path_6 = os.path.abspath(os.path.join(model_dir, '2d_flat.rdf'))
    if not os.path.isfile(resource_path_6):
        record_error('路面文件路径（2d_flat.rdf）', FileNotFoundError(resource_path_6))
    else:
        try:
            if set_resource('.template_5_turn_motion.luntai1_2.rpf_file', resource_path_6):
                updated += 1
        except Exception as exc:
            record_error('路面文件路径（2d_flat.rdf）', exc)
    resource_path_7 = os.path.abspath(os.path.join(model_dir, 'NLG.tir'))
    if not os.path.isfile(resource_path_7):
        record_error('轮胎文件路径（NLG.tir）', FileNotFoundError(resource_path_7))
    else:
        try:
            if set_resource('.template_5_turn_motion.luntai2_2.tpf_file', resource_path_7):
                updated += 1
        except Exception as exc:
            record_error('轮胎文件路径（NLG.tir）', exc)
    resource_path_8 = os.path.abspath(os.path.join(model_dir, '2d_flat.rdf'))
    if not os.path.isfile(resource_path_8):
        record_error('路面文件路径（2d_flat.rdf）', FileNotFoundError(resource_path_8))
    else:
        try:
            if set_resource('.template_5_turn_motion.luntai2_2.rpf_file', resource_path_8):
                updated += 1
        except Exception as exc:
            record_error('路面文件路径（2d_flat.rdf）', exc)
    return {'updated': updated, 'warnings': warnings, 'errors': errors}

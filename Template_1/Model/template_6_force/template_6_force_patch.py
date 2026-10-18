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

SOURCE_MODEL_NAME = 'template_6_force'
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
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=10.0 step_size=1.0E-02 model_name=.gcmb6_force')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_3')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_3')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=.retract_mlg_force')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_3', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_2_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_2_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_2_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_3_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_3_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_nlg_post_2hubs')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_3_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_2_2_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_2_2_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_2_2_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_4')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_4')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=13.0 step_size=1.0E-02 model_name=.retract_suo_force_nlg_mlg')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_4', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_2_3')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_2_3')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_2_3', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_3_3')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_3_3')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=.retract_mlg_force')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_3_3', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_2_2_3')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_2_2_3')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_2_2_3', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_3_2_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_3_2_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_nlg_post_2hubs')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_3_2_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_2_2_2_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_2_2_2_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_2_2_2_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_4_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_4_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=13.0 step_size=1.0E-02 model_name=.retract_suo_force_nlg_mlg')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_4_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_2_3_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_2_3_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_2_3_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_3_3_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_3_3_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=.retract_mlg_force')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_3_3_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_2_2_3_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_2_2_3_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_2_2_3_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_3_2_2_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_3_2_2_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_nlg_post_2hubs')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_3_2_2_2', exc)

    try:
        node = get_or_create('SimuScript', '.template_6_force.Last_Sim_2_2_2_2_2')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_6_force.Last_Sim_2_2_2_2_2')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=12.0 step_size=1.0E-02 model_name=._AA_mlg_post_1hub_retract')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_6_force.Last_Sim_2_2_2_2_2', exc)

    try:
        node = get_object('.template_6_force.nlg_ZDT_FORCE')
        node.function = rewrite_expression('STEP( time , 0 , 0 , .template_6_force.nlg_zdtup_t1 , .template_6_force.NLG_RETRACT_FORCE )+STEP( time , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME , 0 , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3 , -.template_6_force.NLG_RETRACT_FORCE )+STEP( time , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3+.template_6_force.nlg_zdt_t0 , 0 , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3+.template_6_force.nlg_zdt_t0+.template_6_force.nlg_zdtdown_t1 , -.template_6_force.NLG_EXTEND_FORCE )+STEP( time , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3+.template_6_force.nlg_zdt_t0+.template_6_force.nlg_zdtdown_t1+.template_6_force.NLG_EXTEND_HOLD_TIME , 0 , .template_6_force.nlg_zdtup_t1+.template_6_force.NLG_RETRACT_HOLD_TIME+.template_6_force.nlg_zdtup_t3+.template_6_force.nlg_zdt_t0+.template_6_force.nlg_zdtdown_t1+.template_6_force.NLG_EXTEND_HOLD_TIME+.template_6_force.nlg_zdtdown_t3 , .template_6_force.NLG_EXTEND_FORCE )')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.nlg_ZDT_FORCE', exc)

    try:
        node = get_object('.template_6_force.nlg_suo_unlock')
        node.function = rewrite_expression('STEP( time , .template_6_force.NLG_LOCK_UNLOCK_TIME , 0 , .template_6_force.NLG_LOCK_UNLOCK_TIME+0.1 , -.template_6_force.NLG_UNLOCK_FORCE )+STEP( time , .template_6_force.NLG_LOCK_UNLOCK_TIME+1.0 , 0 , .template_6_force.NLG_LOCK_UNLOCK_TIME+1.1 , .template_6_force.NLG_UNLOCK_FORCE )')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.nlg_suo_unlock', exc)

    try:
        node = get_object('.template_6_force.NLG_stopper_low')
        node.function = rewrite_expression('-abs(IF( .template_6_force.NLG_disp_sf-1217.6474 :50000000000*abs(.template_6_force.NLG_disp_sf-1217.6474), 0 ,0 ))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.NLG_stopper_low', exc)

    try:
        node = get_object('.template_6_force.nlg_suo_rod_springdamper')
        node.function = rewrite_expression('-10.0*VR(.template_6_force.nlg_suo_rod.MARKER_1099,.template_6_force.nlg_suo_actuator.MARKER_1100)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.nlg_suo_rod_springdamper', exc)

    try:
        node = get_object('.template_6_force.nlg_suo_springF_1')
        node.function = rewrite_expression('-.template_6_force.NLG_LOCK_SPRING_K*(DM(.template_6_force.nlg_suo_liangan.MARKER_1382,.template_6_force.nlg_suo_suogou.MARKER_1383)-54.0458262355)-.template_6_force.NLG_LOCK_SPRING_C*VR(.template_6_force.nlg_suo_liangan.MARKER_1382,.template_6_force.nlg_suo_suogou.MARKER_1383)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.nlg_suo_springF_1', exc)

    try:
        node = get_object('.template_6_force.nlg_suo_springF_2')
        node.function = rewrite_expression('-.template_6_force.NLG_LOCK_SPRING_K*(DM(.template_6_force.nlg_suo_liangan.MARKER_1384,.template_6_force.nlg_suo_suogou.MARKER_1385)-54.0458262355)-.template_6_force.NLG_LOCK_SPRING_C*VR(.template_6_force.nlg_suo_liangan.MARKER_1384,.template_6_force.nlg_suo_suogou.MARKER_1385)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.nlg_suo_springF_2', exc)

    try:
        node = get_object('.template_6_force.mlg_suo_unlock_L')
        node.function = rewrite_expression('STEP( time , .template_6_force.MLG_LOCK_UNLOCK_TIME , 0 , .template_6_force.MLG_LOCK_UNLOCK_TIME+0.1 , -.template_6_force.MLG_UNLOCK_FORCE )+STEP( time , .template_6_force.MLG_LOCK_UNLOCK_TIME+1.0 , 0 , .template_6_force.MLG_LOCK_UNLOCK_TIME+1.1 , .template_6_force.MLG_UNLOCK_FORCE )')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_suo_unlock_L', exc)

    try:
        node = get_object('.template_6_force.mlg_suo_rod_springdamper_L')
        node.function = rewrite_expression('-10.0*VR(.template_6_force.mlg_suo_rod_L.MARKER_1099,.template_6_force.mlg_suo_actuator_L.MARKER_1100)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_suo_rod_springdamper_L', exc)

    try:
        node = get_object('.template_6_force.mlg_suo_springF_1_L')
        node.function = rewrite_expression('-.template_6_force.MLG_LOCK_SPRING_K*(DM(.template_6_force.mlg_suo_liangan_L.MARKER_1336,.template_6_force.mlg_suo_suogou_L.MARKER_1337)-60.0749531835)-.template_6_force.MLG_LOCK_SPRING_C*VR(.template_6_force.mlg_suo_liangan_L.MARKER_1336,.template_6_force.mlg_suo_suogou_L.MARKER_1337)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_suo_springF_1_L', exc)

    try:
        node = get_object('.template_6_force.mlg_suo_springF_2_L')
        node.function = rewrite_expression('-.template_6_force.MLG_LOCK_SPRING_K*(DM(.template_6_force.mlg_suo_liangan_L.MARKER_1338,.template_6_force.mlg_suo_suogou_L.MARKER_1339)-60.0749531835)-.template_6_force.MLG_LOCK_SPRING_C*VR(.template_6_force.mlg_suo_liangan_L.MARKER_1338,.template_6_force.mlg_suo_suogou_L.MARKER_1339)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_suo_springF_2_L', exc)

    try:
        node = get_object('.template_6_force.mlg_stopper_low_R')
        node.function = rewrite_expression('abs(IF(.template_6_force.mlg_sf_angle+0.1 :0, 0 ,10000000*abs(.template_6_force.mlg_sf_angle+0.1) ))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_stopper_low_R', exc)

    try:
        node = get_object('.template_6_force.mlg_suo_unlock_R')
        node.function = rewrite_expression('STEP( time , .template_6_force.MLG_LOCK_UNLOCK_TIME , 0 , .template_6_force.MLG_LOCK_UNLOCK_TIME+0.1 , -.template_6_force.MLG_UNLOCK_FORCE )+STEP( time , .template_6_force.MLG_LOCK_UNLOCK_TIME+1.0 , 0 , .template_6_force.MLG_LOCK_UNLOCK_TIME+1.1 , .template_6_force.MLG_UNLOCK_FORCE )')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_suo_unlock_R', exc)

    try:
        node = get_object('.template_6_force.mlg_suo_rod_springdamper_R')
        node.function = rewrite_expression('-10.0*VR(.template_6_force.mlg_suo_rod_R.MARKER_1099,.template_6_force.mlg_suo_actuator_R.MARKER_1100)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_suo_rod_springdamper_R', exc)

    try:
        node = get_object('.template_6_force.mlg_suo_springF_1_R')
        node.function = rewrite_expression('-.template_6_force.MLG_LOCK_SPRING_K*(DM(.template_6_force.mlg_suo_liangan_R.MARKER_1336,.template_6_force.mlg_suo_suogou_R.MARKER_1337)-60.0749531835)-.template_6_force.MLG_LOCK_SPRING_C*VR(.template_6_force.mlg_suo_liangan_R.MARKER_1336,.template_6_force.mlg_suo_suogou_R.MARKER_1337)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_suo_springF_1_R', exc)

    try:
        node = get_object('.template_6_force.mlg_suo_springF_2_R')
        node.function = rewrite_expression('-.template_6_force.MLG_LOCK_SPRING_K*(DM(.template_6_force.mlg_suo_liangan_R.MARKER_1338,.template_6_force.mlg_suo_suogou_R.MARKER_1339)-60.0749531835)-.template_6_force.MLG_LOCK_SPRING_C*VR(.template_6_force.mlg_suo_liangan_R.MARKER_1338,.template_6_force.mlg_suo_suogou_R.MARKER_1339)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_suo_springF_2_R', exc)

    try:
        node = get_object('.template_6_force.mlg_stopper_low_L')
        node.function = rewrite_expression('abs(IF(.template_6_force.mlg_sf_angle+0.1 :0, 0 ,10000000*abs(.template_6_force.mlg_sf_angle+0.1) ))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_stopper_low_L', exc)

    try:
        node = get_object('.template_6_force.mlg_zdtF_L')
        node.function = rewrite_expression('STEP( time , 0 , 0 , .template_6_force.mlg_zdtup_t1 , .template_6_force.MLG_RETRACT_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3 , -.template_6_force.MLG_RETRACT_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0 , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1 , -.template_6_force.MLG_EXTEND_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1+.template_6_force.MLG_EXTEND_HOLD_TIME , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1+.template_6_force.MLG_EXTEND_HOLD_TIME+.template_6_force.mlg_zdtdown_t3 ,.template_6_force.MLG_EXTEND_FORCE)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_zdtF_L', exc)

    try:
        node = get_object('.template_6_force.mlg_zdtF_R')
        node.function = rewrite_expression('STEP( time , 0 , 0 , .template_6_force.mlg_zdtup_t1 , .template_6_force.MLG_RETRACT_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3 , -.template_6_force.MLG_RETRACT_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0 , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1 , -.template_6_force.MLG_EXTEND_FORCE)+STEP( time , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1+.template_6_force.MLG_EXTEND_HOLD_TIME , 0 , .template_6_force.mlg_zdtup_t1+.template_6_force.MLG_RETRACT_HOLD_TIME+.template_6_force.mlg_zdtup_t3+.template_6_force.mlg_zdt_t0+.template_6_force.mlg_zdtdown_t1+.template_6_force.MLG_EXTEND_HOLD_TIME+.template_6_force.mlg_zdtdown_t3 ,.template_6_force.MLG_EXTEND_FORCE)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_6_force.mlg_zdtF_R', exc)

    try:
        node = get_object('.template_6_force.NLG_aeroforce')
        node.x_force_function = rewrite_expression('.template_6_force.NLG_DRAG_COEFF*abs(IF( -.template_6_force.NLG_sf_angle-60 : COS( 1.225*-.template_6_force.NLG_sf_angle*pi/180 ) , COS( 1.225*-.template_6_force.NLG_sf_angle*pi/180 ) , COS( -.template_6_force.NLG_sf_angle*pi/180 ) ))*.template_6_force.NLG_PROJ_AREA*cos(-.template_6_force.NLG_sf_angle*pi/180)*0.5*.template_6_force.AIR_DENSITY*.template_6_force.AIR_VELOCITY*abs(.template_6_force.AIR_VELOCITY)*cos(-.template_6_force.NLG_sf_angle*pi/180) ')
        node.y_force_function = rewrite_expression('0')
        node.z_force_function = rewrite_expression('.template_6_force.NLG_DRAG_COEFF*abs(IF( -.template_6_force.NLG_sf_angle-60 : COS( 1.225*-.template_6_force.NLG_sf_angle*pi/180 ) , COS( 1.225*-.template_6_force.NLG_sf_angle*pi/180 ) , COS( -.template_6_force.NLG_sf_angle*pi/180 ) ))*.template_6_force.NLG_PROJ_AREA*cos(-.template_6_force.NLG_sf_angle*pi/180)*0.5*.template_6_force.AIR_DENSITY*.template_6_force.AIR_VELOCITY*abs(.template_6_force.AIR_VELOCITY)*sin(-.template_6_force.NLG_sf_angle*pi/180) ')
        node.x_torque_function = rewrite_expression('0')
        node.y_torque_function = rewrite_expression('-1*CUBSPL( -1*.template_6_force.NLG_sf_angle, 0 , .template_6_force.SPLINE_angle_aeroforce, 0 )')
        node.z_torque_function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('force modify direct general_force .template_6_force.NLG_aeroforce', exc)

    try:
        mts_mount_j_2 = get_object('.template_6_force.ground.mts_mount_j_2')
        mts_mount_j_2.marker_name = target_path('.template_6_force.ground.mts_mount_j_2')
        _template_6_force_mts_body_mount = get_object('.template_6_force.mts_body_mount')
        mts_mount_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mts_body_mount))
        _template_6_force_mts_body_mount = get_object('.template_6_force.mts_body_mount')
        mts_mount_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mts_body_mount))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.mts_mount_j_2', exc)

    try:
        cfs_collar_top = get_object('.template_6_force.ground.cfs_collar_top')
        cfs_collar_top.marker_name = target_path('.template_6_force.ground.cfs_collar_top')
        _template_6_force_ground_hps_uc_bot = get_object('.template_6_force.ground.hps_uc_bot').location
        _template_6_force_ground_hps_uc_top = get_object('.template_6_force.ground.hps_uc_top').location
        cfs_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_6_force_ground_hps_uc_bot, _template_6_force_ground_hps_uc_top, 0.11 * VecUtils.DM(_template_6_force_ground_hps_uc_bot, _template_6_force_ground_hps_uc_top)))
        _template_6_force_ground_hps_uc_bot = get_object('.template_6_force.ground.hps_uc_bot').location
        _template_6_force_ground_hps_uc_top = get_object('.template_6_force.ground.hps_uc_top').location
        cfs_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_uc_bot, _template_6_force_ground_hps_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.cfs_collar_top', exc)

    try:
        MARKER_996 = get_object('.template_6_force.ground.MARKER_996')
        MARKER_996.marker_name = target_path('.template_6_force.ground.MARKER_996')
        _template_6_force_nlg_suo_suogou_PT200 = get_object('.template_6_force.nlg_suo_suogou.PT200')
        MARKER_996.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_suo_suogou_PT200))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.MARKER_996', exc)

    try:
        MARKER_1031 = get_object('.template_6_force.ground.MARKER_1031')
        MARKER_1031.marker_name = target_path('.template_6_force.ground.MARKER_1031')
        _template_6_force_ground_POINT_483 = get_object('.template_6_force.ground.POINT_483')
        MARKER_1031.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_483))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.MARKER_1031', exc)

    try:
        MARKER_1049 = get_object('.template_6_force.ground.MARKER_1049')
        MARKER_1049.marker_name = target_path('.template_6_force.ground.MARKER_1049')
        _template_6_force_ground_POINT_483 = get_object('.template_6_force.ground.POINT_483')
        MARKER_1049.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_483))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.MARKER_1049', exc)

    try:
        MARKER_1070 = get_object('.template_6_force.ground.MARKER_1070')
        MARKER_1070.marker_name = target_path('.template_6_force.ground.MARKER_1070')
        _template_6_force_nlg_suo_suogou_PT200 = get_object('.template_6_force.nlg_suo_suogou.PT200')
        MARKER_1070.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_suo_suogou_PT200))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.MARKER_1070', exc)

    try:
        MARKER_1313 = get_object('.template_6_force.ground.MARKER_1313')
        MARKER_1313.marker_name = target_path('.template_6_force.ground.MARKER_1313')
        _template_6_force_ground_hpl_uc_top = get_object('.template_6_force.ground.hpl_uc_top')
        MARKER_1313.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_uc_top))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.MARKER_1313', exc)

    try:
        MARKER_1335 = get_object('.template_6_force.ground.MARKER_1335')
        MARKER_1335.marker_name = target_path('.template_6_force.ground.MARKER_1335')
        _template_6_force_mlg_suo_suogou_L_PT200 = get_object('.template_6_force.mlg_suo_suogou_L.PT200')
        MARKER_1335.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mlg_suo_suogou_L_PT200))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.MARKER_1335', exc)

    try:
        MARKER_1470 = get_object('.template_6_force.ground.MARKER_1470')
        MARKER_1470.marker_name = target_path('.template_6_force.ground.MARKER_1470')
        _template_6_force_ground_hpl_db_top1_2 = get_object('.template_6_force.ground.hpl_db_top1_2')
        MARKER_1470.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_db_top1_2))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.MARKER_1470', exc)

    try:
        MARKER_1485 = get_object('.template_6_force.ground.MARKER_1485')
        MARKER_1485.marker_name = target_path('.template_6_force.ground.MARKER_1485')
        _template_6_force_ground_hpl_db_top = get_object('.template_6_force.ground.hpl_db_top')
        MARKER_1485.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_db_top))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.ground.MARKER_1485', exc)

    try:
        MARKER_1374 = get_object('.template_6_force.nlg_suo_liangan.MARKER_1374')
        relative_to = get_object('.template_6_force.nlg_suo_liangan')
        MARKER_1374.relative_to = relative_to
        MARKER_1374.marker_name = target_path('.template_6_force.nlg_suo_liangan.MARKER_1374')
        _template_6_force_ground_POINT_3 = get_object('.template_6_force.ground.POINT_3')
        MARKER_1374.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1374.location, MARKER_1374.orientation)
        MARKER_1374.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_liangan.MARKER_1374', exc)

    try:
        MARKER_1382 = get_object('.template_6_force.nlg_suo_liangan.MARKER_1382')
        relative_to = get_object('.template_6_force.nlg_suo_liangan')
        MARKER_1382.relative_to = relative_to
        MARKER_1382.marker_name = target_path('.template_6_force.nlg_suo_liangan.MARKER_1382')
        _template_6_force_ground_hps_spring_slg1 = get_object('.template_6_force.ground.hps_spring_slg1')
        MARKER_1382.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_spring_slg1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1382.location, MARKER_1382.orientation)
        MARKER_1382.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_liangan.MARKER_1382', exc)

    try:
        MARKER_1384 = get_object('.template_6_force.nlg_suo_liangan.MARKER_1384')
        relative_to = get_object('.template_6_force.nlg_suo_liangan')
        MARKER_1384.relative_to = relative_to
        MARKER_1384.marker_name = target_path('.template_6_force.nlg_suo_liangan.MARKER_1384')
        _template_6_force_ground_hps_spring_slg2 = get_object('.template_6_force.ground.hps_spring_slg2')
        MARKER_1384.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_spring_slg2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1384.location, MARKER_1384.orientation)
        MARKER_1384.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_liangan.MARKER_1384', exc)

    try:
        gralin_1 = get_object('.template_6_force.nlg_sf_actuator.gralin_1')
        relative_to = get_object('.template_6_force.nlg_sf_actuator')
        gralin_1.relative_to = relative_to
        gralin_1.marker_name = target_path('.template_6_force.nlg_sf_actuator.gralin_1')
        _template_6_force_ground_hps_db_sf_atch = get_object('.template_6_force.ground.hps_db_sf_atch')
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_db_sf_atch))
        _template_6_force_ground_hps_db_sf_atch = get_object('.template_6_force.ground.hps_db_sf_atch').location
        _template_6_force_ground_hps_db_uc_atch = get_object('.template_6_force.ground.hps_db_uc_atch').location
        gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_db_sf_atch, _template_6_force_ground_hps_db_uc_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_sf_actuator.gralin_1', exc)

    try:
        jxs_joint_i_14 = get_object('.template_6_force.nlg_sf_actuator.jxs_joint_i_14')
        relative_to = get_object('.template_6_force.nlg_sf_actuator')
        jxs_joint_i_14.relative_to = relative_to
        jxs_joint_i_14.marker_name = target_path('.template_6_force.nlg_sf_actuator.jxs_joint_i_14')
        _template_6_force_nlg_subframe_jxs_joint_j_14 = get_object('.template_6_force.nlg_subframe.jxs_joint_j_14')
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_subframe_jxs_joint_j_14))
        _template_6_force_nlg_subframe_jxs_joint_j_14 = get_object('.template_6_force.nlg_subframe.jxs_joint_j_14')
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_subframe_jxs_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_sf_actuator.jxs_joint_i_14', exc)

    try:
        MARKER_532 = get_object('.template_6_force.nlg_sf_actuator.MARKER_532')
        relative_to = get_object('.template_6_force.nlg_sf_actuator')
        MARKER_532.relative_to = relative_to
        MARKER_532.marker_name = target_path('.template_6_force.nlg_sf_actuator.MARKER_532')
        _template_6_force_ground_hps_db_sf_atch = get_object('.template_6_force.ground.hps_db_sf_atch')
        MARKER_532.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_db_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_532.location, MARKER_532.orientation)
        MARKER_532.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_sf_actuator.MARKER_532', exc)

    try:
        gralin_dragbrace_geom = get_object('.template_6_force.nlg_sf_actuator.gralin_dragbrace_geom')
        gralin_dragbrace_geom.cylinder_name = target_path('.template_6_force.nlg_sf_actuator.gralin_dragbrace_geom')
        _template_6_force_ground_hps_db_sf_atch = get_object('.template_6_force.ground.hps_db_sf_atch').location
        _template_6_force_ground_hps_db_uc_atch = get_object('.template_6_force.ground.hps_db_uc_atch').location
        gralin_dragbrace_geom.length = (VecUtils.DM(_template_6_force_ground_hps_db_sf_atch, _template_6_force_ground_hps_db_uc_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_sf_actuator.gralin_dragbrace_geom', exc)

    try:
        MARKER_4 = get_object('.template_6_force.nlg_upper_cylinder.MARKER_4')
        relative_to = get_object('.template_6_force.nlg_upper_cylinder')
        MARKER_4.relative_to = relative_to
        MARKER_4.marker_name = target_path('.template_6_force.nlg_upper_cylinder.MARKER_4')
        _template_6_force_nlg_sf_rod_PT3 = get_object('.template_6_force.nlg_sf_rod.PT3')
        MARKER_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_sf_rod_PT3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_4.location, MARKER_4.orientation)
        MARKER_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_upper_cylinder.MARKER_4', exc)

    try:
        gralin_2 = get_object('.template_6_force.nlg_upper_cylinder.gralin_2')
        relative_to = get_object('.template_6_force.nlg_upper_cylinder')
        gralin_2.relative_to = relative_to
        gralin_2.marker_name = target_path('.template_6_force.nlg_upper_cylinder.gralin_2')
        _template_6_force_ground_hps_uc_top = get_object('.template_6_force.ground.hps_uc_top')
        gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_uc_top))
        _template_6_force_ground_hps_uc_top = get_object('.template_6_force.ground.hps_uc_top').location
        _template_6_force_ground_hps_uc_bot = get_object('.template_6_force.ground.hps_uc_bot').location
        gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_uc_top, _template_6_force_ground_hps_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_2.location, gralin_2.orientation)
        gralin_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_upper_cylinder.gralin_2', exc)

    try:
        gralin_3 = get_object('.template_6_force.nlg_upper_cylinder.gralin_3')
        relative_to = get_object('.template_6_force.nlg_upper_cylinder')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_6_force.nlg_upper_cylinder.gralin_3')
        _template_6_force_ground_hps_uc_sf_atch_l = get_object('.template_6_force.ground.hps_uc_sf_atch_l')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_uc_sf_atch_l))
        _template_6_force_ground_hps_uc_sf_atch_l = get_object('.template_6_force.ground.hps_uc_sf_atch_l').location
        _template_6_force_ground_hps_uc_geompt = get_object('.template_6_force.ground.hps_uc_geompt').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_uc_sf_atch_l, _template_6_force_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_upper_cylinder.gralin_3', exc)

    try:
        gralin_4 = get_object('.template_6_force.nlg_upper_cylinder.gralin_4')
        relative_to = get_object('.template_6_force.nlg_upper_cylinder')
        gralin_4.relative_to = relative_to
        gralin_4.marker_name = target_path('.template_6_force.nlg_upper_cylinder.gralin_4')
        _template_6_force_ground_hps_uc_sf_atch_r = get_object('.template_6_force.ground.hps_uc_sf_atch_r')
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_uc_sf_atch_r))
        _template_6_force_ground_hps_uc_sf_atch_r = get_object('.template_6_force.ground.hps_uc_sf_atch_r').location
        _template_6_force_ground_hps_uc_geompt = get_object('.template_6_force.ground.hps_uc_geompt').location
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_uc_sf_atch_r, _template_6_force_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_upper_cylinder.gralin_4', exc)

    try:
        jxs_joint_j_1 = get_object('.template_6_force.nlg_upper_cylinder.jxs_joint_j_1')
        relative_to = get_object('.template_6_force.nlg_upper_cylinder')
        jxs_joint_j_1.relative_to = relative_to
        jxs_joint_j_1.marker_name = target_path('.template_6_force.nlg_upper_cylinder.jxs_joint_j_1')
        _template_6_force_ground_cfs_collar_top = get_object('.template_6_force.ground.cfs_collar_top')
        jxs_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_cfs_collar_top))
        _template_6_force_ground_hps_uc_bot = get_object('.template_6_force.ground.hps_uc_bot').location
        _template_6_force_ground_hps_uc_top = get_object('.template_6_force.ground.hps_uc_top').location
        jxs_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_uc_bot, _template_6_force_ground_hps_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
        jxs_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_upper_cylinder.jxs_joint_j_1', exc)

    try:
        gralin_upper_cylinder_geom1 = get_object('.template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom1')
        gralin_upper_cylinder_geom1.cylinder_name = target_path('.template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom1')
        _template_6_force_ground_hps_uc_top = get_object('.template_6_force.ground.hps_uc_top').location
        _template_6_force_ground_hps_uc_bot = get_object('.template_6_force.ground.hps_uc_bot').location
        gralin_upper_cylinder_geom1.length = (VecUtils.DM(_template_6_force_ground_hps_uc_top, _template_6_force_ground_hps_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom1', exc)

    try:
        gralin_upper_cylinder_geom2 = get_object('.template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom2')
        gralin_upper_cylinder_geom2.cylinder_name = target_path('.template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom2')
        _template_6_force_ground_hps_uc_sf_atch_l = get_object('.template_6_force.ground.hps_uc_sf_atch_l').location
        _template_6_force_ground_hps_uc_geompt = get_object('.template_6_force.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom2.length = (VecUtils.DM(_template_6_force_ground_hps_uc_sf_atch_l, _template_6_force_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom2', exc)

    try:
        gralin_upper_cylinder_geom3 = get_object('.template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom3')
        gralin_upper_cylinder_geom3.cylinder_name = target_path('.template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom3')
        _template_6_force_ground_hps_uc_sf_atch_r = get_object('.template_6_force.ground.hps_uc_sf_atch_r').location
        _template_6_force_ground_hps_uc_geompt = get_object('.template_6_force.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom3.length = (VecUtils.DM(_template_6_force_ground_hps_uc_sf_atch_r, _template_6_force_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_upper_cylinder.gralin_upper_cylinder_geom3', exc)

    try:
        gralin_5 = get_object('.template_6_force.nlg_lower_cylinder.gralin_5')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_6_force.nlg_lower_cylinder.gralin_5')
        _template_6_force_ground_hps_lc_top = get_object('.template_6_force.ground.hps_lc_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_lc_top))
        _template_6_force_ground_hps_lc_top = get_object('.template_6_force.ground.hps_lc_top').location
        _template_6_force_ground_hps_lc_bot = get_object('.template_6_force.ground.hps_lc_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_lc_top, _template_6_force_ground_hps_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.gralin_5', exc)

    try:
        jxs_joint_i_11 = get_object('.template_6_force.nlg_lower_cylinder.jxs_joint_i_11')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        jxs_joint_i_11.relative_to = relative_to
        jxs_joint_i_11.marker_name = target_path('.template_6_force.nlg_lower_cylinder.jxs_joint_i_11')
        _template_6_force_nlg_upper_cylinder_jxs_joint_j_11 = get_object('.template_6_force.nlg_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_upper_cylinder_jxs_joint_j_11))
        _template_6_force_nlg_upper_cylinder_jxs_joint_j_11 = get_object('.template_6_force.nlg_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_upper_cylinder_jxs_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
        jxs_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.jxs_joint_i_11', exc)

    try:
        gralin_7 = get_object('.template_6_force.nlg_lower_cylinder.gralin_7')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        gralin_7.relative_to = relative_to
        gralin_7.marker_name = target_path('.template_6_force.nlg_lower_cylinder.gralin_7')
        _template_6_force_ground_hpr_wheel_center = get_object('.template_6_force.ground.hpr_wheel_center')
        gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_wheel_center))
        _template_6_force_ground_hpr_wheel_center = get_object('.template_6_force.ground.hpr_wheel_center').location
        _template_6_force_ground_hpl_wheel_center = get_object('.template_6_force.ground.hpl_wheel_center').location
        gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hpr_wheel_center, _template_6_force_ground_hpl_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.gralin_7', exc)

    try:
        gralin_9 = get_object('.template_6_force.nlg_lower_cylinder.gralin_9')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        gralin_9.relative_to = relative_to
        gralin_9.marker_name = target_path('.template_6_force.nlg_lower_cylinder.gralin_9')
        _template_6_force_ground_hps_uta_uc_atch = get_object('.template_6_force.ground.hps_uta_uc_atch')
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_uta_uc_atch))
        _template_6_force_ground_hps_uta_uc_atch = get_object('.template_6_force.ground.hps_uta_uc_atch').location
        _template_6_force_ground_hps_lta_uta_atch = get_object('.template_6_force.ground.hps_lta_uta_atch').location
        gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_uta_uc_atch, _template_6_force_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.gralin_9', exc)

    try:
        gralin_10 = get_object('.template_6_force.nlg_lower_cylinder.gralin_10')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        gralin_10.relative_to = relative_to
        gralin_10.marker_name = target_path('.template_6_force.nlg_lower_cylinder.gralin_10')
        _template_6_force_ground_hps_lta_lc_atch = get_object('.template_6_force.ground.hps_lta_lc_atch')
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_lta_lc_atch))
        _template_6_force_ground_hps_lta_lc_atch = get_object('.template_6_force.ground.hps_lta_lc_atch').location
        _template_6_force_ground_hps_lta_uta_atch = get_object('.template_6_force.ground.hps_lta_uta_atch').location
        gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_lta_lc_atch, _template_6_force_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.gralin_10', exc)

    try:
        MARKER_359 = get_object('.template_6_force.nlg_lower_cylinder.MARKER_359')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        MARKER_359.relative_to = relative_to
        MARKER_359.marker_name = target_path('.template_6_force.nlg_lower_cylinder.MARKER_359')
        _template_6_force_ground_hps_lockroller_l = get_object('.template_6_force.ground.hps_lockroller_l')
        MARKER_359.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_lockroller_l))
        _template_6_force_ground_hps_lockroller_l = get_object('.template_6_force.ground.hps_lockroller_l').location
        _template_6_force_ground_hps_lockroller_l_2 = get_object('.template_6_force.ground.hps_lockroller_l_2').location
        MARKER_359.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_lockroller_l, _template_6_force_ground_hps_lockroller_l_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_359.location, MARKER_359.orientation)
        MARKER_359.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_359.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.MARKER_359', exc)

    try:
        MARKER_360 = get_object('.template_6_force.nlg_lower_cylinder.MARKER_360')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        MARKER_360.relative_to = relative_to
        MARKER_360.marker_name = target_path('.template_6_force.nlg_lower_cylinder.MARKER_360')
        _template_6_force_ground_hps_lockroller_r = get_object('.template_6_force.ground.hps_lockroller_r')
        MARKER_360.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_lockroller_r))
        _template_6_force_ground_hps_lockroller_r = get_object('.template_6_force.ground.hps_lockroller_r').location
        _template_6_force_ground_hps_lockroller_r_2 = get_object('.template_6_force.ground.hps_lockroller_r_2').location
        MARKER_360.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_lockroller_r, _template_6_force_ground_hps_lockroller_r_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_360.location, MARKER_360.orientation)
        MARKER_360.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_360.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.MARKER_360', exc)

    try:
        MARKER_361 = get_object('.template_6_force.nlg_lower_cylinder.MARKER_361')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        MARKER_361.relative_to = relative_to
        MARKER_361.marker_name = target_path('.template_6_force.nlg_lower_cylinder.MARKER_361')
        _template_6_force_ground_hps_lockroller_r_2 = get_object('.template_6_force.ground.hps_lockroller_r_2')
        MARKER_361.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_lockroller_r_2))
        _template_6_force_ground_hps_lockroller_r_2 = get_object('.template_6_force.ground.hps_lockroller_r_2').location
        _template_6_force_ground_hps_lockroller_l_2 = get_object('.template_6_force.ground.hps_lockroller_l_2').location
        MARKER_361.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_lockroller_r_2, _template_6_force_ground_hps_lockroller_l_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_361.location, MARKER_361.orientation)
        MARKER_361.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_361.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.MARKER_361', exc)

    try:
        MARKER_436 = get_object('.template_6_force.nlg_lower_cylinder.MARKER_436')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        MARKER_436.relative_to = relative_to
        MARKER_436.marker_name = target_path('.template_6_force.nlg_lower_cylinder.MARKER_436')
        _template_6_force_ground_suo_qiu_point = get_object('.template_6_force.ground.suo_qiu_point')
        MARKER_436.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_suo_qiu_point))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_436.location, MARKER_436.orientation)
        MARKER_436.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.MARKER_436', exc)

    try:
        MARKER_1562 = get_object('.template_6_force.nlg_lower_cylinder.MARKER_1562')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        MARKER_1562.relative_to = relative_to
        MARKER_1562.marker_name = target_path('.template_6_force.nlg_lower_cylinder.MARKER_1562')
        _template_6_force_ground_hpl_ob_axle = get_object('.template_6_force.ground.hpl_ob_axle')
        MARKER_1562.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_ob_axle))
        _template_6_force_ground_hpl_ob_axle = get_object('.template_6_force.ground.hpl_ob_axle').location
        _template_6_force_ground_hpl_wheel_center = get_object('.template_6_force.ground.hpl_wheel_center').location
        MARKER_1562.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hpl_ob_axle, _template_6_force_ground_hpl_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1562.location, MARKER_1562.orientation)
        MARKER_1562.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_1562.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.MARKER_1562', exc)

    try:
        MARKER_1563 = get_object('.template_6_force.nlg_lower_cylinder.MARKER_1563')
        relative_to = get_object('.template_6_force.nlg_lower_cylinder')
        MARKER_1563.relative_to = relative_to
        MARKER_1563.marker_name = target_path('.template_6_force.nlg_lower_cylinder.MARKER_1563')
        _template_6_force_ground_hpr_ob_axle = get_object('.template_6_force.ground.hpr_ob_axle')
        MARKER_1563.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_ob_axle))
        _template_6_force_ground_hpr_ob_axle = get_object('.template_6_force.ground.hpr_ob_axle').location
        _template_6_force_ground_hpr_wheel_center = get_object('.template_6_force.ground.hpr_wheel_center').location
        MARKER_1563.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hpr_ob_axle, _template_6_force_ground_hpr_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1563.location, MARKER_1563.orientation)
        MARKER_1563.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_1563.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_lower_cylinder.MARKER_1563', exc)

    try:
        gralin_geom1 = get_object('.template_6_force.nlg_lower_cylinder.gralin_geom1')
        gralin_geom1.cylinder_name = target_path('.template_6_force.nlg_lower_cylinder.gralin_geom1')
        _template_6_force_ground_hps_lc_top = get_object('.template_6_force.ground.hps_lc_top').location
        _template_6_force_ground_hps_lc_bot = get_object('.template_6_force.ground.hps_lc_bot').location
        gralin_geom1.length = (VecUtils.DM(_template_6_force_ground_hps_lc_top, _template_6_force_ground_hps_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_lower_cylinder.gralin_geom1', exc)

    try:
        gralin_geom2 = get_object('.template_6_force.nlg_lower_cylinder.gralin_geom2')
        gralin_geom2.cylinder_name = target_path('.template_6_force.nlg_lower_cylinder.gralin_geom2')
        _template_6_force_ground_hpr_wheel_center = get_object('.template_6_force.ground.hpr_wheel_center').location
        _template_6_force_ground_hpl_wheel_center = get_object('.template_6_force.ground.hpl_wheel_center').location
        gralin_geom2.length = (VecUtils.DM(_template_6_force_ground_hpr_wheel_center, _template_6_force_ground_hpl_wheel_center))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_lower_cylinder.gralin_geom2', exc)

    try:
        CYLINDER_128 = get_object('.template_6_force.nlg_lower_cylinder.CYLINDER_128')
        CYLINDER_128.cylinder_name = target_path('.template_6_force.nlg_lower_cylinder.CYLINDER_128')
        CYLINDER_128.length = 73.0
        CYLINDER_128.radius = 8.125


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_lower_cylinder.CYLINDER_128', exc)

    try:
        CYLINDER_132 = get_object('.template_6_force.nlg_lower_cylinder.CYLINDER_132')
        CYLINDER_132.cylinder_name = target_path('.template_6_force.nlg_lower_cylinder.CYLINDER_132')
        CYLINDER_132.length = 73.0
        CYLINDER_132.radius = 8.125


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_lower_cylinder.CYLINDER_132', exc)

    try:
        CYLINDER_136 = get_object('.template_6_force.nlg_lower_cylinder.CYLINDER_136')
        CYLINDER_136.cylinder_name = target_path('.template_6_force.nlg_lower_cylinder.CYLINDER_136')
        CYLINDER_136.length = 100.0
        CYLINDER_136.radius = 7.5


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_lower_cylinder.CYLINDER_136', exc)

    try:
        gralin_lower_torque_arm_geom = get_object('.template_6_force.nlg_lower_cylinder.gralin_lower_torque_arm_geom')
        gralin_lower_torque_arm_geom.cylinder_name = target_path('.template_6_force.nlg_lower_cylinder.gralin_lower_torque_arm_geom')
        _template_6_force_ground_hps_lta_lc_atch = get_object('.template_6_force.ground.hps_lta_lc_atch').location
        _template_6_force_ground_hps_lta_uta_atch = get_object('.template_6_force.ground.hps_lta_uta_atch').location
        gralin_lower_torque_arm_geom.length = (VecUtils.DM(_template_6_force_ground_hps_lta_lc_atch, _template_6_force_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_lower_cylinder.gralin_lower_torque_arm_geom', exc)

    try:
        gralin_upper_torque_arm_geom = get_object('.template_6_force.nlg_lower_cylinder.gralin_upper_torque_arm_geom')
        gralin_upper_torque_arm_geom.cylinder_name = target_path('.template_6_force.nlg_lower_cylinder.gralin_upper_torque_arm_geom')
        _template_6_force_ground_hps_uta_uc_atch = get_object('.template_6_force.ground.hps_uta_uc_atch').location
        _template_6_force_ground_hps_lta_uta_atch = get_object('.template_6_force.ground.hps_lta_uta_atch').location
        gralin_upper_torque_arm_geom.length = (VecUtils.DM(_template_6_force_ground_hps_uta_uc_atch, _template_6_force_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_lower_cylinder.gralin_upper_torque_arm_geom', exc)

    try:
        CYLINDER_882 = get_object('.template_6_force.nlg_lower_cylinder.CYLINDER_882')
        CYLINDER_882.cylinder_name = target_path('.template_6_force.nlg_lower_cylinder.CYLINDER_882')
        CYLINDER_882.radius = 120.0


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_lower_cylinder.CYLINDER_882', exc)

    try:
        MARKER_1027 = get_object('.template_6_force.nlg_suo_yaobi.MARKER_1027')
        relative_to = get_object('.template_6_force.nlg_suo_yaobi')
        MARKER_1027.relative_to = relative_to
        MARKER_1027.marker_name = target_path('.template_6_force.nlg_suo_yaobi.MARKER_1027')
        _template_6_force_ground_POINT_483 = get_object('.template_6_force.ground.POINT_483')
        MARKER_1027.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_483))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1027.location, MARKER_1027.orientation)
        MARKER_1027.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_yaobi.MARKER_1027', exc)

    try:
        MARKER_1030 = get_object('.template_6_force.nlg_suo_yaobi.MARKER_1030')
        relative_to = get_object('.template_6_force.nlg_suo_yaobi')
        MARKER_1030.relative_to = relative_to
        MARKER_1030.marker_name = target_path('.template_6_force.nlg_suo_yaobi.MARKER_1030')
        _template_6_force_ground_POINT_483 = get_object('.template_6_force.ground.POINT_483')
        MARKER_1030.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_483))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1030.location, MARKER_1030.orientation)
        MARKER_1030.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_yaobi.MARKER_1030', exc)

    try:
        MARKER_1048 = get_object('.template_6_force.nlg_suo_yaobi.MARKER_1048')
        relative_to = get_object('.template_6_force.nlg_suo_yaobi')
        MARKER_1048.relative_to = relative_to
        MARKER_1048.marker_name = target_path('.template_6_force.nlg_suo_yaobi.MARKER_1048')
        _template_6_force_ground_POINT_483 = get_object('.template_6_force.ground.POINT_483')
        MARKER_1048.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_483))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1048.location, MARKER_1048.orientation)
        MARKER_1048.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_yaobi.MARKER_1048', exc)

    try:
        CYLINDER_499 = get_object('.template_6_force.nlg_suo_rod.CYLINDER_499')
        CYLINDER_499.cylinder_name = target_path('.template_6_force.nlg_suo_rod.CYLINDER_499')
        CYLINDER_499.radius = 1.8


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_suo_rod.CYLINDER_499', exc)

    try:
        inertia_frame = get_object('.template_6_force.nlg_subframe.inertia_frame')
        relative_to = get_object('.template_6_force.nlg_subframe')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_6_force.nlg_subframe.inertia_frame')
        _template_6_force_nlg_subframe_cm = get_object('.template_6_force.nlg_subframe.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_subframe_cm))
        _template_6_force_nlg_subframe = get_object('.template_6_force.nlg_subframe')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_subframe))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_subframe.inertia_frame', exc)

    try:
        graout_1 = get_object('.template_6_force.nlg_subframe.graout_1')
        relative_to = get_object('.template_6_force.nlg_subframe')
        graout_1.relative_to = relative_to
        graout_1.marker_name = target_path('.template_6_force.nlg_subframe.graout_1')
        _template_6_force_ground_hps_uc_sf_atch_r = get_object('.template_6_force.ground.hps_uc_sf_atch_r')
        graout_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_uc_sf_atch_r))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_1.location, graout_1.orientation)
        graout_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_subframe.graout_1', exc)

    try:
        graout_2 = get_object('.template_6_force.nlg_subframe.graout_2')
        relative_to = get_object('.template_6_force.nlg_subframe')
        graout_2.relative_to = relative_to
        graout_2.marker_name = target_path('.template_6_force.nlg_subframe.graout_2')
        _template_6_force_ground_hps_uc_sf_atch_l = get_object('.template_6_force.ground.hps_uc_sf_atch_l')
        graout_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_uc_sf_atch_l))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_2.location, graout_2.orientation)
        graout_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_subframe.graout_2', exc)

    try:
        graout_3 = get_object('.template_6_force.nlg_subframe.graout_3')
        relative_to = get_object('.template_6_force.nlg_subframe')
        graout_3.relative_to = relative_to
        graout_3.marker_name = target_path('.template_6_force.nlg_subframe.graout_3')
        _template_6_force_ground_hps_db_sf_atch = get_object('.template_6_force.ground.hps_db_sf_atch')
        graout_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_db_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_3.location, graout_3.orientation)
        graout_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_subframe.graout_3', exc)

    try:
        jxs_joint_i_16 = get_object('.template_6_force.nlg_subframe.jxs_joint_i_16')
        relative_to = get_object('.template_6_force.nlg_subframe')
        jxs_joint_i_16.relative_to = relative_to
        jxs_joint_i_16.marker_name = target_path('.template_6_force.nlg_subframe.jxs_joint_i_16')
        _template_6_force_mts_body_mount_jxs_joint_j_16 = get_object('.template_6_force.mts_body_mount.jxs_joint_j_16')
        jxs_joint_i_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mts_body_mount_jxs_joint_j_16))
        _template_6_force_mts_body_mount_jxs_joint_j_16 = get_object('.template_6_force.mts_body_mount.jxs_joint_j_16')
        jxs_joint_i_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mts_body_mount_jxs_joint_j_16))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_16.location, jxs_joint_i_16.orientation)
        jxs_joint_i_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_subframe.jxs_joint_i_16', exc)

    try:
        jxs_joint_j_14 = get_object('.template_6_force.nlg_subframe.jxs_joint_j_14')
        relative_to = get_object('.template_6_force.nlg_subframe')
        jxs_joint_j_14.relative_to = relative_to
        jxs_joint_j_14.marker_name = target_path('.template_6_force.nlg_subframe.jxs_joint_j_14')
        _template_6_force_ground_hps_db_sf_atch = get_object('.template_6_force.ground.hps_db_sf_atch')
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_db_sf_atch))
        _template_6_force_ground_origo = get_object('.template_6_force.ground.origo')
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_6_force_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_subframe.jxs_joint_j_14', exc)

    try:
        MARKER_533 = get_object('.template_6_force.nlg_subframe.MARKER_533')
        relative_to = get_object('.template_6_force.nlg_subframe')
        MARKER_533.relative_to = relative_to
        MARKER_533.marker_name = target_path('.template_6_force.nlg_subframe.MARKER_533')
        _template_6_force_ground_hps_db_sf_atch = get_object('.template_6_force.ground.hps_db_sf_atch')
        MARKER_533.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_db_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_533.location, MARKER_533.orientation)
        MARKER_533.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_subframe.MARKER_533', exc)

    try:
        jxs_joint_j_16 = get_object('.template_6_force.mts_body_mount.jxs_joint_j_16')
        relative_to = get_object('.template_6_force.mts_body_mount')
        jxs_joint_j_16.relative_to = relative_to
        jxs_joint_j_16.marker_name = target_path('.template_6_force.mts_body_mount.jxs_joint_j_16')
        _template_6_force_ground_cfs_subframe_to_body_point = get_object('.template_6_force.ground.cfs_subframe_to_body_point')
        jxs_joint_j_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_cfs_subframe_to_body_point))
        _template_6_force_ground_origo = get_object('.template_6_force.ground.origo')
        jxs_joint_j_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_16.location, jxs_joint_j_16.orientation)
        jxs_joint_j_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mts_body_mount.jxs_joint_j_16', exc)

    try:
        mts_body_mount = get_object('.template_6_force.mts_body_mount')
        mts_body_mount.part_name = target_path('.template_6_force.mts_body_mount')
        _template_6_force_ground_cfs_subframe_to_body_point = get_object('.template_6_force.ground.cfs_subframe_to_body_point')
        mts_body_mount.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_cfs_subframe_to_body_point))
        _template_6_force_ground_origo = get_object('.template_6_force.ground.origo')
        mts_body_mount.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('part modify rigid_body name_and_position .template_6_force.mts_body_mount', exc)

    try:
        gralin_24 = get_object('.template_6_force.nlg_collar.gralin_24')
        relative_to = get_object('.template_6_force.nlg_collar')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_6_force.nlg_collar.gralin_24')
        _template_6_force_ground_hps_uc_bot = get_object('.template_6_force.ground.hps_uc_bot')
        gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_uc_bot))
        _template_6_force_ground_hps_uc_bot = get_object('.template_6_force.ground.hps_uc_bot').location
        _template_6_force_ground_cfs_collar_top = get_object('.template_6_force.ground.cfs_collar_top').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_ground_hps_uc_bot, _template_6_force_ground_cfs_collar_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_collar.gralin_24', exc)

    try:
        jxs_joint_i_1 = get_object('.template_6_force.nlg_collar.jxs_joint_i_1')
        relative_to = get_object('.template_6_force.nlg_collar')
        jxs_joint_i_1.relative_to = relative_to
        jxs_joint_i_1.marker_name = target_path('.template_6_force.nlg_collar.jxs_joint_i_1')
        _template_6_force_nlg_upper_cylinder_jxs_joint_j_1 = get_object('.template_6_force.nlg_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_upper_cylinder_jxs_joint_j_1))
        _template_6_force_nlg_upper_cylinder_jxs_joint_j_1 = get_object('.template_6_force.nlg_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
        jxs_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_collar.jxs_joint_i_1', exc)

    try:
        gralin_collar = get_object('.template_6_force.nlg_collar.gralin_collar')
        gralin_collar.cylinder_name = target_path('.template_6_force.nlg_collar.gralin_collar')
        _template_6_force_ground_hps_uc_bot = get_object('.template_6_force.ground.hps_uc_bot').location
        _template_6_force_ground_cfs_collar_top = get_object('.template_6_force.ground.cfs_collar_top').location
        gralin_collar.length = (VecUtils.DM(_template_6_force_ground_hps_uc_bot, _template_6_force_ground_cfs_collar_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_collar.gralin_collar', exc)

    try:
        MARKER_1105 = get_object('.template_6_force.nlg_suo_rod_base.MARKER_1105')
        relative_to = get_object('.template_6_force.nlg_suo_rod_base')
        MARKER_1105.relative_to = relative_to
        MARKER_1105.marker_name = target_path('.template_6_force.nlg_suo_rod_base.MARKER_1105')
        _template_6_force_ground_POINT_483 = get_object('.template_6_force.ground.POINT_483')
        MARKER_1105.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_483))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1105.location, MARKER_1105.orientation)
        MARKER_1105.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_rod_base.MARKER_1105', exc)

    try:
        MARKER_1113 = get_object('.template_6_force.nlg_suo_rod_base.MARKER_1113')
        relative_to = get_object('.template_6_force.nlg_suo_rod_base')
        MARKER_1113.relative_to = relative_to
        MARKER_1113.marker_name = target_path('.template_6_force.nlg_suo_rod_base.MARKER_1113')
        _template_6_force_nlg_suo_suogou_PT200 = get_object('.template_6_force.nlg_suo_suogou.PT200')
        MARKER_1113.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_suo_suogou_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1113.location, MARKER_1113.orientation)
        MARKER_1113.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_rod_base.MARKER_1113', exc)

    try:
        MARKER_5 = get_object('.template_6_force.nlg_sf_rod.MARKER_5')
        relative_to = get_object('.template_6_force.nlg_sf_rod')
        MARKER_5.relative_to = relative_to
        MARKER_5.marker_name = target_path('.template_6_force.nlg_sf_rod.MARKER_5')
        _template_6_force_nlg_sf_rod_PT3 = get_object('.template_6_force.nlg_sf_rod.PT3')
        MARKER_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_sf_rod_PT3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_5.location, MARKER_5.orientation)
        MARKER_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_sf_rod.MARKER_5', exc)

    try:
        gralin_25 = get_object('.template_6_force.nlg_sf_rod.gralin_25')
        relative_to = get_object('.template_6_force.nlg_sf_rod')
        gralin_25.relative_to = relative_to
        gralin_25.marker_name = target_path('.template_6_force.nlg_sf_rod.gralin_25')
        _template_6_force_ground_hps_rod_bot = get_object('.template_6_force.ground.hps_rod_bot')
        gralin_25.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_rod_bot))
        _template_6_force_nlg_sf_rod_PT3 = get_object('.template_6_force.nlg_sf_rod.PT3').location
        _template_6_force_ground_hps_db_sf_atch = get_object('.template_6_force.ground.hps_db_sf_atch').location
        gralin_25.orientation = (VecUtils.ORI_ALONG_AXIS(_template_6_force_nlg_sf_rod_PT3, _template_6_force_ground_hps_db_sf_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_25.location, gralin_25.orientation)
        gralin_25.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_25.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_sf_rod.gralin_25', exc)

    try:
        CYLINDER_30 = get_object('.template_6_force.nlg_sf_rod.CYLINDER_30')
        CYLINDER_30.cylinder_name = target_path('.template_6_force.nlg_sf_rod.CYLINDER_30')
        _template_6_force_ground_hps_rod_bot = get_object('.template_6_force.ground.hps_rod_bot').location
        _template_6_force_ground_hps_rod_top = get_object('.template_6_force.ground.hps_rod_top').location
        CYLINDER_30.length = (VecUtils.DM(_template_6_force_ground_hps_rod_bot, _template_6_force_ground_hps_rod_top))
        CYLINDER_30.radius = 27.5


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.nlg_sf_rod.CYLINDER_30', exc)

    try:
        MARKER_1336 = get_object('.template_6_force.mlg_suo_liangan_L.MARKER_1336')
        relative_to = get_object('.template_6_force.mlg_suo_liangan_L')
        MARKER_1336.relative_to = relative_to
        MARKER_1336.marker_name = target_path('.template_6_force.mlg_suo_liangan_L.MARKER_1336')
        _template_6_force_ground_mlg_suo_spring_lg1 = get_object('.template_6_force.ground.mlg_suo_spring_lg1')
        MARKER_1336.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_mlg_suo_spring_lg1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1336.location, MARKER_1336.orientation)
        MARKER_1336.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_liangan_L.MARKER_1336', exc)

    try:
        MARKER_1338 = get_object('.template_6_force.mlg_suo_liangan_L.MARKER_1338')
        relative_to = get_object('.template_6_force.mlg_suo_liangan_L')
        MARKER_1338.relative_to = relative_to
        MARKER_1338.marker_name = target_path('.template_6_force.mlg_suo_liangan_L.MARKER_1338')
        _template_6_force_ground_mlg_suo_spring_lg2 = get_object('.template_6_force.ground.mlg_suo_spring_lg2')
        MARKER_1338.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_mlg_suo_spring_lg2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1338.location, MARKER_1338.orientation)
        MARKER_1338.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_liangan_L.MARKER_1338', exc)

    try:
        MARKER_998 = get_object('.template_6_force.mlg_suo_liangan_L.MARKER_998')
        relative_to = get_object('.template_6_force.mlg_suo_liangan_L')
        MARKER_998.relative_to = relative_to
        MARKER_998.marker_name = target_path('.template_6_force.mlg_suo_liangan_L.MARKER_998')
        _template_6_force_ground_POINT_636 = get_object('.template_6_force.ground.POINT_636')
        MARKER_998.location = (VecUtils.LOC_RELATIVE_TO([-4.3751313683e-07, -1.0769163339e-11, 0.0], _template_6_force_ground_POINT_636))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_998.location, MARKER_998.orientation)
        MARKER_998.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_liangan_L.MARKER_998', exc)

    try:
        MARKER_1468 = get_object('.template_6_force.mlg_dragbrace_R.MARKER_1468')
        relative_to = get_object('.template_6_force.mlg_dragbrace_R')
        MARKER_1468.relative_to = relative_to
        MARKER_1468.marker_name = target_path('.template_6_force.mlg_dragbrace_R.MARKER_1468')
        _template_6_force_ground_hpl_db_top1_2 = get_object('.template_6_force.ground.hpl_db_top1_2')
        MARKER_1468.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_db_top1_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1468.location, MARKER_1468.orientation)
        MARKER_1468.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_dragbrace_R.MARKER_1468', exc)

    try:
        MARKER_1469 = get_object('.template_6_force.mlg_dragbrace_R.MARKER_1469')
        relative_to = get_object('.template_6_force.mlg_dragbrace_R')
        MARKER_1469.relative_to = relative_to
        MARKER_1469.marker_name = target_path('.template_6_force.mlg_dragbrace_R.MARKER_1469')
        _template_6_force_ground_hpl_db_top1_2 = get_object('.template_6_force.ground.hpl_db_top1_2')
        MARKER_1469.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_db_top1_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1469.location, MARKER_1469.orientation)
        MARKER_1469.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_dragbrace_R.MARKER_1469', exc)

    try:
        MARKER_1027 = get_object('.template_6_force.mlg_suo_yaobi_L.MARKER_1027')
        relative_to = get_object('.template_6_force.mlg_suo_yaobi_L')
        MARKER_1027.relative_to = relative_to
        MARKER_1027.marker_name = target_path('.template_6_force.mlg_suo_yaobi_L.MARKER_1027')
        _template_6_force_ground_POINT_4832 = get_object('.template_6_force.ground.POINT_4832')
        MARKER_1027.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_4832))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1027.location, MARKER_1027.orientation)
        MARKER_1027.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_yaobi_L.MARKER_1027', exc)

    try:
        MARKER_1030 = get_object('.template_6_force.mlg_suo_yaobi_L.MARKER_1030')
        relative_to = get_object('.template_6_force.mlg_suo_yaobi_L')
        MARKER_1030.relative_to = relative_to
        MARKER_1030.marker_name = target_path('.template_6_force.mlg_suo_yaobi_L.MARKER_1030')
        _template_6_force_ground_POINT_4832 = get_object('.template_6_force.ground.POINT_4832')
        MARKER_1030.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_4832))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1030.location, MARKER_1030.orientation)
        MARKER_1030.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_yaobi_L.MARKER_1030', exc)

    try:
        MARKER_1048 = get_object('.template_6_force.mlg_suo_yaobi_L.MARKER_1048')
        relative_to = get_object('.template_6_force.mlg_suo_yaobi_L')
        MARKER_1048.relative_to = relative_to
        MARKER_1048.marker_name = target_path('.template_6_force.mlg_suo_yaobi_L.MARKER_1048')
        _template_6_force_ground_POINT_4832 = get_object('.template_6_force.ground.POINT_4832')
        MARKER_1048.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_4832))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1048.location, MARKER_1048.orientation)
        MARKER_1048.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_yaobi_L.MARKER_1048', exc)

    try:
        CYLINDER_499 = get_object('.template_6_force.mlg_suo_rod_L.CYLINDER_499')
        CYLINDER_499.cylinder_name = target_path('.template_6_force.mlg_suo_rod_L.CYLINDER_499')
        CYLINDER_499.radius = 1.8


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_suo_rod_L.CYLINDER_499', exc)

    try:
        MARKER_1105 = get_object('.template_6_force.mlg_suo_base_L.MARKER_1105')
        relative_to = get_object('.template_6_force.mlg_suo_base_L')
        MARKER_1105.relative_to = relative_to
        MARKER_1105.marker_name = target_path('.template_6_force.mlg_suo_base_L.MARKER_1105')
        _template_6_force_ground_POINT_4832 = get_object('.template_6_force.ground.POINT_4832')
        MARKER_1105.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_4832))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1105.location, MARKER_1105.orientation)
        MARKER_1105.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_base_L.MARKER_1105', exc)

    try:
        MARKER_1113 = get_object('.template_6_force.mlg_suo_base_L.MARKER_1113')
        relative_to = get_object('.template_6_force.mlg_suo_base_L')
        MARKER_1113.relative_to = relative_to
        MARKER_1113.marker_name = target_path('.template_6_force.mlg_suo_base_L.MARKER_1113')
        _template_6_force_mlg_suo_suogou_L_PT200 = get_object('.template_6_force.mlg_suo_suogou_L.PT200')
        MARKER_1113.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mlg_suo_suogou_L_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1113.location, MARKER_1113.orientation)
        MARKER_1113.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_base_L.MARKER_1113', exc)

    try:
        MARKER_1484 = get_object('.template_6_force.mlg_dragbrace_L.MARKER_1484')
        relative_to = get_object('.template_6_force.mlg_dragbrace_L')
        MARKER_1484.relative_to = relative_to
        MARKER_1484.marker_name = target_path('.template_6_force.mlg_dragbrace_L.MARKER_1484')
        _template_6_force_ground_hpl_db_top = get_object('.template_6_force.ground.hpl_db_top')
        MARKER_1484.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_db_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1484.location, MARKER_1484.orientation)
        MARKER_1484.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_dragbrace_L.MARKER_1484', exc)

    try:
        MARKER_1145 = get_object('.template_6_force.mlg_dragbrace_L.MARKER_1145')
        relative_to = get_object('.template_6_force.mlg_dragbrace_L')
        MARKER_1145.relative_to = relative_to
        MARKER_1145.marker_name = target_path('.template_6_force.mlg_dragbrace_L.MARKER_1145')
        _template_6_force_ground_hpl_db_top = get_object('.template_6_force.ground.hpl_db_top')
        MARKER_1145.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_db_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1145.location, MARKER_1145.orientation)
        MARKER_1145.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_dragbrace_L.MARKER_1145', exc)

    try:
        MARKER_1336 = get_object('.template_6_force.mlg_suo_liangan_R.MARKER_1336')
        relative_to = get_object('.template_6_force.mlg_suo_liangan_R')
        MARKER_1336.relative_to = relative_to
        MARKER_1336.marker_name = target_path('.template_6_force.mlg_suo_liangan_R.MARKER_1336')
        _template_6_force_ground_mlg_suo_spring_lg11 = get_object('.template_6_force.ground.mlg_suo_spring_lg11')
        MARKER_1336.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_mlg_suo_spring_lg11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1336.location, MARKER_1336.orientation)
        MARKER_1336.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_liangan_R.MARKER_1336', exc)

    try:
        MARKER_1338 = get_object('.template_6_force.mlg_suo_liangan_R.MARKER_1338')
        relative_to = get_object('.template_6_force.mlg_suo_liangan_R')
        MARKER_1338.relative_to = relative_to
        MARKER_1338.marker_name = target_path('.template_6_force.mlg_suo_liangan_R.MARKER_1338')
        _template_6_force_ground_mlg_suo_spring_lg21 = get_object('.template_6_force.ground.mlg_suo_spring_lg21')
        MARKER_1338.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_mlg_suo_spring_lg21))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1338.location, MARKER_1338.orientation)
        MARKER_1338.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_liangan_R.MARKER_1338', exc)

    try:
        MARKER_998 = get_object('.template_6_force.mlg_suo_liangan_R.MARKER_998')
        relative_to = get_object('.template_6_force.mlg_suo_liangan_R')
        MARKER_998.relative_to = relative_to
        MARKER_998.marker_name = target_path('.template_6_force.mlg_suo_liangan_R.MARKER_998')
        _template_6_force_ground_POINT_6361 = get_object('.template_6_force.ground.POINT_6361')
        MARKER_998.location = (VecUtils.LOC_RELATIVE_TO([-4.3751313683e-07, -1.0769163339e-11, 0.0], _template_6_force_ground_POINT_6361))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_998.location, MARKER_998.orientation)
        MARKER_998.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_liangan_R.MARKER_998', exc)

    try:
        MARKER_1027 = get_object('.template_6_force.mlg_suo_yaobi_R.MARKER_1027')
        relative_to = get_object('.template_6_force.mlg_suo_yaobi_R')
        MARKER_1027.relative_to = relative_to
        MARKER_1027.marker_name = target_path('.template_6_force.mlg_suo_yaobi_R.MARKER_1027')
        _template_6_force_ground_POINT_4831 = get_object('.template_6_force.ground.POINT_4831')
        MARKER_1027.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_4831))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1027.location, MARKER_1027.orientation)
        MARKER_1027.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_yaobi_R.MARKER_1027', exc)

    try:
        MARKER_1030 = get_object('.template_6_force.mlg_suo_yaobi_R.MARKER_1030')
        relative_to = get_object('.template_6_force.mlg_suo_yaobi_R')
        MARKER_1030.relative_to = relative_to
        MARKER_1030.marker_name = target_path('.template_6_force.mlg_suo_yaobi_R.MARKER_1030')
        _template_6_force_ground_POINT_4831 = get_object('.template_6_force.ground.POINT_4831')
        MARKER_1030.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_4831))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1030.location, MARKER_1030.orientation)
        MARKER_1030.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_yaobi_R.MARKER_1030', exc)

    try:
        MARKER_1048 = get_object('.template_6_force.mlg_suo_yaobi_R.MARKER_1048')
        relative_to = get_object('.template_6_force.mlg_suo_yaobi_R')
        MARKER_1048.relative_to = relative_to
        MARKER_1048.marker_name = target_path('.template_6_force.mlg_suo_yaobi_R.MARKER_1048')
        _template_6_force_ground_POINT_4831 = get_object('.template_6_force.ground.POINT_4831')
        MARKER_1048.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_4831))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1048.location, MARKER_1048.orientation)
        MARKER_1048.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_yaobi_R.MARKER_1048', exc)

    try:
        CYLINDER_499 = get_object('.template_6_force.mlg_suo_rod_R.CYLINDER_499')
        CYLINDER_499.cylinder_name = target_path('.template_6_force.mlg_suo_rod_R.CYLINDER_499')
        CYLINDER_499.radius = 1.8


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_suo_rod_R.CYLINDER_499', exc)

    try:
        MARKER_1105 = get_object('.template_6_force.mlg_suo_base_R.MARKER_1105')
        relative_to = get_object('.template_6_force.mlg_suo_base_R')
        MARKER_1105.relative_to = relative_to
        MARKER_1105.marker_name = target_path('.template_6_force.mlg_suo_base_R.MARKER_1105')
        _template_6_force_ground_POINT_4831 = get_object('.template_6_force.ground.POINT_4831')
        MARKER_1105.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_POINT_4831))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1105.location, MARKER_1105.orientation)
        MARKER_1105.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_base_R.MARKER_1105', exc)

    try:
        MARKER_1113 = get_object('.template_6_force.mlg_suo_base_R.MARKER_1113')
        relative_to = get_object('.template_6_force.mlg_suo_base_R')
        MARKER_1113.relative_to = relative_to
        MARKER_1113.marker_name = target_path('.template_6_force.mlg_suo_base_R.MARKER_1113')
        _template_6_force_mlg_suo_suogou_R_PT200 = get_object('.template_6_force.mlg_suo_suogou_R.PT200')
        MARKER_1113.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mlg_suo_suogou_R_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1113.location, MARKER_1113.orientation)
        MARKER_1113.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_base_R.MARKER_1113', exc)

    try:
        MARKER_1314 = get_object('.template_6_force.mlg_struct_R.MARKER_1314')
        relative_to = get_object('.template_6_force.mlg_struct_R')
        MARKER_1314.relative_to = relative_to
        MARKER_1314.marker_name = target_path('.template_6_force.mlg_struct_R.MARKER_1314')
        _template_6_force_ground_hpl_uc_top1 = get_object('.template_6_force.ground.hpl_uc_top1')
        MARKER_1314.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_uc_top1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1314.location, MARKER_1314.orientation)
        MARKER_1314.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_R.MARKER_1314', exc)

    try:
        MARKER_554 = get_object('.template_6_force.mlg_struct_R.MARKER_554')
        relative_to = get_object('.template_6_force.mlg_struct_R')
        MARKER_554.relative_to = relative_to
        MARKER_554.marker_name = target_path('.template_6_force.mlg_struct_R.MARKER_554')
        _template_6_force_ground_hpl_lc_top1 = get_object('.template_6_force.ground.hpl_lc_top1')
        MARKER_554.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_lc_top1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_554.location, MARKER_554.orientation)
        MARKER_554.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_R.MARKER_554', exc)

    try:
        MARKER_555 = get_object('.template_6_force.mlg_struct_R.MARKER_555')
        relative_to = get_object('.template_6_force.mlg_struct_R')
        MARKER_555.relative_to = relative_to
        MARKER_555.marker_name = target_path('.template_6_force.mlg_struct_R.MARKER_555')
        _template_6_force_ground_hpl_tire_axle1 = get_object('.template_6_force.ground.hpl_tire_axle1')
        MARKER_555.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_tire_axle1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_555.location, MARKER_555.orientation)
        MARKER_555.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_R.MARKER_555', exc)

    try:
        MARKER_556 = get_object('.template_6_force.mlg_struct_R.MARKER_556')
        relative_to = get_object('.template_6_force.mlg_struct_R')
        MARKER_556.relative_to = relative_to
        MARKER_556.marker_name = target_path('.template_6_force.mlg_struct_R.MARKER_556')
        _template_6_force_ground_hpl_uc_top1 = get_object('.template_6_force.ground.hpl_uc_top1')
        MARKER_556.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_uc_top1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_556.location, MARKER_556.orientation)
        MARKER_556.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_R.MARKER_556', exc)

    try:
        MARKER_568 = get_object('.template_6_force.mlg_struct_R.MARKER_568')
        relative_to = get_object('.template_6_force.mlg_struct_R')
        MARKER_568.relative_to = relative_to
        MARKER_568.marker_name = target_path('.template_6_force.mlg_struct_R.MARKER_568')
        _template_6_force_ground_hpl_uc_top1 = get_object('.template_6_force.ground.hpl_uc_top1')
        MARKER_568.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_uc_top1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_568.location, MARKER_568.orientation)
        MARKER_568.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_R.MARKER_568', exc)

    try:
        CYLINDER_308 = get_object('.template_6_force.mlg_struct_R.CYLINDER_308')
        CYLINDER_308.cylinder_name = target_path('.template_6_force.mlg_struct_R.CYLINDER_308')
        CYLINDER_308.length = 750.0


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_struct_R.CYLINDER_308', exc)

    try:
        CYLINDER_309 = get_object('.template_6_force.mlg_struct_R.CYLINDER_309')
        CYLINDER_309.cylinder_name = target_path('.template_6_force.mlg_struct_R.CYLINDER_309')
        CYLINDER_309.length = 390.0


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_struct_R.CYLINDER_309', exc)

    try:
        CYLINDER_324 = get_object('.template_6_force.mlg_struct_R.CYLINDER_324')
        CYLINDER_324.cylinder_name = target_path('.template_6_force.mlg_struct_R.CYLINDER_324')
        CYLINDER_324.length = 120.0


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_struct_R.CYLINDER_324', exc)

    try:
        MARKER_559 = get_object('.template_6_force.mlg_rod_R.MARKER_559')
        relative_to = get_object('.template_6_force.mlg_rod_R')
        MARKER_559.relative_to = relative_to
        MARKER_559.marker_name = target_path('.template_6_force.mlg_rod_R.MARKER_559')
        _template_6_force_ground_hpr_rod_bot = get_object('.template_6_force.ground.hpr_rod_bot')
        MARKER_559.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_rod_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_559.location, MARKER_559.orientation)
        MARKER_559.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_rod_R.MARKER_559', exc)

    try:
        MARKER_564 = get_object('.template_6_force.mlg_rod_R.MARKER_564')
        relative_to = get_object('.template_6_force.mlg_rod_R')
        MARKER_564.relative_to = relative_to
        MARKER_564.marker_name = target_path('.template_6_force.mlg_rod_R.MARKER_564')
        _template_6_force_ground_hpr_actuator_bot = get_object('.template_6_force.ground.hpr_actuator_bot')
        MARKER_564.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_actuator_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_564.location, MARKER_564.orientation)
        MARKER_564.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_rod_R.MARKER_564', exc)

    try:
        MARKER_565 = get_object('.template_6_force.mlg_rod_R.MARKER_565')
        relative_to = get_object('.template_6_force.mlg_rod_R')
        MARKER_565.relative_to = relative_to
        MARKER_565.marker_name = target_path('.template_6_force.mlg_rod_R.MARKER_565')
        _template_6_force_ground_hpr_rod_bot = get_object('.template_6_force.ground.hpr_rod_bot')
        MARKER_565.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_rod_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_565.location, MARKER_565.orientation)
        MARKER_565.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_rod_R.MARKER_565', exc)

    try:
        MARKER_593 = get_object('.template_6_force.mlg_rod_R.MARKER_593')
        relative_to = get_object('.template_6_force.mlg_rod_R')
        MARKER_593.relative_to = relative_to
        MARKER_593.marker_name = target_path('.template_6_force.mlg_rod_R.MARKER_593')
        _template_6_force_ground_hpr_rod_bot = get_object('.template_6_force.ground.hpr_rod_bot')
        MARKER_593.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_rod_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_593.location, MARKER_593.orientation)
        MARKER_593.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_rod_R.MARKER_593', exc)

    try:
        MARKER_560 = get_object('.template_6_force.mlg_actuator_R.MARKER_560')
        relative_to = get_object('.template_6_force.mlg_actuator_R')
        MARKER_560.relative_to = relative_to
        MARKER_560.marker_name = target_path('.template_6_force.mlg_actuator_R.MARKER_560')
        _template_6_force_ground_hpr_actuator_bot = get_object('.template_6_force.ground.hpr_actuator_bot')
        MARKER_560.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_actuator_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_560.location, MARKER_560.orientation)
        MARKER_560.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_actuator_R.MARKER_560', exc)

    try:
        MARKER_563 = get_object('.template_6_force.mlg_actuator_R.MARKER_563')
        relative_to = get_object('.template_6_force.mlg_actuator_R')
        MARKER_563.relative_to = relative_to
        MARKER_563.marker_name = target_path('.template_6_force.mlg_actuator_R.MARKER_563')
        _template_6_force_ground_hpr_actuator_bot = get_object('.template_6_force.ground.hpr_actuator_bot')
        MARKER_563.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_actuator_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_563.location, MARKER_563.orientation)
        MARKER_563.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_actuator_R.MARKER_563', exc)

    try:
        MARKER_592 = get_object('.template_6_force.mlg_actuator_R.MARKER_592')
        relative_to = get_object('.template_6_force.mlg_actuator_R')
        MARKER_592.relative_to = relative_to
        MARKER_592.marker_name = target_path('.template_6_force.mlg_actuator_R.MARKER_592')
        _template_6_force_ground_hpr_actuator_bot = get_object('.template_6_force.ground.hpr_actuator_bot')
        MARKER_592.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_actuator_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_592.location, MARKER_592.orientation)
        MARKER_592.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_actuator_R.MARKER_592', exc)

    try:
        MARKER_1557 = get_object('.template_6_force.mlg_actuator_R.MARKER_1557')
        relative_to = get_object('.template_6_force.mlg_actuator_R')
        MARKER_1557.relative_to = relative_to
        MARKER_1557.marker_name = target_path('.template_6_force.mlg_actuator_R.MARKER_1557')
        _template_6_force_ground_hpr_rod_topr = get_object('.template_6_force.ground.hpr_rod_topr')
        MARKER_1557.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpr_rod_topr))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1557.location, MARKER_1557.orientation)
        MARKER_1557.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_actuator_R.MARKER_1557', exc)

    try:
        CYLINDER_320 = get_object('.template_6_force.mlg_actuator_R.CYLINDER_320')
        CYLINDER_320.cylinder_name = target_path('.template_6_force.mlg_actuator_R.CYLINDER_320')
        _template_6_force_ground_hpr_actuator_bot = get_object('.template_6_force.ground.hpr_actuator_bot').location
        _template_6_force_ground_hpr_actuator_top = get_object('.template_6_force.ground.hpr_actuator_top').location
        CYLINDER_320.length = (VecUtils.DM(_template_6_force_ground_hpr_actuator_bot, _template_6_force_ground_hpr_actuator_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_actuator_R.CYLINDER_320', exc)

    try:
        MARKER_995 = get_object('.template_6_force.mlg_suo_suogou_R.MARKER_995')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_R')
        MARKER_995.relative_to = relative_to
        MARKER_995.marker_name = target_path('.template_6_force.mlg_suo_suogou_R.MARKER_995')
        _template_6_force_mlg_suo_suogou_R_PT200 = get_object('.template_6_force.mlg_suo_suogou_R.PT200')
        MARKER_995.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mlg_suo_suogou_R_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_995.location, MARKER_995.orientation)
        MARKER_995.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_R.MARKER_995', exc)

    try:
        MARKER_1334 = get_object('.template_6_force.mlg_suo_suogou_R.MARKER_1334')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_R')
        MARKER_1334.relative_to = relative_to
        MARKER_1334.marker_name = target_path('.template_6_force.mlg_suo_suogou_R.MARKER_1334')
        _template_6_force_mlg_suo_suogou_R_PT200 = get_object('.template_6_force.mlg_suo_suogou_R.PT200')
        MARKER_1334.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mlg_suo_suogou_R_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1334.location, MARKER_1334.orientation)
        MARKER_1334.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_R.MARKER_1334', exc)

    try:
        MARKER_1337 = get_object('.template_6_force.mlg_suo_suogou_R.MARKER_1337')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_R')
        MARKER_1337.relative_to = relative_to
        MARKER_1337.marker_name = target_path('.template_6_force.mlg_suo_suogou_R.MARKER_1337')
        _template_6_force_ground_mlg_suo_spring_sg11 = get_object('.template_6_force.ground.mlg_suo_spring_sg11')
        MARKER_1337.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_mlg_suo_spring_sg11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1337.location, MARKER_1337.orientation)
        MARKER_1337.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_R.MARKER_1337', exc)

    try:
        MARKER_1339 = get_object('.template_6_force.mlg_suo_suogou_R.MARKER_1339')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_R')
        MARKER_1339.relative_to = relative_to
        MARKER_1339.marker_name = target_path('.template_6_force.mlg_suo_suogou_R.MARKER_1339')
        _template_6_force_ground_mlg_suo_spring_sg21 = get_object('.template_6_force.ground.mlg_suo_spring_sg21')
        MARKER_1339.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_mlg_suo_spring_sg21))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1339.location, MARKER_1339.orientation)
        MARKER_1339.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_R.MARKER_1339', exc)

    try:
        MARKER_1135 = get_object('.template_6_force.mlg_suo_suogou_R.MARKER_1135')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_R')
        MARKER_1135.relative_to = relative_to
        MARKER_1135.marker_name = target_path('.template_6_force.mlg_suo_suogou_R.MARKER_1135')
        _template_6_force_mlg_suo_suogou_R_PT200 = get_object('.template_6_force.mlg_suo_suogou_R.PT200')
        MARKER_1135.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mlg_suo_suogou_R_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1135.location, MARKER_1135.orientation)
        MARKER_1135.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_R.MARKER_1135', exc)

    try:
        MARKER_1314 = get_object('.template_6_force.mlg_struct_L.MARKER_1314')
        relative_to = get_object('.template_6_force.mlg_struct_L')
        MARKER_1314.relative_to = relative_to
        MARKER_1314.marker_name = target_path('.template_6_force.mlg_struct_L.MARKER_1314')
        _template_6_force_ground_hpl_uc_top = get_object('.template_6_force.ground.hpl_uc_top')
        MARKER_1314.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1314.location, MARKER_1314.orientation)
        MARKER_1314.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_L.MARKER_1314', exc)

    try:
        MARKER_554 = get_object('.template_6_force.mlg_struct_L.MARKER_554')
        relative_to = get_object('.template_6_force.mlg_struct_L')
        MARKER_554.relative_to = relative_to
        MARKER_554.marker_name = target_path('.template_6_force.mlg_struct_L.MARKER_554')
        _template_6_force_ground_hpl_lc_top = get_object('.template_6_force.ground.hpl_lc_top')
        MARKER_554.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_554.location, MARKER_554.orientation)
        MARKER_554.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_L.MARKER_554', exc)

    try:
        MARKER_555 = get_object('.template_6_force.mlg_struct_L.MARKER_555')
        relative_to = get_object('.template_6_force.mlg_struct_L')
        MARKER_555.relative_to = relative_to
        MARKER_555.marker_name = target_path('.template_6_force.mlg_struct_L.MARKER_555')
        _template_6_force_ground_hpl_tire_axle = get_object('.template_6_force.ground.hpl_tire_axle')
        MARKER_555.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_tire_axle))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_555.location, MARKER_555.orientation)
        MARKER_555.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_L.MARKER_555', exc)

    try:
        MARKER_556 = get_object('.template_6_force.mlg_struct_L.MARKER_556')
        relative_to = get_object('.template_6_force.mlg_struct_L')
        MARKER_556.relative_to = relative_to
        MARKER_556.marker_name = target_path('.template_6_force.mlg_struct_L.MARKER_556')
        _template_6_force_ground_hpl_uc_top = get_object('.template_6_force.ground.hpl_uc_top')
        MARKER_556.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_556.location, MARKER_556.orientation)
        MARKER_556.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_L.MARKER_556', exc)

    try:
        MARKER_566 = get_object('.template_6_force.mlg_struct_L.MARKER_566')
        relative_to = get_object('.template_6_force.mlg_struct_L')
        MARKER_566.relative_to = relative_to
        MARKER_566.marker_name = target_path('.template_6_force.mlg_struct_L.MARKER_566')
        _template_6_force_ground_hpl_rod_bot = get_object('.template_6_force.ground.hpl_rod_bot')
        MARKER_566.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_rod_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_566.location, MARKER_566.orientation)
        MARKER_566.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_L.MARKER_566', exc)

    try:
        MARKER_568 = get_object('.template_6_force.mlg_struct_L.MARKER_568')
        relative_to = get_object('.template_6_force.mlg_struct_L')
        MARKER_568.relative_to = relative_to
        MARKER_568.marker_name = target_path('.template_6_force.mlg_struct_L.MARKER_568')
        _template_6_force_ground_hpl_uc_top = get_object('.template_6_force.ground.hpl_uc_top')
        MARKER_568.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_568.location, MARKER_568.orientation)
        MARKER_568.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_struct_L.MARKER_568', exc)

    try:
        CYLINDER_308 = get_object('.template_6_force.mlg_struct_L.CYLINDER_308')
        CYLINDER_308.cylinder_name = target_path('.template_6_force.mlg_struct_L.CYLINDER_308')
        CYLINDER_308.length = 750.0


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_struct_L.CYLINDER_308', exc)

    try:
        CYLINDER_309 = get_object('.template_6_force.mlg_struct_L.CYLINDER_309')
        CYLINDER_309.cylinder_name = target_path('.template_6_force.mlg_struct_L.CYLINDER_309')
        CYLINDER_309.length = 390.0


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_struct_L.CYLINDER_309', exc)

    try:
        CYLINDER_324 = get_object('.template_6_force.mlg_struct_L.CYLINDER_324')
        CYLINDER_324.cylinder_name = target_path('.template_6_force.mlg_struct_L.CYLINDER_324')
        CYLINDER_324.length = 120.0


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_struct_L.CYLINDER_324', exc)

    try:
        MARKER_559 = get_object('.template_6_force.mlg_rod_L.MARKER_559')
        relative_to = get_object('.template_6_force.mlg_rod_L')
        MARKER_559.relative_to = relative_to
        MARKER_559.marker_name = target_path('.template_6_force.mlg_rod_L.MARKER_559')
        _template_6_force_ground_hpl_rod_bot = get_object('.template_6_force.ground.hpl_rod_bot')
        MARKER_559.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_rod_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_559.location, MARKER_559.orientation)
        MARKER_559.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_rod_L.MARKER_559', exc)

    try:
        MARKER_564 = get_object('.template_6_force.mlg_rod_L.MARKER_564')
        relative_to = get_object('.template_6_force.mlg_rod_L')
        MARKER_564.relative_to = relative_to
        MARKER_564.marker_name = target_path('.template_6_force.mlg_rod_L.MARKER_564')
        _template_6_force_ground_hpl_actuator_bot = get_object('.template_6_force.ground.hpl_actuator_bot')
        MARKER_564.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_actuator_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_564.location, MARKER_564.orientation)
        MARKER_564.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_rod_L.MARKER_564', exc)

    try:
        MARKER_565 = get_object('.template_6_force.mlg_rod_L.MARKER_565')
        relative_to = get_object('.template_6_force.mlg_rod_L')
        MARKER_565.relative_to = relative_to
        MARKER_565.marker_name = target_path('.template_6_force.mlg_rod_L.MARKER_565')
        _template_6_force_ground_hpl_rod_bot = get_object('.template_6_force.ground.hpl_rod_bot')
        MARKER_565.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_rod_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_565.location, MARKER_565.orientation)
        MARKER_565.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_rod_L.MARKER_565', exc)

    try:
        MARKER_593 = get_object('.template_6_force.mlg_rod_L.MARKER_593')
        relative_to = get_object('.template_6_force.mlg_rod_L')
        MARKER_593.relative_to = relative_to
        MARKER_593.marker_name = target_path('.template_6_force.mlg_rod_L.MARKER_593')
        _template_6_force_ground_hpl_rod_bot = get_object('.template_6_force.ground.hpl_rod_bot')
        MARKER_593.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_rod_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_593.location, MARKER_593.orientation)
        MARKER_593.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_rod_L.MARKER_593', exc)

    try:
        MARKER_682 = get_object('.template_6_force.mlg_rod_L.MARKER_682')
        relative_to = get_object('.template_6_force.mlg_rod_L')
        MARKER_682.relative_to = relative_to
        MARKER_682.marker_name = target_path('.template_6_force.mlg_rod_L.MARKER_682')
        _template_6_force_ground_hpl_rod_bot = get_object('.template_6_force.ground.hpl_rod_bot')
        MARKER_682.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_rod_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_682.location, MARKER_682.orientation)
        MARKER_682.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_rod_L.MARKER_682', exc)

    try:
        MARKER_560 = get_object('.template_6_force.mlg_actuatorL.MARKER_560')
        relative_to = get_object('.template_6_force.mlg_actuatorL')
        MARKER_560.relative_to = relative_to
        MARKER_560.marker_name = target_path('.template_6_force.mlg_actuatorL.MARKER_560')
        _template_6_force_ground_hpl_actuator_bot = get_object('.template_6_force.ground.hpl_actuator_bot')
        MARKER_560.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_actuator_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_560.location, MARKER_560.orientation)
        MARKER_560.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_actuatorL.MARKER_560', exc)

    try:
        MARKER_578 = get_object('.template_6_force.mlg_actuatorL.MARKER_578')
        relative_to = get_object('.template_6_force.mlg_actuatorL')
        MARKER_578.relative_to = relative_to
        MARKER_578.marker_name = target_path('.template_6_force.mlg_actuatorL.MARKER_578')
        _template_6_force_ground_hpl_actuator_top = get_object('.template_6_force.ground.hpl_actuator_top')
        MARKER_578.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_actuator_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_578.location, MARKER_578.orientation)
        MARKER_578.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_actuatorL.MARKER_578', exc)

    try:
        MARKER_563 = get_object('.template_6_force.mlg_actuatorL.MARKER_563')
        relative_to = get_object('.template_6_force.mlg_actuatorL')
        MARKER_563.relative_to = relative_to
        MARKER_563.marker_name = target_path('.template_6_force.mlg_actuatorL.MARKER_563')
        _template_6_force_ground_hpl_actuator_bot = get_object('.template_6_force.ground.hpl_actuator_bot')
        MARKER_563.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_actuator_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_563.location, MARKER_563.orientation)
        MARKER_563.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_actuatorL.MARKER_563', exc)

    try:
        MARKER_592 = get_object('.template_6_force.mlg_actuatorL.MARKER_592')
        relative_to = get_object('.template_6_force.mlg_actuatorL')
        MARKER_592.relative_to = relative_to
        MARKER_592.marker_name = target_path('.template_6_force.mlg_actuatorL.MARKER_592')
        _template_6_force_ground_hpl_actuator_bot = get_object('.template_6_force.ground.hpl_actuator_bot')
        MARKER_592.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_actuator_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_592.location, MARKER_592.orientation)
        MARKER_592.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_actuatorL.MARKER_592', exc)

    try:
        MARKER_683 = get_object('.template_6_force.mlg_actuatorL.MARKER_683')
        relative_to = get_object('.template_6_force.mlg_actuatorL')
        MARKER_683.relative_to = relative_to
        MARKER_683.marker_name = target_path('.template_6_force.mlg_actuatorL.MARKER_683')
        _template_6_force_ground_hpl_actuator_bot = get_object('.template_6_force.ground.hpl_actuator_bot')
        MARKER_683.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hpl_actuator_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_683.location, MARKER_683.orientation)
        MARKER_683.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_actuatorL.MARKER_683', exc)

    try:
        CYLINDER_320 = get_object('.template_6_force.mlg_actuatorL.CYLINDER_320')
        CYLINDER_320.cylinder_name = target_path('.template_6_force.mlg_actuatorL.CYLINDER_320')
        _template_6_force_ground_hpl_actuator_bot = get_object('.template_6_force.ground.hpl_actuator_bot').location
        _template_6_force_ground_hpl_actuator_top = get_object('.template_6_force.ground.hpl_actuator_top').location
        CYLINDER_320.length = (VecUtils.DM(_template_6_force_ground_hpl_actuator_bot, _template_6_force_ground_hpl_actuator_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_6_force.mlg_actuatorL.CYLINDER_320', exc)

    try:
        MARKER_995 = get_object('.template_6_force.mlg_suo_suogou_L.MARKER_995')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_L')
        MARKER_995.relative_to = relative_to
        MARKER_995.marker_name = target_path('.template_6_force.mlg_suo_suogou_L.MARKER_995')
        _template_6_force_mlg_suo_suogou_L_PT200 = get_object('.template_6_force.mlg_suo_suogou_L.PT200')
        MARKER_995.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mlg_suo_suogou_L_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_995.location, MARKER_995.orientation)
        MARKER_995.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_L.MARKER_995', exc)

    try:
        MARKER_1334 = get_object('.template_6_force.mlg_suo_suogou_L.MARKER_1334')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_L')
        MARKER_1334.relative_to = relative_to
        MARKER_1334.marker_name = target_path('.template_6_force.mlg_suo_suogou_L.MARKER_1334')
        _template_6_force_mlg_suo_suogou_L_PT200 = get_object('.template_6_force.mlg_suo_suogou_L.PT200')
        MARKER_1334.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mlg_suo_suogou_L_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1334.location, MARKER_1334.orientation)
        MARKER_1334.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_L.MARKER_1334', exc)

    try:
        MARKER_1337 = get_object('.template_6_force.mlg_suo_suogou_L.MARKER_1337')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_L')
        MARKER_1337.relative_to = relative_to
        MARKER_1337.marker_name = target_path('.template_6_force.mlg_suo_suogou_L.MARKER_1337')
        _template_6_force_ground_mlg_suo_spring_sg1 = get_object('.template_6_force.ground.mlg_suo_spring_sg1')
        MARKER_1337.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_mlg_suo_spring_sg1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1337.location, MARKER_1337.orientation)
        MARKER_1337.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_L.MARKER_1337', exc)

    try:
        MARKER_1339 = get_object('.template_6_force.mlg_suo_suogou_L.MARKER_1339')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_L')
        MARKER_1339.relative_to = relative_to
        MARKER_1339.marker_name = target_path('.template_6_force.mlg_suo_suogou_L.MARKER_1339')
        _template_6_force_ground_mlg_suo_spring_sg2 = get_object('.template_6_force.ground.mlg_suo_spring_sg2')
        MARKER_1339.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_mlg_suo_spring_sg2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1339.location, MARKER_1339.orientation)
        MARKER_1339.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_L.MARKER_1339', exc)

    try:
        MARKER_1135 = get_object('.template_6_force.mlg_suo_suogou_L.MARKER_1135')
        relative_to = get_object('.template_6_force.mlg_suo_suogou_L')
        MARKER_1135.relative_to = relative_to
        MARKER_1135.marker_name = target_path('.template_6_force.mlg_suo_suogou_L.MARKER_1135')
        _template_6_force_mlg_suo_suogou_L_PT200 = get_object('.template_6_force.mlg_suo_suogou_L.PT200')
        MARKER_1135.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_mlg_suo_suogou_L_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1135.location, MARKER_1135.orientation)
        MARKER_1135.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.mlg_suo_suogou_L.MARKER_1135', exc)

    try:
        MARKER_995 = get_object('.template_6_force.nlg_suo_suogou.MARKER_995')
        relative_to = get_object('.template_6_force.nlg_suo_suogou')
        MARKER_995.relative_to = relative_to
        MARKER_995.marker_name = target_path('.template_6_force.nlg_suo_suogou.MARKER_995')
        _template_6_force_nlg_suo_suogou_PT200 = get_object('.template_6_force.nlg_suo_suogou.PT200')
        MARKER_995.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_suo_suogou_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_995.location, MARKER_995.orientation)
        MARKER_995.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_suogou.MARKER_995', exc)

    try:
        MARKER_1135 = get_object('.template_6_force.nlg_suo_suogou.MARKER_1135')
        relative_to = get_object('.template_6_force.nlg_suo_suogou')
        MARKER_1135.relative_to = relative_to
        MARKER_1135.marker_name = target_path('.template_6_force.nlg_suo_suogou.MARKER_1135')
        _template_6_force_nlg_suo_suogou_PT200 = get_object('.template_6_force.nlg_suo_suogou.PT200')
        MARKER_1135.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_suo_suogou_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1135.location, MARKER_1135.orientation)
        MARKER_1135.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_suogou.MARKER_1135', exc)

    try:
        MARKER_1069 = get_object('.template_6_force.nlg_suo_suogou.MARKER_1069')
        relative_to = get_object('.template_6_force.nlg_suo_suogou')
        MARKER_1069.relative_to = relative_to
        MARKER_1069.marker_name = target_path('.template_6_force.nlg_suo_suogou.MARKER_1069')
        _template_6_force_nlg_suo_suogou_PT200 = get_object('.template_6_force.nlg_suo_suogou.PT200')
        MARKER_1069.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_nlg_suo_suogou_PT200))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1069.location, MARKER_1069.orientation)
        MARKER_1069.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_suogou.MARKER_1069', exc)

    try:
        MARKER_1383 = get_object('.template_6_force.nlg_suo_suogou.MARKER_1383')
        relative_to = get_object('.template_6_force.nlg_suo_suogou')
        MARKER_1383.relative_to = relative_to
        MARKER_1383.marker_name = target_path('.template_6_force.nlg_suo_suogou.MARKER_1383')
        _template_6_force_ground_hps_spring_sg1 = get_object('.template_6_force.ground.hps_spring_sg1')
        MARKER_1383.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_spring_sg1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1383.location, MARKER_1383.orientation)
        MARKER_1383.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_suogou.MARKER_1383', exc)

    try:
        MARKER_1385 = get_object('.template_6_force.nlg_suo_suogou.MARKER_1385')
        relative_to = get_object('.template_6_force.nlg_suo_suogou')
        MARKER_1385.relative_to = relative_to
        MARKER_1385.marker_name = target_path('.template_6_force.nlg_suo_suogou.MARKER_1385')
        _template_6_force_ground_hps_spring_sg2 = get_object('.template_6_force.ground.hps_spring_sg2')
        MARKER_1385.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_6_force_ground_hps_spring_sg2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_1385.location, MARKER_1385.orientation)
        MARKER_1385.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_6_force.nlg_suo_suogou.MARKER_1385', exc)

    return {'updated': updated, 'warnings': warnings, 'errors': errors}

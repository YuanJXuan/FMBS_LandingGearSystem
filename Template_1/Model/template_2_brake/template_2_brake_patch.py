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

SOURCE_MODEL_NAME = 'template_2_brake'
ADM_UDE_KINDS = {'lumian_1': 'road', 'luntai': 'tire'}

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
        node = get_or_create('DataElementVariable', '.template_2_brake.MLG_Vw')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_brake.MLG_Vw')
        if hasattr(node, 'adams_id'):
            node.adams_id = 34
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_brake.MLG_Vw', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_2_brake.LMLG_S')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_brake.LMLG_S')
        if hasattr(node, 'adams_id'):
            node.adams_id = 30
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_brake.LMLG_S', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_2_brake.LMLG_V')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_brake.LMLG_V')
        if hasattr(node, 'adams_id'):
            node.adams_id = 31
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_brake.LMLG_V', exc)

    try:
        node = get_or_create('DataElementVariable', '.template_2_brake.MLG_slip_ratio')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_brake.MLG_slip_ratio')
        if hasattr(node, 'adams_id'):
            node.adams_id = 35
        if hasattr(node, 'initial_condition'):
            node.initial_condition = 0.0
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_brake.MLG_slip_ratio', exc)

    try:
        node = get_or_create('SimuScript', '.template_2_brake.Last_Sim')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_2_brake.Last_Sim')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=30.0 step_size=1.0E-02 model_name=.GCMB')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_2_brake.Last_Sim', exc)

    try:
        node = get_object('.template_2_brake.MLG_Vw')
        node.function = rewrite_expression('-.template_2_brake.MLG_w*0.457')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_brake.MLG_Vw', exc)

    try:
        node = get_object('.template_2_brake.LMLG_S')
        node.function = rewrite_expression('.template_2_brake.MLG_S0-DM(.template_2_brake.gel_upper_cylinder.MARKER_216,.template_2_brake.gel_lower_cylinder.MARKER_217)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_brake.LMLG_S', exc)

    try:
        node = get_object('.template_2_brake.LMLG_V')
        node.function = rewrite_expression('-1*VR(.template_2_brake.gel_upper_cylinder.MARKER_216,.template_2_brake.gel_lower_cylinder.MARKER_217)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_brake.LMLG_V', exc)

    try:
        node = get_object('.template_2_brake.MLG_slip_ratio')
        node.function = rewrite_expression('1-(VARVAL(.template_2_brake.MLG_Vw))/((.template_2_brake.js_sd)/1000)')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_brake.MLG_slip_ratio', exc)

    try:
        node = get_object('.template_2_brake.LMLG_AIR')
        node.function = rewrite_expression('3*.template_2_brake.MLG_A_LOW*(.template_2_brake.MLG_P_LOW*(.template_2_brake.MLG_V_LOW/(.template_2_brake.MLG_V_LOW-.template_2_brake.MLG_A_LOW*VARVAL(.template_2_brake.LMLG_S)))**1.1-.template_2_brake.Patm)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_brake.LMLG_AIR', exc)

    try:
        node = get_object('.template_2_brake.LMLG_OIL')
        node.function = rewrite_expression('IF(VARVAL(.template_2_brake.LMLG_V):0.003*-1*(VARVAL(.template_2_brake.LMLG_V)*0.5*(VARVAL(.template_2_brake.LMLG_V)-ABS(VARVAL(.template_2_brake.LMLG_V)))*((.template_2_brake.MLG_rho_Oil*.template_2_brake.MLG_A_MAIN_OIL**3/(2*.template_2_brake.MLG_RET_Cd**2*.template_2_brake.MLG_A_MAIN_NEG**2))+(.template_2_brake.MLG_rho_Oil*.template_2_brake.MLG_A_RET_OIL**3/(2*.template_2_brake.MLG_MAIN_Cd**2*.template_2_brake.MLG_A_RET_NEG**2)))),0,0.003*VARVAL(.template_2_brake.LMLG_V)*0.5*(VARVAL(.template_2_brake.LMLG_V)+ABS(VARVAL(.template_2_brake.LMLG_V)))*((.template_2_brake.MLG_rho_Oil*.template_2_brake.MLG_A_MAIN_OIL**3/(2*.template_2_brake.MLG_RET_Cd**2*.template_2_brake.MLG_A_MAIN_POS**2))+(.template_2_brake.MLG_rho_Oil*.template_2_brake.MLG_A_RET_OIL**3/(2*.template_2_brake.MLG_MAIN_Cd**2*.template_2_brake.MLG_A_RET_POS**2))))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_brake.LMLG_OIL', exc)

    try:
        node = get_object('.template_2_brake.LMLG_STOP')
        node.function = rewrite_expression('IF(.template_2_brake.MLG_S0-DM(.template_2_brake.gel_upper_cylinder.MARKER_216,.template_2_brake.gel_lower_cylinder.MARKER_217) :1.0E+09*(.template_2_brake.MLG_S0-DM(.template_2_brake.gel_upper_cylinder.MARKER_216,.template_2_brake.gel_lower_cylinder.MARKER_217)) , 0 , 0 )')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_brake.LMLG_STOP', exc)

    try:
        node = get_object('.template_2_brake.LMLG_Tb')
        node.function = rewrite_expression('if(vx(.template_2_brake.zhiliang.cm,.template_2_brake.ground.MARKER_226):if(time-6:0,0,.template_2_brake.MLG_Tb),0,0)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_brake.LMLG_Tb', exc)

    try:
        node = get_object('.template_2_brake.thrust')
        node.function = rewrite_expression('-30000*2/3.14*atan(.template_2_brake.MLG_Vx-.template_2_brake.js_sd)*(STEP (TIME,0,0,1.2,1)-STEP (TIME,4.8,0,5.0,1))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_brake.thrust', exc)

    try:
        cfl_spin_axis = get_object('.template_2_brake.ground.cfl_spin_axis')
        cfl_spin_axis.marker_name = target_path('.template_2_brake.ground.cfl_spin_axis')
        _template_2_brake_ground_cfl_spin_axis_1 = get_object('.template_2_brake.ground.cfl_spin_axis_1')
        cfl_spin_axis.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_cfl_spin_axis_1))
        _template_2_brake_ground_cfl_spin_axis_1 = get_object('.template_2_brake.ground.cfl_spin_axis_1')
        cfl_spin_axis.orientation = (VecUtils.ORI_RELATIVE_TO([180.0, 180.0, 180.0], _template_2_brake_ground_cfl_spin_axis_1))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.ground.cfl_spin_axis', exc)

    try:
        cfl_uc_top = get_object('.template_2_brake.ground.cfl_uc_top')
        cfl_uc_top.marker_name = target_path('.template_2_brake.ground.cfl_uc_top')
        _template_2_brake_ground_hpl_uc_top = get_object('.template_2_brake.ground.hpl_uc_top')
        cfl_uc_top.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_uc_top))
        _template_2_brake_ground_origo = get_object('.template_2_brake.ground.origo')
        cfl_uc_top.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.ground.cfl_uc_top', exc)

    try:
        cfl_collar_top = get_object('.template_2_brake.ground.cfl_collar_top')
        cfl_collar_top.marker_name = target_path('.template_2_brake.ground.cfl_collar_top')
        _template_2_brake_ground_hpl_uc_top = get_object('.template_2_brake.ground.hpl_uc_top').location
        _template_2_brake_ground_hpl_lc_bot = get_object('.template_2_brake.ground.hpl_lc_bot').location
        cfl_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_2_brake_ground_hpl_uc_top, _template_2_brake_ground_hpl_lc_bot, 0.59 * VecUtils.DM(_template_2_brake_ground_hpl_uc_top, _template_2_brake_ground_hpl_lc_bot)))
        _template_2_brake_ground_hpl_uc_top = get_object('.template_2_brake.ground.hpl_uc_top').location
        _template_2_brake_ground_hpl_lc_bot = get_object('.template_2_brake.ground.hpl_lc_bot').location
        cfl_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_uc_top, _template_2_brake_ground_hpl_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.ground.cfl_collar_top', exc)

    try:
        cfl_collar_bot = get_object('.template_2_brake.ground.cfl_collar_bot')
        cfl_collar_bot.marker_name = target_path('.template_2_brake.ground.cfl_collar_bot')
        _template_2_brake_ground_hpl_uc_top = get_object('.template_2_brake.ground.hpl_uc_top').location
        _template_2_brake_ground_hpl_lc_bot = get_object('.template_2_brake.ground.hpl_lc_bot').location
        cfl_collar_bot.location = (VecUtils.LOC_ALONG_LINE(_template_2_brake_ground_hpl_uc_top, _template_2_brake_ground_hpl_lc_bot, 0.7 * VecUtils.DM(_template_2_brake_ground_hpl_uc_top, _template_2_brake_ground_hpl_lc_bot)))
        _template_2_brake_ground_hpl_uc_top = get_object('.template_2_brake.ground.hpl_uc_top').location
        _template_2_brake_ground_hpl_lc_bot = get_object('.template_2_brake.ground.hpl_lc_bot').location
        cfl_collar_bot.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_uc_top, _template_2_brake_ground_hpl_lc_bot, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.ground.cfl_collar_bot', exc)

    try:
        cfl_plane_ref_2 = get_object('.template_2_brake.ground.cfl_plane_ref_2')
        cfl_plane_ref_2.marker_name = target_path('.template_2_brake.ground.cfl_plane_ref_2')
        _template_2_brake_ground_cfl_plane_ref = get_object('.template_2_brake.ground.cfl_plane_ref')
        cfl_plane_ref_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_cfl_plane_ref))
        _template_2_brake_ground_cfl_plane_ref = get_object('.template_2_brake.ground.cfl_plane_ref')
        cfl_plane_ref_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, -90.0, 0.0], _template_2_brake_ground_cfl_plane_ref))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.ground.cfl_plane_ref_2', exc)

    try:
        cfl_spin_axis_1 = get_object('.template_2_brake.ground.cfl_spin_axis_1')
        cfl_spin_axis_1.marker_name = target_path('.template_2_brake.ground.cfl_spin_axis_1')
        _template_2_brake_ground_hpl_wheel_center = get_object('.template_2_brake.ground.hpl_wheel_center')
        cfl_spin_axis_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_wheel_center))
        _template_2_brake_ground_hpl_wheel_center = get_object('.template_2_brake.ground.hpl_wheel_center').location
        _template_2_brake_ground_hpl_ob_axle = get_object('.template_2_brake.ground.hpl_ob_axle').location
        cfl_spin_axis_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_wheel_center, _template_2_brake_ground_hpl_ob_axle, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.ground.cfl_spin_axis_1', exc)

    try:
        cfl_ldb_geompt_1 = get_object('.template_2_brake.ground.cfl_ldb_geompt_1')
        cfl_ldb_geompt_1.marker_name = target_path('.template_2_brake.ground.cfl_ldb_geompt_1')
        _template_2_brake_ground_hpl_ldb_udb_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_udb_atch_1').location
        _template_2_brake_ground_hpl_ldb_collar_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_collar_atch_1').location
        cfl_ldb_geompt_1.location = (VecUtils.LOC_ALONG_LINE(_template_2_brake_ground_hpl_ldb_udb_atch_1, _template_2_brake_ground_hpl_ldb_collar_atch_1, 0.62 * VecUtils.DM(_template_2_brake_ground_hpl_ldb_udb_atch_1, _template_2_brake_ground_hpl_ldb_collar_atch_1)))
        _template_2_brake_ground_origo = get_object('.template_2_brake.ground.origo')
        cfl_ldb_geompt_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.ground.cfl_ldb_geompt_1', exc)

    try:
        cfl_ldb_geompt_2 = get_object('.template_2_brake.ground.cfl_ldb_geompt_2')
        cfl_ldb_geompt_2.marker_name = target_path('.template_2_brake.ground.cfl_ldb_geompt_2')
        _template_2_brake_ground_hpl_ldb_udb_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_udb_atch_1').location
        _template_2_brake_ground_hpl_ldb_collar_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_collar_atch_1').location
        cfl_ldb_geompt_2.location = (VecUtils.LOC_ALONG_LINE(_template_2_brake_ground_hpl_ldb_udb_atch_1, _template_2_brake_ground_hpl_ldb_collar_atch_1, 0.74 * VecUtils.DM(_template_2_brake_ground_hpl_ldb_udb_atch_1, _template_2_brake_ground_hpl_ldb_collar_atch_1)))
        _template_2_brake_ground_origo = get_object('.template_2_brake.ground.origo')
        cfl_ldb_geompt_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.ground.cfl_ldb_geompt_2', exc)

    try:
        MARKER_240 = get_object('.template_2_brake.ground.MARKER_240')
        MARKER_240.marker_name = target_path('.template_2_brake.ground.MARKER_240')
        _template_2_brake_ground_POINT_48 = get_object('.template_2_brake.ground.POINT_48')
        MARKER_240.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_POINT_48))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.ground.MARKER_240', exc)

    try:
        inertia_frame = get_object('.template_2_brake.gel_upper_cylinder.inertia_frame')
        relative_to = get_object('.template_2_brake.gel_upper_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_brake.gel_upper_cylinder.inertia_frame')
        _template_2_brake_gel_upper_cylinder_cm = get_object('.template_2_brake.gel_upper_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_cylinder_cm))
        _template_2_brake_gel_upper_cylinder = get_object('.template_2_brake.gel_upper_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_cylinder.inertia_frame', exc)

    try:
        gralin_12 = get_object('.template_2_brake.gel_upper_cylinder.gralin_12')
        relative_to = get_object('.template_2_brake.gel_upper_cylinder')
        gralin_12.relative_to = relative_to
        gralin_12.marker_name = target_path('.template_2_brake.gel_upper_cylinder.gralin_12')
        _template_2_brake_ground_cfl_uc_top = get_object('.template_2_brake.ground.cfl_uc_top')
        gralin_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_cfl_uc_top))
        _template_2_brake_ground_cfl_uc_top = get_object('.template_2_brake.ground.cfl_uc_top').location
        _template_2_brake_ground_hpl_uc_bot = get_object('.template_2_brake.ground.hpl_uc_bot').location
        gralin_12.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_cfl_uc_top, _template_2_brake_ground_hpl_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_12.location, gralin_12.orientation)
        gralin_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_cylinder.gralin_12', exc)

    try:
        uel_spring_j_1 = get_object('.template_2_brake.gel_upper_cylinder.uel_spring_j_1')
        relative_to = get_object('.template_2_brake.gel_upper_cylinder')
        uel_spring_j_1.relative_to = relative_to
        uel_spring_j_1.marker_name = target_path('.template_2_brake.gel_upper_cylinder.uel_spring_j_1')
        _template_2_brake_ground_cfl_uc_top = get_object('.template_2_brake.ground.cfl_uc_top')
        uel_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_cfl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_spring_j_1.location, uel_spring_j_1.orientation)
        uel_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_cylinder.uel_spring_j_1', exc)

    try:
        gralin_upper_cylinder = get_object('.template_2_brake.gel_upper_cylinder.gralin_upper_cylinder')
        gralin_upper_cylinder.cylinder_name = target_path('.template_2_brake.gel_upper_cylinder.gralin_upper_cylinder')
        _template_2_brake_ground_hpl_uc_top = get_object('.template_2_brake.ground.hpl_uc_top').location
        _template_2_brake_ground_hpl_uc_bot = get_object('.template_2_brake.ground.hpl_uc_bot').location
        gralin_upper_cylinder.length = (VecUtils.DM(_template_2_brake_ground_hpl_uc_top, _template_2_brake_ground_hpl_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_brake.gel_upper_cylinder.gralin_upper_cylinder', exc)

    try:
        MARKER_216 = get_object('.template_2_brake.gel_upper_cylinder.MARKER_216')
        relative_to = get_object('.template_2_brake.gel_upper_cylinder')
        MARKER_216.relative_to = relative_to
        MARKER_216.marker_name = target_path('.template_2_brake.gel_upper_cylinder.MARKER_216')
        _template_2_brake_ground_hpl_uc_top = get_object('.template_2_brake.ground.hpl_uc_top')
        MARKER_216.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_216.location, MARKER_216.orientation)
        MARKER_216.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_cylinder.MARKER_216', exc)

    try:
        MARKER_218 = get_object('.template_2_brake.gel_upper_cylinder.MARKER_218')
        relative_to = get_object('.template_2_brake.gel_upper_cylinder')
        MARKER_218.relative_to = relative_to
        MARKER_218.marker_name = target_path('.template_2_brake.gel_upper_cylinder.MARKER_218')
        _template_2_brake_ground_hpl_uc_top = get_object('.template_2_brake.ground.hpl_uc_top')
        MARKER_218.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_218.location, MARKER_218.orientation)
        MARKER_218.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_cylinder.MARKER_218', exc)

    try:
        MARKER_220 = get_object('.template_2_brake.gel_upper_cylinder.MARKER_220')
        relative_to = get_object('.template_2_brake.gel_upper_cylinder')
        MARKER_220.relative_to = relative_to
        MARKER_220.marker_name = target_path('.template_2_brake.gel_upper_cylinder.MARKER_220')
        _template_2_brake_ground_hpl_uc_top = get_object('.template_2_brake.ground.hpl_uc_top')
        MARKER_220.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_220.location, MARKER_220.orientation)
        MARKER_220.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_cylinder.MARKER_220', exc)

    try:
        MARKER_234 = get_object('.template_2_brake.gel_upper_cylinder.MARKER_234')
        relative_to = get_object('.template_2_brake.gel_upper_cylinder')
        MARKER_234.relative_to = relative_to
        MARKER_234.marker_name = target_path('.template_2_brake.gel_upper_cylinder.MARKER_234')
        _template_2_brake_ground_POINT_48 = get_object('.template_2_brake.ground.POINT_48')
        MARKER_234.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_POINT_48))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_234.location, MARKER_234.orientation)
        MARKER_234.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_cylinder.MARKER_234', exc)

    try:
        inertia_frame = get_object('.template_2_brake.gel_lower_cylinder.inertia_frame')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_brake.gel_lower_cylinder.inertia_frame')
        _template_2_brake_gel_lower_cylinder_cm = get_object('.template_2_brake.gel_lower_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_lower_cylinder_cm))
        _template_2_brake_gel_lower_cylinder = get_object('.template_2_brake.gel_lower_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_lower_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.inertia_frame', exc)

    try:
        gralin_14 = get_object('.template_2_brake.gel_lower_cylinder.gralin_14')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        gralin_14.relative_to = relative_to
        gralin_14.marker_name = target_path('.template_2_brake.gel_lower_cylinder.gralin_14')
        _template_2_brake_ground_hpl_lc_top = get_object('.template_2_brake.ground.hpl_lc_top')
        gralin_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_lc_top))
        _template_2_brake_ground_hpl_lc_top = get_object('.template_2_brake.ground.hpl_lc_top').location
        _template_2_brake_ground_hpl_lc_bot = get_object('.template_2_brake.ground.hpl_lc_bot').location
        gralin_14.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_lc_top, _template_2_brake_ground_hpl_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_14.location, gralin_14.orientation)
        gralin_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.gralin_14', exc)

    try:
        gralin_22 = get_object('.template_2_brake.gel_lower_cylinder.gralin_22')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        gralin_22.relative_to = relative_to
        gralin_22.marker_name = target_path('.template_2_brake.gel_lower_cylinder.gralin_22')
        _template_2_brake_ground_hpl_ib_axle = get_object('.template_2_brake.ground.hpl_ib_axle')
        gralin_22.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_ib_axle))
        _template_2_brake_ground_hpl_ib_axle = get_object('.template_2_brake.ground.hpl_ib_axle').location
        _template_2_brake_ground_hpl_ob_axle = get_object('.template_2_brake.ground.hpl_ob_axle').location
        gralin_22.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_ib_axle, _template_2_brake_ground_hpl_ob_axle, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_22.location, gralin_22.orientation)
        gralin_22.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_22.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.gralin_22', exc)

    try:
        jxl_joint_j_11 = get_object('.template_2_brake.gel_lower_cylinder.jxl_joint_j_11')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        jxl_joint_j_11.relative_to = relative_to
        jxl_joint_j_11.marker_name = target_path('.template_2_brake.gel_lower_cylinder.jxl_joint_j_11')
        _template_2_brake_ground_hpl_lta_lc_atch_1 = get_object('.template_2_brake.ground.hpl_lta_lc_atch_1')
        jxl_joint_j_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_lta_lc_atch_1))
        _template_2_brake_ground_hpl_lta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_lta_connect_atch_1').location
        _template_2_brake_ground_hpl_uta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_1').location
        jxl_joint_j_11.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_lta_connect_atch_1, _template_2_brake_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_11.location, jxl_joint_j_11.orientation)
        jxl_joint_j_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.jxl_joint_j_11', exc)

    try:
        jxl_joint_i_12 = get_object('.template_2_brake.gel_lower_cylinder.jxl_joint_i_12')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        jxl_joint_i_12.relative_to = relative_to
        jxl_joint_i_12.marker_name = target_path('.template_2_brake.gel_lower_cylinder.jxl_joint_i_12')
        _template_2_brake_gel_upper_cylinder_jxl_joint_j_12 = get_object('.template_2_brake.gel_upper_cylinder.jxl_joint_j_12')
        jxl_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_cylinder_jxl_joint_j_12))
        _template_2_brake_gel_upper_cylinder_jxl_joint_j_12 = get_object('.template_2_brake.gel_upper_cylinder.jxl_joint_j_12')
        jxl_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_cylinder_jxl_joint_j_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_12.location, jxl_joint_i_12.orientation)
        jxl_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.jxl_joint_i_12', exc)

    try:
        coomarker_1 = get_object('.template_2_brake.gel_lower_cylinder.coomarker_1')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        coomarker_1.relative_to = relative_to
        coomarker_1.marker_name = target_path('.template_2_brake.gel_lower_cylinder.coomarker_1')
        _template_2_brake_ground_cfl_spin_axis = get_object('.template_2_brake.ground.cfl_spin_axis')
        coomarker_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_cfl_spin_axis))
        _template_2_brake_ground_cfl_spin_axis = get_object('.template_2_brake.ground.cfl_spin_axis')
        coomarker_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_cfl_spin_axis))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_1.location, coomarker_1.orientation)
        coomarker_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.coomarker_1', exc)

    try:
        uel_spring_i_1 = get_object('.template_2_brake.gel_lower_cylinder.uel_spring_i_1')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        uel_spring_i_1.relative_to = relative_to
        uel_spring_i_1.marker_name = target_path('.template_2_brake.gel_lower_cylinder.uel_spring_i_1')
        _template_2_brake_ground_hpl_lc_top = get_object('.template_2_brake.ground.hpl_lc_top')
        uel_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_spring_i_1.location, uel_spring_i_1.orientation)
        uel_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.uel_spring_i_1', exc)

    try:
        uel_damper_i_1 = get_object('.template_2_brake.gel_lower_cylinder.uel_damper_i_1')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        uel_damper_i_1.relative_to = relative_to
        uel_damper_i_1.marker_name = target_path('.template_2_brake.gel_lower_cylinder.uel_damper_i_1')
        _template_2_brake_ground_hpl_lc_top = get_object('.template_2_brake.ground.hpl_lc_top')
        uel_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_damper_i_1.location, uel_damper_i_1.orientation)
        uel_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.uel_damper_i_1', exc)

    try:
        uel_stopper_i_1 = get_object('.template_2_brake.gel_lower_cylinder.uel_stopper_i_1')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        uel_stopper_i_1.relative_to = relative_to
        uel_stopper_i_1.marker_name = target_path('.template_2_brake.gel_lower_cylinder.uel_stopper_i_1')
        _template_2_brake_ground_hpl_lc_top = get_object('.template_2_brake.ground.hpl_lc_top')
        uel_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_stopper_i_1.location, uel_stopper_i_1.orientation)
        uel_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.uel_stopper_i_1', exc)

    try:
        gralin_lower_cylinder = get_object('.template_2_brake.gel_lower_cylinder.gralin_lower_cylinder')
        gralin_lower_cylinder.cylinder_name = target_path('.template_2_brake.gel_lower_cylinder.gralin_lower_cylinder')
        _template_2_brake_ground_hpl_lc_top = get_object('.template_2_brake.ground.hpl_lc_top').location
        _template_2_brake_ground_hpl_lc_bot = get_object('.template_2_brake.ground.hpl_lc_bot').location
        gralin_lower_cylinder.length = (VecUtils.DM(_template_2_brake_ground_hpl_lc_top, _template_2_brake_ground_hpl_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_brake.gel_lower_cylinder.gralin_lower_cylinder', exc)

    try:
        gralin_geom = get_object('.template_2_brake.gel_lower_cylinder.gralin_geom')
        gralin_geom.cylinder_name = target_path('.template_2_brake.gel_lower_cylinder.gralin_geom')
        _template_2_brake_ground_hpl_ib_axle = get_object('.template_2_brake.ground.hpl_ib_axle').location
        _template_2_brake_ground_hpl_ob_axle = get_object('.template_2_brake.ground.hpl_ob_axle').location
        gralin_geom.length = (VecUtils.DM(_template_2_brake_ground_hpl_ib_axle, _template_2_brake_ground_hpl_ob_axle))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_brake.gel_lower_cylinder.gralin_geom', exc)

    try:
        MARKER_203 = get_object('.template_2_brake.gel_lower_cylinder.MARKER_203')
        relative_to = get_object('.template_2_brake.gel_lower_cylinder')
        MARKER_203.relative_to = relative_to
        MARKER_203.marker_name = target_path('.template_2_brake.gel_lower_cylinder.MARKER_203')
        _template_2_brake_ground_hpl_wheel_center = get_object('.template_2_brake.ground.hpl_wheel_center')
        MARKER_203.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_203.location, MARKER_203.orientation)
        MARKER_203.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_cylinder.MARKER_203', exc)

    try:
        inertia_frame = get_object('.template_2_brake.gel_upper_dragbrace.inertia_frame')
        relative_to = get_object('.template_2_brake.gel_upper_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_brake.gel_upper_dragbrace.inertia_frame')
        _template_2_brake_gel_upper_dragbrace_cm = get_object('.template_2_brake.gel_upper_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_dragbrace_cm))
        _template_2_brake_gel_upper_dragbrace = get_object('.template_2_brake.gel_upper_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_dragbrace.inertia_frame', exc)

    try:
        gralin_24 = get_object('.template_2_brake.gel_upper_dragbrace.gralin_24')
        relative_to = get_object('.template_2_brake.gel_upper_dragbrace')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_2_brake.gel_upper_dragbrace.gralin_24')
        _template_2_brake_ground_hpl_udb_spndl_atch_1 = get_object('.template_2_brake.ground.hpl_udb_spndl_atch_1')
        gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_udb_spndl_atch_1))
        _template_2_brake_ground_hpl_udb_spndl_atch_1 = get_object('.template_2_brake.ground.hpl_udb_spndl_atch_1').location
        _template_2_brake_ground_hpl_ldb_udb_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_udb_atch_1').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_udb_spndl_atch_1, _template_2_brake_ground_hpl_ldb_udb_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_dragbrace.gralin_24', exc)

    try:
        jxl_joint_j_14 = get_object('.template_2_brake.gel_upper_dragbrace.jxl_joint_j_14')
        relative_to = get_object('.template_2_brake.gel_upper_dragbrace')
        jxl_joint_j_14.relative_to = relative_to
        jxl_joint_j_14.marker_name = target_path('.template_2_brake.gel_upper_dragbrace.jxl_joint_j_14')
        _template_2_brake_ground_hpl_ldb_udb_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_udb_atch_1')
        jxl_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_ldb_udb_atch_1))
        _template_2_brake_ground_cfl_plane_ref_2 = get_object('.template_2_brake.ground.cfl_plane_ref_2')
        jxl_joint_j_14.orientation = _template_2_brake_ground_cfl_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_14.location, jxl_joint_j_14.orientation)
        jxl_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_dragbrace.jxl_joint_j_14', exc)

    try:
        uel_actuator_i_3 = get_object('.template_2_brake.gel_upper_dragbrace.uel_actuator_i_3')
        relative_to = get_object('.template_2_brake.gel_upper_dragbrace')
        uel_actuator_i_3.relative_to = relative_to
        uel_actuator_i_3.marker_name = target_path('.template_2_brake.gel_upper_dragbrace.uel_actuator_i_3')
        _template_2_brake_ground_hpl_ldb_udb_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_udb_atch_1')
        uel_actuator_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_ldb_udb_atch_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, uel_actuator_i_3.location, uel_actuator_i_3.orientation)
        uel_actuator_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_dragbrace.uel_actuator_i_3', exc)

    try:
        gralin_upper_dragbrace = get_object('.template_2_brake.gel_upper_dragbrace.gralin_upper_dragbrace')
        gralin_upper_dragbrace.cylinder_name = target_path('.template_2_brake.gel_upper_dragbrace.gralin_upper_dragbrace')
        _template_2_brake_ground_hpl_udb_spndl_atch_1 = get_object('.template_2_brake.ground.hpl_udb_spndl_atch_1').location
        _template_2_brake_ground_hpl_ldb_udb_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_udb_atch_1').location
        gralin_upper_dragbrace.length = (VecUtils.DM(_template_2_brake_ground_hpl_udb_spndl_atch_1, _template_2_brake_ground_hpl_ldb_udb_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_brake.gel_upper_dragbrace.gralin_upper_dragbrace', exc)

    try:
        inertia_frame = get_object('.template_2_brake.gel_lower_dragbrace.inertia_frame')
        relative_to = get_object('.template_2_brake.gel_lower_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_brake.gel_lower_dragbrace.inertia_frame')
        _template_2_brake_gel_lower_dragbrace_cm = get_object('.template_2_brake.gel_lower_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_lower_dragbrace_cm))
        _template_2_brake_gel_lower_dragbrace = get_object('.template_2_brake.gel_lower_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_lower_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_dragbrace.inertia_frame', exc)

    try:
        gralin_26 = get_object('.template_2_brake.gel_lower_dragbrace.gralin_26')
        relative_to = get_object('.template_2_brake.gel_lower_dragbrace')
        gralin_26.relative_to = relative_to
        gralin_26.marker_name = target_path('.template_2_brake.gel_lower_dragbrace.gralin_26')
        _template_2_brake_ground_hpl_ldb_udb_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_udb_atch_1')
        gralin_26.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_ldb_udb_atch_1))
        _template_2_brake_ground_hpl_ldb_udb_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_udb_atch_1').location
        _template_2_brake_ground_hpl_ldb_collar_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_collar_atch_1').location
        gralin_26.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_ldb_udb_atch_1, _template_2_brake_ground_hpl_ldb_collar_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_26.location, gralin_26.orientation)
        gralin_26.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_26.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_dragbrace.gralin_26', exc)

    try:
        jxl_joint_i_14 = get_object('.template_2_brake.gel_lower_dragbrace.jxl_joint_i_14')
        relative_to = get_object('.template_2_brake.gel_lower_dragbrace')
        jxl_joint_i_14.relative_to = relative_to
        jxl_joint_i_14.marker_name = target_path('.template_2_brake.gel_lower_dragbrace.jxl_joint_i_14')
        _template_2_brake_gel_upper_dragbrace_jxl_joint_j_14 = get_object('.template_2_brake.gel_upper_dragbrace.jxl_joint_j_14')
        jxl_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_dragbrace_jxl_joint_j_14))
        _template_2_brake_gel_upper_dragbrace_jxl_joint_j_14 = get_object('.template_2_brake.gel_upper_dragbrace.jxl_joint_j_14')
        jxl_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_dragbrace_jxl_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_14.location, jxl_joint_i_14.orientation)
        jxl_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_dragbrace.jxl_joint_i_14', exc)

    try:
        jxl_joint_i_10 = get_object('.template_2_brake.gel_lower_dragbrace.jxl_joint_i_10')
        relative_to = get_object('.template_2_brake.gel_lower_dragbrace')
        jxl_joint_i_10.relative_to = relative_to
        jxl_joint_i_10.marker_name = target_path('.template_2_brake.gel_lower_dragbrace.jxl_joint_i_10')
        _template_2_brake_gel_uc_collar_jxl_joint_j_10 = get_object('.template_2_brake.gel_uc_collar.jxl_joint_j_10')
        jxl_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_uc_collar_jxl_joint_j_10))
        _template_2_brake_gel_uc_collar_jxl_joint_j_10 = get_object('.template_2_brake.gel_uc_collar.jxl_joint_j_10')
        jxl_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_uc_collar_jxl_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_10.location, jxl_joint_i_10.orientation)
        jxl_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_dragbrace.jxl_joint_i_10', exc)

    try:
        graarm_1 = get_object('.template_2_brake.gel_lower_dragbrace.graarm_1')
        relative_to = get_object('.template_2_brake.gel_lower_dragbrace')
        graarm_1.relative_to = relative_to
        graarm_1.marker_name = target_path('.template_2_brake.gel_lower_dragbrace.graarm_1')
        _template_2_brake_ground_hpl_uplock_tab = get_object('.template_2_brake.ground.hpl_uplock_tab')
        graarm_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_uplock_tab))
        _template_2_brake_ground_hpl_uplock_tab = get_object('.template_2_brake.ground.hpl_uplock_tab').location
        _template_2_brake_ground_cfl_ldb_geompt_1 = get_object('.template_2_brake.ground.cfl_ldb_geompt_1').location
        _template_2_brake_ground_cfl_ldb_geompt_2 = get_object('.template_2_brake.ground.cfl_ldb_geompt_2').location
        graarm_1.orientation = (VecUtils.ORI_IN_PLANE(_template_2_brake_ground_hpl_uplock_tab, _template_2_brake_ground_cfl_ldb_geompt_1, _template_2_brake_ground_cfl_ldb_geompt_2, "X_XY"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_1.location, graarm_1.orientation)
        graarm_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        graarm_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_dragbrace.graarm_1', exc)

    try:
        graarm_2 = get_object('.template_2_brake.gel_lower_dragbrace.graarm_2')
        relative_to = get_object('.template_2_brake.gel_lower_dragbrace')
        graarm_2.relative_to = relative_to
        graarm_2.marker_name = target_path('.template_2_brake.gel_lower_dragbrace.graarm_2')
        _template_2_brake_ground_cfl_ldb_geompt_1 = get_object('.template_2_brake.ground.cfl_ldb_geompt_1')
        graarm_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_cfl_ldb_geompt_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_2.location, graarm_2.orientation)
        graarm_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_dragbrace.graarm_2', exc)

    try:
        graarm_3 = get_object('.template_2_brake.gel_lower_dragbrace.graarm_3')
        relative_to = get_object('.template_2_brake.gel_lower_dragbrace')
        graarm_3.relative_to = relative_to
        graarm_3.marker_name = target_path('.template_2_brake.gel_lower_dragbrace.graarm_3')
        _template_2_brake_ground_cfl_ldb_geompt_2 = get_object('.template_2_brake.ground.cfl_ldb_geompt_2')
        graarm_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_cfl_ldb_geompt_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graarm_3.location, graarm_3.orientation)
        graarm_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_dragbrace.graarm_3', exc)

    try:
        gralin_lower_dragbrace = get_object('.template_2_brake.gel_lower_dragbrace.gralin_lower_dragbrace')
        gralin_lower_dragbrace.cylinder_name = target_path('.template_2_brake.gel_lower_dragbrace.gralin_lower_dragbrace')
        _template_2_brake_ground_hpl_ldb_udb_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_udb_atch_1').location
        _template_2_brake_ground_hpl_ldb_collar_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_collar_atch_1').location
        gralin_lower_dragbrace.length = (VecUtils.DM(_template_2_brake_ground_hpl_ldb_udb_atch_1, _template_2_brake_ground_hpl_ldb_collar_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_brake.gel_lower_dragbrace.gralin_lower_dragbrace', exc)

    try:
        inertia_frame = get_object('.template_2_brake.gel_upper_torquearm.inertia_frame')
        relative_to = get_object('.template_2_brake.gel_upper_torquearm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_brake.gel_upper_torquearm.inertia_frame')
        _template_2_brake_gel_upper_torquearm_cm = get_object('.template_2_brake.gel_upper_torquearm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_torquearm_cm))
        _template_2_brake_gel_upper_torquearm = get_object('.template_2_brake.gel_upper_torquearm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_torquearm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_torquearm.inertia_frame', exc)

    try:
        gralin_11 = get_object('.template_2_brake.gel_upper_torquearm.gralin_11')
        relative_to = get_object('.template_2_brake.gel_upper_torquearm')
        gralin_11.relative_to = relative_to
        gralin_11.marker_name = target_path('.template_2_brake.gel_upper_torquearm.gralin_11')
        _template_2_brake_ground_hpl_uta_collar_atch_1 = get_object('.template_2_brake.ground.hpl_uta_collar_atch_1')
        gralin_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_uta_collar_atch_1))
        _template_2_brake_ground_hpl_uta_collar_atch_1 = get_object('.template_2_brake.ground.hpl_uta_collar_atch_1').location
        _template_2_brake_ground_hpl_uta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_1').location
        gralin_11.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_uta_collar_atch_1, _template_2_brake_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_11.location, gralin_11.orientation)
        gralin_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_torquearm.gralin_11', exc)

    try:
        jxl_joint_i_2 = get_object('.template_2_brake.gel_upper_torquearm.jxl_joint_i_2')
        relative_to = get_object('.template_2_brake.gel_upper_torquearm')
        jxl_joint_i_2.relative_to = relative_to
        jxl_joint_i_2.marker_name = target_path('.template_2_brake.gel_upper_torquearm.jxl_joint_i_2')
        _template_2_brake_gel_connector_jxl_joint_j_2 = get_object('.template_2_brake.gel_connector.jxl_joint_j_2')
        jxl_joint_i_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_connector_jxl_joint_j_2))
        _template_2_brake_gel_connector_jxl_joint_j_2 = get_object('.template_2_brake.gel_connector.jxl_joint_j_2')
        jxl_joint_i_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_connector_jxl_joint_j_2))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_2.location, jxl_joint_i_2.orientation)
        jxl_joint_i_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_torquearm.jxl_joint_i_2', exc)

    try:
        jxl_joint_i_3 = get_object('.template_2_brake.gel_upper_torquearm.jxl_joint_i_3')
        relative_to = get_object('.template_2_brake.gel_upper_torquearm')
        jxl_joint_i_3.relative_to = relative_to
        jxl_joint_i_3.marker_name = target_path('.template_2_brake.gel_upper_torquearm.jxl_joint_i_3')
        _template_2_brake_gel_uc_collar_jxl_joint_j_3 = get_object('.template_2_brake.gel_uc_collar.jxl_joint_j_3')
        jxl_joint_i_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_uc_collar_jxl_joint_j_3))
        _template_2_brake_gel_uc_collar_jxl_joint_j_3 = get_object('.template_2_brake.gel_uc_collar.jxl_joint_j_3')
        jxl_joint_i_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_uc_collar_jxl_joint_j_3))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_3.location, jxl_joint_i_3.orientation)
        jxl_joint_i_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_upper_torquearm.jxl_joint_i_3', exc)

    try:
        gralin_upper_torquearm = get_object('.template_2_brake.gel_upper_torquearm.gralin_upper_torquearm')
        gralin_upper_torquearm.cylinder_name = target_path('.template_2_brake.gel_upper_torquearm.gralin_upper_torquearm')
        _template_2_brake_ground_hpl_uta_collar_atch_1 = get_object('.template_2_brake.ground.hpl_uta_collar_atch_1').location
        _template_2_brake_ground_hpl_uta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_1').location
        gralin_upper_torquearm.length = (VecUtils.DM(_template_2_brake_ground_hpl_uta_collar_atch_1, _template_2_brake_ground_hpl_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_brake.gel_upper_torquearm.gralin_upper_torquearm', exc)

    try:
        inertia_frame = get_object('.template_2_brake.gel_lower_torquearm.inertia_frame')
        relative_to = get_object('.template_2_brake.gel_lower_torquearm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_brake.gel_lower_torquearm.inertia_frame')
        _template_2_brake_gel_lower_torquearm_cm = get_object('.template_2_brake.gel_lower_torquearm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_lower_torquearm_cm))
        _template_2_brake_gel_lower_torquearm = get_object('.template_2_brake.gel_lower_torquearm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_lower_torquearm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_torquearm.inertia_frame', exc)

    try:
        gralin_29 = get_object('.template_2_brake.gel_lower_torquearm.gralin_29')
        relative_to = get_object('.template_2_brake.gel_lower_torquearm')
        gralin_29.relative_to = relative_to
        gralin_29.marker_name = target_path('.template_2_brake.gel_lower_torquearm.gralin_29')
        _template_2_brake_ground_hpl_lta_lc_atch_1 = get_object('.template_2_brake.ground.hpl_lta_lc_atch_1')
        gralin_29.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_lta_lc_atch_1))
        _template_2_brake_ground_hpl_lta_lc_atch_1 = get_object('.template_2_brake.ground.hpl_lta_lc_atch_1').location
        _template_2_brake_ground_hpl_lta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_lta_connect_atch_1').location
        gralin_29.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_lta_lc_atch_1, _template_2_brake_ground_hpl_lta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_29.location, gralin_29.orientation)
        gralin_29.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_29.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_torquearm.gralin_29', exc)

    try:
        jxl_joint_i_11 = get_object('.template_2_brake.gel_lower_torquearm.jxl_joint_i_11')
        relative_to = get_object('.template_2_brake.gel_lower_torquearm')
        jxl_joint_i_11.relative_to = relative_to
        jxl_joint_i_11.marker_name = target_path('.template_2_brake.gel_lower_torquearm.jxl_joint_i_11')
        _template_2_brake_gel_lower_cylinder_jxl_joint_j_11 = get_object('.template_2_brake.gel_lower_cylinder.jxl_joint_j_11')
        jxl_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_lower_cylinder_jxl_joint_j_11))
        _template_2_brake_gel_lower_cylinder_jxl_joint_j_11 = get_object('.template_2_brake.gel_lower_cylinder.jxl_joint_j_11')
        jxl_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_lower_cylinder_jxl_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_11.location, jxl_joint_i_11.orientation)
        jxl_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_torquearm.jxl_joint_i_11', exc)

    try:
        jxl_joint_i_1 = get_object('.template_2_brake.gel_lower_torquearm.jxl_joint_i_1')
        relative_to = get_object('.template_2_brake.gel_lower_torquearm')
        jxl_joint_i_1.relative_to = relative_to
        jxl_joint_i_1.marker_name = target_path('.template_2_brake.gel_lower_torquearm.jxl_joint_i_1')
        _template_2_brake_gel_connector_jxl_joint_j_1 = get_object('.template_2_brake.gel_connector.jxl_joint_j_1')
        jxl_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_connector_jxl_joint_j_1))
        _template_2_brake_gel_connector_jxl_joint_j_1 = get_object('.template_2_brake.gel_connector.jxl_joint_j_1')
        jxl_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_connector_jxl_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_1.location, jxl_joint_i_1.orientation)
        jxl_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_lower_torquearm.jxl_joint_i_1', exc)

    try:
        gralin_lower_torquearm = get_object('.template_2_brake.gel_lower_torquearm.gralin_lower_torquearm')
        gralin_lower_torquearm.cylinder_name = target_path('.template_2_brake.gel_lower_torquearm.gralin_lower_torquearm')
        _template_2_brake_ground_hpl_lta_lc_atch_1 = get_object('.template_2_brake.ground.hpl_lta_lc_atch_1').location
        _template_2_brake_ground_hpl_lta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_lta_connect_atch_1').location
        gralin_lower_torquearm.length = (VecUtils.DM(_template_2_brake_ground_hpl_lta_lc_atch_1, _template_2_brake_ground_hpl_lta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_brake.gel_lower_torquearm.gralin_lower_torquearm', exc)

    try:
        inertia_frame = get_object('.template_2_brake.gel_connector.inertia_frame')
        relative_to = get_object('.template_2_brake.gel_connector')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_brake.gel_connector.inertia_frame')
        _template_2_brake_gel_connector_cm = get_object('.template_2_brake.gel_connector.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_connector_cm))
        _template_2_brake_gel_connector = get_object('.template_2_brake.gel_connector')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_connector))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_connector.inertia_frame', exc)

    try:
        gralin_3 = get_object('.template_2_brake.gel_connector.gralin_3')
        relative_to = get_object('.template_2_brake.gel_connector')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_2_brake.gel_connector.gralin_3')
        _template_2_brake_ground_hpl_connect_1 = get_object('.template_2_brake.ground.hpl_connect_1')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_connect_1))
        _template_2_brake_ground_hpl_connect_1 = get_object('.template_2_brake.ground.hpl_connect_1').location
        _template_2_brake_ground_hpl_uta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_1').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_connect_1, _template_2_brake_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_connector.gralin_3', exc)

    try:
        jxl_joint_j_1 = get_object('.template_2_brake.gel_connector.jxl_joint_j_1')
        relative_to = get_object('.template_2_brake.gel_connector')
        jxl_joint_j_1.relative_to = relative_to
        jxl_joint_j_1.marker_name = target_path('.template_2_brake.gel_connector.jxl_joint_j_1')
        _template_2_brake_ground_hpl_lta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_lta_connect_atch_1')
        jxl_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_lta_connect_atch_1))
        _template_2_brake_ground_hpl_lta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_lta_connect_atch_1').location
        _template_2_brake_ground_hpl_uta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_1').location
        jxl_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_lta_connect_atch_1, _template_2_brake_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_1.location, jxl_joint_j_1.orientation)
        jxl_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_connector.jxl_joint_j_1', exc)

    try:
        jxl_joint_j_2 = get_object('.template_2_brake.gel_connector.jxl_joint_j_2')
        relative_to = get_object('.template_2_brake.gel_connector')
        jxl_joint_j_2.relative_to = relative_to
        jxl_joint_j_2.marker_name = target_path('.template_2_brake.gel_connector.jxl_joint_j_2')
        _template_2_brake_ground_hpl_uta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_1')
        jxl_joint_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_uta_connect_atch_1))
        _template_2_brake_ground_hpl_uta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_1').location
        _template_2_brake_ground_hpl_uta_connect_atch_2 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_2').location
        jxl_joint_j_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_uta_connect_atch_1, _template_2_brake_ground_hpl_uta_connect_atch_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_2.location, jxl_joint_j_2.orientation)
        jxl_joint_j_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_connector.jxl_joint_j_2', exc)

    try:
        gralin_connector = get_object('.template_2_brake.gel_connector.gralin_connector')
        gralin_connector.cylinder_name = target_path('.template_2_brake.gel_connector.gralin_connector')
        _template_2_brake_ground_hpl_connect_1 = get_object('.template_2_brake.ground.hpl_connect_1').location
        _template_2_brake_ground_hpl_uta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_1').location
        gralin_connector.length = (VecUtils.DM(_template_2_brake_ground_hpl_connect_1, _template_2_brake_ground_hpl_uta_connect_atch_1))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_brake.gel_connector.gralin_connector', exc)

    try:
        inertia_frame = get_object('.template_2_brake.gel_uc_collar.inertia_frame')
        relative_to = get_object('.template_2_brake.gel_uc_collar')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_brake.gel_uc_collar.inertia_frame')
        _template_2_brake_gel_uc_collar_cm = get_object('.template_2_brake.gel_uc_collar.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_uc_collar_cm))
        _template_2_brake_gel_uc_collar = get_object('.template_2_brake.gel_uc_collar')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_uc_collar))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_uc_collar.inertia_frame', exc)

    try:
        gralin_5 = get_object('.template_2_brake.gel_uc_collar.gralin_5')
        relative_to = get_object('.template_2_brake.gel_uc_collar')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_2_brake.gel_uc_collar.gralin_5')
        _template_2_brake_ground_cfl_collar_top = get_object('.template_2_brake.ground.cfl_collar_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_cfl_collar_top))
        _template_2_brake_ground_cfl_collar_top = get_object('.template_2_brake.ground.cfl_collar_top').location
        _template_2_brake_ground_cfl_collar_bot = get_object('.template_2_brake.ground.cfl_collar_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_cfl_collar_top, _template_2_brake_ground_cfl_collar_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_uc_collar.gralin_5', exc)

    try:
        jxl_joint_j_3 = get_object('.template_2_brake.gel_uc_collar.jxl_joint_j_3')
        relative_to = get_object('.template_2_brake.gel_uc_collar')
        jxl_joint_j_3.relative_to = relative_to
        jxl_joint_j_3.marker_name = target_path('.template_2_brake.gel_uc_collar.jxl_joint_j_3')
        _template_2_brake_ground_hpl_uta_collar_atch_1 = get_object('.template_2_brake.ground.hpl_uta_collar_atch_1')
        jxl_joint_j_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_uta_collar_atch_1))
        _template_2_brake_ground_hpl_lta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_lta_connect_atch_1').location
        _template_2_brake_ground_hpl_uta_connect_atch_1 = get_object('.template_2_brake.ground.hpl_uta_connect_atch_1').location
        jxl_joint_j_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_brake_ground_hpl_lta_connect_atch_1, _template_2_brake_ground_hpl_uta_connect_atch_1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_3.location, jxl_joint_j_3.orientation)
        jxl_joint_j_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_uc_collar.jxl_joint_j_3', exc)

    try:
        jxl_joint_i_4 = get_object('.template_2_brake.gel_uc_collar.jxl_joint_i_4')
        relative_to = get_object('.template_2_brake.gel_uc_collar')
        jxl_joint_i_4.relative_to = relative_to
        jxl_joint_i_4.marker_name = target_path('.template_2_brake.gel_uc_collar.jxl_joint_i_4')
        _template_2_brake_gel_upper_cylinder_jxl_joint_j_4 = get_object('.template_2_brake.gel_upper_cylinder.jxl_joint_j_4')
        jxl_joint_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_cylinder_jxl_joint_j_4))
        _template_2_brake_gel_upper_cylinder_jxl_joint_j_4 = get_object('.template_2_brake.gel_upper_cylinder.jxl_joint_j_4')
        jxl_joint_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_gel_upper_cylinder_jxl_joint_j_4))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_i_4.location, jxl_joint_i_4.orientation)
        jxl_joint_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_uc_collar.jxl_joint_i_4', exc)

    try:
        jxl_joint_j_10 = get_object('.template_2_brake.gel_uc_collar.jxl_joint_j_10')
        relative_to = get_object('.template_2_brake.gel_uc_collar')
        jxl_joint_j_10.relative_to = relative_to
        jxl_joint_j_10.marker_name = target_path('.template_2_brake.gel_uc_collar.jxl_joint_j_10')
        _template_2_brake_ground_hpl_ldb_collar_atch_1 = get_object('.template_2_brake.ground.hpl_ldb_collar_atch_1')
        jxl_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_ldb_collar_atch_1))
        _template_2_brake_ground_cfl_plane_ref_2 = get_object('.template_2_brake.ground.cfl_plane_ref_2')
        jxl_joint_j_10.orientation = _template_2_brake_ground_cfl_plane_ref_2.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxl_joint_j_10.location, jxl_joint_j_10.orientation)
        jxl_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxl_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.gel_uc_collar.jxl_joint_j_10', exc)

    try:
        gralin_uc_collar = get_object('.template_2_brake.gel_uc_collar.gralin_uc_collar')
        gralin_uc_collar.cylinder_name = target_path('.template_2_brake.gel_uc_collar.gralin_uc_collar')
        _template_2_brake_ground_cfl_collar_top = get_object('.template_2_brake.ground.cfl_collar_top').location
        _template_2_brake_ground_cfl_collar_bot = get_object('.template_2_brake.ground.cfl_collar_bot').location
        gralin_uc_collar.length = (VecUtils.DM(_template_2_brake_ground_cfl_collar_top, _template_2_brake_ground_cfl_collar_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_brake.gel_uc_collar.gralin_uc_collar', exc)

    try:
        MARKER_202 = get_object('.template_2_brake.luntai.wheel_part.MARKER_202')
        relative_to = get_object('.template_2_brake.luntai.wheel_part')
        MARKER_202.relative_to = relative_to
        MARKER_202.marker_name = target_path('.template_2_brake.luntai.wheel_part.MARKER_202')
        _template_2_brake_ground_hpl_wheel_center = get_object('.template_2_brake.ground.hpl_wheel_center')
        MARKER_202.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_202.location, MARKER_202.orientation)
        MARKER_202.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.luntai.wheel_part.MARKER_202', exc)

    try:
        MARKER_209 = get_object('.template_2_brake.luntai.wheel_part.MARKER_209')
        relative_to = get_object('.template_2_brake.luntai.wheel_part')
        MARKER_209.relative_to = relative_to
        MARKER_209.marker_name = target_path('.template_2_brake.luntai.wheel_part.MARKER_209')
        _template_2_brake_ground_hpl_wheel_center = get_object('.template_2_brake.ground.hpl_wheel_center')
        MARKER_209.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_209.location, MARKER_209.orientation)
        MARKER_209.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.luntai.wheel_part.MARKER_209', exc)

    try:
        MARKER_224 = get_object('.template_2_brake.luntai.wheel_part.MARKER_224')
        relative_to = get_object('.template_2_brake.luntai.wheel_part')
        MARKER_224.relative_to = relative_to
        MARKER_224.marker_name = target_path('.template_2_brake.luntai.wheel_part.MARKER_224')
        _template_2_brake_ground_hpl_wheel_center = get_object('.template_2_brake.ground.hpl_wheel_center')
        MARKER_224.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_224.location, MARKER_224.orientation)
        MARKER_224.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.luntai.wheel_part.MARKER_224', exc)

    try:
        MARKER_225 = get_object('.template_2_brake.luntai.wheel_part.MARKER_225')
        relative_to = get_object('.template_2_brake.luntai.wheel_part')
        MARKER_225.relative_to = relative_to
        MARKER_225.marker_name = target_path('.template_2_brake.luntai.wheel_part.MARKER_225')
        _template_2_brake_ground_hpl_wheel_center = get_object('.template_2_brake.ground.hpl_wheel_center')
        MARKER_225.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_hpl_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_225.location, MARKER_225.orientation)
        MARKER_225.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.luntai.wheel_part.MARKER_225', exc)

    try:
        gfo_i = get_object('.template_2_brake.luntai.wheel_part.gfo_i')
        relative_to = get_object('.template_2_brake.luntai.wheel_part')
        gfo_i.relative_to = relative_to
        gfo_i.marker_name = target_path('.template_2_brake.luntai.wheel_part.gfo_i')
        _template_2_brake_luntai_wheel_part_wheel_cm = get_object('.template_2_brake.luntai.wheel_part.wheel_cm')
        gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _template_2_brake_luntai_wheel_part_wheel_cm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
        gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.luntai.wheel_part.gfo_i', exc)

    try:
        MARKER_199 = get_object('.template_2_brake.zhiliang.MARKER_199')
        relative_to = get_object('.template_2_brake.zhiliang')
        MARKER_199.relative_to = relative_to
        MARKER_199.marker_name = target_path('.template_2_brake.zhiliang.MARKER_199')
        _template_2_brake_ground_POINT_48 = get_object('.template_2_brake.ground.POINT_48')
        MARKER_199.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_POINT_48))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_199.location, MARKER_199.orientation)
        MARKER_199.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.zhiliang.MARKER_199', exc)

    try:
        MARKER_229 = get_object('.template_2_brake.zhiliang.MARKER_229')
        relative_to = get_object('.template_2_brake.zhiliang')
        MARKER_229.relative_to = relative_to
        MARKER_229.marker_name = target_path('.template_2_brake.zhiliang.MARKER_229')
        _template_2_brake_ground_POINT_48 = get_object('.template_2_brake.ground.POINT_48')
        MARKER_229.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_POINT_48))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_229.location, MARKER_229.orientation)
        MARKER_229.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.zhiliang.MARKER_229', exc)

    try:
        MARKER_233 = get_object('.template_2_brake.zhiliang.MARKER_233')
        relative_to = get_object('.template_2_brake.zhiliang')
        MARKER_233.relative_to = relative_to
        MARKER_233.marker_name = target_path('.template_2_brake.zhiliang.MARKER_233')
        _template_2_brake_ground_POINT_48 = get_object('.template_2_brake.ground.POINT_48')
        MARKER_233.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_POINT_48))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_233.location, MARKER_233.orientation)
        MARKER_233.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.zhiliang.MARKER_233', exc)

    try:
        MARKER_239 = get_object('.template_2_brake.zhiliang.MARKER_239')
        relative_to = get_object('.template_2_brake.zhiliang')
        MARKER_239.relative_to = relative_to
        MARKER_239.marker_name = target_path('.template_2_brake.zhiliang.MARKER_239')
        _template_2_brake_ground_POINT_48 = get_object('.template_2_brake.ground.POINT_48')
        MARKER_239.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_brake_ground_POINT_48))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_239.location, MARKER_239.orientation)
        MARKER_239.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_brake.zhiliang.MARKER_239', exc)

    if model_dir is None:
        model_dir = os.path.dirname(os.path.abspath(__file__))
    resource_path_1 = os.path.abspath(os.path.join(model_dir, 'MLG.tir'))
    if not os.path.isfile(resource_path_1):
        record_error('轮胎文件路径（MLG.tir）', FileNotFoundError(resource_path_1))
    else:
        try:
            if set_resource('.template_2_brake.luntai.tpf_file', resource_path_1):
                updated += 1
        except Exception as exc:
            record_error('轮胎文件路径（MLG.tir）', exc)
    resource_path_2 = os.path.abspath(os.path.join(model_dir, '2d_flat.rdf'))
    if not os.path.isfile(resource_path_2):
        record_error('路面文件路径（2d_flat.rdf）', FileNotFoundError(resource_path_2))
    else:
        try:
            if set_resource('.template_2_brake.luntai.rpf_file', resource_path_2):
                updated += 1
        except Exception as exc:
            record_error('路面文件路径（2d_flat.rdf）', exc)
    return {'updated': updated, 'warnings': warnings, 'errors': errors}

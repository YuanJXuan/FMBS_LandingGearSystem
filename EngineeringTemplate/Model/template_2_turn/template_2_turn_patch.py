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

SOURCE_MODEL_NAME = 'template_2_turn'
ADM_UDE_KINDS = {'lm': 'road', 'lt_l': 'tire', 'lt_r': 'tire'}

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
        node = get_or_create('DataElementVariable', '.template_2_turn._cv_solver_variable')
        if hasattr(node, 'variable_name'):
            node.variable_name = target_path('.template_2_turn._cv_solver_variable')
        if hasattr(node, 'adams_id'):
            node.adams_id = 1
        updated += 1

    except Exception as exc:
        record_error('data_element create variable .template_2_turn._cv_solver_variable', exc)

    try:
        node = get_or_create('SimuScript', '.template_2_turn.Last_Sim')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_2_turn.Last_Sim')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=6.0 step_size=1.0E-03 model_name=.gcmb_2')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_2_turn.Last_Sim', exc)

    try:
        node = get_object('.template_2_turn.angle_drive')
        node.function = rewrite_expression('step(time,.template_2_turn.T_1,0d,.template_2_turn.T_2,-30d)')
        updated += 1

    except Exception as exc:
        record_error('constraint modify motion_generator .template_2_turn.angle_drive', exc)

    try:
        node = get_object('.template_2_turn._cv_solver_variable')
        node.function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('data_element modify variable .template_2_turn._cv_solver_variable', exc)

    try:
        node = get_object('.template_2_turn.jiaodu')
        node.function = rewrite_expression('AZ(.template_2_turn.ges_collar.inertia_frame, .template_2_turn.ges_upper_cylinder.inertia_frame)*180/pi-180')
        updated += 1

    except Exception as exc:
        record_error('measure modify function .template_2_turn.jiaodu', exc)

    try:
        node = get_object('.template_2_turn.jsd')
        node.function = rewrite_expression('wz(.template_2_turn.ges_collar.inertia_frame, .template_2_turn.ges_upper_cylinder.inertia_frame)*30/pi')
        updated += 1

    except Exception as exc:
        record_error('measure modify function .template_2_turn.jsd', exc)

    try:
        node = get_object('.template_2_turn._cv_diff')
        node.function = rewrite_expression('0')
        updated += 1

    except Exception as exc:
        record_error('part modify equation differential_equation .template_2_turn._cv_diff', exc)

    try:
        node = get_object('.template_2_turn.turning_force')
        node.function = rewrite_expression('step(time,2,0,4,1)*(5000/30)*(.template_2_turn.angle+.template_2_turn.jiaodu)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_turn.turning_force', exc)

    try:
        node = get_object('.template_2_turn.damping_force')
        node.function = rewrite_expression('.template_2_turn.jsd*.template_2_turn.damping_coefficient')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_turn.damping_force', exc)

    try:
        node = get_object('.template_2_turn.NLG_AIR')
        node.function = rewrite_expression('if((DM(.template_2_turn.ges_upper_cylinder.MARKER_124,.template_2_turn.ges_lower_cylinder.MARKER_125)-228.6):-.template_2_turn.stiffness_air*(DM(.template_2_turn.ges_upper_cylinder.MARKER_124,.template_2_turn.ges_lower_cylinder.MARKER_125)-228.6)-.template_2_turn.damping_air*VR(.template_2_turn.ges_upper_cylinder.MARKER_124,.template_2_turn.ges_lower_cylinder.MARKER_125),0,0)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_turn.NLG_AIR', exc)

    try:
        node = get_object('.template_2_turn.NLG_STOP')
        node.function = rewrite_expression('-if((DM(.template_2_turn.ges_upper_cylinder.MARKER_126,.template_2_turn.ges_lower_cylinder.MARKER_127)-258.6):0,0,-.template_2_turn.stiffness_stop*(DM(.template_2_turn.ges_upper_cylinder.MARKER_126,.template_2_turn.ges_lower_cylinder.MARKER_127)-258.6)-.template_2_turn.damping_stop*VR(.template_2_turn.ges_upper_cylinder.MARKER_126,.template_2_turn.ges_lower_cylinder.MARKER_127))')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_turn.NLG_STOP', exc)

    try:
        node = get_object('.template_2_turn.thrust')
        node.function = rewrite_expression('-30000*2/3.14*atan(.template_2_turn.vel-.template_2_turn.jscm_sd)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_turn.thrust', exc)

    try:
        node = get_object('.template_2_turn.NLG_OIL')
        node.function = rewrite_expression('if(DM(.template_2_turn.ges_upper_cylinder.MARKER_163,.template_2_turn.ges_lower_cylinder.MARKER_164)-228.6:-.template_2_turn.stiffness_oil*(DM(.template_2_turn.ges_upper_cylinder.MARKER_163,.template_2_turn.ges_lower_cylinder.MARKER_164)-228.6)-.template_2_turn.damping_oil*VR(.template_2_turn.ges_upper_cylinder.MARKER_163,.template_2_turn.ges_lower_cylinder.MARKER_164),0,0)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_turn.NLG_OIL', exc)

    try:
        mts_mount_j_2 = get_object('.template_2_turn.ground.mts_mount_j_2')
        mts_mount_j_2.marker_name = target_path('.template_2_turn.ground.mts_mount_j_2')
        _template_2_turn_mts_body_mount = get_object('.template_2_turn.mts_body_mount')
        mts_mount_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_mts_body_mount))
        _template_2_turn_mts_body_mount = get_object('.template_2_turn.mts_body_mount')
        mts_mount_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_mts_body_mount))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ground.mts_mount_j_2', exc)

    try:
        cfl_spin_axis = get_object('.template_2_turn.ground.cfl_spin_axis')
        cfl_spin_axis.marker_name = target_path('.template_2_turn.ground.cfl_spin_axis')
        _template_2_turn_ground_hpl_wheel_center = get_object('.template_2_turn.ground.hpl_wheel_center')
        cfl_spin_axis.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hpl_wheel_center))
        _template_2_turn_ground_hpl_wheel_center = get_object('.template_2_turn.ground.hpl_wheel_center').location
        _template_2_turn_ground_hpl_ob_axle = get_object('.template_2_turn.ground.hpl_ob_axle').location
        cfl_spin_axis.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hpl_wheel_center, _template_2_turn_ground_hpl_ob_axle, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ground.cfl_spin_axis', exc)

    try:
        cfr_spin_axis = get_object('.template_2_turn.ground.cfr_spin_axis')
        cfr_spin_axis.marker_name = target_path('.template_2_turn.ground.cfr_spin_axis')
        _template_2_turn_ground_hpr_wheel_center = get_object('.template_2_turn.ground.hpr_wheel_center')
        cfr_spin_axis.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hpr_wheel_center))
        _template_2_turn_ground_hpr_wheel_center = get_object('.template_2_turn.ground.hpr_wheel_center').location
        _template_2_turn_ground_hpr_ob_axle = get_object('.template_2_turn.ground.hpr_ob_axle').location
        cfr_spin_axis.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hpr_wheel_center, _template_2_turn_ground_hpr_ob_axle, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ground.cfr_spin_axis', exc)

    try:
        cfs_nlg_axle_lowpoint = get_object('.template_2_turn.ground.cfs_nlg_axle_lowpoint')
        cfs_nlg_axle_lowpoint.marker_name = target_path('.template_2_turn.ground.cfs_nlg_axle_lowpoint')
        _template_2_turn_ground_hps_nlg_axle_lowpoint = get_object('.template_2_turn.ground.hps_nlg_axle_lowpoint')
        cfs_nlg_axle_lowpoint.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_nlg_axle_lowpoint))
        _template_2_turn_ground_origo = get_object('.template_2_turn.ground.origo')
        cfs_nlg_axle_lowpoint.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ground.cfs_nlg_axle_lowpoint', exc)

    try:
        cfs_collar_top = get_object('.template_2_turn.ground.cfs_collar_top')
        cfs_collar_top.marker_name = target_path('.template_2_turn.ground.cfs_collar_top')
        _template_2_turn_ground_hps_uc_bot = get_object('.template_2_turn.ground.hps_uc_bot').location
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top').location
        cfs_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_2_turn_ground_hps_uc_bot, _template_2_turn_ground_hps_uc_top, 0.11 * VecUtils.DM(_template_2_turn_ground_hps_uc_bot, _template_2_turn_ground_hps_uc_top)))
        _template_2_turn_ground_hps_uc_bot = get_object('.template_2_turn.ground.hps_uc_bot').location
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top').location
        cfs_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_uc_bot, _template_2_turn_ground_hps_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ground.cfs_collar_top', exc)

    try:
        lm_ref_1 = get_object('.template_2_turn.ground.lm_ref_1')
        lm_ref_1.marker_name = target_path('.template_2_turn.ground.lm_ref_1')
        _template_2_turn_lm = get_object('.template_2_turn.lm').location
        lm_ref_1.location = _template_2_turn_lm
        _template_2_turn_lm = get_object('.template_2_turn.lm').orientation
        lm_ref_1.orientation = _template_2_turn_lm


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ground.lm_ref_1', exc)

    try:
        zdt1 = get_object('.template_2_turn.ground.zdt1')
        zdt1.marker_name = target_path('.template_2_turn.ground.zdt1')
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_hsg_2 = get_object('.template_2_turn.ground.hsg_2').location
        zdt1.location = (VecUtils.LOC_ALONG_LINE(_template_2_turn_ground_hsg_1, _template_2_turn_ground_hsg_2, 0.6 * VecUtils.DM(_template_2_turn_ground_hsg_1, _template_2_turn_ground_hsg_2)))
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_hsg_2 = get_object('.template_2_turn.ground.hsg_2').location
        zdt1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hsg_1, _template_2_turn_ground_hsg_2, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ground.zdt1', exc)

    try:
        zdt2 = get_object('.template_2_turn.ground.zdt2')
        zdt2.marker_name = target_path('.template_2_turn.ground.zdt2')
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_hsg_2 = get_object('.template_2_turn.ground.hsg_2').location
        zdt2.location = (VecUtils.LOC_ALONG_LINE(_template_2_turn_ground_hsg_1, _template_2_turn_ground_hsg_2, 0.9 * VecUtils.DM(_template_2_turn_ground_hsg_1, _template_2_turn_ground_hsg_2)))
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_hsg_2 = get_object('.template_2_turn.ground.hsg_2').location
        zdt2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hsg_1, _template_2_turn_ground_hsg_2, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ground.zdt2', exc)

    try:
        inertia_frame = get_object('.template_2_turn.ges_dragbrace.inertia_frame')
        relative_to = get_object('.template_2_turn.ges_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_turn.ges_dragbrace.inertia_frame')
        _template_2_turn_ges_dragbrace_cm = get_object('.template_2_turn.ges_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_dragbrace_cm))
        _template_2_turn_ges_dragbrace = get_object('.template_2_turn.ges_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_dragbrace.inertia_frame', exc)

    try:
        gralin_1 = get_object('.template_2_turn.ges_dragbrace.gralin_1')
        relative_to = get_object('.template_2_turn.ges_dragbrace')
        gralin_1.relative_to = relative_to
        gralin_1.marker_name = target_path('.template_2_turn.ges_dragbrace.gralin_1')
        _template_2_turn_ground_hps_db_sf_atch = get_object('.template_2_turn.ground.hps_db_sf_atch')
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_db_sf_atch))
        _template_2_turn_ground_hps_db_sf_atch = get_object('.template_2_turn.ground.hps_db_sf_atch').location
        _template_2_turn_ground_hps_db_uc_atch = get_object('.template_2_turn.ground.hps_db_uc_atch').location
        gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_db_sf_atch, _template_2_turn_ground_hps_db_uc_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_dragbrace.gralin_1', exc)

    try:
        jxs_joint_i_12 = get_object('.template_2_turn.ges_dragbrace.jxs_joint_i_12')
        relative_to = get_object('.template_2_turn.ges_dragbrace')
        jxs_joint_i_12.relative_to = relative_to
        jxs_joint_i_12.marker_name = target_path('.template_2_turn.ges_dragbrace.jxs_joint_i_12')
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_12 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_12')
        jxs_joint_i_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_12))
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_12 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_12')
        jxs_joint_i_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_12.location, jxs_joint_i_12.orientation)
        jxs_joint_i_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_dragbrace.jxs_joint_i_12', exc)

    try:
        jxs_joint_i_14 = get_object('.template_2_turn.ges_dragbrace.jxs_joint_i_14')
        relative_to = get_object('.template_2_turn.ges_dragbrace')
        jxs_joint_i_14.relative_to = relative_to
        jxs_joint_i_14.marker_name = target_path('.template_2_turn.ges_dragbrace.jxs_joint_i_14')
        _template_2_turn_ges_subframe_jxs_joint_j_14 = get_object('.template_2_turn.ges_subframe.jxs_joint_j_14')
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_subframe_jxs_joint_j_14))
        _template_2_turn_ges_subframe_jxs_joint_j_14 = get_object('.template_2_turn.ges_subframe.jxs_joint_j_14')
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_subframe_jxs_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_dragbrace.jxs_joint_i_14', exc)

    try:
        gralin_dragbrace_geom = get_object('.template_2_turn.ges_dragbrace.gralin_dragbrace_geom')
        gralin_dragbrace_geom.cylinder_name = target_path('.template_2_turn.ges_dragbrace.gralin_dragbrace_geom')
        _template_2_turn_ground_hps_db_sf_atch = get_object('.template_2_turn.ground.hps_db_sf_atch').location
        _template_2_turn_ground_hps_db_uc_atch = get_object('.template_2_turn.ground.hps_db_uc_atch').location
        gralin_dragbrace_geom.length = (VecUtils.DM(_template_2_turn_ground_hps_db_sf_atch, _template_2_turn_ground_hps_db_uc_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.ges_dragbrace.gralin_dragbrace_geom', exc)

    try:
        inertia_frame = get_object('.template_2_turn.ges_upper_cylinder.inertia_frame')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_turn.ges_upper_cylinder.inertia_frame')
        _template_2_turn_ges_upper_cylinder_cm = get_object('.template_2_turn.ges_upper_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_cm))
        _template_2_turn_ges_upper_cylinder = get_object('.template_2_turn.ges_upper_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.inertia_frame', exc)

    try:
        gralin_2 = get_object('.template_2_turn.ges_upper_cylinder.gralin_2')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        gralin_2.relative_to = relative_to
        gralin_2.marker_name = target_path('.template_2_turn.ges_upper_cylinder.gralin_2')
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top')
        gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_top))
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top').location
        _template_2_turn_ground_hps_uc_bot = get_object('.template_2_turn.ground.hps_uc_bot').location
        gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_uc_top, _template_2_turn_ground_hps_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_2.location, gralin_2.orientation)
        gralin_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.gralin_2', exc)

    try:
        gralin_3 = get_object('.template_2_turn.ges_upper_cylinder.gralin_3')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_2_turn.ges_upper_cylinder.gralin_3')
        _template_2_turn_ground_hps_uc_sf_atch_l = get_object('.template_2_turn.ground.hps_uc_sf_atch_l')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_sf_atch_l))
        _template_2_turn_ground_hps_uc_sf_atch_l = get_object('.template_2_turn.ground.hps_uc_sf_atch_l').location
        _template_2_turn_ground_hps_uc_geompt = get_object('.template_2_turn.ground.hps_uc_geompt').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_uc_sf_atch_l, _template_2_turn_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.gralin_3', exc)

    try:
        gralin_4 = get_object('.template_2_turn.ges_upper_cylinder.gralin_4')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        gralin_4.relative_to = relative_to
        gralin_4.marker_name = target_path('.template_2_turn.ges_upper_cylinder.gralin_4')
        _template_2_turn_ground_hps_uc_sf_atch_r = get_object('.template_2_turn.ground.hps_uc_sf_atch_r')
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_sf_atch_r))
        _template_2_turn_ground_hps_uc_sf_atch_r = get_object('.template_2_turn.ground.hps_uc_sf_atch_r').location
        _template_2_turn_ground_hps_uc_geompt = get_object('.template_2_turn.ground.hps_uc_geompt').location
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_uc_sf_atch_r, _template_2_turn_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.gralin_4', exc)

    try:
        jxs_joint_j_12 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_12')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        jxs_joint_j_12.relative_to = relative_to
        jxs_joint_j_12.marker_name = target_path('.template_2_turn.ges_upper_cylinder.jxs_joint_j_12')
        _template_2_turn_ground_hps_db_uc_atch = get_object('.template_2_turn.ground.hps_db_uc_atch')
        jxs_joint_j_12.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_db_uc_atch))
        _template_2_turn_ground_origo = get_object('.template_2_turn.ground.origo')
        jxs_joint_j_12.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_12.location, jxs_joint_j_12.orientation)
        jxs_joint_j_12.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_12.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.jxs_joint_j_12', exc)

    try:
        jxs_joint_i_15 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_i_15')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        jxs_joint_i_15.relative_to = relative_to
        jxs_joint_i_15.marker_name = target_path('.template_2_turn.ges_upper_cylinder.jxs_joint_i_15')
        _template_2_turn_ges_subframe_jxs_joint_j_15 = get_object('.template_2_turn.ges_subframe.jxs_joint_j_15')
        jxs_joint_i_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_subframe_jxs_joint_j_15))
        _template_2_turn_ges_subframe_jxs_joint_j_15 = get_object('.template_2_turn.ges_subframe.jxs_joint_j_15')
        jxs_joint_i_15.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_subframe_jxs_joint_j_15))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_15.location, jxs_joint_i_15.orientation)
        jxs_joint_i_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.jxs_joint_i_15', exc)

    try:
        ues_spring_j_1 = get_object('.template_2_turn.ges_upper_cylinder.ues_spring_j_1')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        ues_spring_j_1.relative_to = relative_to
        ues_spring_j_1.marker_name = target_path('.template_2_turn.ges_upper_cylinder.ues_spring_j_1')
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top')
        ues_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_j_1.location, ues_spring_j_1.orientation)
        ues_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.ues_spring_j_1', exc)

    try:
        ues_damper_j_1 = get_object('.template_2_turn.ges_upper_cylinder.ues_damper_j_1')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        ues_damper_j_1.relative_to = relative_to
        ues_damper_j_1.marker_name = target_path('.template_2_turn.ges_upper_cylinder.ues_damper_j_1')
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top')
        ues_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_j_1.location, ues_damper_j_1.orientation)
        ues_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.ues_damper_j_1', exc)

    try:
        ues_stopper_j_1 = get_object('.template_2_turn.ges_upper_cylinder.ues_stopper_j_1')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        ues_stopper_j_1.relative_to = relative_to
        ues_stopper_j_1.marker_name = target_path('.template_2_turn.ges_upper_cylinder.ues_stopper_j_1')
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top')
        ues_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_j_1.location, ues_stopper_j_1.orientation)
        ues_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.ues_stopper_j_1', exc)

    try:
        jxs_joint_j_1 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_1')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        jxs_joint_j_1.relative_to = relative_to
        jxs_joint_j_1.marker_name = target_path('.template_2_turn.ges_upper_cylinder.jxs_joint_j_1')
        _template_2_turn_ground_cfs_collar_top = get_object('.template_2_turn.ground.cfs_collar_top')
        jxs_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_cfs_collar_top))
        _template_2_turn_ground_hps_uc_bot = get_object('.template_2_turn.ground.hps_uc_bot').location
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top').location
        jxs_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_uc_bot, _template_2_turn_ground_hps_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
        jxs_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.jxs_joint_j_1', exc)

    try:
        ues_actuator_j_1 = get_object('.template_2_turn.ges_upper_cylinder.ues_actuator_j_1')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        ues_actuator_j_1.relative_to = relative_to
        ues_actuator_j_1.marker_name = target_path('.template_2_turn.ges_upper_cylinder.ues_actuator_j_1')
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_1.location, ues_actuator_j_1.orientation)
        ues_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.ues_actuator_j_1', exc)

    try:
        ues_actuator_j_4 = get_object('.template_2_turn.ges_upper_cylinder.ues_actuator_j_4')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        ues_actuator_j_4.relative_to = relative_to
        ues_actuator_j_4.marker_name = target_path('.template_2_turn.ges_upper_cylinder.ues_actuator_j_4')
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_4.location, ues_actuator_j_4.orientation)
        ues_actuator_j_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_j_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.ues_actuator_j_4', exc)

    try:
        gralin_upper_cylinder_geom1 = get_object('.template_2_turn.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        gralin_upper_cylinder_geom1.cylinder_name = target_path('.template_2_turn.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top').location
        _template_2_turn_ground_hps_uc_bot = get_object('.template_2_turn.ground.hps_uc_bot').location
        gralin_upper_cylinder_geom1.length = (VecUtils.DM(_template_2_turn_ground_hps_uc_top, _template_2_turn_ground_hps_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.ges_upper_cylinder.gralin_upper_cylinder_geom1', exc)

    try:
        gralin_upper_cylinder_geom2 = get_object('.template_2_turn.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        gralin_upper_cylinder_geom2.cylinder_name = target_path('.template_2_turn.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        _template_2_turn_ground_hps_uc_sf_atch_l = get_object('.template_2_turn.ground.hps_uc_sf_atch_l').location
        _template_2_turn_ground_hps_uc_geompt = get_object('.template_2_turn.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom2.length = (VecUtils.DM(_template_2_turn_ground_hps_uc_sf_atch_l, _template_2_turn_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.ges_upper_cylinder.gralin_upper_cylinder_geom2', exc)

    try:
        gralin_upper_cylinder_geom3 = get_object('.template_2_turn.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        gralin_upper_cylinder_geom3.cylinder_name = target_path('.template_2_turn.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        _template_2_turn_ground_hps_uc_sf_atch_r = get_object('.template_2_turn.ground.hps_uc_sf_atch_r').location
        _template_2_turn_ground_hps_uc_geompt = get_object('.template_2_turn.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom3.length = (VecUtils.DM(_template_2_turn_ground_hps_uc_sf_atch_r, _template_2_turn_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.ges_upper_cylinder.gralin_upper_cylinder_geom3', exc)

    try:
        MARKER_77 = get_object('.template_2_turn.ges_upper_cylinder.MARKER_77')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        MARKER_77.relative_to = relative_to
        MARKER_77.marker_name = target_path('.template_2_turn.ges_upper_cylinder.MARKER_77')
        _template_2_turn_ground_zdt1 = get_object('.template_2_turn.ground.zdt1')
        MARKER_77.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_zdt1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_77.location, MARKER_77.orientation)
        MARKER_77.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.MARKER_77', exc)

    try:
        MARKER_123 = get_object('.template_2_turn.ges_upper_cylinder.MARKER_123')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        MARKER_123.relative_to = relative_to
        MARKER_123.marker_name = target_path('.template_2_turn.ges_upper_cylinder.MARKER_123')
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top')
        MARKER_123.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_123.location, MARKER_123.orientation)
        MARKER_123.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.MARKER_123', exc)

    try:
        MARKER_163 = get_object('.template_2_turn.ges_upper_cylinder.MARKER_163')
        relative_to = get_object('.template_2_turn.ges_upper_cylinder')
        MARKER_163.relative_to = relative_to
        MARKER_163.marker_name = target_path('.template_2_turn.ges_upper_cylinder.MARKER_163')
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top')
        MARKER_163.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_163.location, MARKER_163.orientation)
        MARKER_163.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_cylinder.MARKER_163', exc)

    try:
        inertia_frame = get_object('.template_2_turn.ges_lower_cylinder.inertia_frame')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_turn.ges_lower_cylinder.inertia_frame')
        _template_2_turn_ges_lower_cylinder_cm = get_object('.template_2_turn.ges_lower_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_lower_cylinder_cm))
        _template_2_turn_ges_lower_cylinder = get_object('.template_2_turn.ges_lower_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_lower_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.inertia_frame', exc)

    try:
        gralin_5 = get_object('.template_2_turn.ges_lower_cylinder.gralin_5')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_2_turn.ges_lower_cylinder.gralin_5')
        _template_2_turn_ground_hps_lc_top = get_object('.template_2_turn.ground.hps_lc_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_lc_top))
        _template_2_turn_ground_hps_lc_top = get_object('.template_2_turn.ground.hps_lc_top').location
        _template_2_turn_ground_hps_lc_bot = get_object('.template_2_turn.ground.hps_lc_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_lc_top, _template_2_turn_ground_hps_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.gralin_5', exc)

    try:
        jxs_joint_j_9 = get_object('.template_2_turn.ges_lower_cylinder.jxs_joint_j_9')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        jxs_joint_j_9.relative_to = relative_to
        jxs_joint_j_9.marker_name = target_path('.template_2_turn.ges_lower_cylinder.jxs_joint_j_9')
        _template_2_turn_ground_hps_lta_lc_atch = get_object('.template_2_turn.ground.hps_lta_lc_atch')
        jxs_joint_j_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_lta_lc_atch))
        _template_2_turn_ground_origo = get_object('.template_2_turn.ground.origo')
        jxs_joint_j_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_9.location, jxs_joint_j_9.orientation)
        jxs_joint_j_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.jxs_joint_j_9', exc)

    try:
        jxs_joint_i_11 = get_object('.template_2_turn.ges_lower_cylinder.jxs_joint_i_11')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        jxs_joint_i_11.relative_to = relative_to
        jxs_joint_i_11.marker_name = target_path('.template_2_turn.ges_lower_cylinder.jxs_joint_i_11')
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_11))
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
        jxs_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.jxs_joint_i_11', exc)

    try:
        gralin_7 = get_object('.template_2_turn.ges_lower_cylinder.gralin_7')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        gralin_7.relative_to = relative_to
        gralin_7.marker_name = target_path('.template_2_turn.ges_lower_cylinder.gralin_7')
        _template_2_turn_ground_hpr_wheel_center = get_object('.template_2_turn.ground.hpr_wheel_center')
        gralin_7.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hpr_wheel_center))
        _template_2_turn_ground_hpr_wheel_center = get_object('.template_2_turn.ground.hpr_wheel_center').location
        _template_2_turn_ground_hpl_wheel_center = get_object('.template_2_turn.ground.hpl_wheel_center').location
        gralin_7.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hpr_wheel_center, _template_2_turn_ground_hpl_wheel_center, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_7.location, gralin_7.orientation)
        gralin_7.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_7.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.gralin_7', exc)

    try:
        ues_spring_i_1 = get_object('.template_2_turn.ges_lower_cylinder.ues_spring_i_1')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        ues_spring_i_1.relative_to = relative_to
        ues_spring_i_1.marker_name = target_path('.template_2_turn.ges_lower_cylinder.ues_spring_i_1')
        _template_2_turn_ground_hps_lc_top = get_object('.template_2_turn.ground.hps_lc_top')
        ues_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_i_1.location, ues_spring_i_1.orientation)
        ues_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.ues_spring_i_1', exc)

    try:
        ues_damper_i_1 = get_object('.template_2_turn.ges_lower_cylinder.ues_damper_i_1')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        ues_damper_i_1.relative_to = relative_to
        ues_damper_i_1.marker_name = target_path('.template_2_turn.ges_lower_cylinder.ues_damper_i_1')
        _template_2_turn_ground_hps_lc_top = get_object('.template_2_turn.ground.hps_lc_top')
        ues_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_i_1.location, ues_damper_i_1.orientation)
        ues_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.ues_damper_i_1', exc)

    try:
        ues_stopper_i_1 = get_object('.template_2_turn.ges_lower_cylinder.ues_stopper_i_1')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        ues_stopper_i_1.relative_to = relative_to
        ues_stopper_i_1.marker_name = target_path('.template_2_turn.ges_lower_cylinder.ues_stopper_i_1')
        _template_2_turn_ground_hps_lc_top = get_object('.template_2_turn.ground.hps_lc_top')
        ues_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_i_1.location, ues_stopper_i_1.orientation)
        ues_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.ues_stopper_i_1', exc)

    try:
        coomarker_2 = get_object('.template_2_turn.ges_lower_cylinder.coomarker_2')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        coomarker_2.relative_to = relative_to
        coomarker_2.marker_name = target_path('.template_2_turn.ges_lower_cylinder.coomarker_2')
        _template_2_turn_ground_cfs_wheel_centers_midpoint = get_object('.template_2_turn.ground.cfs_wheel_centers_midpoint')
        coomarker_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_cfs_wheel_centers_midpoint))
        _template_2_turn_ground_cfs_wheel_centers_midpoint = get_object('.template_2_turn.ground.cfs_wheel_centers_midpoint')
        coomarker_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_cfs_wheel_centers_midpoint))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_2.location, coomarker_2.orientation)
        coomarker_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.coomarker_2', exc)

    try:
        coomarker_3 = get_object('.template_2_turn.ges_lower_cylinder.coomarker_3')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        coomarker_3.relative_to = relative_to
        coomarker_3.marker_name = target_path('.template_2_turn.ges_lower_cylinder.coomarker_3')
        _template_2_turn_ground_cfs_nlg_axle_lowpoint = get_object('.template_2_turn.ground.cfs_nlg_axle_lowpoint')
        coomarker_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_cfs_nlg_axle_lowpoint))
        _template_2_turn_ground_cfs_nlg_axle_lowpoint = get_object('.template_2_turn.ground.cfs_nlg_axle_lowpoint')
        coomarker_3.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_cfs_nlg_axle_lowpoint))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_3.location, coomarker_3.orientation)
        coomarker_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.coomarker_3', exc)

    try:
        gralin_geom1 = get_object('.template_2_turn.ges_lower_cylinder.gralin_geom1')
        gralin_geom1.cylinder_name = target_path('.template_2_turn.ges_lower_cylinder.gralin_geom1')
        _template_2_turn_ground_hps_lc_top = get_object('.template_2_turn.ground.hps_lc_top').location
        _template_2_turn_ground_hps_lc_bot = get_object('.template_2_turn.ground.hps_lc_bot').location
        gralin_geom1.length = (VecUtils.DM(_template_2_turn_ground_hps_lc_top, _template_2_turn_ground_hps_lc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.ges_lower_cylinder.gralin_geom1', exc)

    try:
        gralin_geom2 = get_object('.template_2_turn.ges_lower_cylinder.gralin_geom2')
        gralin_geom2.cylinder_name = target_path('.template_2_turn.ges_lower_cylinder.gralin_geom2')
        _template_2_turn_ground_hpr_wheel_center = get_object('.template_2_turn.ground.hpr_wheel_center').location
        _template_2_turn_ground_hpl_wheel_center = get_object('.template_2_turn.ground.hpl_wheel_center').location
        gralin_geom2.length = (VecUtils.DM(_template_2_turn_ground_hpr_wheel_center, _template_2_turn_ground_hpl_wheel_center))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.ges_lower_cylinder.gralin_geom2', exc)

    try:
        MARKER_122 = get_object('.template_2_turn.ges_lower_cylinder.MARKER_122')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        MARKER_122.relative_to = relative_to
        MARKER_122.marker_name = target_path('.template_2_turn.ges_lower_cylinder.MARKER_122')
        _template_2_turn_ground_hps_lc_top = get_object('.template_2_turn.ground.hps_lc_top')
        MARKER_122.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_122.location, MARKER_122.orientation)
        MARKER_122.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.MARKER_122', exc)

    try:
        MARKER_158 = get_object('.template_2_turn.ges_lower_cylinder.MARKER_158')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        MARKER_158.relative_to = relative_to
        MARKER_158.marker_name = target_path('.template_2_turn.ges_lower_cylinder.MARKER_158')
        _template_2_turn_ground_hpl_wheel_center = get_object('.template_2_turn.ground.hpl_wheel_center')
        MARKER_158.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hpl_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_158.location, MARKER_158.orientation)
        MARKER_158.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.MARKER_158', exc)

    try:
        MARKER_160 = get_object('.template_2_turn.ges_lower_cylinder.MARKER_160')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        MARKER_160.relative_to = relative_to
        MARKER_160.marker_name = target_path('.template_2_turn.ges_lower_cylinder.MARKER_160')
        _template_2_turn_ground_hpr_wheel_center = get_object('.template_2_turn.ground.hpr_wheel_center')
        MARKER_160.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hpr_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_160.location, MARKER_160.orientation)
        MARKER_160.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.MARKER_160', exc)

    try:
        MARKER_164 = get_object('.template_2_turn.ges_lower_cylinder.MARKER_164')
        relative_to = get_object('.template_2_turn.ges_lower_cylinder')
        MARKER_164.relative_to = relative_to
        MARKER_164.marker_name = target_path('.template_2_turn.ges_lower_cylinder.MARKER_164')
        _template_2_turn_ground_hps_lc_top = get_object('.template_2_turn.ground.hps_lc_top')
        MARKER_164.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_164.location, MARKER_164.orientation)
        MARKER_164.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_cylinder.MARKER_164', exc)

    try:
        inertia_frame = get_object('.template_2_turn.ges_upper_torque_arm.inertia_frame')
        relative_to = get_object('.template_2_turn.ges_upper_torque_arm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_turn.ges_upper_torque_arm.inertia_frame')
        _template_2_turn_ges_upper_torque_arm_cm = get_object('.template_2_turn.ges_upper_torque_arm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_torque_arm_cm))
        _template_2_turn_ges_upper_torque_arm = get_object('.template_2_turn.ges_upper_torque_arm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_torque_arm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_torque_arm.inertia_frame', exc)

    try:
        gralin_9 = get_object('.template_2_turn.ges_upper_torque_arm.gralin_9')
        relative_to = get_object('.template_2_turn.ges_upper_torque_arm')
        gralin_9.relative_to = relative_to
        gralin_9.marker_name = target_path('.template_2_turn.ges_upper_torque_arm.gralin_9')
        _template_2_turn_ground_hps_uta_uc_atch = get_object('.template_2_turn.ground.hps_uta_uc_atch')
        gralin_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uta_uc_atch))
        _template_2_turn_ground_hps_uta_uc_atch = get_object('.template_2_turn.ground.hps_uta_uc_atch').location
        _template_2_turn_ground_hps_lta_uta_atch = get_object('.template_2_turn.ground.hps_lta_uta_atch').location
        gralin_9.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_uta_uc_atch, _template_2_turn_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_9.location, gralin_9.orientation)
        gralin_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_torque_arm.gralin_9', exc)

    try:
        jxs_joint_j_8 = get_object('.template_2_turn.ges_upper_torque_arm.jxs_joint_j_8')
        relative_to = get_object('.template_2_turn.ges_upper_torque_arm')
        jxs_joint_j_8.relative_to = relative_to
        jxs_joint_j_8.marker_name = target_path('.template_2_turn.ges_upper_torque_arm.jxs_joint_j_8')
        _template_2_turn_ground_hps_lta_uta_atch = get_object('.template_2_turn.ground.hps_lta_uta_atch')
        jxs_joint_j_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_lta_uta_atch))
        _template_2_turn_ground_origo = get_object('.template_2_turn.ground.origo')
        jxs_joint_j_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_2_turn_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_8.location, jxs_joint_j_8.orientation)
        jxs_joint_j_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_torque_arm.jxs_joint_j_8', exc)

    try:
        jxs_joint_i_10 = get_object('.template_2_turn.ges_upper_torque_arm.jxs_joint_i_10')
        relative_to = get_object('.template_2_turn.ges_upper_torque_arm')
        jxs_joint_i_10.relative_to = relative_to
        jxs_joint_i_10.marker_name = target_path('.template_2_turn.ges_upper_torque_arm.jxs_joint_i_10')
        _template_2_turn_ges_collar_jxs_joint_j_10 = get_object('.template_2_turn.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_collar_jxs_joint_j_10))
        _template_2_turn_ges_collar_jxs_joint_j_10 = get_object('.template_2_turn.ges_collar.jxs_joint_j_10')
        jxs_joint_i_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_collar_jxs_joint_j_10))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_10.location, jxs_joint_i_10.orientation)
        jxs_joint_i_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_upper_torque_arm.jxs_joint_i_10', exc)

    try:
        gralin_upper_torque_arm_geom = get_object('.template_2_turn.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        gralin_upper_torque_arm_geom.cylinder_name = target_path('.template_2_turn.ges_upper_torque_arm.gralin_upper_torque_arm_geom')
        _template_2_turn_ground_hps_uta_uc_atch = get_object('.template_2_turn.ground.hps_uta_uc_atch').location
        _template_2_turn_ground_hps_lta_uta_atch = get_object('.template_2_turn.ground.hps_lta_uta_atch').location
        gralin_upper_torque_arm_geom.length = (VecUtils.DM(_template_2_turn_ground_hps_uta_uc_atch, _template_2_turn_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.ges_upper_torque_arm.gralin_upper_torque_arm_geom', exc)

    try:
        inertia_frame = get_object('.template_2_turn.ges_lower_torque_arm.inertia_frame')
        relative_to = get_object('.template_2_turn.ges_lower_torque_arm')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_turn.ges_lower_torque_arm.inertia_frame')
        _template_2_turn_ges_lower_torque_arm_cm = get_object('.template_2_turn.ges_lower_torque_arm.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_lower_torque_arm_cm))
        _template_2_turn_ges_lower_torque_arm = get_object('.template_2_turn.ges_lower_torque_arm')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_lower_torque_arm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_torque_arm.inertia_frame', exc)

    try:
        jxs_joint_i_8 = get_object('.template_2_turn.ges_lower_torque_arm.jxs_joint_i_8')
        relative_to = get_object('.template_2_turn.ges_lower_torque_arm')
        jxs_joint_i_8.relative_to = relative_to
        jxs_joint_i_8.marker_name = target_path('.template_2_turn.ges_lower_torque_arm.jxs_joint_i_8')
        _template_2_turn_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_2_turn.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_torque_arm_jxs_joint_j_8))
        _template_2_turn_ges_upper_torque_arm_jxs_joint_j_8 = get_object('.template_2_turn.ges_upper_torque_arm.jxs_joint_j_8')
        jxs_joint_i_8.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_torque_arm_jxs_joint_j_8))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_8.location, jxs_joint_i_8.orientation)
        jxs_joint_i_8.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_8.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_torque_arm.jxs_joint_i_8', exc)

    try:
        gralin_10 = get_object('.template_2_turn.ges_lower_torque_arm.gralin_10')
        relative_to = get_object('.template_2_turn.ges_lower_torque_arm')
        gralin_10.relative_to = relative_to
        gralin_10.marker_name = target_path('.template_2_turn.ges_lower_torque_arm.gralin_10')
        _template_2_turn_ground_hps_lta_lc_atch = get_object('.template_2_turn.ground.hps_lta_lc_atch')
        gralin_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_lta_lc_atch))
        _template_2_turn_ground_hps_lta_lc_atch = get_object('.template_2_turn.ground.hps_lta_lc_atch').location
        _template_2_turn_ground_hps_lta_uta_atch = get_object('.template_2_turn.ground.hps_lta_uta_atch').location
        gralin_10.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_lta_lc_atch, _template_2_turn_ground_hps_lta_uta_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_10.location, gralin_10.orientation)
        gralin_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_torque_arm.gralin_10', exc)

    try:
        jxs_joint_i_9 = get_object('.template_2_turn.ges_lower_torque_arm.jxs_joint_i_9')
        relative_to = get_object('.template_2_turn.ges_lower_torque_arm')
        jxs_joint_i_9.relative_to = relative_to
        jxs_joint_i_9.marker_name = target_path('.template_2_turn.ges_lower_torque_arm.jxs_joint_i_9')
        _template_2_turn_ges_lower_cylinder_jxs_joint_j_9 = get_object('.template_2_turn.ges_lower_cylinder.jxs_joint_j_9')
        jxs_joint_i_9.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_lower_cylinder_jxs_joint_j_9))
        _template_2_turn_ges_lower_cylinder_jxs_joint_j_9 = get_object('.template_2_turn.ges_lower_cylinder.jxs_joint_j_9')
        jxs_joint_i_9.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_lower_cylinder_jxs_joint_j_9))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_9.location, jxs_joint_i_9.orientation)
        jxs_joint_i_9.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_9.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_lower_torque_arm.jxs_joint_i_9', exc)

    try:
        gralin_lower_torque_arm_geom = get_object('.template_2_turn.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        gralin_lower_torque_arm_geom.cylinder_name = target_path('.template_2_turn.ges_lower_torque_arm.gralin_lower_torque_arm_geom')
        _template_2_turn_ground_hps_lta_lc_atch = get_object('.template_2_turn.ground.hps_lta_lc_atch').location
        _template_2_turn_ground_hps_lta_uta_atch = get_object('.template_2_turn.ground.hps_lta_uta_atch').location
        gralin_lower_torque_arm_geom.length = (VecUtils.DM(_template_2_turn_ground_hps_lta_lc_atch, _template_2_turn_ground_hps_lta_uta_atch))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.ges_lower_torque_arm.gralin_lower_torque_arm_geom', exc)

    try:
        inertia_frame = get_object('.template_2_turn.ges_subframe.inertia_frame')
        relative_to = get_object('.template_2_turn.ges_subframe')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_turn.ges_subframe.inertia_frame')
        _template_2_turn_ges_subframe_cm = get_object('.template_2_turn.ges_subframe.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_subframe_cm))
        _template_2_turn_ges_subframe = get_object('.template_2_turn.ges_subframe')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_subframe))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_subframe.inertia_frame', exc)

    try:
        graout_1 = get_object('.template_2_turn.ges_subframe.graout_1')
        relative_to = get_object('.template_2_turn.ges_subframe')
        graout_1.relative_to = relative_to
        graout_1.marker_name = target_path('.template_2_turn.ges_subframe.graout_1')
        _template_2_turn_ground_hps_uc_sf_atch_r = get_object('.template_2_turn.ground.hps_uc_sf_atch_r')
        graout_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_sf_atch_r))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_1.location, graout_1.orientation)
        graout_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_subframe.graout_1', exc)

    try:
        graout_2 = get_object('.template_2_turn.ges_subframe.graout_2')
        relative_to = get_object('.template_2_turn.ges_subframe')
        graout_2.relative_to = relative_to
        graout_2.marker_name = target_path('.template_2_turn.ges_subframe.graout_2')
        _template_2_turn_ground_hps_uc_sf_atch_l = get_object('.template_2_turn.ground.hps_uc_sf_atch_l')
        graout_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_sf_atch_l))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_2.location, graout_2.orientation)
        graout_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_subframe.graout_2', exc)

    try:
        graout_3 = get_object('.template_2_turn.ges_subframe.graout_3')
        relative_to = get_object('.template_2_turn.ges_subframe')
        graout_3.relative_to = relative_to
        graout_3.marker_name = target_path('.template_2_turn.ges_subframe.graout_3')
        _template_2_turn_ground_hps_db_sf_atch = get_object('.template_2_turn.ground.hps_db_sf_atch')
        graout_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_db_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_3.location, graout_3.orientation)
        graout_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_subframe.graout_3', exc)

    try:
        jxs_joint_j_15 = get_object('.template_2_turn.ges_subframe.jxs_joint_j_15')
        relative_to = get_object('.template_2_turn.ges_subframe')
        jxs_joint_j_15.relative_to = relative_to
        jxs_joint_j_15.marker_name = target_path('.template_2_turn.ges_subframe.jxs_joint_j_15')
        _template_2_turn_ground_cfs_uc_sf_atch_mid = get_object('.template_2_turn.ground.cfs_uc_sf_atch_mid')
        jxs_joint_j_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_cfs_uc_sf_atch_mid))
        _template_2_turn_ground_cfs_uc_sf_atch_mid = get_object('.template_2_turn.ground.cfs_uc_sf_atch_mid')
        jxs_joint_j_15.orientation = _template_2_turn_ground_cfs_uc_sf_atch_mid.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_15.location, jxs_joint_j_15.orientation)
        jxs_joint_j_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_subframe.jxs_joint_j_15', exc)

    try:
        jxs_joint_j_14 = get_object('.template_2_turn.ges_subframe.jxs_joint_j_14')
        relative_to = get_object('.template_2_turn.ges_subframe')
        jxs_joint_j_14.relative_to = relative_to
        jxs_joint_j_14.marker_name = target_path('.template_2_turn.ges_subframe.jxs_joint_j_14')
        _template_2_turn_ground_hps_db_sf_atch = get_object('.template_2_turn.ground.hps_db_sf_atch')
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_db_sf_atch))
        _template_2_turn_ground_origo = get_object('.template_2_turn.ground.origo')
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_2_turn_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_subframe.jxs_joint_j_14', exc)

    try:
        mts_body_mount = get_object('.template_2_turn.mts_body_mount')
        mts_body_mount.part_name = target_path('.template_2_turn.mts_body_mount')
        _template_2_turn_ground_cfs_subframe_to_body_point = get_object('.template_2_turn.ground.cfs_subframe_to_body_point')
        mts_body_mount.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_cfs_subframe_to_body_point))
        _template_2_turn_ground_origo = get_object('.template_2_turn.ground.origo')
        mts_body_mount.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('part modify rigid_body name_and_position .template_2_turn.mts_body_mount', exc)

    try:
        jxs_joint_j_10 = get_object('.template_2_turn.ges_collar.jxs_joint_j_10')
        relative_to = get_object('.template_2_turn.ges_collar')
        jxs_joint_j_10.relative_to = relative_to
        jxs_joint_j_10.marker_name = target_path('.template_2_turn.ges_collar.jxs_joint_j_10')
        _template_2_turn_ground_hps_uta_uc_atch = get_object('.template_2_turn.ground.hps_uta_uc_atch')
        jxs_joint_j_10.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uta_uc_atch))
        _template_2_turn_ground_origo = get_object('.template_2_turn.ground.origo')
        jxs_joint_j_10.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_2_turn_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_10.location, jxs_joint_j_10.orientation)
        jxs_joint_j_10.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_10.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_collar.jxs_joint_j_10', exc)

    try:
        inertia_frame = get_object('.template_2_turn.ges_collar.inertia_frame')
        relative_to = get_object('.template_2_turn.ges_collar')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_turn.ges_collar.inertia_frame')
        _template_2_turn_ges_collar_cm = get_object('.template_2_turn.ges_collar.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_collar_cm))
        _template_2_turn_ges_collar = get_object('.template_2_turn.ges_collar')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_collar))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_collar.inertia_frame', exc)

    try:
        gralin_24 = get_object('.template_2_turn.ges_collar.gralin_24')
        relative_to = get_object('.template_2_turn.ges_collar')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_2_turn.ges_collar.gralin_24')
        _template_2_turn_ground_hps_uc_bot = get_object('.template_2_turn.ground.hps_uc_bot')
        gralin_24.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hps_uc_bot))
        _template_2_turn_ground_hps_uc_bot = get_object('.template_2_turn.ground.hps_uc_bot').location
        _template_2_turn_ground_cfs_collar_top = get_object('.template_2_turn.ground.cfs_collar_top').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hps_uc_bot, _template_2_turn_ground_cfs_collar_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_collar.gralin_24', exc)

    try:
        jxs_joint_i_1 = get_object('.template_2_turn.ges_collar.jxs_joint_i_1')
        relative_to = get_object('.template_2_turn.ges_collar')
        jxs_joint_i_1.relative_to = relative_to
        jxs_joint_i_1.marker_name = target_path('.template_2_turn.ges_collar.jxs_joint_i_1')
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_turn_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_turn.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
        jxs_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_collar.jxs_joint_i_1', exc)

    try:
        ues_actuator_i_1 = get_object('.template_2_turn.ges_collar.ues_actuator_i_1')
        relative_to = get_object('.template_2_turn.ges_collar')
        ues_actuator_i_1.relative_to = relative_to
        ues_actuator_i_1.marker_name = target_path('.template_2_turn.ges_collar.ues_actuator_i_1')
        _template_2_turn_ges_collar_jxs_joint_i_1 = get_object('.template_2_turn.ges_collar.jxs_joint_i_1')
        ues_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_collar_jxs_joint_i_1))
        _template_2_turn_ges_collar_jxs_joint_i_1 = get_object('.template_2_turn.ges_collar.jxs_joint_i_1')
        ues_actuator_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_collar_jxs_joint_i_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_1.location, ues_actuator_i_1.orientation)
        ues_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_collar.ues_actuator_i_1', exc)

    try:
        ues_actuator_i_4 = get_object('.template_2_turn.ges_collar.ues_actuator_i_4')
        relative_to = get_object('.template_2_turn.ges_collar')
        ues_actuator_i_4.relative_to = relative_to
        ues_actuator_i_4.marker_name = target_path('.template_2_turn.ges_collar.ues_actuator_i_4')
        _template_2_turn_ges_collar_jxs_joint_i_1 = get_object('.template_2_turn.ges_collar.jxs_joint_i_1')
        ues_actuator_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_collar_jxs_joint_i_1))
        _template_2_turn_ges_collar_jxs_joint_i_1 = get_object('.template_2_turn.ges_collar.jxs_joint_i_1')
        ues_actuator_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ges_collar_jxs_joint_i_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_4.location, ues_actuator_i_4.orientation)
        ues_actuator_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_collar.ues_actuator_i_4', exc)

    try:
        gralin_collar = get_object('.template_2_turn.ges_collar.gralin_collar')
        gralin_collar.cylinder_name = target_path('.template_2_turn.ges_collar.gralin_collar')
        _template_2_turn_ground_hps_uc_bot = get_object('.template_2_turn.ground.hps_uc_bot').location
        _template_2_turn_ground_cfs_collar_top = get_object('.template_2_turn.ground.cfs_collar_top').location
        gralin_collar.length = (VecUtils.DM(_template_2_turn_ground_hps_uc_bot, _template_2_turn_ground_cfs_collar_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.ges_collar.gralin_collar', exc)

    try:
        MARKER_75 = get_object('.template_2_turn.ges_collar.MARKER_75')
        relative_to = get_object('.template_2_turn.ges_collar')
        MARKER_75.relative_to = relative_to
        MARKER_75.marker_name = target_path('.template_2_turn.ges_collar.MARKER_75')
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1')
        MARKER_75.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hsg_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_75.location, MARKER_75.orientation)
        MARKER_75.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.ges_collar.MARKER_75', exc)

    try:
        gralin_73 = get_object('.template_2_turn.hsg.gralin_73')
        relative_to = get_object('.template_2_turn.hsg')
        gralin_73.relative_to = relative_to
        gralin_73.marker_name = target_path('.template_2_turn.hsg.gralin_73')
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1')
        gralin_73.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hsg_1))
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_hsg_2 = get_object('.template_2_turn.ground.hsg_2').location
        gralin_73.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hsg_1, _template_2_turn_ground_hsg_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_73.location, gralin_73.orientation)
        gralin_73.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_73.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.hsg.gralin_73', exc)

    try:
        CYLINDER_50 = get_object('.template_2_turn.hsg.CYLINDER_50')
        CYLINDER_50.cylinder_name = target_path('.template_2_turn.hsg.CYLINDER_50')
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_hsg_2 = get_object('.template_2_turn.ground.hsg_2').location
        CYLINDER_50.length = (VecUtils.DM(_template_2_turn_ground_hsg_1, _template_2_turn_ground_hsg_2))
        CYLINDER_50.radius = 15.084427744


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.hsg.CYLINDER_50', exc)

    try:
        MARKER_76 = get_object('.template_2_turn.hsg.MARKER_76')
        relative_to = get_object('.template_2_turn.hsg')
        MARKER_76.relative_to = relative_to
        MARKER_76.marker_name = target_path('.template_2_turn.hsg.MARKER_76')
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1')
        MARKER_76.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hsg_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_76.location, MARKER_76.orientation)
        MARKER_76.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.hsg.MARKER_76', exc)

    try:
        MARKER_81 = get_object('.template_2_turn.hsg.MARKER_81')
        relative_to = get_object('.template_2_turn.hsg')
        MARKER_81.relative_to = relative_to
        MARKER_81.marker_name = target_path('.template_2_turn.hsg.MARKER_81')
        _template_2_turn_hsg_cm = get_object('.template_2_turn.hsg.cm')
        MARKER_81.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_hsg_cm))
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_zdt1 = get_object('.template_2_turn.ground.zdt1').location
        MARKER_81.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hsg_1, _template_2_turn_ground_zdt1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_81.location, MARKER_81.orientation)
        MARKER_81.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_81.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.hsg.MARKER_81', exc)

    try:
        MARKER_82 = get_object('.template_2_turn.hsg.MARKER_82')
        relative_to = get_object('.template_2_turn.hsg')
        MARKER_82.relative_to = relative_to
        MARKER_82.marker_name = target_path('.template_2_turn.hsg.MARKER_82')
        _template_2_turn_hsg_cm = get_object('.template_2_turn.hsg.cm')
        MARKER_82.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_hsg_cm))
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_zdt1 = get_object('.template_2_turn.ground.zdt1').location
        MARKER_82.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hsg_1, _template_2_turn_ground_zdt1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_82.location, MARKER_82.orientation)
        MARKER_82.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_82.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.hsg.MARKER_82', exc)

    try:
        MARKER_85 = get_object('.template_2_turn.hsg.MARKER_85')
        relative_to = get_object('.template_2_turn.hsg')
        MARKER_85.relative_to = relative_to
        MARKER_85.marker_name = target_path('.template_2_turn.hsg.MARKER_85')
        _template_2_turn_zdt_cm = get_object('.template_2_turn.zdt.cm')
        MARKER_85.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_zdt_cm))
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_zdt1 = get_object('.template_2_turn.ground.zdt1').location
        MARKER_85.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hsg_1, _template_2_turn_ground_zdt1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_85.location, MARKER_85.orientation)
        MARKER_85.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_85.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.hsg.MARKER_85', exc)

    try:
        gralin_74 = get_object('.template_2_turn.zdt.gralin_74')
        relative_to = get_object('.template_2_turn.zdt')
        gralin_74.relative_to = relative_to
        gralin_74.marker_name = target_path('.template_2_turn.zdt.gralin_74')
        _template_2_turn_ground_zdt1 = get_object('.template_2_turn.ground.zdt1')
        gralin_74.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_zdt1))
        _template_2_turn_ground_zdt1 = get_object('.template_2_turn.ground.zdt1').location
        _template_2_turn_ground_zdt2 = get_object('.template_2_turn.ground.zdt2').location
        gralin_74.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_zdt1, _template_2_turn_ground_zdt2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_74.location, gralin_74.orientation)
        gralin_74.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_74.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.zdt.gralin_74', exc)

    try:
        CYLINDER_51 = get_object('.template_2_turn.zdt.CYLINDER_51')
        CYLINDER_51.cylinder_name = target_path('.template_2_turn.zdt.CYLINDER_51')
        _template_2_turn_ground_zdt1 = get_object('.template_2_turn.ground.zdt1').location
        _template_2_turn_ground_zdt2 = get_object('.template_2_turn.ground.zdt2').location
        CYLINDER_51.length = (VecUtils.DM(_template_2_turn_ground_zdt1, _template_2_turn_ground_zdt2))
        CYLINDER_51.radius = 33.4634781504


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_turn.zdt.CYLINDER_51', exc)

    try:
        MARKER_78 = get_object('.template_2_turn.zdt.MARKER_78')
        relative_to = get_object('.template_2_turn.zdt')
        MARKER_78.relative_to = relative_to
        MARKER_78.marker_name = target_path('.template_2_turn.zdt.MARKER_78')
        _template_2_turn_ground_zdt1 = get_object('.template_2_turn.ground.zdt1')
        MARKER_78.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_zdt1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_78.location, MARKER_78.orientation)
        MARKER_78.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.zdt.MARKER_78', exc)

    try:
        MARKER_86 = get_object('.template_2_turn.zdt.MARKER_86')
        relative_to = get_object('.template_2_turn.zdt')
        MARKER_86.relative_to = relative_to
        MARKER_86.marker_name = target_path('.template_2_turn.zdt.MARKER_86')
        _template_2_turn_zdt_cm = get_object('.template_2_turn.zdt.cm')
        MARKER_86.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_zdt_cm))
        _template_2_turn_ground_hsg_1 = get_object('.template_2_turn.ground.hsg_1').location
        _template_2_turn_ground_zdt1 = get_object('.template_2_turn.ground.zdt1').location
        MARKER_86.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_turn_ground_hsg_1, _template_2_turn_ground_zdt1, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_86.location, MARKER_86.orientation)
        MARKER_86.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_86.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.zdt.MARKER_86', exc)

    try:
        MARKER_117 = get_object('.template_2_turn.js.MARKER_117')
        relative_to = get_object('.template_2_turn.js')
        MARKER_117.relative_to = relative_to
        MARKER_117.marker_name = target_path('.template_2_turn.js.MARKER_117')
        _template_2_turn_ground_hps_uc_top = get_object('.template_2_turn.ground.hps_uc_top')
        MARKER_117.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 200.0], _template_2_turn_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_117.location, MARKER_117.orientation)
        MARKER_117.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.js.MARKER_117', exc)

    try:
        MARKER_157 = get_object('.template_2_turn.lt_l.wheel_part.MARKER_157')
        relative_to = get_object('.template_2_turn.lt_l.wheel_part')
        MARKER_157.relative_to = relative_to
        MARKER_157.marker_name = target_path('.template_2_turn.lt_l.wheel_part.MARKER_157')
        _template_2_turn_ground_hpl_wheel_center = get_object('.template_2_turn.ground.hpl_wheel_center')
        MARKER_157.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hpl_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_157.location, MARKER_157.orientation)
        MARKER_157.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.lt_l.wheel_part.MARKER_157', exc)

    try:
        gfo_i = get_object('.template_2_turn.lt_l.wheel_part.gfo_i')
        relative_to = get_object('.template_2_turn.lt_l.wheel_part')
        gfo_i.relative_to = relative_to
        gfo_i.marker_name = target_path('.template_2_turn.lt_l.wheel_part.gfo_i')
        _template_2_turn_lt_l_wheel_part_wheel_cm = get_object('.template_2_turn.lt_l.wheel_part.wheel_cm')
        gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _template_2_turn_lt_l_wheel_part_wheel_cm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
        gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.lt_l.wheel_part.gfo_i', exc)

    try:
        MARKER_159 = get_object('.template_2_turn.lt_r.wheel_part.MARKER_159')
        relative_to = get_object('.template_2_turn.lt_r.wheel_part')
        MARKER_159.relative_to = relative_to
        MARKER_159.marker_name = target_path('.template_2_turn.lt_r.wheel_part.MARKER_159')
        _template_2_turn_ground_hpr_wheel_center = get_object('.template_2_turn.ground.hpr_wheel_center')
        MARKER_159.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_turn_ground_hpr_wheel_center))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_159.location, MARKER_159.orientation)
        MARKER_159.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.lt_r.wheel_part.MARKER_159', exc)

    try:
        gfo_i = get_object('.template_2_turn.lt_r.wheel_part.gfo_i')
        relative_to = get_object('.template_2_turn.lt_r.wheel_part')
        gfo_i.relative_to = relative_to
        gfo_i.marker_name = target_path('.template_2_turn.lt_r.wheel_part.gfo_i')
        _template_2_turn_lt_r_wheel_part_wheel_cm = get_object('.template_2_turn.lt_r.wheel_part.wheel_cm')
        gfo_i.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 270.0, 0.0], _template_2_turn_lt_r_wheel_part_wheel_cm))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gfo_i.location, gfo_i.orientation)
        gfo_i.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gfo_i.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_turn.lt_r.wheel_part.gfo_i', exc)

    if model_dir is None:
        model_dir = os.path.dirname(os.path.abspath(__file__))
    resource_path_1 = os.path.abspath(os.path.join(model_dir, 'uat_1.tir'))
    if not os.path.isfile(resource_path_1):
        record_error('轮胎文件路径（uat_1.tir）', FileNotFoundError(resource_path_1))
    else:
        try:
            if set_resource('.template_2_turn.lt_l.tpf_file', resource_path_1):
                updated += 1
        except Exception as exc:
            record_error('轮胎文件路径（uat_1.tir）', exc)
    resource_path_2 = os.path.abspath(os.path.join(model_dir, '2d_flat.rdf'))
    if not os.path.isfile(resource_path_2):
        record_error('路面文件路径（2d_flat.rdf）', FileNotFoundError(resource_path_2))
    else:
        try:
            if set_resource('.template_2_turn.lt_l.rpf_file', resource_path_2):
                updated += 1
        except Exception as exc:
            record_error('路面文件路径（2d_flat.rdf）', exc)
    resource_path_3 = os.path.abspath(os.path.join(model_dir, 'uat_1.tir'))
    if not os.path.isfile(resource_path_3):
        record_error('轮胎文件路径（uat_1.tir）', FileNotFoundError(resource_path_3))
    else:
        try:
            if set_resource('.template_2_turn.lt_r.tpf_file', resource_path_3):
                updated += 1
        except Exception as exc:
            record_error('轮胎文件路径（uat_1.tir）', exc)
    resource_path_4 = os.path.abspath(os.path.join(model_dir, '2d_flat.rdf'))
    if not os.path.isfile(resource_path_4):
        record_error('路面文件路径（2d_flat.rdf）', FileNotFoundError(resource_path_4))
    else:
        try:
            if set_resource('.template_2_turn.lt_r.rpf_file', resource_path_4):
                updated += 1
        except Exception as exc:
            record_error('路面文件路径（2d_flat.rdf）', exc)
    return {'updated': updated, 'warnings': warnings, 'errors': errors}

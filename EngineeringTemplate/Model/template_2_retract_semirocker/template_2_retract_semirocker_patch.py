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

SOURCE_MODEL_NAME = 'template_2_retract_semirocker'
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
        node = get_or_create('SimuScript', '.template_2_retract_semirocker.Last_Sim')
        if hasattr(node, 'sim_script_name'):
            node.sim_script_name = target_path('.template_2_retract_semirocker.Last_Sim')
        node.commands = rewrite_simulation_command('simulation single_run transient type=auto_select initial_static=no end_time=5.0 number_of_steps=500 model_name=._AA_nlg_post_2hubs')
        updated += 1

    except Exception as exc:
        record_error('simulation script create .template_2_retract_semirocker.Last_Sim', exc)

    try:
        node = get_object('.template_2_retract_semirocker.MOTION_1')
        node.function = rewrite_expression('STEP( time , 0 , 0 , 1 , -635 )-STEP( time , 2 , 0 , 3, -635 )')
        updated += 1

    except Exception as exc:
        record_error('constraint modify motion_generator .template_2_retract_semirocker.MOTION_1', exc)

    try:
        node = get_object('.template_2_retract_semirocker.SFORCE_1')
        node.function = rewrite_expression('-100.0*(DM(.template_2_retract_semirocker.ges_upper_cylinder.MARKER_69,.template_2_retract_semirocker.ges_lower_cylinder.MARKER_70)-25.0)-10.0*VR(.template_2_retract_semirocker.ges_upper_cylinder.MARKER_69,.template_2_retract_semirocker.ges_lower_cylinder.MARKER_70)')
        updated += 1

    except Exception as exc:
        record_error('force modify direct single_component_force .template_2_retract_semirocker.SFORCE_1', exc)

    try:
        mts_mount_j_2 = get_object('.template_2_retract_semirocker.ground.mts_mount_j_2')
        mts_mount_j_2.marker_name = target_path('.template_2_retract_semirocker.ground.mts_mount_j_2')
        _template_2_retract_semirocker_mts_body_mount = get_object('.template_2_retract_semirocker.mts_body_mount')
        mts_mount_j_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_mts_body_mount))
        _template_2_retract_semirocker_mts_body_mount = get_object('.template_2_retract_semirocker.mts_body_mount')
        mts_mount_j_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_mts_body_mount))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ground.mts_mount_j_2', exc)

    try:
        cfs_collar_top = get_object('.template_2_retract_semirocker.ground.cfs_collar_top')
        cfs_collar_top.marker_name = target_path('.template_2_retract_semirocker.ground.cfs_collar_top')
        _template_2_retract_semirocker_ground_hps_uc_bot = get_object('.template_2_retract_semirocker.ground.hps_uc_bot').location
        _template_2_retract_semirocker_ground_hps_uc_top = get_object('.template_2_retract_semirocker.ground.hps_uc_top').location
        cfs_collar_top.location = (VecUtils.LOC_ALONG_LINE(_template_2_retract_semirocker_ground_hps_uc_bot, _template_2_retract_semirocker_ground_hps_uc_top, 0.11 * VecUtils.DM(_template_2_retract_semirocker_ground_hps_uc_bot, _template_2_retract_semirocker_ground_hps_uc_top)))
        _template_2_retract_semirocker_ground_hps_uc_bot = get_object('.template_2_retract_semirocker.ground.hps_uc_bot').location
        _template_2_retract_semirocker_ground_hps_uc_top = get_object('.template_2_retract_semirocker.ground.hps_uc_top').location
        cfs_collar_top.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_uc_bot, _template_2_retract_semirocker_ground_hps_uc_top, "Z"))


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ground.cfs_collar_top', exc)

    try:
        inertia_frame = get_object('.template_2_retract_semirocker.ges_dragbrace.inertia_frame')
        relative_to = get_object('.template_2_retract_semirocker.ges_dragbrace')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_retract_semirocker.ges_dragbrace.inertia_frame')
        _template_2_retract_semirocker_ges_dragbrace_cm = get_object('.template_2_retract_semirocker.ges_dragbrace.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_dragbrace_cm))
        _template_2_retract_semirocker_ges_dragbrace = get_object('.template_2_retract_semirocker.ges_dragbrace')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_dragbrace))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_dragbrace.inertia_frame', exc)

    try:
        gralin_1 = get_object('.template_2_retract_semirocker.ges_dragbrace.gralin_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_dragbrace')
        gralin_1.relative_to = relative_to
        gralin_1.marker_name = target_path('.template_2_retract_semirocker.ges_dragbrace.gralin_1')
        _template_2_retract_semirocker_ground_hps_db_sf_atch = get_object('.template_2_retract_semirocker.ground.hps_db_sf_atch')
        gralin_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_db_sf_atch))
        _template_2_retract_semirocker_ground_hps_db_sf_atch = get_object('.template_2_retract_semirocker.ground.hps_db_sf_atch').location
        _template_2_retract_semirocker_ground_hps_db_uc_atch = get_object('.template_2_retract_semirocker.ground.hps_db_uc_atch').location
        gralin_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_db_sf_atch, _template_2_retract_semirocker_ground_hps_db_uc_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_1.location, gralin_1.orientation)
        gralin_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_dragbrace.gralin_1', exc)

    try:
        jxs_joint_i_14 = get_object('.template_2_retract_semirocker.ges_dragbrace.jxs_joint_i_14')
        relative_to = get_object('.template_2_retract_semirocker.ges_dragbrace')
        jxs_joint_i_14.relative_to = relative_to
        jxs_joint_i_14.marker_name = target_path('.template_2_retract_semirocker.ges_dragbrace.jxs_joint_i_14')
        _template_2_retract_semirocker_ges_subframe_jxs_joint_j_14 = get_object('.template_2_retract_semirocker.ges_subframe.jxs_joint_j_14')
        jxs_joint_i_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_subframe_jxs_joint_j_14))
        _template_2_retract_semirocker_ges_subframe_jxs_joint_j_14 = get_object('.template_2_retract_semirocker.ges_subframe.jxs_joint_j_14')
        jxs_joint_i_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_subframe_jxs_joint_j_14))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_14.location, jxs_joint_i_14.orientation)
        jxs_joint_i_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_dragbrace.jxs_joint_i_14', exc)

    try:
        gralin_dragbrace_geom = get_object('.template_2_retract_semirocker.ges_dragbrace.gralin_dragbrace_geom')
        gralin_dragbrace_geom.cylinder_name = target_path('.template_2_retract_semirocker.ges_dragbrace.gralin_dragbrace_geom')
        _template_2_retract_semirocker_ground_hps_db_sf_atch = get_object('.template_2_retract_semirocker.ground.hps_db_sf_atch').location
        _template_2_retract_semirocker_ground_hps_db_uc_atch = get_object('.template_2_retract_semirocker.ground.hps_db_uc_atch').location
        gralin_dragbrace_geom.length = (VecUtils.DM(_template_2_retract_semirocker_ground_hps_db_sf_atch, _template_2_retract_semirocker_ground_hps_db_uc_atch) - 100.0)


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract_semirocker.ges_dragbrace.gralin_dragbrace_geom', exc)

    try:
        inertia_frame = get_object('.template_2_retract_semirocker.ges_upper_cylinder.inertia_frame')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.inertia_frame')
        _template_2_retract_semirocker_ges_upper_cylinder_cm = get_object('.template_2_retract_semirocker.ges_upper_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder_cm))
        _template_2_retract_semirocker_ges_upper_cylinder = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.inertia_frame', exc)

    try:
        gralin_2 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.gralin_2')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        gralin_2.relative_to = relative_to
        gralin_2.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.gralin_2')
        _template_2_retract_semirocker_ground_hps_uc_top = get_object('.template_2_retract_semirocker.ground.hps_uc_top')
        gralin_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_uc_top))
        _template_2_retract_semirocker_ground_hps_uc_top = get_object('.template_2_retract_semirocker.ground.hps_uc_top').location
        _template_2_retract_semirocker_ground_hps_uc_bot = get_object('.template_2_retract_semirocker.ground.hps_uc_bot').location
        gralin_2.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_uc_top, _template_2_retract_semirocker_ground_hps_uc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_2.location, gralin_2.orientation)
        gralin_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.gralin_2', exc)

    try:
        gralin_3 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.gralin_3')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        gralin_3.relative_to = relative_to
        gralin_3.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.gralin_3')
        _template_2_retract_semirocker_ground_hps_uc_sf_atch_l = get_object('.template_2_retract_semirocker.ground.hps_uc_sf_atch_l')
        gralin_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_uc_sf_atch_l))
        _template_2_retract_semirocker_ground_hps_uc_sf_atch_l = get_object('.template_2_retract_semirocker.ground.hps_uc_sf_atch_l').location
        _template_2_retract_semirocker_ground_hps_uc_geompt = get_object('.template_2_retract_semirocker.ground.hps_uc_geompt').location
        gralin_3.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_uc_sf_atch_l, _template_2_retract_semirocker_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_3.location, gralin_3.orientation)
        gralin_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_3.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.gralin_3', exc)

    try:
        gralin_4 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.gralin_4')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        gralin_4.relative_to = relative_to
        gralin_4.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.gralin_4')
        _template_2_retract_semirocker_ground_hps_uc_sf_atch_r = get_object('.template_2_retract_semirocker.ground.hps_uc_sf_atch_r')
        gralin_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_uc_sf_atch_r))
        _template_2_retract_semirocker_ground_hps_uc_sf_atch_r = get_object('.template_2_retract_semirocker.ground.hps_uc_sf_atch_r').location
        _template_2_retract_semirocker_ground_hps_uc_geompt = get_object('.template_2_retract_semirocker.ground.hps_uc_geompt').location
        gralin_4.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_uc_sf_atch_r, _template_2_retract_semirocker_ground_hps_uc_geompt, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_4.location, gralin_4.orientation)
        gralin_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.gralin_4', exc)

    try:
        jxs_joint_i_15 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_i_15')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        jxs_joint_i_15.relative_to = relative_to
        jxs_joint_i_15.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_i_15')
        _template_2_retract_semirocker_ges_subframe_jxs_joint_j_15 = get_object('.template_2_retract_semirocker.ges_subframe.jxs_joint_j_15')
        jxs_joint_i_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_subframe_jxs_joint_j_15))
        _template_2_retract_semirocker_ges_subframe_jxs_joint_j_15 = get_object('.template_2_retract_semirocker.ges_subframe.jxs_joint_j_15')
        jxs_joint_i_15.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_subframe_jxs_joint_j_15))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_15.location, jxs_joint_i_15.orientation)
        jxs_joint_i_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_i_15', exc)

    try:
        ues_spring_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.ues_spring_j_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        ues_spring_j_1.relative_to = relative_to
        ues_spring_j_1.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.ues_spring_j_1')
        _template_2_retract_semirocker_ground_hps_uc_top = get_object('.template_2_retract_semirocker.ground.hps_uc_top')
        ues_spring_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_j_1.location, ues_spring_j_1.orientation)
        ues_spring_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.ues_spring_j_1', exc)

    try:
        ues_damper_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.ues_damper_j_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        ues_damper_j_1.relative_to = relative_to
        ues_damper_j_1.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.ues_damper_j_1')
        _template_2_retract_semirocker_ground_hps_uc_top = get_object('.template_2_retract_semirocker.ground.hps_uc_top')
        ues_damper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_j_1.location, ues_damper_j_1.orientation)
        ues_damper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.ues_damper_j_1', exc)

    try:
        ues_stopper_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.ues_stopper_j_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        ues_stopper_j_1.relative_to = relative_to
        ues_stopper_j_1.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.ues_stopper_j_1')
        _template_2_retract_semirocker_ground_hps_uc_top = get_object('.template_2_retract_semirocker.ground.hps_uc_top')
        ues_stopper_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_uc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_j_1.location, ues_stopper_j_1.orientation)
        ues_stopper_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.ues_stopper_j_1', exc)

    try:
        jxs_joint_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        jxs_joint_j_1.relative_to = relative_to
        jxs_joint_j_1.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1')
        _template_2_retract_semirocker_ground_cfs_collar_top = get_object('.template_2_retract_semirocker.ground.cfs_collar_top')
        jxs_joint_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_cfs_collar_top))
        _template_2_retract_semirocker_ground_hps_uc_bot = get_object('.template_2_retract_semirocker.ground.hps_uc_bot').location
        _template_2_retract_semirocker_ground_hps_uc_top = get_object('.template_2_retract_semirocker.ground.hps_uc_top').location
        jxs_joint_j_1.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_uc_bot, _template_2_retract_semirocker_ground_hps_uc_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_1.location, jxs_joint_j_1.orientation)
        jxs_joint_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1', exc)

    try:
        ues_actuator_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        ues_actuator_j_1.relative_to = relative_to
        ues_actuator_j_1.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_1')
        _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_1.location, ues_actuator_j_1.orientation)
        ues_actuator_j_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_j_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_1', exc)

    try:
        ues_actuator_j_4 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_4')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        ues_actuator_j_4.relative_to = relative_to
        ues_actuator_j_4.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_4')
        _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1')
        ues_actuator_j_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_j_4.location, ues_actuator_j_4.orientation)
        ues_actuator_j_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_j_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.ues_actuator_j_4', exc)

    try:
        gralin_upper_cylinder_geom1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        gralin_upper_cylinder_geom1.cylinder_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom1')
        _template_2_retract_semirocker_ground_hps_uc_top = get_object('.template_2_retract_semirocker.ground.hps_uc_top').location
        _template_2_retract_semirocker_ground_hps_uc_bot = get_object('.template_2_retract_semirocker.ground.hps_uc_bot').location
        gralin_upper_cylinder_geom1.length = (VecUtils.DM(_template_2_retract_semirocker_ground_hps_uc_top, _template_2_retract_semirocker_ground_hps_uc_bot))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom1', exc)

    try:
        gralin_upper_cylinder_geom2 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        gralin_upper_cylinder_geom2.cylinder_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom2')
        _template_2_retract_semirocker_ground_hps_uc_sf_atch_l = get_object('.template_2_retract_semirocker.ground.hps_uc_sf_atch_l').location
        _template_2_retract_semirocker_ground_hps_uc_geompt = get_object('.template_2_retract_semirocker.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom2.length = (VecUtils.DM(_template_2_retract_semirocker_ground_hps_uc_sf_atch_l, _template_2_retract_semirocker_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom2', exc)

    try:
        gralin_upper_cylinder_geom3 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        gralin_upper_cylinder_geom3.cylinder_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom3')
        _template_2_retract_semirocker_ground_hps_uc_sf_atch_r = get_object('.template_2_retract_semirocker.ground.hps_uc_sf_atch_r').location
        _template_2_retract_semirocker_ground_hps_uc_geompt = get_object('.template_2_retract_semirocker.ground.hps_uc_geompt').location
        gralin_upper_cylinder_geom3.length = (VecUtils.DM(_template_2_retract_semirocker_ground_hps_uc_sf_atch_r, _template_2_retract_semirocker_ground_hps_uc_geompt))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract_semirocker.ges_upper_cylinder.gralin_upper_cylinder_geom3', exc)

    try:
        MARKER_69 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.MARKER_69')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        MARKER_69.relative_to = relative_to
        MARKER_69.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.MARKER_69')
        _template_2_retract_semirocker_ground_hps_lc_top = get_object('.template_2_retract_semirocker.ground.hps_lc_top')
        MARKER_69.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_69.location, MARKER_69.orientation)
        MARKER_69.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.MARKER_69', exc)

    try:
        MARKER_97 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.MARKER_97')
        relative_to = get_object('.template_2_retract_semirocker.ges_upper_cylinder')
        MARKER_97.relative_to = relative_to
        MARKER_97.marker_name = target_path('.template_2_retract_semirocker.ges_upper_cylinder.MARKER_97')
        _template_2_retract_semirocker_ground_hps_db_uc_atch = get_object('.template_2_retract_semirocker.ground.hps_db_uc_atch')
        MARKER_97.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_db_uc_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_97.location, MARKER_97.orientation)
        MARKER_97.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_upper_cylinder.MARKER_97', exc)

    try:
        inertia_frame = get_object('.template_2_retract_semirocker.ges_lower_cylinder.inertia_frame')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.inertia_frame')
        _template_2_retract_semirocker_ges_lower_cylinder_cm = get_object('.template_2_retract_semirocker.ges_lower_cylinder.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_lower_cylinder_cm))
        _template_2_retract_semirocker_ges_lower_cylinder = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_lower_cylinder))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.inertia_frame', exc)

    try:
        gralin_5 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.gralin_5')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        gralin_5.relative_to = relative_to
        gralin_5.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.gralin_5')
        _template_2_retract_semirocker_ground_hps_lc_top = get_object('.template_2_retract_semirocker.ground.hps_lc_top')
        gralin_5.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_lc_top))
        _template_2_retract_semirocker_ground_hps_lc_top = get_object('.template_2_retract_semirocker.ground.hps_lc_top').location
        _template_2_retract_semirocker_ground_hps_lc_bot = get_object('.template_2_retract_semirocker.ground.hps_lc_bot').location
        gralin_5.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_lc_top, _template_2_retract_semirocker_ground_hps_lc_bot, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_5.location, gralin_5.orientation)
        gralin_5.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_5.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.gralin_5', exc)

    try:
        jxs_joint_i_11 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.jxs_joint_i_11')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        jxs_joint_i_11.relative_to = relative_to
        jxs_joint_i_11.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.jxs_joint_i_11')
        _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_11))
        _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_11 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_11')
        jxs_joint_i_11.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_11))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_11.location, jxs_joint_i_11.orientation)
        jxs_joint_i_11.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_11.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.jxs_joint_i_11', exc)

    try:
        ues_spring_i_1 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.ues_spring_i_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        ues_spring_i_1.relative_to = relative_to
        ues_spring_i_1.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.ues_spring_i_1')
        _template_2_retract_semirocker_ground_hps_lc_top = get_object('.template_2_retract_semirocker.ground.hps_lc_top')
        ues_spring_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_spring_i_1.location, ues_spring_i_1.orientation)
        ues_spring_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.ues_spring_i_1', exc)

    try:
        ues_damper_i_1 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.ues_damper_i_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        ues_damper_i_1.relative_to = relative_to
        ues_damper_i_1.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.ues_damper_i_1')
        _template_2_retract_semirocker_ground_hps_lc_top = get_object('.template_2_retract_semirocker.ground.hps_lc_top')
        ues_damper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_damper_i_1.location, ues_damper_i_1.orientation)
        ues_damper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.ues_damper_i_1', exc)

    try:
        ues_stopper_i_1 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.ues_stopper_i_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        ues_stopper_i_1.relative_to = relative_to
        ues_stopper_i_1.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.ues_stopper_i_1')
        _template_2_retract_semirocker_ground_hps_lc_top = get_object('.template_2_retract_semirocker.ground.hps_lc_top')
        ues_stopper_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_lc_top))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_stopper_i_1.location, ues_stopper_i_1.orientation)
        ues_stopper_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.ues_stopper_i_1', exc)

    try:
        coomarker_2 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.coomarker_2')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        coomarker_2.relative_to = relative_to
        coomarker_2.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.coomarker_2')
        _template_2_retract_semirocker_ground_cfs_wheel_centers_midpoint = get_object('.template_2_retract_semirocker.ground.cfs_wheel_centers_midpoint')
        coomarker_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_cfs_wheel_centers_midpoint))
        _template_2_retract_semirocker_ground_cfs_wheel_centers_midpoint = get_object('.template_2_retract_semirocker.ground.cfs_wheel_centers_midpoint')
        coomarker_2.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_cfs_wheel_centers_midpoint))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, coomarker_2.location, coomarker_2.orientation)
        coomarker_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        coomarker_2.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.coomarker_2', exc)

    try:
        gralin_geom1 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.gralin_geom1')
        gralin_geom1.cylinder_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.gralin_geom1')
        _template_2_retract_semirocker_ground_hps_lc_top = get_object('.template_2_retract_semirocker.ground.hps_lc_top').location
        _template_2_retract_semirocker_ground_hps_lc_bot = get_object('.template_2_retract_semirocker.ground.hps_lc_bot').location
        gralin_geom1.length = (VecUtils.DM(_template_2_retract_semirocker_ground_hps_lc_top, _template_2_retract_semirocker_ground_hps_lc_bot) + 30.0)


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract_semirocker.ges_lower_cylinder.gralin_geom1', exc)

    try:
        MARKER_70 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.MARKER_70')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        MARKER_70.relative_to = relative_to
        MARKER_70.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.MARKER_70')
        _template_2_retract_semirocker_ground_hps_uc_bot = get_object('.template_2_retract_semirocker.ground.hps_uc_bot')
        MARKER_70.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_uc_bot))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_70.location, MARKER_70.orientation)
        MARKER_70.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.MARKER_70', exc)

    try:
        MARKER_71 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.MARKER_71')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        MARKER_71.relative_to = relative_to
        MARKER_71.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.MARKER_71')
        _template_2_retract_semirocker_ground_hps_lb_uc_atch = get_object('.template_2_retract_semirocker.ground.hps_lb_uc_atch')
        MARKER_71.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_lb_uc_atch))
        _template_2_retract_semirocker_ground_hps_lb_uc_atch = get_object('.template_2_retract_semirocker.ground.hps_lb_uc_atch').location
        _template_2_retract_semirocker_ground_POINT_12 = get_object('.template_2_retract_semirocker.ground.POINT_12').location
        MARKER_71.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_lb_uc_atch, _template_2_retract_semirocker_ground_POINT_12, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_71.location, MARKER_71.orientation)
        MARKER_71.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_71.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.MARKER_71', exc)

    try:
        CYLINDER_14 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.CYLINDER_14')
        CYLINDER_14.cylinder_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.CYLINDER_14')
        CYLINDER_14.length = 155.71520440843997


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract_semirocker.ges_lower_cylinder.CYLINDER_14', exc)

    try:
        MARKER_82 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.MARKER_82')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        MARKER_82.relative_to = relative_to
        MARKER_82.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.MARKER_82')
        _template_2_retract_semirocker_ground_POINT_12 = get_object('.template_2_retract_semirocker.ground.POINT_12')
        MARKER_82.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_POINT_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_82.location, MARKER_82.orientation)
        MARKER_82.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.MARKER_82', exc)

    try:
        MARKER_89 = get_object('.template_2_retract_semirocker.ges_lower_cylinder.MARKER_89')
        relative_to = get_object('.template_2_retract_semirocker.ges_lower_cylinder')
        MARKER_89.relative_to = relative_to
        MARKER_89.marker_name = target_path('.template_2_retract_semirocker.ges_lower_cylinder.MARKER_89')
        _template_2_retract_semirocker_ground_POINT_27 = get_object('.template_2_retract_semirocker.ground.POINT_27')
        MARKER_89.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_POINT_27))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_89.location, MARKER_89.orientation)
        MARKER_89.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_lower_cylinder.MARKER_89', exc)

    try:
        inertia_frame = get_object('.template_2_retract_semirocker.ges_subframe.inertia_frame')
        relative_to = get_object('.template_2_retract_semirocker.ges_subframe')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_retract_semirocker.ges_subframe.inertia_frame')
        _template_2_retract_semirocker_ges_subframe_cm = get_object('.template_2_retract_semirocker.ges_subframe.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_subframe_cm))
        _template_2_retract_semirocker_ges_subframe = get_object('.template_2_retract_semirocker.ges_subframe')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_subframe))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_subframe.inertia_frame', exc)

    try:
        graout_1 = get_object('.template_2_retract_semirocker.ges_subframe.graout_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_subframe')
        graout_1.relative_to = relative_to
        graout_1.marker_name = target_path('.template_2_retract_semirocker.ges_subframe.graout_1')
        _template_2_retract_semirocker_ground_hps_uc_sf_atch_r = get_object('.template_2_retract_semirocker.ground.hps_uc_sf_atch_r')
        graout_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_uc_sf_atch_r))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_1.location, graout_1.orientation)
        graout_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_subframe.graout_1', exc)

    try:
        graout_2 = get_object('.template_2_retract_semirocker.ges_subframe.graout_2')
        relative_to = get_object('.template_2_retract_semirocker.ges_subframe')
        graout_2.relative_to = relative_to
        graout_2.marker_name = target_path('.template_2_retract_semirocker.ges_subframe.graout_2')
        _template_2_retract_semirocker_ground_hps_uc_sf_atch_l = get_object('.template_2_retract_semirocker.ground.hps_uc_sf_atch_l')
        graout_2.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_uc_sf_atch_l))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_2.location, graout_2.orientation)
        graout_2.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_subframe.graout_2', exc)

    try:
        graout_3 = get_object('.template_2_retract_semirocker.ges_subframe.graout_3')
        relative_to = get_object('.template_2_retract_semirocker.ges_subframe')
        graout_3.relative_to = relative_to
        graout_3.marker_name = target_path('.template_2_retract_semirocker.ges_subframe.graout_3')
        _template_2_retract_semirocker_ground_hps_db_sf_atch = get_object('.template_2_retract_semirocker.ground.hps_db_sf_atch')
        graout_3.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_db_sf_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, graout_3.location, graout_3.orientation)
        graout_3.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_subframe.graout_3', exc)

    try:
        jxs_joint_j_15 = get_object('.template_2_retract_semirocker.ges_subframe.jxs_joint_j_15')
        relative_to = get_object('.template_2_retract_semirocker.ges_subframe')
        jxs_joint_j_15.relative_to = relative_to
        jxs_joint_j_15.marker_name = target_path('.template_2_retract_semirocker.ges_subframe.jxs_joint_j_15')
        _template_2_retract_semirocker_ground_cfs_uc_sf_atch_mid = get_object('.template_2_retract_semirocker.ground.cfs_uc_sf_atch_mid')
        jxs_joint_j_15.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_cfs_uc_sf_atch_mid))
        _template_2_retract_semirocker_ground_cfs_uc_sf_atch_mid = get_object('.template_2_retract_semirocker.ground.cfs_uc_sf_atch_mid')
        jxs_joint_j_15.orientation = _template_2_retract_semirocker_ground_cfs_uc_sf_atch_mid.orientation
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_15.location, jxs_joint_j_15.orientation)
        jxs_joint_j_15.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_15.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_subframe.jxs_joint_j_15', exc)

    try:
        jxs_joint_i_16 = get_object('.template_2_retract_semirocker.ges_subframe.jxs_joint_i_16')
        relative_to = get_object('.template_2_retract_semirocker.ges_subframe')
        jxs_joint_i_16.relative_to = relative_to
        jxs_joint_i_16.marker_name = target_path('.template_2_retract_semirocker.ges_subframe.jxs_joint_i_16')
        _template_2_retract_semirocker_mts_body_mount_jxs_joint_j_16 = get_object('.template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16')
        jxs_joint_i_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_mts_body_mount_jxs_joint_j_16))
        _template_2_retract_semirocker_mts_body_mount_jxs_joint_j_16 = get_object('.template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16')
        jxs_joint_i_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_mts_body_mount_jxs_joint_j_16))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_16.location, jxs_joint_i_16.orientation)
        jxs_joint_i_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_subframe.jxs_joint_i_16', exc)

    try:
        jxs_joint_j_14 = get_object('.template_2_retract_semirocker.ges_subframe.jxs_joint_j_14')
        relative_to = get_object('.template_2_retract_semirocker.ges_subframe')
        jxs_joint_j_14.relative_to = relative_to
        jxs_joint_j_14.marker_name = target_path('.template_2_retract_semirocker.ges_subframe.jxs_joint_j_14')
        _template_2_retract_semirocker_ground_hps_db_sf_atch = get_object('.template_2_retract_semirocker.ground.hps_db_sf_atch')
        jxs_joint_j_14.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_db_sf_atch))
        _template_2_retract_semirocker_ground_origo = get_object('.template_2_retract_semirocker.ground.origo')
        jxs_joint_j_14.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 90.0, 0.0], _template_2_retract_semirocker_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_14.location, jxs_joint_j_14.orientation)
        jxs_joint_j_14.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_14.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_subframe.jxs_joint_j_14', exc)

    try:
        jxs_joint_j_16 = get_object('.template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16')
        relative_to = get_object('.template_2_retract_semirocker.mts_body_mount')
        jxs_joint_j_16.relative_to = relative_to
        jxs_joint_j_16.marker_name = target_path('.template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16')
        _template_2_retract_semirocker_ground_cfs_subframe_to_body_point = get_object('.template_2_retract_semirocker.ground.cfs_subframe_to_body_point')
        jxs_joint_j_16.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_cfs_subframe_to_body_point))
        _template_2_retract_semirocker_ground_origo = get_object('.template_2_retract_semirocker.ground.origo')
        jxs_joint_j_16.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_origo))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_j_16.location, jxs_joint_j_16.orientation)
        jxs_joint_j_16.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_j_16.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.mts_body_mount.jxs_joint_j_16', exc)

    try:
        mts_body_mount = get_object('.template_2_retract_semirocker.mts_body_mount')
        mts_body_mount.part_name = target_path('.template_2_retract_semirocker.mts_body_mount')
        _template_2_retract_semirocker_ground_cfs_subframe_to_body_point = get_object('.template_2_retract_semirocker.ground.cfs_subframe_to_body_point')
        mts_body_mount.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_cfs_subframe_to_body_point))
        _template_2_retract_semirocker_ground_origo = get_object('.template_2_retract_semirocker.ground.origo')
        mts_body_mount.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_origo))


        updated += 1

    except Exception as exc:
        record_error('part modify rigid_body name_and_position .template_2_retract_semirocker.mts_body_mount', exc)

    try:
        inertia_frame = get_object('.template_2_retract_semirocker.ges_collar.inertia_frame')
        relative_to = get_object('.template_2_retract_semirocker.ges_collar')
        inertia_frame.relative_to = relative_to
        inertia_frame.marker_name = target_path('.template_2_retract_semirocker.ges_collar.inertia_frame')
        _template_2_retract_semirocker_ges_collar_cm = get_object('.template_2_retract_semirocker.ges_collar.cm')
        inertia_frame.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_collar_cm))
        _template_2_retract_semirocker_ges_collar = get_object('.template_2_retract_semirocker.ges_collar')
        inertia_frame.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_collar))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, inertia_frame.location, inertia_frame.orientation)
        inertia_frame.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        inertia_frame.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_collar.inertia_frame', exc)

    try:
        gralin_24 = get_object('.template_2_retract_semirocker.ges_collar.gralin_24')
        relative_to = get_object('.template_2_retract_semirocker.ges_collar')
        gralin_24.relative_to = relative_to
        gralin_24.marker_name = target_path('.template_2_retract_semirocker.ges_collar.gralin_24')
        _template_2_retract_semirocker_ground_hps_uc_bot = get_object('.template_2_retract_semirocker.ground.hps_uc_bot').location
        _template_2_retract_semirocker_ground_cfs_collar_top = get_object('.template_2_retract_semirocker.ground.cfs_collar_top').location
        gralin_24.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_uc_bot, _template_2_retract_semirocker_ground_cfs_collar_top, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, gralin_24.location, gralin_24.orientation)
        gralin_24.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        gralin_24.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_collar.gralin_24', exc)

    try:
        jxs_joint_i_1 = get_object('.template_2_retract_semirocker.ges_collar.jxs_joint_i_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_collar')
        jxs_joint_i_1.relative_to = relative_to
        jxs_joint_i_1.marker_name = target_path('.template_2_retract_semirocker.ges_collar.jxs_joint_i_1')
        _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1))
        _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1 = get_object('.template_2_retract_semirocker.ges_upper_cylinder.jxs_joint_j_1')
        jxs_joint_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_upper_cylinder_jxs_joint_j_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, jxs_joint_i_1.location, jxs_joint_i_1.orientation)
        jxs_joint_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        jxs_joint_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_collar.jxs_joint_i_1', exc)

    try:
        ues_actuator_i_1 = get_object('.template_2_retract_semirocker.ges_collar.ues_actuator_i_1')
        relative_to = get_object('.template_2_retract_semirocker.ges_collar')
        ues_actuator_i_1.relative_to = relative_to
        ues_actuator_i_1.marker_name = target_path('.template_2_retract_semirocker.ges_collar.ues_actuator_i_1')
        _template_2_retract_semirocker_ges_collar_jxs_joint_i_1 = get_object('.template_2_retract_semirocker.ges_collar.jxs_joint_i_1')
        ues_actuator_i_1.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_collar_jxs_joint_i_1))
        _template_2_retract_semirocker_ges_collar_jxs_joint_i_1 = get_object('.template_2_retract_semirocker.ges_collar.jxs_joint_i_1')
        ues_actuator_i_1.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_collar_jxs_joint_i_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_1.location, ues_actuator_i_1.orientation)
        ues_actuator_i_1.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_i_1.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_collar.ues_actuator_i_1', exc)

    try:
        ues_actuator_i_4 = get_object('.template_2_retract_semirocker.ges_collar.ues_actuator_i_4')
        relative_to = get_object('.template_2_retract_semirocker.ges_collar')
        ues_actuator_i_4.relative_to = relative_to
        ues_actuator_i_4.marker_name = target_path('.template_2_retract_semirocker.ges_collar.ues_actuator_i_4')
        _template_2_retract_semirocker_ges_collar_jxs_joint_i_1 = get_object('.template_2_retract_semirocker.ges_collar.jxs_joint_i_1')
        ues_actuator_i_4.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_collar_jxs_joint_i_1))
        _template_2_retract_semirocker_ges_collar_jxs_joint_i_1 = get_object('.template_2_retract_semirocker.ges_collar.jxs_joint_i_1')
        ues_actuator_i_4.orientation = (VecUtils.ORI_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ges_collar_jxs_joint_i_1))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, ues_actuator_i_4.location, ues_actuator_i_4.orientation)
        ues_actuator_i_4.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        ues_actuator_i_4.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.ges_collar.ues_actuator_i_4', exc)

    try:
        gralin_collar = get_object('.template_2_retract_semirocker.ges_collar.gralin_collar')
        gralin_collar.cylinder_name = target_path('.template_2_retract_semirocker.ges_collar.gralin_collar')
        _template_2_retract_semirocker_ground_hps_uc_bot = get_object('.template_2_retract_semirocker.ground.hps_uc_bot').location
        _template_2_retract_semirocker_ground_cfs_collar_top = get_object('.template_2_retract_semirocker.ground.cfs_collar_top').location
        gralin_collar.length = (VecUtils.DM(_template_2_retract_semirocker_ground_hps_uc_bot, _template_2_retract_semirocker_ground_cfs_collar_top))


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract_semirocker.ges_collar.gralin_collar', exc)

    try:
        MARKER_73 = get_object('.template_2_retract_semirocker.lunzhou.MARKER_73')
        relative_to = get_object('.template_2_retract_semirocker.lunzhou')
        MARKER_73.relative_to = relative_to
        MARKER_73.marker_name = target_path('.template_2_retract_semirocker.lunzhou.MARKER_73')
        _template_2_retract_semirocker_ground_POINT = get_object('.template_2_retract_semirocker.ground.POINT')
        MARKER_73.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_POINT))
        _template_2_retract_semirocker_ground_POINT = get_object('.template_2_retract_semirocker.ground.POINT').location
        _template_2_retract_semirocker_ground_POINT_2 = get_object('.template_2_retract_semirocker.ground.POINT_2').location
        MARKER_73.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_POINT, _template_2_retract_semirocker_ground_POINT_2, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_73.location, MARKER_73.orientation)
        MARKER_73.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_73.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.lunzhou.MARKER_73', exc)

    try:
        MARKER_83 = get_object('.template_2_retract_semirocker.lunzhou.MARKER_83')
        relative_to = get_object('.template_2_retract_semirocker.lunzhou')
        MARKER_83.relative_to = relative_to
        MARKER_83.marker_name = target_path('.template_2_retract_semirocker.lunzhou.MARKER_83')
        _template_2_retract_semirocker_ground_POINT_12 = get_object('.template_2_retract_semirocker.ground.POINT_12')
        MARKER_83.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_POINT_12))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_83.location, MARKER_83.orientation)
        MARKER_83.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.lunzhou.MARKER_83', exc)

    try:
        MARKER_85 = get_object('.template_2_retract_semirocker.lunzhou.MARKER_85')
        relative_to = get_object('.template_2_retract_semirocker.lunzhou')
        MARKER_85.relative_to = relative_to
        MARKER_85.marker_name = target_path('.template_2_retract_semirocker.lunzhou.MARKER_85')
        _template_2_retract_semirocker_ground_POINT = get_object('.template_2_retract_semirocker.ground.POINT')
        MARKER_85.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_POINT))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_85.location, MARKER_85.orientation)
        MARKER_85.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.lunzhou.MARKER_85', exc)

    try:
        CYLINDER_24 = get_object('.template_2_retract_semirocker.lunzhou.CYLINDER_24')
        CYLINDER_24.cylinder_name = target_path('.template_2_retract_semirocker.lunzhou.CYLINDER_24')
        CYLINDER_24.length = 240.0


        updated += 1

    except Exception as exc:
        record_error('geometry modify shape cylinder .template_2_retract_semirocker.lunzhou.CYLINDER_24', exc)

    try:
        MARKER_88 = get_object('.template_2_retract_semirocker.lunzhou.MARKER_88')
        relative_to = get_object('.template_2_retract_semirocker.lunzhou')
        MARKER_88.relative_to = relative_to
        MARKER_88.marker_name = target_path('.template_2_retract_semirocker.lunzhou.MARKER_88')
        _template_2_retract_semirocker_ground_POINT_27 = get_object('.template_2_retract_semirocker.ground.POINT_27')
        MARKER_88.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_POINT_27))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_88.location, MARKER_88.orientation)
        MARKER_88.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.lunzhou.MARKER_88', exc)

    try:
        MARKER_94 = get_object('.template_2_retract_semirocker.sf_rod.MARKER_94')
        relative_to = get_object('.template_2_retract_semirocker.sf_rod')
        MARKER_94.relative_to = relative_to
        MARKER_94.marker_name = target_path('.template_2_retract_semirocker.sf_rod.MARKER_94')
        _template_2_retract_semirocker_ground_hps_db_uc_atch = get_object('.template_2_retract_semirocker.ground.hps_db_uc_atch')
        MARKER_94.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_db_uc_atch))
        _template_2_retract_semirocker_ground_hps_db_uc_atch = get_object('.template_2_retract_semirocker.ground.hps_db_uc_atch').location
        _template_2_retract_semirocker_ground_hps_db_sf_atch = get_object('.template_2_retract_semirocker.ground.hps_db_sf_atch').location
        MARKER_94.orientation = (VecUtils.ORI_ALONG_AXIS(_template_2_retract_semirocker_ground_hps_db_uc_atch, _template_2_retract_semirocker_ground_hps_db_sf_atch, "Z"))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_94.location, MARKER_94.orientation)
        MARKER_94.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])
        MARKER_94.orientation = (loc_ori[1][0],loc_ori[1][1],loc_ori[1][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.sf_rod.MARKER_94', exc)

    try:
        MARKER_98 = get_object('.template_2_retract_semirocker.sf_rod.MARKER_98')
        relative_to = get_object('.template_2_retract_semirocker.sf_rod')
        MARKER_98.relative_to = relative_to
        MARKER_98.marker_name = target_path('.template_2_retract_semirocker.sf_rod.MARKER_98')
        _template_2_retract_semirocker_ground_hps_db_uc_atch = get_object('.template_2_retract_semirocker.ground.hps_db_uc_atch')
        MARKER_98.location = (VecUtils.LOC_RELATIVE_TO([0.0, 0.0, 0.0], _template_2_retract_semirocker_ground_hps_db_uc_atch))
        loc_ori = VecUtils.global2local(relative_to.location, relative_to.orientation, MARKER_98.location, MARKER_98.orientation)
        MARKER_98.location = (loc_ori[0][0],loc_ori[0][1],loc_ori[0][2])


        updated += 1

    except Exception as exc:
        record_error('marker modify .template_2_retract_semirocker.sf_rod.MARKER_98', exc)

    return {'updated': updated, 'warnings': warnings, 'errors': errors}

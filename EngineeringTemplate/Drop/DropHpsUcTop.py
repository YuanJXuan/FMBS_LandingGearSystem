import Jusme
from FmbsShortcut.SCcmd.utils import VecUtils

import AbstractHps
import Common


class DropHpsUcTopAdjust(AbstractHps.AbstractHpsAdjust):
    """Update the Drop model after ``hps_uc_top`` is changed.

    The node set and the geometric relationships in this class mirror
    ``AutoGenerater/model_template_2_drop.py``. All required nodes are
    resolved before any dependent property is changed so that an obsolete or
    incomplete model cannot be left half-updated.
    """

    _ORIGIN = [0.0, 0.0, 0.0]

    def __init__(self, hps_full_name) -> None:
        super().__init__(hps_full_name)
        self.last_error = ""
        self._last_valid_hps_location = None

        scene = getattr(Jusme, "ActiveUSScene", None)
        hps = scene.getObject(hps_full_name) if scene else None
        if hps:
            self._last_valid_hps_location = self._xyz(hps.location)

    @staticmethod
    def _xyz(value):
        """Return a coordinate/orientation value as a plain 3-tuple."""
        if hasattr(value, "x"):
            return (value.x, value.y, value.z)
        return (value[0], value[1], value[2])

    @classmethod
    def _local_pose(cls, parent, global_location, global_orientation):
        return cls._local_pose_from_transform(
            parent.location,
            parent.orientation,
            global_location,
            global_orientation,
        )

    @classmethod
    def _local_pose_from_transform(
        cls, parent_location, parent_orientation, global_location, global_orientation
    ):
        location, orientation = VecUtils.global2local(
            parent_location,
            parent_orientation,
            global_location,
            global_orientation,
        )
        return cls._xyz(location), cls._xyz(orientation)

    @classmethod
    def _global_location(cls, node):
        return VecUtils.LOC_RELATIVE_TO(cls._ORIGIN, node)

    @classmethod
    def _global_orientation(cls, node, orientation=None):
        if orientation is None:
            orientation = cls._ORIGIN
        return VecUtils.ORI_RELATIVE_TO(orientation, node)

    def _restore_hardpoint(self, hps):
        if hps and self._last_valid_hps_location is not None:
            hps.location = Jusme.Vector(*self._last_valid_hps_location)

    def _fail(self, message, hps=None):
        self.last_error = message
        self._restore_hardpoint(hps)
        print(">>>[ERROR] Drop hps_uc_top adjustment failed: {}".format(message))
        return False

    @staticmethod
    def _apply_updates(updates):
        """Apply property updates and roll them back if an assignment fails."""
        old_values = []
        try:
            for node, attribute, value in updates:
                old_values.append((node, attribute, getattr(node, attribute)))
                setattr(node, attribute, value)
        except Exception:
            for node, attribute, old_value in reversed(old_values):
                setattr(node, attribute, old_value)
            raise

        return old_values

    @staticmethod
    def _rollback_updates(old_values):
        for node, attribute, old_value in reversed(old_values):
            setattr(node, attribute, old_value)

    def Adjust(self):
        scene = getattr(Jusme, "ActiveUSScene", None)
        if scene is None:
            return self._fail("no active scene")

        model_name = Common.getModelName()
        prefix = ".{}.".format(model_name)

        paths = {
            # Ground construction points/markers.
            "hps_uc_top": self.hps_full_name,
            "origo1": prefix + "ground.origo1",
            "hps_uc_bot": prefix + "ground.hps_uc_bot",
            "hps_uc_sf_atch_l": prefix + "ground.hps_uc_sf_atch_l",
            "hps_uc_sf_atch_r": prefix + "ground.hps_uc_sf_atch_r",
            "hps_uc_geompt": prefix + "ground.hps_uc_geompt",
            "hps_db_uc_atch": prefix + "ground.hps_db_uc_atch",
            "hps_uta_uc_atch": prefix + "ground.hps_uta_uc_atch",
            "cfs_collar_top": prefix + "ground.cfs_collar_top",

            # Upper-cylinder part, geometry and markers.
            "upper": prefix + "ges_upper_cylinder",
            "upper_geom1": prefix + "ges_upper_cylinder.gralin_upper_cylinder_geom1",
            "upper_gralin_2": prefix + "ges_upper_cylinder.gralin_2",
            "upper_gralin_3": prefix + "ges_upper_cylinder.gralin_3",
            "upper_gralin_4": prefix + "ges_upper_cylinder.gralin_4",
            "upper_joint_j_1": prefix + "ges_upper_cylinder.jxs_joint_j_1",
            "upper_joint_j_11": prefix + "ges_upper_cylinder.jxs_joint_j_11",
            "upper_joint_j_12": prefix + "ges_upper_cylinder.jxs_joint_j_12",
            "upper_actuator_j_1": prefix + "ges_upper_cylinder.ues_actuator_j_1",
            "upper_actuator_j_4": prefix + "ges_upper_cylinder.ues_actuator_j_4",
            "upper_spring_j_1": prefix + "ges_upper_cylinder.ues_spring_j_1",
            "upper_damper_j_1": prefix + "ges_upper_cylinder.ues_damper_j_1",
            "upper_stopper_j_1": prefix + "ges_upper_cylinder.ues_stopper_j_1",
            "upper_marker_2": prefix + "ges_upper_cylinder.MARKER_2",
            "upper_marker_116": prefix + "ges_upper_cylinder.MARKER_116",
            "upper_marker_405": prefix + "ges_upper_cylinder.MARKER_405",
            "upper_marker_407": prefix + "ges_upper_cylinder.MARKER_407",
            "upper_marker_409": prefix + "ges_upper_cylinder.MARKER_409",
            "upper_marker_428": prefix + "ges_upper_cylinder.MARKER_428",

            # The lower-cylinder marker fixes the cylinder-joint frame.
            "lower_joint_i_11": prefix + "ges_lower_cylinder.jxs_joint_i_11",

            # Collar part and its hps_uc_top-dependent markers.
            "collar": prefix + "ges_collar",
            "collar_geom": prefix + "ges_collar.gralin_collar",
            "collar_gralin_24": prefix + "ges_collar.gralin_24",
            "collar_joint_j_10": prefix + "ges_collar.jxs_joint_j_10",
            "collar_joint_i_1": prefix + "ges_collar.jxs_joint_i_1",
            "collar_actuator_i_1": prefix + "ges_collar.ues_actuator_i_1",
            "collar_actuator_i_4": prefix + "ges_collar.ues_actuator_i_4",

            # Body-mount side of the fixed upper-cylinder joint.
            "body_mount": prefix + "mts_body_mount_2",
            "body_mount_marker_427": prefix + "mts_body_mount_2.MARKER_427",

            # Joints affected by the marker updates.
            "joint_collar_upper": prefix + "josrev_collar_uc_joint",
            "joint_dragbrace_upper": prefix + "jossph_db_uc_joint",
            "joint_lower_upper": prefix + "joscyl_lc_uc_joint",
            "joint_torque_arm_collar": prefix + "josrev_uta_uc_joint",
            "joint_body_mount": prefix + "JOINT_56",
        }

        nodes = {name: scene.getObject(path) for name, path in paths.items()}
        missing = [paths[name] for name, node in nodes.items() if not node]
        hps_uc_top = nodes["hps_uc_top"]
        if missing:
            return self._fail(
                "required node(s) not found: {}".format(", ".join(missing)),
                hps_uc_top,
            )

        try:
            hps_uc_top_loc = hps_uc_top.location
            hps_uc_bot_loc = nodes["hps_uc_bot"].location
            upper_length = VecUtils.DM(hps_uc_top_loc, hps_uc_bot_loc)
            if upper_length <= 1.0e-9:
                return self._fail(
                    "hps_uc_top and hps_uc_bot cannot coincide", hps_uc_top
                )

            # Part frames follow the same endpoint rules used by the template.
            upper_location = 0.5 * (hps_uc_top_loc + hps_uc_bot_loc)
            upper_orientation = VecUtils.ORI_ALONG_AXIS(
                hps_uc_top_loc, hps_uc_bot_loc, "z"
            )
            collar_top_location = VecUtils.LOC_ALONG_LINE(
                hps_uc_bot_loc, hps_uc_top_loc, 0.11 * upper_length
            )
            collar_orientation = VecUtils.ORI_ALONG_AXIS(
                hps_uc_bot_loc, hps_uc_top_loc, "z"
            )
            collar_location = 0.5 * (hps_uc_bot_loc + collar_top_location)
            collar_length = VecUtils.DM(hps_uc_bot_loc, collar_top_location)

            top_global = self._global_location(hps_uc_top)
            bot_global = self._global_location(nodes["hps_uc_bot"])
            collar_top_global = collar_top_location
            origin_orientation = self._global_orientation(nodes["origo1"])

            upper = nodes["upper"]
            collar = nodes["collar"]
            body_mount = nodes["body_mount"]

            # Compute every child pose against its future parent transform.
            def upper_local_pose(global_location, global_orientation):
                return self._local_pose_from_transform(
                    upper_location,
                    upper_orientation,
                    global_location,
                    global_orientation,
                )

            def collar_local_pose(global_location, global_orientation):
                return self._local_pose_from_transform(
                    collar_location,
                    collar_orientation,
                    global_location,
                    global_orientation,
                )

            upper_local_poses = {
                "upper_gralin_2": upper_local_pose(top_global, upper_orientation),
                "upper_gralin_3": upper_local_pose(
                    self._global_location(nodes["hps_uc_sf_atch_l"]),
                    VecUtils.ORI_ALONG_AXIS(
                        nodes["hps_uc_sf_atch_l"].location,
                        nodes["hps_uc_geompt"].location,
                        "z",
                    ),
                ),
                "upper_gralin_4": upper_local_pose(
                    self._global_location(nodes["hps_uc_sf_atch_r"]),
                    VecUtils.ORI_ALONG_AXIS(
                        nodes["hps_uc_sf_atch_r"].location,
                        nodes["hps_uc_geompt"].location,
                        "z",
                    ),
                ),
                "upper_joint_j_12": upper_local_pose(
                    self._global_location(nodes["hps_db_uc_atch"]),
                    origin_orientation,
                ),
                "upper_joint_j_11": upper_local_pose(
                    self._global_location(nodes["lower_joint_i_11"]),
                    self._global_orientation(nodes["lower_joint_i_11"]),
                ),
                "upper_joint_j_1": upper_local_pose(
                    collar_top_global, collar_orientation
                ),
            }

            # Spring/damper/stopper J markers point from the top toward the
            # lower end; actuator J markers share the collar joint frame.
            for name in (
                "upper_spring_j_1",
                "upper_damper_j_1",
                "upper_stopper_j_1",
            ):
                upper_local_poses[name] = upper_local_pose(
                    top_global, upper_orientation
                )

            for name in ("upper_actuator_j_1", "upper_actuator_j_4"):
                upper_local_poses[name] = upper_local_pose(
                    collar_top_global, collar_orientation
                )

            # These markers are all located at hps_uc_top in the Drop model.
            # Their global frame is the model origin frame.
            for name in (
                "upper_marker_2",
                "upper_marker_116",
                "upper_marker_405",
                "upper_marker_407",
                "upper_marker_409",
                "upper_marker_428",
            ):
                upper_local_poses[name] = upper_local_pose(
                    top_global, origin_orientation
                )

            collar_local_poses = {
                "collar_gralin_24": collar_local_pose(
                    bot_global, collar_orientation
                ),
                "collar_joint_i_1": collar_local_pose(
                    collar_top_global, collar_orientation
                ),
                "collar_actuator_i_1": collar_local_pose(
                    collar_top_global, collar_orientation
                ),
                "collar_actuator_i_4": collar_local_pose(
                    collar_top_global, collar_orientation
                ),
                "collar_joint_j_10": collar_local_pose(
                    self._global_location(nodes["hps_uta_uc_atch"]),
                    self._global_orientation(nodes["origo1"], [0.0, 90.0, 0.0]),
                ),
            }

            body_mount_marker_pose = self._local_pose(
                body_mount, top_global, origin_orientation
            )
        except Exception as exc:
            return self._fail("calculation error: {}".format(exc), hps_uc_top)

        updates = [
            (nodes["cfs_collar_top"], "location", collar_top_location),
            (nodes["cfs_collar_top"], "orientation", collar_orientation),
            (upper, "location", upper_location),
            (upper, "orientation", upper_orientation),
            (nodes["upper_geom1"], "length", upper_length),
            (collar, "location", collar_location),
            (collar, "orientation", collar_orientation),
            (nodes["collar_geom"], "length", collar_length),
        ]

        for name, (location, orientation) in upper_local_poses.items():
            updates.append((nodes[name], "location", location))
            updates.append((nodes[name], "orientation", orientation))

        for name, (location, orientation) in collar_local_poses.items():
            updates.append((nodes[name], "location", location))
            updates.append((nodes[name], "orientation", orientation))

        updates.append(
            (nodes["body_mount_marker_427"], "location", body_mount_marker_pose[0])
        )
        updates.append(
            (nodes["body_mount_marker_427"], "orientation", body_mount_marker_pose[1])
        )

        old_values = []
        try:
            old_values = self._apply_updates(updates)
            for joint_name in (
                "joint_collar_upper",
                "joint_dragbrace_upper",
                "joint_lower_upper",
                "joint_torque_arm_collar",
                "joint_body_mount",
            ):
                nodes[joint_name].recompute()
        except Exception as exc:
            if old_values:
                self._rollback_updates(old_values)
            return self._fail("update error: {}".format(exc), hps_uc_top)

        self._last_valid_hps_location = self._xyz(hps_uc_top.location)
        self.last_error = ""
        print(">>>[INFO] Drop hps_uc_top adjustment completed")
        return True

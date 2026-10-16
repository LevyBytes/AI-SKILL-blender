# Constraint Type Items

Motion Tracking

| Value | Meaning |
| --- | --- |
| `CAMERA_SOLVER` | Camera Solver. |
| `FOLLOW_TRACK` | Follow Track. |
| `OBJECT_SOLVER` | Object Solver.<br>Transform |
| `COPY_LOCATION` | Copy Location.<br>Make the owner share the target's location, optionally offset, so the two travel as one. |
| `COPY_ROTATION` | Copy Rotation.<br>Make the owner share the target's rotation, optionally offset, so the two turn together. |
| `COPY_SCALE` | Copy Scale.<br>Make the owner share the target's scale factors, optionally offset, so both end up scaled alike. |
| `COPY_TRANSFORMS` | Copy Transforms.<br>Adopt every transformation of the target so the two move as one. |
| `LIMIT_DISTANCE` | Limit Distance.<br>Keep motion bounded to a set distance from a target, checked only when the constraint is evaluated. |
| `LIMIT_LOCATION` | Limit Location.<br>Clamp movement on each axis to the ranges you specify. |
| `LIMIT_ROTATION` | Limit Rotation.<br>Clamp rotation on each axis to the ranges you specify. |
| `LIMIT_SCALE` | Limit Scale.<br>Clamp scaling on each axis to the ranges you specify. |
| `MAINTAIN_VOLUME` | Maintain Volume.<br>Offset scaling on one axis by scaling the remaining two axes to keep volume constant. |
| `TRANSFORM` | Transformation.<br>Drive one property on the owner from a transform property read off the target (or itself). |
| `TRANSFORM_CACHE` | Transform Cache.<br>Read the transformation matrix in from an external file.<br>Tracking |
| `CLAMP_TO` | Clamp To.<br>Pin motion onto a curve by mapping location along the curve's longest axis. |
| `DAMPED_TRACK` | Damped Track.<br>Aim at a target using the least rotation that gets there. |
| `IK` | Inverse Kinematics.<br>Drive a chain of bones from a chosen endpoint target (bones only). |
| `LOCKED_TRACK` | Locked Track.<br>Spin about a fixed ('locked') axis to face a target. |
| `SPLINE_IK` | Spline IK.<br>Lay a chain of bones out along a curve (bones only). |
| `STRETCH_TO` | Stretch To.<br>Extend along the Y axis to reach toward a target. |
| `TRACK_TO` | Track To.<br>An older tracking constraint that tends to introduce twisting artifacts.<br>Relationship |
| `ACTION` | Action.<br>Pull a pose for the owner from an Action, keyed off a transform property of the target. |
| `ARMATURE` | Armature.<br>Blend weighted transforms from several bones, much like the Armature modifier does. |
| `CHILD_OF` | Child Of.<br>Treat the target as a 'detachable' parent of the owner. |
| `FLOOR` | Floor.<br>Turn the target's position (and optionally rotation) into a 'wall' or 'floor' the owner is blocked from passing. |
| `FOLLOW_PATH` | Follow Path.<br>Drive an object or bone so it travels along a path. |
| `GEOMETRY_ATTRIBUTE` | Geometry Attribute.<br>Read a transform out of an attribute stored on the target geometry. |
| `PIVOT` | Pivot.<br>Shift the pivot point used for transforms (buggy). |
| `SHRINKWRAP` | Shrinkwrap.<br>Keep motion clinging to the surface of the target mesh. |

[Related references](INDEX.md).

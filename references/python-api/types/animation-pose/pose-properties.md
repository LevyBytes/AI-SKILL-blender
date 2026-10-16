# bpy.types.Pose: properties

## Pose(bpy_struct)

### Pose(bpy_struct)

base class — bpy_struct
class bpy.types. Pose ( bpy_struct )

A set of pose channels together with the settings that animate bones.
animation_visualization

Animation data attached to this data-block (readonly, never None)

Type :

AnimViz
bones

The armature's pose bones, one per bone (default None, readonly)

Type :

bpy_prop_collection[PoseBone]
ik_param

Configuration passed to the IK solver (readonly)

Type :

IKParam
ik_solver

Which IK solver drives the IK chain (default 'LEGACY' )

- LEGACY
Standard – The original IK solver.

- ITASC
iTaSC – A stateful solver handling multiple constraints.

Type :

Literal[‘LEGACY’, ‘ITASC’]
use_auto_ik

Insert short-lived IK constraints while grabbing bones in Pose Mode (default False)

Type :

bool
use_mirror_relative

Treat transforms as relative when working in X-mirror mode (not supported with Auto IK) (default False)

Type :

bool
use_mirror_x

Mirror edits onto the matching bone across the X-Axis (default False)

Type :

bool

[Related references](INDEX.md).

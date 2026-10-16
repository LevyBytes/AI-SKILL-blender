# bpy.ops.object.fix_to_camera

bpy.ops.object. fix_to_camera ( * , use_location = True , use_rotation = True , use_scale = True ) 

Produce new animation frames anchoring the selected object/bone to the view camera when frames lack existing keyframes

Parameters :

- use_location ( bool ) – Location, Add position keyframes for fixing to the active scene camera (optional)

- use_rotation ( bool ) – Rotation, Add orientation keyframes for fixing to the active scene camera (optional)

- use_scale ( bool ) – Scale, Add scaling keyframes for fixing to the active scene camera (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/copy_global_transform.py:639

[Related references](INDEX.md).

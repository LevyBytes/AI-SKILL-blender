# bpy.ops.armature.copy_bone_color_to_selected

bpy.ops.armature. copy_bone_color_to_selected ( * , bone_type = 'EDIT' )

Apply the focused bone's tint to all active bones.

Parameters :

bone_type ( Literal [ 'EDIT' , 'POSE' ] ) – Type, (optional)

- EDIT
Bone – Apply Bone colors from the focused bone to all active bones.

- POSE
Pose Bone – Apply Pose Bone colors from the focused pose bone to all active pose bones.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/anim.py:493

[Related references](INDEX.md).

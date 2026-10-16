# bpy.ops.armature.duplicate_move

bpy.ops.armature. duplicate_move ( * , `ARMATURE_OT`_duplicate = {} , `TRANSFORM_OT`_translate = {} )

Produce copies of active bones within the same rig and relocate them.

Parameters :

- `ARMATURE_OT`_duplicate ( dict [ str , Any ] ) – Duplicate Selected Bone(s), Produce copies of active bones within the same rig (optional, bpy.ops.armature.duplicate() keyword arguments)

- `TRANSFORM_OT`_translate ( dict [ str , Any ] ) – Move, Move selected items (optional, bpy.ops.transform.translate() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

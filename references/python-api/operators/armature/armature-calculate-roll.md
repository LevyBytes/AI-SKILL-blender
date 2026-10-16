# bpy.ops.armature.calculate_roll

bpy.ops.armature. calculate_roll ( * , type = '`POS_X`' , axis_flip = False , axis_only = False )

Immediately correct the orientation of active bones' local axes.

Parameters :

- type ( Literal [ '`POS_X`' , '`POS_Z`' , '`GLOBAL_POS_X`' , '`GLOBAL_POS_Y`' , '`GLOBAL_POS_Z`' , '`NEG_X`' , '`NEG_Z`' , '`GLOBAL_NEG_X`' , '`GLOBAL_NEG_Y`' , '`GLOBAL_NEG_Z`' , 'ACTIVE' , 'VIEW' , 'CURSOR' ] ) – Type, (optional)

- axis_flip ( bool ) – Flip Axis, Negate the alignment axis (optional)

- axis_only ( bool ) – Shortest Rotation, Ignore the axis direction, use the shortest rotation to align (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

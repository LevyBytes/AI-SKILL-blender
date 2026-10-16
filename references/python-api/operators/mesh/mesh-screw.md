# bpy.ops.mesh.screw

bpy.ops.mesh. screw ( * , steps = 9 , turns = 1 , center = (0.0, 0.0, 0.0) , axis = (0.0, 0.0, 0.0) ) 

Generate a spiral by spinning chosen vertices around the viewport origin

Parameters :

- steps ( int ) – Steps, How many divisions (in [1, 100000], optional)

- turns ( int ) – Turns, How many full rotations (in [1, 100000], optional)

- center (mathutils.Vector) – Center, Focal point in global coordinate space (array of 3 items, in [-inf, inf], optional)

- axis (mathutils.Vector) – Axis, Rotation axis in global coordinate space (array of 3 items, in [-1, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

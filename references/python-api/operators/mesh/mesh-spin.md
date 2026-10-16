# bpy.ops.mesh.spin

bpy.ops.mesh. spin ( * , steps = 12 , dupli = False , angle = 1.5708 , use_auto_merge = True , use_normal_flip = False , center = (0.0, 0.0, 0.0) , axis = (0.0, 0.0, 0.0) ) 

Create copies by rotating chosen points around the viewport origin

Parameters :

- steps ( int ) – Steps, How many divisions (in [0, 1000000], optional)

- dupli ( bool ) – Use Duplicates, (optional)

- angle ( float ) – Angle, How much to turn per step (in [-inf, inf], optional)

- use_auto_merge ( bool ) – Auto Merge, Collapse first/last when the angle equals a full turn (optional)

- use_normal_flip ( bool ) – Flip Normals, (optional)

- center (mathutils.Vector) – Center, Focal point in global coordinate space (array of 3 items, in [-inf, inf], optional)

- axis (mathutils.Vector) – Axis, Rotation axis in global coordinate space (array of 3 items, in [-1, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

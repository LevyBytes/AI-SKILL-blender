# bpy.ops.object.randomize_transform

bpy.ops.object. randomize_transform ( * , random_seed = 0 , use_delta = False , use_loc = True , loc = (0.0, 0.0, 0.0) , use_rot = True , rot = (0.0, 0.0, 0.0) , use_scale = True , scale_even = False , scale = (1.0, 1.0, 1.0) ) 

Vary objects position, direction, and dimension unpredictably

Parameters :

- random_seed ( int ) – Random Seed, Initialization state for the random generator (in [0, 10000], optional)

- use_delta ( bool ) – Transform Delta, Randomize offset transformation instead of primary transformation (optional)

- use_loc ( bool ) – Randomize Location, Vary the placement values (optional)

- loc (mathutils.Vector) – Location, Maximum scatter span per axis (array of 3 items, in [-100, 100], optional)

- use_rot ( bool ) – Randomize Rotation, Vary the orientation values (optional)

- rot (mathutils.Euler) – Rotation, Maximum turn per axis (array of 3 items, in [-3.14159, 3.14159], optional)

- use_scale ( bool ) – Randomize Scale, Vary the scaling values (optional)

- scale_even ( bool ) – Scale Even, Apply identical scaling on all axes (optional)

- scale ( Sequence [ float ] ) – Scale, Maximum scaling shift per axis (array of 3 items, in [-100, 100], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/object_randomize_transform.py:163

[Related references](INDEX.md).

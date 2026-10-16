# bpy.ops.uv.randomize_uv_transform

bpy.ops.uv. randomize_uv_transform ( * , random_seed = 0 , use_loc = True , loc = (0.0, 0.0) , use_rot = True , rot = 0.0 , use_scale = True , scale_even = False , scale = (1.0, 1.0) ) 

Jitters the UV island's position, rotation, and scale at random

Parameters :

- random_seed ( int ) – Random Seed, Seed value for the random generator (in [0, 10000], optional)

- use_loc ( bool ) – Randomize Location, Randomize the location values (optional)

- loc (mathutils.Vector) – Location, Maximum distance the objects can spread over each axis (array of 2 items, in [-100, 100], optional)

- use_rot ( bool ) – Randomize Rotation, Randomize the rotation value (optional)

- rot ( float ) – Rotation, Maximum rotation (in [-6.28319, 6.28319], optional)

- use_scale ( bool ) – Randomize Scale, Randomize the scale values (optional)

- scale_even ( bool ) – Scale Even, Use the same scale value for both axes (optional)

- scale ( Sequence [ float ] ) – Scale, Maximum scale randomization over each axis (array of 2 items, in [-100, 100], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/uvcalc_transform.py:536

[Related references](INDEX.md).

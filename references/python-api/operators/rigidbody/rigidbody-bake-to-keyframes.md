# bpy.ops.rigidbody.bake_to_keyframes

bpy.ops.rigidbody. bake_to_keyframes ( * , frame_start = 1 , frame_end = 250 , step = 1 )

Records rigid body object transformations at each frame, storing them as animation keyframes

Parameters :

- frame_start ( int ) – Start Frame, Opening frame where recording begins (in [0, 300000], optional)

- frame_end ( int ) – End Frame, Closing frame where recording ends (in [1, 300000], optional)

- step ( int ) – Frame Step, Interval between recorded frames (in [1, 120], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/rigidbody.py:108

[Related references](INDEX.md).

# bpy.ops.pose.blend_with_rest

bpy.ops.pose. blend_with_rest ( * , factor = 0.5 , prev_frame = 0 , next_frame = 0 , channels = 'ALL' , axis_lock = 'FREE' ) 

Shift the current pose closer to or further from the rest configuration

Parameters :

- factor ( float ) – Factor, Weighting factor for which keyframe is favored more (in [0, 1], optional)

- prev_frame ( int ) – Previous Keyframe, Frame number of keyframe immediately before the current frame (in [-1048574, 1048574], optional)

- next_frame ( int ) – Next Keyframe, Frame number of keyframe immediately after the current frame (in [-1048574, 1048574], optional)

- channels ( Literal [ 'ALL' , 'LOC' , 'ROT' , 'SIZE' , 'BBONE' , 'CUSTOM' ] ) – Channels, Set of properties that are affected (optional)

- ALL
All Properties – All properties, including transforms, bendy bone shape, and custom properties.

- LOC
Location – Location only.

- ROT
Rotation – Rotation only.

- SIZE
Scale – Scale only.

- BBONE
Bendy Bone – Bendy Bone shape properties.

- CUSTOM
Custom Properties – Custom properties.

- axis_lock ( Literal [ 'FREE' , 'X' , 'Y' , 'Z' ] ) – Axis Lock, Transform axis to restrict effects to (optional)

- FREE
Free – All axes are affected.

- X
X – Only X-axis transforms are affected.

- Y
Y – Only Y-axis transforms are affected.

- Z
Z – Only Z-axis transforms are affected.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

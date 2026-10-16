# bpy.ops.object.shade_smooth_by_angle

bpy.ops.object. shade_smooth_by_angle ( * , angle = 0.523599 , keep_sharp_edges = True ) 

Tag mesh edges based on the angle between adjacent polygons

Parameters :

- angle ( float ) – Angle, Upper threshold for face normal divergence that is still treated as smooth (in [0, 3.14159], optional)

- keep_sharp_edges ( bool ) – Keep Sharp Edges, Insert sharp tags instead of blanking previous ones (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.transform.vertex_warp

bpy.ops.transform. vertex_warp ( * , warp_angle = 6.28319 , offset_angle = 0.0 , min = -1.0 , max = 1.0 , viewmat = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)) , center = (0.0, 0.0, 0.0) ) 

Bends vertices in an arc centered on the cursor

Parameters :

- warp_angle ( float ) – Warp Angle, Amount to warp about the cursor (in [-inf, inf], optional)

- offset_angle ( float ) – Offset Angle, Angle to use as the basis for warping (in [-inf, inf], optional)

- min ( float ) – Min, (in [-inf, inf], optional)

- max ( float ) – Max, (in [-inf, inf], optional)

- viewmat (mathutils.Matrix) – Matrix, (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)

- center (mathutils.Vector) – Center, (array of 3 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

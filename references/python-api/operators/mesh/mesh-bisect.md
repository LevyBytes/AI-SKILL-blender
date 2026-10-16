# bpy.ops.mesh.bisect

bpy.ops.mesh. bisect ( * , plane_co = (0.0, 0.0, 0.0) , plane_no = (0.0, 0.0, 0.0) , use_fill = False , clear_inner = False , clear_outer = False , threshold = 0.0001 , xstart = 0 , xend = 0 , ystart = 0 , yend = 0 , flip = False , cursor = 5 )

Slice the mesh with a plane (drag to orient it)

Parameters :

- plane_co (mathutils.Vector) – Plane Point, A point on the plane (array of 3 items, in [-inf, inf], optional)

- plane_no (mathutils.Vector) – Plane Normal, The direction the plane points (array of 3 items, in [-1, 1], optional)

- use_fill ( bool ) – Fill, Fill in the cut (optional)

- clear_inner ( bool ) – Clear Inner, Remove geometry behind the plane (optional)

- clear_outer ( bool ) – Clear Outer, Remove geometry in front of the plane (optional)

- threshold ( float ) – Axis Threshold, Preserves the existing geometry along the cut plane (in [0, 10], optional)

- xstart ( int ) – X Start, (in [-inf, inf], optional)

- xend ( int ) – X End, (in [-inf, inf], optional)

- ystart ( int ) – Y Start, (in [-inf, inf], optional)

- yend ( int ) – Y End, (in [-inf, inf], optional)

- flip ( bool ) – Flip, (optional)

- cursor ( int ) – Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.sculpt.trim_line_gesture

bpy.ops.sculpt. trim_line_gesture ( * , xstart = 0 , xend = 0 , ystart = 0 , yend = 0 , flip = False , cursor = 5 , use_front_faces_only = False , use_limit_to_segment = False , location = (0, 0) , trim_mode = 'DIFFERENCE' , use_cursor_depth = False , trim_orientation = 'VIEW' , trim_extrude_mode = 'FIXED' , trim_solver = 'MANIFOLD' )

Remove geometry on one side of a line gesture

Parameters :

- xstart ( int ) – X Start, (in [-inf, inf], optional)

- xend ( int ) – X End, (in [-inf, inf], optional)

- ystart ( int ) – Y Start, (in [-inf, inf], optional)

- yend ( int ) – Y End, (in [-inf, inf], optional)

- flip ( bool ) – Flip, (optional)

- cursor ( int ) – Cursor, Pointer appearance during the interactive operation (in [0, inf], optional)

- use_front_faces_only ( bool ) – Front Faces Only, Influence only surfaces oriented toward the camera (optional)

- use_limit_to_segment ( bool ) – Limit to Segment, Confine the gesture activity to the zone within the segment without extending along the complete line (optional)

- location ( Sequence [ int ] ) – Location, Cursor position (array of 2 items, in [-inf, inf], optional)

- trim_mode ( Literal [ 'DIFFERENCE' , 'UNION' , 'JOIN' ] ) – Trim Mode, (optional)

- DIFFERENCE
Difference – Use a difference boolean operation.

- UNION
Union – Use a union boolean operation.

- JOIN
Join – Join the new mesh as separate geometry, without performing any boolean operation.

- use_cursor_depth ( bool ) – Use Cursor for Depth, Use cursor position and span for the size and placement of the trimming boundary (optional)

- trim_orientation ( Literal [ 'VIEW' , 'SURFACE' ] ) – Shape Orientation, (optional)

- VIEW
View – Use the view to orientate the trimming shape.

- SURFACE
Surface – Use the surface normal to orientate the trimming shape.

- trim_extrude_mode ( Literal [ 'PROJECT' , 'FIXED' ] ) – Extrude Mode, (optional)

- PROJECT
Project – Align trim geometry with the perspective of the current view for a tapered shape.

- FIXED
Fixed – Align trim geometry orthogonally for a shape with 90 degree angles.

- trim_solver ( Literal [ 'EXACT' , 'FLOAT' , 'MANIFOLD' ] ) – Solver, (optional)

- EXACT
Exact – Slower solver with the best results for coplanar faces.

- FLOAT
Float – Simple solver with good performance, without support for overlapping geometry.

- MANIFOLD
Manifold – Fastest solver that works only on manifold meshes but gives better results.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

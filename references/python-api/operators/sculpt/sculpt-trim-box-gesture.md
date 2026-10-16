# bpy.ops.sculpt.trim_box_gesture

bpy.ops.sculpt. trim_box_gesture ( * , xmin = 0 , xmax = 0 , ymin = 0 , ymax = 0 , wait_for_input = True , use_front_faces_only = False , location = (0, 0) , trim_mode = 'DIFFERENCE' , use_cursor_depth = False , trim_orientation = 'VIEW' , trim_extrude_mode = 'FIXED' , trim_solver = 'MANIFOLD' )

Perform a shape operation on the surface and a rectangular boundary specified by the cursor

Parameters :

- xmin ( int ) – X Min, (in [-inf, inf], optional)

- xmax ( int ) – X Max, (in [-inf, inf], optional)

- ymin ( int ) – Y Min, (in [-inf, inf], optional)

- ymax ( int ) – Y Max, (in [-inf, inf], optional)

- wait_for_input ( bool ) – Wait for Input, (optional)

- use_front_faces_only ( bool ) – Front Faces Only, Influence only surfaces oriented toward the camera (optional)

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

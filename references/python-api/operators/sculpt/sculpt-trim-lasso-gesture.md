# bpy.ops.sculpt.trim_lasso_gesture

bpy.ops.sculpt. trim_lasso_gesture ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 , use_front_faces_only = False , location = (0, 0) , trim_mode = 'DIFFERENCE' , use_cursor_depth = False , trim_orientation = 'VIEW' , trim_extrude_mode = 'FIXED' , trim_solver = 'MANIFOLD' )

Perform a shape operation on the surface and a form specified by the cursor

Parameters :

- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)

- use_smooth_stroke ( bool ) – Stabilize Stroke, Cursor motion lags behind and pursues a softer route (optional)

- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Greater levels yield softer motion (in [0.5, 0.99], optional)

- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Smallest span from prior point prior to resuming motion (in [10, 200], optional)

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
bpy.ops.sculpt. trim_lasso_gesture ( * , path = None , use_smooth_stroke = False , smooth_stroke_factor = 0.75 , smooth_stroke_radius = 35 , use_front_faces_only = False , location = (0, 0) , trim_mode = 'DIFFERENCE' , use_cursor_depth = False , trim_orientation = 'VIEW' , trim_extrude_mode = 'FIXED' , trim_solver = 'MANIFOLD' )
Runs a boolean operation between the mesh and a shape defined by the cursor.
Parameters:
- path ( bpy_prop_collection [ OperatorMousePath ]) – Path, (optional)
- use_smooth_stroke ( bool ) – Stabilize Stroke, Selection lags behind mouse and follows a smoother path (optional)
- smooth_stroke_factor ( float ) – Smooth Stroke Factor, Higher values give a smoother stroke (in [0.5, 0.99], optional)
- smooth_stroke_radius ( int ) – Smooth Stroke Radius, Minimum distance from last point before selection continues (in [10, 200], optional)
- use_front_faces_only ( bool ) – Front Faces Only, Affect only faces facing towards the view (optional)
- location ( Sequence [ int ] ) – Location, Mouse location (array of 2 items, in [-inf, inf], optional)
- trim_mode ( Literal [ 'DIFFERENCE' , 'UNION' , 'JOIN' ] ) – Trim Mode, (optional)
- DIFFERENCE - Difference: use a difference boolean operation.
- UNION - Union: use a union boolean operation.
- JOIN - Join: join the new mesh as separate geometry, without performing any boolean operation.
- use_cursor_depth ( bool ) – Use Cursor for Depth, Use cursor location and radius for the dimensions and position of the trimming shape (optional)
- trim_orientation ( Literal [ 'VIEW' , 'SURFACE' ] ) – Shape Orientation, (optional)
- VIEW - View: use the view to orientate the trimming shape.
- SURFACE - Surface: use the surface normal to orientate the trimming shape.
- trim_extrude_mode ( Literal [ 'PROJECT' , 'FIXED' ] ) – Extrude Mode, (optional)
- PROJECT - Project: align trim geometry with the perspective of the current view for a tapered shape.
- FIXED - Fixed: align trim geometry orthogonally for a shape with 90 degree angles.
- trim_solver ( Literal [ 'EXACT' , 'FLOAT' , 'MANIFOLD' ] ) – Solver, (optional)
- EXACT - Exact: slower solver with the best results for coplanar faces.
- FLOAT - Float: simple solver with good performance, without support for overlapping geometry.
- MANIFOLD - Manifold: fastest solver, works only on manifold meshes but gives better results.
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

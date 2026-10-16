# bpy.ops.sculpt.face_set_extract

bpy.ops.sculpt. face_set_extract ( * , add_boundary_loop = True , smooth_iterations = 4 , apply_shrinkwrap = True , add_solidify = True )

Produce a fresh mesh form from the chosen face set

Parameters :

- add_boundary_loop ( bool ) – Add Boundary Loop, Introduce an additional edge loop for improved shape retention when a subdivision surface modifier is applied (optional)

- smooth_iterations ( int ) – Smooth Iterations, Smoothing passes applied to the fresh mesh (in [0, inf], optional)

- apply_shrinkwrap ( bool ) – Project to Sculpt, Conform the fresh mesh to the original sculpt (optional)

- add_solidify ( bool ) – Extract as Solid, Form the selection as a solid item with a solidify modifier (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

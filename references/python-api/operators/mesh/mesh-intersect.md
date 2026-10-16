# bpy.ops.mesh.intersect

bpy.ops.mesh. intersect ( * , mode = '`SELECT_UNSELECT`' , separate_mode = 'CUT' , threshold = 1e-06 , solver = 'EXACT' )

Form an intersection cut across polygons

Parameters :

- mode ( Literal [ 'SELECT' , '`SELECT_UNSELECT`' ] ) – Source, (optional)

- SELECT
Self Intersect – Self intersect selected faces.

- `SELECT_UNSELECT`
Selected/Unselected – Intersect selected with unselected faces.

- separate_mode ( Literal [ 'ALL' , 'CUT' , 'NONE' ] ) – Separate Mode, (optional)

- ALL
All – Separate all geometry from intersections.

- CUT
Cut – Cut into geometry keeping each side separate (Selected/Unselected only).

- NONE
Merge – Merge all geometry from the intersection.

- threshold ( float ) – Merge Threshold, (in [0, 0.01], optional)

- solver ( Literal [ 'FLOAT' , 'EXACT' ] ) – Solver, Which Intersect solver to use (optional)

- FLOAT
Float – Simple solver with good performance, without support for overlapping geometry.

- EXACT
Exact – Slower solver with the best results for coplanar faces.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

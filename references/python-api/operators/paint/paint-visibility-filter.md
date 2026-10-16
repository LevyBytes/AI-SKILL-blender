# bpy.ops.paint.visibility_filter

bpy.ops.paint. visibility_filter ( * , action = 'GROW' , iterations = 1 , auto_iteration_count = True ) 

Modify the visibility of the current mesh based on a filter operation

Parameters :

- action ( Literal [ 'GROW' , 'SHRINK' ] ) – Action, (optional)

- GROW
Grow Visibility – Expand visible regions by one face according to the mesh's topology.

- SHRINK
Shrink Visibility – Reduce visible regions by one face according to the mesh's topology.

- iterations ( int ) – Iterations, Number of times that the filter is going to be applied (in [1, 100], optional)

- auto_iteration_count ( bool ) – Auto Iteration Count, Use an automatic number of iterations based on the number of vertices of the sculpt (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

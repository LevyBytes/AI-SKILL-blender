# bpy.ops.sculpt.mask_filter

bpy.ops.sculpt. mask_filter ( * , filter_type = 'SMOOTH' , iterations = 1 , auto_iteration_count = True )

Enact a transformation to modify the present mask

Parameters :

- filter_type ( Literal [ 'SMOOTH' , 'SHARPEN' , 'GROW' , 'SHRINK' , '`CONTRAST_INCREASE`' , '`CONTRAST_DECREASE`' ] ) – Type, Transformation that will be applied to the mask (optional)

- iterations ( int ) – Iterations, Frequency of filter application (in [1, 100], optional)

- auto_iteration_count ( bool ) – Auto Iteration Count, Determine iteration frequency based on mesh vertex count (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.sculpt.paint_mask_slice

bpy.ops.sculpt. paint_mask_slice ( * , mask_threshold = 0.5 , fill_holes = True , new_object = True )

Divide the paint mask from the surface

Parameters :

- mask_threshold ( float ) – Threshold, Lowest mask level needed to classify the point viable for creating a surface from the original (in [0, 1], optional)

- fill_holes ( bool ) – Fill Holes, Seal openings after dividing the mask (optional)

- new_object ( bool ) – Slice to New Object, Form a distinct item from the divided mask (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.sculpt. paint_mask_slice ( * , mask_threshold = 0.5 , fill_holes = True , new_object = True )
Slices the paint mask out of the mesh.
Parameters:
- mask_threshold ( float ) – Threshold, Minimum mask value to consider the vertex valid to extract a face from the original mesh (in [0, 1], optional)
- fill_holes ( bool ) – Fill Holes, Fill holes after slicing the mask (optional)
- new_object ( bool ) – Slice to New Object, Create a new object from the sliced mask (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

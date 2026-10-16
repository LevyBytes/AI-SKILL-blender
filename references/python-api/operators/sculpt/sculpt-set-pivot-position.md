# bpy.ops.sculpt.set_pivot_position

bpy.ops.sculpt. set_pivot_position ( * , mode = 'UNMASKED' , mouse_x = 0.0 , mouse_y = 0.0 )

Establish where the sculpt deformation pivot is located

Parameters :

- mode ( Literal [ 'ORIGIN' , 'UNMASKED' , 'BORDER' , 'ACTIVE' , 'SURFACE' ] ) – Mode, (optional)

- ORIGIN
Origin – Sets the pivot to the origin of the sculpt.

- UNMASKED
Unmasked – Sets the pivot position to the average position of the unmasked vertices.

- BORDER
Mask Border – Sets the pivot position to the center of the border of the mask.

- ACTIVE
Active Vertex – Sets the pivot position to the active vertex position.

- SURFACE
Surface – Sets the pivot position to the surface under the cursor.

- mouse_x ( float ) – Mouse Position X, Position of the mouse used for "Surface" and "Active Vertex" mode (in [0, inf], optional)

- mouse_y ( float ) – Mouse Position Y, Position of the mouse used for "Surface" and "Active Vertex" mode (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.sculpt. set_pivot_position ( * , mode = 'UNMASKED' , mouse_x = 0.0 , mouse_y = 0.0 )
Sets the sculpt transform pivot position.
Parameters:
- mode ( Literal [ 'ORIGIN' , 'UNMASKED' , 'BORDER' , 'ACTIVE' , 'SURFACE' ] ) – Mode, (optional)
- ORIGIN — Origin: set the pivot to the sculpt's origin.
- UNMASKED — Unmasked: set the pivot to the average position of the unmasked vertices.
- BORDER — Mask Border: set the pivot to the center of the mask's border.
- ACTIVE — Active Vertex: set the pivot to the active vertex position.
- SURFACE — Surface: set the pivot to the surface under the cursor.
- mouse_x ( float ) – Mouse Position X, Position of the mouse used for "Surface" and "Active Vertex" mode (in [0, inf], optional)
- mouse_y ( float ) – Mouse Position Y, Position of the mouse used for "Surface" and "Active Vertex" mode (in [0, inf], optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

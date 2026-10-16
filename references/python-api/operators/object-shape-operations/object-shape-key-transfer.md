# bpy.ops.object.shape_key_transfer

bpy.ops.object. shape_key_transfer ( * , mode = 'OFFSET' , use_clamp = False ) 

Duplicates the shape key from another picked object onto the current one

Parameters :

- mode ( Literal [ 'OFFSET' , '`RELATIVE_FACE`' , '`RELATIVE_EDGE`' ] ) – Transformation Mode, How to position the shape in relation to the fresh configuration (optional)

- OFFSET
Offset – Applies the relative positional movement.

- `RELATIVE_FACE`
Relative Face – Computes relative placement (based on faces).

- `RELATIVE_EDGE`
Relative Edge – Computes relative placement (based on edges).

- use_clamp ( bool ) – Clamp Offset, Limit the transformation so vertices stay within original movement distances (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/object.py:515

[Related references](INDEX.md).

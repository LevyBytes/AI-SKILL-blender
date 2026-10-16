# bpy.ops.mesh.poke

bpy.ops.mesh. poke ( * , offset = 0.0 , use_relative_offset = False , center_mode = '`MEDIAN_WEIGHTED`' )

Subdivide a polygon into a radial fan

Parameters :

- offset ( float ) – Poke Offset, Poke Offset (in [-1000, 1000], optional)

- use_relative_offset ( bool ) – Offset Relative, Scale the offset by surrounding geometry (optional)

- center_mode ( Literal [ '`MEDIAN_WEIGHTED`' , 'MEDIAN' , 'BOUNDS' ] ) – Poke Center, Poke face center calculation (optional)

- `MEDIAN_WEIGHTED`
Weighted Median – Weighted median face center.

- MEDIAN
Median – Median face center.

- BOUNDS
Bounds – Face bounds center.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

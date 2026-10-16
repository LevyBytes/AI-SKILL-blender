# bpy.ops.sculpt.uv_sculpt_relax

bpy.ops.sculpt. uv_sculpt_relax ( * , use_invert = False , relax_method = 'LAPLACIAN' )

Unwind UVs

Parameters :

- use_invert ( bool ) – Invert, Reverse action during the mark (optional)

- relax_method ( Literal [ 'LAPLACIAN' , 'HC' , 'COTAN' ] ) – Relax Method, Formula used for UV unwinding (optional)

- LAPLACIAN
Laplacian – Use Laplacian method for relaxation.

- HC
HC – Use HC method for relaxation.

- COTAN
Geometry – Use Geometry (cotangent) relaxation, making UVs follow the underlying 3D geometry.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

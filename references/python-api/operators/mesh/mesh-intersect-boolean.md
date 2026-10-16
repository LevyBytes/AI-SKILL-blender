# bpy.ops.mesh.intersect_boolean

bpy.ops.mesh. intersect_boolean ( * , operation = 'DIFFERENCE' , use_swap = False , use_self = False , threshold = 1e-06 , solver = 'EXACT' )

Subtract solid geometry from picked to unpicked

Parameters :

- operation ( Literal [ 'INTERSECT' , 'UNION' , 'DIFFERENCE' ] ) – Boolean Operation, Which boolean operation to apply (optional)

- use_swap ( bool ) – Swap, Use with difference intersection to swap which side is kept (optional)

- use_self ( bool ) – Self Intersection, Do self-union or self-intersection (optional)

- threshold ( float ) – Merge Threshold, (in [0, 0.01], optional)

- solver ( Literal [ 'FLOAT' , 'EXACT' ] ) – Solver, Which Boolean solver to use (optional)

- FLOAT
Float – Faster solver, some limitations.

- EXACT
Exact – Exact solver, slower, handles more cases.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

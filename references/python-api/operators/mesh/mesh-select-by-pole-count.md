# bpy.ops.mesh.select_by_pole_count

bpy.ops.mesh. select_by_pole_count ( * , pole_count = 4 , type = 'NOTEQUAL' , extend = False , exclude_nonmanifold = True ) 

Highlight vertices based on how many edges connect to them. In edge and face pick mode the linked forms are highlighted

Parameters :

- pole_count ( int ) – Pole Count, (in [0, inf], optional)

- type ( Literal [ 'LESS' , 'EQUAL' , 'GREATER' , 'NOTEQUAL' ] ) – Type, The kind of comparison to perform (optional)

- extend ( bool ) – Extend, Grow the current highlighting (optional)

- exclude_nonmanifold ( bool ) – Exclude Non Manifold, Leave out poles that are not manifold (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

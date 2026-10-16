# bpy.types.GreasePencilDrawing: set_types, set_vertex_weights

set_types ( * , type = '`CATMULL_ROM`' , indices = (0,) )

Set the curve type. If indices are provided, set only the types with the given curve indices.

Parameters :

- type (Literal[Curves Type Items]) – Type, (optional)

- indices ( Sequence [ int ] ) – Indices, The indices of the curves to resize (array of 1 items, in [0, inf], optional)
set_vertex_weights ( vertex_group_name , indices , weights , * , assign_mode = 'REPLACE' )

Set the weights of vertices in a grease pencil drawing

Parameters :

- vertex_group_name ( str ) – Vertex Group Name, Name of the vertex group (never None)

- indices ( Sequence [ int ] ) – Indices, The point indices in the vertex group to modify (array of 1 items, in [-inf, inf])

- weights ( Sequence [ float ] ) – Weights, The weight for each corresponding index in the indices array (array of 1 items, in [0, 1])

- assign_mode ( Literal [ 'REPLACE' , 'ADD' , 'SUBTRACT' ] ) – (optional)

- REPLACE
Replace – Replace.

- ADD
Add – Add.

- SUBTRACT
Subtract – Subtract.

[Related references](INDEX.md).

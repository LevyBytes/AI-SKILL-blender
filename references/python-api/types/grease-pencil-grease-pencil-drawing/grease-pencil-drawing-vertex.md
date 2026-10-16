# bpy.types.GreasePencilDrawing: vertex_group_assign, vertex_group_remove

vertex_group_assign ( vgroup_name , indices_ptr , weight )

Assign points to vertex group

Parameters :

- vgroup_name ( str ) – Vertex Group Name, Name of the vertex group (never None)

- indices_ptr ( Sequence [ int ] ) – Indices, The point indices to assign the weight to (array of 1 items, in [-inf, inf])

- weight ( float ) – Vertex weight (in [0, 1])
vertex_group_remove ( vgroup_name , indices_ptr )

Remove points from vertex group

Parameters :

- vgroup_name ( str ) – Vertex Group Name, Name of the vertex group (never None)

- indices_ptr ( Sequence [ int ] ) – Indices, The point indices to remove from the vertex group (array of 1 items, in [-inf, inf])

[Related references](INDEX.md).

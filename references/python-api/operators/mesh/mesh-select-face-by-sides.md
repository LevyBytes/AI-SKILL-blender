# bpy.ops.mesh.select_face_by_sides

bpy.ops.mesh. select_face_by_sides ( * , number = 4 , type = 'EQUAL' , extend = True ) 

Pick vertices or face regions by how many edges frame them

Parameters :

- number ( int ) – Number of Vertices, (in [3, inf], optional)

- type ( Literal [ 'LESS' , 'EQUAL' , 'GREATER' , 'NOTEQUAL' ] ) – Type, The kind of comparison to perform (optional)

- extend ( bool ) – Extend, Grow the current highlighting (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

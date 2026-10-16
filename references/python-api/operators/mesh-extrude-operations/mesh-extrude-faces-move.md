# bpy.ops.mesh.extrude_faces_move

bpy.ops.mesh. extrude_faces_move ( * , `MESH_OT`_extrude_faces_indiv = {} , `TRANSFORM_OT`_shrink_fatten = {} )

Protrude every face in turn along its local surface normal

Parameters :

- `MESH_OT`_extrude_faces_indiv ( dict [ str , Any ] ) – Extrude Individual Faces, Extrude individual faces only (optional, bpy.ops.mesh.extrude_faces_indiv() keyword arguments)

- `TRANSFORM_OT`_shrink_fatten ( dict [ str , Any ] ) – Shrink/Fatten, Shrink/fatten selected vertices along normals (optional, bpy.ops.transform.shrink_fatten() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

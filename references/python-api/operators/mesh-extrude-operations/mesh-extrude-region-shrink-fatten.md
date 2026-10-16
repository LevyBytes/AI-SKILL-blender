# bpy.ops.mesh.extrude_region_shrink_fatten

bpy.ops.mesh. extrude_region_shrink_fatten ( * , `MESH_OT`_extrude_region = {} , `TRANSFORM_OT`_shrink_fatten = {} )

Push a zone outward matching its local surface direction

Parameters :

- `MESH_OT`_extrude_region ( dict [ str , Any ] ) – Extrude Region, Extrude region of faces (optional, bpy.ops.mesh.extrude_region() keyword arguments)

- `TRANSFORM_OT`_shrink_fatten ( dict [ str , Any ] ) – Shrink/Fatten, Shrink/fatten selected vertices along normals (optional, bpy.ops.transform.shrink_fatten() keyword arguments)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

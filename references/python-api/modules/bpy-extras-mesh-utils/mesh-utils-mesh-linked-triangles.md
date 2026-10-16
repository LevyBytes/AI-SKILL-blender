# bpy_extras.mesh_utils: bpy_extras.mesh_utils. mesh_linked_triangles ( mesh )

bpy_extras.mesh_utils. mesh_linked_triangles ( mesh ) 

Break the mesh into connected triangles; handy for splitting cubes apart from
other geometry inside a single mesh data-block.

Parameters :

mesh (bpy.types.Mesh) – the mesh used to group with.

Returns :

Lists of lists containing triangles.

Return type :

list[list[bpy.types.MeshLoopTriangle]]

[Related references](INDEX.md).

# bpy.types.Mesh: normals_split_custom_set, normals_split_custom_set_from_vertices

normals_split_custom_set ( normals )

Assign this mesh's custom normals (pass zero-vectors where you want the automatic ones kept)

Parameters :

normals ( Sequence [ float ] ) – Normals (multi-dimensional array of 1 * 3 items, in [-1, 1])
normals_split_custom_set_from_vertices ( normals )

Assign this mesh's custom normals from the vertices' normals (pass zero-vectors where you want the automatic ones kept)

Parameters :

normals ( Sequence [ float ] ) – Normals (multi-dimensional array of 1 * 3 items, in [-1, 1])

[Related references](INDEX.md).

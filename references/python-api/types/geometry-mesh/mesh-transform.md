# bpy.types.Mesh: transform

transform ( matrix , * , shape_keys = False )

Apply a matrix to the mesh's vertices (Warning: a negative matrix flips the normals)

Parameters :

- matrix (mathutils.Matrix) – Matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])

- shape_keys ( bool ) – Transform Shape Keys (optional)

[Related references](INDEX.md).

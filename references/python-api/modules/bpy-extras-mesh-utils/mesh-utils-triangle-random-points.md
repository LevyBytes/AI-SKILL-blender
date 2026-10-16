# bpy_extras.mesh_utils: bpy_extras.mesh_utils. triangle_random_points ( num_points , loop_triangles )

bpy_extras.mesh_utils. triangle_random_points ( num_points , loop_triangles ) 

Produce a list of random points scattered over mesh loop triangles.

Parameters :

- num_points ( int ) – The number of random points to generate on each triangle.

- loop_triangles (Sequence[bpy.types.MeshLoopTriangle]) – Sequence of the triangles to generate points on.

Returns :

List of random points over all triangles.

Return type :

list[mathutils.Vector]

[Related references](INDEX.md).

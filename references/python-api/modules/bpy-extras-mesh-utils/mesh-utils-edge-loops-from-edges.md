# bpy_extras.mesh_utils: bpy_extras.mesh_utils. edge_loops_from_edges ( mesh , edges = None )

bpy_extras.mesh_utils. edge_loops_from_edges ( mesh , edges = None ) 

Edge loops defined by edges.

Accepts mesh.edges or a list of edges and gives back the edge loops
as lists of vertex indices.
On closed loops the first and last values are equal.

Parameters :

- mesh (bpy.types.Mesh) – The mesh to extract edge loops from.

- edges (list[bpy.types.MeshEdge] | None) – Edges to use, or None to use all edges in the mesh.

Returns :

A list of edge loops, each a list of vertex indices.

Return type :

list[list[int]]

[Related references](INDEX.md).

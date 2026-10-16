# bpy.ops.mesh.remove_doubles

bpy.ops.mesh. remove_doubles ( * , threshold = 0.0001 , use_centroid = True , use_unselected = False , use_sharp_edge_from_normals = False )

Join points by their closeness

Parameters :

- threshold ( float ) – Merge Distance, Maximum distance between elements to merge (in [1e-06, 50], optional)

- use_centroid ( bool ) – Centroid Merge, Move vertices to the centroid of the duplicate cluster, otherwise the vertex closest to the centroid is used. (optional)

- use_unselected ( bool ) – Unselected, Merge selected to other unselected vertices (optional)

- use_sharp_edge_from_normals ( bool ) – Sharp Edges, Calculate sharp edges using custom normal data (when available) (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

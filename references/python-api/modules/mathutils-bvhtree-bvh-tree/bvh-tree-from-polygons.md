# mathutils.bvhtree.BVHTree: classmethod FromPolygons ( vertices , polygons , * , all_triangles = False , epsilon = 0.0 )

classmethod FromPolygons ( vertices , polygons , * , all_triangles = False , epsilon = 0.0 )

BVH tree assembled from geometry handed in through the arguments.

Parameters :

- vertices ( Sequence [ Sequence [ float ] ] ) – float triplets each representing (x, y, z) coordinates.

- polygons ( Sequence [ Sequence [ int ] ] ) – Sequence of polygons, each containing indices to the vertices argument.

- all_triangles ( bool ) – Use when all polygons are triangles for more efficient conversion.

- epsilon ( float ) – Increase the threshold for detecting overlap and raycast hits.

Returns :

BVHTree from polygon data.

Return type :

BVHTree

[Related references](INDEX.md).

# mathutils.geometry: mathutils.geometry. tessellate_polygon ( polylines , / )

mathutils.geometry. tessellate_polygon ( polylines , / )

Accepts a list of polylines (each point being a pair or triplet of numbers) and returns the point indices for that polyline filled in with triangles. Degenerate geometry (such as zero-length lines from repeated identical points) isn't handled.

Parameters :

polylines ( Sequence [ Sequence [ Sequence [ float ] ] ] ) – Polygons where each polygon is a sequence of 2D or 3D points.

Returns :

A list of triangles.

Return type :

list[tuple[int, int, int]]

[Related references](INDEX.md).

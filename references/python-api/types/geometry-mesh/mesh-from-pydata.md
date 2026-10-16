# bpy.types.Mesh: from_pydata

from_pydata ( vertices , edges , faces , shade_flat = True )

Build a mesh out of vertex, edge, and face lists.
This is the stopgap until a nicer geometry-creation path exists.

Parameters :

- vertices ( Iterable [ Sequence [ float ] ] ) – one float triplet per point, holding its (X, Y, Z)
eg: [(0.0, 1.0, 0.5), …].

- edges ( Iterable [ Sequence [ int ] ] ) – int pairs, where each pair holds two indices back into the
vertices argument. eg: [(1, 2), …]

Hand in an empty iterable and the edges get worked out from the polygons instead.

- faces ( Iterable [ Sequence [ int ] ] ) – an iterator over faces, where each face holds three or more indices back into
the vertices argument. eg: [(5, 6, 8, 9), (1, 2, 3), …]

Warning

Invalid mesh data
(out of range indices, edges with matching indices,
2 sided faces… etc) are not prevented.
If the data used for mesh creation isn’t known to be valid,
run Mesh.validate after this function.

[Related references](INDEX.md).

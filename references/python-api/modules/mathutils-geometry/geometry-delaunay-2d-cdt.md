# mathutils.geometry: mathutils.geometry. delaunay_2d_cdt ( vert_coords , edges , faces , output_type , epsilon , need_ids = True , / )

mathutils.geometry. delaunay_2d_cdt ( vert_coords , edges , faces , output_type , epsilon , need_ids = True , / )

Builds the Constrained Delaunay Triangulation over a collection of vertices, where the given edges and faces are forced to show up in the result. Depending on the output type, some triangles get consumed or fused with neighbors. The verts that come back may be reordered relative to the input, nudged a little, and merged with nearby ones. Each of the three returned orig lists maps, per vert, edge, and face, to the input element indices that line up positionally with each output element. The edge orig indices begin with the input edges and then run on with the edges that each face implies (n of them for an n-gon). When the need_ids argument is passed as False, the routine skips building the orig arrays, which can shave off some time.

Parameters :

- vert_coords (Sequence[mathutils.Vector]) – Vertex coordinates (2d)

- edges ( Sequence [ tuple [ int , int ] ] ) – Edges, as pairs of indices in vert_coords

- faces ( Sequence [ Sequence [ int ] ] ) – Faces, each sublist is a face, as indices in vert_coords (CCW oriented).

- output_type ( int ) – What output looks like. 0 => triangles with convex hull. 1 => triangles inside constraints. 2 => the input constraints, intersected. 3 => like 2 but detect holes and omit them from output. 4 => like 2 but with extra edges to make valid BMesh faces. 5 => like 4 but detect holes and omit them from output.

- epsilon ( float ) – For nearness tests; should not be zero

- need_ids ( bool ) – are the orig output arrays needed?

Returns :

Output tuple, (vert_coords, edges, faces, orig_verts, orig_edges, orig_faces)

Return type :

tuple[list[mathutils.Vector], list[tuple[int, int]], list[list[int]], list[list[int]], list[list[int]], list[list[int]]]

[Related references](INDEX.md).

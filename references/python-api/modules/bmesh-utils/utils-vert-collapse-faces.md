# bmesh.utils: bmesh.utils. vert_collapse_faces ( vert , edge , fac , join_faces )

bmesh.utils. vert_collapse_faces ( vert , edge , fac , join_faces )
Collapses a vertex that has only two manifold edges onto a vertex it shares an edge with.
Parameters:
- vert (bmesh.types.BMVert) – The vert that will be collapsed.
- edge (bmesh.types.BMEdge) – The edge to collapse into.
- fac ( float ) – The factor to use when merging customdata [0 - 1].
- join_faces ( bool ) – When true the faces around the vertex will be joined, otherwise collapse the vertex by merging the 2 edges this vertex connects to into one.
Returns: The resulting edge from the collapse operation.
Return type: bmesh.types.BMEdge

[Related references](INDEX.md).

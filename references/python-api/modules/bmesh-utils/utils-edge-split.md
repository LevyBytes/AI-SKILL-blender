# bmesh.utils: bmesh.utils. edge_split ( edge , vert , fac )

bmesh.utils. edge_split ( edge , vert , fac )
Splits an edge and returns the newly created data.
Parameters:
- edge (bmesh.types.BMEdge) – The edge to split.
- vert (bmesh.types.BMVert) – One of the verts on the edge, defines the split direction.
- fac ( float ) – The point on the edge where the new vert will be created [0 - 1].
Returns: The newly created (edge, vert) pair.
Return type: tuple[bmesh.types.BMEdge, bmesh.types.BMVert]

[Related references](INDEX.md).

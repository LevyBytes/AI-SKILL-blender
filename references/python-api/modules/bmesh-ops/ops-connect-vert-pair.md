# bmesh.ops: bmesh.ops. connect_vert_pair ( bm , verts =  , verts_exclude =  , faces_exclude =  )

bmesh.ops. connect_vert_pair ( bm , verts = [] , verts_exclude = [] , faces_exclude = [] ) 

Connect Vert Pair.

Connect a pair of vertices by splitting faces along the shortest path between them.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- verts (list[bmesh.types.BMVert]) – Input vertices.

- verts_exclude (list[bmesh.types.BMVert]) – Input vertices to explicitly exclude from connecting.

- faces_exclude (list[bmesh.types.BMFace]) – Input faces to explicitly exclude from connecting.

Returns :

- edges :

type list[bmesh.types.BMEdge]

Return type :

dict[str, Any]

[Related references](INDEX.md).

# bmesh.ops: bmesh.ops. connect_verts ( bm , verts =  , faces_exclude =  , check_degenerate = False )

bmesh.ops. connect_verts ( bm , verts = [] , faces_exclude = [] , check_degenerate = False ) 

Connect Verts.

Split faces by adding edges that connect verts .

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- verts (list[bmesh.types.BMVert]) – Input vertices.

- faces_exclude (list[bmesh.types.BMFace]) – Input faces to explicitly exclude from connecting.

- check_degenerate ( bool ) – Prevent splits with overlaps & intersections.

Returns :

- edges :

type list[bmesh.types.BMEdge]

Return type :

dict[str, Any]

[Related references](INDEX.md).

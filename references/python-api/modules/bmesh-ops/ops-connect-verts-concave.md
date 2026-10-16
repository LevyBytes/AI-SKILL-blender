# bmesh.ops: bmesh.ops. connect_verts_concave ( bm , faces =  )

bmesh.ops. connect_verts_concave ( bm , faces = [] ) 

Connect Verts to form Convex Faces.

Splits concave faces into convex faces.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- faces (list[bmesh.types.BMFace]) – Input faces.

Returns :

- edges :

type list[bmesh.types.BMEdge]

- faces :

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

# bmesh.ops: bmesh.ops. connect_verts_nonplanar ( bm , angle_limit = 0 , faces =  )

bmesh.ops. connect_verts_nonplanar ( bm , angle_limit = 0 , faces = [] ) 

Connect Verts Across non Planar Faces.

Split faces by connecting edges along non planar faces .

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- angle_limit ( float ) – Maximum angle of non-planarity before splitting (radians).

- faces (list[bmesh.types.BMFace]) – Input faces.

Returns :

- edges :

type list[bmesh.types.BMEdge]

- faces :

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

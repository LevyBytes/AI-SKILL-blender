# bmesh.ops: bmesh.ops. triangulate ( bm , faces =  , quad_method = 'BEAUTY' , ngon_method = 'BEAUTY' )

bmesh.ops. triangulate ( bm , faces = [] , quad_method = 'BEAUTY' , ngon_method = 'BEAUTY' ) 

Triangulate.

Triangulate faces, splitting quads and n-gons into triangles.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- faces (list[bmesh.types.BMFace]) – Input faces.

- quad_method ( Literal [ 'BEAUTY' , 'FIXED' , 'ALTERNATE' , '`SHORT_EDGE`' , '`LONG_EDGE`' ] ) – Method for splitting the quads into triangles.

- ngon_method ( Literal [ 'BEAUTY' , '`EAR_CLIP`' ] ) – Method for splitting the polygons into triangles.

Returns :

- edges :

type list[bmesh.types.BMEdge]

- faces :

type list[bmesh.types.BMFace]

- face_map :

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- face_map_double :
Duplicate faces.

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

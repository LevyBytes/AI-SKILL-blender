# bmesh.ops: bmesh.ops. delete ( bm , geom =  , context = 'VERTS' )

bmesh.ops. delete ( bm , geom = [] , context = 'VERTS' ) 

Delete Geometry.

Utility operator to delete geometry.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.

- context ( Literal [ 'VERTS' , 'EDGES' , '`FACES_ONLY`' , '`EDGES_FACES`' , 'FACES' , '`FACES_KEEP_BOUNDARY`' , '`TAGGED_ONLY`' ] ) – Geometry types to delete.

[Related references](INDEX.md).

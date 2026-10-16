# bmesh.ops: bmesh.ops. holes_fill ( bm , edges =  , sides = 0 )

bmesh.ops. holes_fill ( bm , edges = [] , sides = 0 ) 

Fill Holes.

Fill boundary edges with faces, copying surrounding custom-data.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- sides ( int ) – Maximum number of sides for holes to fill (holes with more edges are skipped).

Returns :

- faces :
New faces.

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

# bmesh.ops: bmesh.ops. edgeloop_fill ( bm , edges =  , mat_nr = 0 , use_smooth = False )

bmesh.ops. edgeloop_fill ( bm , edges = [] , mat_nr = 0 , use_smooth = False ) 

Edge Loop Fill.

Create faces defined by one or more non overlapping edge loops.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- mat_nr ( int ) – Material to use.

- use_smooth ( bool ) – Smooth state to use.

Returns :

- faces :
New faces.

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

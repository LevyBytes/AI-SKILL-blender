# bmesh.ops: bmesh.ops. edgenet_fill ( bm , edges =  , mat_nr = 0 , use_smooth = False , sides = 0 )

bmesh.ops. edgenet_fill ( bm , edges = [] , mat_nr = 0 , use_smooth = False , sides = 0 ) 

Edge Net Fill.

Create faces defined by enclosed edges.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- mat_nr ( int ) – Material to use.

- use_smooth ( bool ) – Smooth state to use.

- sides ( int ) – Maximum number of sides for created faces.

Returns :

- faces :
New faces.

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

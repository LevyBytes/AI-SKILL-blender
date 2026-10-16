# bmesh.ops: bmesh.ops. grid_fill ( bm , edges =  , mat_nr = 0 , use_smooth = False , use_interp_simple = False )

bmesh.ops. grid_fill ( bm , edges = [] , mat_nr = 0 , use_smooth = False , use_interp_simple = False ) 

Grid Fill.

Create faces defined by 2 disconnected edge loops (which share edges).

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- mat_nr ( int ) – Material to use.

- use_smooth ( bool ) – Smooth state to use.

- use_interp_simple ( bool ) – Use simple interpolation.

Returns :

- faces :
New faces.

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

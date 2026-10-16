# bmesh.ops: bmesh.ops. dissolve_limit ( bm , angle_limit = 0 , use_dissolve_boundaries = False , verts =  , edges =  , delimit = set() )

bmesh.ops. dissolve_limit ( bm , angle_limit = 0 , use_dissolve_boundaries = False , verts = [] , edges = [] , delimit = set() ) 

Limited Dissolve.

Dissolve planar faces and co-linear edges.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- angle_limit ( float ) – Maximum angle (radians) between face normals for dissolving.

- use_dissolve_boundaries ( bool ) – Dissolve all vertices in between face boundaries.

- verts (list[bmesh.types.BMVert]) – Input vertices.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- delimit ( set [ Literal [ 'NORMAL' , 'MATERIAL' , 'SEAM' , 'SHARP' , 'UV' ] ] ) – Delimit dissolve operation.

Returns :

- region :

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

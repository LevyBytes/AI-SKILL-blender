# bmesh.ops: bmesh.ops. dissolve_edges ( bm , edges =  , use_verts = False , use_face_split = False , angle_threshold = 0 )

bmesh.ops. dissolve_edges ( bm , edges = [] , use_verts = False , use_face_split = False , angle_threshold = 0 ) 

Dissolve Edges.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- use_verts ( bool ) – Dissolve verts left between only 2 edges.

- use_face_split ( bool ) – Split off face corners to maintain surrounding geometry.

- angle_threshold ( float ) – Do not dissolve verts between 2 edges when their angle exceeds this threshold.
Disabled by default.

Returns :

- region :

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

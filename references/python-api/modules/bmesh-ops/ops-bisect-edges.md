# bmesh.ops: bmesh.ops. bisect_edges ( bm , edges =  , cuts = 0 , edge_percents = {} )

bmesh.ops. bisect_edges ( bm , edges = [] , cuts = 0 , edge_percents = {} ) 

Edge Bisect.

Divides input edges into segments (creating 2-valence verts).

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- cuts ( int ) – Number of cuts.

- edge_percents (dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, float]) – Undocumented.

Returns :

- geom_split :
Newly created vertices and edges.

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

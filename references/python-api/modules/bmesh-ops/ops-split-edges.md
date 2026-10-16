# bmesh.ops: bmesh.ops. split_edges ( bm , edges =  , verts =  , use_verts = False )

bmesh.ops. split_edges ( bm , edges = [] , verts = [] , use_verts = False ) 

Edge Split.

Disconnects faces along input edges.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- verts (list[bmesh.types.BMVert]) – Optional tag verts, use to have greater control of splits.

- use_verts ( bool ) – Use verts for splitting, else just find verts to split from edges.

Returns :

- edges :
The original edges that were disconnected.

type list[bmesh.types.BMEdge]

Return type :

dict[str, Any]

[Related references](INDEX.md).

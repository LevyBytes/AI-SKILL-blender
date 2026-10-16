# bmesh.ops: bmesh.ops. extrude_vert_indiv ( bm , verts =  , use_select_history = False )

bmesh.ops. extrude_vert_indiv ( bm , verts = [] , use_select_history = False ) 

Individual Vertex Extrude.

Extrudes individual vertices, creating new vertices connected by wire edges.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- verts (list[bmesh.types.BMVert]) – Input vertices.

- use_select_history ( bool ) – Preserve the selection history in the extruded geometry.

Returns :

- edges :
Output wire edges.

type list[bmesh.types.BMEdge]

- verts :
Output vertices.

type list[bmesh.types.BMVert]

Return type :

dict[str, Any]

[Related references](INDEX.md).

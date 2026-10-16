# bmesh.ops: bmesh.ops. extrude_edge_only ( bm , edges =  , use_normal_flip = False , use_select_history = False )

bmesh.ops. extrude_edge_only ( bm , edges = [] , use_normal_flip = False , use_select_history = False ) 

Extrude Only Edges.

Extrudes Edges into faces, note that this is very simple, there's no fancy
winged extrusion.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- use_normal_flip ( bool ) – Create faces with reversed direction.

- use_select_history ( bool ) – Preserve the selection history in the extruded geometry.

Returns :

- geom :
Output geometry.

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

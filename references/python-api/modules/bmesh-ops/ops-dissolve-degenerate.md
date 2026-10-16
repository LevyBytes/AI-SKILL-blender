# bmesh.ops: bmesh.ops. dissolve_degenerate ( bm , dist = 0 , edges =  )

bmesh.ops. dissolve_degenerate ( bm , dist = 0 , edges = [] ) 

Degenerate Dissolve.

Dissolve edges with no length, faces with no area.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- dist ( float ) – Maximum distance to consider degenerate.

- edges (list[bmesh.types.BMEdge]) – Input edges.

[Related references](INDEX.md).

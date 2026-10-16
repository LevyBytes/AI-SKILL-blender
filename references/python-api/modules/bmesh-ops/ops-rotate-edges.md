# bmesh.ops: bmesh.ops. rotate_edges ( bm , edges =  , use_ccw = False )

bmesh.ops. rotate_edges ( bm , edges = [] , use_ccw = False ) 

Edge Rotate.

Rotates edges topologically. Also known as "spin edge" to some people.
Simple example: [/] becomes [|] then [\\] .

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- use_ccw ( bool ) – Turn edges counter-clockwise if true, else clockwise.

Returns :

- edges :
Newly spun edges.

type list[bmesh.types.BMEdge]

Return type :

dict[str, Any]

[Related references](INDEX.md).

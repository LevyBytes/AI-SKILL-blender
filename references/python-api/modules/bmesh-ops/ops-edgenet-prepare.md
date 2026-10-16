# bmesh.ops: bmesh.ops. edgenet_prepare ( bm , edges =  )

bmesh.ops. edgenet_prepare ( bm , edges = [] ) 

Edge-net Prepare.

Identifies several useful edge loop cases and modifies them so
they'll become a face when edgenet_fill is called. The cases covered are:

- One single loop; an edge is added to connect the ends

- Two loops; two edges are added to connect the endpoints (based on the
shortest distance between each endpoint).

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

Returns :

- edges :
New edges.

type list[bmesh.types.BMEdge]

Return type :

dict[str, Any]

[Related references](INDEX.md).

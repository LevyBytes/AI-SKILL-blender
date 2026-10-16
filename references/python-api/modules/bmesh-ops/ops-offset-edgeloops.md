# bmesh.ops: bmesh.ops. offset_edgeloops ( bm , edges =  , use_cap_endpoint = False )

bmesh.ops. offset_edgeloops ( bm , edges = [] , use_cap_endpoint = False )
Edge-loop Offset. Adds edge loops using a simple edge-outset method.
Parameters:
- bm (bmesh.types.BMesh) – The bmesh to act on.
- edges (list[bmesh.types.BMEdge]) – Input edges.
- use_cap_endpoint ( bool ) – Extend loop around end-points.
Returns:
- edges: Output edges. type list[bmesh.types.BMEdge]
Return type: dict[str, Any]

[Related references](INDEX.md).

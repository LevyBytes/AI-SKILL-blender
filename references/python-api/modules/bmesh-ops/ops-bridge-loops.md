# bmesh.ops: bmesh.ops. bridge_loops ( bm , edges =  , use_pairs = False , use_cyclic = False , use_merge = False , merge_factor = 0 , twist_offset = 0 )

bmesh.ops. bridge_loops ( bm , edges = [] , use_pairs = False , use_cyclic = False , use_merge = False , merge_factor = 0 , twist_offset = 0 ) 

Bridge edge loops with faces.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- use_pairs ( bool ) – Undocumented.

- use_cyclic ( bool ) – Undocumented.

- use_merge ( bool ) – Merge rather than creating faces.

- merge_factor ( float ) – Merge factor.

- twist_offset ( int ) – Twist offset for closed loops.

Returns :

- faces :
New faces.

type list[bmesh.types.BMFace]

- edges :
New edges.

type list[bmesh.types.BMEdge]

Return type :

dict[str, Any]

[Related references](INDEX.md).

# bmesh.ops: bmesh.ops. find_doubles ( bm , verts =  , keep_verts =  , use_connected = False , dist = 0 )

bmesh.ops. find_doubles ( bm , verts = [] , keep_verts = [] , use_connected = False , dist = 0 ) 

Find Doubles.

Identifies which vertices should be merged together.
Returns a mapping suitable for the weld verts BMOP.

If keep_verts is used, vertices outside that set can only be merged
with vertices in that set.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- verts (list[bmesh.types.BMVert]) – Input vertices.

- keep_verts (list[bmesh.types.BMVert]) – List of verts to keep.

- use_connected ( bool ) – Limit the search for doubles by connected geometry.

- dist ( float ) – Maximum distance.

Returns :

- targetmap :

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

# bmesh.ops: bmesh.ops. remove_doubles ( bm , verts =  , use_connected = False , dist = 0 )

bmesh.ops. remove_doubles ( bm , verts = [] , use_connected = False , dist = 0 ) 

Remove Doubles.

Locates groups of vertices within a threshold distance and joins them,
using the weld verts BMOP.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- verts (list[bmesh.types.BMVert]) – Input verts.

- use_connected ( bool ) – Limit the search for doubles by connected geometry.

- dist ( float ) – Maximum distance.

[Related references](INDEX.md).

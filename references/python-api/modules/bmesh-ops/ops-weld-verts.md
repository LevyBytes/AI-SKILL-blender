# bmesh.ops: bmesh.ops. weld_verts ( bm , targetmap = {} , use_centroid = False )

bmesh.ops. weld_verts ( bm , targetmap = {} , use_centroid = False ) 

Weld Verts.

Fuses verts together (like remove doubles, merge, etc, which
use or will use this BMOP). You supply mappings from vertices to the vertices
they should merge with.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- targetmap (dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Maps welded vertices to where they merge.

- use_centroid ( bool ) – Merge vertices to their centroid position,
otherwise use the position of the target vertex.

[Related references](INDEX.md).

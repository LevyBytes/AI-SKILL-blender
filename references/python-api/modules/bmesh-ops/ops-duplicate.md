# bmesh.ops: bmesh.ops. duplicate ( bm , geom =  , dest = None , use_select_history = False , use_edge_flip_from_face = False )

bmesh.ops. duplicate ( bm , geom = [] , dest = None , use_select_history = False , use_edge_flip_from_face = False ) 

Duplicate Geometry.

Utility operator to duplicate geometry,
optionally into a destination mesh.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.

- dest (bmesh.types.BMesh | None) – Destination bmesh, if None will use current one.

- use_select_history ( bool ) – Preserve the selection history in the duplicated geometry.

- use_edge_flip_from_face ( bool ) – Copy edge flip state from connected faces.

Returns :

- geom_orig :

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- geom :

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- vert_map :

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- edge_map :

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- face_map :

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- boundary_map :
Boundary edges from the split geometry that maps edges from the original geometry
to the destination edges.

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- isovert_map :

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

# bmesh.ops: bmesh.ops. split ( bm , geom =  , dest = None , use_only_faces = False )

bmesh.ops. split ( bm , geom = [] , dest = None , use_only_faces = False ) 

Split Off Geometry.

Disconnect geometry from adjacent edges and faces,
optionally into a destination mesh.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.

- dest (bmesh.types.BMesh | None) – Destination bmesh, if None will use current one.

- use_only_faces ( bool ) – When enabled, don't duplicate loose verts/edges.

Returns :

- geom :

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- boundary_map :
Boundary edges from the split geometry that maps edges from the original geometry
to the destination edges.

When the source edges have been deleted, the destination edge will be used
for both the key and the value.

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- isovert_map :

type dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

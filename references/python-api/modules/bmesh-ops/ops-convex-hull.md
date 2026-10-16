# bmesh.ops: bmesh.ops. convex_hull ( bm , input =  , use_existing_faces = False )

bmesh.ops. convex_hull ( bm , input = [] , use_existing_faces = False )
Convex Hull. Builds a convex hull from the vertices supplied in input. With use_existing_faces true, the hull won't output triangles already covered by a pre-existing face. Every hull vertex, face, and edge is added to geom.out; any input elements that end up inside the hull (not used by an output face) are added to the geom_interior.out slot; the geom_unused.out slot holds all interior geometry that is completely unused; and geom_holes.out holds the edges and faces that were in the input and form part of the hull.
Parameters:
- bm (bmesh.types.BMesh) – The bmesh to act on.
- input (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.
- use_existing_faces ( bool ) – Skip hull triangles that are covered by a pre-existing face.
Returns:
- geom: type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]
- geom_interior: type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]
- geom_unused: type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]
- geom_holes: type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]
Return type: dict[str, Any]

[Related references](INDEX.md).

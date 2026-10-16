# bmesh.ops: bmesh.ops. symmetrize ( bm , input =  , direction = '-X' , dist = 0 , use_shapekey = False )

bmesh.ops. symmetrize ( bm , input = [] , direction = '-X' , dist = 0 , use_shapekey = False )
Symmetrize. Makes the mesh elements in the input slot symmetrical. Unlike ordinary mirroring it copies in only one direction, set by the direction slot, splitting the edges and faces that cross the plane of symmetry as needed to enforce symmetry. All new vertices, edges, and faces are added to the geom.out slot.
Parameters:
- bm (bmesh.types.BMesh) – The bmesh to act on.
- input (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.
- direction ( Literal [ '-X' , '-Y' , '-Z' , 'X' , 'Y' , 'Z' ] ) – Axis to use.
- dist ( float ) – Minimum distance.
- use_shapekey ( bool ) – Transform shape keys too.
Returns:
- geom: type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]
Return type: dict[str, Any]

[Related references](INDEX.md).

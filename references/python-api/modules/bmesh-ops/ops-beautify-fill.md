# bmesh.ops: bmesh.ops. beautify_fill ( bm , faces =  , edges =  , use_restrict_tag = False , method = 'AREA' ) –

bmesh.ops. beautify_fill ( bm , faces = [] , edges = [] , use_restrict_tag = False , method = 'AREA' ) –

Triangle Equalization

Reorientation of polygon diagonals to produce evenly proportioned triangles.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh target for the operation.

- faces (list[bmesh.types.BMFace]) – Triangulated regions to process.

- edges (list[bmesh.types.BMEdge]) – Boundaries available for diagonal flipping.

- use_restrict_tag ( bool ) – Flip only diagonals between differently marked boundary vertices.

- method ( Literal [ 'AREA' , 'ANGLE' ] ) – Optimization metric (smallest enclosed area or minimal corner angles).

Returns :

- geom :
New flipped faces and edges

Parameters:
- bm (bmesh.types.BMesh) – The bmesh to act on.
- faces (list[bmesh.types.BMFace]) – Input faces.
- faces_exclude (list[bmesh.types.BMFace]) – Input faces to explicitly exclude from inset.
- use_boundary ( bool ) – Inset face boundaries.
- use_even_offset ( bool ) – Scale the offset to give more even thickness.
- use_interpolate ( bool ) – Blend face data across the inset.
- use_relative_offset ( bool ) – Scale the offset by surrounding geometry.
- use_edge_rail ( bool ) – Inset the region along existing edges.
- thickness ( float ) – Inset distance from the boundary.
- depth ( float ) – Distance to raise or lower the inset face along its normal.
- use_outset ( bool ) – Outset rather than inset.
Returns:
- faces: Output faces. type list[bmesh.types.BMFace]
Return type: dict[str, Any]

[Related references](INDEX.md).

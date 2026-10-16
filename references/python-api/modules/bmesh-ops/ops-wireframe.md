# bmesh.ops: bmesh.ops. wireframe ( bm , faces =  , thickness = 0 , offset = 0 , use_replace = False , use_boundary = False , use_even_offset = False , use_crease = False , crease_weight = 0 , use_relative_offset = False , material_offset = 0 )

bmesh.ops. wireframe ( bm , faces = [] , thickness = 0 , offset = 0 , use_replace = False , use_boundary = False , use_even_offset = False , use_crease = False , crease_weight = 0 , use_relative_offset = False , material_offset = 0 )
Wire Frame. Produces a wire-frame copy of the faces.
Parameters:
- bm (bmesh.types.BMesh) – The bmesh to act on.
- faces (list[bmesh.types.BMFace]) – Input faces.
- thickness ( float ) – Wire thickness.
- offset ( float ) – Offset the thickness from the center.
- use_replace ( bool ) – Remove original geometry.
- use_boundary ( bool ) – Inset face boundaries.
- use_even_offset ( bool ) – Scale the offset to give more even thickness.
- use_crease ( bool ) – Crease hub edges for improved subdivision surface.
- crease_weight ( float ) – The mean crease weight for resulting edges.
- use_relative_offset ( bool ) – Scale the offset by surrounding geometry.
- material_offset ( int ) – Offset material index of generated faces.
Returns:
- faces: Output faces. type list[bmesh.types.BMFace]
Return type: dict[str, Any]

[Related references](INDEX.md).

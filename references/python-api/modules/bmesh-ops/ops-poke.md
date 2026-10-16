# bmesh.ops: bmesh.ops. poke ( bm , faces =  , offset = 0 , center_mode = 'MEAN_WEIGHTED' , use_relative_offset = False )

bmesh.ops. poke ( bm , faces = [] , offset = 0 , center_mode = '`MEAN_WEIGHTED`' , use_relative_offset = False )
Poke. Splits each face into a triangle fan from a central vertex.
Parameters:
- bm (bmesh.types.BMesh) – The bmesh to act on.
- faces (list[bmesh.types.BMFace]) – Input faces.
- offset ( float ) – Center vertex offset along normal.
- center_mode ( Literal [ '`MEAN_WEIGHTED`' , 'MEAN' , 'BOUNDS' ] ) – Calculation mode for center vertex.
- use_relative_offset ( bool ) – Apply offset.
Returns:
- verts: Output verts. type list[bmesh.types.BMVert]
- faces: Output faces. type list[bmesh.types.BMFace]
Return type: dict[str, Any]

[Related references](INDEX.md).

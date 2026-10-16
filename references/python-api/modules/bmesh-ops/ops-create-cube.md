# bmesh.ops: bmesh.ops. create_cube ( bm , size = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False ) –

bmesh.ops. create_cube ( bm , size = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False ) –

Cube Generation

Produces a six-sided box primitive within the bmesh.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh target for the operation.

- size ( float ) – Dimensions of each side.

- matrix (mathutils.Matrix) – Linear transformation to apply to all new vertices.

- calc_uvs ( bool ) – Whether to generate default texture coordinate mapping.

Returns :

- verts :
Output verts.

type list[bmesh.types.BMVert]

Return type :

dict[str, Any]

[Related references](INDEX.md).

# bmesh.ops: bmesh.ops. create_monkey ( bm , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False )

bmesh.ops. create_monkey ( bm , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False ) 

Create Suzanne.

Creates a monkey (standard blender primitive).

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- matrix (mathutils.Matrix) – Matrix to multiply the new geometry with.

- calc_uvs ( bool ) – Calculate default UVs.

Returns :

- verts :
Output verts.

type list[bmesh.types.BMVert]

Return type :

dict[str, Any]

[Related references](INDEX.md).

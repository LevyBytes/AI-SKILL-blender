# bmesh.ops: bmesh.ops. create_cone ( bm , cap_ends = False , cap_tris = False , segments = 0 , radius1 = 0 , radius2 = 0 , depth = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False )

bmesh.ops. create_cone ( bm , cap_ends = False , cap_tris = False , segments = 0 , radius1 = 0 , radius2 = 0 , depth = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False ) 

Create Cone.

Creates a cone with variable radius at both ends

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- cap_ends ( bool ) – Whether or not to fill in the ends with faces.

- cap_tris ( bool ) – Fill ends with triangles instead of ngons.

- segments ( int ) – Number of vertices in the base circle.

- radius1 ( float ) – Radius of one end.

- radius2 ( float ) – Radius of the opposite end.

- depth ( float ) – Distance between ends.

- matrix (mathutils.Matrix) – Matrix to multiply the new geometry with.

- calc_uvs ( bool ) – Calculate default UVs.

Returns :

- verts :
Output verts.

type list[bmesh.types.BMVert]

Return type :

dict[str, Any]

[Related references](INDEX.md).

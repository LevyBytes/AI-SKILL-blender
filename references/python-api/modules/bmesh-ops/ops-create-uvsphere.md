# bmesh.ops: bmesh.ops. create_uvsphere ( bm , u_segments = 0 , v_segments = 0 , radius = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False )

bmesh.ops. create_uvsphere ( bm , u_segments = 0 , v_segments = 0 , radius = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False ) 

Create UV Sphere.

Creates a UV sphere with a variable number of subdivisions.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- u_segments ( int ) – Number of u segments.

- v_segments ( int ) – Number of v segments.

- radius ( float ) – Radius.

- matrix (mathutils.Matrix) – Matrix to multiply the new geometry with.

- calc_uvs ( bool ) – Calculate default UVs.

Returns :

- verts :
Output verts.

type list[bmesh.types.BMVert]

Return type :

dict[str, Any]

[Related references](INDEX.md).

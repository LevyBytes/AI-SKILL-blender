# bmesh.ops: bmesh.ops. create_circle ( bm , cap_ends = False , cap_tris = False , segments = 0 , radius = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False )

bmesh.ops. create_circle ( bm , cap_ends = False , cap_tris = False , segments = 0 , radius = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False ) 

Generates a circle.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- cap_ends ( bool ) – Optionally fill in the circle with a face.

- cap_tris ( bool ) – Fill the circle with triangles instead of an n-gon.

- segments ( int ) – Number of vertices in the circle.

- radius ( float ) – Radius of the circle.

When multiplying new geometry with a transformation, the matrix parameter accepts a mathutils.Matrix object to apply scaling, rotation, or translation to generated vertices.

calc_uvs ( bool ) – Whether to generate texture coordinates automatically upon creation.

Returns :

- verts :
Output verts.

type list[bmesh.types.BMVert]

Return type :

dict[str, Any]

[Related references](INDEX.md).

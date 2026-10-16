# bmesh.ops: bmesh.ops. create_icosphere ( bm , subdivisions = 0 , radius = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False )

bmesh.ops. create_icosphere ( bm , subdivisions = 0 , radius = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False ) 

Create Ico-Sphere.

Creates an ico-sphere with a variable number of subdivisions.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- subdivisions ( int ) – How many times to recursively subdivide the sphere.

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

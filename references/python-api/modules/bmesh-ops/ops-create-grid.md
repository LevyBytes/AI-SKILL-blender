# bmesh.ops: bmesh.ops. create_grid ( bm , x_segments = 0 , y_segments = 0 , size = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False )

bmesh.ops. create_grid ( bm , x_segments = 0 , y_segments = 0 , size = 0 , matrix = mathutils.Matrix.Identity(4) , calc_uvs = False ) 

Create Grid.

Creates a grid with a variable number of subdivisions

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- x_segments ( int ) – Number of x segments.

- y_segments ( int ) – Number of y segments.

- size ( float ) – Size of the grid.

- matrix (mathutils.Matrix) – Matrix to multiply the new geometry with.

- calc_uvs ( bool ) – Calculate default UVs.

Returns :

- verts :
Output verts.

type list[bmesh.types.BMVert]

Return type :

dict[str, Any]

[Related references](INDEX.md).

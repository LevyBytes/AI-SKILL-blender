# bmesh.ops: bmesh.ops. transform ( bm , matrix = mathutils.Matrix.Identity(4) , space = mathutils.Matrix.Identity(4) , verts =  , use_shapekey = False )

bmesh.ops. transform ( bm , matrix = mathutils.Matrix.Identity(4) , space = mathutils.Matrix.Identity(4) , verts = [] , use_shapekey = False ) 

Transform.

Applies a matrix transformation to a set of vertices. Multiplies
the vertex coordinates with the matrix.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- matrix (mathutils.Matrix) – Transform matrix.

- space (mathutils.Matrix) – Matrix to define the space (typically object matrix).

- verts (list[bmesh.types.BMVert]) – Input vertices.

- use_shapekey ( bool ) – Transform shape keys too.

[Related references](INDEX.md).

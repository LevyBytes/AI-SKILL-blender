# bmesh.ops: bmesh.ops. scale ( bm , vec = mathutils.Vector() , space = mathutils.Matrix.Identity(4) , verts =  , use_shapekey = False )

bmesh.ops. scale ( bm , vec = mathutils.Vector() , space = mathutils.Matrix.Identity(4) , verts = [] , use_shapekey = False ) 

Scale.

Scales vertices by a factor.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- vec ( Sequence [ float ] ) – Scale factor.

- space (mathutils.Matrix) – Matrix to define the space (typically object matrix).

- verts (list[bmesh.types.BMVert]) – Input vertices.

- use_shapekey ( bool ) – Transform shape keys too.

[Related references](INDEX.md).

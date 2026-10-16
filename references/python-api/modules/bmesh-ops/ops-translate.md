# bmesh.ops: bmesh.ops. translate ( bm , vec = mathutils.Vector() , space = mathutils.Matrix.Identity(4) , verts =  , use_shapekey = False )

bmesh.ops. translate ( bm , vec = mathutils.Vector() , space = mathutils.Matrix.Identity(4) , verts = [] , use_shapekey = False ) 

Translate.

Translate vertices by an offset.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- vec ( Sequence [ float ] ) – Translation offset.

- space (mathutils.Matrix) – Matrix to define the space (typically object matrix).

- verts (list[bmesh.types.BMVert]) – Input vertices.

- use_shapekey ( bool ) – Transform shape keys too.

[Related references](INDEX.md).

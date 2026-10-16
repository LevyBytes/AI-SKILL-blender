# bmesh.ops: bmesh.ops. spin ( bm , geom =  , cent = mathutils.Vector() , axis = mathutils.Vector() , dvec = mathutils.Vector() , angle = 0 , space = mathutils.Matrix.Identity(4) , steps = 0 , use_merge = False , use_normal_flip = False , use_duplicate = False )

bmesh.ops. spin ( bm , geom = [] , cent = mathutils.Vector() , axis = mathutils.Vector() , dvec = mathutils.Vector() , angle = 0 , space = mathutils.Matrix.Identity(4) , steps = 0 , use_merge = False , use_normal_flip = False , use_duplicate = False ) 

Spin.

Extrude or duplicate geometry a number of times,
rotating and possibly translating after each step

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.

- cent ( Sequence [ float ] ) – Rotation center.

- axis ( Sequence [ float ] ) – Rotation axis.

- dvec ( Sequence [ float ] ) – Translation delta per step.

- angle ( float ) – Total rotation angle (radians).

- space (mathutils.Matrix) – Matrix to define the space (typically object matrix).

[Related references](INDEX.md).

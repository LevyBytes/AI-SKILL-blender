# bmesh.ops: bmesh.ops. planar_faces ( bm , faces =  , iterations = 0 , factor = 0 )

bmesh.ops. planar_faces ( bm , faces = [] , iterations = 0 , factor = 0 ) 

Planar Faces.

Iteratively flatten faces.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- faces (list[bmesh.types.BMFace]) – Input geometry.

- iterations ( int ) – Number of times to flatten faces (for when connected faces are used)

- factor ( float ) – Influence for making planar each iteration

Returns :

- geom :
Output slot, computed boundary geometry.

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

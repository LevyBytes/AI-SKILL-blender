# bmesh.ops: bmesh.ops. contextual_create ( bm , geom =  , mat_nr = 0 , use_smooth = False )

bmesh.ops. contextual_create ( bm , geom = [] , mat_nr = 0 , use_smooth = False ) 

Contextual Create.

This operates like the F-key, creating
new faces from vertices, forms geometry from edge nets,
constructs wire edges, etc. It also merges faces.

Three verts become a triangle, four become a quad. Two
become a wire edge.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Input geometry.

- mat_nr ( int ) – Material to use.

- use_smooth ( bool ) – Set smooth shading on newly created faces.

Returns :

- faces :
Newly-made face(s).

type list[bmesh.types.BMFace]

- edges :
Newly-made edge(s).

type list[bmesh.types.BMEdge]

Return type :

dict[str, Any]

[Related references](INDEX.md).

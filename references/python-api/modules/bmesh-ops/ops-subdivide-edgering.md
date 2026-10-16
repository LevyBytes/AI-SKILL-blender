# bmesh.ops: bmesh.ops. subdivide_edgering ( bm , edges =  , interp_mode = 'LINEAR' , smooth = 0 , cuts = 0 , profile_shape = 'SMOOTH' , profile_shape_factor = 0 )

bmesh.ops. subdivide_edgering ( bm , edges = [] , interp_mode = 'LINEAR' , smooth = 0 , cuts = 0 , profile_shape = 'SMOOTH' , profile_shape_factor = 0 ) 

Subdivide Edge-Ring.

Take an edge-ring, and subdivide with interpolation options.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- interp_mode ( Literal [ 'LINEAR' , 'PATH' , 'SURFACE' ] ) – Interpolation method.

- smooth ( float ) – Smoothness factor.

- cuts ( int ) – Number of cuts.

- profile_shape ( Literal [ 'SMOOTH' , 'SPHERE' , 'ROOT' , 'SHARP' , 'LINEAR' , '`INVERSE_SQUARE`' ] ) – Profile shape type.

- profile_shape_factor ( float ) – How much intermediary new edges are shrunk/expanded.

Returns :

- faces :
Output faces.

type list[bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

# bmesh.ops: bmesh.ops. subdivide_edges ( bm , edges =  , smooth = 0 , smooth_falloff = 'SMOOTH' , fractal = 0 , along_normal = 0 , cuts = 0 , seed = 0 , custom_patterns = {} , edge_percents = {} , quad_corner_type = 'STRAIGHT_CUT' , use_grid_fill = False , use_single_edge = False , use_only_quads = False , use_sphere = False , use_smooth_even = False )

bmesh.ops. subdivide_edges ( bm , edges = [] , smooth = 0 , smooth_falloff = 'SMOOTH' , fractal = 0 , along_normal = 0 , cuts = 0 , seed = 0 , custom_patterns = {} , edge_percents = {} , quad_corner_type = '`STRAIGHT_CUT`' , use_grid_fill = False , use_single_edge = False , use_only_quads = False , use_sphere = False , use_smooth_even = False ) 

Subdivide Edges.

Advanced operator for subdividing edges
with options for face patterns, smoothing and randomization.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- edges (list[bmesh.types.BMEdge]) – Input edges.

- smooth ( float ) – Smoothness factor.

- smooth_falloff ( Literal [ 'SMOOTH' , 'SPHERE' , 'ROOT' , 'SHARP' , 'LINEAR' , '`INVERSE_SQUARE`' ] ) – Smooth falloff type.

- fractal ( float ) – Fractal randomness factor.

- along_normal ( float ) – Factor (0 to 1) controlling how much fractal displacement is restricted to the normal.

- cuts ( int ) – Number of cuts.

- seed ( int ) – Seed for the random number generator.

- custom_patterns ( dict ) – Internal use only, not accessible from Python.

- edge_percents (dict[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace, float]) – Mapping of edges to a float (0 to 1) controlling the cut position along each edge.

- quad_corner_type ( Literal [ '`STRAIGHT_CUT`' , '`INNER_VERT`' , 'PATH' , 'FAN' ] ) – Quad corner type.

- use_grid_fill ( bool ) – Fill in fully-selected faces with a grid.

- use_single_edge ( bool ) – Tessellate the case of one edge selected in a quad or triangle.

- use_only_quads ( bool ) – Only subdivide quads (for loop-cut).

- use_sphere ( bool ) – Project new vertices onto a sphere (used for spherical primitives).

- use_smooth_even ( bool ) – Maintain even offset when smoothing.

Returns :

- geom_inner :

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- geom_split :

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

- geom :
Contains all output geometry.

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).

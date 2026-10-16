# bmesh.ops: bmesh.ops. bevel ( bm , geom =  , offset = 0 , offset_type = 'OFFSET' , profile_type = 'SUPERELLIPSE' , segments = 0 , profile = 0 , affect = 'VERTICES' , clamp_overlap = False , material = 0 , loop_slide = False , mark_seam = False , mark_sharp = False , harden_normals = False , face_strength_mode = 'NONE' , miter_outer = 'SHARP' , miter_inner = 'SHARP' , spread = 0 , custom_profile = None , vmesh_method = 'ADJ' ) –

bmesh.ops. bevel ( bm , geom = [] , offset = 0 , offset_type = 'OFFSET' , profile_type = 'SUPERELLIPSE' , segments = 0 , profile = 0 , affect = 'VERTICES' , clamp_overlap = False , material = 0 , loop_slide = False , mark_seam = False , mark_sharp = False , harden_normals = False , face_strength_mode = 'NONE' , miter_outer = 'SHARP' , miter_inner = 'SHARP' , spread = 0 , custom_profile = None , vmesh_method = 'ADJ' ) –

Chamfering Tool

Rounds off edges and vertex corners with configurable geometry.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh target for the operation.

- geom (list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]) – Selection of edges and corner vertices to process.

- offset ( float ) – Distance to move the chamfered edge outward.

- offset_type ( Literal [ 'OFFSET' , 'WIDTH' , 'DEPTH' , 'PERCENT' , 'ABSOLUTE' ] ) – Interpretation of the offset value (absolute distance, perpendicular width, depth into faces, scaled percentage, or pixel-perfect measurement).

- profile_type ( Literal [ 'SUPERELLIPSE' , 'CUSTOM' ] ) – Shape type for the rounded edge (standard superellipse or user-defined curve).

- segments ( int ) – How many subdivisions to add along the chamfered region.

- profile ( float ) – Curvature from linear (0) through rounded (0.5) to pinched (1).

- affect ( Literal [ 'VERTICES' , 'EDGES' ] ) – Which geometry type to process (corner points or connecting edges).

- clamp_overlap ( bool ) – Prevent chamfered regions from intersecting one another.

- material ( int ) – Slot index for new faces (-1 uses surrounding face materials).

- loop_slide ( bool ) – Maintain edge-aligned width rather than centering the offset.

- mark_seam ( bool ) – Mark seams so they continue across the chamfered area.

- mark_sharp ( bool ) – Preserve sharp markings through the chamfer.

- harden_normals ( bool ) – Make surface normal discontinuities explicit.

- face_strength_mode ( Literal [ 'NONE' , 'NEW' , 'AFFECTED' , 'ALL' ] ) – Whether to apply face strength weighting and which faces to include.

- miter_outer ( Literal [ 'SHARP' , 'PATCH' , 'ARC' ] ) – Intersection style at outer corners (peaked, flat patch, or curved).

- miter_inner ( Literal [ 'SHARP' , 'PATCH' , 'ARC' ] ) – Intersection style at inner corners (peaked, flat patch, or curved).

- spread ( float ) – Offset distance applied to miter vertices.

- custom_profile (bpy.types.bpy_struct | None) – A CurveProfile object defining edge shape; passes through when None.

- vmesh_method ( Literal [ 'ADJ' , 'CUTOFF' ] ) – Algorithm for vertex-corner geometry (adjacency-based or threshold cutoff).

Returns :

- faces :
Output faces.

type list[bmesh.types.BMFace]

- edges :
Output edges.

type list[bmesh.types.BMEdge]

- verts :
Output verts.

type list[bmesh.types.BMVert]

Return type :

dict[str, Any]

[Related references](INDEX.md).

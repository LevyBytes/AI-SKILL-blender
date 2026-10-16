# bpy.ops.mesh.bevel: mesh.bevel signature, width, profile, geometry and normals

bpy.ops.mesh. bevel ( * , offset_type = 'OFFSET' , offset = 0.0 , profile_type = 'SUPERELLIPSE' , offset_pct = 0.0 , segments = 1 , profile = 0.5 , affect = 'EDGES' , clamp_overlap = False , loop_slide = True , mark_seam = False , mark_sharp = False , material = -1 , harden_normals = False , face_strength_mode = 'NONE' , miter_outer = 'SHARP' , miter_inner = 'SHARP' , spread = 0.1 , vmesh_method = 'ADJ' , release_confirm = False )

Slant edges and vertices to generate bevels and chamfers

Parameters :

- offset_type ( Literal [ 'OFFSET' , 'WIDTH' , 'DEPTH' , 'PERCENT' , 'ABSOLUTE' ] ) – Width Type, The method for determining the size of the bevel (optional)

- OFFSET
Offset – Amount is offset of new edges from original.

- WIDTH
Width – Amount is width of new face.

- DEPTH
Depth – Amount is perpendicular distance from original edge to bevel face.

- PERCENT
Percent – Amount is percent of adjacent edge length.

- ABSOLUTE
Absolute – Amount is absolute distance along adjacent edge.

- offset ( float ) – Width, Bevel amount (in [0, 1e+06], optional)

- profile_type ( Literal [ 'SUPERELLIPSE' , 'CUSTOM' ] ) – Profile Type, The type of shape used to rebuild a beveled section (optional)

- SUPERELLIPSE
Superellipse – The profile can be a concave or convex curve.

- CUSTOM
Custom – The profile can be any arbitrary path between its endpoints.

- offset_pct ( float ) – Width Percent, Bevel amount for percentage method (in [0, 100], optional)

- segments ( int ) – Segments, Segments for curved edge (in [1, 1000], optional)

- profile ( float ) – Profile, Controls profile shape (0.5 = round) (in [0, 1], optional)

- affect ( Literal [ 'VERTICES' , 'EDGES' ] ) – Affect, Affect edges or vertices (optional)

- VERTICES
Vertices – Affect only vertices.

- EDGES
Edges – Affect only edges.

- clamp_overlap ( bool ) – Clamp Overlap, Do not allow beveled edges/vertices to overlap each other (optional)

- loop_slide ( bool ) – Loop Slide, Prefer sliding along edges to even widths (optional)

- mark_seam ( bool ) – Mark Seams, Preserve seams along beveled edges (optional)

- mark_sharp ( bool ) – Mark Sharp, Preserve sharp edges along beveled edges (optional)

- material ( int ) – Material Index, Material for bevel faces (-1 means use adjacent faces) (in [-1, inf], optional)

- harden_normals ( bool ) – Harden Normals, Match normals of new faces to adjacent faces (optional)

[Related references](INDEX.md).

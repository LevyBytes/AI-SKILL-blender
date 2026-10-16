# bpy.ops.mesh.dissolve_mode

bpy.ops.mesh. dissolve_mode ( * , use_verts = False , angle_threshold = 3.14159 , use_face_split = False , use_boundary_tear = False )

Demolish topology depending on edit mode selection

Parameters :

- use_verts ( bool ) – Dissolve Vertices, Dissolve remaining vertices which connect to only two edges (optional)

- angle_threshold ( float ) – Angle Threshold, Remaining vertices which separate edge pairs are preserved if their edge angle exceeds this threshold. (in [0, 3.14159], optional)

- use_face_split ( bool ) – Face Split, Split off face corners to maintain surrounding geometry (optional)

- use_boundary_tear ( bool ) – Tear Boundary, Split off face corners instead of merging faces (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

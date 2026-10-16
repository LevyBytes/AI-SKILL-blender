# bpy.ops.mesh.dissolve_verts

bpy.ops.mesh. dissolve_verts ( * , use_face_split = False , use_boundary_tear = False )

Obliterate points and stitch surrounding edges and faces

Parameters :

- use_face_split ( bool ) – Face Split, Split off face corners to maintain surrounding geometry (optional)

- use_boundary_tear ( bool ) – Tear Boundary, Split off face corners instead of merging faces (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

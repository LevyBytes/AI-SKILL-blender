# bpy.ops.mesh.bevel: mesh.bevel face strength, miters, intersection and result

bpy.ops.mesh. bevel ( * , offset_type = 'OFFSET' , offset = 0.0 , profile_type = 'SUPERELLIPSE' , offset_pct = 0.0 , segments = 1 , profile = 0.5 , affect = 'EDGES' , clamp_overlap = False , loop_slide = True , mark_seam = False , mark_sharp = False , material = -1 , harden_normals = False , face_strength_mode = 'NONE' , miter_outer = 'SHARP' , miter_inner = 'SHARP' , spread = 0.1 , vmesh_method = 'ADJ' , release_confirm = False )

- face_strength_mode ( Literal [ 'NONE' , 'NEW' , 'AFFECTED' , 'ALL' ] ) – Face Strength Mode, Whether to set face strength, and which faces to set face strength on (optional)

- NONE
None – Do not set face strength.

- NEW
New – Set face strength on new faces only.

- AFFECTED
Affected – Set face strength on new and modified faces only.

- ALL
All – Set face strength on all faces.

- miter_outer ( Literal [ 'SHARP' , 'PATCH' , 'ARC' ] ) – Outer Miter, Pattern to use for outside of miters (optional)

- SHARP
Sharp – Outside of miter is sharp.

- PATCH
Patch – Outside of miter is squared-off patch.

- ARC
Arc – Outside of miter is arc.

- miter_inner ( Literal [ 'SHARP' , 'ARC' ] ) – Inner Miter, Pattern to use for inside of miters (optional)

- SHARP
Sharp – Inside of miter is sharp.

- ARC
Arc – Inside of miter is arc.

- spread ( float ) – Spread, Amount to spread arcs for arc inner miters (in [0, 1e+06], optional)

- vmesh_method ( Literal [ 'ADJ' , 'CUTOFF' ] ) – Vertex Mesh Method, The method to use to create meshes at intersections (optional)

- ADJ
Grid Fill – Default patterned fill.

- CUTOFF
Cutoff – A cutoff at each profile's end before the intersection.

- release_confirm ( bool ) – Confirm on Release, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.mesh.tris_convert_to_quads

bpy.ops.mesh. tris_convert_to_quads ( * , face_threshold = 0.698132 , shape_threshold = 0.698132 , topology_influence = 0.0 , uvs = False , vcols = False , seam = False , sharp = False , materials = False , deselect_joined = False ) 

Join three-cornered faces into four-cornered forms where feasible

Parameters :

- face_threshold ( float ) – Max Face Angle, Maximum opening (in [0, 3.14159], optional)

- shape_threshold ( float ) – Max Shape Angle, Maximum shape opening (in [0, 3.14159], optional)

- topology_influence ( float ) – Topology Influence, How much to favor rectangular lattices and touching shapes (in [0, 2], optional)

- uvs ( bool ) – Compare UVs, (optional)

- vcols ( bool ) – Compare Color Attributes, (optional)

- seam ( bool ) – Compare Seam, (optional)

- sharp ( bool ) – Compare Sharp, (optional)

- materials ( bool ) – Compare Materials, (optional)

- deselect_joined ( bool ) – Deselect Joined, Mark only unjoined three-cornered forms that persist (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

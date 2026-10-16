# bpy.ops.object.quadriflow_remesh

bpy.ops.object. quadriflow_remesh ( * , use_mesh_symmetry = True , use_preserve_sharp = False , use_preserve_boundary = False , preserve_attributes = False , smooth_normals = False , mode = 'FACES' , target_ratio = 1.0 , target_edge_length = 0.1 , target_faces = 4000 , mesh_area = -1.0 , seed = 0 ) 

Rebuild the mesh using quadrilateral topology computed from the existing surface. All per-vertex layers will be erased

Parameters :

- use_mesh_symmetry ( bool ) – Use Mesh Symmetry, Outputs a symmetrical mesh using configured symmetry settings (optional)

- use_preserve_sharp ( bool ) – Preserve Sharp, Attempt to maintain sharp corners (optional)

- use_preserve_boundary ( bool ) – Preserve Mesh Boundary, Attempt to maintain the outer perimeter (optional)

- preserve_attributes ( bool ) – Preserve Attributes, Re-transfer properties to the newly built mesh (optional)

- smooth_normals ( bool ) – Smooth Normals, Configure output surface normals as smooth (optional)

- mode ( Literal [ 'RATIO' , 'EDGE' , 'FACES' ] ) – Mode, How to set the granularity of the new mesh (optional)

- RATIO
Ratio – Set density as a ratio of face count relative to original.

- EDGE
Edge Length – Set density using target spacing between vertices.

- FACES
Faces – Set density using target face count.

- target_ratio ( float ) – Ratio, Density relative to the original face count (in [0, inf], optional)

- target_edge_length ( float ) – Edge Length, Spacing goal for the new mesh (in [1e-07, inf], optional)

- target_faces ( int ) – Number of Faces, Expected face count (quads) in the new mesh (in [1, inf], optional)

- mesh_area ( float ) – Old Object Face Area, Cache for computing object bounds; used internally (in [-inf, inf], optional)

- seed ( int ) – Seed, RNG state for solver variation. Changing will alter the quad distribution pattern (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

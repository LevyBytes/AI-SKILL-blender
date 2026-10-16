# bpy.ops.mesh.wireframe

bpy.ops.mesh. wireframe ( * , use_boundary = True , use_even_offset = True , use_relative_offset = False , use_replace = True , thickness = 0.01 , offset = 0.01 , use_crease = False , crease_weight = 0.01 ) 

Produce a framework by hollowing out surfaces

Parameters :

- use_boundary ( bool ) – Boundary, Hollow face edges (optional)

- use_even_offset ( bool ) – Offset Even, Balance the offset to give more steady thinness (optional)

- use_relative_offset ( bool ) – Offset Relative, Weigh the offset by nearby topology (optional)

- use_replace ( bool ) – Replace, Strip out the original surfaces (optional)

- thickness ( float ) – Thickness, (in [0, 10000], optional)

- offset ( float ) – Offset, (in [0, 10000], optional)

- use_crease ( bool ) – Crease, Crease hubs to enhance subdivision surface (optional)

- crease_weight ( float ) – Crease Weight, (in [0, 1000], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

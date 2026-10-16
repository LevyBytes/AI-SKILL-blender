# bpy.ops.uv.cube_project

bpy.ops.uv. cube_project ( * , cube_size = 1.0 , correct_aspect = True , clip_to_bounds = False , scale_to_bounds = False ) 

Maps the mesh's UV vertices onto the six sides of a cube

Parameters :

- cube_size ( float ) – Cube Size, Size of the cube to project on (in [0, inf], optional)

- correct_aspect ( bool ) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)

- clip_to_bounds ( bool ) – Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)

- scale_to_bounds ( bool ) – Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

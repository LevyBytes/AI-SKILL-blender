# bpy.ops.uv.project_from_view

bpy.ops.uv. project_from_view ( * , orthographic = False , camera_bounds = True , correct_aspect = True , clip_to_bounds = False , scale_to_bounds = False ) 

Maps the mesh's UV vertices using the current 3D viewpoint

Parameters :

- orthographic ( bool ) – Orthographic, Use orthographic projection (optional)

- camera_bounds ( bool ) – Camera Bounds, Map UVs to the camera region taking resolution and aspect into account (optional)

- correct_aspect ( bool ) – Correct Aspect, Map UVs taking aspect ratio of the image associated with the material into account (optional)

- clip_to_bounds ( bool ) – Clip to Bounds, Clip UV coordinates to bounds after unwrapping (optional)

- scale_to_bounds ( bool ) – Scale to Bounds, Scale UV coordinates to bounds after unwrapping (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

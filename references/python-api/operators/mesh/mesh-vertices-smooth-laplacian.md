# bpy.ops.mesh.vertices_smooth_laplacian

bpy.ops.mesh. vertices_smooth_laplacian ( * , repeat = 1 , lambda_factor = 1.0 , lambda_border = 5e-05 , use_x = True , use_y = True , use_z = True , preserve_volume = True ) 

Ease picked points by diffusion-based smoothing

Parameters :

- repeat ( int ) – How many times to ease the mesh, (in [1, 1000], optional)

- lambda_factor ( float ) – Spread rate, (in [1e-07, 1000], optional)

- lambda_border ( float ) – Spread rate at edges, (in [1e-07, 1000], optional)

- use_x ( bool ) – Smooth X Axis, Ease the object leftward and rightward (optional)

- use_y ( bool ) – Smooth Y Axis, Ease the object forward and back (optional)

- use_z ( bool ) – Smooth Z Axis, Ease the object upward and downward (optional)

- preserve_volume ( bool ) – Preserve Volume, Keep the amount of stuff constant after easing (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

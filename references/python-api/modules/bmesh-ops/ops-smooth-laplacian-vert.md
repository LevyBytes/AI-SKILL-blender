# bmesh.ops: bmesh.ops. smooth_laplacian_vert ( bm , verts =  , lambda_factor = 0 , lambda_border = 0 , use_x = False , use_y = False , use_z = False , preserve_volume = False )

bmesh.ops. smooth_laplacian_vert ( bm , verts = [] , lambda_factor = 0 , lambda_border = 0 , use_x = False , use_y = False , use_z = False , preserve_volume = False ) 

Vertex Smooth Laplacian.

Smooths vertices using Laplacian smoothing based on
Desbrun et al. Implicit Fairing of Irregular Meshes using Diffusion and Curvature Flow.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- verts (list[bmesh.types.BMVert]) – Input vertices.

- lambda_factor ( float ) – Lambda parameter.

- lambda_border ( float ) – Lambda param in border.

- use_x ( bool ) – Smooth object along X axis.

- use_y ( bool ) – Smooth object along Y axis.

- use_z ( bool ) – Smooth object along Z axis.

- preserve_volume ( bool ) – Apply volume preservation after smooth.

[Related references](INDEX.md).

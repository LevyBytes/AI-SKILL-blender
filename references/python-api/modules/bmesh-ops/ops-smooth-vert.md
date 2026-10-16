# bmesh.ops: bmesh.ops. smooth_vert ( bm , verts =  , factor = 0 , mirror_clip_x = False , mirror_clip_y = False , mirror_clip_z = False , clip_dist = 0 , use_axis_x = False , use_axis_y = False , use_axis_z = False )

bmesh.ops. smooth_vert ( bm , verts = [] , factor = 0 , mirror_clip_x = False , mirror_clip_y = False , mirror_clip_z = False , clip_dist = 0 , use_axis_x = False , use_axis_y = False , use_axis_z = False ) 

Vertex Smooth.

Smooths vertices by averaging their positions with neighboring vertices.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- verts (list[bmesh.types.BMVert]) – Input vertices.

- factor ( float ) – Smoothing factor.

- mirror_clip_x ( bool ) – Set vertices close to the x axis before the operation to 0.

- mirror_clip_y ( bool ) – Set vertices close to the y axis before the operation to 0.

- mirror_clip_z ( bool ) – Set vertices close to the z axis before the operation to 0.

- clip_dist ( float ) – Clipping threshold for the above three slots.

- use_axis_x ( bool ) – Smooth vertices along X axis.

- use_axis_y ( bool ) – Smooth vertices along Y axis.

- use_axis_z ( bool ) – Smooth vertices along Z axis.

[Related references](INDEX.md).

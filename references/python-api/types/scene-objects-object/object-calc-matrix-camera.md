# bpy.types.Object: calc_matrix_camera

calc_matrix_camera ( depsgraph , * , x = 1 , y = 1 , scale_x = 1.0 , scale_y = 1.0 ) 

Build this object's camera projection matrix (chiefly handy for Camera and Light types)

Parameters :

- depsgraph (Depsgraph) – Depsgraph to get evaluated data from

- x ( int ) – Width of the render area (in [0, inf], optional)

- y ( int ) – Height of the render area (in [0, inf], optional)

- scale_x ( float ) – Width scaling factor (in [1e-06, inf], optional)

- scale_y ( float ) – Height scaling factor (in [1e-06, inf], optional)

Returns :

The camera projection matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])

Return type :

mathutils.Matrix

[Related references](INDEX.md).

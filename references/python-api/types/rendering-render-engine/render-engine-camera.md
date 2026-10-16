# bpy.types.RenderEngine: camera_shift_x, camera_model_matrix

camera_shift_x ( camera , * , use_spherical_stereo = False ) 

camera_shift_x

Parameters :

use_spherical_stereo ( bool ) – Spherical Stereo, (optional)

Returns :

Shift X, (in [0, inf])

Return type :

float
camera_model_matrix ( camera , * , use_spherical_stereo = False ) 

camera_model_matrix

Parameters :

use_spherical_stereo ( bool ) – Spherical Stereo, (optional)

Returns :

Model Matrix, Normalized camera model matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])

Return type :

mathutils.Matrix

[Related references](INDEX.md).

# bpy.types.RegionView3D: view_camera_offset, view_camera_zoom, view_distance, view_location, view_matrix, view_perspective, view_rotation

view_camera_offset 

How far the view is shifted in camera view (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

bpy_prop_array[float]
view_camera_zoom 

The zoom amount in camera view (in [-30, 600], default 0.0)

Type :

float
view_distance 

How far the viewpoint sits from the view location (in [0, inf], default 0.0)

Type :

float
view_location 

The pivot point of the view (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
view_matrix 

The active view matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

Type :

mathutils.Matrix
view_perspective 

View Perspective (default 'ORTHO' )

Type :

Literal[‘PERSP’, ‘ORTHO’, ‘CAMERA’]
view_rotation 

Rotation expressed as quaternions (keep them normalized) (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

mathutils.Quaternion

[Related references](INDEX.md).

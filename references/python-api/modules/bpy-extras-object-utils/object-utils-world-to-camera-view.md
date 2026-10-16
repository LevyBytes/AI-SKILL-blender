# bpy_extras.object_utils: bpy_extras.object_utils. world_to_camera_view ( scene , obj , coord )

bpy_extras.object_utils. world_to_camera_view ( scene , obj , coord ) 

Give back the camera-space coordinates of a 3d point
(these are also called normalized device coordinates - NDC).

Here (0, 0) marks the bottom left and (1, 1)
the top right of the camera frame;
values beyond the 0-1 range are allowed too.
When 'z' is negative the point sits behind the camera.

Shift-x/y, the lens angle and the sensor size are all accounted for,
as are perspective and ortho projections.

Parameters :

- scene (bpy.types.Scene) – Scene to use for frame size.

- obj (bpy.types.Object) – Camera object.

- coord (mathutils.Vector) – World space location.

Returns :

a vector where X and Y map to the view plane and
Z is the depth on the view axis.

Return type :

[Related references](INDEX.md).

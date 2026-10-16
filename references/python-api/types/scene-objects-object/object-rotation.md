# bpy.types.Object: rotation_axis_angle, rotation_euler, rotation_mode, rotation_quaternion

rotation_axis_angle 

The rotation angle for the Axis-Angle rotation representation (array of 4 items, in [-inf, inf], default (0.0, 0.0, 1.0, 0.0))

Type :

bpy_prop_array[float]
rotation_euler 

Rotation expressed as Eulers (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Euler
rotation_mode 

Which rotation method to use; values from the other rotation modes are ignored (default 'XYZ' )

Type :

Literal[Object Rotation Mode Items]
rotation_quaternion 

Rotation expressed as Quaternions (array of 4 items, in [-inf, inf], default (1.0, 0.0, 0.0, 0.0))

Type :

mathutils.Quaternion

[Related references](INDEX.md).

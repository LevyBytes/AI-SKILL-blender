# bpy.types.PoseBone: rotation_axis_angle, rotation_euler, rotation_mode, rotation_quaternion

rotation_axis_angle

Rotation angle for the Axis-Angle rotation form (array of 4 items, in [-inf, inf], default (0.0, 0.0, 1.0, 0.0))

Type :

bpy_prop_array[float]
rotation_euler

Euler-form rotation (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Euler
rotation_mode

Which rotation form is active; values from the other forms stay unused (default 'QUATERNION' )

Type :

Literal[Object Rotation Mode Items]
rotation_quaternion

Quaternion-form rotation (array of 4 items, in [-inf, inf], default (1.0, 0.0, 0.0, 0.0))

Type :

mathutils.Quaternion

[Related references](INDEX.md).

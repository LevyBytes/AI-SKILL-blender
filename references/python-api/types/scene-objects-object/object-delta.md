# bpy.types.Object: delta_location, delta_rotation_euler, delta_rotation_quaternion, delta_scale

delta_location 

A further translation layered onto the object's location (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
delta_rotation_euler 

A further rotation layered onto the object's rotation (when Euler rotations are in use) (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Euler
delta_rotation_quaternion 

A further rotation layered onto the object's rotation (when Quaternion rotations are in use) (array of 4 items, in [-inf, inf], default (1.0, 0.0, 0.0, 0.0))

Type :

mathutils.Quaternion
delta_scale 

A further scaling layered onto the object's scale (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

Type :

mathutils.Vector

[Related references](INDEX.md).

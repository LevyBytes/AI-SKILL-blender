# bpy.types.PoseBone: custom_shape, custom_shape_rotation_euler, custom_shape_scale_xyz, custom_shape_transform, custom_shape_translation, custom_shape_wire_width

custom_shape

Object used as the custom display shape for this bone

Type :

Object
custom_shape_rotation_euler

Tweak the rotation of the custom shape (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Euler
custom_shape_scale_xyz

Tweak the size of the custom shape (array of 3 items, in [-inf, inf], default (1.0, 1.0, 1.0))

Type :

mathutils.Vector
custom_shape_transform

Bone whose transform drives the display of this custom shape

Type :

PoseBone
custom_shape_translation

Tweak the position of the custom shape (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
custom_shape_wire_width

Tweak how thick the wire of custom shapes appears (in [1, 16], default 0.0)

Type :

float

[Related references](INDEX.md).

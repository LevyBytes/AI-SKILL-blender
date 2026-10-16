# bpy.types.MovieTrackingStabilization: target_position, target_rotation, target_scale

target_position

Known relative offset of the original shot that gets subtracted out (e.g. for a panning shot; can be animated) (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
target_rotation

Rotation present in the original shot that gets compensated (e.g. for deliberate tilting) (in [-inf, inf], default 0.0)

Type :

float
target_scale

Scale applied to the result to offset zoom in the original shot (in [1.192e-07, inf], default 0.0)

Type :

float

[Related references](INDEX.md).

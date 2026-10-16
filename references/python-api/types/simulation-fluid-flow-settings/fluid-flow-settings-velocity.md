# bpy.types.FluidFlowSettings: velocity_coord, velocity_factor, velocity_normal, velocity_random

velocity_coord

Extra starting velocity along X, Y and Z, added on top of the source velocity (array of 3 items, in [-1000.1, 1000.1], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
velocity_factor

Multiplier applied to the source velocity handed to the fluid (the source velocity is nonzero only while the object moves) (in [-100, 100], default 1.0)

Type :

float
velocity_normal

How much velocity is added along the surface normal (in [-100, 100], default 0.0)

Type :

float
velocity_random

How much randomized velocity is added (in [0, 10], default 0.0)

Type :

float

[Related references](INDEX.md).

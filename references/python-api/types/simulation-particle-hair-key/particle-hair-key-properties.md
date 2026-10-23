# bpy.types.ParticleHairKey: properties

## ParticleHairKey(bpy_struct)

### ParticleHairKey(bpy_struct)

base class: bpy_struct
class bpy.types. ParticleHairKey ( bpy_struct )

A particle key belonging to a hair particle system
co

Where the hair key sits in object space (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
co_local

Position of the hair key within its own local frame, measured against the emitting face (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
time

Where the key falls along the hair length, as a relative time (in [0, inf], default 0.0)

Type :

float
weight

Weight for cloth simulation (in [0, 1], default 0.0)

Type :

float

[Related references](INDEX.md).

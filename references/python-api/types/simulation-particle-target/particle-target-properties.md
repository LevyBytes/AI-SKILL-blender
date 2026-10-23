# bpy.types.ParticleTarget: properties

## ParticleTarget(bpy_struct)

### ParticleTarget(bpy_struct)

base class: bpy_struct
class bpy.types. ParticleTarget ( bpy_struct )

A particle system designated as a target
alliance

(default 'NEUTRAL' )

Type :

Literal[‘FRIEND’, ‘NEUTRAL’, ‘ENEMY’]
duration

(in [0, 1.04857e+06], default 0.0)

Type :

float
is_valid

Whether the keyed-particles target is valid (default False)

Type :

bool
name

Particle target name (default “”, readonly, never None)

Type :

str
object

The object holding the target particle system (left empty if it is the same object)

Type :

Object
system

Index of the particle system on the target object (in [1, inf], default 0)

Type :

int
time

(in [0, 1.04857e+06], default 0.0)

Type :

float

[Related references](INDEX.md).

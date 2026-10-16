# bpy.types.FluidDomainSettings: flame_grid, flame_ignition, flame_max_temp, flame_smoke, flame_smoke_color, flame_vorticity

flame_grid

Smoke flame grid (array of 32 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), readonly)

Type :

bpy_prop_array[float]
flame_ignition

Temperature at which the flames first ignite; raising it makes flames rise more quickly (in [0.5, 5], default 1.5)

Type :

float
flame_max_temp

Hottest the flames can get; raising it makes flames rise more quickly (in [1, 10], default 3.0)

Type :

float
flame_smoke

How much smoke the burning fuel gives off (in [0, 8], default 1.0)

Type :

float
flame_smoke_color

Color given to the smoke that rises off burning fuel (array of 3 items, in [0, inf], default (0.7, 0.7, 0.7))

Type :

mathutils.Color
flame_vorticity

Extra swirl added to the flames (in [0, 2], default 0.5)

Type :

float

[Related references](INDEX.md).

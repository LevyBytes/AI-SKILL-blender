# bpy.types.FluidDomainSettings: color_grid, color_ramp, color_ramp_field, color_ramp_field_scale

color_grid

Smoke color grid (array of 32 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), readonly)

Type :

bpy_prop_array[float]
color_ramp

(readonly)

Type :

ColorRamp
color_ramp_field

Simulation field to color map (default 'NONE' )

Type :

Literal[‘NONE’]
color_ramp_field_scale

Multiplier for scaling the selected field to color map (in [0.001, 100000], default 1.0)

Type :

float

[Related references](INDEX.md).

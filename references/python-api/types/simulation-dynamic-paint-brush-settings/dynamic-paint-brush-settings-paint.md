# bpy.types.DynamicPaintBrushSettings: paint_alpha, paint_color, paint_distance, paint_ramp, paint_source, paint_wetness

paint_alpha

Alpha of the paint (in [0, 1], default 0.0)

Type :

float
paint_color

The paint’s color (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
paint_distance

Furthest the brush can sit from the mesh surface and still affect paint (in [0, 500], default 0.0)

Type :

float
paint_ramp

Color ramp that shapes the proximity falloff (readonly)

Type :

ColorRamp
paint_source

(default 'VOLUME' )

Type :

Literal[‘`PARTICLE_SYSTEM`’, ‘POINT’, ‘DISTANCE’, ‘`VOLUME_DISTANCE`’, ‘VOLUME’]
paint_wetness

How wet the paint is, shown in the wetmap (a few effects act only on wet paint) (in [0, 1], default 0.0)

Type :

float

[Related references](INDEX.md).

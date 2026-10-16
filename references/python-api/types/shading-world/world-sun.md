# bpy.types.World: sun_angle, sun_shadow_filter_radius, sun_shadow_jitter_overblur, sun_shadow_maximum_resolution, sun_threshold

sun_angle 

Apparent angular size of the Sun viewed from Earth (in [0, 3.14159], default 0.00918043)

Type :

float
sun_shadow_filter_radius 

Soften shadow stair-stepping with Percentage Closer Filtering (in [0, inf], default 1.0)

Type :

float
sun_shadow_jitter_overblur 

Run shadow tracing on every jittered sample to cut down on under-sampling artifacts (in [0, 100], default 10.0)

Type :

float
sun_shadow_maximum_resolution 

Largest allowed shadow-map texel size. Bigger values save memory but lower shadow fidelity. (in [0, inf], default 0.001)

Type :

float
sun_threshold 

When non-zero, caps the world contribution stored in the world light probe. Anything beyond that cap becomes a sun light, cutting the bleed from extremely bright sources. (in [0, inf], default 10.0)

Type :

float

[Related references](INDEX.md).

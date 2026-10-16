# bpy.types.LightProbeVolume: capture_distance, capture_emission, capture_indirect, capture_world

capture_distance 

Range around the probe volume taken into account while baking (in [1e-06, inf], default 20.0)

Type :

float
capture_emission 

Include emissive surfaces in the bake for more accurate lighting (default True)

Type :

bool
capture_indirect 

Include bounced light from light sources in the bake for more accurate lighting (default True)

Type :

bool
capture_world 

Bake the actual incoming world light, not merely its visibility, for more accurate lighting, at the cost of correct blending with nearby irradiance volumes (default False)

Type :

bool

[Related references](INDEX.md).

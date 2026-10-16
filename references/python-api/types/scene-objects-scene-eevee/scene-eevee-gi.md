# bpy.types.SceneEEVEE: gi_cubemap_resolution, gi_diffuse_bounces, gi_glossy_clamp, gi_irradiance_pool_size, gi_visibility_resolution

gi_cubemap_resolution

Size of each cubemap (default '512' )

Type :

Literal[‘128’, ‘256’, ‘512’, ‘1024’, ‘2048’, ‘4096’]
gi_diffuse_bounces

How many times light is reinjected into the light grids; 0 turns off indirect diffuse light (in [0, inf], default 3)

Type :

int
gi_glossy_clamp

Cap pixel intensity to reduce noise in glossy reflections coming from reflection cubemaps; 0 disables it (in [0, inf], default 0.0)

Type :

float
gi_irradiance_pool_size

Size of the irradiance pool; a larger pool fits more irradiance grids in the scene but may overflow GPU memory and hurt performance (default '16' )

Type :

Literal[‘16’, ‘32’, ‘64’, ‘128’, ‘256’, ‘512’, ‘1024’]
gi_visibility_resolution

Size of the shadow map used for each irradiance sample (default '32' )

Type :

Literal[‘8’, ‘16’, ‘32’, ‘64’]

[Related references](INDEX.md).

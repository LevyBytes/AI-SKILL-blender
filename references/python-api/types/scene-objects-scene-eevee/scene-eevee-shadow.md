# bpy.types.SceneEEVEE: shadow_pool_size, shadow_ray_count, shadow_resolution_scale, shadow_step_count

shadow_pool_size

Size of the shadow pool; a larger pool fits more shadows in the scene but may overflow GPU memory (default '512' )

Type :

Literal[‘16’, ‘32’, ‘64’, ‘128’, ‘256’, ‘512’, ‘1024’]
shadow_ray_count

How many shadow rays are traced per light (in [1, 4], default 1)

Type :

int
shadow_resolution_scale

Resolution percentage of shadow maps (in [0, 1], default 1.0)

Type :

float
shadow_step_count

How many shadow map samples are taken per shadow ray (in [1, 16], default 6)

Type :

int

[Related references](INDEX.md).

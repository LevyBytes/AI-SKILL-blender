# bpy.types.FluidDomainSettings: mesh_concave_lower, mesh_concave_upper, mesh_generator, mesh_particle_radius, mesh_scale, mesh_smoothen_neg, mesh_smoothen_pos

mesh_concave_lower

Lower bound for mesh concavity; high values tend to smooth out and fill in concave regions (in [0, 10], default 0.4)

Type :

float
mesh_concave_upper

Upper bound for mesh concavity; high values tend to smooth out and fill in concave regions (in [0, 10], default 3.5)

Type :

float
mesh_generator

Pick which particle level-set generator runs (default 'IMPROVED' )

- IMPROVED
Final – Use improved particle level set (slower but more precise and with mesh smoothening options).

- UNION
Preview – Use union particle level set (faster but lower quality).

Type :

Literal[‘IMPROVED’, ‘UNION’]
mesh_particle_radius

Factor scaling particle radius; larger values give bigger meshed particles. Re-tune it whenever the mesh scale changes. (in [0, 10], default 2.0)

Type :

float
mesh_scale

Factor by which the meshing simulation is enlarged relative to the domain's base resolution. For the best mesh, tune the mesh particle radius together with this value. (in [1, 100], default 2)

Type :

int
mesh_smoothen_neg

Inward smoothing applied to the mesh (in [0, 100], default 1)

Type :

int
mesh_smoothen_pos

Outward smoothing applied to the mesh (in [0, 100], default 1)

Type :

int

[Related references](INDEX.md).

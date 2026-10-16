# bpy.types.FluidDomainSettings: particle_band_width, particle_max, particle_min, particle_number, particle_radius, particle_randomness, particle_scale

particle_band_width

Width of the narrow particle band; larger values widen the band and add more particles (in [0, 1000], default 3.0)

Type :

float
particle_max

Most particles a cell may contain; guarantees no cell exceeds this count (in [0, 1000], default 16)

Type :

int
particle_min

Fewest particles a cell may contain; guarantees every cell holds at least this count (in [0, 1000], default 8)

Type :

int
particle_number

Particle count factor; larger values produce more particles (in [1, 5], default 2)

Type :

int
particle_radius

Factor scaling particle radius. Raise it if the simulation appears to leak volume, lower it if the simulation appears to gain volume. (in [0, 10], default 1.0)

Type :

float
particle_randomness

How much randomness is applied when sampling particles (in [0, 10], default 0.1)

Type :

float
particle_scale

Factor by which the particle simulation is enlarged relative to the domain's base resolution (in [1, 100], default 1)

Type :

int

[Related references](INDEX.md).

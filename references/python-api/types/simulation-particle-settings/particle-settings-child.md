# bpy.types.ParticleSettings: child_length, child_length_threshold, child_parting_factor, child_parting_max, child_parting_min, child_percent, child_radius, child_roundness, child_size, child_size_random, child_type

child_length

Length of child paths (in [0, 1], default 1.0)

Type :

float
child_length_threshold

Share of particles the child path length leaves alone (in [0, 1], default 0.0)

Type :

float
child_parting_factor

Add parting to the children, derived from the parent strands (in [0, 1], default 0.0)

Type :

float
child_parting_max

Maximum root to tip angle (tip distance/root distance for long hair) (in [0, 180], default 0.0)

Type :

float
child_parting_min

Minimum root to tip angle (tip distance/root distance for long hair) (in [0, 180], default 0.0)

Type :

float
child_percent

Number of children per parent (in [0, 100000], default 10)

Type :

int
child_radius

Radius of children around parent (in [0, 100000], default 0.2)

Type :

float
child_roundness

Roundness of children around parent (in [0, 1], default 0.0)

Type :

float
child_size

Scale factor applied to the child particle size (in [0.001, 100000], default 1.0)

Type :

float
child_size_random

Random spread in the size of the child particles (in [0, 1], default 0.0)

Type :

float
child_type

Create child particles (default 'NONE' )

Type :

Literal[‘NONE’, ‘SIMPLE’, ‘INTERPOLATED’]

[Related references](INDEX.md).

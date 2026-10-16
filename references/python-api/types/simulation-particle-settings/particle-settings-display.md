# bpy.types.ParticleSettings: display_color, display_method, display_percentage, display_size, display_step

display_color

Show extra particle data tinted as a color (default 'MATERIAL' )

Type :

Literal[‘NONE’, ‘MATERIAL’, ‘VELOCITY’, ‘ACCELERATION’]
display_method

How particles are displayed in viewport (default 'RENDER' )

Type :

Literal[‘NONE’, ‘RENDER’, ‘DOT’, ‘CIRC’, ‘CROSS’, ‘AXIS’]
display_percentage

Share of particles shown in the 3D view (in [0, 100], default 100)

Type :

int
display_size

Size of particles on viewport (in [0, 1000], default 0.1)

Type :

float
display_step

Number of steps (as a power of 2) used when drawing paths (in [0, 10], default 2)

Type :

int

[Related references](INDEX.md).

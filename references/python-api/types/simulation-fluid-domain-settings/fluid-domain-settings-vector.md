# bpy.types.FluidDomainSettings: vector_display_type, vector_field, vector_scale, vector_scale_with_magnitude, vector_show_mac_x, vector_show_mac_y, vector_show_mac_z

vector_display_type

(default 'NEEDLE' )

- NEEDLE
Needle – Display vectors as needles.

- STREAMLINE
Streamlines – Display vectors as streamlines.

- MAC
MAC Grid – Display vector field as MAC grid.

Type :

Literal[‘NEEDLE’, ‘STREAMLINE’, ‘MAC’]
vector_field

Which vector field the display vectors stand for (default '`FLUID_VELOCITY`' )

- `FLUID_VELOCITY`
Fluid Velocity – Velocity field of the fluid domain.

- `GUIDE_VELOCITY`
Guide Velocity – Guide velocity field of the fluid domain.

- FORCE
Force – Force field of the fluid domain.

Type :

Literal[‘`FLUID_VELOCITY`’, ‘`GUIDE_VELOCITY`’, ‘FORCE’]
vector_scale

Multiplier for scaling the vectors (in [0, 1000], default 1.0)

Type :

float
vector_scale_with_magnitude

Scale vectors with their magnitudes (default False)

Type :

bool
vector_show_mac_x

Show X-component of MAC Grid (default True)

Type :

bool
vector_show_mac_y

Show Y-component of MAC Grid (default True)

Type :

bool
vector_show_mac_z

Show Z-component of MAC Grid (default True)

Type :

bool

[Related references](INDEX.md).

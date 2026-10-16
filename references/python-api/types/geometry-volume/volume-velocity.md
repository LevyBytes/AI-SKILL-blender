# bpy.types.Volume: velocity_grid, velocity_scale, velocity_unit, velocity_x_grid, velocity_y_grid, velocity_z_grid

velocity_grid

Name of the velocity field, or its base name when the velocity spans several grids (default "", never None)

Type :

str
velocity_scale

Factor controlling how much motion blur is produced (in [0, inf], default 1.0)

Type :

float
velocity_unit

How velocity vectors relate to time: 'frame' treats the delta as 1 frame, 'second' treats it as 1 / FPS (default 'FRAME' )

Type :

Literal[Velocity Unit Items]
velocity_x_grid

Grid name holding the X component of the velocity field when it is stored across separate grids (default "", readonly, never None)

Type :

str
velocity_y_grid

Grid name holding the Y component of the velocity field when it is stored across separate grids (default "", readonly, never None)

Type :

str
velocity_z_grid

Grid name holding the Z component of the velocity field when it is stored across separate grids (default "", readonly, never None)

Type :

str

[Related references](INDEX.md).

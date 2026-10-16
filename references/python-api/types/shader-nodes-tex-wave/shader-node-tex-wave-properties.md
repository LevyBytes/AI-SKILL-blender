# bpy.types.ShaderNodeTexWave: properties

## ShaderNodeTexWave(ShaderNode)

### ShaderNodeTexWave(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTexWave ( ShaderNode )

Produces procedural striping or concentric rings, with optional noise applied.
bands_direction

(default 'X' )

- X
X – Stripes oriented across the X axis.

- Y
Y – Stripes oriented across the Y axis.

- Z
Z – Stripes oriented across the Z axis.

- DIAGONAL
Diagonal – Stripes oriented along the diagonal.

Type :

Literal[‘X’, ‘Y’, ‘Z’, ‘DIAGONAL’]
color_mapping

Settings controlling how color is mapped (readonly, never None)

Type :

ColorMapping
rings_direction

(default 'X' )

- X
X – Concentric rings measured along the X axis.

- Y
Y – Concentric rings measured along the Y axis.

- Z
Z – Concentric rings measured along the Z axis.

- SPHERICAL
Spherical – Rings derived from spherical distance.

Type :

Literal[‘X’, ‘Y’, ‘Z’, ‘SPHERICAL’]
texture_mapping

Settings for mapping texture coordinates (readonly, never None)

Type :

TexMapping
wave_profile

(default 'SIN' )

- SIN
Sine – Apply a plain sine wave profile.

- SAW
Saw – Apply a sawtooth wave profile.

- TRI
Triangle – Apply a triangular wave profile.

Type :

Literal[‘SIN’, ‘SAW’, ‘TRI’]
wave_type

(default 'BANDS' )

- BANDS
Bands – Render the wave texture as parallel bands.

- RINGS
Rings – Render the wave texture as rings.

Type :

Literal[‘BANDS’, ‘RINGS’]

[Related references](INDEX.md).

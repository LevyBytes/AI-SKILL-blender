# bpy.types.ShaderNodeTexNoise: properties

## ShaderNodeTexNoise(ShaderNode)

### ShaderNodeTexNoise(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTexNoise ( ShaderNode )

Builds fractal Perlin noise.
color_mapping

Color mapping settings (readonly, never None)

Type :

ColorMapping
noise_dimensions

Number of dimensions to output noise for (default '1D' )

- 1D
1D – Use the scalar value W as input.

- 2D
2D – Use the 2D vector (X, Y) as input. The Z component is ignored..

- 3D
3D – Use the 3D vector (X, Y, Z) as input.

- 4D
4D – Use the 4D vector (X, Y, Z, W) as input.

Type :

Literal[‘1D’, ‘2D’, ‘3D’, ‘4D’]
noise_type

Type of the Noise texture (default 'MULTIFRACTAL' )

- MULTIFRACTAL
Multifractal – More uneven result (varies with location), more similar to a real terrain.

- `RIDGED_MULTIFRACTAL`
Ridged Multifractal – Create sharp peaks.

- `HYBRID_MULTIFRACTAL`
Hybrid Multifractal – Create peaks and valleys with different roughness values.

- FBM
fBM – The standard fractal Perlin noise.

- `HETERO_TERRAIN`
Hetero Terrain – Similar to Hybrid Multifractal creates a heterogeneous terrain, but with the likeness of river channels.

Type :

Literal[‘MULTIFRACTAL’, ‘`RIDGED_MULTIFRACTAL`’, ‘`HYBRID_MULTIFRACTAL`’, ‘FBM’, ‘`HETERO_TERRAIN`’]
normalize

Normalize outputs to 0.0 to 1.0 range (default False)

Type :

bool
texture_mapping

Texture coordinate mapping settings (readonly, never None)

Type :

TexMapping

[Related references](INDEX.md).

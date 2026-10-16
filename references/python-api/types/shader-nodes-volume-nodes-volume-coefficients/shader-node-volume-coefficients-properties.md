# bpy.types.ShaderNodeVolumeCoefficients: properties

## ShaderNodeVolumeCoefficients(ShaderNode)

### ShaderNodeVolumeCoefficients(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeVolumeCoefficients ( ShaderNode )

Represents all three volumetric physical processes through their coefficients.
phase

Phase function used for light that scatters (default '`HENYEY_GREENSTEIN`' )

- `HENYEY_GREENSTEIN`
Henyey-Greenstein – The standard default; models how light scatters via the Henyey-Greenstein term.

- `FOURNIER_FORAND`
Fournier-Forand – A Fournier-Forand model, typically chosen for light scattering underwater.

- DRAINE
Draine – The Draine family of phase functions, most often applied to scattering within interstellar dust.

- RAYLEIGH
Rayleigh – A Rayleigh model, suited to particles below the light's wavelength, like sunlight scattering through earth’s atmosphere.

- MIE
Mie – An approximate Mie response from water droplets, handy for scattering inside clouds and fog.

Type :

Literal[‘`HENYEY_GREENSTEIN`’, ‘`FOURNIER_FORAND`’, ‘DRAINE’, ‘RAYLEIGH’, ‘MIE’]

[Related references](INDEX.md).

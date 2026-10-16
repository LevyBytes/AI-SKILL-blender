# bpy.types.ShaderNodeBsdfMetallic: properties

## ShaderNodeBsdfMetallic(ShaderNode)

### ShaderNodeBsdfMetallic(ShaderNode) 

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeBsdfMetallic ( ShaderNode ) 

Microfacet-based metal reflection paired with a metallic Fresnel response
distribution 

Microfacet model controlling how light scatters across the rough surface (default 'BECKMANN' )

- BECKMANN
Beckmann.

- GGX
GGX.

- `MULTI_GGX`
Multiscatter GGX – GGX extended with a correction for multiple scattering, so energy is preserved and high-roughness surfaces avoid the usual darkening artifacts.

Type :

Literal[‘BECKMANN’, ‘GGX’, ‘`MULTI_GGX`’]
fresnel_type 

Which Fresnel formulation gives the metal its tint (default '`PHYSICAL_CONDUCTOR`' )

- `PHYSICAL_CONDUCTOR`
Physical Conductor – Conductor Fresnel computed from the complex refractive index for each color channel.

- F82
F82 Tint – A fit of the conductor Fresnel response built from the colors seen head-on and near the grazing (about 82°) direction.

Type :

Literal[‘`PHYSICAL_CONDUCTOR`’, ‘F82’]

[Related references](INDEX.md).

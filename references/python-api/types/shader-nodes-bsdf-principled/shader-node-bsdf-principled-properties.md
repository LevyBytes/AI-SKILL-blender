# bpy.types.ShaderNodeBsdfPrincipled: properties

## ShaderNodeBsdfPrincipled(ShaderNode)

### ShaderNodeBsdfPrincipled(ShaderNode) 

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeBsdfPrincipled ( ShaderNode ) 

An approachable, physically grounded surface shader built on the OpenPBR model
distribution 

Microfacet model controlling how light scatters across the rough surface (default 'GGX' )

- GGX
GGX.

- `MULTI_GGX`
Multiscatter GGX – GGX extended with a correction for multiple scattering, so energy is preserved and high-roughness surfaces avoid the usual darkening artifacts.

Type :

Literal[‘GGX’, ‘`MULTI_GGX`’]
subsurface_method 

Technique used to render scattering beneath the surface (default 'BURLEY' )

- BURLEY
Christensen-Burley – A practical approximation of physically based volumetric scattering.

- `RANDOM_WALK`
Random Walk – Volumetric take on physically based scattering driven by the given scattering radius.

- `RANDOM_WALK_SKIN`
Random Walk (Skin) – Volumetric physically based scattering whose radius is tuned automatically against color textures, intended for shading skin..

Type :

Literal[‘BURLEY’, ‘`RANDOM_WALK`’, ‘`RANDOM_WALK_SKIN`’]

[Related references](INDEX.md).

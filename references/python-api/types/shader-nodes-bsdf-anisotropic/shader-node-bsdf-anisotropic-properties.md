# bpy.types.ShaderNodeBsdfAnisotropic: properties

## ShaderNodeBsdfAnisotropic(ShaderNode)

### ShaderNodeBsdfAnisotropic(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeBsdfAnisotropic ( ShaderNode )

Microfacet-based reflection suited to surfaces like metal or mirrors
distribution

How light scatters off the rough surface (default 'BECKMANN' )

- BECKMANN
Beckmann.

- GGX
GGX.

- `ASHIKHMIN_SHIRLEY`
Ashikhmin-Shirley.

- `MULTI_GGX`
Multiscatter GGX – GGX with an extra correction for multiple scattering, which conserves energy and avoids the unexpected darkening that otherwise shows up at high roughness.

Type :

Literal[‘BECKMANN’, ‘GGX’, ‘`ASHIKHMIN_SHIRLEY`’, ‘`MULTI_GGX`’]

[Related references](INDEX.md).

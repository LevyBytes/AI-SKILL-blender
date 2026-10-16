# bpy.types.ShaderNodeBsdfGlass: properties

## ShaderNodeBsdfGlass(ShaderNode)

### ShaderNodeBsdfGlass(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeBsdfGlass ( ShaderNode )

A glassy shader that blends refraction with reflection toward grazing angles
distribution

How light scatters off the rough surface (default 'BECKMANN' )

- BECKMANN
Beckmann.

- GGX
GGX.

- `MULTI_GGX`
Multiscatter GGX – GGX with an extra correction for multiple scattering, which conserves energy and avoids the unexpected darkening that otherwise shows up at high roughness.

Type :

Literal[‘BECKMANN’, ‘GGX’, ‘`MULTI_GGX`’]

[Related references](INDEX.md).

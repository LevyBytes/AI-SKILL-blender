# bpy.types.ShaderNodeSubsurfaceScattering: properties

## ShaderNodeSubsurfaceScattering(ShaderNode)

### ShaderNodeSubsurfaceScattering(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeSubsurfaceScattering ( ShaderNode )

A multiple-scattering subsurface shader that models light sinking into a surface and scattering around beneath it.
Well suited to substances like skin, wax, marble, and milk
falloff

Method for rendering subsurface scattering (default 'BURLEY' )

- BURLEY
Christensen-Burley – Approximation to physically based volume scattering.

- `RANDOM_WALK`
Random Walk – Volumetric approximation to physically based volume scattering, using the scattering radius as specified.

- `RANDOM_WALK_SKIN`
Random Walk (Skin) – Volumetric approximation to physically based volume scattering, with scattering radius automatically adjusted to match color textures. Designed for skin shading..

Type :

Literal[‘BURLEY’, ‘`RANDOM_WALK`’, ‘`RANDOM_WALK_SKIN`’]

[Related references](INDEX.md).

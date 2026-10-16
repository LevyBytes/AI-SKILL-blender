# bpy.types.ParticleSettingsTextureSlot: texture_coords

texture_coords

Texture coordinates used to project the texture onto the background (default 'UV' )

- GLOBAL
Global – Drive the texture coordinates from global space.

- OBJECT
Object – Drive them from the linked object’s coordinates.

- UV
UV – Drive them from the UV coordinates.

- ORCO
Generated – Drive them from the object’s original, undeformed coordinates.

- STRAND
Strand / Particle – Drive them from the normalized strand coordinate (1D), or from particle age (X) and trail position (Y).

Type :

Literal[‘GLOBAL’, ‘OBJECT’, ‘UV’, ‘ORCO’, ‘STRAND’]

[Related references](INDEX.md).

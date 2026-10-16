# bpy.types.Material: blend_method

blend_method

Blend Mode for Transparent Faces (Deprecated: use ‘surface_render_method’) (default 'OPAQUE' )

- OPAQUE
Opaque – Render surface without transparency.

- CLIP
Alpha Clip – Use the alpha threshold to clip the visibility (binary visibility).

- HASHED
Alpha Hashed – Use noise to dither the binary visibility (works well with multi-samples).

- BLEND
Alpha Blend – Render polygon transparent, depending on alpha channel of the texture.

Type :

Literal[‘OPAQUE’, ‘CLIP’, ‘HASHED’, ‘BLEND’]

[Related references](INDEX.md).

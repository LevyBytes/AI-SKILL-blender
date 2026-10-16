# bpy.types.Brush: mask_overlay_alpha, mask_stencil_dimension, mask_stencil_pos, mask_texture, mask_texture_slot, mask_tool

mask_overlay_alpha

(in [0, 100], default 33)

Type :

int
mask_stencil_dimension

Size of the mask stencil within the viewport (array of 2 items, in [-inf, inf], default (256.0, 256.0))

Type :

mathutils.Vector
mask_stencil_pos

Where the mask stencil sits within the viewport (array of 2 items, in [-inf, inf], default (256.0, 256.0))

Type :

mathutils.Vector
mask_texture

Type :

Texture
mask_texture_slot

(readonly)

Type :

BrushTextureSlot
mask_tool

(default 'DRAW' )

Type :

Literal['DRAW', 'SMOOTH']

[Related references](INDEX.md).

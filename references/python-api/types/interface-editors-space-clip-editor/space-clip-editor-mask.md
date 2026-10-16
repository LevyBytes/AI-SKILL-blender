# bpy.types.SpaceClipEditor: mask, mask_display_type, mask_overlay_mode

mask

The mask shown and edited within this space

Type :

Mask
mask_display_type

How mask splines are drawn (default 'OUTLINE' )

- OUTLINE
Outline – Display white edges with black outline.

- DASH
Dash – Display dashed black-white edges.

- BLACK
Black – Display black edges.

- WHITE
White – Display white edges.

Type :

Literal[‘OUTLINE’, ‘DASH’, ‘BLACK’, ‘WHITE’]
mask_overlay_mode

Which overlay mode the rasterized mask uses (default 'ALPHACHANNEL' )

- ALPHACHANNEL
Alpha Channel – Show alpha channel of the mask.

- COMBINED
Combined – Combine space background image with the mask.

Type :

Literal[‘ALPHACHANNEL’, ‘COMBINED’]

[Related references](INDEX.md).

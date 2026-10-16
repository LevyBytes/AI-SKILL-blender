# bpy.types.Image: alpha_mode

alpha_mode

How alpha is held in the image file, used to convert in both directions while saving and loading (default 'STRAIGHT' )

- STRAIGHT
Straight – Hold the RGB and alpha channels apart, with alpha used as a mask; also called unassociated alpha. Widely used by image editors and by formats such as PNG..

- PREMUL
Premultiplied – Hold RGB channels with alpha already multiplied in; also called associated alpha. The natural choice for renders, and used by formats such as OpenEXR..

- `CHANNEL_PACKED`
Channel Packed – Pack unrelated images into the RGB and alpha channels so they stay independent. Channel packing is a common memory-saving trick in game engines..

- NONE
None – Disregard the file's alpha channel and treat the image as fully opaque.

Type :

Literal[‘STRAIGHT’, ‘PREMUL’, ‘`CHANNEL_PACKED`’, ‘NONE’]

[Related references](INDEX.md).

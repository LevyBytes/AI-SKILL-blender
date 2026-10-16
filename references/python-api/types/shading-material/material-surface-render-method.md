# bpy.types.Material: surface_render_method

surface_render_method

Governs blending and compatibility with certain features (default 'DITHERED' )

- DITHERED
Dithered – Allows for grayscale hashed transparency, and compatible with render passes and raytracing. Also known as deferred rendering..

- BLENDED
Blended – Allows for colored transparency, but incompatible with render passes and raytracing. Also known as forward rendering..

Type :

Literal[‘DITHERED’, ‘BLENDED’]

[Related references](INDEX.md).

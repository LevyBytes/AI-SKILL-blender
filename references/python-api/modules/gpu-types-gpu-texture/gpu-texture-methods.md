# gpu.types.GPUTexture: methods

anisotropic_filter ( use_anisotropic )

Turn anisotropic filtering on or off. This matters only while mipmapping is active.

Parameters :

use_anisotropic ( bool ) – If set to true, the texture will use anisotropic filtering.
clear ( format = 'FLOAT' , value = (0.0, 0.0, 0.0, 1.0) )

Load the texture with a chosen value.

Parameters :

- format ( Literal [ 'FLOAT' , 'INT' , 'UINT' , 'UBYTE' , '`UINT_24_8`' , '10_11_11_REV' ] ) – The format that describes the content of a single item.
`UINT_24_8` is deprecated, use FLOAT instead.

- value ( Sequence [ float ] | Sequence [ int ] ) – Sequence each representing the value to fill. Sizes 1..4 are supported.
extend_mode ( extend_mode = 'EXTEND' , / )

Choose how the texture is sampled for coordinates that fall outside the [0..1] uv range on
both the x and y axis.

Parameters :

extend_mode ( Literal [ 'EXTEND' , 'REPEAT' , '`MIRRORED_REPEAT`' , '`CLAMP_TO_BORDER`' ] ) – the specified extent mode.
extend_mode_x ( extend_mode = 'EXTEND' , / )

Choose how the texture is sampled for coordinates that fall outside the [0..1] uv range on the x axis.

Parameters :

extend_mode ( Literal [ 'EXTEND' , 'REPEAT' , '`MIRRORED_REPEAT`' , '`CLAMP_TO_BORDER`' ] ) – the specified extent mode.
extend_mode_y ( extend_mode = 'EXTEND' , / )

Choose how the texture is sampled for coordinates that fall outside the [0..1] uv range on the y axis.

Parameters :

extend_mode ( Literal [ 'EXTEND' , 'REPEAT' , '`MIRRORED_REPEAT`' , '`CLAMP_TO_BORDER`' ] ) – the specified extent mode.
filter_mode ( use_filter )

Turn texture filtering on or off.

Parameters :

use_filter ( bool ) – If set to true, the texture will use linear interpolation between neighboring texels.
mipmap_mode ( use_mipmap = True , use_filter = True )

Turn texture filtering and mip-mapping on or off.

Parameters :

- use_mipmap ( bool ) – If set to true, the texture will use mip-mapping as anti-aliasing method.

- use_filter ( bool ) – If set to true, the texture will use linear interpolation between neighboring texels.
read ( )

Produce a buffer holding the value of every pixel.

Returns :

The Buffer with the read pixels.

Return type :

[Related references](INDEX.md).

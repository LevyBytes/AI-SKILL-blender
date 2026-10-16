# gpu.types.GPUTexture: overview

class gpu.types. GPUTexture ( size , * , layers = 0 , is_cubemap = False , format = 'RGBA8' , data = None )

This object opens up GPU textures.

Parameters :

- size ( int | Sequence [ int ] ) – Dimensions of the texture 1D, 2D, 3D or cubemap.

- layers ( int ) – Number of layers in texture array or number of cubemaps in cubemap array

- is_cubemap ( bool ) – Indicates the creation of a cubemap texture.

- format ( Literal [ 'RGBA8UI' , 'RGBA8I' , 'RGBA8' , 'RGBA32UI' , 'RGBA32I' , 'RGBA32F' , 'RGBA16UI' , 'RGBA16I' , 'RGBA16F' , 'RGBA16' , 'RG8UI' , 'RG8I' , 'RG8' , 'RG32UI' , 'RG32I' , 'RG32F' , 'RG16UI' , 'RG16I' , 'RG16F' , 'RG16' , 'R8UI' , 'R8I' , 'R8' , 'R32UI' , 'R32I' , 'R32F' , 'R16UI' , 'R16I' , 'R16F' , 'R16' , '`R11F_G11F_B10F`' , '`DEPTH32F_STENCIL8`' , '`DEPTH24_STENCIL8`' , '`SRGB8_A8`' , 'RGB16F' , '`SRGB8_A8_DXT1`' , '`SRGB8_A8_DXT3`' , '`SRGB8_A8_DXT5`' , '`RGBA8_DXT1`' , '`RGBA8_DXT3`' , '`RGBA8_DXT5`' , '`DEPTH_COMPONENT32F`' , '`DEPTH_COMPONENT24`' , '`DEPTH_COMPONENT16`' ] ) – Internal data format inside GPU memory.
`DEPTH24_STENCIL8` is deprecated, use `DEPTH32F_STENCIL8` .
`DEPTH_COMPONENT24` is deprecated, use `DEPTH_COMPONENT32F` .
- data (gpu.types.Buffer | None) – Buffer object to fill the texture.

[Related references](INDEX.md).

# gpu.types.GPUShaderCreateInfo: image ( slot , format , type , name , * , qualifiers = {'NO_RESTRICT'} )

image ( slot , format , type , name , * , qualifiers = {'`NO_RESTRICT`'} )

Declare an image resource for arbitrary load and store operations.

Parameters :

- slot ( int ) – The image resource index.

- format ( Literal [ 'RGBA8UI' , 'RGBA8I' , 'RGBA8' , 'RGBA32UI' , 'RGBA32I' , 'RGBA32F' , 'RGBA16UI' , 'RGBA16I' , 'RGBA16F' , 'RGBA16' , 'RG8UI' , 'RG8I' , 'RG8' , 'RG32UI' , 'RG32I' , 'RG32F' , 'RG16UI' , 'RG16I' , 'RG16F' , 'RG16' , 'R8UI' , 'R8I' , 'R8' , 'R32UI' , 'R32I' , 'R32F' , 'R16UI' , 'R16I' , 'R16F' , 'R16' , '`R11F_G11F_B10F`' , '`DEPTH32F_STENCIL8`' , '`DEPTH24_STENCIL8`' , '`SRGB8_A8`' , 'RGB16F' , '`SRGB8_A8_DXT1`' , '`SRGB8_A8_DXT3`' , '`SRGB8_A8_DXT5`' , '`RGBA8_DXT1`' , '`RGBA8_DXT3`' , '`RGBA8_DXT5`' , '`DEPTH_COMPONENT32F`' , '`DEPTH_COMPONENT24`' , '`DEPTH_COMPONENT16`' ] ) – The GPUTexture format that is passed to the shader.

- type ( Literal [ '`FLOAT_BUFFER`' , '`FLOAT_1D`' , '`FLOAT_1D_ARRAY`' , '`FLOAT_2D`' , '`FLOAT_2D_ARRAY`' , '`FLOAT_3D`' , '`FLOAT_CUBE`' , '`FLOAT_CUBE_ARRAY`' , '`INT_BUFFER`' , '`INT_1D`' , '`INT_1D_ARRAY`' , '`INT_2D`' , '`INT_2D_ARRAY`' , '`INT_3D`' , '`INT_CUBE`' , '`INT_CUBE_ARRAY`' , '`UINT_BUFFER`' , '`UINT_1D`' , '`UINT_1D_ARRAY`' , '`UINT_2D`' , '`UINT_2D_ARRAY`' , '`UINT_3D`' , '`UINT_CUBE`' , '`UINT_CUBE_ARRAY`' , '`SHADOW_2D`' , '`SHADOW_2D_ARRAY`' , '`SHADOW_CUBE`' , '`SHADOW_CUBE_ARRAY`' , '`DEPTH_2D`' , '`DEPTH_2D_ARRAY`' , '`DEPTH_CUBE`' , '`DEPTH_CUBE_ARRAY`' ] ) – The data type describing how the image is to be read in the shader.

- name ( str ) – The image resource name.

- qualifiers ( set [ Literal [ '`NO_RESTRICT`' , 'READ' , 'WRITE' ] ] ) – Set containing values that describe how the image resource is to be read or written.

[Related references](INDEX.md).

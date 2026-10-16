# gpu.types.GPUShaderCreateInfo: uniform_buf ( slot , type_name , name )

uniform_buf ( slot , type_name , name )

Declare a uniform variable whose type may be any of those listed in gpu.types.GPUShaderCreateInfo.typedef_source().

Parameters :

- slot ( int ) – The uniform variable index.

- type_name ( str ) – Name of the data type. It can be a struct type defined in the source passed through the gpu.types.GPUShaderCreateInfo.typedef_source().

- name ( str ) – The uniform variable name.

[Related references](INDEX.md).

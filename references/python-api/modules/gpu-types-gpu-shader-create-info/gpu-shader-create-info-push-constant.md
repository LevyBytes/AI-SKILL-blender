# gpu.types.GPUShaderCreateInfo: push_constant ( type , name , size = 0 )

push_constant ( type , name , size = 0 )

Declare a globally accessible constant.

Parameters :

- type ( Literal [ 'FLOAT' , 'VEC2' , 'VEC3' , 'VEC4' , 'MAT3' , 'MAT4' , 'UINT' , 'UVEC2' , 'UVEC3' , 'UVEC4' , 'INT' , 'IVEC2' , 'IVEC3' , 'IVEC4' , 'BOOL' ] ) – The data type of the constant.

- name ( str ) – Name of the constant.

- size ( int ) – If not zero, indicates that the constant is an array with the specified size.

[Related references](INDEX.md).

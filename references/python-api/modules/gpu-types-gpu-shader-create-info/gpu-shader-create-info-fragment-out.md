# gpu.types.GPUShaderCreateInfo: fragment_out ( slot , type , name , * , blend = 'NONE' )

fragment_out ( slot , type , name , * , blend = 'NONE' )

Declare a fragment output that maps to a framebuffer target slot.

Parameters :

- slot ( int ) – The attribute index.

- type ( Literal [ 'FLOAT' , 'VEC2' , 'VEC3' , 'VEC4' , 'MAT3' , 'MAT4' , 'UINT' , 'UVEC2' , 'UVEC3' , 'UVEC4' , 'INT' , 'IVEC2' , 'IVEC3' , 'IVEC4' , 'BOOL' ] ) – The data type of the output.

- name ( str ) – Name of the attribute.

- blend ( Literal [ 'NONE' , '`SRC_0`' , '`SRC_1`' ] ) – Dual Source Blending Index.

[Related references](INDEX.md).

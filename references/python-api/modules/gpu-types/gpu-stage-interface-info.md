# gpu.types.GPUStageInterfaceInfo

class gpu.types. GPUStageInterfaceInfo ( name )

List of varyings between shader stages.

Parameters :

name ( str ) – Name of the interface block.
flat ( type , name )

Append an attribute carrying the flat qualifier to the interface block.

Parameters :

- type ( Literal [ 'FLOAT' , 'VEC2' , 'VEC3' , 'VEC4' , 'MAT3' , 'MAT4' , 'UINT' , 'UVEC2' , 'UVEC3' , 'UVEC4' , 'INT' , 'IVEC2' , 'IVEC3' , 'IVEC4' , 'BOOL' ] ) – The data type of the attribute.

- name ( str ) – name of the attribute.
no_perspective ( type , name )

Append an attribute carrying the no_perspective qualifier to the interface block.

Parameters :

- type ( Literal [ 'FLOAT' , 'VEC2' , 'VEC3' , 'VEC4' , 'MAT3' , 'MAT4' , 'UINT' , 'UVEC2' , 'UVEC3' , 'UVEC4' , 'INT' , 'IVEC2' , 'IVEC3' , 'IVEC4' , 'BOOL' ] ) – The data type of the attribute.

- name ( str ) – name of the attribute.
smooth ( type , name )

Append an attribute carrying the smooth qualifier to the interface block.

Parameters :

- type ( Literal [ 'FLOAT' , 'VEC2' , 'VEC3' , 'VEC4' , 'MAT3' , 'MAT4' , 'UINT' , 'UVEC2' , 'UVEC3' , 'UVEC4' , 'INT' , 'IVEC2' , 'IVEC3' , 'IVEC4' , 'BOOL' ] ) – The data type of the attribute.

- name ( str ) – name of the attribute.
name

Name of the interface block.

Type :

str

[Related references](INDEX.md).

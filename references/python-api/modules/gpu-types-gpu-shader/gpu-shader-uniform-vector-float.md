# gpu.types.GPUShader: uniform_vector_float ( location , buffer , length , count )

uniform_vector_float ( location , buffer , length , count )

Supply the buffer that fills the uniform.

Parameters :

- location ( int ) – Location of the uniform variable to be modified.

- buffer ( Sequence [ float ] ) – The data that should be set. Can support the buffer protocol.

- length ( int ) – Size of the uniform data type:

- 1: float

- 2: vec2 or float[2]

- 3: vec3 or float[3]

- 4: vec4 or float[4]

- 9: mat3

- 16: mat4

- count ( int ) – Specifies the number of elements, vector or matrices that are to be modified.

[Related references](INDEX.md).

# gpu_extras.batch

## gpu_extras submodule (gpu_extras.batch)

### gpu_extras submodule (gpu_extras.batch)
gpu_extras.batch. batch_for_shader ( shader , type , content , * , indices = None )

Give back a batch that is already set up to match the shader.

Parameters :

- shader (gpu.types.GPUShader) – shader for which a compatible format will be computed.

- type ( Literal [ 'POINTS' , 'LINES' , 'TRIS' , '`LINE_STRIP`' , '`TRI_STRIP`' , '`LINES_ADJ`' , '`TRIS_ADJ`' , '`LINE_STRIP_ADJ`' ] ) – The primitive type of batch geometry.

- content ( dict [ str , Buffer | Sequence [ float ] | Sequence [ int ] | Sequence [ Sequence [ float ] ] | Sequence [ Sequence [ int ] ] ] ) – Maps the name of the shader attribute with the data to fill the vertex buffer.
For the dictionary values see documentation for gpu.types.GPUVertBuf.attr_fill data argument.

Returns :

compatible batch

Return type :

[Related references](INDEX.md).

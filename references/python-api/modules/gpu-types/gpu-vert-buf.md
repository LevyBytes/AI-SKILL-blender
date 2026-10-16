# gpu.types.GPUVertBuf

class gpu.types. GPUVertBuf ( format , len )

Holds a VBO.

Parameters :

- format (gpu.types.GPUVertFormat) – Vertex format.

- len ( int ) – Amount of vertices that will fit into this buffer.
attr_fill ( id , data )

Place data into the buffer for one specific attribute.

Parameters :

- id ( int | str ) – Either the name or the id of the attribute.

- data (Buffer | Sequence [ float ] | Sequence [ int ] | Sequence [ Sequence [ float ] ] | Sequence [ Sequence [ int ] ] ) – Buffer or sequence of data that should be stored in the buffer

[Related references](INDEX.md).

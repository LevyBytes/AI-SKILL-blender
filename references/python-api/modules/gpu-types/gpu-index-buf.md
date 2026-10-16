# gpu.types.GPUIndexBuf

class gpu.types. GPUIndexBuf ( type , seq )

Holds an index buffer.

Parameters :

- type ( Literal [ 'POINTS' , 'LINES' , 'TRIS' , '`LINES_ADJ`' , '`TRIS_ADJ`' ] ) – The primitive type this index buffer is composed of.

- seq (Buffer | Sequence [ int ] | Sequence [ Sequence [ int ] ] ) – Indices this index buffer will contain.
Whether a 1D or 2D sequence is required depends on the type.
Optionally the sequence can support the buffer protocol.

[Related references](INDEX.md).

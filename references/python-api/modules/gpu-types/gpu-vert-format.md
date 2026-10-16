# gpu.types.GPUVertFormat

class gpu.types. GPUVertFormat

This object carries the layout details of a vertex buffer.
attr_add ( id , comp_type , len , fetch_mode )

Register a new attribute on the format.

Parameters :

- id ( str ) – Name of the attribute. Often position , normal , …

- comp_type ( Literal [ 'I8' , 'U8' , 'I16' , 'U16' , 'I32' , 'U32' , 'F32' , 'I10' ] ) – The data type that will be used to store the value in memory.

- len ( int ) – How many individual values the attribute consists of
(e.g. 2 for uv coordinates).

- fetch_mode ( Literal [ 'FLOAT' , 'INT' , '`INT_TO_FLOAT_UNIT`' ] ) – How values from memory will be converted when used in the shader.
This is mainly useful for memory optimizations when you want to store values with
reduced precision. E.g. you can store a float in only 1 byte but it will be
converted to a normal 4 byte float when used.

[Related references](INDEX.md).

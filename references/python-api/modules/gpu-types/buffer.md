# gpu.types.Buffer

### GPU Types (gpu.types)
class gpu.types. Buffer ( format , dimensions , data )

Lets Python reach GPU functions that expect a pointer.

Parameters :

- format ( Literal [ 'FLOAT' , 'INT' , 'UINT' , 'UBYTE' , '`UINT_24_8`' , '10_11_11_REV' ] ) – Format type to interpret the buffer.
`UINT_24_8` is deprecated, use FLOAT instead.

- dimensions ( int | Sequence [ int ] ) – Array describing the dimensions.

- data (Buffer | Sequence [ float ] | Sequence [ int ] ) – Optional data array.
to_list ( )

Hand back the buffer as a list.

Returns :

The buffer as a list.

Return type :

list
dimensions

Undocumented, consider contributing.

[Related references](INDEX.md).

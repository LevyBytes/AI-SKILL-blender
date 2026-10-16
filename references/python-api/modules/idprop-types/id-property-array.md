# idprop.types.IDPropertyArray

class idprop.types. IDPropertyArray

A fixed-type array of values that you can index into and slice.
to_list ( )

Hand back the array as a list.

Returns :

The array as a list.

Return type :

list[int] | list[float] | list[bool]
typecode

The type of the data in the array {‘f’: float (32-bit), ‘d’: double (64-bit), ‘i’: int, ‘b’: bool}. Both ‘f’ and ‘d’ use Python’s float type but differ in storage precision.

[Related references](INDEX.md).

# freestyle.utils: freestyle.utils. integrate ( func , it , it_end , integration_type )

freestyle.utils. integrate ( func , it , it_end , integration_type ) 

Collapses into one value the set of values evaluated at each 0D element of a given 1D element.

Parameters :

- func ( UnaryFunction0D ) – The UnaryFunction0D used to compute a value at each
Interface0D.

- it ( Interface0DIterator ) – The Interface0DIterator used to iterate over the 0D
elements of this 1D element. The integration will occur over
the 0D elements starting from the one pointed by it.

- it_end ( Interface0DIterator ) – The Interface0DIterator pointing the end of the 0D
elements of the 1D element.

- integration_type ( IntegrationType ) – The integration method used to compute a
single value from a set of values.

Returns :

The single value obtained for the 1D element. The return
value type is float if func is of the UnaryFunction0DDouble
or UnaryFunction0DFloat type, and int if func is of the
UnaryFunction0DUnsigned type.

Return type :

int | float

[Related references](INDEX.md).

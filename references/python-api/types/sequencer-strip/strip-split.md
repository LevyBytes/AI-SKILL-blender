# bpy.types.Strip: split

split ( frame , split_method , * , ignore_connections = False )

Split Strip

Parameters :

- frame ( int ) – Frame where to split the strip (in [-inf, inf])

- split_method ( Literal [ 'SOFT' , 'HARD' ] ) – (never None)

- ignore_connections ( bool ) – Don’t propagate split to connected strips (optional)

Returns :

Right side Strip

Return type :

Strip

[Related references](INDEX.md).

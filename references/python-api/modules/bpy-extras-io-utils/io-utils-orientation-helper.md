# bpy_extras.io_utils: bpy_extras.io_utils. orientation_helper ( axis_forward = 'Y' , axis_up = 'Z' )

bpy_extras.io_utils. orientation_helper ( axis_forward = 'Y' , axis_up = 'Z' ) 

A decorator for import/export classes that adds the properties the axis conversion system and IO helpers need,
preset to the given default axes.

Parameters :

- axis_forward ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – The default forward axis.

- axis_up ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – The default up axis.

Returns :

A class decorator.

Return type :

Callable[[type], type]

[Related references](INDEX.md).

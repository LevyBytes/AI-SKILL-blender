# bpy_extras.io_utils: bpy_extras.io_utils. axis_conversion ( from_forward = 'Y' , from_up = 'Z' , to_forward = 'Y' , to_up = 'Z' )

bpy_extras.io_utils. axis_conversion ( from_forward = 'Y' , from_up = 'Z' , to_forward = 'Y' , to_up = 'Z' ) 

Every argument names an axis;
the first two describe the source and the last two the target.

Parameters :

- from_forward ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Source forward axis.

- from_up ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Source up axis.

- to_forward ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Target forward axis.

- to_up ( Literal [ 'X' , 'Y' , 'Z' , '-X' , '-Y' , '-Z' ] ) – Target up axis.

Returns :

The conversion matrix.

Return type :

[Related references](INDEX.md).

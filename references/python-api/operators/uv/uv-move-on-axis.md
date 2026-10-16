# bpy.ops.uv.move_on_axis

bpy.ops.uv. move_on_axis ( * , type = 'UDIM' , axis = 'X' , distance = 1 ) 

Shifts UVs along one axis

Parameters :

- type ( Literal [ 'DYNAMIC' , 'PIXEL' , 'UDIM' ] ) – Type, Move Type (optional)

- DYNAMIC
Dynamic – Step by the dynamic grid.

- PIXEL
Pixel – Step by a pixel.

- UDIM
UDIM – Step by a UDIM.

- axis ( Literal [ 'X' , 'Y' ] ) – Axis, Axis to move UVs on (optional)

- X
X axis – Shift vertices along the X axis.

- Y
Y axis – Shift vertices along the Y axis.

- distance ( int ) – Distance, Distance to move UVs (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.paint.weight_gradient

bpy.ops.paint. weight_gradient ( * , type = 'LINEAR' , xstart = 0 , xend = 0 , ystart = 0 , yend = 0 , flip = False , cursor = 5 ) 

Apply a graduated weight transition by drawing a line across selected vertices

Parameters :

- type ( Literal [ 'LINEAR' , 'RADIAL' ] ) – Type, (optional)

- xstart ( int ) – X Start, (in [-inf, inf], optional)

- xend ( int ) – X End, (in [-inf, inf], optional)

- ystart ( int ) – Y Start, (in [-inf, inf], optional)

- yend ( int ) – Y End, (in [-inf, inf], optional)

- flip ( bool ) – Flip, (optional)

- cursor ( int ) – Cursor, Mouse cursor style to use during the modal operator (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

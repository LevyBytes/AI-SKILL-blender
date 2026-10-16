# bpy.ops.view3d.view_roll

bpy.ops.view3d. view_roll ( * , angle = 0.0 , type = 'ANGLE' ) 

Tilts the viewport

Parameters :

- angle ( float ) - Roll, (in [-inf, inf], optional)

- type ( Literal [ 'ANGLE' , 'LEFT' , 'RIGHT' ] ) - Roll Angle Source, Mechanism for computing roll rotation (optional)

- ANGLE
Roll Angle - Tilts using a supplied angle.

- LEFT
Roll Left - Tilts the viewport leftward.

- RIGHT
Roll Right - Tilts the viewport rightward.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

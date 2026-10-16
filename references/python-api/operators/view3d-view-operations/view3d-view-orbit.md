# bpy.ops.view3d.view_orbit

bpy.ops.view3d. view_orbit ( * , angle = 0.0 , type = 'ORBITLEFT' ) 

Revolves the viewport

Parameters :

- angle ( float ) - Roll, (in [-inf, inf], optional)

- type ( Literal [ 'ORBITLEFT' , 'ORBITRIGHT' , 'ORBITUP' , 'ORBITDOWN' ] ) - Orbit, Rotational direction (optional)

- ORBITLEFT
Orbit Left - Spin the viewport leftward.

- ORBITRIGHT
Orbit Right - Spin the viewport rightward.

- ORBITUP
Orbit Up - Rotate the viewport upward.

- ORBITDOWN
Orbit Down - Rotate the viewport downward.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

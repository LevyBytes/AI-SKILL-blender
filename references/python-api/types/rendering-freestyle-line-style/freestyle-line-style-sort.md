# bpy.types.FreestyleLineStyle: sort_key, sort_order

sort_key 

Pick the value that determines how chains stack on top of one another (default '`DISTANCE_FROM_CAMERA`' )

- `DISTANCE_FROM_CAMERA`
Distance from Camera – Sort by distance from camera (closer lines lie on top of further lines).

- 2`D_LENGTH`
2D Length – Sort by curvilinear 2D length (longer lines lie on top of shorter lines).

- `PROJECTED_X`
Projected X – Sort by the projected X value in the image coordinate system.

- `PROJECTED_Y`
Projected Y – Sort by the projected Y value in the image coordinate system.

Type :

Literal[‘`DISTANCE_FROM_CAMERA`’, ‘2`D_LENGTH`’, ‘`PROJECTED_X`’, ‘`PROJECTED_Y`’]
sort_order 

Pick the direction in which the sort key is applied (default 'DEFAULT' )

- DEFAULT
Default – Default order of the sort key.

- REVERSE
Reverse – Reverse order.

Type :

Literal[‘DEFAULT’, ‘REVERSE’]

[Related references](INDEX.md).

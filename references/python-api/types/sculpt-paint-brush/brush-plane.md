# bpy.types.Brush: plane_depth, plane_height, plane_inversion_mode, plane_offset, plane_trim

plane_depth

Furthest distance below the plane that vertices are affected. Larger depth reaches vertices deeper beneath the plane. (in [0, 1], default 0.0)

Type :

float
plane_height

Furthest distance above the plane that vertices are affected. Larger height reaches vertices higher above the plane. (in [0, 1], default 1.0)

Type :

float
plane_inversion_mode

Inversion Mode (default '`INVERT_DISPLACEMENT`' )

- `INVERT_DISPLACEMENT`
Invert Displacement – Pushes the vertices in the opposite direction, away from the plane..

- `SWAP_DEPTH_AND_HEIGHT`
Swap Height and Depth – Exchanges what Height and Depth control..

Type :

Literal['`INVERT_DISPLACEMENT`', '`SWAP_DEPTH_AND_HEIGHT`']
plane_offset

Shift the plane the brush works on toward or away from the object's surface (in [-2, 2], default 0.0)

Type :

float
plane_trim

Any vertex farther from the offset plane than this is left untouched (in [0, 1], default 0.5)

Type :

float

[Related references](INDEX.md).

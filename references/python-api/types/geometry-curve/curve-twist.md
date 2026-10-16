# bpy.types.Curve: twist_mode, twist_smooth

twist_mode

Which tilt-calculation method 3D Curves use (default 'MINIMUM' )

- `Z_UP`
Z-Up – Derive each point's twist from the Z-Up axis.

- MINIMUM
Minimum – Keep the twist as small as possible across the whole curve.

- TANGENT
Tangent – Derive the twist from the tangent.

Type :

Literal['`Z_UP`', 'MINIMUM', 'TANGENT']
twist_smooth

Smoothing iteration for tangents (in [-inf, inf], default 0.0)

Type :

float

[Related references](INDEX.md).

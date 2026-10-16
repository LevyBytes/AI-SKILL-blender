# bpy.types.Curve: taper_object, taper_radius_mode

taper_object

Curve object name that defines the taper (width)

Type :

Object
taper_radius_mode

Pick how the spline point's effective radius is worked out once a taper object is in play (default 'OVERRIDE' )

- OVERRIDE
Override – Swap the spline point's radius out for the taper radius.

- MULTIPLY
Multiply – Scale the spline point's radius by the taper radius.

- ADD
Add – Sum the bevel point's radius together with the taper radius.

Type :

Literal['OVERRIDE', 'MULTIPLY', 'ADD']

[Related references](INDEX.md).

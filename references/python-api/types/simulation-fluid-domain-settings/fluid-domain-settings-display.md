# bpy.types.FluidDomainSettings: display_interpolation, display_thickness

display_interpolation

Which interpolation is applied to smoke and fire volumes shown in solid mode (default 'LINEAR' )

- LINEAR
Linear – Good smoothness and speed.

- CUBIC
Cubic – Smoothed high quality interpolation, but slower.

- CLOSEST
Closest – No interpolation.

Type :

Literal[‘LINEAR’, ‘CUBIC’, ‘CLOSEST’]
display_thickness

Thickness of smoke display in the viewport (in [0.001, 1000], default 1.0)

Type :

float

[Related references](INDEX.md).

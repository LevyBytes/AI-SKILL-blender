# bpy.types.View3DShading: cavity_ridge_factor, cavity_type, cavity_valley_factor

cavity_ridge_factor

Strength applied to the cavity ridges (in [0, 250], default 1.0)

Type :

float
cavity_type

Picks how cavity shading is computed (default 'SCREEN' )

- WORLD
World – Compute cavity in world space; handy for broad occlusion.

- SCREEN
Screen – Curvature-driven shading that brings out small surface detail.

- BOTH
Both – Combine the two cavity methods at once.

Type :

Literal['WORLD', 'SCREEN', 'BOTH']
cavity_valley_factor

Strength applied to the cavity valleys (in [0, 250], default 1.0)

Type :

float

[Related references](INDEX.md).

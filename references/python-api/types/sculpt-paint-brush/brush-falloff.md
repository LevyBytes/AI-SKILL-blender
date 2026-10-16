# bpy.types.Brush: falloff_angle, falloff_shape

falloff_angle

Concentrate paint on faces angled toward the view within this angle (in [0, 1.5708], default 0.0)

Type :

float
falloff_shape

Whether falloff is projected or spherical (default 'SPHERE' )

- SPHERE
Sphere – Spreads brush influence outward from the center in a sphere.

- PROJECTED
Projected – Spreads brush influence as a flat circle projected from the view.

Type :

Literal['SPHERE', 'PROJECTED']

[Related references](INDEX.md).

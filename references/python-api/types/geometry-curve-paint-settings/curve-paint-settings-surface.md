# bpy.types.CurvePaintSettings: surface_offset, surface_plane

surface_offset

Lift the stroke off the surface by this amount (in [-10, 10], default 0.0)

Type :

float
surface_plane

Which plane a projected stroke is drawn in (default '`NORMAL_VIEW`' )

- `NORMAL_VIEW`
Normal to Surface – Lay the stroke in a plane that stands at right angles to the surface.

- `NORMAL_SURFACE`
Tangent to Surface – Lay the stroke flat within the surface plane.

- VIEW
View – Lay the stroke in a plane that lines up with the viewport.

Type :

Literal['`NORMAL_VIEW`', '`NORMAL_SURFACE`', 'VIEW']

[Related references](INDEX.md).

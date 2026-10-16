# bpy.types.Curve: fill_mode, fill_rule, fill_solver

fill_mode

Mode of filling curve (default 'FULL' )

Type :

Literal['FULL', 'BACK', 'FRONT', 'HALF']
fill_rule

Fill rule for Delaunay fill solver (default '`EVEN_ODD`' )

- `EVEN_ODD`
Even-Odd – Flip between inside and outside according to how many crossings are counted.

- NONZERO
Non-Zero – Where overlapping curves wind the same way, treat the result as a single union.

Type :

Literal['`EVEN_ODD`', 'NONZERO']
fill_solver

Triangulation solver for filling 2D curves (default '`SWEEP_LINE`' )

- `SWEEP_LINE`
Sweep Line – Quick, though it can't cope with self-intersection.

- CDT
Delaunay – Constrained Delaunay Triangulation (CDT), sturdy and able to handle self-intersections.

Type :

Literal['`SWEEP_LINE`', 'CDT']

[Related references](INDEX.md).

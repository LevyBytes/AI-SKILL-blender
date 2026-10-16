# bpy.types.GreasePencilSimplifyModifier: mode

mode

How to simplify the stroke (default 'FIXED' )

- FIXED
Fixed – Drop every other vertex along the stroke, sparing the end points.

- ADAPTIVE
Adaptive – Run a Ramer-Douglas-Peucker pass that thins the stroke while holding its overall shape.

- SAMPLE
Sample – Lay the stroke out again using segments of the length you set.

- MERGE
Merge – Collapse stroke vertices that sit closer together than a set distance.

Type :

Literal['FIXED', 'ADAPTIVE', 'SAMPLE', 'MERGE']

[Related references](INDEX.md).

# bpy.types.SoftBodySettings: collision_collection, collision_type

collision_collection

Limit colliders to this collection

Type :

Collection
collision_type

Choose Collision Type (default 'MANUAL' )

- MANUAL
Manual – Manual adjust.

- AVERAGE
Average – Average Spring length * Ball Size.

- MINIMAL
Minimal – Minimal Spring length * Ball Size.

- MAXIMAL
Maximal – Maximal Spring length * Ball Size.

- MINMAX
AvMinMax – (Min+Max)/2 * Ball Size.

Type :

Literal[‘MANUAL’, ‘AVERAGE’, ‘MINIMAL’, ‘MAXIMAL’, ‘MINMAX’]

[Related references](INDEX.md).

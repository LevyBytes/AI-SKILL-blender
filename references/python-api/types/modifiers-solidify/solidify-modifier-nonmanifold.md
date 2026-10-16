# bpy.types.SolidifyModifier: nonmanifold_boundary_mode, nonmanifold_merge_threshold, nonmanifold_thickness_mode

nonmanifold_boundary_mode

Picks which algorithm handles boundary adjustment (default 'NONE' )

- NONE
None – No shape correction.

- ROUND
Round – Round open perimeter shape.

- FLAT
Flat – Flat open perimeter shape.

Type :

Literal[‘NONE’, ‘ROUND’, ‘FLAT’]
nonmanifold_merge_threshold

Below this distance, degenerate geometry gets merged together (in [0, 1], default 0.0001)

Type :

float
nonmanifold_thickness_mode

Picks which algorithm computes thickness (default 'CONSTRAINTS' )

- FIXED
Fixed – Most basic thickness calculation.

- EVEN
Even – Even thickness calculation which takes the angle between faces into account.

- CONSTRAINTS
Constraints – Thickness calculation using constraints, most advanced.

Type :

Literal[‘FIXED’, ‘EVEN’, ‘CONSTRAINTS’]

[Related references](INDEX.md).

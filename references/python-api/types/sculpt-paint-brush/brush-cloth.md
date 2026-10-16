# bpy.types.Brush: cloth_constraint_softbody_strength, cloth_damping, cloth_deform_type, cloth_force_falloff_type, cloth_mass, cloth_sim_falloff, cloth_sim_limit, cloth_simulation_area_type

cloth_constraint_softbody_strength

Degree to which the cloth holds onto its starting shape, behaving like a soft body (in [0, 1], default 0.0)

Type :

float
cloth_damping

Degree to which applied forces travel through the cloth (in [0.01, 1], default 0.01)

Type :

float
cloth_deform_type

The kind of deformation the brush applies (default 'DRAG' )

Type :

Literal['DRAG', 'PUSH', '`PINCH_POINT`', '`PINCH_PERPENDICULAR`', 'INFLATE', 'GRAB', 'EXPAND', '`SNAKE_HOOK`']
cloth_force_falloff_type

The shape the brush uses to push force into the cloth (default 'RADIAL' )

Type :

Literal['RADIAL', 'PLANE']
cloth_mass

Weight assigned to each simulated particle (in [0.01, 2], default 1.0)

Type :

float
cloth_sim_falloff

Region over which the simulation's effects fade out (in [0, 1], default 0.75)

Type :

float
cloth_sim_limit

Multiplier relative to the radius that caps how far the cloth simulation reaches (in [0.1, 10], default 2.5)

Type :

float
cloth_simulation_area_type

Which portion of the mesh gets simulated while the stroke runs (default 'LOCAL' )

- LOCAL
Local – Simulates just a region around the brush, bounded by a fixed radius.

- GLOBAL
Global – Simulates the whole mesh.

- DYNAMIC
Dynamic – Keeps the simulated area following the brush as it moves.

Type :

Literal['LOCAL', 'GLOBAL', 'DYNAMIC']

[Related references](INDEX.md).

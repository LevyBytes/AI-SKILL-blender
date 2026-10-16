# bpy.types.Brush: boundary_deform_type, boundary_falloff_type, boundary_offset

boundary_deform_type

The kind of deformation the brush applies (default 'BEND' )

Type :

Literal['BEND', 'EXPAND', 'INFLATE', 'GRAB', 'TWIST', 'SMOOTH']
boundary_falloff_type

Manner in which the brush falloff spreads over the boundary (default 'CONSTANT' )

- CONSTANT
Constant – Deforms the whole boundary by the same amount.

- RADIUS
Brush Radius – Confines the deformation to a region bounded by the brush radius.

- LOOP
Loop – Lays the brush falloff out in a repeating loop.

- `LOOP_INVERT`
Loop and Invert – Repeats the falloff radius in a loop, flipping the displacement direction with each repetition.

Type :

Literal['CONSTANT', 'RADIUS', 'LOOP', '`LOOP_INVERT`']
boundary_offset

How far the boundary origin sits from the brush radius (in [0, 30], default 0.0)

Type :

float

[Related references](INDEX.md).

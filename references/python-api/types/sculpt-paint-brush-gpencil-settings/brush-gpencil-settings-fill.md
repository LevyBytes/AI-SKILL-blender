# bpy.types.BrushGpencilSettings: fill_direction, fill_draw_mode, fill_extend_mode, fill_factor, fill_layer_mode, fill_simplify_level, fill_threshold

fill_direction

Orientation of the fill operation (default 'NORMAL' )

- NORMAL
Normal – Fill internal area.

- INVERT
Inverted – Fill inverted area.

Type :

Literal['NORMAL', 'INVERT']
fill_draw_mode

Which strokes define fill boundaries (default 'BOTH' )

- BOTH
All – Use both visible strokes and edit lines as fill boundary limits.

- STROKE
Strokes – Use visible strokes as fill boundary limits.

- CONTROL
Edit Lines – Use edit lines as fill boundary limits.

Type :

Literal['BOTH', 'STROKE', 'CONTROL']
fill_extend_mode

How to connect stroke gaps when filling (default 'EXTEND' )

- EXTEND
Extend – Extend strokes in straight lines.

- RADIUS
Radius – Connect endpoints that are close together.

Type :

Literal['EXTEND', 'RADIUS']
fill_factor

Adjustment for boundary precision; greater values increase accuracy but reduce speed (in [0.05, 8], default 0.0)

Type :

float
fill_layer_mode

Which layers supply fill boundaries (default 'VISIBLE' )

- VISIBLE
Visible – Visible layers.

- ACTIVE
Active – Only active layer.

- ABOVE
Layer Above – Layer above active.

- BELOW
Layer Below – Layer below active.

- `ALL_ABOVE`
All Above – All layers above active.

- `ALL_BELOW`
All Below – All layers below active.

Type :

Literal['VISIBLE', 'ACTIVE', 'ABOVE', 'BELOW', '`ALL_ABOVE`', '`ALL_BELOW`']
fill_simplify_level

Count of simplification passes (higher counts reduce accuracy) (in [0, 10], default 0)

Type :

int
fill_threshold

Color opacity level for detecting transparent regions during fill (in [0, 1], default 0.0)

Type :

float

[Related references](INDEX.md).

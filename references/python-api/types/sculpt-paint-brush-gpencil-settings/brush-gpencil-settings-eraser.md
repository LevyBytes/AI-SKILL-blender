# bpy.types.BrushGpencilSettings: eraser_mode, eraser_strength_factor, eraser_thickness_factor

eraser_mode

Behavior of the eraser tool (default 'SOFT' )

- SOFT
Dissolve – Erase strokes, fading their points strength and thickness.

- HARD
Point – Erase stroke points.

- STROKE
Stroke – Erase entire strokes.

Type :

Literal['SOFT', 'HARD', 'STROKE']
eraser_strength_factor

Removal intensity affecting stroke color strength (in [0, 100], default 0.0)

Type :

float
eraser_thickness_factor

Removal intensity affecting stroke width (in [0, 100], default 0.0)

Type :

float

[Related references](INDEX.md).

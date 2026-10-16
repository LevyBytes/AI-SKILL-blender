# bpy.types.BrushGpencilSettings: vertex_color_factor, vertex_mode

vertex_color_factor

Blending strength between vertex color and brush color (in [0, 1], default 0.0)

Type :

float
vertex_mode

How vertex color interacts with strokes (default 'STROKE' )

- STROKE
Stroke – Vertex Color affects to Stroke only.

- FILL
Fill – Vertex Color affects to Fill only.

- BOTH
Stroke & Fill – Vertex Color affects to Stroke and Fill.

Type :

Literal['STROKE', 'FILL', 'BOTH']

[Related references](INDEX.md).

# bpy.types.Brush: stroke_method

stroke_method

(default 'DOTS' )

- DOTS
Dots – Lay paint down at each mouse-move step.

- `DRAG_DOT`
Drag Dot – Lets you carefully place one single dot.

- SPACE
Space – Restrict brush application to the gap set by spacing.

- AIRBRUSH
Airbrush – Keep spraying paint for as long as the mouse is held.

- ANCHORED
Anchored – Pin the brush to where it first landed.

- LINE
Line – Stroke out a line whose dabs are spaced according to spacing.

- CURVE
Curve – Lay the stroke along a Bézier curve (dabs spaced according to spacing).

Type :

Literal['DOTS', '`DRAG_DOT`', 'SPACE', 'AIRBRUSH', 'ANCHORED', 'LINE', 'CURVE']

[Related references](INDEX.md).

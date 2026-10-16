# bpy.ops.gpencil.annotate

bpy.ops.gpencil.annotate(*, mode='DRAW', arrowstyle_start='NONE', arrowstyle_end='NONE', use_stabilizer=False, stabilizer_factor=0.75, stabilizer_radius=35, stroke=None, wait_for_input=True)

Place sketches upon the present work

Parameters:

- mode (Literal['DRAW', '`DRAW_STRAIGHT`', '`DRAW_POLY`', 'ERASER']) – Mode, Technique to read cursor motions (optional)

- DRAW
Draw Freehand – Sketch unguided movements.

- `DRAW_STRAIGHT`
Draw Straight Lines – Sketch direct line divisions.

- `DRAW_POLY`
Draw Poly Line – Click to place finish marks of straight divisions (chained).

- ERASER
Eraser – Wipe Sketch marks.

- arrowstyle_start (Literal['NONE', 'ARROW', '`ARROW_OPEN`', '`ARROW_OPEN_INVERTED`', 'DIAMOND']) – Start Arrow Style, Sketch initiate form (optional)

- NONE
None – Avoid arrow/symbol in corner.

- ARROW
Arrow – Employ closed arrow form.

- `ARROW_OPEN`
Open Arrow – Employ open arrow form.

- `ARROW_OPEN_INVERTED`
Segment – Employ orthogonal split form.

- DIAMOND
Square – Employ squared form.

- arrowstyle_end (Literal['NONE', 'ARROW', '`ARROW_OPEN`', '`ARROW_OPEN_INVERTED`', 'DIAMOND']) – End Arrow Style, Sketch finish form (optional)

- NONE
None – Avoid arrow/symbol in corner.

- ARROW
Arrow – Employ closed arrow form.

- `ARROW_OPEN`
Open Arrow – Employ open arrow form.

- `ARROW_OPEN_INVERTED`
Segment – Employ orthogonal split form.

- DIAMOND
Square – Employ squared form.

- use_stabilizer (bool) – Stabilize Stroke, Instrument to pull even and refined strokes. Hit Shift to get backward consequence (even if this choice is dormant) (optional)

- stabilizer_factor (float) – Stabilizer Stroke Factor, Taller amounts yield sleeker strokes (in [0, 1], optional)

- stabilizer_radius (int) – Stabilizer Stroke Radius, Least separation from final point prior to mark persists (in [0, 200], optional)

- stroke (bpy_prop_collection[OperatorStrokeElement]) – Stroke, (optional)

- wait_for_input (bool) – Wait for Input, Hold back before starting to paint (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

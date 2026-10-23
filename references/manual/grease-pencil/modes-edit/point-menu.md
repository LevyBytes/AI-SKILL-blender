# Point Menu

## Point Menu

**Extrude.**

Menu ‣ Point ‣ Extrude; Toolbar ‣ Extrude; shortcut E. Duplicates selected points, which can then be moved; the new points remain connected to the originals.

Note: Since Grease Pencil strokes have only one start and end point, extruding intermediate points creates a new stroke.

**Smooth.**

Menu ‣ Point ‣ Smooth. Softens strokes by reducing location differences among points while maintaining fluid appearance.

Iterations: number of procedure repeats.

Factor: smoothness amount to apply.

Smooth Endpoints: applies smoothing to the stroke's start and end.

Keep Shape: tries to retain the stroke's overall geometry.

Position: when enabled, affects point location.

Radius: when enabled, affects point thickness.

Opacity: when enabled, affects point strength (alpha).

**Vertex Groups.**

Operators for vertex group management.

**Set Handle Type.**

Menu ‣ Point ‣ Set Handle Type; shortcut V. Sets the handle type for Bézier curve points in the selection.

Type - the target handle type:
- Auto: automatic length and direction for smoothest result; converts to Align when moved.
- Vector: both handle parts point to adjacent handles, allowing straight lines or sharp corners; converts to Free when moved.
- Align: handles lie in a straight line for continuous curves without sharp angles.
- Free: independent handles.
- Toggle Free/Align: replaces Free with Align and vice versa.

**Set Corner Type.**

Menu ‣ Point ‣ Set Corner Type. Controls how corners between strokes or segments appear when using stroke thickness or fills, affecting geometry joins at sharp angles.

Corner Type: the style for selected points:
- Round: smoothly rounds the corner with a curved transition.
- Flat: cuts the corner flat with a beveled join.
- Sharp: preserves the original angle.

Miter Cut Angle: angle threshold (degrees) for flattening sharp corners; corners sharper than this become flat when Corner Type is Flat or Round.

[Related references](INDEX.md).

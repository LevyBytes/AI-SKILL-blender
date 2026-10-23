# Selecting Grease Pencil Elements

## Selecting Grease Pencil Elements

**Select Mode.**

Edit Mode offers three selection modes accessible via header buttons or shortcuts 1, 2, 3.

Points: select individual points.

Strokes: select an entire stroke.

Segments: select all points between other strokes.

**Select All/None/Invert.**

Behaves identically to Object Mode.

**Select Random.**

Menu ‣ Select ‣ Select Random. Randomly selects unselected points or strokes.

Ratio: probability that an unselected element gets picked (not percentage count).

Random Seed: seed for the pseudo-random number generator.

Action: toggle between picking and unpicking elements.

**Select Alternated.**

Menu ‣ Select ‣ Select Alternated. Picks alternate points in selected strokes.

**Select More/Less.**

Menu ‣ Select ‣ More/Less; shortcuts Ctrl+NumpadPlus, Ctrl+NumpadMinus. Expands or shrinks the current selection within a stroke (never crossing stroke boundaries).

More: for each selected point, select all linked points (one or two adjacent ones).

Less: for each selected point, retain the selection only if every linked point is also selected; else remove it.

Hint: when all stroke points are picked, no change occurs (all linked ones are inherently selected, so More has nothing to add). Identical behavior occurs when no points are selected.

**By Stroke Type.**

Menu ‣ Select ‣ By Stroke Type. Selects curves based on type.

Type:
- Stroke: all stroke curves (outlines).
- Fill: all fill curves (enclosed filled shapes).

Deselect: when enabled, matching curves are deselected instead of selected.

**Select Similar.**

Menu ‣ Select ‣ Select Similar; shortcut Shift+G. Selects all strokes with similar characteristics.

Mode - the characteristic to compare:
- Layer: points/strokes with a similar layer index.
- Material: points/strokes with a similar material index.
- Vertex Color: points/strokes with a similar vertex color.
- Radius: points/strokes with a similar stroke radius.
- Opacity: points/strokes with a similar layer opacity.

Threshold: how closely characteristics must match.

**Select Fill.**

Menu ‣ Select ‣ Select Fill; shortcut Ctrl+L. Selects all curves belonging to the same fill region as the active curve.

Grease Pencil fills may consist of multiple boundary curves; this operator grows the selection to encompass all curves that bound the same enclosed fill area, valuable when transforming entire filled compositions.

**Select Linked.**

Menu ‣ Select ‣ Select Linked; shortcut L. Adds the cursor's nearest control point and all linked points (all points in the same stroke) to the selection.

**Select First/Last.**

Menu ‣ Select ‣ First/Last. Toggles selection of the first or last point(s) of strokes in the object, useful for quickly finding stroke starts.

[Related references](INDEX.md).

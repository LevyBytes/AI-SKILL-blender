# Snap to Symmetry

## Snap to Symmetry

### Snap to Symmetry

Reference

Mode:

Edit Mode

Menu:

Mesh → Snap to Symmetry

Snap to Symmetry corrects near-symmetrical meshes to perfect symmetry. Unlike Symmetrize, which cuts one half and mirrors the other, this operator pairs vertices by position and relocates them.

Useful after accidentally moving vertices while Mesh Symmetry was off.

### Options

Direction
The axis and direction of effect, in local object space.
Example: -X to +X affects vertices left of the origin (negative X) and aligns them with those on the right (positive X).

Threshold
Search radius for discovering matching vertices.

Factor
At 1, both vertices in a pair move to the "from" side position. At 0, both go to the "to" side.
Intermediate values interpolate; 0.5 moves both to their average position.

Center
Shifts vertices near the symmetry plane to sit exactly on it (setting their Direction-axis coordinate to zero).

| Description | Description |
| --- | --- |
| Before Snap to Symmetry. | After Snap to Symmetry. |

[Related references](INDEX.md).

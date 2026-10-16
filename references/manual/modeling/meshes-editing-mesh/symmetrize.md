# Symmetrize

## Symmetrize

### Symmetrize

Reference

Mode:

Edit Mode

Menu:

Mesh → Symmetrize

Symmetrize rapidly produces a symmetrical mesh by performing:

- Divides selected geometry along the object's origin using an infinite plane, similar to Bisect.

- Removes geometry on one plane side.

- Duplicates the opposite side's geometry and reverses it.

- Joins vertices that lie on the plane.

See also

- Mesh Symmetry continuously preserves symmetry during editing.

- The Mirror Modifier symmetrizes non-destructively.

- The Mirror operator flips the mesh without dividing or duplicating.

### Options

Direction
The axis and direction of effect, in local object space.
Example: -X to +X deletes geometry right of the origin (positive X) and replaces it with a mirrored copy of geometry on the left (negative X).

Threshold
Vertices within this distance snap to the symmetry plane.

| Description | Description |
| --- | --- |
| Mesh before Symmetrize. | Mesh after Symmetrize. |

[Related references](INDEX.md).

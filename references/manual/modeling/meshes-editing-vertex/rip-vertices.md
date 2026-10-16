# Rip Vertices

## Rip Vertices

### Rip Vertices

Reference

Mode:

Edit Mode

Menu:

Vertex → Rip Vertices

Shortcut:

V

Splits the mesh at two adjacent edges of each chosen vertex.
Vertices then move using the cursor to open a gap.
When positioned, hit LMB or Return to lock in place. Alternatively, press RMB or Esc to cancel (vertices stay separated).

With a single chosen vertex, the mouse position decides the cut direction.
With multiple chosen vertices, linked edge orientation decides direction.

Note

Rip Vertices doesn't support removing whole faces. Use Split Selection instead.

See also

Split Faces by Edges cuts only chosen edges, leaving adjacent unselected edges intact.

### Examples

Single vertex ripping:

| Mouse cursor to the right. | Ripping results in a vertical cut. |
| --- | --- |
| Mouse cursor below. | Ripping results in a horizontal cut. |

Ripping vertices along connected edges:

| Description | Description |
| --- | --- |
| Vertical edges selected. | Ripping cuts vertically regardless of mouse position. |

As a rare case, cutting in several directions works:

| Description | Description |
| --- | --- |
| Before ripping. | After ripping. |

Ripping separate "islands" fails and throws an error.

[Related references](INDEX.md).

# Line Set: Edge Marks, Face Marks, Collection

### Edge Marks

In Edit Mode, mark "Freestyle Edges" like Seams or Sharp edges. Marked edges render via Edge Mark selection.

Internally, edge marks store as the freestyle_edge attribute.

Marking procedure:

- Select the mesh and enter Edit Mode.
- Choose edges to mark.
- Press Ctrl-E and select Mark Freestyle Edge.

Edge marks help render lines on particular mesh edges.

Marking Freestyle Edges in Edit Mode; the edge marks are highlighted in green.

With Edge Marks enabled, previously-marked lines always render. Black contour lines and blue edge-mark lines display.

| Description | Description |
| --- | --- |
| Render without Edge Marks. | Render with Edge Marks enabled. |

Edge mark uses:

- Render marks on nearly-flat planes when other edge types find none.
- Full control of edge rendering. Common for angular shapes.
- Mark the full base mesh for base mesh preview.

Edge mark non-uses:

- Round outer edges (use Contour/External Contour/Silhouette instead).

### Face Marks

Face marks suppress lines in certain mesh areas.

Internally, face marks store as the freestyle_face attribute.

Marking procedure:

- Select a mesh and enter Edit Mode.
- Choose faces to mark.
- Press Ctrl-F and select Face Data ‣ Mark Freestyle Face.

This example marks two cube faces. Right image shows render without face marks.

| Description | Description |
| --- | --- |
| Marked faces (Edit Mode). | Render output. |

Line selection via inclusion and face options:

Negation
Include or exclude edges matching face mark conditions.

Condition

One Face:
(De)select edges whose one or both neighbors are marked.

Both Faces:
(De)select edges whose both neighbors are marked.

| Inclusive, One Face. | Inclusive, Both Faces. |
| --- | --- |
| Exclusive, One Face. | Exclusive, Both Faces. |

### Collection

Include/exclude objects for line calculation per Collection membership.

Line Set Collection
Object collection name.

Negation
Include or exclude lines from these objects in this line set.

[Related references](INDEX.md).

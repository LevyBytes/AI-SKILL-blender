# Grid Fill

## Grid Fill

### Grid Fill 

Reference

Mode :

Edit Mode

Menu :

Face ‣ Grid Fill

Produces a grid of quads. It accepts two kinds of input:

- A roughly rectangular loop of edges — or just two opposite sides of one — gets a grid filled
inside it.

- A roughly rectangular patch of faces gets a grid generated in its place.

| Description | Description |
| --- | --- |
| Input.  | Grid Fill result.  |

Results come out best when each pair of opposite sides carries the same vertex count, though
that's not mandatory.

### Options 

Span
How many columns the grid gets. (Row count follows from this on its own.)

Offset
Picks which vertex serves as the grid's first corner. It's the active vertex by default; use it to
spin the grid's layout around.

Simple Blending
Switches to a plainer interpolation for building the grid — a better choice on flat surfaces, or
anywhere preserving curvature looks wrong.

Tip

Blender may give an error such as "Loops are not connected by wire/boundary edges." The "loops" here
can be confusing as it is Blender terminology for "chains," not "closed loops." As such, this error
really means "The selected edge chains are not connected to each other; please create more edges
to form a closed loop."

See also

Bridge Edge Loops

[Related references](INDEX.md).

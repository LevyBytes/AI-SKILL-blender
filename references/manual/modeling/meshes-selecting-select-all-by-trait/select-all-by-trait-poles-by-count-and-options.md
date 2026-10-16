# Select All by Trait: Poles by Count, Options, Ungrouped Vertices

### Poles by Count

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select All by Trait ‣ Poles by Count

Hunts down poles, those vertices wired to an odd number of edges, and then selects the poles themselves (vertex mode) or the edges and faces around them (edge/face mode).

| Description | Description |
| --- | --- |
| Before selecting poles.  | After selecting poles.  |

### Options

Pole Count
The edge count a vertex must (or must not) hit to register as a pole.

Type
The comparison that decides what counts as a pole:

Less Than :

Vertices with fewer than Pole Count edges.

Equal To :

Vertices with exactly Pole Count edges.

Greater Than :

Vertices with more than Pole Count edges.

Not Equal To :

Vertices whose edge count differs from Pole Count .

Extend
Adds to what's selected rather than replacing it.

Exclude Non Manifold
Leaves out poles sitting in non-manifold geometry.

Hint

Since poles can cause ugly pinching under the Subdivision Surface Modifier, this operator is handy for hunting them down.

### Ungrouped Vertices

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select All by Trait ‣ Ungrouped Vertices

Selects all vertices that are not part of any vertex group.

[Related references](INDEX.md).

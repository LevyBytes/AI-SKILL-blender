# Vertex Weight Proximity Modifier: Options

## Vertex Weight Proximity Modifier

### Vertex Weight Proximity Modifier

What this modifier does is set a chosen vertex group's weights from how far the object (or its individual vertices) sits from a second target object (or that object's geometry).

Warning

Weight values get implicitly clamped by this modifier into the usual (0.0 to 1.0) span.
Anything under 0.0 snaps to 0.0, and anything over 1.0 snaps to 1.0.

Note

The reworked weights can be inspected in Weight Paint Mode.
By the same token, you'll need to switch off the Vertex Weight Proximity modifier
to see the vertex group's original weights as you edit them.

### Options

The Vertex Weight Proximity modifier panel.

Vertex Group
The vertex group that gets affected.

Target Object
The object that distances are measured from.

Proximity Mode

Object Distance
Take the gap between the modified mesh object and the target object as the
weight applied to every vertex in the affected vertex group.

Geometry Distance
Measures from each vertex to the target object, or to its geometry.

Vertex
Each vertex's weight comes from how far it lies from the target object's closest vertex.

Edge
Each vertex's weight comes from how far it lies from the target object's closest edge.

Face
Each vertex's weight comes from how far it lies from the target object's closest face.

Note

Turn on more than one and the shortest distance wins.
Where the target object carries no geometry (an empty or camera, say),
the object's own location is used instead.

Lowest
The distance that maps to a weight of 0.0.

Highest
The distance that maps to a weight of 1.0.

Tip

Push Lowest above Highest and the mapping runs the other way.

Normalize Weights
Rescales the vertex group's weights so their relative spacing holds
while the lowest and highest values stretch across the full 0 - 1 range.

[Related references](INDEX.md).

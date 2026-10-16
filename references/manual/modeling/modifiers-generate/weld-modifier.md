# Weld Modifier

## Weld Modifier

### Weld Modifier

Scan the mesh for clusters of vertices sitting within a set threshold of one another, fuse each cluster, and let the geometry wrapped around it collapse inward: that is what the Weld modifier does.

### Options

The Weld modifier.

Mode
Sets the rule for deciding which vertices get merged.

All :

The merge takes in every bit of geometry, loose parts included.

Connected :

The merge covers only attached geometry, so the modifier leaves loose parts un-joined.

Distance
The largest gap two vertices may sit apart and still be merged.

Only Loose Edges Connected Mode
Restricts collapsing to short edges that touch no face.
Handy, for instance, when stitching together the seams used in cloth simulations.

Vertex Group
With the Vertex Group option active, the modifier touches only those vertices carrying a weight greater than zero.

Invert
Flips which vertices the chosen vertex group covers, so the group instead
marks the vertices the modifier will leave un-merged.

The group's weight values are reversed by this setting.

[Related references](INDEX.md).

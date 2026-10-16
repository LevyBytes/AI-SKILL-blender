# Editing Weight Paint: Mirror, Invert

### Mirror

The Mirror Vertex Group operation duplicates weights
across a perfectly symmetrical mesh's opposite sides.
Vertices lacking a corresponding match remain unaffected.
Note: weights transfer to the matching opposite bone's group only with additional configuration.

Note

Mirroring requires perfect X-axis symmetry in the object's rest pose.

Mirror example.

Mirror Weights
When enabled, any selected vertex obtains
the weight profile from its symmetrical opposite.
If both vertices are selected, weights exchange;
if only one is selected, unselected vertex data replaces selected data.
Active group transfers receive weight information,
or all groups if All Groups is selected.

Flip Group Names
Works on selected vertices in groups with "symmetrical nomenclature"
(containing components like "L", "R", "right", "left").
Selected vertices in the active group or its symmetrical partner
get reassigned to the symmetrical counterpart;
the original weight value persists.
With All Groups active, all such reassignments
change to their symmetrical equivalents, preserving old weights.

All Groups
Apply to every vertex group instead of just the current one.

Topology Mirror
Mirror for asymmetric meshes (approximate mirror).
Refer to documentation for additional details.

Tip

Mirror to Opposite Bone

To generate a mirrored group for an opposing bone
(in a symmetric character), follow these:

- Delete the destination vertex group (target for mirrored data).

- Duplicate the source bone vertex group
(the one containing weights to copy).

- Rename this new group to the destination group name
(the one you removed above).

- Activate the destination group and invoke Mirror
(use Mirror Weights only and optionally Topology Mirror for asymmetric meshes).

### Invert

Changes each weight in a selected group by × -1.0.

Examples:

- 1.0 becomes 0.0
- 0.5 stays 0.5
- 0.0 becomes 1.0

Invert.

Subset
Limit operation to a subset.
See The Subset Option above for subset definitions.

Add Weights
Include vertices with zero weight prior to inverting (set to 1.0).

Remove Weights
Eliminate vertices from the group if they hit 0.0 post-inversion.

Note

Locked groups remain unchanged.

[Related references](INDEX.md).

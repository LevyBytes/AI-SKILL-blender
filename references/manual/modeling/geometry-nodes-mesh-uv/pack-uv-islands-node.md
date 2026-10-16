# Pack UV Islands Node

## Pack UV Islands Node

Pack UV Islands Node

Rearranges UV islands for efficient space use. Islands scale, translate, rotate with margins. Procedurally optimizes within Geometry Nodes—atlases, bake prep.

Tip: In contrast to the UV Editor operator, this node runs non-destructively and takes procedural inputs, which makes it a good fit for automated or parametric UV workflows.

Inputs
UV: The UV map to pack. Island topology is determined from this input.
Selection: Faces to include when packing. Only islands containing at least one selected face are affected. UVs on unselected faces stay unchanged.
Margin: Distance between islands in UV space units.
Rotate: Allow island rotation for more efficient packing.
Method: How each island's shape is evaluated.
  Bounding Box: Uses the axis-aligned bounding box. Fastest but less space-efficient.
  Convex Hull: Uses the convex hull. Balances accuracy and performance, won't place islands inside holes.
  Exact Shape: Uses the full island shape including concave regions and holes. Tightest packing but slowest.
Bottom Left: The bottom-left corner of the region for packing.
Top Right: The top-right corner of the region for packing.

Output
UV: Packed UVs with islands repositioned and scaled per node settings.

[Related references](INDEX.md).

# Baking

## Baking

Baking preserves intermediate geometries for later retrieval.

The internal data format is not an exchange format. OpenVDB is used for volumes (interchangeable across tools).

Two baking methods exist:

- Bake Node – any node-tree section.
- Simulation Zone Baking – animations where one geometry state feeds the next.

Disk writing happens only when Bake is executed.

Important:

- Save the blend file before baking.
- Data format between Blender versions is not guaranteed compatible.

The Bake Geometry node bakes all simulations and bake nodes in chosen objects' modifiers.

Tip: Once baked, frame count displays above zone or node.

Reference

Editor: Geometry Node Editor
Panel: Sidebar ‣ Node ‣ Data-Block References

List baked geometries that reference other data (materials, for example).

This panel lets you update those references post-baking.

Note: Currently only materials are supported.

[Related references](INDEX.md).

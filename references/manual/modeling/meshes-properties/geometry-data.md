# Geometry Data

## Geometry Data

### Geometry Data

This panel handles the assorted generic data attributes a mesh might carry.

Warning

Clear any of this data and those values are gone for good.

Clear Sculpt Mask Data
Removes the internal sculpt_mask attribute, which drives the Sculpt Masking Feature.

Add/Clear Skin Data
Manages the skin data the Skin Modifier relies on. You may need it when a Skin modifier exists but its skin data doesn't.

Reorder Mesh Spatially
Sorts vertex and face indices by spatial position, so elements near each other in the scene also sit near each other in memory.

The topology and visible geometry stay the same. What improves is performance wherever spatial coherence counts, such as:

- Quicker BVH (Bounding Volume Hierarchy) builds, helping both rendering and the viewport.

- Tighter memory access while sculpting dense, high-poly meshes.

- Possibly smoother handling of heavy geometry in edit and sculpt modes.

Warning

- Because vertex and face indices change, anything depending on stable indices can break, including shape keys, UV maps, or external scripts that reference vertex indices.

- Tread carefully on meshes already tied to rigs or shape keys.

Tip

It pays off most on static, high-resolution meshes for sculpting or rendering, where speed outweighs index stability.

For animated or deformed meshes, leaving the order alone is generally the safer call.

Add/Clear Custom Split Normals Data
Creates Custom Split Normals data when there isn't any.

[Related references](INDEX.md).

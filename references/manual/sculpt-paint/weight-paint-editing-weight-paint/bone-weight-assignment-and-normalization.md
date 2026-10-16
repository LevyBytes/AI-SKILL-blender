# Editing Weight Paint: Assign from Bone Envelopes, Assign Automatic from Bone, Normalize All, Normalize

## Editing Weight Paint

### Editing Weight Paint

Reference

Mode :
Edit Mode and Weight Paint Mode

Menu :
Weights

Weight Paint Tools.

Blender offers multiple utilities to facilitate weight painting operations.

The Subset Option

Many tools provide a Subset filter allowing you to narrow their scope to particular vertex groups
(available in the Adjust Last Operation panel after tool activation)
with these available choices:

- Active Group
- Selected Pose Bones
- Deform Pose Bones
- All Groups

All tools are compatible with Vertex Selection Masking and Face Selection Masking.
When active, tools only influence selected vertices or faces.

### Assign from Bone Envelopes

Transfer envelope weights from chosen bone(s) to the active vertex group.

### Assign Automatic from Bone

Use the same automated weighting approaches on the chosen bone(s) and their vertex group
as found in the Parent armature menu.

### Normalize All

Ensures each vertex's total weight across all groups sums to 1. All vertex groups are normalized
except locked ones, which retain unchanged values.

Lock Active
Maintain active group values while normalizing the remaining groups.

### Normalize

Works exclusively on the active vertex group. Vertex relative weights stay the same,
while the entire weight set is scaled such that the peak value reaches 1.0.

Normalize example.

[Related references](INDEX.md).

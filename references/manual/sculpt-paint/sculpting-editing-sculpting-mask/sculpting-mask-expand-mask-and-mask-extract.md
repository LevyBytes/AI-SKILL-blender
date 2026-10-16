# Mask: Expand Mask, Mask Extract, Mask Slice

### Expand Mask

Note

Further data on Mask Expand along connectivity at the Expand section.

### Mask Extract

Reference

Mode:
Sculpt Mode

Menu:
Mask ‣ Mask Extract

Duplicates a mesh based on protected zones.
Extracted geometry additionally undergoes standard refinement for neater outcomes.

Threshold
Baseline protected value for vertex consideration during extraction.

Add Boundary Loop
Generates edge loops on boundaries,
facilitating boundary smoothing and supplementary option use.

Smooth Iterations
Iterations applied to the extracted component.

Project to Sculpt
Aligns the extracted mesh with the starting sculpt component.

Extract as Solid
Implements a Solidify Modifier on the new component.

### Mask Slice

Reference

Mode:
Sculpt Mode

Menu:
Mask ‣ Mask Slice

Eliminates protected points from the mesh.

Threshold
Baseline protected value for vertex consideration during extraction.

Fill Holes
Fills interior gaps that may form post-Mask Slice.

Tip

Without masking, this works to fill all gaps.
Handy when using Trim Tools
options and the Voxel Remesher.

Slice to New Object
Constructs a fresh component from protected areas.

[Related references](INDEX.md).

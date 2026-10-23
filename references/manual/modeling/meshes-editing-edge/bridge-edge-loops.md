# Bridge Edge Loops

## Bridge Edge Loops

Removes the chosen faces and stitches fresh ones across two or more of the selected edge loops.

Note: In Blender, an edge loop is any chain of connected edges—need not be closed. See Select Edge Loops.

Connect Loops option:
- Open Loop: Last loop disconnects from first
- Closed Loop: Last connects back to first
- Loop Pairs: First connects to second, third to fourth, etc.

Merge: Instead of creating faces, merge all loops (or loop pairs if selected) into single loop

Merge Factor: 0 = merge into first loop; 1 = merge into last; intermediate = interpolation

Twist: Offsets target vertex choice for source vertices; makes tube twist along axis

Number of Cuts: Intermediate loop count between existing loop pairs

Interpolation: Intermediate loop calculation when Number of Cuts > 0:
- Linear: Straight-line loops
- Blend Path: Bézier spline loops (disregards neighboring surfaces)
- Blend Surface: Bézier loops along surface normals (surface-aware)

Smoothness: Blend Path/Surface smoothing (1 = full Bézier; 0 ≈ Linear)

Profile Factor: Profile Shape strength (-value shrinks tube middle; +value inflates)

Profile Shape: Tube segment thickness variation between source loops. See Proportional Editing page for option details.

Examples:

Bridging same-vertex-count loops: input → result

Bridging different-vertex-count loops: input → result

Hole connection in surfaces: input → result

Series loop connection in single operation: input → result

Blend Surface interpolation on textured surfaces: input → result

See also: Grid Fill

[Related references](INDEX.md).

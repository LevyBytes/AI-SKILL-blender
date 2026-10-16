# Weighted Normal Modifier

## Weighted Normal Modifier

### Weighted Normal Modifier

A mesh's custom normals are reworked by this modifier through any of several methods you can pick from. One thing it's good for, among others, is making certain faces read as extremely flat under shading. See Normals for the background on normals and custom normals.

### Options

Weighting Mode
The normals around a vertex are blended into a single custom (per face corner) normal,
each contributing by some weight. Weighting Mode sets how those weights are worked out.

Face Area
Weights by the area of the face a normal comes from.
The larger that face, the heavier its normal counts toward the result.

Corner Angle
Weights by the angle each face makes at the vertex.
This is what Blender falls back on by default when blending face normals into a vertex normal.

Face Area and Angle
The weights come from multiplying the face-area weights by the corner-angle ones.

Weight
Sets how hard the weighting leans on face areas and/or corner angles,
rather like turning up the contrast on a photo.

Set it to 50 and every face carries the same weight.
Go above 50 and faces with larger area or wider angles count for still more (more "contrast").
Drop below 50 and those same faces count for less (less "contrast").

Threshold
A rounding threshold for the weights: when two angles or areas differ by less than it,
they come out with the same weight.

Keep Sharp
Holds onto Sharp edges,
though smoothing still occurs where more than one face sits between any two Sharp edges.

Face Influence
Draws on face weights (weak, medium, or strong) handed out by
the Set Strength tool, or
by a Bevel modifier's Set Strength mode.

Say three faces meet at a vertex carrying the face weights weak, medium, and strong:
the final result then takes only the normal that belongs to the strong face.

Vertex Group
Name a vertex group and the modifier confines itself to those vertices.
The "arrow" button beside it flips the selection (acting only on the vertices outside the vertex group).

[Related references](INDEX.md).

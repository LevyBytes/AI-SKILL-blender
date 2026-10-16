# Bevel: Miter Outer O, (Miter) Inner I

Miter Outer O
When beveling three or more edges meeting at one vertex, and two form a corner over 180° on the face side, Outer Miter determines whether extra geometry prevents pinching.

| Description | Description | Description |
| --- | --- | --- |
| Sharp outer miter (no extra geometry). | Patch outer miter. | Arc outer miter. |

(Miter) Inner I
When beveling two or more edges meeting at one vertex and they form a corner under 180° on the face side, Inner Miter determines whether extra geometry prevents pinching.

| Description | Description |
| --- | --- |
| Sharp inner miter (no extra geometry). | Arc inner miter. |

Spread
The size of the Inner Miter when Arc. This also impacts the Outer Miter.

Intersection Type N
Geometry type at points where three or more beveled edges converge.

Grid Fill:

Fill the space with geometry that smoothly joins the edges.

Cutoff:

Cap each edge with a flat surface.

| Description | Description | Description |
| --- | --- | --- |
| Grid fill. | Cutoff. | Cutoff with a center face. |

Face Strength
Whether to set a Face Strength for beveled faces.
Pair with a Weight Normals Modifier (Face Influence checked).

None:

No face strength assignment.

New:

Set new edge faces to Medium and new vertex faces to Weak.

Affected:

Plus all Set for New, also set neighboring faces to Strong.

All:

Plus all Set for Affected, also set remaining mesh faces to Strong.

Profile Type Z
Controls the edge flow generated along each beveled edge.

Superellipse
Auto-profile based on Profile Shape setting.

Custom

The custom profile widget.

Use a custom profile from the Curve Widget in Adjust Last Operation panel. The curve shows a side view of a bevel between two 90° faces; shaded zones represent the mesh interior.

Presets
Support Loops and Steps build dynamically with the bevel Segments count. Changing segment count requires re-applying the preset.

Sample Straight Edges
Whether to sample at the middle of fully straight curve segments (lines with Vector handles between control points).
Off by default, as sampling at control points typically suffices.

Sample Even Lengths
By default, each profile segment (between control points) gets the same sample count. Enable to distribute samples evenly along the entire profile length.

[Related references](INDEX.md).

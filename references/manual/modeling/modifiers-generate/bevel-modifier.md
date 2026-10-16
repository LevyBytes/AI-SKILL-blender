# Bevel Modifier

## Bevel Modifier

The Bevel modifier bevels the edges of the mesh it's applied to, with some control over how and where the bevel is applied — a non-destructive alternative to the Bevel operation in Edit Mode.

Options:
Affect:
- Vertices: only the areas near vertices are beveled; the edges stay unchanged.
- Edges: bevel the edges, creating intersections at vertices.
(For example, three cubes at 0.1, 0.3, and 0.5 bevel widths with the Vertices option selected.)
Width Type — defines how Width is interpreted to determine the bevel amount.
- Offset: the distance from the new edge to the original.
- Width: the distance between the two new edges formed by the bevel (or the edges on either side of the bevel when there's more than one segment).
- Depth: the perpendicular distance from the new bevel face to the original edge.
- Percent: the percentage of the adjacent edge length that the new edges slide along.
- Absolute: the exact distance along edges adjacent to the beveled edge; it differs from Offset when the unbeveled edges attached to beveled edges meet at an angle other than a right angle.
Width — the size of the bevel effect (see Width Type above). (E.g. three cubes at 0.1, 0.3, and 0.5 bevel widths.)
Segments — the number of edge loops added along the bevel's face.
Limit Method — controls where the bevel is applied to the mesh.
- None: no limit; all edges are beveled.
- Angle: bevel only edges whose angle of adjacent face normals plus the defined Angle is less than 180 degrees — meant to bevel only an object's sharp edges without affecting its smooth surfaces.
- Weight: use an attribute to determine the bevel width; at bevel weight 0.0, no bevel is applied. Any attribute on the input mesh can be chosen — by default the bevel_weight_edge and bevel_weight_vert attributes adjusted in edit mode are used, and the modifier conveniently lists the original mesh's attributes in the dropdown, though attributes created by previous modifiers can also be used (attributes with non-matching domains or types are automatically interpolated to the correct type).
- Vertex Group: use weights from a vertex group to determine the bevel width; at vertex weight 0.0, no bevel is applied, and an edge is beveled only if both of its vertices are in the group.
Invert — invert the influence of the selected vertex group, so the group now represents vertices that will not be deformed by the modifier; the setting reverses the group's weight values.

Profile — Superellipse: creates a bevel with a uniform concave or convex curve.
Shape — the shape of the bevel, from concave to convex; it has no effect if Segments is less than 2.
Custom Profile — a widget for a user-defined profile with more complexity than the single Shape parameter; the modal tool can toggle the custom profile, but the profile's shape is only editable in the options panel after the operation is confirmed. The profile starts at the widget's bottom-right and ends at its top-left, as if between two edges meeting at a right angle; control points are created in the widget, then the path is sampled with the number of segments from the Bevel modifier.
Miter Shape — the shape of the miter patterns, from concave to convex; it has no effect if Segments is less than 2. (Note: the Miter Shape slider stays active when miters are enabled, because it still controls the shape of the miter profiles.)
Presets — the Support Loops and Steps presets build dynamically depending on the bevel's number of segments, so if the segments change the preset must be re-applied.
Sampling — samples are first added to each control point, then, if there are enough, divided evenly between the edges. The Sample Straight Edges option toggles whether samples are added to edges with sharp control points on either side; if there aren't enough samples to give each edge the same number, they go to the most curved edges, so use at least as many segments as there are control points.

Geometry:
Miter Inner/Outer — a miter is formed where two beveled edges meet at an angle: on the side where the angle is greater than 180 degrees it's an outer miter, and where it's less than 180 degrees it's an inner miter. Each can be set to one of these patterns:
- Sharp: edges meet at a sharp point, with no extra vertices introduced on the edges.
- Patch: edges meet at a sharp point, but two extra vertices are introduced near the point so the edges and faces are less pinched than in the Sharp case; this makes no sense for inner miters, so it behaves like Arc for them.
- Arc: two vertices are introduced near the meeting point, joined by a curved arc.
(The Spread slider controls how far the new vertices are from the meeting point, and the Profile curve widget controls the shape of the arc.)
Spread — the value used to spread extra vertices apart for non-sharp miters; available when Miter Inner is set to Arc.
Intersections — when more than two beveled edges meet at a vertex, a mesh is created to complete the intersection between the generated geometry; this option controls the method used to create that mesh.

Grid Fill (the default intersection method) continues the bevel profile through the intersection, or with a custom profile, creates a smooth grid within the boundary.

Cutoff creates a terminal face at each beveled edge entering the vertex, most useful for custom profiles when the intersection becomes too complex for a smooth grid. When inner corners of cutoff faces meet, no central face forms. The direction depends on the original vertex normal.

Clamp Overlap restricts beveled edge width to prevent overlapping with nearby geometry.

Loop Slide attempts to slide bevel along unbeveled edges when mixed with beveled edges; disabling this can produce more uniform bevel widths.

Harden Normals adjusts per-vertex face normals of bevel faces to match surrounding surfaces, maintaining flat appearance of original faces while bevel faces shade smoothly into them. This requires a custom split normals attribute (automatically created if missing).

Seam propagation maintains expected seam continuity when a seam edge crosses a non-seam edge and all are beveled.

Sharp mark handling applies the same principle to sharp edges.

Material Index selects the material slot for bevel faces; -1 uses the material from the nearest original face.

Face Strength modes: None applies no strength, New sets bevel edge faces to Medium and vertex faces to Weak, Affected also marks adjacent faces as Strong, All marks remaining faces as Strong and works with Weighted Normals modifier (Face Influence enabled).

[Related references](INDEX.md).

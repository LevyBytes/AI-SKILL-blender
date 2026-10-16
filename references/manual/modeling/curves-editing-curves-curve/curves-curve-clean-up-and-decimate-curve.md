# Curve: Clean Up, Decimate Curve

Clean Up:

Decimate Curve:

Reference

Mode :

Edit Mode

Menu :

Curve ‣ Clean Up ‣ Decimate Curve

Lower the point count while attempting to keep the original shape.
Works similarly to the mesh equivalent.

Ratio
Percentage of control points to remove.

Note

Only Bézier curves can be decimated.

Delete:

Reference

Mode :

Edit Mode

Menu :

Curve ‣ Delete

Shortcut :

X , Delete

Delete pop-up menu options:

Vertices
Remove chosen control points without breaking the curve
(adjacent points link directly).
Remember: NURBS order cannot exceed its point count,
so it might decrease when deleting points.
When one point remains, no visible curve exists.
With all points deleted, the curve itself is removed.

Segment
Remove the segment connecting chosen control points and disconnect them.

Dissolve Vertices:

Reference

Mode :

Edit Mode

Menu :

Curve ‣ Delete ‣ Dissolve Vertices

Shortcut :

Ctrl - X

Remove chosen control points, with remaining segments fitted by adjusting handles.

| Before deleting.  | Deleting vertices.  |
| --- | --- |
| Deleting segment.  | Dissolve vertices.  |

[Related references](INDEX.md).

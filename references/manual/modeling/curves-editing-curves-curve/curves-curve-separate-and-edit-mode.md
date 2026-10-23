# Curve: Separate, Edit Mode

Separate:

Reference

Mode :

Edit Mode

Menu :

Curve ‣ Separate

Shortcut :

P

Break curve objects made of multiple distinct curves into individual objects.

Note: single-curve objects become new Curve objects with no control points.

Toggle Cyclic:

Reference

Mode :

Edit Mode

Menu :

Curve ‣ Toggle Cyclic

Shortcut :

Alt - C

Switch between open and closed (Cyclic) curves.
Only curves with at least one chosen control point are affected.
Closing segments use start/end handles for Bézier and adjacent points for NURBS.
Auto handles update only if they are Auto type.

Open and Closed curves. 

This action applies only to the original first or the last added control point.
Deleting segments doesn't change this: only the starting and last points matter. This means
Alt - C may join two curves instead of closing one!
Remember: closing a 2D curve creates a renderable flat face.

Open and Closed curves.

[Related references](INDEX.md).

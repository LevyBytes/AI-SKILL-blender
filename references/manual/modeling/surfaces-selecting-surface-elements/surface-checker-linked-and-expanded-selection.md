# Selecting Surface Elements: Checker Deselect, Select More/Less, Select Linked

### Checker Deselect

Reference

Mode :

Edit Mode

Menu :

Select ‣ Checker Deselect

Working outward from the active point, this operator removes control points from the selection following a repeating pattern.
Say Deselected is 2 and Selected is 3: the operator
clears the first two points in a row, leaves the next three alone, clears
the following two, and keeps going. It runs this in both the "horizontal" and
"vertical" direction of the grid.

Deselected
How many control points each repetition of the pattern drops from the selection.

Selected
How many control points each repetition of the pattern leaves alone.

Offset
How far to shift away from the starting point.

### Select More/Less

Reference

Mode :

Edit Mode

Menu :

Select ‣ More/Less

Shortcut :

Ctrl - NumpadPlus / Ctrl - NumpadMinus

Grows or shrinks the selection starting from the control points already selected.

More
Pulls the neighbors of the selected control points into the selection.

Less
Drops any control point that has at least one neighbor left unselected.

### Select Linked

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select Linked

Shortcut :

Ctrl - L , L

Hit Ctrl - L to grab every control point "linked to" (sharing the same
surface as) one that's already selected.

Or press L to select the control point beneath the mouse cursor plus every
control point linked to it.

[Related references](INDEX.md).

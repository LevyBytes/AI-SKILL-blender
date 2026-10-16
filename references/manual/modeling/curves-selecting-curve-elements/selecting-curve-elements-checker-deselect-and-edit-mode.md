# Selecting Curve Elements: Checker Deselect, Edit Mode

Checker Deselect:

Reference

Mode :

Edit Mode

Menu :

Select ‣ Checker Deselect

Create an alternating selected/deselected checker pattern.
Works only with multiple already-selected points.

Modifies the selection so every Nth
point stays selected, starting from the active one.

Deselected
Deselected count in each pattern unit.

Selected
Selected count in each pattern unit.

Offset
Starting point offset.

Select More/Less:

Reference

Mode :

Edit Mode

Menu :

Select ‣ More/Less

Shortcut :

Ctrl - NumpadPlus , Ctrl - NumpadMinus

Based on current selection, shrink or expand it.

More
For each chosen point, activate its linked points (one or two).

Less
For each chosen point, if all linked points are active, keep it chosen.
Otherwise, deselect it.

Two consequences:

- When all points are chosen, nothing occurs
(all linked points are already active, and More can't add). Same for no selection.

- These tools stay within a curve
(they don't jump to another curve in the object).

Select Linked:

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select Linked

Shortcut :

Ctrl - L

Activate all points connected to the active one.

Makes it easier to select or deselect whole curve sections, especially in
dense curves, where manual point selection takes time.

[Related references](INDEX.md).

# Curve selection basics

## Selecting Curve Elements

This section covers curve-specific selection in Edit Mode.
The Curve Edit Mode also uses general select tools described
in the interface section.

Curve selection has fewer options than meshes.
Mainly because there's one selectable type: control points
(no select mode needed). These are more complex than simple vertices,
especially for Bézier curves, with central vertex and two handles.

Basic tools match meshes:
select a point with LMB ,
add with Shift - LMB , Box Select B , and so on.

For Bézier points: selecting the main vertex auto-selects both handles, moving the whole point
without creating angles. Selecting a handle alone changes just that vector.

Note: unlike mesh edges, segments can't be directly selected. Select all points making up the segment instead.

Select Menu:

All advanced selection options for curves
appear in the 3D Viewport header's Select menu.

All:

Reference

Mode :

Edit Mode

Menu :

Select ‣ All

Shortcut :

A

Activate all selectable elements.

None:

Reference

Mode :

Edit Mode

Menu :

Select ‣ None

Shortcut :

Alt - A

Deselect all, but the active element remains.

Invert:

Reference

Mode :

Edit Mode

Menu :

Select ‣ Invert

Shortcut :

Ctrl - I

Choose all unselected geometry and deselect current components.

[Related references](INDEX.md).

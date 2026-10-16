# Selecting Surface Elements: Select Similar, Select Control Point Row

### Select Similar

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select Similar

Shortcut :

Shift - G

Starting from a selected control point, this operator picks up other control points that resemble it in some way.
The Adjust Last Operation panel provides options for this:

Type
Which property gets compared when deciding what counts as similar.

Type :

Has no bearing on Surfaces, since — Curves aside — they offer only a single handle type.

Radius :

Grabs control points whose Radius value comes out similar.
See Transform Panel.

Weight :

Grabs control points whose Weight value comes out similar.
See Transform Panel.

Direction :

Grabs control points whose normal vector points a similar way.

Compare
Which test decides whether an unselected control point counts against the selected ones.

Equal :

Picks control points whose property matches that of a selected point.

Greater :

Picks control points whose property is at least as large as the smallest property
found among the selected points.

Less :

Picks control points whose property is no larger than the greatest property
found among the selected points.

Threshold
A leeway that widens the net to control points whose property merely lands near
that of a selected one. Suppose a Weight of 0.6 on the selected control point with
Threshold at 0.1: every control point whose Weight falls anywhere from 0.5 to 0.7
then gets caught by Select Similar.

### Select Control Point Row

Reference

Mode :

Edit Mode

Menu :

Select ‣ Control Point Row

Shortcut :

Shift - Ctrl - R

Grabs the control points sharing the active one's grid line (much like
edge loop selection on meshes).
Run the operator a second time to switch to the grid line going the other way.

[Related references](INDEX.md).

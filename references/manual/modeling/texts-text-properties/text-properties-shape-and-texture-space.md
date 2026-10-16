# Text Properties: Shape, Texture Space, Geometry, Extrusion, Taper & Bevel

## Text Properties

### Text Properties

### Shape

Reference

Mode :

All Modes

Panel :

Properties ‣ Data ‣ Shape

Most settings in the Shape panel come straight from the
Curves
data-blocks, so check there for the details.

Fill Solver
Which triangulation method handles the filling of 2D curves.

Sweep Line :

A quick triangulation approach meant for tidy, well-behaved outlines.
It can't cope with curves that cross themselves.

Delaunay :

Relies on Constrained Delaunay Triangulation (CDT).
Sturdier and able to handle self-intersecting curves, though it runs slower.

Important

Since most font files contain self-intersecting curves,
Delaunay is the recommended choice
whenever you work with text objects.

Fill Rule
Which rule the Delaunay Fill Solver applies to decide which regions count as inside.

Even-Odd :

Flips between inside and outside according to how many boundary crossings there are.
Overlapping regions can cancel one another out, depending on the crossing tally.

Non-Zero :

Settles inside versus outside from the winding direction.
Overlapping curves winding the same way merge into a union,
while curves winding the opposite way can punch out holes.

Fast Editing
Skips filling the letters in Edit Mode and shows only their outline.

### Texture Space

Every Object can carry an automatically generated UV map, which you tweak here.

See Generated UV Properties for more information.

### Geometry

Reference

Mode :

All Modes

Panel :

Properties ‣ Data ‣ Geometry

Offset
Shifts the control points of the curves that define the letters, thinning or thickening them.
Handle it carefully, since artifacts crop up fast…

### Extrusion, Taper & Bevel

The panel's remaining settings, the ones that add volume to the letters,
likewise come from the Curves data-blocks,
so check there for the details.

Note

Exactly how the Taper object effect plays out hinges on how the curves defining the letters are built.
The outcome can look pretty unpredictable…

Note

Bevel acts on the curves that define the letters,
so it generally traces their outlines
(yielding two parallel beveled curves rather than the single one you might expect).

[Related references](INDEX.md).

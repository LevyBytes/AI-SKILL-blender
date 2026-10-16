# Bisect

## Bisect

### Bisect 

Reference

Mode :

Edit Mode

Tool :

Toolbar ‣ Knife ‣ Bisect

Menu :

Mesh ‣ Bisect

Slices the selected geometry into two halves using an infinitely large plane.

### Usage 

Angle the view so the cutting plane reads as a line — the Top view, say, when splitting the mesh
left from right. Then turn on the tool and drag out the cut line with LMB . These shortcuts are
live while dragging (and listed in the status bar):

Move Spacebar
Repositions the line.

Snap Ctrl
Locks the line's rotation to 15-degree steps.

Flip F
Swaps which side of the plane counts as the "outer" one. Fill and Clear Inner/Outer rely on this
later.

### Options 

Drag the line and a yellow arrow marks the way toward the "outer" side; the Adjust Last Operation
panel then exposes these:

Plane Point, Plane Normal
Type exact figures here to pin the plane down precisely.

Fill
Adds faces along the cutting plane to seal any gaps left by Clear Inner/Outer , drawing
materials, UVs, and Color Attributes from the surrounding geometry.

Clear Inner/Outer
Wipes out any geometry on the "inner" or "outer" side of the plane — including geometry that
wasn't originally selected.

Axis Threshold
Vertices nearer the plane than this threshold are reused; everywhere else, fresh vertices and
edges get built.

### Examples 

| Description | Description |
| --- | --- |
| Example of a common use of bisect.  | Example of bisect with the Fill option enabled.  |

[Related references](INDEX.md).

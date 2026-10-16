# Control Points: Extrude Curve and Move, Example, Make Segment, Smooth

## Control Points

### Control Points

### Extrude Curve and Move

Reference

Mode :

Edit Mode

Menu :

Control Points ‣ Extrude Curve and Move

Shortcut :

E

Adding new control points to a surface is done primarily through extrusion — and unlike Curves, you can't simply add them directly.

The workflow: first select an entire border of the surface grid, then hit E to copy those control points and drag the mouse to position them where you want.
Wrap up by clicking LMB to lock them in. (Or back out with RMB or Esc, which cancels the move and leaves the new control points sitting where they started.)

### Example

To begin, pick one border control point and grow the selection to cover its whole row
with Select Control Point Row.

| Description | Description |
| --- | --- |
| Selecting control point | Selecting remaining control points in the row |

From there, run the extrusion a couple of times:

Control points extruded twice

### Make Segment

Reference

Mode :

Edit Mode

Menu :

Control Points ‣ Make Segment

Shortcut :

F

The name suggests a single grid line gets drawn between two control points, but the behavior is closer to Bridge Edge Loops for meshes: it spans the gap
between two separate surfaces, laying down however many new segments that takes. Just pick a border
row (or column) on each surface and press F to stitch those borders together.

Bear in mind that both surfaces have to belong to the same Surface object. Two standalone
objects must first be merged into one with Join.
On top of that, the two borders you're joining need an equal count of control points.

### Example

In the pictures below, two "surfaces" that are really just curves get bridged, though
joining full sheets works the same way.

| Description | Description |
| --- | --- |
| Before bridging. | After bridging. |

### Smooth

Reference

Mode :

Edit Mode

Menu :

Control Points ‣ Smooth

Nudges the chosen control points so the surface reads as smoother.

[Related references](INDEX.md).

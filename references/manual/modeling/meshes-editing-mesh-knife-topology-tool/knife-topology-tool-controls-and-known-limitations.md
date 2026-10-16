# Knife Topology Tool: Controls, Known Limitations, Duplicate Vertices

### Controls 

These keyboard shortcuts are shown in the
status bar while cutting.
They're available both when using the tool from the Toolbar and when pressing K .

Cut LMB
Click to drop a new cutting line, or drag to lay cutting lines as the cursor crosses edges.

Close Loop - Double-click LMB
Drops a cutting point at the cursor (as a single click would), then ties it back to the path's
first point, sealing the loop.

Stop RMB
Finishes the current cutting path and opens a new one. The cursor snaps to cuts you've already
made.

Confirm Spacebar or Return
Locks in the cut, converting the cutting paths into real edges.

Cancel Esc
Drops the cut entirely.

Undo Ctrl - Z
Undoes the last cutting line — or, if you'd been dragging, every cutting line from that drag.

Midpoint Snap Shift
Hold it down to pull the cursor onto the midpoint of each edge.

Ignore Snap Ctrl
Hold it down to momentarily switch off snapping to existing vertices, edges, and cutting lines.

Cut Through C
Cut through occluded faces too, not just the visible ones. This mirrors (and inverts) the Occlude
Geometry setting above.

Axis X , Y , or Z
Pins the current cutting line to a global axis. A second press uses the object's local axis; a
third lifts the constraint.

Measure S
Steps through the measurement readouts — distances, angles, or both at once.

X-Ray V
Switches the display of geometry-hidden cuts on or off.

Angle Constraint A
Pins cutting lines to multiples of the Snap Increment angle. Set that angle in the Tool Settings
beforehand (see above), or type it while cutting with Angle Constraint active.

Snapping starts in the Screen plane by default. A second A press snaps in planes on the geometry,
Relative to an automatically picked edge or cutting line; press R to choose a different reference
line.

A third A press switches the snapping off again.

### Known Limitations 

### Duplicate Vertices 

When a cut spawns duplicate vertices, an oversized clipping range is usually the culprit. Try
raising the Clip Start to dodge it. Also see Depth Troubleshooting for details.

[Related references](INDEX.md).

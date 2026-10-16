# Snapping

## Snapping

Reference — Mode: Object, Edit, and Pose Mode. Location: Header ‣ Snapping. Shortcut: Shift-Tab.

Snapping makes lining objects and mesh elements up with one another straightforward. Switch it on or off with the Snap Off / Snap On toggle in the 3D Viewport header, or engage it briefly by holding Ctrl.

See also Transform Modal Map for additional keyboard shortcuts.

Snap Base — Reference: Mode: Object, Edit, and Pose Mode; Header: Snapping ‣ Snap Base; Shortcut: Shift-Ctrl-Tab. This setting picks which point on your geometry actually meets the target.
Closest — snaps from whichever bounding-box corner (Object Mode) or vertex (Edit Mode) sits nearest the target.
Center — snaps from the current transformation center, i.e. the pivot point. Pairing this with the 3D Cursor lets you choose the snap point entirely by hand.
Median — snaps from the mean position of the selected objects' origins (Object Mode) or vertices (Edit Mode).
Active — snaps from the origin (Object Mode) or center (Edit Mode) of the active element.

Snap Target — Reference: Mode: Object, Edit, and Pose Mode; Header: Snapping ‣ Snap Target; Shortcut: Shift-Ctrl-Tab. This setting picks what the selection gets snapped onto.
Increment — snaps to a virtual grid that begins at the selection's starting location and matches the viewport grid's spacing, effectively shifting the selection in steps equal to one grid cell.
Grid — snaps to the grid drawn in the viewport.
Vertex — snaps to whichever vertex is nearest the mouse pointer.
Edge — snaps to whichever edge is nearest the mouse pointer.
Face — snaps onto the surface of the face beneath the pointer, which is handy for retopology.
Volume — snaps the selection to a depth centered within the object under the cursor. This helps when, say, you want an Armature bone centered inside a character's arm; the other modes would instead drop it on the arm's surface. (Despite the name, this is unrelated to Blender's Volume objects.)
Edge Center — snaps to the midpoint of the edge nearest the pointer.
Edge Perpendicular — snaps to the point on an edge where the line from the selection's start (marked by a white cross) to its new spot meets that edge at a right angle.
Face Center — snaps to the midpoint of the face under the pointer.
Tip: hold Shift-LMB to turn on several snapping modes together.

Snap Target for Individual Elements — Reference: Mode: Object, Edit, and Pose Mode; Header: Snapping ‣ Snap Target for Individual Elements; Shortcut: Shift-Ctrl-Tab.
Face Project — snaps each object (Object Mode) or vertex (Edit Mode) one at a time onto the face hit by projecting from the present viewing depth along the present viewing direction; useful, for instance, to wrap a flat sheet snugly over a curved form.
Face Nearest — snaps each object or vertex individually onto the face closest to its new location and, unlike Face Project, can snap to hidden geometry.
See also the Shrinkwrap constraint / modifier.

Target Selection: configures finer snapping behavior, with the available choices depending on both the mode (Object/Edit) and the chosen Snap Target.
Align Rotation to Target — turns the selection so its Z axis lines up with the target's normal.
Backface Culling — leaves back-facing geometry out of snapping.
Include Active (Edit Mode) — snaps to the active object's other mesh elements.
This is ignored while Proportional Editing is on.
Include Edited (Edit Mode) — snaps to other objects that are likewise in Edit Mode.
Include Non-Edited (Edit Mode) — snaps to other objects that are not in Edit Mode.
Exclude Non-Selectable — restricts snapping to objects that can be selected.
Absolute Increment Snap (Increment) — snaps to the viewport grid outright instead of advancing by grid-cell increments. This resembles a Snap Target of Grid, except Grid pulls the selection to the grid point nearest the cursor.
Snap Peel Object (Volume) — when the target object is made of several overlapping but disconnected mesh islands, Snap To Volume normally targets only the island beneath the cursor. Turning on Snap Peel Object treats the object as a single whole, looking just at its outer "peel" and ignoring inner or enclosed faces.
Snap to Same Target (Face Nearest) — snaps only to the object the selection was nearest before the transform began.
Face Nearest Steps (Face Nearest, Edit Mode) — divides the whole transform into several stages, snapping at each one, which can yield cleaner results in some situations.

Affect: chooses which transforms snapping applies to. Out of the box only movement snaps, but you can extend it to rotation and scaling as well.

Rotation Increment: the angle used for incremental snapping of the rotate operator. Its second figure, the Rotation Precision Increment, drives finer transforms and is engaged by default while Shift is held.

Snapping makes aligning UV elements to one another easy. Toggle it with the magnet icon in the UV Editor's header, or briefly by holding Ctrl. This page is about the Snap header button; the Snap menu is covered under UV Editing.

Snap Target — Reference: Header: Snapping ‣ Snap To; Shortcut: Shift-Ctrl-Tab.
Increment — snaps to grid points, using a virtual grid that begins at the selection's starting location and matches the editor's displayed grid resolution, so you can move the selection in steps of one grid cell.
Grid — snaps to grid points.
Vertex — snaps to whichever vertex is nearest the mouse pointer.

Additional Options:
Snap Base (Vertex) — see 3D Viewport Snapping for details.

Affect — chooses which transforms snapping applies to; out of the box only movement snaps, but you can extend it to rotation and scaling.

Rotation Increment — the angle used for incremental snapping of the rotate operator; its second figure, the Rotation Precision Increment, drives finer transforms and is on by default while Shift is held.

[Related references](INDEX.md).

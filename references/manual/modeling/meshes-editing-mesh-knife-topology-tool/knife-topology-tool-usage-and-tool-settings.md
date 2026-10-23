# Knife Topology Tool: Usage, Tool Settings

## Knife Topology Tool

### Knife Topology Tool 

Reference

Mode :

Edit Mode

Tool :

Toolbar ‣ Knife

Menu :

Mesh ‣ Knife Topology Tool

Shortcut :

K

The Knife tool lets you interactively slice through faces, subdividing them and trailing a chain
of new edges behind the cut.

### Usage 

To begin, grab the tool from the Toolbar or press K . A scalpel cursor signals it's live.

LMB wherever the cut should start - that can be anywhere: on a vertex, edge, or face, or even off
the mesh entirely.

Move toward your next point. A yellow line previews the edges to come and aqua dots mark the new
vertices. LMB confirms and starts the next segment.

When you're finished, press Spacebar or Return to commit the cuts. Esc cancels instead.

Hint

By using Multi-Object Editing, you can cut multiple objects
at the same time.

| Description | Description | Description |
| --- | --- | --- |
| Mesh before knife cut.  | Knife cut active.  | After applying knife cut.  |

### Tool Settings 

These appear only when you launch the tool from the Toolbar, not via K . Find them in the Tool tab
of both the Properties Editor and the Sidebar.

Occlude Geometry
Cut only what's visible on screen. Turn it off to cut clean through the mesh, faces on the back or
hidden behind others included.

Only Selected
Cut through selected geometry alone. Press Shift - K rather than K to start cutting with this
already on.

X-Ray
Keep the cutting path visible even where geometry sits in front of it.

Measurements
The measurements to show along the cutting path: distances, angles, or both.

Angle Snapping
Whether to constrain the cutting lines to multiples of the Snap Increment angle.

None :

No snapping.

Screen :

Snap in screen space (the viewing plane).

Relative :

Snap in a plane on the geometry, relative to an adjacent edge or cutting line.

| Description | Description |
| --- | --- |
| Relative snapping at 90°. Blender highlights the reference edge in red and shows the snapping direction in white.  | Doing a few more cuts and applying.  |

Snap Increment
The angle to use for Angle Snapping .

[Related references](INDEX.md).

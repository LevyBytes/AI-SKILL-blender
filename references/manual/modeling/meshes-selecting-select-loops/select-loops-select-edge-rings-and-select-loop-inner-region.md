# Select Loops: Select Edge Rings, Select Loop Inner-Region, Options, Examples, Select Boundary Loop

### Select Edge Rings

Reference

Mode :

Edit Mode (Edge select mode)

Menu :

Select ‣ Select Loops ‣ Edge Rings

Shortcut :

Ctrl - Alt - LMB or Shift - Ctrl - Alt - LMB

Ctrl - Alt - LMB on an edge also grabs the parallel edges in the face row perpendicular to it. Use Shift - Ctrl - Alt - LMB to add to the previous selection rather than replace it.

That set of edges is called an edge ring in Blender terms, since it usually closes into a ring around the mesh, though as shown below it needn't.

Selecting edge rings in Edge mode. The clicked edge is highlighted in green.

The shortcut works in Vertex mode too, but yields a face loop selection instead:

Selecting edge rings in Vertex mode.

Hint

To turn an edge ring selection into a face loop, either switch to Vertex mode or switch to Face mode while holding Ctrl (see Expand/Contract Selection).

### Select Loop Inner-Region

Reference

Mode :

Edit Mode (Edge select mode)

Menu :

Select ‣ Select Loops ‣ Select Loop Inner-Region

Selects every face sitting inside a selected, closed loop of edges. It can be run in Vertex and Face modes, but the results may surprise you.

Note that if the selected edges do not form a closed loop, all connected faces will be selected.

### Options

Select Bigger
Select the faces outside the edge loop instead of those inside it.

### Examples

Single edge loop to region.

Multiple edge loops.

Holes are also supported.

### Select Boundary Loop

Reference

Mode :

Edit Mode

Menu :

Select ‣ Select Loops ‣ Select Boundary Loop

Swaps the current face selection for an edge selection tracing the border of each face "island." It's basically the inverse of Select Loop Inner-Region.

You can run it in any selection mode. Run in Face mode, it switches to Edge mode by itself.

Before and after running Select Boundary Loop.

[Related references](INDEX.md).

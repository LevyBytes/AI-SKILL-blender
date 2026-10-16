# Repeat Zone

## Repeat Zone

Runs a set of nodes repeatedly over iterations.

The zone spans from an input node (left) to an output node (right), with an orange area in between.
On first execution, inputs are evaluated and sent into the inner nodes.
These nodes write to the output node for the next iteration's inputs and the final result.

Inner nodes can read inputs from outside the zone (same value every iteration);
they cannot send outputs outside.

**Inputs**

Iterations
How many times to execute. The Iteration socket provides the current index (starting at 0).

Geometry
Default geometry input. Extra inputs are added by connecting external outputs to the zone's blank socket,
or via the Repeat Items list in Properties.

Labels are editable via Ctrl-LMB in the zone or Repeat Items panel (double-click to rename).

**Properties**

Reference: Sidebar ‣ Node ‣ Properties

Repeat Items
List view for creating, deleting, reordering, and relabeling inputs.

Socket Type
Data type of the selected input.

Inspection Index
Which iteration to display in socket inspection and the Viewer Node.

**Example**

Builds a pyramid with adjustable levels. Each iteration creates a cube, positions it,
and merges it with the prior iteration's result.

### Repeat Zone

A Repeat Zone runs a set of nodes over and over.

Picture the zone as three parts: an input node off to one side, an output node off the other, and an orange band between for the nodes you want repeated. The first time through, it reads its inputs and passes them along to the inner nodes. Those inner nodes write back to the output node — feeding the round that follows, and, after the last round, delivering the zone's final result.

Nodes inside the zone may also draw inputs from nodes outside it — those stay the same every iteration. They cannot, though, send their outputs back out to nodes beyond the zone.

### Inputs

Iterations
How many times to run the zone. The Iteration socket reports the current iteration's index, counting from 0.

Geometry
The default geometry input. To add others, run a node's output into the zone's spare input, or use the Repeat Items list found on the node's Properties panel.

Relabel inputs by Ctrl - LMB on them, whether on the zone directly or over in the Repeat Items list — and that list responds to a double-click as well.

### Properties

Reference

Menu :

Sidebar ‣ Node ‣ Properties

Repeat Items
List View for adding, removing, reordering, and renaming the zone's inputs.

Socket Type
The data type of the selected input.

Inspection Index
The iteration surfaced during socket inspection and inside the Viewer Node.

### Cycles and EEVEE Differences

In Cycles the iteration count has to resolve to a constant, which means it cannot be driven by Input Nodes or Texture Nodes.

Error shown when Cycles is selected as the active Render Engine .

EEVEE carries no such limit, so any kind of node can drive the iteration count.

[Related references](INDEX.md).

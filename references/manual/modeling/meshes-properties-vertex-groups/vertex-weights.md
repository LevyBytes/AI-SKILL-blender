# Vertex Weights

## Vertex Weights

### Vertex Weights

Reference

Mode :

Edit and Weight Paint Modes

Panel :

Sidebar region ‣ Vertex Weights

Vertex Weights panel.

For every vertex it holds, a vertex group records a weight between 0 and 1. A group can span many vertices, and any vertex may appear in many groups.

Sitting in the 3D Viewport's Sidebar, the Vertex Weights panel lists the groups the active vertex belongs to and lets you view and change those weights. It's there in Edit Mode, and in Weight Paint Mode whenever the header has Vertex Selection turned on.

### Vertex Group Categories

Every vertex group is the same thing under the hood, yet by how they're used we can split them in two:

Deform Groups
Sometimes called a "weight group" or "weight map," this kind ties certain vertices to a given bone in the Armature, deciding which stretch of mesh moves as that bone does.

Other Groups
Everything else, put to work with shape keys, modifiers, and so on.

The deform groups are linked: a vertex's deform weights usually have to total 1. That's why the filter buttons atop the panel can narrow the view to just these groups, or hide them.

### Weight Table

The Weight Table lists all weights on the active vertex , the one selected most recently (and shown in white). With no active vertex, or one outside every group, the panel doesn't appear.

### Set the Active Group

Click a vertex group's name to make it active.

Changing the active vertex group.

### Display Weights in Edit Mode

Enable display of weights in Edit Mode.

While in Edit Mode you can paint the active group's weights onto the mesh: pop open the Mesh Edit Mode Overlays popover and tick Vertex Group Weights .

Weights in Edit Mode.

### Change a Weight

To edit a group's weight, click the number and type a fresh value, or drag left and right with LMB . The arrows that surface on hover nudge it by 0.01 at a time.

Changing a weight value.

### Copy a Weight

Paste Weight to Selected pushes the active vertex's weight onto the other selected vertices. Despite the "paste" label, it has nothing to do with the Copy button and never touches the clipboard.

Copying a weight.

### Delete a Weight

Delete Weight drops the active vertex from the group, and its row vanishes from the list.

Deleting a weight.

### Operators

Vertex weight operators.

Normalize
Rescales the active vertex's weights to sum to 1.0 while keeping them in the same proportion to one another.

Copy
Pushes every weight on the active vertex onto the rest of the selected vertices.

Tip

Either tool acts only on the vertex groups passing the current filter.

### Locking

Locked vertex group.

Lock a vertex group and its weights freeze, with the copy and normalize buttons going dim.

Tip

Normalize and Copy gray out only when the current list holds a locked group. So if, say, just the non-deforming groups are locked, flip to the Deform filter and normalize from there.

[Related references](INDEX.md).

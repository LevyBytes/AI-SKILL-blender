# Assigning a Vertex Group: Creating Vertex Groups, Vertex Groups Panel Controls, Deleting Vertex Groups, Locking Vertex Groups, Working with Content of Vertex Groups, Assigning Vertices to a Group, Checking Assignments

## Assigning a Vertex Group

### Assigning a Vertex Group

### Creating Vertex Groups

Empty Vertex Groups panel.

The Object Data tab (1) in the Properties is where vertex groups live. New mesh objects start with none, so the panel sits empty (2).

To make one, LMB the button at the right edge of the panel (3). It comes in named "Group" (or "Group.nnn" if that name is taken) and shows up in the panel (2) (see next image).

### Vertex Groups Panel Controls

One vertex group.

A freshly added group appears in the Vertex Groups panel, where three clickable parts await:

Group Name
Double-click LMB on the name to rename the group, then type whatever you want.

Filter (arrow icon)
Clicking the small arrow at the lower left opens a row for a search term, which earns its keep once you've amassed a lot of vertex groups.

Drag Handle
With many groups and a wish to see more at once, LMB the little drag handle to grow or shrink the list.

Active Group
Creating a group also makes it the Active Group , flagged by a light-gray background on its panel entry. With two or more in the list, LMB another entry to switch which is active.

### Deleting Vertex Groups

Delete a vertex group.

Make the group active (pick it in the panel), then LMB the button at the panel's right edge to delete it.

Removing a group only drops the vertex assignments; the vertices stay put.

### Locking Vertex Groups

Lock a vertex group.

A new group shows an open padlock at the right of its entry, signaling that it's editable. You're free to add or pull assignments and paint it with the weight brushes, and so on.

Click the icon and it closes, freezing every change to the group. From there you can only rename, delete, or unlock it. Nothing else is permitted, so the matching buttons gray out for locked groups.

### Working with Content of Vertex Groups

### Assigning Vertices to a Group

Assign weights to active group.

To add vertices to a group:

- In the group list, click the group so it becomes active (1).

- Back in the 3D Viewport, Shift - LMB each vertex you mean to add.

- Dial in the weight that every chosen vertex should take (2).

- LMB Assign to bind the selection into the active group at that weight (3).

Locked groups don't allow this; the Assign button grays out when one is locked.

Note

Assign is additive

Pressing Assign only adds the current selection to the active group. Vertices already in the group stay, and a single vertex can belong to several groups at once.

### Checking Assignments

To confirm your selected vertices really sit in the group you mean, try the deselect button. Any vertices that stay selected aren't in the group yet.

You can assign them now, but be careful: every selected vertex takes on whatever weight is in the Weight field.

[Related references](INDEX.md).

# Editing

## Editing

These preferences control how various tools respond to your input.

Objects — New Objects:
Link Materials To — to grasp this option, it helps to know how Blender treats Objects. Nearly everything in Blender lives in a hierarchy of data-blocks, each one acting as a container for a particular kind of information: the Object data-block carries the Object's location, rotation, and scale, while the linked Object Data data-block carries the mesh. A material can be linked two ways — Object Data (a new material becomes part of the Object Data's data-block) or Object (a new material becomes part of the Object's data-block). See also Blender's Data System.
Align to — World (new objects line up with world coordinates), View (new objects line up with view coordinates), 3D Cursor (new objects take the 3D cursor's orientation).
Enter Edit Mode — when on, Edit Mode switches on automatically as you create a new object.
Instance Empty Size — the display size of empties when a new collection instance is made.

Copy on Duplicate — these checkboxes set which data a duplicated object copies and which stays linked. A checked box copies that data with the duplicate; an unchecked box leaves it linked to the source object. Check Mesh, for instance, and the new object gets a full copy of the mesh data, each behaving on its own; leave it unchecked and editing one object's mesh shows up in the duplicate too. The same logic covers every checkbox in the data-block list.

3D Cursor:
Cursor – Surface Project — when you place the cursor by clicking, it lands projected onto the surface beneath it.
Cursor – Lock Adjust — while the viewport is locked to the cursor, moving the cursor keeps the view from jumping because of the new offset.

Annotations:
Default Color — the starting color for new Annotate layers.
Eraser Radius — the eraser's size with the Annotate Tool.
See also Annotations.

Weight Paint — mesh skin weighting governs how much a bone deforms a character's mesh. To show and paint these weights Blender uses a color ramp (blue to green, yellow to red); ticking the checkbox switches to an alternate map whose ramp starts from an empty range, letting you build a custom map with the usual color-ramp options. See the Color ramps page for detail.

Grease Pencil:
Manhattan — the fewest pixels the mouse must move horizontally or vertically before the motion is recorded; lowering it helps with curvy lines.
Euclidean — the shortest distance the mouse must travel before motion is recorded.
See also Grease Pencil.

Text Editor:
Auto Close Character Pairs — automatically adds the matching closing character when you type quotes, brackets, braces, or parentheses.

Node Editor:
Auto-Offset — automatically nudges the following or previous nodes in a chain when you insert a new node (see Auto-Offset).
Auto-offset Margin — the margin used when offsetting nodes.

Miscellaneous:
Sculpt Overlay Color — sets a color for the inner part of the brush circle in Sculpt Mode, laid over the brush to mark the focal point of its influence. The overlay color shows only when overlay visibility is on (click the eye to set it), and its transparency comes from the alpha slider in the Sidebar's Tool tab ‣ Display panel.

[Related references](INDEX.md).

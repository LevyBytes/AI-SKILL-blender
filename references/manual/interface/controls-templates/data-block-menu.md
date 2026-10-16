# Data-Block Menu

## Data-Block Menu

### Data-Block Menu

Picking a Data-Block (a material, for instance) so it can be linked onto something else (an object, say) is what this menu is for.

A data-block menu with a search field.

Type
An icon here flags the data-block type. The popup menu opens when you click the image or the down arrow. Drag the image instead and you can apply the data-block elsewhere. (Dropping a material onto an object in the 3D Viewport assigns it, for example. Dropping onto Data ID fields works too.)

List
Available data-blocks in the current blend-file, or a way to link an item from somewhere else. Alongside the items the menu can carry a preview, plus a search field for finding items by name.

Note

Names that start with . keep their data-blocks out of the list, unless the search field is given a string that also begins with ., or the Show Hidden Files/Data-Blocks user preference is on.

Name
Shows, and lets you edit, the name of the selected data-block.

User Count
How many users the data has (when there's more than one) appears here. Click it to make a single-user copy.

Say three separate objects all pointed at one material — its user count would read 3, and editing the material would hit all three. Select one of those objects, click the user count, and that object gets its own private copy of the material, free to change without disturbing the original still shared by the other two.

Fake User (shield icon)
Normally a data-block with no real users gets cleaned up (deleted) when the blend-file is saved. Assigning it a fake user heads that off, guaranteeing it "survives." In the drop-down list, an "F" prefix marks data-blocks carrying a fake user.

For a rundown of every data-block in the blend-file that lacks real users, switch the Outliner's Display Mode to Orphan Data.

New/Add (files icon)
Makes a fresh data-block (or copies the current one) and selects it.

Open File (folder icon)
Brings up the File Browser — to import an image, for instance.

Unpack File (bin icon)
Writes the file packed inside the current blend-file back out to an external one.

(Unlink Data-block)
Drops the link. Use Shift - LMB to zero the user count so the data can be wiped from the blend-file entirely.

At times a list of applied data-blocks appears (the materials used on an object, say).

See also

The Data System chapter goes deeper into data-blocks.

### Preview
A Data-Block menu with preview.

Rather than plain icons and names, some data-block menus carry large preview images in their drop-down.

### Data ID
A Data ID field.

Much like a Data Block Menu, a Data ID field exists purely for selection — creating new data or managing users isn't part of it.

These elements may appear:

Type
On the left, an icon names which data-block type is accepted.

Name
This text field doubles as a search box, matching against the list. Tab auto-completes a name as far as one unique match allows; with several matches you carry on typing; an invalid entry leaves the value where it was.

List
Picks the data-block straight away.

Eyedropper
Certain Data IDs offer an Eyedropper, reached via the pipette icon over on the right.

(Clear Button String)
The button on the right clears the reference when clicked.

### ID Sub-Data
Depending on the data-block type and how it's meant to be used, related kinds of ID sub-data may open up for selection.

Sub-data Example.

Vertex Group
Should the Target field hold a mesh or lattice Object, an extra field can appear for picking one of its vertex groups.

Bone
Should the Target field hold an armature Object, an extra field can appear for picking one of its bones.

Head/Tail
Once a bone is chosen, a numeric field may turn up to name a spot along it. A value of 0.0 marks the head and 1.0 the tail, with everything between interpolated linearly (0.5 landing dead center).

Use B-Bone Shape
On a bendy bone, this button bends the point along the B-spline arc running head to tail instead of letting it track a plain straight line.

[Related references](INDEX.md).

# Assignment: Reusing Existing Materials, Deleting a Material, Multiple Materials

### Reusing Existing Materials

Blender is built to allow you to reuse anything , including material settings, between many objects. Instead of creating duplicate materials, you can simply reuse an existing material. There are several ways to do this using the Material's data-block menu:

Single Object – With the object selected, click the sphere located to the left of the Material name. A pop-up appears showing all the materials available in the current blend-file. To use one, just click on it.

Tip

Searching for Materials

The search field at the bottom of the material list allows you to search the names in the list. For example, by entering "wood" all existent materials are filtered so that only materials containing "wood" are displayed in the list.

Multiple Objects – In the 3D Viewport, with Ctrl - L you can quickly link all selected objects to the material (and other aspects) of the active object. Very useful if you need to set a large number of objects to the same material; just select all of them, then the object that has the desired material, and Ctrl - L links them to that "parent".

### Deleting a Material

To delete a material, select the material and click X in the Available Materials List entry.

Although the material will seem to disappear immediately, the Delete action can depend on how the material is used elsewhere.

If the material is linked to the object and there are other objects which use this material, then the material will be removed from that object (but remain on all its other objects).

If the "Fake User" button has been lit in the Available Materials list, then the material will be retained when the file is saved, even if it has no users.

Only if it has 0 "real" users, and no "Fake" user, will the material be permanently deleted. Note that it will still remain in the Materials list until the blend-file is saved, but will have disappeared when the file is reloaded.

### Multiple Materials

Normally, different colors or patterns on an object are achieved by adding textures to your materials. However, in some applications you can obtain multiple colors on an object by assigning different materials to the individual faces of the object.

To apply several materials to different faces of the same object, you use the Material Slots options in the Materials header panel.

The workflow for applying a second material to some faces of an object covered by a base material is as follows:

- In Object Mode, create a base material.

- Go into Edit Mode and Face Select (a new list will appear below the Active Material list with Assign , Select , Deselect buttons).

- Select the faces to be colored with the second material.

- In the Object Material Slots list, create a new slot or select an existing material.

- Click the Assign button, and the material will appear on the selected object faces.

[Related references](INDEX.md).

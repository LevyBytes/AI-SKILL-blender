# Assignment: Material Slots, Slot List, Data-Block, Edit Mode

## Assignment

### Assignment

Reference

Panel :

Material ‣ Material Slots

Materials are data-blocks that can be created and then assigned to one or more objects. An object can also have multiple materials assigned in different material slots, which correspond to different parts of an object. If a smooth transition between materials is desired, then mixing shader nodes with a Mix shader is a better solution.

### Material Slots

Material slots link materials to objects and meshes. By default objects only have a single material slot, which assigns a material to the entire object. If different parts of the mesh need different materials, multiple material slots can be created.

Material slots panel.

### Slot List

The object's material slots and active material displayed in a List View.

(Add Material Slot)
Add a new material slot on the object.

(Remove Material Slot)
Remove a material slot from the object.

(Material Specials)

Copy Material
Copy material shader nodes and settings to clipboard.

Paste Material
Paste material shader nodes and settings from clipboard.

Copy Material to Selected
Copy the same material assignment from the active to other selected objects.

Remove Unused Slots
Removes all material slots not assigned to the object.

Remove All Materials
Clears all material slots from the active object. The material data-blocks remain available in the blend file but are no longer assigned.

### Data-Block

Material
The Material Data-Block Menu for the selected material slot. Here new materials can be created, or existing materials linked to the material slot.

Link
Specifies whether the material is to be linked to the object or to the object data.

The Link selector has two choices, Data and Object. These two menu choices determine whether the material is linked to the object or to the data (e.g. a mesh or curve). The Data menu item determines that this material will be linked to the mesh's data-block which is linked to the object's data-block. The Object menu item determines that the material will be linked to the object's data-block directly.

This has consequences of course. For example, different objects may share the same mesh data-block. Since this data-block defines the shape of the object any change in Edit Mode will be reflected on all of those objects. Moreover, anything linked to that mesh data-block will be shared by every object that shares that mesh. So, if the material is linked to the mesh, every object will share it.

On the other hand, if the material is linked directly to the object data-block, the objects can have different materials and still share the same mesh.

Short explanation: If connected to the object, you can have several instances of the same Object Data using different materials. If linked to mesh data, you cannot. See Data System for more information.

### Edit Mode

To assign materials to different parts of a mesh, enter Edit Mode on the mesh. Additional buttons will then appear in the material slots panel.

Material slots panel in Edit Mode.

Assign
Assign active material slot and material to the selected faces in the mesh, strokes in a Grease Pencil, and similar for other object types.

Select
Select faces assigned to the active material slot.

Deselect
Deselect faces assigned to the active material slot.

[Related references](INDEX.md).

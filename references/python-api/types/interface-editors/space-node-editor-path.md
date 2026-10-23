# bpy.types.SpaceNodeEditorPath

to_string

(default “”, readonly, never None)

Type :

str
clear ( )

Empty the node tree path
start ( node_tree )

Define the root node tree

Parameters :

node_tree (NodeTree) – Node Tree
append ( node_tree , * , node = None )

Add a node group tree onto the path

Parameters :

- node_tree (NodeTree) – Node Tree, the node tree to tack onto the end of the node editor path

- node (Node) – Node, Group node linking to this node tree (optional)
pop ( )

Drop the last node tree off the path
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – Identifier for the RNA type.

- default (bpy.types.Struct | None) – Value returned if nothing matches.

Returns :

The matching RNA type, or the default if none is found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – Identifier for the RNA type.

- default ( type | None ) – Value returned if nothing matches.

Returns :

The matching class, or the default if none is found.

Return type :

type
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data | |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Description | Description |
| --- | --- |
| SpaceNodeEditor.path | |
## SpaceNodeEditorPath(bpy_prop_collection)

### SpaceNodeEditorPath(bpy_prop_collection)

base classes: bpy_prop, bpy_prop_collection
class bpy.types. SpaceNodeEditorPath ( bpy_prop_collection )

Retrieve the node tree path as a string

[Related references](INDEX.md).

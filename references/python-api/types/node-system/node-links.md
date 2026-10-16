# bpy.types.NodeLinks

new ( input , output , * , verify_limits = True , handle_dynamic_sockets = False )

Create a link inside this node tree.

Parameters :

- input (NodeSocket) – The input socket (never None)

- output (NodeSocket) – The output socket (never None)

- verify_limits ( bool ) – Verify Limits, Remove existing links if connection limit is exceeded (optional)

- handle_dynamic_sockets ( bool ) – Handle Dynamic Sockets, Handle node specific features like virtual sockets (optional)

Returns :

New node link

Return type :

NodeLink
remove ( link )

Delete a link from the node tree.

Parameters :

link (NodeLink) – The node link to remove (never None)
clear ( )

Delete every link in the node tree.
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

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
| NodeTree.links | |
## NodeLinks(bpy_prop_collection)

### NodeLinks(bpy_prop_collection)

base classes — bpy_prop, bpy_prop_collection
class bpy.types. NodeLinks ( bpy_prop_collection )

A set holding the node links.

[Related references](INDEX.md).

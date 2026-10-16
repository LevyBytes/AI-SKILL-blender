# bpy.types.NodeTreeInterfacePanel

default_closed 

On new nodes the panel starts out collapsed (default False)

Type :

bool
description 

Panel description (default “”, never None)

Type :

str
interface_items 

Every entry held in the node panel (default None, readonly)

Type :

bpy_prop_collection[NodeTreeInterfaceItem]
name 

Panel name (default “”, never None)

Type :

str
persistent_uid 

An identifier that uniquely tags this panel inside its node tree (in [-inf, inf], default 0, readonly)

Type :

int
select 

Whether the panel is selected in the interface (default False)

Type :

bool
classmethod bl_rna_get_subclass ( id , default = None , / ) 

Parameters :

- id ( str ) – Identifier naming the RNA type.

- default (bpy.types.Struct | None) – Fallback returned if no match is found.

Returns :

Either the matching RNA type or the supplied fallback when nothing matches.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / ) 

Parameters :

- id ( str ) – Identifier naming the RNA type.

- default ( type | None ) – Fallback returned if no match is found.

Returns :

Either the matching class or the supplied fallback when nothing matches.

Return type :

type
### Inherited Properties 

| Members | Members |
| --- | --- |
| bpy_struct.id_data NodeTreeInterfaceItem.item_type NodeTreeInterfaceItem.parent | NodeTreeInterfaceItem.position NodeTreeInterfaceItem.index |
### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values NodeTreeInterfaceItem.bl_rna_get_subclass NodeTreeInterfaceItem.bl_rna_get_subclass_py |
### References 

| Description | Description |
| --- | --- |
| NodeTreeInterface.move_to_parent NodeTreeInterface.new_panel | NodeTreeInterface.new_socket NodeTreeInterfaceItem.parent |
## NodeTreeInterfacePanel(NodeTreeInterfaceItem)

### NodeTreeInterfacePanel(NodeTreeInterfaceItem) 

base classes — bpy_struct, NodeTreeInterfaceItem
class bpy.types. NodeTreeInterfacePanel ( NodeTreeInterfaceItem ) 

A panel declared inside a node interface.

[Related references](INDEX.md).

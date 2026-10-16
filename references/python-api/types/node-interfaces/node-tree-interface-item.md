# bpy.types.NodeTreeInterfaceItem

index 

The item's overall position across every entry in the interface (in [-1, inf], default 0, readonly)

Type :

int
item_type 

Kind of interface entry this is (default 'PANEL' , readonly)

Type :

Literal[Node Tree Interface Item Type Items]
parent 

The panel this item sits inside (readonly)

Type :

NodeTreeInterfacePanel
position 

Where the item falls within its parent panel (in [-1, inf], default 0, readonly)

Type :

int
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
| bpy_struct.id_data | |
### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References 

| Description | Description |
| --- | --- |
| NodeTreeInterface.active NodeTreeInterface.copy NodeTreeInterface.copy NodeTreeInterface.items_tree | NodeTreeInterface.move NodeTreeInterface.move_to_parent NodeTreeInterface.remove NodeTreeInterfacePanel.interface_items |
## NodeTreeInterfaceItem(bpy_struct)

### NodeTreeInterfaceItem(bpy_struct) 

base class — bpy_struct

subclasses —
NodeTreeInterfacePanel, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceItem ( bpy_struct ) 

A single entry within a node tree interface.

[Related references](INDEX.md).

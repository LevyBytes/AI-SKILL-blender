# bpy.types.KeyMapItem: methods

## KeyMapItem(bpy_struct)

### KeyMapItem(bpy_struct) 

base class: bpy_struct
class bpy.types. KeyMapItem ( bpy_struct ) 

A single entry within a Key Map
compare ( item ) 

compare

Parameters :

item (KeyMapItem) – Item

Returns :

Comparison result

Return type :

bool
to_string ( * , compact = False ) 

to_string

Parameters :

compact ( bool ) – Compact, (optional)

Returns :

result, (never None)

Return type :

str
classmethod bl_rna_get_subclass ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The matching RNA type, or the supplied default if there is none.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default (type | None ) – The value to return when not found.

Returns :

The matching class, or the supplied default if there is none.

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
| KeyConfigurations.find_item_from_operator KeyMap.keymap_items KeyMap.restore_item_to_default KeyMapItem.compare KeyMapItems.find_from_operator KeyMapItems.find_match KeyMapItems.find_match KeyMapItems.from_id | KeyMapItems.match_event KeyMapItems.new KeyMapItems.new_from_item KeyMapItems.new_from_item KeyMapItems.new_modal KeyMapItems.remove UILayout.template_event_from_keymap_item UILayout.template_keymap_item_properties |

[Related references](INDEX.md).

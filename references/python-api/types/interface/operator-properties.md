# bpy.types.OperatorProperties

bl_system_properties_get ( * , do_create = False ) 

DEBUG ONLY. Internal hook into the runtime-defined RNA data storage, meant purely for testing and debugging. Steer clear of it in normal scripting, and in particular don't count on it holding writable data

Parameters :

do_create ( bool ) – Ensure that system properties are created if they do not exist yet (optional)

Returns :

The system properties root container, or None if there are no system properties stored in this data yet, and its creation was not requested

Return type :

PropertyGroup
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
| Gizmo.target_set_operator KeyConfigurations.find_item_from_operator KeyMapItem.properties KeyMapItems.find_from_operator Macro.properties Operator.description Operator.properties OperatorMacro.properties | UILayout.operator UILayout.operator_menu_enum UILayout.operator_menu_hold UILayout.template_popup_confirm WindowManager.operator_properties_last WorkSpaceTool.operator_properties XrActionMapItem.op_properties |
## OperatorProperties(bpy_struct)

### OperatorProperties(bpy_struct) 

base class — bpy_struct
class bpy.types. OperatorProperties ( bpy_struct ) 

The input properties belonging to an operator

[Related references](INDEX.md).

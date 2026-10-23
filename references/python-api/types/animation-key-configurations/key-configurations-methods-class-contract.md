# bpy.types.KeyConfigurations: methods - class-contract, Inherited Properties, Inherited Functions

new ( name )

new

Parameters :

name ( str ) – Name, (never None)

Returns :

Key Configuration, Added key configuration

Return type :

KeyConfig
remove ( keyconfig )

remove

Parameters :

keyconfig (KeyConfig) – Key Configuration, Removed key configuration (never None)
find_item_from_operator ( idname , * , context = '`INVOKE_DEFAULT`' , properties = None , include = {'ACTIONZONE', 'KEYBOARD', 'MOUSE', 'NDOF'} , exclude = set() )

find_item_from_operator

Parameters :

- idname ( str ) – Operator Identifier, (never None)

- context (Literal[Operator Context Items]) – context, (optional)

- properties (OperatorProperties) – (optional)

- include (set[Literal[Event Type Mask Items]]) – Include, (optional)

- exclude (set[Literal[Event Type Mask Items]]) – Exclude, (optional)

Returns :

keymap , KeyMap

item , KeyMapItem

Return type :

tuple[KeyMap, KeyMapItem]
update ( * , keep_properties = False )

update

Parameters :

keep_properties ( bool ) – Keep Properties, Operator properties are kept to allow the operators to be registered again in the future (optional)
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

[Related references](INDEX.md).

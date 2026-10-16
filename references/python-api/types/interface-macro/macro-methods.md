# bpy.types.Macro: methods

report ( type , message )

report

Parameters :

- type (set[Literal[Wm Report Items]]) – Type

- message ( str ) – Report Message, (never None)
classmethod poll ( context )

Check whether the operator is allowed to run

Parameters :

context (Context) – (never None)

Return type :

bool
draw ( context )

Draw function for the operator

Parameters :

context (Context) – (never None)
classmethod define ( operator )

Append an operator to a registered macro class.

Parameters :

operator ( str ) – Identifier of the operator. This does not have to be defined when this function is called.

Returns :

The operator macro for property access.

Return type :

OperatorMacro
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
| Operator.macros | |

[Related references](INDEX.md).

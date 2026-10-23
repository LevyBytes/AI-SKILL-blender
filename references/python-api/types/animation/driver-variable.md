# bpy.types.DriverVariable

is_name_valid

Whether this name works as a driver variable name (default True, readonly)

Type :

bool
name

The name used inside scripted expressions and functions (spaces and dots aren’t permitted, and it has to begin with a letter) (default “”, never None)

Type :

str
targets

Where this variable’s input data comes from for evaluation (default None, readonly)

Type :

bpy_prop_collection[DriverTarget]
type

Which driver variable type this is (default '`SINGLE_PROP`' )

- `SINGLE_PROP`
Single Property – Read the value off some RNA property.

- TRANSFORMS
Transform Channel – The fully resolved transform value of an object or bone.

- `ROTATION_DIFF`
Rotational Difference – The angle separating two bones.

- `LOC_DIFF`
Distance – The gap between a pair of bones or objects.

- `CONTEXT_PROP`
Context Property – Read the value off an RNA property within the active evaluation context.

Type :

Literal[‘`SINGLE_PROP`’, ‘TRANSFORMS’, ‘`ROTATION_DIFF`’, ‘`LOC_DIFF`’, ‘`CONTEXT_PROP`’]
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

- default (type | None ) – The value to return when not found.

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
| ChannelDriverVariables.new ChannelDriverVariables.remove | Driver.variables |
## DriverVariable(bpy_struct)

### DriverVariable(bpy_struct)

base class: bpy_struct
class bpy.types. DriverVariable ( bpy_struct )

A variable pulled from some source or target within a driver relationship

[Related references](INDEX.md).

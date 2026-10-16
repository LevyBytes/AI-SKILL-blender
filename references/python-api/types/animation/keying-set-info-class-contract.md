# bpy.types.KeyingSetInfo — class-contract, Inherited Properties, Inherited Functions, References, KeyingSetInfo(bpy_struct)

bl_description

A brief description of the keying set (default “”, never None)

Type :

str
bl_idname

When set, the Keying Set is given a custom ID; otherwise it inherits the name of the class that defines it (for instance, with a class named “`BUILTIN_KSI`_location” and no bl_idname set by the script, bl_idname becomes “`BUILTIN_KSI`_location”) (default “”, never None)

Type :

str
bl_label

(default “”, never None)

Type :

str
bl_options

The Keying Set options applied while inserting keyframes (default set())

Type :

set[Literal[Keying Flag Items]]
poll ( context )

Check whether the Keying Set is usable.

Return type :

bool
iterator ( context , ks )

Invoke generate() on the structs whose properties are to be keyframed.
generate ( context , ks , data )

Add Paths to the Keying Set so the given data's properties get keyframed.

Parameters :

data (AnyType) – (never None)
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
| KeyingSet.type_info | |
## KeyingSetInfo(bpy_struct)

[Related references](INDEX.md).

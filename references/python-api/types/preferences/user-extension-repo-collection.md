# bpy.types.UserExtensionRepoCollection

classmethod new ( * , name = '' , module = '' , custom_directory = '' , remote_url = '' , source = 'USER' ) 

Create a fresh repository

Parameters :

- name ( str ) – Name, (optional, never None)

- module ( str ) – Module, (optional, never None)

- custom_directory ( str ) – Custom Directory, (optional, never None)

- remote_url ( str ) – Remote URL, (optional, never None)

- source ( Literal [ 'USER' , 'SYSTEM' ] ) – Source, The way the repository gets managed (optional)

- USER
User – Repository managed by the user, stored in user directories.

- SYSTEM
System – Read-only repository provided by the system.

Returns :

Newly added repository

Return type :

UserExtensionRepo
classmethod remove ( repo ) 

Delete repos

Parameters :

repo (UserExtensionRepo) – Repository to remove (never None)
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
| PreferencesExtensions.repos | |
## UserExtensionRepoCollection(bpy_prop_collection)

### UserExtensionRepoCollection(bpy_prop_collection) 

base classes — bpy_prop, bpy_prop_collection
class bpy.types. UserExtensionRepoCollection ( bpy_prop_collection ) 

A grouping that holds the user's extension repositories

[Related references](INDEX.md).

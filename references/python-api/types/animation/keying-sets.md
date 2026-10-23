# bpy.types.KeyingSets

active 

The currently active Keying Set used when inserting or deleting keyframes

Type :

KeyingSet
active_index 

Index of the Keying Set in use right now (negative values mean 'builtin', positive ones mean 'absolute') (in [-inf, inf], default 0)

Type :

int
new ( * , idname = 'KeyingSet' , name = 'KeyingSet' ) 

Create a fresh Keying Set on the Scene

Parameters :

- idname ( str ) – IDName, Internal identifier of Keying Set (optional, never None)

- name ( str ) – Name, User visible name of Keying Set (optional, never None)

Returns :

Newly created Keying Set

Return type :

KeyingSet
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

- default ( type | None ) – The value to return when not found.

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
| Scene.keying_sets | |
## KeyingSets(bpy_prop_collection)

### KeyingSets(bpy_prop_collection) 

base classes: bpy_prop, bpy_prop_collection
class bpy.types. KeyingSets ( bpy_prop_collection ) 

The keying sets belonging to a scene

[Related references](INDEX.md).

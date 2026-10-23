# bpy.types.KeyingSetPaths - class-contract, Inherited Properties, Inherited Functions, References, KeyingSetPaths(bpy_prop_collection)

active 

The currently active Keying Set used when inserting or deleting keyframes

Type :

KeyingSetPath
active_index 

Index of the Keying Set in use right now (in [-inf, inf], default 0)

Type :

int
add ( target_id , data_path , * , index = -1 , group_method = 'KEYINGSET' , group_name = '' ) 

Register an additional path on the Keying Set

Parameters :

- target_id (ID) – Target ID, ID data-block for the destination

- data_path ( str ) – Data-Path, RNA-Path to destination property (never None)

- index ( int ) – Index, The index of the destination property (i.e. axis of Location/Rotation/etc.), or -1 for the entire array (in [-1, inf], optional)

- group_method (Literal[Keyingset Path Grouping Items]) – Grouping Method, Method used to define which Group-name to use (optional)

- group_name ( str ) – Group Name, Name of Action Group to assign destination to (only if grouping mode is to use this name) (optional, never None)

Returns :

New Path, Path created and added to the Keying Set

Return type :

KeyingSetPath
remove ( path ) 

Take the specified path out of the Keying Set

Parameters :

path (KeyingSetPath) – Path, (never None)
clear ( ) 

Drop every path the Keying Set holds
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
| KeyingSet.paths | |
## KeyingSetPaths(bpy_prop_collection)

[Related references](INDEX.md).

# bpy.types.ObjectModifiers

active 

The active modifier in the list

Type :

Modifier
new ( name , type ) 

Attach a fresh modifier

Parameters :

- name ( str ) – New name for the modifier (never None)

- type (Literal[Object Modifier Type Items]) – Modifier type to add

Returns :

Newly created modifier

Return type :

Modifier
remove ( modifier ) 

Detach an existing modifier from the object

Parameters :

modifier (Modifier) – Modifier to remove (never None)
clear ( ) 

Detach every modifier from the object
move ( from_index , to_index ) 

Shift a modifier to another slot

Parameters :

- from_index ( int ) – From Index, Index to move (in [-inf, inf])

- to_index ( int ) – To Index, Target index (in [-inf, inf])
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
| Object.modifiers | |
## ObjectModifiers(bpy_prop_collection)

### ObjectModifiers(bpy_prop_collection) 

base classes: bpy_prop, bpy_prop_collection
class bpy.types. ObjectModifiers ( bpy_prop_collection ) 

The set of modifiers attached to an object

[Related references](INDEX.md).

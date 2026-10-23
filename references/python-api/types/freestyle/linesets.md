# bpy.types.Linesets

active 

The line set on display right now (readonly)

Type :

FreestyleLineSet
active_index 

Slot index of the active line set (in [0, inf], default 0)

Type :

int
new ( name ) 

Add a line set into the scene render layer's Freestyle settings

Parameters :

name ( str ) – New name for the line set (not unique) (never None)

Returns :

Newly created line set

Return type :

FreestyleLineSet
remove ( lineset ) 

Take a line set out of the scene render layer's Freestyle settings

Parameters :

lineset (FreestyleLineSet) – Line set to remove (never None)
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
| FreestyleSettings.linesets | |
## Linesets(bpy_prop_collection)

### Linesets(bpy_prop_collection) 

base classes: bpy_prop, bpy_prop_collection
class bpy.types. Linesets ( bpy_prop_collection ) 

Line sets that pair lines with their style parameters

[Related references](INDEX.md).

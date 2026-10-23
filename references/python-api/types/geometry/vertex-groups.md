# bpy.types.VertexGroups

active 

Vertex groups of the object

Type :

VertexGroup
active_index 

Active index in vertex group array (in [0, inf], default 0)

Type :

int
new ( * , name = 'Group' ) 

Attach a vertex group to the object

Parameters :

name ( str ) – Vertex group name (optional, never None)

Returns :

New vertex group

Return type :

VertexGroup
remove ( group ) 

Drop a vertex group from the object

Parameters :

group (VertexGroup) – Vertex group to remove (never None)
clear ( ) 

Drop every vertex group from the object
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
| Object.vertex_groups | |
## VertexGroups(bpy_prop_collection)

### VertexGroups(bpy_prop_collection) 

base classes: bpy_prop, bpy_prop_collection
class bpy.types. VertexGroups ( bpy_prop_collection ) 

A grouping that holds vertex groups

[Related references](INDEX.md).

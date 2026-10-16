# bpy.types.VertexGroup: methods

add ( index , weight , type ) 

Place vertices into the group

Parameters :

- index ( Sequence [ int ] ) – List of indices (array of 1 items, in [-inf, inf])

- weight ( float ) – Vertex weight (in [0, 1])

- type ( Literal [ 'REPLACE' , 'ADD' , 'SUBTRACT' ] ) – Vertex assign mode

- REPLACE
Replace – Replace.

- ADD
Add – Add.

- SUBTRACT
Subtract – Subtract.
remove ( index ) 

Take vertices out of the group

Parameters :

index ( Sequence [ int ] ) – List of indices (array of 1 items, in [-inf, inf])
weight ( index ) 

Read back a vertex's weight in the group

Parameters :

index ( int ) – Index, The index of the vertex (in [0, inf])

Returns :

Vertex weight (in [0, 1])

Return type :

float
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
| Object.vertex_groups VertexGroups.active | VertexGroups.new VertexGroups.remove |

[Related references](INDEX.md).

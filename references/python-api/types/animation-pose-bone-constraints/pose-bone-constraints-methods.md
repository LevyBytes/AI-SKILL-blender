# bpy.types.PoseBoneConstraints: methods

new ( type )

Attach a new constraint to this object

Parameters :

type (Literal[Constraint Type Items]) – Which kind of constraint to add

Returns :

New constraint

Return type :

Constraint
remove ( constraint )

Detach a constraint from this object

Parameters :

constraint (Constraint) – The constraint being removed (never None)
move ( from_index , to_index )

Shift a constraint to another slot

Parameters :

- from_index ( int ) – From Index, The slot to move from (in [-inf, inf])

- to_index ( int ) – To Index, The destination slot (in [-inf, inf])
copy ( constraint )

Append a constraint that duplicates the one supplied

Parameters :

constraint (Constraint) – The constraint to duplicate - it may live on another object (never None)

Returns :

New constraint

Return type :

Constraint
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
| PoseBone.constraints | |

[Related references](INDEX.md).

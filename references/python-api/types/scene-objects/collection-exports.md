# bpy.types.CollectionExports

new ( type , * , name = '' )

Create and attach another export handler within the collection

Parameters :

- type ( Literal [ '`IO_FH`_alembic' , '`IO_FH`_usd' , '`IO_FH`_obj' , '`IO_FH`_ply' , '`IO_FH`_stl' , '`IO_FH`_fbx' , '`IO_FH`_gltf2' ] ) – Type, Which kind of export handler to create

- name ( str ) – Name, The label assigned to this freshly made handler (optional, never None)

Returns :

The export handler that was just created

Return type :

CollectionExport
remove ( exporter )

Detach the given export handler so it no longer belongs to the collection

Parameters :

exporter (CollectionExport) – Export Handler to remove
move ( from_index , to_index )

Reorder an export handler within the collection

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
| Collection.exporters | |
## CollectionExports(bpy_prop_collection)

### CollectionExports(bpy_prop_collection)

base classes — bpy_prop, bpy_prop_collection
class bpy.types. CollectionExports ( bpy_prop_collection )

A group holding the export handlers

[Related references](INDEX.md).

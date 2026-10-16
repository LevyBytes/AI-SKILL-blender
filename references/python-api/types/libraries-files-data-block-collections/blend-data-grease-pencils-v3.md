# bpy.types.BlendDataGreasePencilsV3

tag ( value ) 

tag

Parameters :

value ( bool ) – Value
new ( name ) 

Insert a sketch into the database

Parameters :

name ( str ) – New name for the data-block (never None)

Returns :

New Grease Pencil data-block

Return type :

GreasePencil
remove ( grease_pencil , * , do_unlink = True , do_id_user = True , do_ui_user = True ) 

Remove a sketch from the current file

Parameters :

- grease_pencil (GreasePencil) – Grease Pencil to remove (never None)

- do_unlink ( bool ) – Break all references to this Grease Pencil before deletion (optional)

- do_id_user ( bool ) – Reduce user count for all data-blocks used (optional)

- do_ui_user ( bool ) – Ensure the interface is updated (optional)
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
| BlendData.grease_pencils | |
class bpy.types. BlendDataGreasePencilsV3 ( bpy_prop_collection )

Collection of Grease Pencils
## BlendDataGreasePencilsV3(bpy_prop_collection)

Registry of procedural hair objects.

base classes — bpy_prop, bpy_prop_collection

[Related references](INDEX.md).

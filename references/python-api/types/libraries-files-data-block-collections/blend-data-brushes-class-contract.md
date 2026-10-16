# bpy.types.BlendDataBrushes — class-contract, Inherited Properties, Inherited Functions, References

new ( name , * , mode = '`TEXTURE_PAINT`' ) 

Add a brush to the database

Parameters :

- name ( str ) – New name for the data-block (never None)

- mode (Literal[Object Mode Items]) – Paint Mode for the new brush (optional)

Returns :

New brush data-block

Return type :

Brush
remove ( brush , * , do_unlink = True , do_id_user = True , do_ui_user = True ) 

Delete a brush from the current file

Parameters :

- brush (Brush) – Brush to remove (never None)

- do_unlink ( bool ) – Break all references to this brush before deletion (optional)

- do_id_user ( bool ) – Reduce user count for all data-blocks used (optional)

- do_ui_user ( bool ) – Ensure the interface is updated (optional)
tag ( value ) 

tag

Parameters :

value ( bool ) – Value
create_gpencil_data ( brush ) 

Extend a brush with hand-drawn tool properties

Parameters :

brush (Brush) – Brush (never None)
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
| BlendData.brushes | |
class bpy.types. BlendDataBrushes ( bpy_prop_collection )

List of paint tool configurations

[Related references](INDEX.md).

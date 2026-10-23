# bpy.types.RenderSettings: methods

## RenderSettings(bpy_struct)

### RenderSettings(bpy_struct)

base class: bpy_struct
class bpy.types. RenderSettings ( bpy_struct )

Per-Scene data-block holding that scene's render configuration
frame_path ( * , frame = -2147483648 , preview = False , view = '' )

Give back the full path of the file that a particular frame will be written to

Parameters :

- frame ( int ) – Frame number to use, if unset the current frame will be used (in [-inf, inf], optional)

- preview ( bool ) – Preview, Use preview range (optional)

- view ( str ) – View, The name of the view to use to replace the “%” chars (optional, never None)

Returns :

File Path, The resulting filepath from the scenes render settings (never None)

Return type :

str
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
| RenderEngine.render | Scene.render |

[Related references](INDEX.md).

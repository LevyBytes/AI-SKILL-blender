# bpy.types.RenderResult — class-contract, Inherited Properties, Inherited Functions, References, RenderResult(bpy_struct)

layers 

(default None, readonly)

Type :

bpy_prop_collection[RenderLayer]
resolution_x 

(in [-inf, inf], default 0, readonly)

Type :

int
resolution_y 

(in [-inf, inf], default 0, readonly)

Type :

int
views 

(default None, readonly)

Type :

bpy_prop_collection[RenderView]
load_from_file ( filepath ) 

Read pixel data into this render result out of an image file on disk

Parameters :

filepath ( str ) – File Name, Filename to load into this render tile, must be no smaller than the render result (never None)
stamp_data_add_field ( field , value ) 

Add engine-specific stamp data to the result

Parameters :

- field ( str ) – Field, Name of the stamp field to add (never None)

- value ( str ) – Value, Value of the stamp data (never None)
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
| RenderEngine.begin_result RenderEngine.end_result | RenderEngine.get_result RenderEngine.update_result |
## RenderResult(bpy_struct)

[Related references](INDEX.md).

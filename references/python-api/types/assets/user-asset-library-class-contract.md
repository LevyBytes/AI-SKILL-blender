# bpy.types.UserAssetLibrary — class-contract, Inherited Properties, Inherited Functions, References, UserAssetLibrary(bpy_struct)

enabled 

Turn the asset library on (default True)

Type :

bool
import_method 

Choose the way assets get brought in, unless the Asset Browser overrides it (default 'PACK' )

- LINK
Link – Import the assets as linked data-block.

- APPEND
Append – Import the assets as copied data-block, with no link to the original asset data-block.

- `APPEND_REUSE`
Append (Reuse Data) – Import the assets as copied data-block while avoiding multiple copies of nested, typically heavy data. For example the textures of a material asset, or the mesh of an object asset, don't have to be copied every time this asset is imported. The instances of the asset share the data instead..

- PACK
Pack – Import the asset as linked data-block, and pack it in the current file (ensures that it remains unchanged in case the library data is modified, is not available anymore, etc.).

Type :

Literal['LINK', 'APPEND', '`APPEND_REUSE`', 'PACK']
name 

A label for the asset library, which need not be unique (default "", never None)

Type :

str
path 

Location of a folder holding .blend files that serve as the asset library (default "", never None)

Type :

str
use_relative_path 

Store a relative path when assets from this library are linked (default True)

Type :

bool
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
| AssetLibraryCollection.new AssetLibraryCollection.remove | PreferencesFilePaths.asset_libraries |
## UserAssetLibrary(bpy_struct)

[Related references](INDEX.md).

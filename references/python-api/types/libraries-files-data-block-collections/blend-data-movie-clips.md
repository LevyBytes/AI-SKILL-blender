# bpy.types.BlendDataMovieClips

tag ( value ) 

tag

Parameters :

value ( bool ) – Value
remove ( clip , * , do_unlink = True , do_id_user = True , do_ui_user = True ) 

Erase a movie clip from the current file.

Parameters :

- clip (MovieClip) – Movie clip to remove (never None)

- do_unlink ( bool ) – Break all references to this movie clip before deletion (optional)

- do_id_user ( bool ) – Reduce user count for all data-blocks used (optional)

- do_ui_user ( bool ) – Ensure the interface is updated (optional)
load ( filepath , * , check_existing = False ) 

Link a movie clip into the database from a file (note: check_existing is disabled by default for consistency with other load operations, but using multiple clips with the same file path can create unwanted proxy artifacts)

Parameters :

- filepath ( str ) – path for the data-block (never None, blend relative // prefix supported)

- check_existing ( bool ) – Using existing data-block if this file is already loaded (optional)

Returns :

New movie clip data-block

Return type :

MovieClip
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
| BlendData.movieclips | |
class bpy.types. BlendDataMovieClips ( bpy_prop_collection )

Collection of movie clips
## BlendDataMovieClips(bpy_prop_collection)

Registry of reusable node setup templates.

base classes: bpy_prop, bpy_prop_collection

[Related references](INDEX.md).

# bpy.types.MovieClipUser

frame_current

Frame currently shown within the movie or image sequence (in [-1048574, 1048574], default 1)

Type :

int
proxy_render_size

Show the preview at full resolution or at one of the proxy resolutions (default 'FULL' )

Type :

Literal[‘`PROXY_25`’, ‘`PROXY_50`’, ‘`PROXY_75`’, ‘`PROXY_100`’, ‘FULL’]
use_render_undistorted

Render the preview from the undistorted proxy (default False)

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
| CameraBackgroundImage.clip_user SpaceClipEditor.clip_user | UILayout.template_marker UILayout.template_movieclip_information |
## MovieClipUser(bpy_struct)

### MovieClipUser(bpy_struct)

base class: bpy_struct
class bpy.types. MovieClipUser ( bpy_struct )

Settings that describe how one data-block consumes a MovieClip data-block

[Related references](INDEX.md).

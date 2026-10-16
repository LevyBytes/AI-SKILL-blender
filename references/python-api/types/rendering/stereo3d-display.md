# bpy.types.Stereo3dDisplay

anaglyph_type

(default '`RED_CYAN`' )

Type :

Literal[Stereo3D Anaglyph Type Items]
display_mode

(default 'ANAGLYPH' )

Type :

Literal[Stereo3D Display Items]
interlace_type

(default '`ROW_INTERLEAVED`' )

Type :

Literal[Stereo3D Interlace Type Items]
use_interlace_swap

Exchange the left and right stereo channels (default False)

Type :

bool
use_sidebyside_crosseyed

Have the right eye view the left image and the other way around (default False)

Type :

bool
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – Identifier of the RNA type.

- default (bpy.types.Struct | None) – Value returned if nothing matches.

Returns :

Either the matching RNA type, or the default when there is no match.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – Identifier of the RNA type.

- default ( type | None ) – Value returned if nothing matches.

Returns :

Either the matching class, or the default when there is no match.

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
| Window.stereo_3d_display | |
## Stereo3dDisplay(bpy_struct)

### Stereo3dDisplay(bpy_struct)

base class — bpy_struct
class bpy.types. Stereo3dDisplay ( bpy_struct )

Configuration for showing stereo 3D

[Related references](INDEX.md).

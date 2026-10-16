# bpy.types.SpaceImageOverlay

passepartout_alpha

How opaque the darkened overlay is outside the render region (in [0, 1], default 0.5)

Type :

float
show_grid_background

Draw the grid background together with its borders (default False)

Type :

bool
show_overlays

Draw overlays such as UV Maps and Metadata (default False)

Type :

bool
show_render_size

Draw the area that the final render covers (default False)

Type :

bool
show_text_info

Draw the overlay text (default False)

Type :

bool
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – Identifier for the RNA type.

- default (bpy.types.Struct | None) – Value returned if nothing matches.

Returns :

The matching RNA type, or the default if none is found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – Identifier for the RNA type.

- default ( type | None ) – Value returned if nothing matches.

Returns :

The matching class, or the default if none is found.

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
| SpaceImageEditor.overlay | |
## SpaceImageOverlay(bpy_struct)

### SpaceImageOverlay(bpy_struct)

base class — bpy_struct
class bpy.types. SpaceImageOverlay ( bpy_struct )

Configuration for the overlays drawn in the UV/Image editor
## See also

- [Bpy Struct](../data-types-bpy-struct/INDEX.md)

[Related references](INDEX.md).

# bpy.types.BlendFileColorspace

is_missing_opencolorio_config

An OpenColorIO color scheme, display mode, or gamma profile could not be found, which signals that the OpenColorIO profile applied during file creation is unavailable (default False, readonly)

Type:
bool
working_space

The color reproduction system used for all scene-linear pixel values, as well as for node-based compositing, shader node processing, and geometry node computations (readonly)

- Linear Rec.709
Linear Rec.709 – Linear BT.709 using D65 white illumination.

- Linear Rec.2020
Linear Rec.2020 – Linear BT.2020 using D65 white illumination.

- ACEScg
ACEScg – AP1 linear with ACES reference white.

Type:
Literal['Linear Rec.709', 'Linear Rec.2020', 'ACEScg']
working_space_interop_id

Standard name assigned by the Color Interop Forum for typical color reproduction systems; may be empty when no interop mapping is defined for the selected working space. Frequently encountered assignments: lin_rec709_scene, lin_rec2020_scene, lin_ap1_scene (for ACEScg) (default "", readonly, never None)

Type:
str
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:
- id (str) – Type designation for the RNA.
- default (bpy.types.Struct | None) – Fallback to return if not located.

Returns:
The RNA type or fallback.

Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:
- id (str) – Type designation for the RNA.
- default (type | None) – Fallback to return if not located.

Returns:
The class or fallback.

Return type:
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
| BlendData.colorspace | |
## BlendFileColorspace(bpy_struct)

### BlendFileColorspace(bpy_struct)

base class — bpy_struct
class bpy.types.BlendFileColorspace(bpy_struct)

Holds metadata about the color encoding system selected for stored data in a blend file.

[Related references](INDEX.md).

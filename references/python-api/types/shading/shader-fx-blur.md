# bpy.types.ShaderFxBlur

rotation

How much the effect is turned (in [-inf, inf], default 0.0)

Type :

float
samples

Sample count for the blur, where zero turns blurring off (in [0, 32], default 4)

Type :

int
size

Strength of the blur (array of 2 items, in [0, inf], default (0.0, 0.0))

Type :

mathutils.Vector
use_dof_mode

Blur according to the camera's depth of field (default False)

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
| bpy_struct.id_data ShaderFx.name ShaderFx.type ShaderFx.show_viewport | ShaderFx.show_render ShaderFx.show_in_editmode ShaderFx.show_expanded |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values ShaderFx.bl_rna_get_subclass ShaderFx.bl_rna_get_subclass_py |
## ShaderFxBlur(ShaderFx)

### ShaderFxBlur(ShaderFx)

base classes: bpy_struct, ShaderFx
class bpy.types. ShaderFxBlur ( ShaderFx )

Gaussian Blur effect

[Related references](INDEX.md).

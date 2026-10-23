# bpy.types.ShaderFxWave

amplitude

Height of the wave (in [0, inf], default 0.0)

Type :

float
orientation

Which way the wave travels (default 'HORIZONTAL' )

Type :

Literal[‘HORIZONTAL’, ‘VERTICAL’]
period

Length of one wave cycle (in [0, inf], default 0.0)

Type :

float
phase

Offset applied to the wave's phase (in [-inf, inf], default 0.0)

Type :

float
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
## ShaderFxWave(ShaderFx)

### ShaderFxWave(ShaderFx)

base classes: bpy_struct, ShaderFx
class bpy.types. ShaderFxWave ( ShaderFx )

Wave Deformation effect

[Related references](INDEX.md).

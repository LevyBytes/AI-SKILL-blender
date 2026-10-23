# bpy.types.CollectionProperty

fixed_type

The locked pointer type; left empty when the type can vary (readonly)

Type :

Struct
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
| bpy_struct.id_data Property.name Property.identifier Property.description Property.translation_context Property.type Property.subtype Property.srna Property.unit Property.icon Property.is_readonly Property.is_animatable Property.is_overridable Property.is_required Property.is_argument_optional Property.is_never_none Property.is_hidden | Property.is_skip_save Property.is_skip_preset Property.is_output Property.is_registered Property.is_registered_optional Property.is_runtime Property.is_enum_flag Property.is_library_editable Property.is_path_output Property.is_path_supports_blend_relative Property.is_path_supports_templates Property.is_deprecated Property.deprecated_note Property.deprecated_version Property.deprecated_removal_version Property.tags |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values Property.bl_rna_get_subclass Property.bl_rna_get_subclass_py |
## CollectionProperty(Property)

### CollectionProperty(Property)

base classes: bpy_struct, Property
class bpy.types. CollectionProperty ( Property )

An RNA collection property used for lists, arrays, and mappings

[Related references](INDEX.md).

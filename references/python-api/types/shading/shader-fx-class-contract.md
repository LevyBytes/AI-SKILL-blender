# bpy.types.ShaderFx — class-contract, Inherited Properties, Inherited Functions, References, ShaderFx(bpy_struct)

name

A name for the effect (default “”, never None)

Type :

str
show_expanded

Whether the effect is expanded in the interface (default False)

Type :

bool
show_in_editmode

Render the effect while in Edit mode (default False)

Type :

bool
show_render

Apply the effect at render time (default False)

Type :

bool
show_viewport

Render the effect in the viewport (default False)

Type :

bool
type

(default '`FX_BLUR`' , readonly)

Type :

Literal[Object Shaderfx Type Items]
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

- default (type | None ) – The value to return when not found.

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
| Object.shader_effects ObjectShaderFx.new | ObjectShaderFx.remove |
## ShaderFx(bpy_struct)

[Related references](INDEX.md).

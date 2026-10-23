# bpy.types.LineStyleGeometryModifier_TipRemover

expanded 

Whether the modifier's tab is shown in its unfolded state (default False)

Type :

bool
tip_length 

Length of tips to be removed (in [-inf, inf], default 0.0)

Type :

float
type 

Which kind of modifier this is (default '2`D_OFFSET`' , readonly)

Type :

Literal[Linestyle Geometry Modifier Type Items]
use 

Turn this modifier on or off while the stroke is being rendered (default False)

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

- default (type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type
### Inherited Properties 

| Members | Members |
| --- | --- |
| bpy_struct.id_data | LineStyleGeometryModifier.name |
### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete bpy_struct.keyframe_insert | bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values LineStyleModifier.bl_rna_get_subclass LineStyleModifier.bl_rna_get_subclass_py LineStyleGeometryModifier.bl_rna_get_subclass LineStyleGeometryModifier.bl_rna_get_subclass_py |
## LineStyleGeometryModifier_TipRemover(LineStyleGeometryModifier)

### LineStyleGeometryModifier_TipRemover(LineStyleGeometryModifier) 

base classes: bpy_struct, LineStyleModifier, LineStyleGeometryModifier
class bpy.types. LineStyleGeometryModifier_TipRemover ( LineStyleGeometryModifier ) 

Trim a segment off each end of the stroke backbone

[Related references](INDEX.md).

# bpy.types.LineStyleThicknessModifier

name 

Name of the modifier (default “”, never None)

Type :

str
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
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values LineStyleModifier.bl_rna_get_subclass LineStyleModifier.bl_rna_get_subclass_py |
### References 

| Description | Description |
| --- | --- |
| FreestyleLineStyle.thickness_modifiers LineStyleThicknessModifiers.new | LineStyleThicknessModifiers.remove |
## LineStyleThicknessModifier(LineStyleModifier)

### LineStyleThicknessModifier(LineStyleModifier) 

base classes: bpy_struct, LineStyleModifier

subclasses —
LineStyleThicknessModifier_AlongStroke, LineStyleThicknessModifier_Calligraphy, LineStyleThicknessModifier_CreaseAngle, LineStyleThicknessModifier_Curvature_3D, LineStyleThicknessModifier_DistanceFromCamera, LineStyleThicknessModifier_DistanceFromObject, LineStyleThicknessModifier_Material, LineStyleThicknessModifier_Noise, LineStyleThicknessModifier_Tangent
class bpy.types. LineStyleThicknessModifier ( LineStyleModifier ) 

Parent type from which line thickness modifiers derive

[Related references](INDEX.md).

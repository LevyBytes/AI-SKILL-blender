# bpy.types.CurveModifier

deform_axis

Along which axis the curve does its deforming (default '`POS_X`' )

Type :

Literal['`POS_X`', '`POS_Y`', '`POS_Z`', '`NEG_X`', '`NEG_Y`', '`NEG_Z`']
invert_vertex_group

Flip the weighting of the vertex group (default False)

Type :

bool
object

Curve object to deform with

Type :

Object
vertex_group

The vertex group whose weights set the modifier's per-point strength (default "", never None)

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
| bpy_struct.id_data Modifier.name Modifier.type Modifier.show_viewport Modifier.show_render Modifier.show_in_editmode Modifier.show_on_cage | Modifier.show_expanded Modifier.is_active Modifier.use_pin_to_last Modifier.is_override_data Modifier.use_apply_on_spline Modifier.execution_time Modifier.persistent_uid |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values Modifier.bl_rna_get_subclass Modifier.bl_rna_get_subclass_py |
## CurveModifier(Modifier)

### CurveModifier(Modifier)

base classes — bpy_struct, Modifier
class bpy.types. CurveModifier ( Modifier )

A modifier that bends geometry along a curve.

[Related references](INDEX.md).

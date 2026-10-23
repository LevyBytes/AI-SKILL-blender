# bpy.types.MaintainVolumeConstraint

free_axis

The axis left free for scaling on the object (default '`SAMEVOL_X`' )

Type :

Literal[‘`SAMEVOL_X`’, ‘`SAMEVOL_Y`’, ‘`SAMEVOL_Z`’]
mode

How the constraint handles scaling on the original non-free axes (default 'STRICT' )

- STRICT
Strict – Volume is strictly preserved, overriding the scaling of non-free axes.

- UNIFORM
Uniform – Volume is preserved when the object is scaled uniformly. Deviations from uniform scale on non-free axes are passed through..

- `SINGLE_AXIS`
Single Axis – Volume is preserved when the object is scaled only on the free axis. Non-free axis scaling is passed through..

Type :

Literal[‘STRICT’, ‘UNIFORM’, ‘`SINGLE_AXIS`’]
volume

Resting volume of the bone (in [0, inf], default 0.0)

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
| bpy_struct.id_data Constraint.name Constraint.type Constraint.is_override_data Constraint.owner_space Constraint.target_space Constraint.space_object Constraint.space_subtarget | Constraint.mute Constraint.enabled Constraint.show_expanded Constraint.is_valid Constraint.active Constraint.influence Constraint.error_location Constraint.error_rotation |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values Constraint.bl_rna_get_subclass Constraint.bl_rna_get_subclass_py |
## MaintainVolumeConstraint(Constraint)

### MaintainVolumeConstraint(Constraint)

base classes: bpy_struct, Constraint
class bpy.types. MaintainVolumeConstraint ( Constraint )

Holds volume steady while scaling occurs along one axis.

[Related references](INDEX.md).

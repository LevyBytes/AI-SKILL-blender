# bpy.types.FloorConstraint

floor_location

Side of the target that the object is blocked from passing through (default '`FLOOR_X`' )

Type :

Literal[‘`FLOOR_X`’, ‘`FLOOR_Y`’, ‘`FLOOR_Z`’, ‘`FLOOR_NEGATIVE_X`’, ‘`FLOOR_NEGATIVE_Y`’, ‘`FLOOR_NEGATIVE_Z`’]
offset

Offset of floor from object origin (in [-inf, inf], default 0.0)

Type :

float
subtarget

Armature bone, mesh or lattice vertex group, … (default “”, never None)

Type :

str
target

Target object

Type :

Object
use_rotation

Use the target’s rotation to determine floor (default False)

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
| bpy_struct.id_data Constraint.name Constraint.type Constraint.is_override_data Constraint.owner_space Constraint.target_space Constraint.space_object Constraint.space_subtarget | Constraint.mute Constraint.enabled Constraint.show_expanded Constraint.is_valid Constraint.active Constraint.influence Constraint.error_location Constraint.error_rotation |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values Constraint.bl_rna_get_subclass Constraint.bl_rna_get_subclass_py |
## FloorConstraint(Constraint)

### FloorConstraint(Constraint)

base classes — bpy_struct, Constraint
class bpy.types. FloorConstraint ( Constraint )

Restrict where an object may move by treating a target as a floor it cannot cross.

[Related references](INDEX.md).

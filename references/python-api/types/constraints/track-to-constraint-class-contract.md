# bpy.types.TrackToConstraint - class-contract, Inherited Properties, Inherited Functions, TrackToConstraint(Constraint)

head_tail 

Position along the bone’s length to target: 0 is Head, 1 is Tail (in [0, 1], default 0.0)

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
track_axis 

Which axis aims at the target object (default '`TRACK_X`' )

Type :

Literal[‘`TRACK_X`’, ‘`TRACK_Y`’, ‘`TRACK_Z`’, ‘`TRACK_NEGATIVE_X`’, ‘`TRACK_NEGATIVE_Y`’, ‘`TRACK_NEGATIVE_Z`’]
up_axis 

Which axis aims upward (default '`UP_X`' )

Type :

Literal[‘`UP_X`’, ‘`UP_Y`’, ‘`UP_Z`’]
use_bbone_shape 

Trace the shape of the B-Bone segments when computing the Head/Tail position (default False)

Type :

bool
use_target_z 

Constrain the Up direction using the target’s Z axis rather than the World Z axis (default False)

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
## TrackToConstraint(Constraint)

[Related references](INDEX.md).

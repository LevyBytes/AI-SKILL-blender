# bpy.types.NDOFMotionEventData

progress

Reports which phase the gesture is currently in (default 'STARTING' , readonly)

Type :

Literal[‘STARTING’, ‘`IN_PROGRESS`’, ‘FINISHING’]
rotation

Rotation of this motion event given as an axis-angle pair. A magnitude of 1.0 on the vector corresponds to a full 360-degree turn, and the angle is usually multiplied by the time-delta before it is applied. (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
time_delta

Elapsed time in seconds since the prior motion event (in [-inf, inf], default 0.0, readonly)

Type :

float
translation

Movement carried by this motion event. Each axis ranges from -1 to 1 before the sensitivity preference scales it, and the result is usually multiplied by the time-delta prior to use. (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
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
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Description | Description |
| --- | --- |
| Event.ndof_motion | |
## NDOFMotionEventData(bpy_struct)

### NDOFMotionEventData(bpy_struct)

base class — bpy_struct
class bpy.types. NDOFMotionEventData ( bpy_struct )

Motion information from an NDOF device carried on window manager events.

[Related references](INDEX.md).

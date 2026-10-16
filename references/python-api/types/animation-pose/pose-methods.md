# bpy.types.Pose: methods

classmethod apply_pose_from_action ( action , * , evaluation_time = 0.0 )

Evaluate the supplied action at a chosen time and set this pose from it. Affects only the selected bones, or every bone when nothing is selected.

Parameters :

- action (Action) – Action, The Action that holds the pose

- evaluation_time ( float ) – Evaluation Time, The time at which the action is sampled to read off the pose (in [-inf, inf], optional)
classmethod blend_pose_from_action ( action , * , blend_factor = 1.0 , evaluation_time = 0.0 )

Evaluate the supplied action at a chosen time and mix it into this pose. Affects only the selected bones, or every bone when nothing is selected.

Parameters :

- action (Action) – Action, The Action that holds the pose

- blend_factor ( float ) – Blend Factor, Degree to which the Action sways the resulting pose (in [0, 1], optional)

- evaluation_time ( float ) – Evaluation Time, The time at which the action is sampled to read off the pose (in [-inf, inf], optional)
classmethod backup_create ( action )

Save the current pose as a backup. Only bones animated in the Action are captured. The backup belongs to the object, which may hold just one at a time; release it with backup_clear() once it is no longer needed.

Parameters :

action (Action) – Action, An Action carrying animation for the bones. Only animated bones go into the backup.
classmethod backup_restore ( )

Reapply the pose backup taken earlier. It may be invoked repeatedly. Refer to Pose.backup_create() for details.

Returns :

True once the backup is reapplied, False when none exists to reapply

Return type :

bool
classmethod backup_clear ( )

Discard a pose backup made earlier. Refer to Pose.backup_create() for details.
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
| Object.pose | |

[Related references](INDEX.md).

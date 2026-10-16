# bpy.types.Action: methods

deselect_keys()

Clear selection on all keys of the Action. F-Curve selection remains unaffected.
fcurve_ensure_for_datablock(datablock, data_path, *, index=0, group_name='')

Guarantee that an F-Curve exists for the given property path and index on the given data-block. This action must already be linked to the data-block. The function creates the layer, keyframe strip, and action slot automatically if needed, and assigns the action slot.

Parameters:

- datablock (ID) – The data-block animated by this action, for which to ensure the F-Curve exists. This action must already be assigned to the data-block (never None)

- data_path (str) – Property path for the F-Curve (never None)

- index (int) – Array index ([0, inf], optional)

- group_name (str) – Name of the group to host this F-Curve if it is newly created. Ignored if the F-Curve already exists (optional, never None)

Returns: The found or created F-Curve

Return type: FCurve
flip_with_pose(object)

Reflect the action around the X axis using a pose

Parameters:

object (Object) – The reference armature object to use when flipping (never None)
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:

- id (str) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns: The RNA type or default when not found.

Return type: bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:

- id (str) – The RNA type identifier.

- default (type | None) – The value to return when not found.

Returns: The class or default when not found.

Return type: type
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data ID.name ID.name_full ID.id_type ID.session_uid ID.is_evaluated ID.original ID.users ID.use_fake_user ID.use_extra_user ID.is_embedded_data | ID.is_linked_packed ID.is_missing ID.is_runtime_data ID.is_editable ID.tag ID.is_library_indirect ID.library ID.library_weak_reference ID.asset_data ID.override_library ID.preview |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors | bpy_struct.type_recast bpy_struct.values ID.bl_system_properties_get ID.rename ID.evaluated_get ID.copy ID.asset_mark ID.asset_clear ID.asset_generate_preview ID.override_create ID.override_hierarchy_create ID.user_clear ID.user_remap ID.make_local ID.user_of_id ID.animation_data_create ID.animation_data_clear ID.update_tag ID.preview_ensure ID.bl_rna_get_subclass ID.bl_rna_get_subclass_py |
### References

| Members | Members |
| --- | --- |
| bpy.context.active_action bpy.context.selected_editable_actions bpy.context.selected_visible_actions ActionConstraint.action AnimData.action AnimData.action_tweak_storage BlendData.actions BlendDataActions.new | BlendDataActions.remove GLTF2_filter_action.action NlaStrip.action NlaStrips.new Pose.apply_pose_from_action Pose.backup_create Pose.blend_pose_from_action WindowManager.poselib_previous_action |

[Related references](INDEX.md).

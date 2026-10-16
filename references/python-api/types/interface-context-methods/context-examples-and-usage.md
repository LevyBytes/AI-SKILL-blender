# bpy.types.Context: Methods: Inherited Properties, Inherited Functions, References, Type overview

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
| AssetShelf.draw_context_menu AssetShelf.poll FileHandler.poll_drop Gizmo.draw Gizmo.draw_select Gizmo.exit Gizmo.invoke Gizmo.modal Gizmo.test_select GizmoGroup.draw_prepare GizmoGroup.invoke_prepare GizmoGroup.poll GizmoGroup.refresh GizmoGroup.setup Header.draw KeyingSetInfo.generate KeyingSetInfo.iterator KeyingSetInfo.poll Macro.draw Macro.poll Menu.draw Menu.poll Node.draw_buttons Node.draw_buttons_ext Node.init Node.socket_value_update NodeInternal.draw_buttons NodeInternal.draw_buttons_ext NodeSocket.draw NodeSocket.draw_color NodeSocketStandard.draw NodeSocketStandard.draw_color NodeTree.get_from_context NodeTree.interface_update NodeTree.poll NodeTreeInterfaceSocket.draw NodeTreeInterfaceSocketBool.draw NodeTreeInterfaceSocketBundle.draw NodeTreeInterfaceSocketClosure.draw NodeTreeInterfaceSocketCollection.draw NodeTreeInterfaceSocketColor.draw NodeTreeInterfaceSocketFloat.draw NodeTreeInterfaceSocketFloatAngle.draw NodeTreeInterfaceSocketFloatColorTemperature.draw NodeTreeInterfaceSocketFloatDistance.draw NodeTreeInterfaceSocketFloatFactor.draw NodeTreeInterfaceSocketFloatFrequency.draw NodeTreeInterfaceSocketFloatMass.draw NodeTreeInterfaceSocketFloatPercentage.draw NodeTreeInterfaceSocketFloatTime.draw NodeTreeInterfaceSocketFloatTimeAbsolute.draw NodeTreeInterfaceSocketFloatUnsigned.draw NodeTreeInterfaceSocketFloatWavelength.draw NodeTreeInterfaceSocketGeometry.draw NodeTreeInterfaceSocketImage.draw NodeTreeInterfaceSocketInt.draw NodeTreeInterfaceSocketIntFactor.draw NodeTreeInterfaceSocketIntPercentage.draw NodeTreeInterfaceSocketIntUnsigned.draw NodeTreeInterfaceSocketMaterial.draw NodeTreeInterfaceSocketMatrix.draw NodeTreeInterfaceSocketMenu.draw NodeTreeInterfaceSocketObject.draw NodeTreeInterfaceSocketRotation.draw | NodeTreeInterfaceSocketShader.draw NodeTreeInterfaceSocketString.draw NodeTreeInterfaceSocketStringFilePath.draw NodeTreeInterfaceSocketTexture.draw NodeTreeInterfaceSocketVector.draw NodeTreeInterfaceSocketVector2D.draw NodeTreeInterfaceSocketVector4D.draw NodeTreeInterfaceSocketVectorAcceleration.draw NodeTreeInterfaceSocketVectorAcceleration2D.draw NodeTreeInterfaceSocketVectorAcceleration4D.draw NodeTreeInterfaceSocketVectorDirection.draw NodeTreeInterfaceSocketVectorDirection2D.draw NodeTreeInterfaceSocketVectorDirection4D.draw NodeTreeInterfaceSocketVectorEuler.draw NodeTreeInterfaceSocketVectorEuler2D.draw NodeTreeInterfaceSocketVectorEuler4D.draw NodeTreeInterfaceSocketVectorFactor.draw NodeTreeInterfaceSocketVectorFactor2D.draw NodeTreeInterfaceSocketVectorFactor4D.draw NodeTreeInterfaceSocketVectorPercentage.draw NodeTreeInterfaceSocketVectorPercentage2D.draw NodeTreeInterfaceSocketVectorPercentage4D.draw NodeTreeInterfaceSocketVectorTranslation.draw NodeTreeInterfaceSocketVectorTranslation2D.draw NodeTreeInterfaceSocketVectorTranslation4D.draw NodeTreeInterfaceSocketVectorVelocity.draw NodeTreeInterfaceSocketVectorVelocity2D.draw NodeTreeInterfaceSocketVectorVelocity4D.draw NodeTreeInterfaceSocketVectorXYZ.draw NodeTreeInterfaceSocketVectorXYZ2D.draw NodeTreeInterfaceSocketVectorXYZ4D.draw Operator.cancel Operator.check Operator.description Operator.draw Operator.execute Operator.invoke Operator.modal Operator.poll Panel.draw Panel.draw_header Panel.draw_header_preset Panel.poll RenderEngine.draw RenderEngine.view_draw RenderEngine.view_update UIList.draw_filter UIList.draw_item UIList.filter_items XrSessionState.action_binding_create XrSessionState.action_create XrSessionState.action_set_create XrSessionState.action_state_get XrSessionState.active_action_set_set XrSessionState.controller_aim_location_get XrSessionState.controller_aim_rotation_get XrSessionState.controller_grip_location_get XrSessionState.controller_grip_rotation_get XrSessionState.controller_pose_actions_set XrSessionState.haptic_action_apply XrSessionState.haptic_action_stop XrSessionState.is_running XrSessionState.reset_to_base_pose |
Logging Context Member Access

To record which members are touched, call logging_set(True) on the object returned by the "with" of a temporary override.
It prints out the members accessed over the course of the operation, which can be handy for working out which members still need overriding.

When an operator refuses to run because a context member is absent, this logging can point you at the missing one.

The snippet below records which context members get read.
The log lines go to your system console.

Important

Some operators don't consult Context Members at all, so bpy.types.Context.temp_override leaves them unaffected; lean on logging to find which members, if any, are read.

```python
import bpy
from bpy import context

my_objects = [context.scene.camera]

with context.temp_override(selected_objects=my_objects) as override:
    override.logging_set(
        True,  # Enable logging.
        hide_missing=True,  # Don't show failed attempts.
    )
    bpy.ops.object.delete()
```

[Related references](INDEX.md).

# bpy.types.FCurve: inheritance

## FCurve(bpy_struct)

### FCurve(bpy_struct)

base class — bpy_struct
class bpy.types. FCurve ( bpy_struct )

A function curve that drives a value over a span of time.
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data | |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Members | Members |
| --- | --- |
| bpy.context.active_editable_fcurve bpy.context.editable_fcurves bpy.context.selected_editable_fcurves bpy.context.selected_visible_fcurves bpy.context.visible_fcurves Action.fcurve_ensure_for_datablock ActionChannelbag.fcurves ActionChannelbagFCurves.ensure ActionChannelbagFCurves.find ActionChannelbagFCurves.new ActionChannelbagFCurves.new_from_fcurve | ActionChannelbagFCurves.new_from_fcurve ActionChannelbagFCurves.remove ActionGroup.channels AnimData.drivers AnimDataDrivers.find AnimDataDrivers.from_existing AnimDataDrivers.from_existing AnimDataDrivers.new AnimDataDrivers.remove NlaStrip.fcurves NlaStripFCurves.find |

[Related references](INDEX.md).

# bpy.types.ColorManagedDisplaySettings

display_device

Name of the display. When viewing, it sets the display device that gets emulated by clamping the gamut and HDR colors; for image and video output, it sets the display space used when writing. (default 'NONE' )

Type :

Literal[‘NONE’]
emulation

Determines how images in the selected display map onto the physical screen (default 'AUTO' )

- OFF
Off – Send the image straight out as OpenColorIO produced it. Generally incorrect, but usable when the system setup and real display device are known to line up with the selected display.

- AUTO
Automatic – Show images the way most other applications do, for previewing images and video before export. Best effort is made to emulate the selected display on the real display device.

Type :

Literal[‘OFF’, ‘AUTO’]
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
| CompositorNodeConvertToDisplay.display_settings ImageFormatSettings.display_settings | Scene.display_settings |
## ColorManagedDisplaySettings(bpy_struct)

### ColorManagedDisplaySettings(bpy_struct)

base class: bpy_struct
class bpy.types. ColorManagedDisplaySettings ( bpy_struct )

Color management settings that are particular to a display device

[Related references](INDEX.md).

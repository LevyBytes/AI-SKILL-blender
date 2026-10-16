# bpy.types.ActionKeyframeStrip

channelbags

(default None, readonly)

Type: ActionChannelbags[ActionChannelbag]
channelbag(slot, *, ensure=False)

Locate the ActionChannelbag for a specified Slot

Parameters:

- slot (ActionSlot) – Slot, The slot for which to locate the channelbag

- ensure (bool) – Create if necessary, Guarantee the channelbag exists for this slot, creating it if needed (optional)

Returns: Channels

Return type: ActionChannelbag
key_insert(slot, data_path, array_index, value, time)

key_insert

Parameters:

- slot (ActionSlot) – Slot, The slot that identifies which 'thing' should be keyed

- data_path (str) – Data Path, F-Curve data path (never None)

- array_index (int) – Array Index, Index of the animated array element, or -1 if the property is not an array ([-inf, inf])

- value (float) – Value to key, Value of the animated property ([-inf, inf])

- time (float) – Time of the key, Time, in frames, of the key ([-inf, inf])

Returns: Success, Whether the key was successfully inserted

Return type: bool
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
| bpy_struct.id_data | ActionStrip.type |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values ActionStrip.bl_rna_get_subclass ActionStrip.bl_rna_get_subclass_py |
## ActionKeyframeStrip(ActionStrip)

### ActionKeyframeStrip(ActionStrip)

base classes — bpy_struct, ActionStrip
class bpy.types.ActionKeyframeStrip(ActionStrip)

A strip holding F-Curves for each action slot

[Related references](INDEX.md).

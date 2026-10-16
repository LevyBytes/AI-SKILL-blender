# bpy.types.CurveProfile: methods

update ( )

Refresh the internal data, merge any doubles, and clip the points
reset_view ( )

Set the curve profile grid back to match its clipping size
initialize ( totsegments )

Choose how many display segments there are and populate the tables

Parameters :

totsegments ( int ) – The number of segment values to initialize the segments table with (in [1, 1000], never None)
evaluate ( length_portion )

Evaluate the at the given portion of the path length

Parameters :

length_portion ( float ) – Length Portion, Portion of the path length to travel before evaluation (in [0, 1])

Returns :

Location, The location at the given portion of the profile (array of 2 items, in [-100, 100])

Return type :

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
| BevelModifier.custom_profile Curve.bevel_profile | ToolSettings.custom_bevel_profile_preset |

[Related references](INDEX.md).

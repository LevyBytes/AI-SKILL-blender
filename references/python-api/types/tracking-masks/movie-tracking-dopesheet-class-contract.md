# bpy.types.MovieTrackingDopesheet - class-contract, Inherited Properties, Inherited Functions, References, MovieTrackingDopesheet(bpy_struct)

show_hidden

Bring in channels from objects or bones that are not visible (default False)

Type :

bool
show_only_selected

Limit channels to those of the selected objects and data (default False)

Type :

bool
sort_method

Which ordering applies to channels in the dopesheet view (default 'NAME' )

- NAME
Name – Sort channels by their names.

- LONGEST
Longest – Sort channels by longest tracked segment.

- TOTAL
Total – Sort channels by overall amount of tracked segments.

- `AVERAGE_ERROR`
Average Error – Sort channels by average reprojection error of tracks after solve.

- START
Start Frame – Sort channels by first frame number.

- END
End Frame – Sort channels by last frame number.

Type :

Literal[‘NAME’, ‘LONGEST’, ‘TOTAL’, ‘`AVERAGE_ERROR`’, ‘START’, ‘END’]
use_invert_sort

Reverse the dopesheet channel ordering (default False)

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
| bpy_struct.id_data | |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Description | Description |
| --- | --- |
| MovieTracking.dopesheet | |
## MovieTrackingDopesheet(bpy_struct)

[Related references](INDEX.md).

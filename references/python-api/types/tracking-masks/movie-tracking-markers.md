# bpy.types.MovieTrackingMarkers

find_frame ( frame , * , exact = True )

Get marker for specified frame

Parameters :

- frame ( int ) – Frame, Frame number to find marker for (in [0, 1048574])

- exact ( bool ) – Exact, Get marker at exact frame number rather than get estimated marker (optional)

Returns :

Marker for specified frame

Return type :

MovieTrackingMarker
insert_frame ( frame , * , co = (0.0, 0.0) )

Insert a new marker at the specified frame

Parameters :

- frame ( int ) – Frame, Frame number to insert marker to (in [0, 1048574])

- co (mathutils.Vector) – Coordinate, Place new marker at the given frame using specified in normalized space coordinates (array of 2 items, in [-1, 1], optional)

Returns :

Newly created marker

Return type :

MovieTrackingMarker
delete_frame ( frame )

Delete marker at specified frame

Parameters :

frame ( int ) – Frame, Frame number to delete marker from (in [0, 1048574])
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
| MovieTrackingTrack.markers | |
## MovieTrackingMarkers(bpy_prop_collection)

### MovieTrackingMarkers(bpy_prop_collection)

base classes: bpy_prop, bpy_prop_collection
class bpy.types. MovieTrackingMarkers ( bpy_prop_collection )

Set of markers attached to a movie-tracking track

[Related references](INDEX.md).

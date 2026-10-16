# bpy.types.BlendDataPointClouds

new(name)

Registers a newly-created point cloud in Blender's database.

Parameters:
- name (str) – Point cloud identifier (cannot be None)

Returns:
New point cloud data-block

Return type:
PointCloud
remove(pointcloud, *, do_unlink=True, do_id_user=True, do_ui_user=True)

Eliminates a point cloud from the current blend file.

Parameters:
- pointcloud (PointCloud) – Point cloud to delete (cannot be None)
- do_unlink (bool) – Break all linkages to this cloud before deletion (WARNING: will also delete objects instancing that point cloud data) (optional)
- do_id_user (bool) – Decrement counters in all dependent data-blocks (optional)
- do_ui_user (bool) – Purge UI references (optional)
tag(value)

Tag with metadata.

Parameters:
- value (bool) – Tag state
classmethod bl_rna_get_subclass(id, default=None, /)

Parameters:
- id (str) – RNA class identifier.
- default (bpy.types.Struct | None) – Default response.

Returns:
The RNA type or default.

Return type:
bpy.types.Struct
classmethod bl_rna_get_subclass_py(id, default=None, /)

Parameters:
- id (str) – RNA class identifier.
- default (type | None) – Default response.

Returns:
The class or default.

Return type:
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
| BlendData.pointclouds | |
## BlendDataPointClouds(bpy_prop_collection)

### BlendDataPointClouds(bpy_prop_collection)

base classes — bpy_prop, bpy_prop_collection
class bpy.types.BlendDataPointClouds(bpy_prop_collection)

Houses a collection of point cloud data structures.

[Related references](INDEX.md).

# bpy.types.GeometrySet: methods

instance_references ( )

Returns the list of geometries that the .reference_index attribute on the pointcloud from bpy.types.GeometrySet.instances_pointcloud() points into. Entries may be other geometry sets, objects, collections, or None.

Return type :

list[None | bpy.types.Object | bpy.types.Collection | bpy.types.GeometrySet]
instances_pointcloud ( )

Hands back a pointcloud describing the geometry’s instances, which you should treat as read-only. Each instance gets one point, and its per-instance data lives in the point attributes. Local transforms are kept in the instance_transform attribute, and the .reference_index attribute names what each point instances by indexing into the list from bpy.types.GeometrySet.instance_references() .

Return type :

bpy.types.PointCloud
static from_evaluated_object ( evaluated_object )

Produces a geometry set out of an evaluated object’s evaluated geometry; usually bpy.types.Object.evaluated_geometry() is the handier route.

Parameters :

evaluated_object (bpy.types.Object) – The object, already evaluated, that the geometry set is built from.

[Related references](INDEX.md).

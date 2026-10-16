# bpy_extras.view3d_utils: methods

bpy_extras.view3d_utils. region_2d_to_vector_3d ( region , rv3d , coord ) 

Give back a direction vector from the viewport at the given 2D region
coordinate.

Parameters :

- region (bpy.types.Region) – region of the 3D viewport, typically bpy.context.region.

- rv3d (bpy.types.RegionView3D) – 3D region data, typically bpy.context.space_data.region_3d.

- coord ( Sequence [ float ] ) – 2D coordinates relative to the region:
(event.mouse_region_x, event.mouse_region_y) for example.

Returns :

normalized 3D vector.

Return type :
bpy_extras.view3d_utils. region_2d_to_origin_3d ( region , rv3d , coord , * , clamp = None ) 

Give back the 3D view origin from region-relative 2D coords.

Note

Orthographic views have a less obvious origin,
the far clip is used to define the viewport near/far extents.
Since far clip can be a very large value,
the result may have numeric precision issues.

To avoid this problem, you can optionally clamp the far clip to a
smaller value based on the data you're operating on.

Parameters :

- region (bpy.types.Region) – region of the 3D viewport, typically bpy.context.region.

- rv3d (bpy.types.RegionView3D) – 3D region data, typically bpy.context.space_data.region_3d.

- coord ( Sequence [ float ] ) – 2D coordinates relative to the region;
(event.mouse_region_x, event.mouse_region_y) for example.

- clamp ( float | None ) – Clamp the maximum far-clip value used.
(negative value will move the offset away from the view_location)

Returns :

The origin of the viewpoint in 3D space.

Return type :
bpy_extras.view3d_utils. region_2d_to_location_3d ( region , rv3d , coord , depth_location ) 

Give back a 3D location from region-relative 2D coords, lined up with
depth_location .

Parameters :

- region (bpy.types.Region) – region of the 3D viewport, typically bpy.context.region.

- rv3d (bpy.types.RegionView3D) – 3D region data, typically bpy.context.space_data.region_3d.

- coord ( Sequence [ float ] ) – 2D coordinates relative to the region;
(event.mouse_region_x, event.mouse_region_y) for example.

- depth_location (mathutils.Vector) – the returned vectors depth is aligned with this since
there is no defined depth with a 2D region input.

Returns :

normalized 3D vector.

Return type :
bpy_extras.view3d_utils. location_3d_to_region_2d ( region , rv3d , coord , * , default = None ) 

Give back the region-relative 2D location of a 3D position.

Parameters :

- region (bpy.types.Region) – region of the 3D viewport, typically bpy.context.region.

- rv3d (bpy.types.RegionView3D) – 3D region data, typically bpy.context.space_data.region_3d.

- coord (mathutils.Vector) – 3D world-space location.

- default ( Any ) – Return this value if coord
is behind the origin of a perspective view.

Returns :

2D location

Return type :

mathutils.Vector | Any

[Related references](INDEX.md).

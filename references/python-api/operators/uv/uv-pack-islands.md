# bpy.ops.uv.pack_islands

bpy.ops.uv. pack_islands ( * , udim_source = '`CLOSEST_UDIM`' , rotate = True , rotate_method = 'ANY' , scale = True , merge_overlap = False , margin_method = 'SCALED' , margin = 0.001 , pin = False , pin_method = 'LOCKED' , shape_method = 'CONCAVE' ) 

Reshapes every island so the UV/UDIM space is filled as completely as possible

Parameters :

- udim_source ( Literal [ '`CLOSEST_UDIM`' , '`ACTIVE_UDIM`' , '`ORIGINAL_AABB`' , '`CUSTOM_REGION`' ] ) – Pack to, (optional)

- `CLOSEST_UDIM`
Closest UDIM – Send islands to the nearest UDIM.

- `ACTIVE_UDIM`
Active UDIM – Send islands to the active UDIM image tile or to the UDIM grid tile under the 2D cursor.

- `ORIGINAL_AABB`
Original bounding box – Pack within the islands' starting bounding box.

- `CUSTOM_REGION`
Custom Region – Send islands into a custom region.

- rotate ( bool ) – Rotate, Rotate islands to improve layout (optional)

- rotate_method ( Literal [ 'ANY' , 'CARDINAL' , '`AXIS_ALIGNED`' , '`AXIS_ALIGNED_X`' , '`AXIS_ALIGNED_Y`' ] ) – Rotation Method, (optional)

- ANY
Any – Permit rotation at any angle.

- CARDINAL
Cardinal – Permit only 90-degree turns.

- `AXIS_ALIGNED`
Axis-aligned – Turned to its tightest rectangle, vertical or horizontal.

- `AXIS_ALIGNED_X`
Axis-aligned (Horizontal) – Turn islands so they line up horizontally.

- `AXIS_ALIGNED_Y`
Axis-aligned (Vertical) – Turn islands so they line up vertically.

- scale ( bool ) – Scale, Scale islands to fill unit square (optional)

- merge_overlap ( bool ) – Merge Overlapping, Overlapping islands stick together (optional)

- margin_method ( Literal [ 'SCALED' , 'ADD' , 'FRACTION' ] ) – Margin Method, (optional)

- SCALED
Scaled – Multiply the margin by the existing UV scale.

- ADD
Add – Apply the margin straight, disregarding UV scale.

- FRACTION
Fraction – Give an exact fraction of the final UV output.

- margin ( float ) – Margin, Space between islands (in [0, 1], optional)

- pin ( bool ) – Lock Pinned Islands, Constrain islands containing any pinned UV’s (optional)

- pin_method ( Literal [ 'SCALE' , 'ROTATION' , '`ROTATION_SCALE`' , 'LOCKED' ] ) – Pin Method, (optional)

- SCALE
Scale – Keep pinned islands from rescaling.

- ROTATION
Rotation – Keep pinned islands from rotating.

- `ROTATION_SCALE`
Rotation and Scale – Let pinned islands only translate.

- LOCKED
All – Hold pinned islands fixed in place.

- shape_method ( Literal [ 'CONCAVE' , 'CONVEX' , 'AABB' ] ) – Shape Method, (optional)

- CONCAVE
Exact Shape (Concave) – Work from the exact geometry.

- CONVEX
Boundary Shape (Convex) – Work from the convex hull.

- AABB
Bounding Box – Work from bounding boxes.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

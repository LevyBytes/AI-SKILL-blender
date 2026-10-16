# bpy.ops.object.origin_set

bpy.ops.object. origin_set ( * , type = '`GEOMETRY_ORIGIN`' , center = 'MEDIAN' ) 

Position the object's origin point, either by moving the data or repositioning to data bounds or 3D cursor

Parameters :

- type ( Literal [ '`GEOMETRY_ORIGIN`' , '`ORIGIN_GEOMETRY`' , '`ORIGIN_CURSOR`' , '`ORIGIN_CENTER_OF_MASS`' , '`ORIGIN_CENTER_OF_VOLUME`' ] ) – Type, (optional)

- `GEOMETRY_ORIGIN`
Geometry to Origin – Relocate geometry to the object origin.

- `ORIGIN_GEOMETRY`
Origin to Geometry – Set origin to the geometric center (using the chosen pivot standard or bounding envelope).

- `ORIGIN_CURSOR`
Origin to 3D Cursor – Place the object origin where the 3D cursor is positioned.

- `ORIGIN_CENTER_OF_MASS`
Origin to Center of Mass (Surface) – Calculate the point of equal weight using surface area.

- `ORIGIN_CENTER_OF_VOLUME`
Origin to Center of Mass (Volume) – Calculate the point of equal weight using enclosed volume (requires closed geometry).

- center ( Literal [ 'MEDIAN' , 'BOUNDS' ] ) – Center, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

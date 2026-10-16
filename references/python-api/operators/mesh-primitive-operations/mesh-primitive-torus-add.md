# bpy.ops.mesh.primitive_torus_add

bpy.ops.mesh. primitive_torus_add ( * , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , major_segments = 48 , minor_segments = 12 , mode = '`MAJOR_MINOR`' , major_radius = 1.0 , minor_radius = 0.25 , abso_major_rad = 1.25 , abso_minor_rad = 0.75 , generate_uvs = True )

Build a donut-shaped mesh

Parameters :

- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, (optional)

- WORLD
World – Align the new object to the world.

- VIEW
View – Align the new object to the view.

- CURSOR
3D Cursor – Use the 3D cursor orientation for the new object.

- location (mathutils.Vector) – Location, (array of 3 items, in [-inf, inf], optional)

- rotation (mathutils.Euler) – Rotation, (array of 3 items, in [-inf, inf], optional)

- major_segments ( int ) – Major Segments, Number of segments for the main ring of the torus (in [3, 256], optional)

- minor_segments ( int ) – Minor Segments, Number of segments for the minor ring of the torus (in [3, 256], optional)

- mode ( Literal [ '`MAJOR_MINOR`' , '`EXT_INT`' ] ) – Dimensions Mode, (optional)

- `MAJOR_MINOR`
Major/Minor – Use the major/minor radii for torus dimensions.

- `EXT_INT`
Exterior/Interior – Use the exterior/interior radii for torus dimensions.

- major_radius ( float ) – Major Radius, Radius from the origin to the center of the cross sections (in [0, 10000], optional)

- minor_radius ( float ) – Minor Radius, Radius of the torus's cross section (in [0, 10000], optional)

- abso_major_rad ( float ) – Exterior Radius, Total Exterior Radius of the torus (in [0, 10000], optional)

- abso_minor_rad ( float ) – Interior Radius, Total Interior Radius of the torus (in [0, 10000], optional)

- generate_uvs ( bool ) – Generate UVs, Generate a default UV map (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/add_mesh_torus.py:222

[Related references](INDEX.md).

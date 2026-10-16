# bpy.ops.mesh.primitive_uv_sphere_add

bpy.ops.mesh. primitive_uv_sphere_add ( * , segments = 32 , ring_count = 16 , radius = 1.0 , calc_uvs = True , enter_editmode = False , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) )

Build a ball-like mesh with quad faces, with triangular faces at the pole zones

Parameters :

- segments ( int ) – Segments, (in [3, 100000], optional)

- ring_count ( int ) – Rings, (in [3, 100000], optional)

- radius ( float ) – Radius, (in [0, inf], optional)

- calc_uvs ( bool ) – Generate UVs, Generate a default UV map (optional)

- enter_editmode ( bool ) – Enter Edit Mode, Enter edit mode when adding this object (optional)

- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, The alignment of the new object (optional)

- WORLD
World – Align the new object to the world.

- VIEW
View – Align the new object to the view.

- CURSOR
3D Cursor – Use the 3D cursor orientation for the new object.

- location (mathutils.Vector) – Location, Location for the newly added object (array of 3 items, in [-inf, inf], optional)

- rotation (mathutils.Euler) – Rotation, Rotation for the newly added object (array of 3 items, in [-inf, inf], optional)

- scale (mathutils.Vector) – Scale, Scale for the newly added object (array of 3 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

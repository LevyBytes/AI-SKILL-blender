# bpy.ops.mesh.primitive_cylinder_add

bpy.ops.mesh. primitive_cylinder_add ( * , vertices = 32 , radius = 1.0 , depth = 2.0 , end_fill_type = 'NGON' , calc_uvs = True , enter_editmode = False , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) )

Build a tubular mesh

Parameters :

- vertices ( int ) – Vertices, (in [3, 10000000], optional)

- radius ( float ) – Radius, (in [0, inf], optional)

- depth ( float ) – Depth, (in [0, inf], optional)

- end_fill_type ( Literal [ 'NOTHING' , 'NGON' , 'TRIFAN' ] ) – Cap Fill Type, (optional)

- NOTHING
Nothing – Don't fill at all.

- NGON
N-Gon – Use n-gons.

- TRIFAN
Triangle Fan – Use triangle fans.

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

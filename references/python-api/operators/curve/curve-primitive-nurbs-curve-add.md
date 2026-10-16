# bpy.ops.curve.primitive_nurbs_curve_add

**bpy.ops.curve.primitive_nurbs_curve_add**( * , radius = 1.0 , enter_editmode = False , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) )

Insert a new NURBS spline.

Parameters:
- radius ( float ) – Radius, (in [0, inf], optional)
- enter_editmode ( bool ) – Enter Edit Mode, Enter edit mode when adding this object (optional)
- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, The alignment of the new object (optional)

- WORLD
World – Align the new object to the world.

- VIEW
View – Align the new object to the view.

- CURSOR
3D Cursor – Use the 3D cursor orientation for the new object.

- location (mathutils.Vector) – Location, Position for the new object (array of 3 items, in [-inf, inf], optional)
- rotation (mathutils.Euler) – Rotation, Orientation for the new object (array of 3 items, in [-inf, inf], optional)
- scale (mathutils.Vector) – Scale, Size for the new object (array of 3 items, in [-inf, inf], optional)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).

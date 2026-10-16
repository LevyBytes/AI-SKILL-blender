# bpy.ops.mesh.point_normals

bpy.ops.mesh. point_normals ( * , mode = 'COORDINATES' , invert = False , align = False , target_location = (0.0, 0.0, 0.0) , spherize = False , spherize_strength = 0.1 )

Orient picked custom normals toward a definite Focal Point

Parameters :

- mode ( Literal [ 'COORDINATES' , 'MOUSE' ] ) – Mode, How to define coordinates to point custom normals to (optional)

- COORDINATES
Coordinates – Use static coordinates (defined by various means).

- MOUSE
Mouse – Follow mouse cursor.

- invert ( bool ) – Invert, Invert affected normals (optional)

- align ( bool ) – Align, Make all affected normals parallel (optional)

- target_location (mathutils.Vector) – Target, Target location to which normals will point (array of 3 items, in [-inf, inf], optional)

- spherize ( bool ) – Spherize, Interpolate between original and new normals (optional)

- spherize_strength ( float ) – Spherize Strength, Ratio of spherized normal to original normal (in [0, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# UV Warp Modifier

## UV Warp Modifier

### UV Warp Modifier

An object's UV map gets reshaped by the UV Warp modifier, drawing on either set values or a pair of objects. The aim is to hand you direct command of the object's UVs right inside the 3D Viewport, so the existing UV coordinates can be moved, rotated, and scaled using fixed values or a controller object or bone.

### Options

UV Map
Picks which UV map gets modified; left unset, it falls back to the active rendering layer.

UV Center
The point on the UV map that scaling or rotation pivots around,
where the bottom left reads (0, 0) and the top right reads (1, 1).

Axis U, V
Sets which axes carry the 3D coordinates as they're flattened into 2D.

Object From, To
The pair of objects that set the transformation. See Usage below.

Vertex Group
The vertex group serves to scale the transformation's influence on a per-vertex basis.

Invert
Flips which vertices the chosen vertex group covers, so the group instead
marks the vertices the modifier will leave undeformed.

The group's weight values are reversed by this setting.

### Transform

Offset
How far to shift the UV map.

Scale
How much to scale the UV map.

Rotation
How far to rotate the UV map.

### Usage

What warps the UVs is the mismatch in transform, that is location, rotation and scale,
separating the from object and the to object.

Should the to object carry the same transforms as the from object, the UVs stay put.

Take a UV Axis of X/Y on the modifier and object scales of (1, 1, 1): move the to object
a single unit from the from object along X, and the UVs shift on the U axis (horizontally)
across one whole UV space, the full width of the image.

[Related references](INDEX.md).

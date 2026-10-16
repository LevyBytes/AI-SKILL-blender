# Mapping Node

## Mapping Node

### Mapping Node

This node adjusts an input vector through translation, rotation, and scaling transformations.

### Inputs

Node inputs vary by configuration. The Location input appears only for Texture and Point vector interpretations.

Vector
The vector subject to transformation.

Location
Translation displacement along each axis.

Rotation
Rotation angle along each axis. XYZ order.

Scale
Scaling amount along each axis.

### Properties

Vector Type
The node applies the transformation based on the interpretation of the input vector.

Point :

The node performs a direct transformation.

Adjusting texture coordinates parallels adjusting a UV map. Moving texture coordinates in the positive X direction shifts the displayed texture in the negative X direction, similar to UV adjustment. Similarly, increasing texture coordinate values reduces the texture size. Coordinate transformation produces opposite visual effects compared to the texture itself.

Transformation order: Scale –> Rotate –> Translate, which means:

- Translation shifts the input along the local rotation axis.

- Rotation pivots the input around the origin.

- Scaling adjusts the input along the global axis.

Texture :

The node performs an opposite transformation.

Reverse-transforming texture coordinates, unlike Point mode, modifies the displayed texture directly. Moving texture coordinates in the positive X direction shifts the displayed texture in the positive X direction as expected. Similarly, raising texture coordinate values enlarges the texture as expected.

Transformation order: Translate –> Rotate –> Scale, which means:

- Translation shifts the input along the global axis.

- Rotation pivots the input around the translation vector.

- Scaling adjusts the input along the local rotation axis.

Vector :

The node applies a Point transformation without translation.

Normal :

The node performs the inverse transpose of the transformation and normalizes the result. This procedure ensures normals remain accurate under non-uniform scaling. Apply this type when transforming normals.

### Outputs

Vector
The input vector following transformation.

### Examples

Mapping node example.

[Related references](INDEX.md).

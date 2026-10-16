# Align Euler to Vector Node

## Align Euler to Vector Node

### Align Euler to Vector Node

Rotate an Euler rotation toward a given direction.

**Important:** This node is deprecated; use Align Rotation to Vector instead.

### Inputs

**Rotation**
Euler rotation to align.

**Important:** Provide a rotation input. Do not connect direction vectors like normals.

**Factor**
Rotation degree: zero disables; one aligns perfectly.

**Vector**
Direction vector for rotation.
Local space to the object being modified.
Zero vector: no rotation.

### Properties

**Axis**
Local object axis to rotate toward the vector.

**Pivot**
Rotation axis.

- **Auto:** Compute best angle automatically (minimize rotation).
- **X, Y, Z:** Rotate around specified axis.

### Outputs

**Rotation**
Rotated Euler output.

[Related references](INDEX.md).

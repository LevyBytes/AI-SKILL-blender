# bpy.types.Bone: MatrixFromAxisRoll

classmethod MatrixFromAxisRoll ( axis , roll )

Convert the axis + roll representation to a matrix

Parameters:
- axis (mathutils.Vector) – The main axis of the bone (tail - head) (array of 3 items, in [-inf, inf], never None)

- roll ( float ) – The roll of the bone (in [-inf, inf])

Returns:
The resulting orientation matrix (multi-dimensional array of 3 * 3 items, in [-inf, inf])

Return type:
mathutils.Matrix

[Related references](INDEX.md).

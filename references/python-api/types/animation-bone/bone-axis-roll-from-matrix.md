# bpy.types.Bone: AxisRollFromMatrix

classmethod AxisRollFromMatrix ( matrix , * , axis = (0.0, 0.0, 0.0) )

Convert a rotational matrix to the axis + roll representation. Note that the resulting value of the roll may not be as expected if the matrix has shear or negative determinant.

Parameters:
- matrix (mathutils.Matrix) – The orientation matrix of the bone (multi-dimensional array of 3 * 3 items, in [-inf, inf], never None)

- axis ( Sequence [ float ] ) – The optional override for the axis (finds closest approximation for the matrix) (array of 3 items, in [-inf, inf], optional)

Returns:
result_axis , The main axis of the bone, mathutils.Vector

result_roll , The roll of the bone, float

Return type:
tuple[mathutils.Vector, float]

[Related references](INDEX.md).

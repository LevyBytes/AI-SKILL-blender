# bpy.types.PoseBone: matrix, matrix_basis, matrix_channel

matrix

The final 4×4 matrix in armature object space, with constraints and drivers already applied (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

Type :

mathutils.Matrix
matrix_basis

A secondary way to reach location/scale/rotation relative to the parent and the bone's own rest pose (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)))

Type :

mathutils.Matrix
matrix_channel

4×4 matrix combining the bone's location/rotation/scale channels (animation and drivers included) together with the result of bone constraints (multi-dimensional array of 4 * 4 items, in [-inf, inf], default ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), readonly)

Type :

mathutils.Matrix

[Related references](INDEX.md).

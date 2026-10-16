# bpy.types.Bone: convert_local_to_pose

convert_local_to_pose ( matrix , matrix_local , * , parent_matrix = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)) , parent_matrix_local = ((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)) , invert = False )

Convert a matrix between Local and Pose space (in either direction), accounting for settings such as Inherit Scale and Local Location. In contrast to Object.convert_space, this relies on rest and pose matrices that the caller supplies. When the parent matrices are left out, the bone is treated as parentless.

Parameters:
- matrix (mathutils.Matrix) – The matrix to transform (multi-dimensional array of 4 * 4 items, in [-inf, inf])

- matrix_local (mathutils.Matrix) – The custom rest matrix of this bone (Bone.matrix_local) (multi-dimensional array of 4 * 4 items, in [-inf, inf])

- parent_matrix (mathutils.Matrix) – The custom pose matrix of the parent bone (PoseBone.matrix) (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)

- parent_matrix_local (mathutils.Matrix) – The custom rest matrix of the parent bone (Bone.matrix_local) (multi-dimensional array of 4 * 4 items, in [-inf, inf], optional)

- invert ( bool ) – Convert from Pose to Local space (optional)

Returns:
The transformed matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])

Return type:
mathutils.Matrix

With this method you can switch bones between Local and Pose space partway through an armature update, carrying refreshed matrices through a recursive traversal yourself, so dependencies need not be recomputed after every individual change.

```python
def set_pose_matrices(obj, matrix_map):
    "Assign pose space matrices of all bones at once, ignoring constraints."

    def rec(pbone, parent_matrix):
        if pbone.name in matrix_map:
            matrix = matrix_map[pbone.name]

            # # Instead of:
            # pbone.matrix = matrix
            # bpy.context.view_layer.update()

            # Compute and assign local matrix, using the new parent matrix.
            if pbone.parent:
                pbone.matrix_basis = pbone.bone.convert_local_to_pose(
                    matrix,
                    pbone.bone.matrix_local,
                    parent_matrix=parent_matrix,
                    parent_matrix_local=pbone.parent.bone.matrix_local,
                    invert=True
                )
            else:
                pbone.matrix_basis = pbone.bone.convert_local_to_pose(
                    matrix,
                    pbone.bone.matrix_local,
                    invert=True
                )
        else:
            # Compute the updated pose matrix from local and new parent matrix.
            if pbone.parent:
                matrix = pbone.bone.convert_local_to_pose(
                    pbone.matrix_basis,
                    pbone.bone.matrix_local,
                    parent_matrix=parent_matrix,
                    parent_matrix_local=pbone.parent.bone.matrix_local,
                )
            else:
                matrix = pbone.bone.convert_local_to_pose(
                    pbone.matrix_basis,
                    pbone.bone.matrix_local,
                )

        # Recursively process children, passing the new matrix through.
        for child in pbone.children:
            rec(child, matrix)

    # Scan all bone trees from their roots.
    for pbone in obj.pose.bones:
        if not pbone.parent:
            rec(pbone, None)
```

[Related references](INDEX.md).

# bpy.types.SplineIKConstraint: y_scale_mode

y_scale_mode

How scaling of the bones' Y axis is decided, layered onto the curve's own shape and scaling (default 'NONE' )

- NONE
None – Leave the Y axis unscaled.

- `FIT_CURVE`
Fit Curve – Scale the bones to span the full length of the curve.

- `BONE_ORIGINAL`
Bone Original – Keep the bone's original Y scale.

Type :

Literal[‘NONE’, ‘`FIT_CURVE`’, ‘`BONE_ORIGINAL`’]

[Related references](INDEX.md).

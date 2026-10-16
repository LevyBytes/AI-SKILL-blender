# bpy.types.SplineIKConstraint: xz_scale_mode

xz_scale_mode

How scaling of the bones' X and Z axes is decided (default 'NONE' )

- NONE
None – Leave the X and Z axes unscaled.

- `BONE_ORIGINAL`
Bone Original – Keep the bones' original scaling.

- `INVERSE_PRESERVE`
Inverse Scale – The X and Z axis scale becomes the inverse of the Y-Scale.

- `VOLUME_PRESERVE`
Volume Preservation – X and Z axis scale is tuned to keep the bones' volume.

Type :

Literal[‘NONE’, ‘`BONE_ORIGINAL`’, ‘`INVERSE_PRESERVE`’, ‘`VOLUME_PRESERVE`’]

[Related references](INDEX.md).

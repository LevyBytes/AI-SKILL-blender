# bpy.types.Bone: bbone_mapping_mode

bbone_mapping_mode

Chooses how vertices are matched to B-Bone segments according to where they sit (default 'STRAIGHT')

- STRAIGHT
Straight – Fast mapping that is good for most situations, but ignores the rest pose curvature of the B-Bone.

- CURVED
Curved – Slower mapping that gives better deformation for B-Bones that are sharply curved in rest pose.

Type:
Literal['STRAIGHT', 'CURVED']

[Related references](INDEX.md).

# bpy.types.EditBone: bbone_mapping_mode

bbone_mapping_mode

How vertices get assigned to B-Bone segments according to where they sit (default 'STRAIGHT' )

- STRAIGHT
Straight – A quick mapping that suits most cases but disregards the B-Bone’s rest-pose curvature.

- CURVED
Curved – A slower mapping that deforms B-Bones with heavy rest-pose curvature better.

Type :

Literal[‘STRAIGHT’, ‘CURVED’]

[Related references](INDEX.md).

# bpy.types.ClothSettings: bending_damping, bending_model, bending_stiffness, bending_stiffness_max

bending_damping

Damping for bending forces (in [0, 1000], default 0.5)

Type :

float
bending_model

Bending physics method (default 'ANGULAR' )

- ANGULAR
Angular – Cloth model with angular bending springs.

- LINEAR
Linear – Cloth model with linear bending springs (legacy).

Type :

Literal['ANGULAR', 'LINEAR']
bending_stiffness

Material rigidity against bending (in [0, 10000], default 0.5)

Type :

float
bending_stiffness_max

Upper limit for bending rigidity (in [0, 10000], default 0.5)

Type :

float

[Related references](INDEX.md).

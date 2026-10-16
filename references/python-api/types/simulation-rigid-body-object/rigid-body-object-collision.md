# bpy.types.RigidBodyObject: collision_collections, collision_margin, collision_shape

collision_collections

Collision collections this rigid body is part of (array of 20 items, default (False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))

Type :

bpy_prop_array[bool]
collision_margin

Distance band near the surface within which collisions still register; non-zero values give the best results (in [0, 1], default 0.04)

Type :

float
collision_shape

Shape used for the object's collisions in Rigid Body Simulations (default 'BOX' )

Type :

Literal[Rigidbody Object Shape Items]

[Related references](INDEX.md).

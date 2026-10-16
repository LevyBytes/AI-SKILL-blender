# bpy.types.PoseBone: compute_bbone_handles

compute_bbone_handles ( * , rest = False , ease = False , offsets = False )

Read back the vectors and rolls produced by the B-Bone's custom handles

Parameters :

- rest ( bool ) – Hand back the rest pose state (optional)

- ease ( bool ) – Fold in scaling taken from the ease values (optional)

- offsets ( bool ) – Fold in roll and curve offsets read from bone properties (optional)

Returns :

handle1 , The direction vector of the start handle in bone local space, mathutils.Vector

roll1 , Roll of the start handle, float

handle2 , The direction vector of the end handle in bone local space, mathutils.Vector

roll2 , Roll of the end handle, float

Return type :

tuple[mathutils.Vector, float, mathutils.Vector, float]

[Related references](INDEX.md).

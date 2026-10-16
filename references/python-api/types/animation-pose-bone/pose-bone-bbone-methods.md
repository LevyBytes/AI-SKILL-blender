# bpy.types.PoseBone: bbone_segment_index, bbone_segment_matrix

bbone_segment_index ( point )

From a vertex position, look up which B-Bone segment applies and how it blends

Parameters :

point (mathutils.Vector) – Point, The vertex's location in armature pose space (array of 3 items, in [-inf, inf])

Returns :

index , The index of the first segment joint affecting the point, int

blend_next , The blend factor between the given and the following joint, float

Return type :

tuple[int, float]
bbone_segment_matrix ( index , * , rest = False )

Look up the matrix at the joint between B-Bone segments, when one exists

Parameters :

- index ( int ) – The segment endpoint's index (in [0, inf])

- rest ( bool ) – Hand back the rest pose matrix (optional)

Returns :

The resulting matrix in bone local space (multi-dimensional array of 4 * 4 items, in [-inf, inf])

Return type :

mathutils.Matrix

The snippet below reproduces, via B-Bone segment matrices, the deformation that the Armature modifier or constraint would apply to a given bone (Preserve Volume off). All coordinates are handled in armature Pose space:

[Related references](INDEX.md).

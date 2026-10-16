# bpy.types.Brush: pose_deform_type, pose_ik_segments, pose_offset, pose_origin_type, pose_smooth_iterations

pose_deform_type

The kind of deformation the brush applies (default '`ROTATE_TWIST`' )

Type :

Literal['`ROTATE_TWIST`', '`SCALE_TRANSLATE`', '`SQUASH_STRETCH`']
pose_ik_segments

How many segments of the IK chain will bend the mesh (in [1, 20], default 1)

Type :

int
pose_offset

How far the pose origin sits from the brush radius (in [0, 2], default 0.0)

Type :

float
pose_origin_type

How the rotation origins for the brush's segments get chosen (default 'TOPOLOGY' )

- TOPOLOGY
Topology – Picks the rotation origin on its own, guided by the mesh's topology and shape.

- `FACE_SETS`
Face Sets – Builds one pose segment for each face set, beginning at the active one.

- `FACE_SETS_FK`
Face Sets FK – Mimics an FK deformation, using the face set beneath the cursor to control it.

Type :

Literal['TOPOLOGY', '`FACE_SETS`', '`FACE_SETS_FK`']
pose_smooth_iterations

Smoothing passes run once each vertex's pose factor is computed (in [0, 100], default 4)

Type :

int

[Related references](INDEX.md).

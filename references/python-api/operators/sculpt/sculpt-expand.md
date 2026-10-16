# bpy.ops.sculpt.expand

bpy.ops.sculpt. expand ( * , target = 'MASK' , falloff_type = 'GEODESIC' , invert = False , use_mask_preserve = False , use_falloff_gradient = False , use_modify_active = False , use_reposition_pivot = True , max_geodesic_move_preview = 10000 , use_auto_mask = False , normal_falloff_smooth = 2 )

Multi-purpose sculpt extend capability

Parameters :

- target ( Literal [ 'MASK' , '`FACE_SETS`' , 'COLOR' ] ) – Data Target, Which property receives modification during the extend operation (optional)

- falloff_type ( Literal [ 'GEODESIC' , 'TOPOLOGY' , '`TOPOLOGY_DIAGONALS`' , 'NORMALS' , 'SPHERICAL' , '`BOUNDARY_TOPOLOGY`' , '`BOUNDARY_FACE_SET`' , '`ACTIVE_FACE_SET`' ] ) – Falloff Type, Starting falloff characteristic of the extend operation (optional)

- invert ( bool ) – Invert, Flip the extend active areas (optional)

- use_mask_preserve ( bool ) – Preserve Previous, Keep the earlier condition of the target property (optional)

- use_falloff_gradient ( bool ) – Falloff Gradient, Extend applying a linear falloff (optional)

- use_modify_active ( bool ) – Modify Active, Alter the active face set rather than forming a fresh one (optional)

- use_reposition_pivot ( bool ) – Reposition Pivot, Shift the sculpt transform anchor to the limit of the extend active zone (optional)

- max_geodesic_move_preview ( int ) – Max Vertex Count for Geodesic Move Preview, Highest number of mesh vertices permitting geodesic falloff during anchor movement. Beyond this, falloff switches to spherical (in [0, inf], optional)

- use_auto_mask ( bool ) – Auto Create, Populate mask if no existing mask exists (optional)

- normal_falloff_smooth ( int ) – Normal Smooth, Softening iterations for normal falloff (in [0, 10], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

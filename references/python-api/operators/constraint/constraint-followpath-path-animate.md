# bpy.ops.constraint.followpath_path_animate

bpy.ops.constraint. followpath_path_animate ( * , constraint = '' , owner = 'OBJECT' , frame_start = 1 , length = 100 )

Establish a standard timeline progression for the path used by this constraint unless one is already in place

Parameters :

- constraint ( str ) – Constraint, Name of the constraint to edit (optional, never None)

- owner ( Literal [ 'OBJECT' , 'BONE' ] ) – Owner, The owner of this constraint (optional)

- OBJECT
Object – Edit a constraint on the active object.

- BONE
Bone – Edit a constraint on the active bone.

- frame_start ( int ) – Start Frame, First frame of path animation (in [-1048574, 1048574], optional)

- length ( int ) – Length, Number of frames that path animation should take (in [0, 1048574], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

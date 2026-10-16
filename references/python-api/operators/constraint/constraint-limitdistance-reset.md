# bpy.ops.constraint.limitdistance_reset

bpy.ops.constraint. limitdistance_reset ( * , constraint = '' , owner = 'OBJECT' )

Reinitialize the maximum span for Limit Distance Constraint

Parameters :

- constraint ( str ) – Constraint, Name of the constraint to edit (optional, never None)

- owner ( Literal [ 'OBJECT' , 'BONE' ] ) – Owner, The owner of this constraint (optional)

- OBJECT
Object – Edit a constraint on the active object.

- BONE
Bone – Edit a constraint on the active bone.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

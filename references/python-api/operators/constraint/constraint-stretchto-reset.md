# bpy.ops.constraint.stretchto_reset

bpy.ops.constraint. stretchto_reset ( * , constraint = '' , owner = 'OBJECT' )

Restore the standard distance of the skeletal part for Stretch To Constraint

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

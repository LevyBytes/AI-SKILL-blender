# bpy.ops.constraint.copy

bpy.ops.constraint. copy ( * , constraint = '' , owner = 'OBJECT' , report = False )

Reproduce constraint at the same location in the roster

Parameters :

- constraint ( str ) – Constraint, Name of the constraint to edit (optional, never None)

- owner ( Literal [ 'OBJECT' , 'BONE' ] ) – Owner, The owner of this constraint (optional)

- OBJECT
Object – Edit a constraint on the active object.

- BONE
Bone – Edit a constraint on the active bone.

- report ( bool ) – Report, Create a notification after the operation (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.constraint.move_to_index

bpy.ops.constraint. move_to_index ( * , constraint = '' , owner = 'OBJECT' , index = 0 )

Adjust the constraint's location in the catalog so evaluation follows the specified number of other constraints

Parameters :

- constraint ( str ) – Constraint, Name of the constraint to edit (optional, never None)

- owner ( Literal [ 'OBJECT' , 'BONE' ] ) – Owner, The owner of this constraint (optional)

- OBJECT
Object – Edit a constraint on the active object.

- BONE
Bone – Edit a constraint on the active bone.

- index ( int ) – Index, The index to move the constraint to (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

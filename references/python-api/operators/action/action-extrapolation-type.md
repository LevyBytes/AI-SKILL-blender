# bpy.ops.action.extrapolation_type

bpy.ops.action. extrapolation_type ( * , type = 'CONSTANT' )

Adjust how curves extend past their final keyframes.

Parameters :

type ( Literal [ 'CONSTANT' , 'LINEAR' , '`MAKE_CYCLIC`' , '`CLEAR_CYCLIC`' ] ) – Type, (optional)

- CONSTANT
Constant Extrapolation – Endpoint keyframe values carry forward.

- LINEAR
Linear Extrapolation – End segment slopes extend as straight lines past the endpoints.

- `MAKE_CYCLIC`
Make Cyclic (F-Modifier) – Insert Cycles modifier if absent.

- `CLEAR_CYCLIC`
Clear Cyclic (F-Modifier) – Discard Cycles modifier if no longer needed.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.graph.extrapolation_type

bpy.ops.graph.extrapolation_type(*, type='CONSTANT')

Configure reach technique for the chose trajectories

Parameters:

type (Literal['CONSTANT', 'LINEAR', '`MAKE_CYCLIC`', '`CLEAR_CYCLIC`']) – Type, (optional)

- CONSTANT
Constant Extrapolation – Principles on endpoint frames are maintained.

- LINEAR
Linear Extrapolation – Straight-mark incline of finish divisions are drawn out onward from the endpoint frames.

- `MAKE_CYCLIC`
Make Cyclic (F-Modifier) – Deposit Cycles filter if sole doesn't exist presently.

- `CLEAR_CYCLIC`
Clear Cyclic (F-Modifier) – Purge Cycles filter if not obliged subsequently.

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

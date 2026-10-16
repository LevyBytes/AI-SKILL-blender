# bpy.ops.graph.keyframe_insert

bpy.ops.graph.keyframe_insert(*, type='ALL')

Deposit frames for the given divisions

Parameters:

type (Literal['ALL', 'SEL', 'ACTIVE', '`CURSOR_ACTIVE`', '`CURSOR_SEL`']) – Type, (optional)

- ALL
All Channels – Deposit a frame on every obvious and editable trajectory utilizing every trajectory's live worth.

- SEL
Only Selected Channels – Deposit a frame on chose trajectories utilizing every trajectory's live worth.

- ACTIVE
Only Active F-Curve – Deposit a frame on the lively trajectory utilizing the trajectory's live worth.

- `CURSOR_ACTIVE`
Active Channels at Cursor – Deposit a frame for the lively trajectory at the arrow spot.

- `CURSOR_SEL`
Selected Channels at Cursor – Deposit a frame for the chose trajectories at the arrow spot.

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

# bpy.ops.graph.equalize_handles

bpy.ops.graph.equalize_handles(*, side='LEFT', handle_length=5.0, flatten=False)

Make certain the chose frames' grips possess proportional width, voluntarily generating them level. Automatic, Automatic Clamped, or Vector grip types shall be switched to Aligned

Parameters:

- side (Literal['LEFT', 'RIGHT', 'BOTH']) – Side, Face of the frames' Bezier grips to exert upon (optional)

- LEFT
Left – Even the chose frames' left grips.

- RIGHT
Right – Even the chose frames' right grips.

- BOTH
Both – Even each of a frame's grips.

- handle_length (float) – Handle Length, Width to construct the chose frames' Bezier grips (in [0.1, inf], optional)
- flatten (bool) – Flatten, Construct the worths of the chose frames' grips the same as their respective frames (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

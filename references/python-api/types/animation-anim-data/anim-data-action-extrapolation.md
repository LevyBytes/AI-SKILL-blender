# bpy.types.AnimData: action_extrapolation

action_extrapolation

Behavior past the Active Action's span (when evaluating with NLA) (default 'HOLD')

- NOTHING
Nothing – Stack has no effect outside its boundaries.

- HOLD
Hold – Maintain the first frame if no prior strips exist in the track, and always maintain the last frame.

- `HOLD_FORWARD`
Hold Forward – Maintain the last frame only.

Type: Literal['NOTHING', 'HOLD', '`HOLD_FORWARD`']

[Related references](INDEX.md).

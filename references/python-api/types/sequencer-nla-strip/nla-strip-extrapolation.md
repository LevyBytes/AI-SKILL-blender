# bpy.types.NlaStrip: extrapolation

extrapolation

What happens in the gaps that fall outside the strip's range (default 'HOLD' )

- NOTHING
Nothing – Strip has no influence past its extents.

- HOLD
Hold – Hold the first frame if no previous strips in track, and always hold last frame.

- `HOLD_FORWARD`
Hold Forward – Only hold last frame.

Type :

Literal[‘NOTHING’, ‘HOLD’, ‘`HOLD_FORWARD`’]

[Related references](INDEX.md).

# bpy.ops.sequencer.fades_add

bpy.ops.sequencer.fades_add(*, duration_seconds=1.0, type='`IN_OUT`')

Create or modify gradual level changes for audio or visual material.

Parameters:

- duration_seconds (float) – Fade Duration, Time span of the fade in seconds (in [0.01, inf], optional)
- type (Literal['`IN_OUT`', 'IN', 'OUT', '`CURSOR_FROM`', '`CURSOR_TO`']) – Fade Type, Direction and timing: entry, exit, both entry and exit, ending at, or beginning from the current frame. Defaults to both entry and exit (optional)
  - `IN_OUT`
    Fade In and Out – Gradually increase then decrease levels.
  - IN
    Fade In – Gradually increase levels.
  - OUT
    Fade Out – Gradually decrease levels.
  - `CURSOR_FROM`
    From Current Frame – Gradually decrease from now until the end of overlapping material.
  - `CURSOR_TO`
    To Current Frame – Gradually increase from material start until now.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

File:

startup/bl_operators/sequencer.py:216

[Related references](INDEX.md).

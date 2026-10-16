# bpy.types.Volume: sequence_mode

sequence_mode

How the frame sequence is played (default 'CLIP' )

- CLIP
Clip – Conceal any frames that fall outside the chosen range.

- EXTEND
Extend – Hold the first frame before the range and the last frame after it.

- REPEAT
Repeat – Loop the frames in the sequence.

- `PING_PONG`
Ping-Pong – Bounce through the frames, flipping direction each pass.

Type :

Literal['CLIP', 'EXTEND', 'REPEAT', '`PING_PONG`']

[Related references](INDEX.md).

# bpy.types.GreasePencil: onion_factor, onion_keyframe_type, onion_mode

onion_factor

Adjusts the fade opacity of the onion frames that are shown (in [0, 1], default 0.5)

Type :

float
onion_keyframe_type

Keyframe category used as a filter (default 'ALL' )

- ALL
All – Include all Keyframe types.

- KEYFRAME
Keyframe – Normal keyframe, e.g. for key poses.

- BREAKDOWN
Breakdown – A breakdown pose, e.g. for transitions between key poses.

- `MOVING_HOLD`
Moving Hold – A keyframe that is part of a moving hold.

- EXTREME
Extreme – An ‘extreme’ pose, or some other purpose as needed.

- JITTER
Jitter – A filler or baked keyframe for keying on ones, or some other purpose as needed.

- GENERATED
Generated – A key generated automatically by a tool, not manually created.

Type :

Literal[‘ALL’, ‘KEYFRAME’, ‘BREAKDOWN’, ‘`MOVING_HOLD`’, ‘EXTREME’, ‘JITTER’, ‘GENERATED’]
onion_mode

Which frames the onion display draws (default 'ABSOLUTE' )

- ABSOLUTE
Frames – Frames in absolute range of the scene frame.

- RELATIVE
Keyframes – Frames in relative range of the Grease Pencil keyframes.

- SELECTED
Selected – Only selected keyframes.

Type :

Literal[‘ABSOLUTE’, ‘RELATIVE’, ‘SELECTED’]

[Related references](INDEX.md).

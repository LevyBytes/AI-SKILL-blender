# bpy.types.NlaStrip: frame_end, frame_end_raw, frame_end_ui, frame_start, frame_start_raw, frame_start_ui

frame_end

(in [-inf, inf], default 0.0)

Type :

float
frame_end_raw

Like frame_end, but accepts any value at all, even ones that leave the strip in an invalid state (in [-inf, inf], default 0.0)

Type :

float
frame_end_ui

Where the NLA strip ends. Be aware that setting it also revises the strip’s repeat count or the end frame of its action; to alter the end frame on its own, reach for the “frame_end” property instead. (in [-inf, inf], default 0.0)

Type :

float
frame_start

(in [-inf, inf], default 0.0)

Type :

float
frame_start_raw

Like frame_start, but accepts any value at all, even ones that leave the strip in an invalid state (in [-inf, inf], default 0.0)

Type :

float
frame_start_ui

Where the NLA strip begins. Be aware that setting it also revises the strip’s end frame; to alter the start frame on its own, reach for the “frame_start” property instead. (in [-inf, inf], default 0.0)

Type :

float

[Related references](INDEX.md).

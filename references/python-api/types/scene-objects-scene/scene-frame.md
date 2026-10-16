# bpy.types.Scene: frame_current, frame_current_final, frame_end, frame_float, frame_preview_end, frame_preview_start, frame_start, frame_step, frame_subframe

frame_current

Current frame; from Python prefer frame_set() to refresh animation data instead (in [-1048574, 1048574], default 1)

Type :

int
frame_current_final

Current frame once subframe and time remapping are applied (in [-1.04857e+06, 1.04857e+06], default 0.0, readonly)

Type :

float
frame_end

Last frame of the playback/rendering range (in [0, 1048574], default 250)

Type :

int
frame_float

(in [-1.04857e+06, 1.04857e+06], default 0.0)

Type :

float
frame_preview_end

Alternative end frame used for UI playback (in [-inf, inf], default 0)

Type :

int
frame_preview_start

Alternative start frame used for UI playback (in [-inf, inf], default 0)

Type :

int
frame_start

First frame of the playback/rendering range (in [0, 1048574], default 1)

Type :

int
frame_step

How many frames to advance for each rendered or played-back frame (in [0, 1048574], default 1)

Type :

int
frame_subframe

(in [0, 1], default 0.0)

Type :

float

[Related references](INDEX.md).

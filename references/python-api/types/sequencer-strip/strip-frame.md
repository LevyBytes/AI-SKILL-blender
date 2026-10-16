# bpy.types.Strip: frame_duration, frame_final_duration, frame_final_end, frame_final_start, frame_offset_end, frame_offset_start, frame_start

frame_duration

How long this strip’s contents run before handles are taken into account (in [1, 1048574], default 0, readonly)

Deprecated since version 5.10: removal planned in version 6.0

Replaced by ‘.content_duration’.

Type :

int
frame_final_duration

How long this strip’s contents run once the handles have been applied (in [-inf, inf], default 0)

Deprecated since version 5.10: removal planned in version 6.0

Replaced by ‘.duration’.

Type :

int
frame_final_end

The end frame shown in the sequence editor after offsets take effect (in [-inf, inf], default 0)

Deprecated since version 5.10: removal planned in version 6.0

Replaced by ‘.right_handle’.

Type :

int
frame_final_start

The start frame shown in the sequence editor once offsets are applied; assigning here is the same as nudging the handle rather than the real start frame (in [-inf, inf], default 0)

Deprecated since version 5.10: removal planned in version 6.0

Replaced by ‘.left_handle’.

Type :

int
frame_offset_end

Offset from the end of the strip in frames (in [-inf, inf], default 0.0)

Deprecated since version 5.10: removal planned in version 6.0

Replaced by ‘.right_handle_offset’.

Type :

float
frame_offset_start

Offset from the start of the strip in frames (in [-inf, inf], default 0.0)

Deprecated since version 5.10: removal planned in version 6.0

Replaced by ‘.left_handle_offset’.

Type :

float
frame_start

X position where the strip begins (in [-inf, inf], default 0.0)

Deprecated since version 5.10: removal planned in version 6.0

Replaced by ‘.content_start’.

Type :

float

[Related references](INDEX.md).

# bpy.types.MovieClip: frame_duration, frame_offset, frame_start

frame_duration

Length of the movie clip in frames, as detected (in [-inf, inf], default 0, readonly)

Type :

int
frame_offset

Shift of the footage's first frame relative to its filename; this only changes how footage loads and leaves the clip's data untouched (in [-inf, inf], default 0)

Type :

int
frame_start

Scene frame on which this movie begins playback; this touches every piece of data tied to the clip (in [-inf, inf], default 1)

Type :

int

[Related references](INDEX.md).

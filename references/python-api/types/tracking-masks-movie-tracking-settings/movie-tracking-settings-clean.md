# bpy.types.MovieTrackingSettings: clean_action, clean_error, clean_frames

clean_action

Which cleanup action to run (default 'SELECT' )

- SELECT
Select – Select unclean tracks.

- `DELETE_TRACK`
Delete Track – Delete unclean tracks.

- `DELETE_SEGMENTS`
Delete Segments – Delete unclean segments of tracks.

Type :

Literal[‘SELECT’, ‘`DELETE_TRACK`’, ‘`DELETE_SEGMENTS`’]
clean_error

Applies to tracks whose re-projection error exceeds this value (in [0, inf], default 0.0)

Type :

float
clean_frames

Applies to tracks shorter than the given number of frames (in [0, inf], default 0)

Type :

int

[Related references](INDEX.md).

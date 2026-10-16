# bpy.types.MovieClipProxy: properties

build_100

Generate a proxy at the full 100% of the original footage resolution (default False)

Type :

bool
build_25

Generate a proxy at 25% of the original footage resolution (default True)

Type :

bool
build_50

Generate a proxy at 50% of the original footage resolution (default False)

Type :

bool
build_75

Generate a proxy at 75% of the original footage resolution (default False)

Type :

bool
build_record_run

Generate the record-run timecode index (default True)

Type :

bool
build_undistorted_100

Generate a proxy at the full 100% of the original undistorted footage resolution (default False)

Type :

bool
build_undistorted_25

Generate a proxy at 25% of the original undistorted footage resolution (default False)

Type :

bool
build_undistorted_50

Generate a proxy at 50% of the original undistorted footage resolution (default False)

Type :

bool
build_undistorted_75

Generate a proxy at 75% of the original undistorted footage resolution (default False)

Type :

bool
directory

Folder where the proxy files are kept (default “”, never None, blend relative // prefix supported)

Type :

str
quality

JPEG compression quality used for proxy images (in [0, 32767], default 50)

Type :

int
timecode

(default 'NONE' )

- NONE
None – Ignore generated timecodes, seek in movie stream based on calculated timestamp.

- `RECORD_RUN`
Record Run – Seek based on timestamps read from movie stream, giving the best match between scene and movie times.

- `FREE_RUN_NO_GAPS`
Record Run No Gaps – Effectively convert movie to an image sequence, ignoring incomplete or dropped frames, and changes in frame rate.

Type :

Literal[‘NONE’, ‘`RECORD_RUN`’, ‘`FREE_RUN_NO_GAPS`’]

[Related references](INDEX.md).

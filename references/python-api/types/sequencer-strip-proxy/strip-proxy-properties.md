# bpy.types.StripProxy: properties

build_100

Build 100% proxy resolution (default False)

Type :

bool
build_25

Build 25% proxy resolution (default False)

Type :

bool
build_50

Build 50% proxy resolution (default False)

Type :

bool
build_75

Build 75% proxy resolution (default False)

Type :

bool
build_record_run

Build record run time code index (default False)

Type :

bool
directory

Location to store the proxy files (default “”, never None, blend relative // prefix supported)

Type :

str
filepath

Location of custom proxy file (default “”, never None, blend relative // prefix supported)

Type :

str
quality

Quality of proxies to build (in [0, 32767], default 0)

Type :

int
timecode

Method for reading the inputs timecode (default 'NONE' )

- NONE
None – Ignore generated timecodes, seek in movie stream based on calculated timestamp.

- `RECORD_RUN`
Record Run – Use the movie stream’s own timestamps when seeking, so scene and movie times line up as closely as possible.

- `RECORD_RUN_NO_GAPS`
Record Run No Gaps – Treat the movie as an image sequence, disregarding dropped or incomplete frames along with frame-rate shifts.

Type :

Literal[‘NONE’, ‘`RECORD_RUN`’, ‘`RECORD_RUN_NO_GAPS`’]
use_overwrite

Overwrite existing proxy files when building (default True)

Type :

bool
use_proxy_custom_directory

Use a custom directory to store data (default False)

Type :

bool
use_proxy_custom_file

Use a custom file to read proxy data from (default False)

Type :

bool

[Related references](INDEX.md).

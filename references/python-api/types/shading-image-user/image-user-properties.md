# bpy.types.ImageUser: properties

## ImageUser(bpy_struct)

### ImageUser(bpy_struct)

base class — bpy_struct
class bpy.types. ImageUser ( bpy_struct )

Settings describing how one data-block draws on an Image data-block.
frame_current

The current frame within the image sequence or movie (in [-1048574, 1048574], default 0)

Type :

int
frame_duration

How many of a movie's images to use (in [0, 1048574], default 0)

Type :

int
frame_offset

Shift which frame number is used in the animation (in [-inf, inf], default 0)

Type :

int
frame_start

The movie/sequence's global start frame, taking the first picture as #1 (in [-1048574, 1048574], default 0)

Type :

int
multilayer_layer

The layer within a multilayer image (in [0, 32767], default 0, readonly)

Type :

int
multilayer_pass

The pass within a multilayer image (in [0, 32767], default 0, readonly)

Type :

int
multilayer_view

The view within a multilayer image (in [0, 32767], default 0, readonly)

Type :

int
tile

The tile within a tiled image (in [0, inf], default 0)

Type :

int
use_auto_refresh

Refresh the image every time the frame changes (default False)

Type :

bool
use_cyclic

Loop through the movie's images (default False)

Type :

bool

[Related references](INDEX.md).

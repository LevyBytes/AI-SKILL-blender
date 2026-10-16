# bpy.types.MotionPath: properties

## MotionPath(bpy_struct)

### MotionPath(bpy_struct)

base class — bpy_struct
class bpy.types. MotionPath ( bpy_struct )

Stored world-space locations of an element sampled across a span of frames
color

Personalized color used for the motion path on frames before the current one (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
color_post

Personalized color used for the motion path on frames after the current one (array of 3 items, in [0, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Color
frame_end

Last frame of the cached span (in [-inf, inf], default 0, readonly)

Type :

int
frame_start

First frame of the cached span (in [-inf, inf], default 0, readonly)

Type :

int
is_modified

Whether the path is currently being edited (default False)

Type :

bool
length

How many frames are held in the cache (in [-inf, inf], default 0, readonly)

Type :

int
line_thickness

Thickness of the drawn motion-path line (in [1, 6], default 0)

Type :

int
lines

Draw straight segments connecting keyframe points (default False)

Type :

bool
points

Per-frame positions held in the cache (default None, readonly)

Type :

bpy_prop_collection[MotionPathVert]
use_bone_head

On PoseBone paths, base the computation on the bone's head position (default False, readonly)

Type :

bool
use_custom_color

Apply a personalized color to this motion path (default False)

Type :

bool

[Related references](INDEX.md).

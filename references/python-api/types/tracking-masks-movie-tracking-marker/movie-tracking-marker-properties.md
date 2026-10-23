# bpy.types.MovieTrackingMarker: properties

## MovieTrackingMarker(bpy_struct)

### MovieTrackingMarker(bpy_struct)

base class: bpy_struct
class bpy.types. MovieTrackingMarker ( bpy_struct )

Marker data used during match-moving tracking
co

Where the marker sits on the frame, in normalized coordinates (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
frame

Frame on which the marker holds a keyframe (in [-inf, inf], default 0)

Type :

int
is_keyed

Whether the marker's position is keyframed rather than tracked (default True)

Type :

bool
mute

Whether the marker is muted on the current frame (default False)

Type :

bool
pattern_bound_box

Bounding box of the pattern area, in normalized coordinates (multi-dimensional array of 2 * 2 items, in [-inf, inf], default ((0.0, 0.0), (0.0, 0.0)), readonly)

Type :

bpy_prop_array[float]
pattern_corners

Coordinates of the pattern's corners, in normalized coordinates relative to the marker position (multi-dimensional array of 4 * 2 items, in [-inf, inf], default ((0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)))

Type :

bpy_prop_array[float]
search_max

Search-area top-right corner, in normalized coordinates relative to the marker position (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector
search_min

Search-area bottom-left corner, in normalized coordinates relative to the marker position (array of 2 items, in [-inf, inf], default (0.0, 0.0))

Type :

mathutils.Vector

[Related references](INDEX.md).

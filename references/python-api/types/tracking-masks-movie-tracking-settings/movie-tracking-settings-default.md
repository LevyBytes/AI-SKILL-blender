# bpy.types.MovieTrackingSettings: default_correlation_min, default_frames_limit, default_margin, default_motion_model, default_pattern_match, default_pattern_size, default_search_size, default_weight

default_correlation_min

Lowest correlation between the matched pattern and the reference that still counts as a successful track, by default (in [0, 1], default 0.0)

Type :

float
default_frames_limit

How many frames get tracked in each tracking cycle (in [0, 32767], default 0)

Type :

int
default_margin

Default border distance at which a marker stops tracking near the image edge (in [0, 300], default 0)

Type :

int
default_motion_model

Which motion model new tracks use by default (default 'Loc' )

- Perspective
Perspective – Search for markers that are perspectively deformed (homography) between frames.

- Affine
Affine – Search for markers that are affine-deformed (t, r, k, and skew) between frames.

- LocRotScale
Location, Rotation & Scale – Search for markers that are translated, rotated, and scaled between frames.

- LocScale
Location & Scale – Search for markers that are translated and scaled between frames.

- LocRot
Location & Rotation – Search for markers that are translated and rotated between frames.

- Loc
Location – Search for markers that are translated between frames.

Type :

Literal[‘Perspective’, ‘Affine’, ‘LocRotScale’, ‘LocScale’, ‘LocRot’, ‘Loc’]
default_pattern_match

Which reference frame the pattern is tracked from when advancing the marker to the next frame (default 'KEYFRAME' )

- KEYFRAME
Keyframe – Track pattern from keyframe to next frame.

- `PREV_FRAME`
Previous frame – Track pattern from current frame to next frame.

Type :

Literal[‘KEYFRAME’, ‘`PREV_FRAME`’]
default_pattern_size

Pattern-area size given to newly created tracks (in [5, 1000], default 0)

Type :

int
default_search_size

Search-area size given to newly created tracks (in [5, 1000], default 0)

Type :

int
default_weight

How much a newly created track contributes to the final solution (in [0, 1], default 0.0)

Type :

float

[Related references](INDEX.md).

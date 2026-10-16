# bpy.types.MovieTrackingTrack: motion_model

motion_model

Which motion model the track uses by default (default 'Loc' )

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

[Related references](INDEX.md).

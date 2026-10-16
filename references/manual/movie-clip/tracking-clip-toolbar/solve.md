# Solve

## Solve

Solve panel options.

Plane Track
See Create Plane Track documentation.

Solve

Tripod
Tripod Motion solves rotation-only footage (camera stationary). Generic solving cannot determine 3D feature positions (insufficient parallax), so this solver recovers relative rotation only, reprojecting features to a sphere (uniform camera-to-feature distance).

Note: Tripod solving behaves differently—more tracks don't guarantee accuracy. 5–10 tracks per frame suffice.

Keyframe
Automatically selects keyframe pairs. Complex algorithms find minimal reconstruction error and optimal scene scale.

Keyframe A/B
Reconstruction range start (A) and end (B).

Refine
Specifies camera-intrinsic parameters to refine during solving. Useful when uncertain; solver explores best values. Requires approximate initial values—completely wrong initial values prevent convergence.

Focal Length: Refines focal length.

Optical Center: Refines optical center.

Radial Distortion: Refines radial coefficients.

Tangential Distortion: Refines tangential coefficients.

Solve Camera/Object Motion
See Solve Camera/Object Motion documentation.

Cleanup

Operators and settings remove poor-quality tracks (insufficient length, high reconstruction error).

Frames
Removes tracks or segments shorter than this frame count.

Error
Removes tracks exceeding this error threshold.

Type
Action applied to flagged tracks.

Select: Highlights them.

Delete Track: Removes entirely.

Delete Segments: Removes bad segments.

Clean Tracks
See Clean Tracks documentation.

Filter Tracks
See Filter Tracks documentation.

[Related references](INDEX.md).

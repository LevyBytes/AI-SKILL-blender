# Track

Track panel—Track header sections.

Clip

Set Scene Frames: See Set Scene Frames documentation.

Prefetch: See Prefetch documentation.

Reload: See Reload Clip documentation.

Marker

Add: See Add Marker documentation.

Delete: See Delete Track documentation.

Detect Features: See Detect Features documentation.

Tracking Settings

The Tracking Settings panel governs 2D tracking parameters. Presets (panel header) provide starting values based on real footage, facilitating workflow.

Pattern Size, Search Size
Dimensions for newly created tracks.

Motion Model
Defines expected feature motion—select based on actual feature behavior for maximum accuracy.

Location, Location & Rotation, Location & Scale, Location, Rotation & Scale, Affine: Standard motion models.

Perspective: Planar feature tracking; Affine approximates well with more stability.

Match
Determines which pattern frame is tracked. Example: the tracker receives search-area images and a first-image feature position, then locates that feature in the second image.

Sequence tracking selects the second image from an unknown-position frame (next tracking target). The first image varies:

Keyframe: Pattern from a keyframed frame. Prevents position drift (original pattern return) but may jump and fail with feature deformation (perspective).

Previous Frame: Keyframes inserted per-frame; tracking occurs between keyframe and next image. Handles large transformations but drifts from original.

Prepass
Enables two-pass tracking: first pass = brute-force location only; second pass = full motion model refining.

Normalize
Normalizes patterns by average intensity, compensating illumination change (e.g., marker in shadow).

R, G, B
Color channels used by the algorithm. Disabling channels increases contrast for feature detection.

Copy from Active Track
Duplicates all settings from the active track, easing multi-track setup.

Tracking Extra Settings

Weight
See Track Weight documentation.

Correlation
Minimum pattern-to-reference correlation for successful tracking. Low values extend tracking (risky); high values stop early. Adjust for desired behavior.

Margin
Disables tracks too close to image boundary (pixel distance).

Use Mask
Applies annotation-tool mask to pattern, narrowing the match region.

Frames Limit
Maximum frames tracked per Track Sequence call, aiding early-notice of slide-off.

Speed
Marker-specific—controls sequence-tracking speed (quality unchanged, aids visibility). Tracking often exceeds real-time; Speed adds delay to catch drift.

Track

Track: See Track Motion documentation.

Clear: See Before documentation.

Refine: See Refine documentation.

Merge

Join Tracks: See Join Tracks documentation.

[Related references](INDEX.md).

# Track: Create Plane Track, Solve Camera/Object Motion

Create Plane Track
Reference
Mode: Tracking
Menu: Track ‣ Create Plane Track

Builds a plane track from coplanar point tracks; used for billboard/screen replacement in compositing.

The operator generates a plane object deforming identically to the plane defined by all selected point tracks.

Minimum requirement: four point tracks spanning the entire footage for the plane to be replaced. More tracks yield superior plane motion estimation.

Feature points need not be corners: they can lie anywhere on the plane. Corners are often occluded or difficult to track precisely. Positioning tracked features distant from the actual surface to be replaced supplies richer information about plane deformation; such markers track even when partially obscured.

Overlapping neighbor frames must share at least four common tracks.

The Plane Track Deform Node can project an image onto the solved plane.

Solve Camera/Object Motion
Reference
Mode: Tracking
Menu: Track ‣ Solve Camera/Object Motion

Computes camera or selected object motion using all tracks and two keyframes.

Requirements:

- At least eight tracks must appear in both keyframes.

- Parallax between keyframes must be significant.

Success reports average reprojection error (editor header)—mean distance from reconstructed 3D positions projected back to 2D footage versus original locations. Below 0.3 = accurate; 0.3–3.0 = acceptable; above 3.0 = tracking error or incorrect camera settings.

Join Tracks
Reference
Mode: Tracking
Menu: Track ‣ Join Tracks
Shortcut: Ctrl - J

Merges all selected tracks into one; selected tracks must not share markers on identical frames.

Average Tracks
Reference
Mode: Tracking
Menu: Track ‣ Average Tracks

Creates a new track by averaging data across selected tracks—useful for stabilizing blurry or low-contrast features. All marker properties are averaged; disabled markers are excluded.

Gaps between segments are linearly interpolated to suppress jumps. Interpolation applies only to interior gaps; tracks lacking markers at beginning or end frames will exhibit jumps in those regions.

Keep Original
When enabled, preserves selected tracks instead of removing them.

Copy Tracks
Referenced elsewhere.

Paste Tracks
Referenced elsewhere.

Animation
Referenced elsewhere.

Show/Hide
Referenced elsewhere.

[Related references](INDEX.md).

# Dope Sheet View

## Dope Sheet View

Dope Sheet View visualizes motion tracking data as a separate Movie Clip editor view (like Graph View).

Dope Sheet View displaying tracked segments.

The view shows channels for selected tracks. Dark bars represent tracked segments; small diamonds mark keyframed positions.

Frame background color indicates track count. Red = fewer than eight tracks (visual feedback, not a solve failure—just warrants attention). Yellow = eight to sixteen tracks. No guarantee that fewer tracks prevent accurate reconstruction; poor-feature tracks reduce accuracy more than sparse tracking.

Header

Channel sort-order controls.

Only Show Selected
Limits display to selected-track data.

Display Hidden
Includes hidden-track information.

Dopesheet Sort Field
Track ordering.

Name: Alphabetical.

Longest: By longest tracked segment.

Total: By total frame count.

Average Error: By average reprojection error post-solve.

Start Frame: By first frame.

End Frame: By last frame.

Invert
Reverses sort direction (ascending ↔ descending).

Usage

The Dope Sheet View is visualization-only; no editing tools exist.

[Related references](INDEX.md).

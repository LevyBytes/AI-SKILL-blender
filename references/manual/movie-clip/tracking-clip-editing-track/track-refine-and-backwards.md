# Track: Refine, Backwards

Refine

Reruns tracking from a prior keyframe forward (or backward), using existing mark positions as starting points. The algorithm then polishes the correspondence.

Useful when a tracked feature vanishes temporarily. After manually placing a mark where the feature reappears, Refine optimizes its position.

Direction (Refine Forwards or Backwards) matches your original tracking pass.

Backwards
Reference
Mode: Tracking
Menu: Track ‣ Refine ‣ Backwards

Refines backward.

Forwards
Reference
Mode: Tracking
Menu: Track ‣ Refine ‣ Forwards

Refines forward.

Add Marker
Reference
Mode: Tracking
Menu: Track ‣ Add Marker

Drops a marker under the cursor, movable before finalizing (LMB / Return / Spacebar confirms). Shortcut: Ctrl - LMB places the marker directly at the click point.

The track preview widget displays the pattern area live, letting you dial in position precision before committing.

Detect Features
Reference
Mode: Tracking
Menu: Track ‣ Detect Features

Identifies trackable points in the current frame and marks them. Detection is frame-local; moving objects and offscreen subjects are unmarked automatically.

Placement
How markers are distributed.

Whole Frame
Marks across the entire image.

Inside Annotated Area
Marks only within hand-drawn regions; narrows focus to areas of interest.

Outside Annotated Area
Marks exclude annotated zones; removes clutter (backgrounds, crowds).

Margin
Inset from image edges (pixels). Edge-adjacent markers fail quickly; increase this to reduce manual fixes.

Threshold
Minimum feature quality; low allows weak features (risky), high skips them. Balance to get desired count.

Distance
Spacing between marks. Prevents clustering, which degrades solver accuracy.

[Related references](INDEX.md).

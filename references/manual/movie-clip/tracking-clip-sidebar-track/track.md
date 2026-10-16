# Track

Track panel settings.

Track panel configuration.

Name
Editable field for track identifier. Used when linking to constraints (Follow Track, etc.).

Enable
Toggle marker status. Disabled markers don't contribute to solving or constraints.

/ Lock
Toggles lock state. Locked tracks resist accidental editing—useful for finalized tracks.

Track Preview Widget

The preview widget displays the pattern area, checking tracking accuracy (feature position consistency) and repositioning. Drag with mouse to move the track directly via widget.

When an anchor differs from the tracked position (setup for masking without good on-position features), preview shows the anchor area. Expand widget height using the highlighted area below (two horizontal lines).

Further Options

R, G, B
Tracking occurs in grayscale; high feature-to-background contrast improves accuracy. Disabling color channels increases contrast.

Grayscale Preview (B/W)
Displays preview as grayscale even with all channels enabled.

Alpha
Applies annotation-tool mask in the preview.

Weight
3D reconstruction assigns reduced weight to problematic tracks, controlling influence on solution. Animatable.

Animating weights corrects jumps as features vanish/degrade. Alternatively: after careful tracking/solving, lock all markers (Ctrl - L), set tracker weight to zero, and use feature detection for quick placement. These markers won't influence solution but provide scene reference.

Stabilization Weight
Used for 2D stabilization (separate from Weight for 3D reconstruction).

Custom Color Presets
Preset selector for custom color.

Custom Color
Overrides default marker color in Clip editor and 3D Viewport; distinguishes feature types (background vs. foreground). Enables track-group selection by color via Select Grouped.

Tip: Select optimal tracking points near timeline midpoint and track bidirectionally outward. This maximizes the chance of markers remaining in-frame.

[Related references](INDEX.md).

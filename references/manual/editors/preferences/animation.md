# Animation

## Animation

The Animation section manages animation-related settings, covering how editors look as well as a few tool properties.

Timeline:
Allow Negative Frame — lets playback and animation happen during negative frame ranges.
Minimum Grid Spacing — the fewest pixels allowed between grid lines.
Timecode Style — the format for timecodes when timing isn't shown in frames.
  Minimal Info — the most compact form, using "+" to separate sub-second frame numbers and truncating left and right as needed.
  SMPTE (Full) — full SMPTE timecode (HH:MM:SS:FF).
  SMPTE (Compact) — SMPTE showing minutes, seconds, and frames only, adding hours when needed but not by default.
  Compact with Decimals — like SMPTE (Compact) but showing the second's decimal part instead of frames.
  Only Seconds — a straight conversion of frame numbers to seconds.
Zoom to Frame Type — sets which time range around the cursor shows when View Frame (Numpad0) runs.
  Keep Range — keeps the currently displayed time range.
  Seconds — shows the number of seconds set in Zoom Seconds around the cursor.
  Keyframes — shows the number of keyframes set in Zoom Keyframes around the cursor.

Keyframes — these control Keyframes, the building blocks of animation.
Default Key Channels — which channels to key when no keying set is active: Location, Rotation, Scale, Rotation Mode, or Custom Properties.
Only Insert Needed — keys only when the property's value has actually changed. Manual skips keys that don't affect the animation when keying by hand; Auto does the same for Auto-Keying.
Keyframing – Visual Keying — when an object uses constraints its property value doesn't really change, so Visual Keying keys the property using the visual transformation the constraint produces.
Auto-Keyframing:
  Enable in New Scenes — turns Auto Keyframe on by default for new scenes.
  Show Warning — shows a warning at the 3D Viewport's top-right while moving objects if Auto Keyframe is on.
  Only Insert Available — keys only channels of F-Curves that already exist.
  See also Auto-Keyframing.

F-Curves — these control how F-Curves look and behave by default.
Unselected Opacity — how opaque unselected F-Curves are against the Graph Editor's background.
Default Smoothing Mode — the default behavior of automatic curve handles on new F-Curves.
Default Interpolation — the default Interpolation for new keyframes.
Default Handles — the default Handle for new F-Curves.
XYZ to RGB — colors X, Y, or Z animation curves (location, scale, rotation) to match the X, Y, and Z axis colors.
Channel Group Colors — draws groups and channels in colors matching their groups.
Only Show Selected F-Curve Keyframes — shows keyframe markers only on the selected curves.
F-Curve High Quality Drawing — draws F-Curves with anti-aliasing and other effects (turn off for better performance).

[Related references](INDEX.md).

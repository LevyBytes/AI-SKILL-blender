# Sidebar

## Sidebar

Action Panel — while the editor sits in Action Editor mode, or in Dope Sheet mode with a selected channel that belongs to an action, this panel lets you change some of that action's settings (see Action Properties).

Custom Properties — create and manage your own properties to stash data in the action's data block; see the Custom Properties page.

Edited Action — Reference: Panel: Sidebar ‣ Edited Action. Holds settings for the object's active action; visible only when the Action Track is selected.
Action — a data-block menu to view, change, and clear the active action (see also the Action Editor's Action).
Slot — which slot within the active action to use.
Extrapolation — decides whether the action influences the frames before/after its bounds once it's pushed down into a strip. (While it's still the active action, Hold applies regardless of the choice.)
  Hold — the values from the action's first keyframe extend back over the earlier frames (if the strip is first in the track), and the values from its last keyframe extend forward over the later ones (up to the next strip).
  Hold Forward — only the last keyframe's values carry to later frames (up to the next strip).
  Nothing — the animated properties revert to their defaults outside the strip's bounds.
Blending — how the action's values combine with those of the tracks below.
  Replace — overwrites the lower tracks' values; with Influence under 1, a linear interpolation between the old and new values is used instead.
  Multiply, Subtract, Add — combines the action's values with the lower tracks' by a simple calculation; with Influence under 1, a linear interpolation between the old values and the calculated ones is used.
  \(result = mix(previous, previous (+-×) value, influence)\)
  Combine — picks one of the following automatically per property type:
  Axis/Angle Rotation: \(result = previous + value × influence\) — which averages the axis while summing the rotation amounts.
  Quaternion Rotation — quaternion math runs on all four channels at once: \(result = {previous} × {value} ^ {influence}\)
  Proportional (Scale): \(result = previous × (value / default) ^ {influence}\)
  Others: \(result = previous + (value - default) × {influence}\)
  Note: since this mode relies on quaternion multiplication for the Quaternion Rotation properties, every one of the four channels is driven during playback, and Insert Single Keyframe must lay down all four keys; other channel types can still be keyed on their own.
Influence — the action's contribution to the NLA stack's overall result.

Strip:
Name — the strip's name.
Mute (checkbox) — unchecked, the strip stops contributing to the animation and shows a dotted outline.

Active Strip — Reference: Panel: Sidebar ‣ Strip ‣ Active Strip. Holds common strip properties.
Frame Start — the frame the strip begins on; changing it moves the strip while keeping its duration.
Frame End — the frame the strip ends on; changing it also changes the Action Clip Frame End, cropping or extending the action. To speed it up or slow it down instead, scale it via Strip ‣ Transform ‣ Scale or the Playback Scale setting.
Extrapolation — see Extrapolation.
Blending — see Blending.
Blend In, Out — how many frames the strip's influence takes to ramp up at the start and wind down at the end.
Auto Blend In/Out — computes Blend In/Out automatically from the strips in the track above or below that overlap this one in time.
Playback:
  Reversed — plays the strip backwards.
  Cyclic Strip Time — whether the Animated Strip Time loops back to the beginning once it runs past the Action Clip Frame End.
Animated Influence — lets you set, and animate, how strongly the strip affects the animation, an alternative to the (Auto) Blend In/Out settings. To set an influence keyframe, enter a value and then either pick Insert Keyframe from its context menu or hover over it and press I; the keyframes show in, e.g., the Graph Editor.
Animated Strip Time — lets you set, and animate, the frame at which the underlying action is sampled. Note: despite the name Strip Time, its value is a frame inside the action, not inside the strip — for an action spanning frames 1 to 50 referenced by a strip spanning 101 to 150, you'd put the Strip Time at 1, not 101, to land on the first keyframe. Combined with Cyclic Strip Time, this lets the action's keyframes play several times within one strip: if the action's keys lie between frames 1 and 50 and you animate the strip time to run 1 to 100 instead, they play twice (at double speed). In practice, though, the Repeat setting below is easier.

Action Clip — Reference: Panel: Sidebar region ‣ Strip ‣ Action Clip. Holds properties specific to Action strips.
Action — the action the strip references.
Slot — which slot within the action to use.
Frame Start, End — how much of the action to use; adjusting these crops or extends the action (and the strip, since its Frame End shifts accordingly), and extending it brings F-Curve Extrapolation into play. One handy case is cyclic animation where the action's first and last keyframes share a value (so the value lasts two frames on restart): lowering the Frame End drops the last keyframe so the value lasts only one frame.
Sync Length — on leaving Tweak Mode, automatically pins Frame Start/End to the action's first and last keyframe.
Now — snaps Frame Start/End to the action's first and last keyframe immediately.
Playback Scale — plays the animation faster (scale < 1) or slower (scale > 1) than the original action.
Repeat — plays the action several times.

Action — Reference: Panel: Sidebar region ‣ Strip ‣ Action. See Action Properties.

Modifiers — Reference: Panel: Sidebar region ‣ Modifiers. Strip modifiers let you make non-destructive changes to every curve inside the strip's action. See F-Curve Modifiers.

[Related references](INDEX.md).

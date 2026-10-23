# Editing Channels

## Editing Channels

Delete Channels - Reference: Menu: Channel ‣ Delete Channels; Shortcut: Delete, X. Strips the selected channels out of the current action. Warning: keep the pointer over the channel region before using the shortcuts; over the main region instead, you'll only delete the selected keyframes, not whole channels.

Un/Group Channels - Reference: Menu: Channel ‣ Un/Group Channels; Shortcut: Ctrl-Alt-G, Ctrl-G. Bundles the selected channels into a collection (renamable by double-clicking its name) or ungroups them; grouping keeps the view tidier.

Toggle/Enable/Disable Channel Settings - Reference: Menu: Channel ‣ Toggle/Enable/Disable Channel Settings; Shortcut: Shift-W, Shift-Ctrl-W, Alt-W. Flips, switches on, or switches off a given setting for the selected channels:
Protect: a protected channel (closed-padlock icon) can't be edited; rather than Shift-W then Toggle, you can just press Tab.
Mute: a muted channel (empty checkbox) has no effect on the animation.

Toggle Channel Editability - Reference: Menu: Channel ‣ Toggle Channel Editability; Shortcut: Tab. Locks or unlocks a channel for editing.

Extrapolation Mode - Reference: Menu: Channel ‣ Extrapolation Mode; Shortcut: Shift-E. Sets how the curve behaves before its first keyframe and after its last.
Constant: carries on as a flat line at the first/last keyframe's value; this is the default.
Linear: carries on as a straight line at the same slope as the first/last keyframe.
Make Cyclic: repeats the whole curve, done by adding a Cycles modifier.
Clear Cyclic: removes that modifier, so the curve stops repeating.

Add F-Curve Modifier - Reference: Menu: Channel ‣ Add F-Curve Modifier; Shortcut: Shift-Ctrl-M. Opens a submenu for adding a modifier to the active curve; the modifiers' settings live in Sidebar ‣ Modifiers.

Show/Hide:
Hide Selected Curves (H): hides the selected curves.
Hide Unselected (Shift-H): hides every curve but the selected ones.
Reveal Curves (Alt-H): brings back all previously hidden curves.

Expand/Collapse Channels - Reference: Menu: Channel ‣ Expand/Collapse Channels; Shortcut: NumpadPlus, NumpadMinus. Expands or collapses the selected headers.

Move - Reference: Menu: Channel ‣ Move…. Shuffles the selected channels or slots up and down the list: To the top (Shift-PageUp), Up one line (PageUp), Down one line (PageDown), To the bottom (Shift-PageDown).

Revive Disabled F-Curves - Reference: Menu: Channel ‣ Revive Disabled F-Curves. Clears the "disabled" tag from every F-Curve to get broken ones working again (a curve breaks when it points at a property that doesn't exist).

Keys to Samples — Reference: Menu: Channel ‣ Keys to Samples; Shortcut: Alt-C. Switches the selected curves from interpolating between keyframes to holding a sampled value at each whole frame. It's destructive — you lose the ability to edit the curve — and is used mainly to shrink file size on large datasets, since samples take less room than keyframes. On the subframes that fall between samples, interpolation runs linearly.

Samples to Keys - Reference: Menu: Channel ‣ Samples to Keys. Switches the selected curves from samples back to keyframes, making them editable; note this drops a keyframe on every frame.

Sound to Samples - Reference: Menu: Channel ‣ Sound to Samples. Builds a sampled curve out of a sound file (reach for Samples to Keys when it needs editing).
Lowest Frequency: the cutoff of a high-pass filter applied to the audio.
Highest Frequency: the cutoff of a low-pass filter applied to the audio.
Attack Time: a hull-curve value setting how fast the hull curve may rise; lower means steeper.
Release Time: a hull-curve value setting how fast the hull curve may fall; lower means steeper.
Threshold: the minimum amplitude needed to influence the hull curve.
Accumulate: sums just the upward jumps in the hull-curve amplitudes into the output.
Additive: the hull-curve amplitudes are summed; with Accumulate on, both positive and negative differences accumulate.
Square: outputs a square curve, negatives always becoming -1 and positives 1.
Square Threshold: anything below this threshold becomes 0.

Bake Channels - Reference: Menu: Channel ‣ Bake Channels. Generates fresh keyframes for the selected curves.
Frame Range: the range to bake; defaults to the scene or preview range.
Frame Step: the gap between keyframes; use it to key every 10 frames, or even every half frame.
Remove Outside Range: deletes existing keys outside the bake range.
Interpolation Type: the interpolation for the new keys.
Bake Modifiers: when on, the new keyframes reflect the modified curve and the modifiers are deleted; when off, they reflect the original curve and the modifiers stay applied.

Discontinuity (Euler) Filter - Reference: Menu: Channel ‣ Discontinuity (Euler) Filter. Cleans up Euler rotation channels plagued by Gimbal Lock; all three Euler axis channels must be selected for it to work.

Frame Selected Channels - Reference: Menu: Channel ‣ Frame Selected Channels; Shortcut: NumpadPeriod. Pans and zooms to show all keyframes of the selected curves; Alt-MMB on a channel does it too.

[Related references](INDEX.md).

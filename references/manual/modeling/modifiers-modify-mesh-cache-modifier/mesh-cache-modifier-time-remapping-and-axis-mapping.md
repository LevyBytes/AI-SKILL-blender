# Mesh Cache Modifier: Time Remapping, Axis Mapping

### Time Remapping

Time Mode
Sets how animation time gets read:

Frame :

Disregards the cache's timing data and runs the frames straight through.
This gives you direct say over playback speed.

Time :

Draws on the cache's own timing data, offsets and frame durations included.

Factor :

Fits the whole animation into a 0-to-1 range for fine control.

Play Mode
Sets how playback timing is worked out:

Scene :

Plays back against the scene's current frame.

Frame Start
Sets which frame playback begins on.

Frame Scale
Speeds up or slows down playback by scaling time.

Custom :

Allows manual control of animation timing.

Evaluation Value
Fixes where playback sits in the animation, and can be animated for fine control.

### Axis Mapping

Forward/Up Axis
Names the forward and up axes of the imported animation so it's oriented properly.

Flip Axis
Mirrors the animation across a chosen axis when the imported data needs correcting.

[Related references](INDEX.md).

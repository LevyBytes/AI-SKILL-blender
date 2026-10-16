# Speed Control Strip

## Speed Control Strip

### Speed Control Strip

Speed Control reshapes how quickly or slowly a strip plays.
Faster playback skips frames, running out before the stop point.
When frames expire, the last one holds (appears frozen). Place the next strip where you want action resuming.

### Options

Speed Control
How to modify play velocity.

Stretch :

Calculates speed from the strip's span.
Half-scale → double speed.

Multiply :

Multiplies playback pace by a Multiply Factor.
0.5 = half speed; 2.0 = double speed.
Negative = reverse while adjusting; negative 2 = reverse + double speed.

Note

You adjust strip length by hand.

Frame Number :

Picks which frame to show at the present moment.
E.g., Frame Number 50 displays frame 50.
Keyframe this to recreate animation effects.

Length :

Uses percentage mapping. 50% picks the halfway frame.

Interpolation
Blurs between frames to soften visual break when playback drops below source rate.

### Examples

### Creating a Slow-Motion Effect

Want slow playback?
Use Add ‣ Effect ‣ Speed Control on the clip.

In the Effect Strip panel, select Multiply.
Enter the speed ratio.
To cut speed in half, enter 0.5.
A 275-frame video plays at half speed, showing 137 frames.

To show the remaining frames in slow-mo, double the source span.
(Effects span from source spans.)
For other ratios, apply:

new_length = real_length / speed_factor

Render all frames (here: 550).

### Keyframing the Speed Control

Keyframing the Frame number.

For finer control, animate!
Keyframing Frame Number directly is typical.
Keyframes are needed for any speed change; otherwise it looks frozen. Graph editor usually wants Linear interpolation (Bézier is rarely wanted).

Tip

Keyframing the Multiply factor also works but remember to Refresh All to apply.

### Changing Video Frame Rates

Remap frame rates using speed.
Rendering as image sequences lets you adjust output image count.
Use Multiply above or below one.

A 30 fps 5-minute video going to 24 fps film uses 30/24 = 1.25.
Instead of 5 × 60 × 30 = 9000 frames, you get 9000 / 1.25 = 7200 = 5 × 60 × 24 frames.
Set start = 1, end = 7200, Format = jpeg 30fps output.
Write 0001.jpg to 7200.jpg, covering the whole 9000.
Image 7200.jpg matches frame 9000.
Reading at 24 fps lasts exactly 5 minutes.

[Related references](INDEX.md).

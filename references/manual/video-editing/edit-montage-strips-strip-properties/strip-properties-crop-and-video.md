# Strip Properties: Crop, Video, Color, Sound

### Crop

Reference

Panel: Sidebar ‣ Strip ‣ Crop

Trims the source image edges. Control trimming with Top, Left, Bottom, and Right parameters.

### Video

Reference

Panel: Sidebar ‣ Strip ‣ Video

Strobe
Render every nth frame. Setting this to 10 shows only frames 1, 11, 21, 31, 41…. This is a float value, allowing beat-synchronized effects.

Reverse Frames
Plays the strip backwards from the final frame.

### Color

Reference

Panel: Sidebar ‣ Strip ‣ Color

Saturation
Modifies color intensity.

Multiply
Scales all color channels by this amount, raising brightness.

Multiply Alpha
When using Multiply, also scale the alpha channel.

Convert to Float
Changes input to floating-point format.

### Sound

Reference

Panel: Sidebar ‣ Strip ‣ Sound

Audio handling is covered in Sound Strip.

Volume
Governs loudness level.

Animated volume displays as an overlay: a dark section following the animation curve. Hide via F-Curves disable. The waveform shows the updated level.

Offset
Audio playback delay from the strip start, in seconds.

Mono
Collapse all channels to a single channel.

Pan
Positions audio across speakers in multi-channel systems. Only mono sources pan; enable Mono to convert non-mono files. The value represents the angle (multiply by 90 degrees).

For stereo: left (-1) to center (0) to right (1). Higher values address rear speakers: -2 is back-left, 2 is back-right.

Tip

Apply values beyond soft bounds for smooth animation, as angle wraps across rotations.

Note

Audio channel count is configurable in Audio Output settings.

Preserve Pitch
When active, holds the original pitch despite strip speed changes. When off, speed adjustments alter pitch (slower = lower pitch, faster = higher pitch). Useful for syncing audio to edited timing without affecting tone or musical key.

Display Waveform
Displays a visual representation of the audio waveform within the Sound strip. Animation keyframes and volume settings influence the waveform appearance. Red indicates clipped audio (above 100% amplitude). Visibility depends on setting the Waveforms overlay option to Per-Strip mode.

[Related references](INDEX.md).

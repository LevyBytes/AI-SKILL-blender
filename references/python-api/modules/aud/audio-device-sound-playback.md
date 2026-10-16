# aud device and sound playback

### Audio System (aud)

Audaspace (pronounced "outer space") is a high-level audio processing library.

### Basic Sound Playback

This example demonstrates Device, Sound, and Handle usage.

```python
import aud

device = aud.Device()
# Load sound file (works with video containing audio).
sound = aud.Sound('music.ogg')

# Play audio; returns a handle for controlling playback.
handle = device.play(sound)
# For recurring sounds, buffering reduces processing.
sound_buffered = aud.Sound.cache(sound)
handle_buffered = device.play(sound_buffered)

# Stop playback (otherwise audio runs to completion).
handle.stop()
handle_buffered.stop()
```

[Related references](INDEX.md).

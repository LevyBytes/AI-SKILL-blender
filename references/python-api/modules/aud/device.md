# aud.Device

class aud.Device

Device objects represent audio output backends (OpenAL, SDL) and also file or memory output.
lock()

Locks the device, stopping sample reading from streams until unlock() is invoked. Useful for synchronizing sound start/stop/pause/resume operations.

Note

Unlock must match each lock call for playback to continue.

Warning

Keep the lock duration brief to avoid audio dropouts.
play(sound, keep=False)

Initiates sound playback.

Parameters:

- sound (Sound) – The sound to begin.

- keep (bool) – See Handle.keep.

Returns:

The playback handle for controlling playback.

Return type:

Handle
stopAll()

Halts all playing and paused sounds.
unlock()

Unlocks after lock(), see lock() details.
channels

The audio channel count of the device.
distance_model

The device's distance model.

See also

OpenAL Documentation
doppler_factor

The doppler scale factor. A value over 1 exaggerates the effect by increasing velocity scaling.
format

The device's native sample format.
listener_location

The listener's position in 3D, a 3D float tuple.
listener_orientation

The listener's orientation in 3D as quaternion, a 4-float tuple.
listener_velocity

The listener's velocity in 3D, a 3D float tuple.
rate

The device's sampling frequency in Hz.
speed_of_sound

The device's speed-of-sound value. Standard air speed is around 343.3 m/s.
volume

The device's overall audio level.
### Audio System (aud) continued: Device properties and DynamicMusic class

[Related references](INDEX.md).

# aud.Sequence

class aud.Sequence

This sound type handles sequenced playback of multiple sounds.
add()

Adds an entry to the sequence.

Parameters:

- sound (Sound) – The sound this entry plays.

- begin (double) – The entry start time.

- end (double) – The entry end time or negative if determined by the sound.

- skip (double) – Seconds to skip from the beginning.

Returns:

The entry added.

Return type:

SequenceEntry
remove()

Removes an entry from the sequence.

Parameters:

entry (SequenceEntry) – The entry to remove.
setAnimationData()

Writes animation metadata to the sequence.

Parameters:

- type (int) – The animation data category.

- frame (int) – The frame for this data.

- data (sequence of float) – The values to write.

- animated (bool) – Whether the property is animated.
channels

The sequence's audio channel count.
distance_model

The sequence's distance model.

See also

OpenAL Documentation
doppler_factor

The doppler scale factor. A value over 1 exaggerates the effect.
fps

The listener's position in 3D, a 3D float tuple.
muted

Whether the entire sequence is silenced.
rate

The sequence's sampling frequency in Hz.
speed_of_sound

The sequence's speed-of-sound value. Standard air is around 343.3 m/s.

[Related references](INDEX.md).

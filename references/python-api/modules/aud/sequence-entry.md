# aud.SequenceEntry

class aud.SequenceEntry

SequenceEntry represents a sound within a sequence.
move()

Relocates an entry.

Parameters:

- begin (double) – The new start time.

- end (double) – The new end time or negative if undetermined.

- skip (double) – Seconds to skip from the start.
setAnimationData()

Writes animation metadata to a sequence entry.

Parameters:

- type (int) – The animation data category.

- frame (int) – The frame for this data.

- data (sequence of float) – The values to write.

- animated (bool) – Whether the property is animated.
attenuation

Distance-based volume reduction factor.

See also

Device.distance_model
cone_angle_inner

Inner cone opening angle. If cone values are set, two audible cones exist with apex at source location, heading toward source orientation. Inside the inner cone, volume is standard. Outside the outer cone, volume becomes cone_volume_outer; between them, volume interpolates linearly.
cone_angle_outer

Outer cone opening angle.

See also

cone_angle_inner
cone_volume_outer

Volume beyond the outer cone.

See also

cone_angle_inner
distance_maximum

Maximum listener distance from the source. Beyond this, volume is zero.

See also

Device.distance_model
distance_reference

Reference distance where volume equals the volume property.

See also

Device.distance_model
muted

Whether the entry is silenced.
relative

Whether source position, velocity, and orientation are relative or absolute to the listener.
sound

The sound the entry plays in the sequence.
volume_maximum

Maximum entry volume.

See also

Device.distance_model
volume_minimum

Minimum entry volume.

See also

Device.distance_model

[Related references](INDEX.md).

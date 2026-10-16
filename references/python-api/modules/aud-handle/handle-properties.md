# aud.Handle: properties

attenuation

Distance-based volume reduction scaling.

See also

Device.distance_model
cone_angle_inner

Inner cone opening angle. If cone values exist, two audible cones originate at the source location, pointing in the source direction. Within the inner cone, volume is unaffected. Outside the outer cone, volume reaches cone_volume_outer; between them, volume interpolates linearly.
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

Reference distance for volume calculation. At this distance, volume equals the volume property.

See also

Device.distance_model
keep

Whether a sound pauses at the end rather than stopping, enabling later resume. Useful for seeking and restarting.

Warning

Set to true and forgotten = memory leak, as the handle persists until device destruction.
location

Source position in 3D, a 3D float tuple.
loop_count

Remaining loop cycles. Negative means infinite.
orientation

Source orientation in 3D as quaternion, a 4-float tuple.
pitch

Audio tone scale.
position

Playback position in seconds.
relative

Whether source position, velocity, and orientation are relative or absolute to the listener.
status

Playback state: playing, paused, or stopped (invalid).
velocity

Source velocity in 3D, a 3D float tuple.

volume

Audio loudness.
volume_maximum

Maximum source volume.

See also

Device.distance_model
volume_minimum

Minimum source volume.

See also

Device.distance_model

[Related references](INDEX.md).

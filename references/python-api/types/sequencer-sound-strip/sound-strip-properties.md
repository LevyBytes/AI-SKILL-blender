# bpy.types.SoundStrip: properties

## SoundStrip(Strip)

### SoundStrip(Strip)

base classes: bpy_struct, Strip
class bpy.types. SoundStrip ( Strip )

A sequencer strip that schedules a sound to play across a span of time
animation_offset_end

Animation end offset (trim end) (in [0, inf], default 0)

Deprecated since version 5.10: removal planned in version 6.0

Replaced by ‘.content_trim_end’.

Type :

int
animation_offset_start

Animation start offset (trim start) (in [0, inf], default 0)

Deprecated since version 5.10: removal planned in version 6.0

Replaced by ‘.content_trim_start’.

Type :

int
content_trim_end

How many frames to skip at the tail of the underlying source. Trimming the source turns later frames into holds (in [0, inf], default 0)

Type :

int
content_trim_start

How many frames to skip at the head of the underlying source. Trimming the source turns earlier frames into holds (in [0, inf], default 0)

Type :

int
pan

Panning applied to the sound during playback (Mono sources only) (in [-inf, inf], default 0.0)

Type :

float
pitch_correction

Hold the audio's original pitch even as playback speed changes (default False)

Type :

bool
retiming_keys

(default None, readonly)

Type :

RetimingKeys[RetimingKey]
show_waveform

Draw the audio waveform within the strip (default False)

Type :

bool
sound

The Sound data-block this strip draws from

Type :

Sound
sound_offset

Subframe shift of where the sound source begins, measured in seconds (in [-inf, inf], default 0.0)

Type :

float
volume

Volume at which the sound plays back (in [0, 100], default 1.0)

Type :

float

[Related references](INDEX.md).

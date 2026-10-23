# bpy.types.Sound: properties

## Sound(ID)

### Sound(ID)

base classes: bpy_struct, ID
class bpy.types. Sound ( ID )

A data-block that points at an external or packed sound file
channels

How the audio channels are laid out (default 'INVALID' , readonly)

- INVALID
Invalid – Invalid.

- MONO
Mono – Mono.

- STEREO
Stereo – Stereo.

- `STEREO_LFE`
Stereo LFE – Stereo FX.

- `CHANNELS_4`
4 Channels – 4 Channels.

- `CHANNELS_5`
5 Channels – 5 Channels.

- `SURROUND_51`
5.1 Surround – 5.1 Surround.

- `SURROUND_61`
6.1 Surround – 6.1 Surround.

- `SURROUND_71`
7.1 Surround – 7.1 Surround.

Type :

Literal[‘INVALID’, ‘MONO’, ‘STEREO’, ‘`STEREO_LFE`’, ‘`CHANNELS_4`’, ‘`CHANNELS_5`’, ‘`SURROUND_51`’, ‘`SURROUND_61`’, ‘`SURROUND_71`’]
filepath

The audio sample file backing this Sound data-block (default “”, never None, blend relative // prefix supported)

Type :

str
packed_file

(readonly)

Type :

PackedFile
samplerate

Audio sample rate, given in Hz (in [-inf, inf], default 0, readonly)

Type :

int
use_memory_cache

Decode the sound file and hold it in RAM (default False)

Type :

bool
use_mono

When several audio channels are present, mix them down to one (default False)

Type :

bool
factory

This sound's aud.Factory object.

(readonly)

[Related references](INDEX.md).

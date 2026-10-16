# bpy.types.FFmpegSettings: audio_bitrate, audio_channels, audio_codec, audio_mixrate, audio_volume

audio_bitrate

Bitrate of the audio in kb/s (in [32, 2048], default 192)

Type :

int
audio_channels

Number of audio channels (default 'STEREO' )

- MONO
Mono – Output a single audio channel.

- STEREO
Stereo – Output two audio channels.

- SURROUND4
4 Channels – Output four audio channels.

- SURROUND51
5.1 Surround – Output 5.1 surround-sound channels.

- SURROUND71
7.1 Surround – Output 7.1 surround-sound channels.

Type :

Literal[‘MONO’, ‘STEREO’, ‘SURROUND4’, ‘SURROUND51’, ‘SURROUND71’]
audio_codec

Which FFmpeg audio codec is used (default 'NONE' )

- NONE
No Audio – Turn off audio, for renders that contain video alone.

- AAC
AAC.

- AC3
AC3.

- FLAC
FLAC.

- MP2
MP2.

- MP3
MP3.

- OPUS
Opus.

- PCM
PCM.

- VORBIS
Vorbis.

Type :

Literal[‘NONE’, ‘AAC’, ‘AC3’, ‘FLAC’, ‘MP2’, ‘MP3’, ‘OPUS’, ‘PCM’, ‘VORBIS’]
audio_mixrate

Sample rate of the audio in samples/s (in [8000, 192000], default 48000)

Type :

int
audio_volume

Loudness of the audio (in [0, 1], default 1.0)

Type :

float

[Related references](INDEX.md).

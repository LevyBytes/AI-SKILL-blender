# bpy.ops.sound.mixdown: sound.mixdown channels, sample format, rate, bitrate and result

bpy.ops.sound. mixdown ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = True , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , display_type = 'DEFAULT' , sort_method = '' , accuracy = 1024 , container = 'FLAC' , codec = 'FLAC' , channels = 'STEREO' , format = 'S16' , mixrate = 48000 , bitrate = 192 , split_channels = False )

- channels ( Literal [ 'MONO' , 'STEREO' , '`STEREO_LFE`' , 'SURROUND4' , 'SURROUND5' , 'SURROUND51' , 'SURROUND61' , 'SURROUND71' ] ) – Channels, Audio channel count (optional)

- MONO
Mono – Single audio channel.

- STEREO
Stereo – Stereo audio channels.

- `STEREO_LFE`
Stereo LFE – Stereo with LFE channel.

- SURROUND4
4 Channels – 4 channel surround sound.

- SURROUND5
5 Channels – 5 channel surround sound.

- SURROUND51
5.1 Surround – 5.1 surround sound.

- SURROUND61
6.1 Surround – 6.1 surround sound.

- SURROUND71
7.1 Surround – 7.1 surround sound.

- format ( Literal [ 'U8' , 'S16' , 'S24' , 'S32' , 'F32' , 'F64' ] ) – Format, Sample format (optional)

- U8
U8 – 8-bit unsigned.

- S16
S16 – 16-bit signed.

- S24
S24 – 24-bit signed.

- S32
S32 – 32-bit signed.

- F32
F32 – 32-bit floating-point.

- F64
F64 – 64-bit floating-point.

- mixrate ( int ) – Sample Rate, Sample rate in samples/s (in [8000, 192000], optional)

- bitrate ( int ) – Bitrate, Bitrate in kbit/s (in [32, 512], optional)

- split_channels ( bool ) – Split channels, Each channel will be rendered into a mono file (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).

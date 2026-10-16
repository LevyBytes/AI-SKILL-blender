# bpy.ops.sound.mixdown: sound.mixdown accuracy, containers and codecs

bpy.ops.sound. mixdown ( * , filepath = '' , check_existing = True , filter_blender = False , filter_backup = False , filter_image = False , filter_movie = False , filter_python = False , filter_font = False , filter_sound = True , filter_text = False , filter_archive = False , filter_btx = False , filter_alembic = False , filter_usd = False , filter_obj = False , filter_volume = False , filter_folder = True , filter_blenlib = False , filemode = 9 , relative_path = True , display_type = 'DEFAULT' , sort_method = '' , accuracy = 1024 , container = 'FLAC' , codec = 'FLAC' , channels = 'STEREO' , format = 'S16' , mixrate = 48000 , bitrate = 192 , split_channels = False )

- accuracy ( int ) – Accuracy, Sample accuracy, important for animation data (the lower the value, the more accurate) (in [1, inf], optional)

- container ( Literal [ 'AAC' , 'AC3' , 'FLAC' , 'MATROSKA' , 'MP2' , 'MP3' , 'OGG' , 'WAV' ] ) – Container, File format (optional)

- AAC
AAC – Advanced Audio Coding.

- AC3
AC3 – Dolby Digital ATRAC 3.

- FLAC
FLAC – Free Lossless Audio Codec.

- MATROSKA
MKV – Matroska.

- MP2
MP2 – MPEG-1 Audio Layer II.

- MP3
MP3 – MPEG-2 Audio Layer III.

- OGG
OGG – Xiph.Org Ogg Container.

- WAV
WAV – Waveform Audio File Format.

- codec ( Literal [ 'AAC' , 'AC3' , 'FLAC' , 'MP2' , 'MP3' , 'PCM' , 'VORBIS' ] ) – Codec, Audio Codec (optional)

- AAC
AAC – Advanced Audio Coding.

- AC3
AC3 – Dolby Digital ATRAC 3.

- FLAC
FLAC – Free Lossless Audio Codec.

- MP2
MP2 – MPEG-1 Audio Layer II.

- MP3
MP3 – MPEG-2 Audio Layer III.

- PCM
PCM – Pulse Code Modulation (RAW).

- VORBIS
Vorbis – Xiph.Org Vorbis Codec.

[Related references](INDEX.md).

# bpy.types.FFmpegSettings: ffmpeg_preset, ffmpeg_prores_profile

ffmpeg_preset

Balance between how fast it encodes and how well it compresses (default 'GOOD' )

- BEST
Slowest – Best pick when you have plenty of time and want top compression efficiency.

- GOOD
Good – The default, suited to most uses.

- REALTIME
Realtime – Best pick when encoding speed matters most.

Type :

Literal[‘BEST’, ‘GOOD’, ‘REALTIME’]
ffmpeg_prores_profile

ProRes Profile (default '422_STD' )

Type :

Literal[‘422_PROXY’, ‘422_LT’, ‘422_STD’, ‘422_HQ’, ‘4444’, ‘4444_XQ’]

[Related references](INDEX.md).

# bpy.types.Scene: sync_mode

sync_mode

How playback stays in sync (default '`AUDIO_SYNC`' )

- NONE
Play Every Frame – Skip syncing and play every frame.

- `FRAME_DROP`
Frame Dropping – Drop frames when playback falls behind.

- `AUDIO_SYNC`
Sync to Audio – Lock to audio playback, dropping frames as needed.

Type :

Literal[‘NONE’, ‘`FRAME_DROP`’, ‘`AUDIO_SYNC`’]

[Related references](INDEX.md).

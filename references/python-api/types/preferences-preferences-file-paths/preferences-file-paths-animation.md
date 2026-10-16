# bpy.types.PreferencesFilePaths: animation_player, animation_player_preset

animation_player

Path to a custom player for animations or frame sequences (default “”, never None)

Type :

str
animation_player_preset

Ready-made setups for outside animation players (default 'INTERNAL' )

- INTERNAL
Internal – Blender's own animation player.

- DJV
DJV – An open-source frame player.

- FRAMECYCLER
FrameCycler – IRIDAS's frame player.

- RV
RV – Tweak Software's frame player.

- MPLAYER
MPlayer – Plays video plus PNG/JPEG/SGI image sequences.

- CUSTOM
Custom – Path to your own animation player executable.

Type :

Literal[‘INTERNAL’, ‘DJV’, ‘FRAMECYCLER’, ‘RV’, ‘MPLAYER’, ‘CUSTOM’]

[Related references](INDEX.md).

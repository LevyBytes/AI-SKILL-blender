# bpy.types.NlaStrip: type

type

Which kind of NLA Strip this is (default 'CLIP' , readonly)

- CLIP
Action Clip – NLA Strip references some Action.

- TRANSITION
Transition – NLA Strip ‘transitions’ between adjacent strips.

- META
Meta – NLA Strip acts as a container for adjacent strips.

- SOUND
Sound Clip – NLA Strip representing a sound event for speakers.

Type :

Literal[‘CLIP’, ‘TRANSITION’, ‘META’, ‘SOUND’]

[Related references](INDEX.md).

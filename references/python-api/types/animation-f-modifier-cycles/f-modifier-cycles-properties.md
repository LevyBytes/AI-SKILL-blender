# bpy.types.FModifierCycles: properties

## FModifierCycles(FModifier)

### FModifierCycles(FModifier)

base classes — bpy_struct, FModifier
class bpy.types. FModifierCycles ( FModifier )

Loops the values from the F-Curve it modifies.
cycles_after

Cap on how many cycles may run past the final keyframe, where 0 means unlimited (in [-32768, 32767], default 0)

Type :

int
cycles_before

Cap on how many cycles may run ahead of the first keyframe, where 0 means unlimited (in [-32768, 32767], default 0)

Type :

int
mode_after

Which cycling mode applies past the last keyframe (default 'NONE' )

- NONE
No Cycles – Don’t do anything.

- REPEAT
Repeat Motion – Repeat keyframe range as-is.

- `REPEAT_OFFSET`
Repeat with Offset – Repeat keyframe range, but with offset based on gradient between start and end values.

- MIRROR
Repeat Mirrored – Alternate between forward and reverse playback of keyframe range.

Type :

Literal[‘NONE’, ‘REPEAT’, ‘`REPEAT_OFFSET`’, ‘MIRROR’]
mode_before

Which cycling mode applies ahead of the first keyframe (default 'NONE' )

- NONE
No Cycles – Don’t do anything.

- REPEAT
Repeat Motion – Repeat keyframe range as-is.

- `REPEAT_OFFSET`
Repeat with Offset – Repeat keyframe range, but with offset based on gradient between start and end values.

- MIRROR
Repeat Mirrored – Alternate between forward and reverse playback of keyframe range.

Type :

Literal[‘NONE’, ‘REPEAT’, ‘`REPEAT_OFFSET`’, ‘MIRROR’]

[Related references](INDEX.md).

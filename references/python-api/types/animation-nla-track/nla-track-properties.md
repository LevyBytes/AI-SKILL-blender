# bpy.types.NlaTrack: properties

## NlaTrack(bpy_struct)

### NlaTrack(bpy_struct)

base class: bpy_struct
class bpy.types. NlaTrack ( bpy_struct )

One animation layer that holds Actions pointed at as NLA strips.
active

Whether this NLA Track is the active one (default False, readonly)

Type :

bool
is_override_data

For local override data, indicates whether this NLA track originates from the linked reference or is local to the override (default True, readonly)

Type :

bool
is_solo

Evaluate just this NLA Track on its own (the active Action together with every other NLA Track in the same AnimData block are turned off) (default False)

Type :

bool
lock

Whether this NLA Track is locked (default False)

Type :

bool
mute

Turn off evaluation of this NLA Track (default False)

Type :

bool
name

(default “”, never None)

Type :

str
select

Whether this NLA Track is selected (default False)

Type :

bool
strips

The NLA Strips sitting on this NLA-track (default None, readonly)

Type :

NlaStrips[NlaStrip]

[Related references](INDEX.md).

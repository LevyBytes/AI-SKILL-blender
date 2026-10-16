# bpy.types.ID: rename

rename ( name , * , mode = 'NEVER' )

Renames with smarter behaviour for the case where the chosen name clashes with another ID.

Parameters :

- name ( str ) – New name to rename the ID to, if empty will re-use the current ID name (never None)

- mode ( Literal [ 'NEVER' , 'ALWAYS' , '`SAME_ROOT`' ] ) – How to handle name collision, in case the requested new name is already used by another ID of the same type (optional)

- NEVER
Never Rename – Leave any conflicting ID untouched; instead a numeric suffix is tacked onto the ID being renamed.

- ALWAYS
Always Rename – Rename whichever existing ID conflicts so that the ID being renamed gets exactly the name asked for.

- `SAME_ROOT`
Rename If Same Root – Only displace a conflicting ID when its name root (the part before the numeric suffix) matches the current name of the ID being renamed.

Returns :

The outcome of the rename attempt

- UNCHANGED
Unchanged – No rename happened, for instance because the ID already carries the requested name.

- `UNCHANGED_COLLISION`
Unchanged Due to Collision – No rename happened: the request would have clashed with another ID, and the auto-adjusted name matched the current name anyway.

- `RENAMED_NO_COLLISION`
Renamed Without Collision – The requested name was applied and no collision arose.

- `RENAMED_COLLISION_ADJUSTED`
Renamed With Collision – The name was applied after being tweaked to sidestep a collision.

- `RENAMED_COLLISION_FORCED`
Renamed Enforced With Collision – The requested name was forced through, with another ID renamed to make room.

Return type :

Literal['UNCHANGED', '`UNCHANGED_COLLISION`', '`RENAMED_NO_COLLISION`', '`RENAMED_COLLISION_ADJUSTED`', '`RENAMED_COLLISION_FORCED`']

[Related references](INDEX.md).
